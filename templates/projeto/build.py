"""Gera o site do livro de receitas, usado como artefato e no GitHub Pages."""

import html
from pathlib import Path

import markdown

from receitas import listar

livro = Path("livro.md").read_text(encoding="utf-8")
titulo = livro.splitlines()[0].removeprefix("#").strip() or "Livro de receitas"
receitas = listar()

indice = "".join(
    f'<li><a href="#{r["arquivo"].stem}">{html.escape(r["nome"])}</a> <small>rende {html.escape(r["rende"])}</small></li>'
    for r in receitas
)
artigos = "".join(
    f'<article id="{r["arquivo"].stem}">{markdown.markdown(r["arquivo"].read_text(encoding="utf-8"))}</article>'
    for r in receitas
)

destino = Path("dist")
destino.mkdir(exist_ok=True)
(destino / "index.html").write_text(
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
    f"<title>{html.escape(titulo)}</title>"
    "<style>body{max-width:46rem;margin:3rem auto;padding:0 1rem;font:1.05rem/1.6 system-ui;"
    "color:#1b2014;background:#f6f7f0}a{color:#4a7300}small{color:#68715c}"
    "article{background:#fff;border:1px solid #dde2d0;border-radius:10px;padding:.5rem 1.5rem;margin:1.5rem 0}"
    "@media (prefers-color-scheme:dark){body{color:#eef2e6;background:#0f120d}a{color:#c3e84b}"
    "small{color:#8a9380}article{background:#161a13;border-color:#262c21}}</style>"
    f"</head><body>{markdown.markdown(livro)}<ul>{indice}</ul>{artigos}</body></html>",
    encoding="utf-8",
)
print(f"Site gerado em dist/index.html com {len(receitas)} receitas")
