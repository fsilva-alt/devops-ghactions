# 02 — Testes no push

**25 minutos · Ambiente obrigatório: GitHub Codespaces**

## Objetivo

Executar testes automaticamente quando a `main` recebe um push e entender a diferença entre `uses` e `run`.

## Onde e estado inicial

```bash
cd ~/labs-actions/02-testes-no-push
code .github/workflows/ci.yml
```

Este laboratório independente já contém a saudação do exercício 01, `app.py`, três testes em `test_app.py`, `requirements.txt` e o gerador de site `build.py`.

**CI, integração contínua**, verifica mudanças automaticamente. Os testes prontos conferem o cálculo de um pedido: preço em centavos × quantidade.

## Tarefa

1. Execute os testes no terminal do Codespace para ver a saída esperada:

   ```bash
   python3 -m unittest -v
   ```

   Procure `Ran 3 tests` e `OK`. Esses testes usam a biblioteca padrão do Python; a dependência de `requirements.txt` será usada no build mais adiante.

2. Substitua o workflow por:

   ```yaml
   name: CI

   on:
     push:
       branches: [main]
     workflow_dispatch:

   permissions:
     contents: read

   jobs:
     testar:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
         - uses: actions/setup-python@v6
           with:
             python-version: '3.12'
         - name: Instalar dependências
           run: python -m pip install -r requirements.txt
         - name: Testar
           run: python -m unittest -v
   ```

   Leia de cima para baixo: o push na `main` dispara o workflow, que prepara o código e o Python antes de testar. As etapas do mesmo job executam em sequência. Coloque `'3.12'` entre aspas: é uma versão, não um número decimal.

3. Verifique e publique:

   ```bash
   check.sh 02
   git add .github/workflows/ci.yml
   git commit -m "Automatiza os testes no push"
   gh repo create actions-02 --public --source=. --remote=origin --push
   gh browse --actions
   ```

4. Abra a execução criada pelo **push**. Expanda as etapas e localize os três testes.
5. Edite o título de `cardapio.md`, salve, faça `git add cardapio.md`, `git commit -m "Personaliza o cardápio"` e `git push`. Observe uma nova execução, com outro hash de commit.

## Conceitos para guardar

- `uses`: chama uma action pronta, identificada por repositório e versão.
- `with`: configura as entradas dessa action.
- `run`: executa um comando de shell no runner.
- Checkout baixa o código; o runner não tem os arquivos do seu Codespace.
- Uma instalação no Codespace não prepara o runner; por isso o YAML descreve o ambiente.

## Verificação e entrega

`check.sh 02` deve aprovar. Entregue uma execução verde cujo evento é `push`, com os três testes passando. Explique por que checkout precisa vir antes do comando de testes.

[Próximo: checks no pull request →](../03-checks-no-pull-request/README.md) · [Índice](../../README.md)
