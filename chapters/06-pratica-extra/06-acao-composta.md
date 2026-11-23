---
duration: 20
---

# Ação composta

{.lead}
Tirar a repetição do workflow. As etapas que preparam o Python nos dois jobs viram uma **ação composta** do próprio repositório, chamada com uma linha de `uses`.

`.github/actions/preparar/action.yml` `runs.using: composite` `shell: bash` `uses: ./.github/actions/preparar`

::::columns
:::card Onde fazer
```console
$ cd ~/labs/13-acao-composta
```

O laboratório começa com o workflow de `testar` e `empacotar` do exercício 5, que repete o preparo do Python.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min · opcional

`módulo`
: Prática extra · Reaproveitamento

`verificação`
: `check.sh 13`

`entrega`
: execução verde com os dois jobs usando a ação preparar

Faça depois da aula, em qualquer ordem.
:::
::::

<p class="eyebrow">Conceito</p>

## Uma action feita por você

```yaml title=".github/actions/preparar/action.yml"
name: Preparar o livro
description: Instala o Python 3.12 e as dependências do livro de receitas

runs:
  using: composite
  steps:
    - uses: actions/setup-python@v6
      with:
        python-version: '3.12'
    - name: Instalar dependências
      shell: bash
      run: python -m pip install -r requirements.txt
```

::::columns
:::card As chaves do action.yml
| Chave | O que define |
| --- | --- |
| `name · description` | o nome e a descrição da ação; os dois são obrigatórios |
| `runs.using: composite` | a ação é uma lista de etapas |
| `steps` | as etapas, escritas como num job |
| `shell: bash` | obrigatório em cada run de uma ação composta |
:::
:::card Ação composta ou workflow reutilizável?
Uma ação composta junta **etapas**, usadas dentro de um job. Um workflow reutilizável, com `workflow_call`, junta **jobs** inteiros.
:::
::::

:::warning Todo run precisa de shell
Em uma ação composta, um `run` sem `shell` é erro, porque o arquivo da ação não herda o shell padrão do job.
:::

<p class="eyebrow">Conceito</p>

## Chamar a ação no job

<div class="flow"><div class="node "><b>actions/checkout</b><small>baixa o repositório, com a pasta da ação</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>./.github/actions/preparar</b><small>setup-python + pip install</small></div><div class="arr"><span class="a">→</span></div><div class="node ok"><b>testes ou build</b><small>como antes</small></div></div>

```yaml title="as etapas do job testar"
      - uses: actions/checkout@v5
      - uses: ./.github/actions/preparar
      - run: python -m unittest -v
```

::::columns
:::card Primeiro o checkout
`uses: ./…` aponta para uma pasta do repositório. Ela só existe no runner depois do `actions/checkout`.
:::
:::card A versão do Python fica em um arquivo só
Para trocar a versão do Python, edite só o `action.yml`, e os dois jobs passam a usar a nova versão.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `mkdir -p .github/actions/preparar` | cria a pasta da ação |
| `code .github/actions/preparar/action.yml` | abre o arquivo da ação no editor |
| `git add .github` | prepara o workflow e a ação para o commit |

:::card Documentação
{.links}
- [Criar uma ação composta](https://docs.github.com/pt/actions/tutorials/create-actions/create-a-composite-action)<small>action.yml com runs.using: composite</small>
- [Sintaxe de metadados de actions](https://docs.github.com/pt/actions/reference/workflows-and-actions/metadata-syntax)<small>name, description, runs e shell</small>
- [Action · actions/setup-python](https://github.com/actions/setup-python)
- [Sintaxe de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-syntax)<small>on, jobs, runs-on, steps, needs, if, permissions</small>
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Entre no laboratório, crie a pasta da ação e abra o arquivo dela:

   ```console
   $ cd ~/labs/13-acao-composta
   $ mkdir -p .github/actions/preparar
   $ code .github/actions/preparar/action.yml
   ```

   Copie o conteúdo abaixo para o editor e salve:

   ```yaml title=".github/actions/preparar/action.yml"
   name: Preparar o livro
   description: Instala o Python 3.12 e as dependências do livro de receitas

   runs:
     using: composite
     steps:
       - uses: actions/setup-python@v6
         with:
           python-version: '3.12'
       - name: Instalar dependências
         shell: bash
         run: python -m pip install -r requirements.txt
   ```

2. Abra o workflow e substitua o bloco `jobs` pelo bloco abaixo. Nos dois jobs, o setup-python e a instalação viram uma única etapa. Mantenha `name`, `on` e `permissions` e salve:

   ```console
   $ code .github/workflows/ci.yml
   ```

   ```yaml title="substitua o bloco jobs"
   jobs:
     testar:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
         - uses: ./.github/actions/preparar
         - run: python -m unittest -v
     empacotar:
       needs: testar
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
         - uses: ./.github/actions/preparar
         - run: python build.py
         - name: Conferir o arquivo gerado
           run: test -s dist/index.html
   ```

3. Rode a verificação. Os dois jobs rodam a ação e terminam verdes:

   ```console
   $ check.sh 13
   ```

4. Publique. Desta vez, o commit leva a pasta `.github` inteira, com o workflow e a ação:

   ```console
   $ git add .github
   $ git commit -m "Configura workflow do exercício 13"
   $ gh repo create actions-13 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```
:::

:::card Verificação
```console
$ check.sh 13
```

Aprova quando a ação composta tem o setup-python 3.12 e a instalação com `shell: bash`, e os dois jobs chamam `./.github/actions/preparar` depois do checkout, sem repetir o setup-python. Os dois jobs precisam ficar verdes na simulação.
:::

:::note Entrega
O link da execução verde. No log, a etapa **Run ./.github/actions/preparar** mostra as etapas internas da ação.
:::

:::card Missão extra · cache nos dois jobs
```yaml title="acrescente ao with do setup-python, em action.yml"
        cache: pip
```

A linha fica alinhada com `python-version`. Envie a mudança. Os dois jobs passam a usar o cache do exercício 9, sem nenhuma alteração no workflow.
:::
