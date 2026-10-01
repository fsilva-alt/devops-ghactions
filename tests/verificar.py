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


for numero in range(1, 8):
    check(numero, False)
    texto = (CURSO / f"docs/solucoes/{numero:02d}.yml").read_text(encoding="utf-8")
    arquivo = next(LABS.glob(f"{numero:02d}-*")) / ".github/workflows/ci.yml"
    arquivo.write_text(texto, encoding="utf-8")
    check(numero, True)
    original = yaml.load(texto, Loader=WorkflowLoader)
    mutacao(numero, original, lambda w: w.pop("jobs"), "Crie jobs")
    mutacao(numero, original, lambda w: w.update(permissions="write-all"), "permissions")
    if numero == 1:
        mutacao(numero, original, lambda w: w.update(on={"push": None}), "workflow_dispatch")
    if numero in (2, 3, 5, 6, 7):
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"].pop(0), "checkout")
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"][1]["with"].update({"python-version": 3.12}), "entre aspas")
        mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"][-1].update({"continue-on-error": True}), "Deixe o teste falhar")
    if numero == 3:
        mutacao(numero, original, lambda w: w["on"].pop("pull_request"), "pull_request")
    if numero == 4:
        mutacao(numero, original, lambda w: w["jobs"]["apresentar"]["steps"][1]["env"].update(TOKEN_DEMO="valor-em-texto"), "secrets.CURSO_TOKEN")
    if numero >= 5:
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"].pop("needs"), "needs: testar")
        mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"].pop(0), "checkout")
    if numero == 6:
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

enunciados = sorted((CURSO / "exercises").glob("*/README.md"))
assert len(enunciados) == 7
assert [p.parent.name[:2] for p in enunciados] == [f"{n:02d}" for n in range(1, 8)]
for arquivo in [CURSO / "README.md", *CURSO.glob("docs/*.md"), *enunciados]:
    texto = arquivo.read_text(encoding="utf-8")
    for link in re.findall(r"\]\(([^)]+)\)", texto):
        if link.startswith(("https://", "http://", "#")):
            continue
        destino = unquote(link.split("#")[0])
        assert (arquivo.parent / destino).exists(), f"Link quebrado: {arquivo}: {link}"
for arquivo in enunciados:
    assert "Codespaces" in arquivo.read_text(encoding="utf-8")
config = json.loads((CURSO / ".devcontainer/devcontainer.json").read_text())
assert "install.sh" in config["postCreateCommand"]
assert len(list((CURSO / "docs/solucoes").glob("*.yml"))) == 7
slides = (CURSO / "docs/curso.js").read_text(encoding="utf-8")
assert re.findall(r"\{id:'(0[1-7])', slug:", slides) == [f"{n:02d}" for n in range(1, 8)]
for enunciado in enunciados:
    assert enunciado.parent.name[3:] in slides
assert sum(map(int, re.findall(r"time:(\d+)", slides))) == 155
print("✅ Exatamente 7 exercícios, 155 minutos de blocos, links locais e configuração do Codespace.")
