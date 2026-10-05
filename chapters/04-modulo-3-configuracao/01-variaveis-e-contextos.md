---
duration: 20
---

# Variáveis e contextos

{.lead}
Configurar uma execução com valores vindos de lugares diferentes: o YAML, o formulário do Run workflow, a própria execução e as configurações do repositório, incluindo um **segredo** que nunca aparece no log.

`env` `inputs` `github.actor` `vars` `secrets` `gh secret set`

::::columns
:::card Onde fazer
No terminal do Codespace, na pasta do laboratório:

```console
$ cd ~/labs/04-variaveis-e-contextos
```

Uma demonstração isolada: o workflow apresenta a receita do dia da cozinha.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min

`módulo`
: Módulo 3 · Configuração

`verificação`
: `check.sh 04`

`entrega`
: execução manual com a sua receita do dia
:::
::::

<p class="eyebrow">Conceito</p>

## De onde vêm os valores

```yaml title="trechos do workflow"
on:
  workflow_dispatch:
    inputs:
      receita:
        description: Receita do dia
        type: string
        default: Brigadeiro

env:
  COZINHA: Cozinha do Curso

# Na etapa:
    env:
      RECEITA: ${{ inputs.receita }}
      AUTOR: ${{ github.actor }}
      TURMA: ${{ vars.TURMA }}
    run: |
      printf 'Cozinha: %s\nReceita do dia: %s\n' "$COZINHA" "$RECEITA"
```

:::card Cinco origens
| Contexto | De onde vem |
| --- | --- |
| `env` | definido no próprio YAML, como o nome da cozinha |
| `inputs` | digitado no formulário do Run workflow |
| `github` | informações da execução: quem iniciou, branch, commit |
| `vars` | variável cadastrada nas configurações do repositório |
| `secrets` | valor sensível cadastrado no repositório |
:::

:::note
**Duas sintaxes:** o Actions troca `${{ … }}` pelo valor antes de rodar a etapa; o shell lê `$VARIAVEL` durante a execução. Passar o input por `env` faz o shell tratá-lo como texto, mesmo com aspas.
:::

<p class="eyebrow">Conceito</p>

## Segredos sem vazamento

```yaml title="última etapa do job"
      - name: Verificar segredo sem exibir o valor
        env:
          TOKEN_DEMO: ${{ secrets.CURSO_TOKEN }}
        run: |
          test -n "$TOKEN_DEMO" || { echo "Cadastre CURSO_TOKEN"; exit 1; }
          echo "Segredo disponível para esta etapa."
```

:::card Vars ou secrets?
Os dois são cadastrados em **Settings → Secrets and variables → Actions**. Use `vars` para configurações comuns, como o nome da turma, e `secrets` para senhas e tokens.
:::

:::card O que protege um segredo
Ele não fica no YAML nem no histórico do Git. Só chega às etapas que o pedem por `env`, e o GitHub troca seu valor por `***` se ele aparecer no log.

`test -n` confere se o valor não está vazio, sem imprimi-lo.
:::

:::warning
**Segredo ausente não dá erro:** vira texto vazio. Por isso a etapa testa o valor e falha com uma dica. No curso, o segredo é fictício: `somente-demonstracao`.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `cp "$CURSO_DIR/docs/solucoes/04.yml" .github/workflows/ci.yml` | copia o workflow completo do exercício |
| `check.sh 04` | confere o YAML e simula com TURMA e CURSO\_TOKEN de demonstração |
| `gh variable set TURMA --body "<turma>"` | cadastra a variável do repositório |
| `gh secret set CURSO_TOKEN --body "<valor>"` | cadastra o segredo do repositório |
| `gh workflow run "<workflow>" -f receita="<receita>"` | inicia o workflow manual pelo terminal |
| `gh run watch` | acompanha a execução no terminal |

:::card Documentação
Links para consultar depois. A documentação do GitHub tem versão em português.

{.links}
- [Contextos](https://docs.github.com/pt/actions/reference/workflows-and-actions/contexts)<small>github, env, inputs, vars, secrets, steps</small>
- [Variáveis](https://docs.github.com/pt/actions/reference/workflows-and-actions/variables)<small>env no YAML e vars do repositório</small>
- [Como usar segredos](https://docs.github.com/pt/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
- [Comando · gh variable set](https://cli.github.com/manual/gh_variable_set)
- [Comando · gh secret set](https://cli.github.com/manual/gh_secret_set)
- [Comando · gh workflow run](https://cli.github.com/manual/gh_workflow_run)<small>-f para preencher os inputs</small>
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Entre no laboratório e copie o workflow completo do exercício:

   ```console
   $ cd ~/labs/04-variaveis-e-contextos
   $ cp "$CURSO_DIR/docs/solucoes/04.yml" .github/workflows/ci.yml
   $ code .github/workflows/ci.yml
   ```

2. No editor, procure o trecho abaixo e troque `Brigadeiro` pela sua receita favorita. Localize também `env.COZINHA`, logo depois de `permissions`:

   ```yaml title="trecho de .github/workflows/ci.yml"
         receita:
           description: Receita do dia
           required: true
           type: string
           default: Brigadeiro
   ```

   Salve e simule; o log mostra a cozinha, a receita e a turma local:

   ```console
   $ check.sh 04
   ```

3. Publique o laboratório:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 04"
   $ gh repo create actions-04 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

4. Cadastre a variável e o segredo fictício no repositório. Os comandos usam o repositório da pasta atual:

   ```console
   $ gh variable set TURMA --body "turma-de-actions"
   $ gh secret set CURSO_TOKEN --body "somente-demonstracao"
   ```

5. Em **Actions → Variáveis e contextos → Run workflow**, digite uma receita e execute na `main`. No log, confira cozinha, receita, autor e turma, e a mensagem do segredo, sem o valor.
:::

:::card Verificação
```console
$ check.sh 04
```

Aprova com o input `receita`, `env.COZINHA` e as referências a `inputs`, `github`, `vars` e `secrets` passadas por `env`. A simulação usa valores locais de demonstração.
:::

:::note A última etapa falhou no GitHub?
Confira o nome `CURSO_TOKEN` e se ele foi cadastrado neste repositório, `actions-04`.
:::

:::card Missão extra
```console
$ gh workflow run "Variáveis e contextos" -f receita="Bolo de cenoura"
$ gh run watch
```

O mesmo Run workflow, pelo terminal. `-f` preenche o input do formulário.
:::
