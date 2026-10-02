"""Simula o workflow do exercício com o act: cada job roda em um container Docker do Codespace.

O act lê .github/workflows/ci.yml, cria um container a partir de uma imagem parecida com
o runner ubuntu-latest e executa as etapas, como o GitHub faria. Assim, o aluno vê os
testes passarem (ou falharem) antes de publicar. Não acessa a conta no GitHub.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

# Evento simulado em cada exercício e jobs que precisam terminar com sucesso.
EVENTO = {0: "push", 1: "workflow_dispatch", 2: "push", 3: "pull_request", 4: "workflow_dispatch",
          5: "push", 6: "push", 7: "pull_request"}
JOBS_OK = {2: {"testar"}, 3: {"testar"}, 5: {"testar", "empacotar"}, 6: {"testar", "empacotar"},
           7: {"testar"}}
# Trechos que precisam aparecer no log da execução.
LOG = {0: "Olá do runner local!", 1: "Olá, GitHub Actions!", 4: "Receita do dia:"}

# Avisos do runner local que não ajudam a entender o exercício.
RUIDO = ("WARNING: Running pip as the 'root' user", "DeprecationWarning", "node --trace-deprecation")

MINIMO = """name: Ambiente
on: push
jobs:
  teste:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Olá do runner local!"
"""


def disponivel():
    """Motivo para não simular, ou None quando o act e o Docker estão prontos."""
    act = os.environ.get("ACT_BIN", "")
    if not (act and os.access(act, os.X_OK)):
        return "o act não está instalado. Rode setup.sh (check.sh 00 mostra o que falta)."
    if not shutil.which("docker"):
        return "o comando docker não foi encontrado."
    try:
        subprocess.run(["docker", "info"], capture_output=True, timeout=20, check=True)
    except (subprocess.SubprocessError, OSError):
        return "o serviço do Docker não respondeu. Num Codespace recém-aberto, espere um minuto."
    return None


def comando(n, pasta, artefatos):
    imagem = os.environ["ACT_IMAGEM"]
    cmd = [os.environ["ACT_BIN"], EVENTO[n], "-W", ".github/workflows/ci.yml",
           "-P", f"ubuntu-latest={imagem}", "--action-offline-mode", "--rm", "--json",
           "--actor", os.environ.get("GITHUB_USER") or "aluno"]
    if n in (3, 7):
        evento = pasta / ".git/curso-actions/pull_request.json"
        evento.parent.mkdir(parents=True, exist_ok=True)
        evento.write_text(json.dumps({"pull_request": {"head": {"ref": "teste-do-ci"}, "base": {"ref": "main"}}}))
        cmd += ["-e", str(evento)]
    if n == 4:
        # Valores locais no lugar dos cadastrados em Settings > Secrets and variables > Actions.
        cmd += ["--var", "TURMA=turma-local", "-s", "CURSO_TOKEN=somente-demonstracao"]
    if n == 6:
        cmd += ["--artifact-server-path", str(artefatos)]
    return cmd


def executar(cmd, pasta):
    """Roda o act e mostra um log curto; devolve (código, resultados dos jobs, saída dos comandos)."""
    jobs, saida = {}, []
    processo = subprocess.Popen(cmd, cwd=pasta, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
    for linha in processo.stdout or []:
        try:
            evento = json.loads(linha)
        except json.JSONDecodeError:
            if linha.strip():
                print(f"  {linha.rstrip()}")
            continue
        if not isinstance(evento, dict):
            continue
        job = evento.get("jobID") or "act"
        msg = str(evento.get("msg", "")).rstrip()
        if evento.get("raw_output"):
            saida.append(msg)
            if not any(r in msg for r in RUIDO):
                print(f"  {job} │ {msg}")
        elif evento.get("stepResult") and evento.get("stage") == "Main":
            marca = {"success": "✅", "failure": "❌", "skipped": "pulada:"}.get(evento["stepResult"], "•")
            print(f"  {job} {marca} {evento.get('step', '')}")
        elif evento.get("jobResult"):
            jobs[job] = evento["jobResult"]
            print(f"  {job} ── {'job concluído' if evento['jobResult'] == 'success' else 'job com falha'}")
        elif evento.get("level") in ("error", "fatal") and msg:
            print(f"  {job} erro: {msg}")
    return processo.wait(), jobs, "\n".join(saida)


def conferir(n, codigo, jobs, saida, artefatos):
    falhas = []
    if not jobs:
        falhas.append(("Nenhum job foi executado na simulação.",
                       f"Confira se o evento {EVENTO[n]} está em on e se os filtros de branch incluem main."))
    for job, resultado in jobs.items():
        if resultado != "success":
            falhas.append((f"O job {job} falhou na simulação.",
                           "Leia a etapa marcada com ❌ acima. No GitHub, a mesma etapa falharia no runner."))
    for job in sorted(JOBS_OK.get(n, set()) - set(jobs)):
        if falhas:
            falhas.append((f"O job {job} foi pulado porque um job anterior falhou.",
                           "É o efeito de needs: corrija a falha e rode check.sh de novo."))
        else:
            falhas.append((f"O job {job} não foi executado.", "Confira o nome do job e o needs entre os jobs."))
    if codigo != 0 and not falhas:
        falhas.append(("O act terminou com erro.", "Leia a mensagem acima e confira o YAML."))
    if n in LOG and LOG[n] not in saida:
        falhas.append((f"A mensagem \"{LOG[n]}\" não apareceu no log.", "Confira o texto da etapa run."))
    if n == 6 and not falhas:
        zips = sorted(Path(artefatos).glob("*/site/*.zip"))
        nomes = zipfile.ZipFile(zips[0]).namelist() if zips else []
        if "index.html" in nomes:
            print(f"  artefato site: {', '.join(nomes)}")
        else:
            falhas.append(("O artefato site não contém index.html.", "Envie a pasta dist/ depois de python build.py."))
    if n == 7 and not falhas:
        fora = [j for j in ("empacotar", "publicar") if j in jobs]
        if fora:
            falhas.append((f"Em um pull request, {' e '.join(fora)} também rodou.",
                           "Use o if do enunciado nos dois jobs: o deploy só pode acontecer na main."))
        else:
            print("  pull_request ── empacotar e publicar não rodaram, como esperado: o deploy só acontece na main.")
    return falhas


def main():
    n = int(sys.argv[1])
    pasta = Path(sys.argv[2])
    motivo = disponivel()
    if motivo:
        print(f"⚠️  Simulação com o act pulada: {motivo}")
        print("   O YAML foi conferido, mas os jobs não foram executados no Codespace.")
        return 0 if n else 1
    if n == 0:
        (pasta / ".github/workflows").mkdir(parents=True, exist_ok=True)
        (pasta / ".github/workflows/ci.yml").write_text(MINIMO, encoding="utf-8")
        subprocess.run(["git", "init", "-q", "-b", "main", str(pasta)], check=True)
    if subprocess.run(["docker", "image", "inspect", os.environ["ACT_IMAGEM"]], capture_output=True).returncode != 0:
        nome = os.environ.get("ACT_IMAGEM_NOME", os.environ["ACT_IMAGEM"])
        print(f"▶ Baixando a imagem do runner local ({nome}, cerca de 2 GB). Só acontece uma vez.")
    print(f"▶ Simulando o workflow com o act (evento {EVENTO[n]}), cada job em um container Docker...")
    with tempfile.TemporaryDirectory(prefix="curso-act-") as artefatos:
        codigo, jobs, saida = executar(comando(n, pasta, artefatos), pasta)
        falhas = conferir(n, codigo, jobs, saida, artefatos)
    if n == 0:
        shutil.rmtree(pasta, ignore_errors=True)
    if falhas:
        print(f"❌ A simulação encontrou {len(falhas)} ponto(s) para ajustar:")
        for problema, dica in falhas:
            print(f"\n • {problema}\n   💡 {dica}")
        print()
        return 1
    print("✅ Simulação concluída: os jobs rodaram em containers, como no runner do GitHub.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
