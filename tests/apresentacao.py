"""Confere a estrutura dos slides, o HTML gerado e os links da apresentação."""

import json
import re
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

CURSO = Path(__file__).resolve().parent.parent
PAGINA = CURSO / "docs/index.html"
VAZIOS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param",
          "source", "track", "wbr", "path", "circle"}


class Html(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pilha, self.links, self.textos = [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for chave in ("href", "src"):
            if chave in attrs:
                self.links.append(attrs[chave])
        if tag not in VAZIOS:
            self.pilha.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VAZIOS:
            self.pilha.pop()

    def handle_endtag(self, tag):
        assert self.pilha and self.pilha[-1] == tag, f"Fechamento HTML incorreto: </{tag}> depois de {self.pilha[-3:]}"
        self.pilha.pop()

    def handle_data(self, data):
        self.textos.append(data)


def analisar(html, onde):
    parser = Html()
    parser.feed(html)
    parser.close()
    assert not parser.pilha, f"{onde}: elementos sem fechamento: {parser.pilha}"
    texto = "".join(parser.textos)
    # ${{ … }} é sintaxe do Actions; um ${ isolado seria uma expressão do JavaScript esquecida.
    assert not re.search(r"\$\{(?!\{)|undefined|\[object Object\]", texto), f"{onde}: expressão não resolvida"
    return parser.links, texto


node = shutil.which("node")
assert node, "Os testes da apresentação precisam do Node.js (node) para executar os slides."
dados = json.loads(subprocess.run([node, str(CURSO / "tests/slides.mjs")], check=True,
                                  capture_output=True, text=True).stdout)

pagina = PAGINA.read_text(encoding="utf-8")
assert "<title>GitHub Actions no Codespaces</title>" in pagina
assert not re.search(r"devops-(git|docker)", pagina), "Os cursos são independentes: sem links entre eles."

exercicios = dados["exercicios"]
assert [e["key"] for e in exercicios] == ["intro", *[f"{n:02d}" for n in range(8)]]
aula = [e for e in exercicios[1:] if not e["antes"]]
assert [e["n"] for e in aula] == list(range(1, 8)) and sum(e["time"] for e in aula) == 155
assert exercicios[1]["antes"], "O exercício 00 é feito antes da aula."

# Introdução: o que é o Actions, os problemas que resolve e o uso em CI/CD.
titulos_intro = [s["h"] for s in exercicios[0]["slides"]]
for tema in ["O que é o GitHub Actions?", "Que problemas ele resolve?", "O Actions em um processo de CI/CD",
             "Como ele é usado na prática?"]:
    assert tema in titulos_intro, f"Introdução sem o slide: {tema}"

# Cada exercício: capa, até três conceitos, comandos e documentação, e a tarefa numerada.
for e in exercicios[1:]:
    tipos = [s["eyebrow"] for s in e["slides"]]
    assert tipos[0] == "", f"{e['key']}: o primeiro slide é a capa"
    conceitos = tipos[1:-2]
    assert 1 <= len(conceitos) <= 3 and set(conceitos) == {"Conceito"}, f"{e['key']}: 1 a 3 slides de conceito"
    assert tipos[-2] == "Referência" and e["slides"][-2]["h"] == "Comandos e documentação", e["key"]
    assert tipos[-1] == f"Tarefa · {e['time']} min" and e["slides"][-1]["h"] == "O exercício", e["key"]
    assert e["entrega"], f"{e['key']}: a capa informa a entrega"

for s in dados["slides"]:
    onde = f"slide {s['key']}/{s['i'] + 1}"
    links, texto = analisar(s["html"], onde)
    if s["eyebrow"] == "Referência":
        assert '<table class="kv">' in s["html"] and '<ul class="links">' in s["html"], f"{onde}: comandos e links"
    if s["eyebrow"].startswith("Tarefa"):
        assert '<ol class="steps">' in s["html"], f"{onde}: passos numerados"
        assert f"check.sh {s['key']}" in texto, f"{onde}: verificação com check.sh"
    if s["key"] not in ("intro", "00") and s["i"] == 0:
        assert f"~/labs/{s['key']}-" in texto, f"{onde}: a capa indica a pasta do laboratório"
    for link in links:
        url = urlsplit(link)
        assert url.scheme in ("https", "") , f"{onde}: link inseguro {link}"
        if not url.scheme and url.path:
            assert (PAGINA.parent / unquote(url.path)).is_file(), f"{onde}: arquivo ausente {link}"

links, texto = analisar(dados["home"], "início")
assert 'class="tema"' in dados["home"], "O início tem o seletor de tema."
assert re.search(r'<div class="right">.*<button class="tema"', pagina), "Os slides têm o seletor de tema."
for n in range(1, 8):
    assert f"#/d/{n:02d}/1" in links
print(f"✅ Apresentação: {len(dados['slides'])} slides, introdução, 00 + 7 exercícios, 155 minutos e links válidos.")
