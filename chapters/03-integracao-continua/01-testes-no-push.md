---
duration: 25
---

# Testes no push

{.lead}
Fazer o runner baixar o código, instalar o Python e rodar os três testes do livro de receitas a cada push na main.

`on: push` `actions/checkout` `actions/setup-python` `python -m unittest`

::::columns
:::card Onde fazer
```console
$ cd ~/labs/02-testes-no-push
```

O laboratório começa com o workflow manual de boas-vindas e não depende do exercício anterior.
:::
:::card Para este exercício
`⏱ tempo`
: 25 min

`módulo`
: Integração contínua

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
Com o evento `push`, o workflow roda a cada commit enviado para a main. O resultado fica ligado ao commit, e o hash na página da execução mostra qual versão foi testada.

```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:
```

:::card Os testes do livro
`receitas.py` calcula a quantidade de um ingrediente para várias receitas. Um dos testes confere que 3 receitas de pão de queijo, com 500 g de polvilho cada, pedem 1500 g.

```console
$ python3 -m unittest -v
Ran 3 tests in 0.001s
OK
```
:::

:::note O filtro branches
Com `branches: [main]`, só os pushes na main iniciam o workflow. O `workflow_dispatch` mantém o botão Run workflow.
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
O que você instalou no Codespace não aparece no runner, que é outra máquina. Por isso `actions/checkout` baixa os arquivos do repositório, e `actions/setup-python` instala o Python. Depois vêm as dependências e os testes.
:::
::::

:::note Escreva '3.12' entre aspas
Sem as aspas, o YAML lê um número decimal.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `python3 receitas.py` | lista as receitas no terminal do Codespace |
| `python3 -m unittest -v` | roda os três testes no Codespace |
| `git diff` | mostra o que mudou antes do git add |
| `git push` | envia novos commits; na main, dispara o workflow |
| `gh run list` | lista as execuções, com evento e resultado |
| `gh run watch` | acompanha a execução em andamento no terminal |

:::card Documentação
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

   Substitua **todo o conteúdo** pelo YAML abaixo, o mesmo do slide **Preparar o runner**, e salve com <kbd>Ctrl+S</kbd>. Para selecionar o arquivo inteiro antes de colar, use <kbd>Ctrl+A</kbd>.

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

3. Rode a verificação. Os três testes rodam em um container, como no runner:

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

5. Personalize o título do livro em `livro.md`, por exemplo `# Livro de receitas da Ana`. Envie e confira a nova execução, com o hash do novo commit:

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

Aprova quando o workflow roda no `push` da main, faz o checkout antes do Python, instala as dependências antes dos testes e os três testes passam na simulação.
:::

:::note A simulação passou, mas a execução falhou no GitHub?
Abra a etapa vermelha no log. Essa diferença é rara, e o que vale para a entrega é a execução no GitHub.
:::

:::card Missão extra
```yaml title="acrescente no fim de steps"
      - name: Listar receitas
        run: python receitas.py
```

O log da execução passa a mostrar as receitas do livro, lidas da pasta `receitas/` pelo runner.
:::
