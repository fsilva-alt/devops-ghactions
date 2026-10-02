"""Casos de integração do verificador e consistência do material didático."""

import copy
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

CURSO = Path(os.environ["CURSO_DIR"])
LABS = Path(os.environ["LABS_DIR"])
sys.path.insert(0, str(CURSO / "scripts"))
from checks import WorkflowLoader  # noqa: E402


def check(numero, sucesso, dica=""):
    resultado = subprocess.run(
        ["bash", str(CURSO / "scripts/check.sh"), f"{numero:02d}"],
        text=True, capture_output=True,
    )
    saida = resultado.stdout + resultado.stderr
    assert (resultado.returncode == 0) == sucesso, saida
    assert "Traceback" not in saida, saida
    assert dica in saida, saida


def mutacao(numero, original, mudar, dica):
    alterado = copy.deepcopy(original)
    mudar(alterado)
    arquivo = next(LABS.glob(f"{numero:02d}-*")) / ".github/workflows/ci.yml"
    arquivo.write_text(yaml.safe_dump(alterado, allow_unicode=True, sort_keys=False), encoding="utf-8")
    check(numero, False, dica)


def remover_matriz(w):
    w["jobs"]["testar"].pop("strategy")


for numero in range(1, 15):
    check(numero, False)
    texto = (CURSO / f"docs/solucoes/{numero:02d}.yml").read_text(encoding="utf-8")
    lab = next(LABS.glob(f"{numero:02d}-*"))
    arquivo = lab / ".github/workflows/ci.yml"
    arquivo.write_text(texto, encoding="utf-8")
    if numero == 13:
        # O workflow sozinho não basta: falta a ação composta que ele chama.
        check(numero, False, "action.yml")
        acao = lab / ".github/actions/preparar/action.yml"
        acao.parent.mkdir(parents=True, exist_ok=True)
        textoacao = (CURSO / "docs/solucoes/13-acao.yml").read_text(encoding="utf-8")
        acao.write_text(textoacao, encoding="utf-8")
        check(numero, True)
        for trocar, dica in [(("      shell: bash\n", ""), "shell: bash"), (("using: composite", "using: node20"), "composite"),
                             (("'3.12'", "3.12"), "entre aspas")]:
            acao.write_text(textoacao.replace(*trocar), encoding="utf-8")
            check(numero, False, dica)
        acao.write_text(textoacao, encoding="utf-8")
    check(numero, True)
    original = yaml.load(texto, Loader=WorkflowLoader)
    mutacao(numero, original, lambda w: w.pop("jobs"), "Crie jobs")
    mutacao(numero, original, lambda w: w.update(permissions="write-all"), "permissions")
    if numero == 1:
        mutacao(numero, original, lambda w: w.update(on={"push": None}), "workflow_dispatch")
    if numero in (2, 3, 5, 6, 7, 9, 10, 11, 12, 14):
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"][1]["with"].update({"python-version": 3.12}), "entre aspas")
    if numero >= 2 and numero != 4:
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"].pop(0), "checkout")
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"][-1].update({"continue-on-error": True}), "Deixe o teste falhar")
    if numero == 3:
        mutacao(numero, original, lambda w: w["on"].pop("pull_request"), "pull_request")
    if numero == 4:
        mutacao(numero, original, lambda w: w["jobs"]["apresentar"]["steps"][1]["env"].update(TOKEN_DEMO="valor-em-texto"), "secrets.CURSO_TOKEN")
    if numero in (5, 6, 7, 9, 13, 14):
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"].pop("needs"), "needs: testar")
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"].pop(0), "checkout")
    if numero == 8:
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["strategy"]["matrix"].update({"python-version": [3.11, 3.12]}), "entre aspas")
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["strategy"].pop("fail-fast"), "fail-fast: false")
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"][1]["with"].update({"python-version": "3.12"}), "matrix.python-version")
        mutacao(numero, original, remover_matriz, "strategy")
    if numero == 9:
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"][1]["with"].pop("cache"), "empacotar: acrescente cache: pip")
    if numero == 10:
        mutacao(numero, original, lambda w: w["on"]["push"].pop("paths-ignore"), "paths-ignore")
        mutacao(numero, original, lambda w: w["on"].update(schedule=[{"cron": "toda segunda"}]), "cron")
        mutacao(numero, original, lambda w: w["on"].update(schedule={"cron": "0 9 * * 1"}), "cron")
    if numero == 11:
        mutacao(numero, original, lambda w: w["jobs"].pop("validar"), "Crie o job validar")
        mutacao(numero, original, lambda w: w["jobs"]["validar"]["steps"][1].update(run="echo ok"), "::error file=")
    if numero == 12:
        mutacao(numero, original, lambda w: w["jobs"]["contar"].pop("outputs"), "outputs: total")
        mutacao(numero, original, lambda w: w["jobs"]["resumo"].update(needs="testar"), "needs com contar")
        mutacao(numero, original, lambda w: w["jobs"]["resumo"]["steps"][1]["env"].update(TOTAL="3"), "needs.contar.outputs.total")
    if numero == 13:
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"].pop(1), "./.github/actions/preparar")
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"].insert(1, {"uses": "actions/setup-python@v6"}), "remova-o do job")
    if numero == 14:
        mutacao(numero, original, lambda w: w["on"]["push"].pop("tags"), "tags")
        mutacao(numero, original, lambda w: w["jobs"]["lancar"].pop("if"), "refs/tags/v")
        mutacao(numero, original, lambda w: w["jobs"]["lancar"].pop("permissions"), "contents: write")
        mutacao(numero, original, lambda w: w["jobs"]["lancar"]["steps"][2]["env"].pop("GH_TOKEN"), "GH_TOKEN")
    if numero in (6, 14):
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"][-1]["with"].update(path="build/"), "Envie dist/")
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"][-1]["with"].update(path=123), "Envie dist/")
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"].insert(0, w["jobs"]["empacotar"]["steps"].pop()), "antes de enviar")
    if numero == 7:
        mutacao(numero, original, lambda w: w["jobs"]["publicar"].pop("if"), "exclua pull_request")
        mutacao(numero, original, lambda w: w["jobs"]["publicar"]["permissions"].pop("id-token"), "id-token")
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"][-1].update(uses="actions/upload-artifact@v4"), "upload-pages-artifact")
    # YAML inválido, chaves duplicadas e formatos errados devem dar uma dica.
    for invalido in ["name: [\n", "name: um\nname: dois\n", "- lista\n", "jobs: []\non: null\n"]:
        arquivo.write_text(invalido, encoding="utf-8")
        check(numero, False)
    arquivo.write_text(texto, encoding="utf-8")
    check(numero, True)
    print(f"✅ {numero:02d}: início reprovado, solução aprovada e erros detectados.")

for arquivo in [CURSO / "README.md", *CURSO.glob("docs/*.md")]:
    texto = arquivo.read_text(encoding="utf-8")
    for link in re.findall(r"\]\(([^)]+)\)", texto):
        if link.startswith(("https://", "http://", "#")):
            continue
        destino = unquote(link.split("#")[0])
        assert (arquivo.parent / destino).exists(), f"Link quebrado: {arquivo}: {link}"
config = json.loads((CURSO / ".devcontainer/devcontainer.json").read_text())
assert "scripts/requirements.txt" in config["postCreateCommand"]
solucoes = sorted(p.name for p in (CURSO / "docs/solucoes").glob("*.yml"))
assert solucoes == sorted([f"{n:02d}.yml" for n in range(1, 15)] + ["13-acao.yml"]), solucoes
subprocess.run([sys.executable, str(CURSO / "tests/apresentacao.py")], check=True)
print("✅ 7 exercícios da aula e 7 opcionais no site, links locais e configuração do Codespace.")
