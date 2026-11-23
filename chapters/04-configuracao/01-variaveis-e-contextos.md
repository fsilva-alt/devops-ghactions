---
duration: 20
---

# Variáveis e contextos

{.lead}
Configurar uma execução com valores que vêm do YAML, do formulário do Run workflow, da própria execução e das configurações do repositório. Um deles é um **segredo**, que nunca aparece no log.

`env` `inputs` `github.actor` `vars` `secrets` `gh secret set`

::::columns
:::card Onde fazer
```console
$ code ~/labs/04-variaveis-e-contextos
```

É uma demonstração isolada, em que o workflow mostra a receita do dia da cozinha.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min

`módulo`
: Configuração

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

:::card Os cinco contextos
| Contexto | De onde vem |
| --- | --- |
| `env` | definido no próprio YAML, como o nome da cozinha |
| `inputs` | digitado no formulário do Run workflow |
| `github` | informações da execução: quem iniciou, branch, commit |
| `vars` | variável cadastrada nas configurações do repositório |
| `secrets` | valor sensível cadastrado no repositório |
:::

:::note Duas sintaxes
O Actions troca `${{ … }}` pelo valor antes de rodar a etapa. O shell lê `$VARIAVEL` durante a execução. Quando o input passa por `env`, o shell trata o valor como texto, mesmo que ele tenha aspas.
:::

<p class="eyebrow">Conceito</p>

## Como usar um segredo

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
O segredo não fica no YAML nem no histórico do Git. Ele só chega às etapas que o pedem por `env`, e o GitHub troca o valor por `***` se ele aparecer no log.
:::

:::warning Um segredo que não existe vira texto vazio
O Actions não dá erro nesse caso. Por isso a etapa usa `test -n`, que confere se o valor não está vazio sem mostrar o valor, e falha com uma dica. No curso, o segredo é fictício e vale `somente-demonstracao`.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `cp "$CURSO_DIR/docs/solucoes/04.yml" .github/workflows/ci.yml` | copia o workflow completo do exercício |
| `gh variable set TURMA --body "<turma>"` | cadastra a variável do repositório |
| `gh secret set CURSO_TOKEN --body "<valor>"` | cadastra o segredo do repositório |
| `gh workflow run "<workflow>" -f receita="<receita>"` | inicia o workflow manual pelo terminal |
| `gh run watch` | acompanha a execução no terminal |

:::card Documentação
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
1. Abra o laboratório no VS Code:

   ```console
   $ code ~/labs/04-variaveis-e-contextos
   ```

   Na janela do laboratório, abra um terminal em **Terminal → New Terminal** e copie o workflow completo do exercício:

   ```console
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

   Salve e rode a verificação. O log mostra a cozinha, a receita e a turma local:

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

5. Em **Actions → Variáveis e contextos → Run workflow**, digite uma receita e rode na `main`. No log, confira a cozinha, a receita, o autor e a turma. A mensagem do segredo aparece sem o valor.
:::

:::card Verificação
```console
$ check.sh 04
```

Aprova quando o workflow tem o input `receita`, `env.COZINHA` e as referências a `inputs`, `github`, `vars` e `secrets` passadas por `env`. A simulação usa valores locais de demonstração.
:::

:::note A última etapa falhou no GitHub?
Confira o nome `CURSO_TOKEN` e se ele foi cadastrado neste repositório, `actions-04`.
:::

:::card Missão extra
```console
$ gh workflow run "Variáveis e contextos" -f receita="Bolo de cenoura"
$ gh run watch
```

É o mesmo Run workflow, feito pelo terminal. O `-f` preenche o input do formulário.
:::
