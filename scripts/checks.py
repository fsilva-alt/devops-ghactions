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

# A ação composta do exercício 13, chamada pelos jobs com uses.
ACAO = "./.github/actions/preparar"


def mapa(valor):
    return valor if isinstance(valor, dict) else {}


def lista(valor):
    return valor if isinstance(valor, list) else [valor] if valor is not None else []


def expressao(valor):
    return re.sub(r"\s+", "", str(valor))


class Verificador:
    def __init__(self, workflow, pasta=None):
        self.w = workflow
        self.pasta = pasta
        self.jobs = mapa(workflow.get("jobs"))
        self.falhas = []
        # Como cada job prepara o Python: setup-python no próprio job ou, no 13, a ação composta.
        self.preparo = self.python
        self.matriz = False

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
        self.preparo("testar")
        self.exigir("python -m unittest" in self.comandos("testar"),
                    "No job testar, execute python -m unittest -v.")
        for step in self.steps("testar"):
            if "unittest" in str(step.get("run", "")):
                self.exigir(not step.get("continue-on-error") and "|| true" not in step["run"],
                            "Deixe o teste falhar: remova continue-on-error ou || true.")

    def depois_do_preparo(self, job, preparo, dica):
        steps = self.steps(job)
        for step in steps:
            if any(cmd in str(step.get("run", "")) for cmd in ["python -m unittest", "python build.py"]):
                self.exigir(steps.index(preparo) < steps.index(step), dica)

    def python(self, job):
        steps = self.steps(job)
        checkout = self.action(job, "actions/checkout")
        setup = self.action(job, "actions/setup-python")
        self.exigir(bool(checkout), f"{job}: adicione actions/checkout antes de ler os arquivos.")
        versao = mapa(setup.get("with")).get("python-version")
        if self.matriz:
            self.exigir(expressao(versao) == "${{matrix.python-version}}",
                        job + ": em actions/setup-python, use python-version: ${{ matrix.python-version }}.")
        else:
            self.exigir(versao == "3.12", f"{job}: configure actions/setup-python com python-version: '3.12' (entre aspas).")
        instalar = next((s for s in steps if "python -m pip install -r requirements.txt" in str(s.get("run", ""))), {})
        self.exigir(bool(instalar), f"{job}: instale com python -m pip install -r requirements.txt.")
        if checkout and setup and instalar:
            self.exigir(steps.index(checkout) < steps.index(setup) < steps.index(instalar),
                        f"{job}: a ordem é checkout, setup-python e instalação.")
            self.depois_do_preparo(job, instalar, f"{job}: instale as dependências antes de testar ou gerar o site.")

    def acao_local(self, job):
        steps = self.steps(job)
        checkout = self.action(job, "actions/checkout")
        acao = next((s for s in steps if str(s.get("uses", "")).rstrip("/") == ACAO), {})
        self.exigir(bool(checkout), f"{job}: adicione actions/checkout antes da ação preparar.")
        self.exigir(bool(acao), f"{job}: troque o setup-python e a instalação por uses: {ACAO}.")
        self.exigir(not self.action(job, "actions/setup-python"),
                    f"{job}: o setup-python agora fica na ação preparar; remova-o do job.")
        if checkout and acao:
            self.exigir(steps.index(checkout) < steps.index(acao),
                        f"{job}: o checkout vem antes da ação preparar, que é uma pasta do repositório.")
            self.depois_do_preparo(job, acao, f"{job}: use a ação preparar antes de testar ou gerar o site.")

    def acao_composta(self):
        pasta = (self.pasta or Path(".")) / ".github/actions/preparar"
        arquivo = next((pasta / nome for nome in ("action.yml", "action.yaml") if (pasta / nome).is_file()), None)
        if not arquivo:
            self.falhas.append("Crie .github/actions/preparar/action.yml com a ação composta do enunciado.")
            return
        try:
            acao = mapa(yaml.load(arquivo.read_text(encoding="utf-8"), Loader=WorkflowLoader))
        except (ValueError, yaml.YAMLError) as exc:
            self.falhas.append(f"Não consegui ler {arquivo.name} da ação preparar: {exc}")
            return
        self.exigir(bool(acao.get("name")) and bool(acao.get("description")), "action.yml: dê name e description à ação.")
        runs = mapa(acao.get("runs"))
        self.exigir(runs.get("using") == "composite", "action.yml: use runs: using: composite.")
        passos = [mapa(s) for s in lista(runs.get("steps"))]
        setup = next((s for s in passos if str(s.get("uses", "")).startswith("actions/setup-python@")), {})
        instalar = next((s for s in passos if "python -m pip install -r requirements.txt" in str(s.get("run", ""))), {})
        self.exigir(mapa(setup.get("with")).get("python-version") == "3.12",
                    "action.yml: use actions/setup-python com python-version: '3.12' (entre aspas).")
        self.exigir(bool(instalar), "action.yml: instale com python -m pip install -r requirements.txt.")
        self.exigir(all(p.get("shell") == "bash" for p in passos if p.get("run")),
                    "action.yml: numa ação composta, cada run precisa de shell: bash.")
        if setup and instalar:
            self.exigir(passos.index(setup) < passos.index(instalar), "action.yml: o setup-python vem antes da instalação.")

    def build(self):
        self.testes(pr=True)
        self.preparo("empacotar")
        self.exigir("testar" in lista(mapa(self.jobs.get("empacotar")).get("needs")),
                    "No job empacotar, use needs: testar.")
        self.exigir("python build.py" in self.comandos("empacotar"),
                    "No job empacotar, gere o site com python build.py.")

    def artefato(self):
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
        elif n == 8:
            self.matriz_de_versoes()
        elif n == 10:
            self.testes(pr=True)
            self.caminhos_e_agenda()
        elif n == 11:
            self.testes(pr=True)
            self.validar()
        elif n == 12:
            self.testes(pr=True)
            self.saidas()
        else:
            # 5, 6, 7, 9, 13 e 14: testes e build do site, em dois jobs.
            if n == 13:
                self.preparo = self.acao_local
                self.acao_composta()
            self.build()
            if n in (6, 14):
                self.artefato()
            if n == 7:
                self.pages()
            elif n == 9:
                self.cache()
            elif n == 14:
                self.release()
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

    def matriz_de_versoes(self):
        estrategia = mapa(mapa(self.jobs.get("testar")).get("strategy"))
        versoes = mapa(estrategia.get("matrix")).get("python-version")
        self.exigir(isinstance(versoes, list) and len(versoes) >= 2 and "3.12" in versoes,
                    "No job testar, crie strategy: matrix: python-version com pelo menos duas versões, incluindo '3.12'.")
        self.exigir(all(isinstance(v, str) for v in lista(versoes)),
                    "Escreva as versões da matriz entre aspas: sem elas, 3.10 vira o número 3.1.")
        self.exigir(estrategia.get("fail-fast") is False,
                    "Em strategy, use fail-fast: false para ver o resultado de todas as versões.")
        self.matriz = True
        self.testes(pr=True)

    def cache(self):
        for job in ("testar", "empacotar"):
            setup = self.action(job, "actions/setup-python")
            self.exigir(mapa(setup.get("with")).get("cache") == "pip",
                        f"{job}: acrescente cache: pip ao with de actions/setup-python.")

    def caminhos_e_agenda(self):
        eventos = mapa(self.w.get("on"))
        push = mapa(eventos.get("push"))
        self.exigir("README.md" in lista(push.get("paths-ignore")),
                    "No evento push, acrescente paths-ignore com 'README.md'.")
        self.exigir(not ("paths" in push and "paths-ignore" in push),
                    "No push, use paths ou paths-ignore, não os dois.")
        agenda = eventos.get("schedule")
        self.exigir(isinstance(agenda, list) and bool(agenda) and all(
            re.fullmatch(r"\S+(\s+\S+){4}", str(mapa(a).get("cron", "")).strip()) for a in agenda),
            "Acrescente schedule com - cron: '0 9 * * 1' (cinco campos separados por espaço, em UTC).")

    def validar(self):
        self.exigir("validar" in self.jobs, "Crie o job validar, no mesmo nível de testar.")
        if "validar" not in self.jobs:
            return
        self.exigir(bool(self.action("validar", "actions/checkout")),
                    "validar: adicione actions/checkout antes de ler as receitas.")
        comandos = self.comandos("validar")
        self.exigir("::error file=" in comandos and "Rende:" in comandos,
                    "validar: escreva uma anotação ::error file=… para cada receita sem a linha Rende:.")
        self.exigir(not any(s.get("continue-on-error") for s in self.steps("validar")),
                    "validar: deixe a etapa falhar: remova continue-on-error.")

    def saidas(self):
        contar, resumo = mapa(self.jobs.get("contar")), mapa(self.jobs.get("resumo"))
        self.exigir(bool(contar) and bool(resumo), "Crie os jobs contar e resumo, no mesmo nível de testar.")
        self.exigir(bool(self.action("contar", "actions/checkout")),
                    "contar: adicione actions/checkout antes de contar as receitas.")
        contagem = next((s for s in self.steps("contar") if s.get("id") == "contagem"), {})
        self.exigir("GITHUB_OUTPUT" in str(contagem.get("run", "")) and "total=" in str(contagem.get("run", "")),
                    "contar: a etapa com id: contagem escreve total=… em $GITHUB_OUTPUT.")
        self.exigir(expressao(mapa(contar.get("outputs")).get("total")) == "${{steps.contagem.outputs.total}}",
                    "contar: exponha a saída com outputs: total: ${{ steps.contagem.outputs.total }}.")
        self.exigir("contar" in lista(resumo.get("needs")), "resumo: use needs com contar, para ler a saída dele.")
        valores = [v for s in self.steps("resumo") for v in mapa(s.get("env")).values()]
        self.exigir(any(expressao(v) == "${{needs.contar.outputs.total}}" for v in valores),
                    "resumo: leia ${{ needs.contar.outputs.total }} em env, na etapa do resumo.")
        self.exigir("GITHUB_STEP_SUMMARY" in self.comandos("resumo"),
                    "resumo: escreva o resumo em $GITHUB_STEP_SUMMARY.")

    def release(self):
        push = mapa(mapa(self.w.get("on")).get("push"))
        self.exigir("v*" in lista(push.get("tags")), "No evento push, acrescente tags: ['v*'].")
        lancar = mapa(self.jobs.get("lancar"))
        self.exigir(bool(lancar), "Crie o job lancar, no mesmo nível de empacotar.")
        self.exigir("empacotar" in lista(lancar.get("needs")), "lancar precisa de needs: empacotar.")
        self.exigir("startsWith(github.ref,'refs/tags/v')" in expressao(lancar.get("if", "")),
                    "lancar: use if: startsWith(github.ref, 'refs/tags/v'), para rodar só com uma tag.")
        self.exigir(mapa(lancar.get("permissions")).get("contents") == "write",
                    "lancar: conceda contents: write só neste job, para criar o release.")
        baixar = self.action("lancar", "actions/download-artifact")
        self.exigir(mapa(baixar.get("with")).get("name") == "site",
                    "lancar: baixe o artefato site com actions/download-artifact.")
        criar = next((s for s in self.steps("lancar") if "gh release create" in str(s.get("run", ""))), {})
        self.exigir(bool(criar), "lancar: crie o release com gh release create.")
        self.exigir(expressao(mapa(criar.get("env")).get("GH_TOKEN")) in ("${{github.token}}", "${{secrets.GITHUB_TOKEN}}"),
                    "lancar: passe o token ao gh com env: GH_TOKEN: ${{ github.token }}.")


def main():
    n = int(sys.argv[1])
    pasta = Path(sys.argv[2])
    arquivo = pasta / ".github/workflows/ci.yml"
    titulo = f"Exercício {n:02d} — {pasta.name.split('-', 1)[-1]}"
    try:
        workflow = yaml.load(arquivo.read_text(encoding="utf-8"), Loader=WorkflowLoader)
        if not isinstance(workflow, dict):
            raise ValueError("O workflow deve ser um mapa YAML, com name, on e jobs.")
        falhas = Verificador(workflow, pasta).verificar(n)
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
