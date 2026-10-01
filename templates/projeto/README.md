# Cardápio da comunidade

Projeto de prática do curso de GitHub Actions. Edite e execute os comandos no
**GitHub Codespaces**. Os workflows executam em runners hospedados pelo GitHub.

## Executar no terminal do Codespace

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest -v
python build.py
```

O build gera `dist/index.html`. Os preços em `app.py` são expressos em centavos.
Os enunciados ficam no repositório do curso, em `exercises/`.
