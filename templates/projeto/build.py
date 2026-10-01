"""Gera o site estático usado como artefato e no GitHub Pages."""

from pathlib import Path

import markdown

conteudo = markdown.markdown(
    Path("cardapio.md").read_text(encoding="utf-8"), extensions=["tables"]
)
destino = Path("dist")
destino.mkdir(exist_ok=True)
(destino / "index.html").write_text(
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
    '<title>Cardápio da comunidade</title>'
    '<style>body{max-width:48rem;margin:3rem auto;padding:0 1rem;'
    'font:1.1rem/1.6 system-ui}table{border-collapse:collapse}'
    'td,th{padding:.5rem 1rem;border:1px solid #ccc}</style>'
    f'</head><body>{conteudo}</body></html>',
    encoding="utf-8",
)
print("Site gerado em dist/index.html")
