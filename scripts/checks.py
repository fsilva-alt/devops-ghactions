"""Verifica requisitos didáticos do YAML, sem executar comandos do aluno."""

import copy
import re
import sys
from pathlib import Path

import yaml


class WorkflowLoader(yaml.SafeLoader):
    # YAML 1.1 interpreta `on` como booleano. Actions usa essa chave como texto.
    yaml_implicit_resolvers = copy.deepcopy(yaml.SafeLoader.yaml_implicit_resolvers)


for letra, resolvers in WorkflowLoader.yaml_implicit_resolvers.items():
    WorkflowLoader.yaml_implicit_resolvers[letra] = [
        (tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:bool"
    ]
WorkflowLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool", re.compile(r"^(?:true|false)$", re.I), list("tTfF")
)


def mapping_unico(loader, node, deep=False):
    resultado = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValueError("As chaves do workflow devem ser texto.")
        if key in resultado:
            raise ValueError(f"Chave duplicada: {key} (linha {key_node.start_mark.line + 1}).")
        resultado[key] = loader.construct_object(value_node, deep=deep)
    return resultado


WorkflowLoader.add_constructor("tag:yaml.org,2002:map", mapping_unico)


def mapa(valor):
    return valor if isinstance(valor, dict) else {}


def lista(valor):
    return valor if isinstance(valor, list) else [valor] if valor is not None else []


def expressao(valor):
    return re.sub(r"\s+", "", str(valor))


class Verificador:
    def __init__(self, workflow):
        self.w = workflow
        self.jobs = mapa(workflow.get("jobs"))
        self.falhas = []

    def exigir(self, condicao, dica):
        if not condicao:
            self.falhas.append(dica)

    def steps(self, job):
        return [mapa(s) for s in lista(mapa(self.jobs.get(job)).get("steps"))]

    def action(self, job, nome):
        return next((s for s in self.steps(job) if str(s.get("uses", "")).startswith(nome + "@")), {})

    def comandos(self, job):
        return "\n".join(str(s.get("run", "")) for s in self.steps(job))

    def evento(self, evento):
        eventos = self.w.get("on", {})
        return evento in (eventos if isinstance(eventos, (dict, list)) else [eventos])

    def base(self):
        self.exigir(bool(self.w.get("name")), "Dê um name ao workflow.")
        self.exigir(bool(self.w.get("on")), "Defina os eventos em on.")
        self.exigir(bool(self.jobs), "Crie jobs com runs-on e steps.")
        self.exigir(mapa(self.w.get("permissions")).get("contents") == "read",
                    "Use permissions: contents: read no nível do workflow.")
        for nome, valor in self.jobs.items():
            job = mapa(valor)
            self.exigir(job.get("runs-on") == "ubuntu-latest", f"{nome}: use runs-on: ubuntu-latest.")
            self.exigir(isinstance(job.get("steps"), list) and bool(self.steps(nome)), f"{nome}: steps deve ser uma lista de etapas.")
            for step in self.steps(nome):
                self.exigir(bool(step.get("uses")) != bool(step.get("run")),
                            f"{nome}: cada etapa deve ter uses ou run, apenas um deles.")
            for dependencia in lista(job.get("needs")):
                self.exigir(isinstance(dependencia, str) and dependencia in self.jobs and dependencia != nome,
                            f"{nome}: needs deve apontar para outro job existente.")

    def testes(self, pr=False):
        for evento in (["push", "pull_request"] if pr else ["push"]):
            self.exigir(self.evento(evento), f"Acrescente o evento {evento} em on.")
            config = mapa(mapa(self.w.get("on")).get(evento))
            self.exigir(config.get("branches") == ["main"], f"{evento}: filtre branches: [main].")
        self.python("testar")
        self.exigir("python -m unittest" in self.comandos("testar"),
                    "No job testar, execute python -m unittest -v.")
        for step in self.steps("testar"):
            if "unittest" in str(step.get("run", "")):
                self.exigir(not step.get("continue-on-error") and "|| true" not in step["run"],
                            "Deixe o teste falhar: remova continue-on-error ou || true.")

    def python(self, job):
        steps = self.steps(job)
        checkout = self.action(job, "actions/checkout")
        setup = self.action(job, "actions/setup-python")
        self.exigir(bool(checkout), f"{job}: adicione actions/checkout antes de ler os arquivos.")
        self.exigir(mapa(setup.get("with")).get("python-version") == "3.12",
                    f"{job}: configure actions/setup-python com python-version: '3.12' (entre aspas).")
        instalar = next((s for s in steps if "python -m pip install -r requirements.txt" in str(s.get("run", ""))), {})
        self.exigir(bool(instalar), f"{job}: instale com python -m pip install -r requirements.txt.")
        if checkout and setup and instalar:
            self.exigir(steps.index(checkout) < steps.index(setup) < steps.index(instalar),
                        f"{job}: a ordem é checkout, setup-python e instalação.")
            for step in steps:
                if any(cmd in str(step.get("run", "")) for cmd in ["python -m unittest", "python build.py"]):
                    self.exigir(steps.index(instalar) < steps.index(step),
                                f"{job}: instale as dependências antes de testar ou gerar o site.")

    def build(self):
        self.testes(pr=True)
        self.python("empacotar")
        self.exigir("testar" in lista(mapa(self.jobs.get("empacotar")).get("needs")),
                    "No job empacotar, use needs: testar.")
        self.exigir("python build.py" in self.comandos("empacotar"),
                    "No job empacotar, gere o site com python build.py.")

    def verificar(self, n):
        self.base()
        if n == 1:
            self.exigir(self.evento("workflow_dispatch"), "Use on: workflow_dispatch para executar manualmente.")
            self.exigir(any("Olá, GitHub Actions!" in self.comandos(j) for j in self.jobs),
                        'Adicione uma etapa run que mostre "Olá, GitHub Actions!".')
        elif n in (2, 3):
            self.testes(pr=n == 3)
        elif n == 4:
            dispatch = mapa(mapa(self.w.get("on")).get("workflow_dispatch"))
            receita = mapa(mapa(dispatch.get("inputs")).get("receita"))
            self.exigir(receita.get("type") == "string", "Defina o input receita como type: string em workflow_dispatch.")
            self.exigir(mapa(self.w.get("env")).get("COZINHA") == "Cozinha do Curso", "Defina env: COZINHA: Cozinha do Curso no workflow.")
            envs = [mapa(s.get("env")) for j in self.jobs for s in self.steps(j)]
            for chave, referencia in [("RECEITA", "inputs.receita"), ("AUTOR", "github.actor"),
                                      ("TURMA", "vars.TURMA"), ("TOKEN_DEMO", "secrets.CURSO_TOKEN")]:
                self.exigir(any(expressao(e.get(chave)) == "${{" + referencia + "}}" for e in envs),
                            f"Passe {referencia} para {chave} usando env na etapa.")
        else:
            self.build()
            if n == 6:
                upload = self.action("empacotar", "actions/upload-artifact")
                config = mapa(upload.get("with"))
                self.exigir(config.get("name") == "site" and str(config.get("path", "")).rstrip("/") == "dist",
                            "Envie dist/ com actions/upload-artifact e name: site.")
                self.exigir(config.get("if-no-files-found") == "error" and config.get("retention-days") == 7,
                            "No upload, use if-no-files-found: error e retention-days: 7.")
                if upload:
                    steps = self.steps("empacotar")
                    self.exigir(any("python build.py" in str(s.get("run", "")) for s in steps[:steps.index(upload)]),
                                "Gere o site antes de enviar o artefato.")
            elif n == 7:
                self.pages()
        return self.falhas

    def pages(self):
        publicar = mapa(self.jobs.get("publicar"))
        leitura = mapa(mapa(self.jobs.get("empacotar")).get("permissions"))
        self.exigir(leitura.get("contents") == "read" and leitura.get("pages") == "read",
                    "No job empacotar, conceda contents: read e pages: read para consultar o site.")
        self.exigir("empacotar" in lista(publicar.get("needs")), "publicar precisa de needs: empacotar.")
        permissoes = mapa(publicar.get("permissions"))
        self.exigir(permissoes.get("pages") == "write" and permissoes.get("id-token") == "write",
                    "No job publicar, conceda pages: write e id-token: write.")
        self.exigir(mapa(publicar.get("environment")).get("name") == "github-pages",
                    "Use environment: name: github-pages no job publicar.")
        for job in ["empacotar", "publicar"]:
            condicao = expressao(mapa(self.jobs.get(job)).get("if", ""))
            self.exigir("github.ref=='refs/heads/main'" in condicao and "github.event_name!='pull_request'" in condicao,
                        f"{job}: limite o deploy à main e exclua pull_request com a condição do enunciado.")
        self.exigir(bool(self.action("empacotar", "actions/configure-pages")), "Adicione actions/configure-pages no build.")
        upload = self.action("empacotar", "actions/upload-pages-artifact")
        self.exigir(str(mapa(upload.get("with")).get("path", "")).rstrip("/") == "dist",
                    "Envie dist/ usando actions/upload-pages-artifact.")
        deploy = self.action("publicar", "actions/deploy-pages")
        self.exigir(bool(deploy) and deploy.get("id") == "deploy", "Use actions/deploy-pages com id: deploy.")
        url = mapa(publicar.get("environment")).get("url")
        self.exigir(expressao(url) == "${{steps.deploy.outputs.page_url}}", "Use a saída steps.deploy.outputs.page_url na URL do environment.")


def main():
    n = int(sys.argv[1])
    pasta = Path(sys.argv[2])
    arquivo = pasta / ".github/workflows/ci.yml"
    titulo = f"Exercício {n:02d} — {pasta.name.split('-', 1)[-1]}"
    try:
        workflow = yaml.load(arquivo.read_text(encoding="utf-8"), Loader=WorkflowLoader)
        if not isinstance(workflow, dict):
            raise ValueError("O workflow deve ser um mapa YAML, com name, on e jobs.")
        falhas = Verificador(workflow).verificar(n)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"❌ {titulo}: ainda não. Não consegui ler .github/workflows/ci.yml:\n\n • {exc}\n"
              "   💡 Confira o nome do arquivo, a indentação e as chaves do YAML.\n")
        return 1
    if falhas:
        print(f"❌ {titulo}: ainda não. Encontrei {len(falhas)} ponto(s) para ajustar no YAML:")
        for dica in falhas:
            print(f"\n • {dica}")
        print()
        return 1
    print(f"✅ YAML do exercício {n:02d}: requisitos atendidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
