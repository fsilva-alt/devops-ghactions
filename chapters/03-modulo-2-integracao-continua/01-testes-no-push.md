---
duration: 25
---

# Testes no push

{.lead}
Fazer o runner baixar o código, instalar o Python e rodar os **três testes** do livro de receitas a cada push na main.

`on: push` `actions/checkout` `actions/setup-python` `python -m unittest`

::::columns
:::card Onde fazer
No terminal do Codespace, na pasta do laboratório:

```console
$ cd ~/labs/02-testes-no-push
```

Ponto de partida: o workflow manual de boas-vindas. Este laboratório é independente do anterior.
:::
:::card Para este exercício
`⏱ tempo`
: 25 min

`módulo`
: Módulo 2 · Integração contínua

`verificação`
: `check.sh 02`

`entrega`
: execução verde disparada por push
:::
::::

<p class="eyebrow">Conceito</p>

## Integração contínua

<div class="flow"><div class="node "><b>git push</b><small>um commit chega à main</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>evento push</b><small>o GitHub cria a execução</small></div><div class="arr"><span class="a">→</span></div><div class="node ok"><b>job testar</b><small>3 testes no runner</small></div></div>

{.lead}
Com `push`, o workflow roda **automaticamente** a cada commit enviado. O resultado fica ligado àquele commit: o hash na página da execução diz exatamente qual versão foi testada.

```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:
```

:::card Os testes do livro
`receitas.py` calcula a quantidade de um ingrediente para várias receitas. Os testes conferem, por exemplo, que **3 receitas** de pão de queijo, com 500 g de polvilho cada, pedem **1500 g**.

```console
$ python3 -m unittest -v
Ran 3 tests in 0.001s
OK
```
:::

:::note
**branches: \[main\]** filtra o evento: só pushes na main iniciam o workflow. Manter `workflow_dispatch` deixa o botão Run workflow disponível.
:::

<p class="eyebrow">Conceito</p>

## Preparar o runner

```yaml title=".github/workflows/ci.yml"
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

::::columns
:::card uses, with e run
| Chave | O que faz |
| --- | --- |
| `uses` | chama uma action pronta; depois do `@` vem a versão |
| `with` | as entradas da action, como a versão do Python |
| `run` | um comando do terminal, executado no runner |
:::
:::card O runner começa vazio
`actions/checkout` baixa os arquivos do repositório. `actions/setup-python` instala o Python pedido. Depois vêm as dependências e, por último, os testes, nessa ordem.
:::
::::

:::note Instalar no Codespace não instala no runner.
São máquinas diferentes. Escreva `'3.12'` entre aspas: sem elas, o YAML lê um número decimal.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `python3 receitas.py` | lista as receitas no terminal do Codespace |
| `python3 -m unittest -v` | roda os três testes no Codespace |
| `check.sh 02` | confere o YAML e roda o job testar em um container |
| `git diff` | mostra o que mudou antes do git add |
| `git push` | envia novos commits; na main, dispara o workflow |
| `gh run list` | lista as execuções, com evento e resultado |
| `gh run watch` | acompanha a execução em andamento no terminal |

:::card Documentação
Links para consultar depois. A documentação do GitHub tem versão em português.

{.links}
- [Integração contínua](https://docs.github.com/pt/actions/get-started/continuous-integration)<small>o que é CI e como o Actions ajuda</small>
- [Eventos que disparam workflows](https://docs.github.com/pt/actions/reference/workflows-and-actions/events-that-trigger-workflows)<small>push, pull\_request, workflow\_dispatch, schedule…</small>
- [Action · actions/checkout](https://github.com/actions/checkout)
- [Action · actions/setup-python](https://github.com/actions/setup-python)
- [Runners hospedados pelo GitHub](https://docs.github.com/pt/actions/concepts/runners/github-hosted-runners)<small>ubuntu-latest e as outras máquinas disponíveis</small>
- [Comando · gh run list](https://cli.github.com/manual/gh_run_list)
:::

<p class="eyebrow">Tarefa · 25 min</p>

## O exercício

:::steps
1. Entre no laboratório, veja as receitas e rode os testes no Codespace. Procure `OK`:

   ```console
   $ cd ~/labs/02-testes-no-push
   $ python3 receitas.py
   $ python3 -m unittest -v
   ```

2. Abra o workflow:

   ```console
   $ code .github/workflows/ci.yml
   ```

   **Substitua todo o conteúdo** pelo YAML abaixo, o mesmo do slide **Preparar o runner**, e salve com <kbd>Ctrl+S</kbd>. Dica: <kbd>Ctrl+A</kbd> seleciona o arquivo inteiro antes de colar.

   ```yaml title=".github/workflows/ci.yml"
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

3. Simule. Os três testes rodam em um container, como no runner:

   ```console
   $ check.sh 02
   ```

4. Publique e abra a execução iniciada pelo `push`. No job `testar`, confira as etapas e os três testes:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 02"
   $ gh repo create actions-02 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

5. Personalize o título do livro em `livro.md`, por exemplo `# Livro de receitas da Ana`. Envie e confira uma nova execução, com o hash do novo commit:

   ```console
   $ code livro.md
   $ git add livro.md
   $ git commit -m "Personaliza o título do livro"
   $ git push
   ```
:::

:::card Verificação
```console
$ check.sh 02
```

Aprova com `push` na main, checkout antes do Python, dependências antes dos testes e os três testes aprovados na simulação.
:::

:::note
**Simulação aprovada e execução com falha no GitHub:** abra a etapa vermelha no log. Diferenças entre o runner local e o do GitHub são raras; a execução considerada na entrega é a do GitHub.
:::

:::card Missão extra
```yaml title="acrescente no fim de steps"
      - name: Listar receitas
        run: python receitas.py
```

O log da execução passa a mostrar as receitas do livro, lidas da pasta `receitas/` pelo runner.
:::
