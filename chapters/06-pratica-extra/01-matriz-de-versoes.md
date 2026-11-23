---
duration: 15
---

# Matriz de versões

{.lead}
Rodar os mesmos testes em **três versões do Python** de uma vez. Uma matriz cria uma cópia do job para cada versão, e o grafo mostra em quais o livro de receitas funciona.

`strategy` `matrix` `fail-fast: false` `${{ matrix.python-version }}`

::::columns
:::card Onde fazer
```console
$ cd ~/labs/08-matriz-de-versoes
```

O laboratório começa com o workflow de testes no push e no pull request, só com o Python 3.12.
:::
:::card Para este exercício
`⏱ tempo`
: 15 min · opcional

`módulo`
: Prática extra · Integração contínua

`verificação`
: `check.sh 08`

`entrega`
: execução com um job testar verde para cada versão

Faça depois da aula, em qualquer ordem.
:::
::::

<p class="eyebrow">Conceito</p>

## Uma cópia do job para cada versão

<div class="flow"><div class="node ok"><b>testar (3.11)</b><small>Python 3.11</small></div><div class="node ok"><b>testar (3.12)</b><small>Python 3.12</small></div><div class="node ok"><b>testar (3.13)</b><small>Python 3.13</small></div></div>

```yaml title="início de jobs.testar"
  testar:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ['3.11', '3.12', '3.13']
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}
```

::::columns
:::card O que a matriz faz
`strategy.matrix` define uma lista de valores. O Actions cria uma cópia do job para cada valor. Todas rodam ao mesmo tempo, cada uma em seu runner.

Em cada cópia, `${{ matrix.python-version }}` vira o valor dela: 3.11, 3.12 ou 3.13.
:::
:::card Por que várias versões?
Quem usa o projeto pode ter outro Python. Com a matriz, o mesmo push mostra em quais versões o código funciona, sem repetir o job no YAML. Uma matriz também pode combinar listas, como versões e sistemas.
:::
::::

:::warning Escreva as versões entre aspas
Sem aspas, o YAML lê `3.10` como o número 3.1, e o setup-python procura uma versão que não existe.
:::

<p class="eyebrow">Conceito</p>

## Quando uma versão falha

::::columns
:::column
### fail-fast: true · o padrão

<div class="flow"><div class="node fail"><b>testar (3.11)</b><small>falhou</small></div><div class="node skip"><b>testar (3.12)</b><small>cancelado</small></div><div class="node skip"><b>testar (3.13)</b><small>cancelado</small></div></div>
:::
:::column
### fail-fast: false

<div class="flow"><div class="node fail"><b>testar (3.11)</b><small>falhou</small></div><div class="node ok"><b>testar (3.12)</b><small>terminou</small></div><div class="node ok"><b>testar (3.13)</b><small>terminou</small></div></div>
:::
::::

::::columns
:::card Cancelar ou terminar?
Por padrão, a primeira falha cancela as cópias que ainda estão rodando, para economizar minutos. Com `fail-fast: false`, todas terminam e você vê quais versões falharam.
:::
:::card Cada cópia vira um check
No grafo e nos pull requests, cada cópia aparece com o valor entre parênteses, como `testar (3.12)`. Uma regra de proteção pode exigir todas verdes.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `gh run watch` | acompanha as cópias ao mesmo tempo no terminal |
| `gh run view` | mostra os jobs da execução, um por versão |

:::card Documentação
{.links}
- [Executar variações de jobs com uma matriz](https://docs.github.com/pt/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)<small>strategy, matrix e fail-fast</small>
- [Action · actions/setup-python](https://github.com/actions/setup-python)
- [Sintaxe de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-syntax)<small>on, jobs, runs-on, steps, needs, if, permissions</small>
- [Comando · gh run view](https://cli.github.com/manual/gh_run_view)<small>--log, --log-failed</small>
:::

<p class="eyebrow">Tarefa · 15 min</p>

## O exercício

:::steps
1. Entre no laboratório e abra o workflow:

   ```console
   $ cd ~/labs/08-matriz-de-versoes
   $ code .github/workflows/ci.yml
   ```

   No job `testar`, acrescente o bloco `strategy` entre `runs-on` e `steps` e troque `'3.12'` por `${{ matrix.python-version }}`. O início do job fica como abaixo, e as outras etapas continuam iguais. Salve:

   ```yaml title="início de jobs.testar"
     testar:
       runs-on: ubuntu-latest
       strategy:
         fail-fast: false
         matrix:
           python-version: ['3.11', '3.12', '3.13']
       steps:
         - uses: actions/checkout@v5
         - uses: actions/setup-python@v6
           with:
             python-version: ${{ matrix.python-version }}
   ```

2. Rode a verificação. Na primeira vez, o act baixa os três Pythons. Cada linha do log mostra a versão entre parênteses:

   ```console
   $ check.sh 08
   ```

3. Publique e abra a execução. No grafo, confira `testar (3.11)`, `testar (3.12)` e `testar (3.13)`:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 08"
   $ gh repo create actions-08 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```
:::

:::card Verificação
```console
$ check.sh 08
```

Aprova quando a matriz tem pelo menos duas versões entre aspas, incluindo a 3.12, e `fail-fast: false`. O setup-python precisa ler `matrix.python-version`, e todas as cópias precisam ficar verdes na simulação.
:::

:::note Entrega
O link da execução com os três jobs `testar` verdes.
:::

:::card Missão extra · uma versão sem aspas
```yaml title="troque a linha da matriz"
        python-version: [3.10, '3.11', '3.12', '3.13']
```

Envie direto com `git commit -am` e `git push`, porque o `check.sh` recusaria a mudança. O job aparece como `testar (3.1)` e falha. Com `fail-fast: false`, as outras versões terminam. Corrija para `'3.10'` e envie de novo.
:::
