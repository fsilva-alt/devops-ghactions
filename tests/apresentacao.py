"""Confere o conteúdo estático e os destinos da navegação da apresentação."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

CURSO = Path(__file__).resolve().parent.parent
PAGINA = CURSO / "docs/index.html"


class Apresentacao(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elementos = []
        self.pilha = []

    def handle_starttag(self, tag, attrs):
        elemento = {"tag": tag, "attrs": dict(attrs), "texto": ""}
        self.elementos.append(elemento)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input",
                       "link", "meta", "param", "source", "track", "wbr"}:
            self.pilha.append(elemento)

    def handle_endtag(self, tag):
        assert self.pilha and self.pilha[-1]["tag"] == tag, f"Fechamento HTML incorreto: {tag}"
        self.pilha.pop()

    def handle_data(self, data):
        for elemento in self.pilha:
            elemento["texto"] += data

    def com_classe(self, classe):
        return [e for e in self.elementos if classe in e["attrs"].get("class", "").split()]


pagina = Apresentacao()
pagina.feed(PAGINA.read_text(encoding="utf-8"))
pagina.close()
assert not pagina.pilha, "Há elementos HTML sem fechamento."
ids = [e["attrs"]["id"] for e in pagina.elementos if "id" in e["attrs"]]
assert len(ids) == len(set(ids)), "IDs duplicados na apresentação."
assert not any(e["tag"] == "script" for e in pagina.elementos), "A apresentação deve funcionar sem scripts."

links = []
for elemento in pagina.elementos:
    attrs = elemento["attrs"]
    for referencia in attrs.get("aria-labelledby", "").split():
        assert referencia in ids, f"Título acessível inexistente: {referencia}"
    for atributo in ("href", "src"):
        if atributo not in attrs:
            continue
        link = attrs[atributo]
        links.append(link)
        url = urlsplit(link)
        if not url.scheme and not url.netloc:
            if url.path:
                assert (PAGINA.parent / unquote(url.path)).is_file(), f"Arquivo ausente: {link}"
            elif url.fragment:
                assert unquote(url.fragment) in ids, f"Âncora quebrada: {link}"

destinos = [f"exercicio-{n:02d}" for n in range(1, 8)]
aulas = pagina.com_classe("lesson")
assert [e["attrs"]["id"] for e in aulas] == ["intro", *destinos]
assert [e["attrs"]["href"] for e in pagina.com_classe("exercise-card")] == [f"#{d}" for d in destinos]
tempos = [int(e["texto"].removesuffix(" min")) for e in pagina.com_classe("card-time")]
assert len(tempos) == 7 and sum(tempos) == 155
for card, aula, tempo in zip(pagina.com_classe("exercise-card"), aulas[1:], tempos):
    titulo = next(e["texto"] for e in pagina.elementos if e["attrs"].get("id") == aula["attrs"]["aria-labelledby"])
    assert titulo in card["texto"] and "Codespaces" in aula["texto"]
    assert f"{tempo} minutos" in aula["texto"]
print("✅ Apresentação estática: 7 exercícios, 155 minutos, títulos e links de navegação válidos.")
