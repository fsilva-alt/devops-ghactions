# Livro de receitas

Projeto de prática do curso de GitHub Actions. As receitas ficam em `receitas/`,
uma por arquivo, e o título do site fica em `livro.md`. Edite e execute os
comandos no **GitHub Codespaces**; os workflows executam em runners hospedados
pelo GitHub.

## Executar no terminal do Codespace

```bash
python3 receitas.py          # lista as receitas no terminal
python3 -m unittest -v       # roda os três testes
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python build.py              # gera dist/index.html
```

`receitas.py` também calcula a quantidade de um ingrediente para várias
receitas: três receitas de pão de queijo, com 500 g de polvilho cada, pedem
1500 g. Os exercícios ficam no [site do curso](https://fsilva-alt.github.io/devops-ghactions/).
