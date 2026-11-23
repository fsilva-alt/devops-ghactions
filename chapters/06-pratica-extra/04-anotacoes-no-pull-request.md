---
duration: 20
---

# Anotações no pull request

{.lead}
Criar uma verificação para as receitas. Um job confere se todas informam o rendimento e, quando falta em alguma, marca o arquivo no pull request com uma **anotação** de erro.

`::error file=…` `job validar` `grep -L` `Files changed`

::::columns
:::card Onde fazer
```console
$ code ~/labs/11-anotacoes-no-pull-request
```

O laboratório começa com o workflow de testes no push e no pull request.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min · opcional

`módulo`
: Prática extra · Integração contínua

`verificação`
: `check.sh 11`

`entrega`
: PR com a anotação na receita e o check verde depois da correção

Faça depois da aula, em qualquer ordem.
:::
::::

<p class="eyebrow">Conceito</p>

## Anotações

```text
# Uma linha especial que um step escreve no log:
::error file=receitas/cafe.md,line=1,title=Receita sem rendimento::Acrescente a linha Rende: nesta receita.
```

| Comando | O que faz |
| --- | --- |
| `::error` | marca um erro, em vermelho |
| `::warning` | marca um aviso, em amarelo |
| `::notice` | faz uma observação, em azul |
| `file= line=` | o arquivo e a linha que recebem a marca |
| `title=` | o título curto da anotação |

::::columns
:::card Onde a anotação aparece
Ela aparece no resumo da execução, em **Annotations**, e no pull request, na aba **Files changed**, ao lado da linha marcada. Quem revisa vê o problema sem abrir o log.
:::
:::card Comandos de workflow
O runner lê as linhas que começam com `::` como comandos, e não como texto comum. A anotação só marca o arquivo. Quem faz a etapa falhar é o código de saída do comando, aqui o `test -z` do fim.
:::
::::

<p class="eyebrow">Conceito</p>

## O job validar

```yaml title="dentro de jobs, no mesmo nível de testar"
  validar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: Conferir o rendimento das receitas
        run: |
          faltando=$(grep -L '^Rende:' receitas/*.md || true)
          for arquivo in $faltando; do
            echo "::error file=$arquivo,line=1,title=Receita sem rendimento::Acrescente a linha Rende: nesta receita."
          done
          test -z "$faltando"
```

::::columns
:::card Linha a linha
| Trecho | O que faz |
| --- | --- |
| `grep -L` | lista os arquivos que **não** têm uma linha começando com Rende: |
| `\|\| true` | não deixa o grep encerrar a etapa antes da hora |
| `for … done` | escreve uma anotação para cada arquivo da lista |
| `test -z` | termina com sucesso se a lista estiver vazia; senão, a etapa falha |
:::
:::card Duas verificações em paralelo
Sem `needs`, `validar` roda ao mesmo tempo que `testar`. No PR, cada um vira um check. Um confere o código, e o outro confere o conteúdo do livro.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `grep -L '^Rende:' receitas/*.md` | lista no Codespace as receitas sem rendimento |
| `git switch -c <branch>` | cria a branch da receita nova |
| `gh pr create --base main --fill` | abre o PR para a main |
| `gh pr checks` | mostra os checks testar e validar no terminal |

:::card Documentação
{.links}
- [Comandos de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-commands)<small>::error, ::warning, GITHUB\_OUTPUT e GITHUB\_STEP\_SUMMARY</small>
- [Como ler os logs de uma execução](https://docs.github.com/pt/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Comando · gh pr create](https://cli.github.com/manual/gh_pr_create)
- [Comando · gh pr checks](https://cli.github.com/manual/gh_pr_checks)
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Abra o laboratório no VS Code:

   ```console
   $ code ~/labs/11-anotacoes-no-pull-request
   ```

   Na janela do laboratório, abra um terminal em **Terminal → New Terminal** e abra o workflow:

   ```console
   $ code .github/workflows/ci.yml
   ```

   Cole o job `validar` no **fim do arquivo**, alinhado com `testar:`, dois espaços depois da margem. Salve:

   ```yaml title="acrescente no fim do arquivo, dentro de jobs"
     validar:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
         - name: Conferir o rendimento das receitas
           run: |
             faltando=$(grep -L '^Rende:' receitas/*.md || true)
             for arquivo in $faltando; do
               echo "::error file=$arquivo,line=1,title=Receita sem rendimento::Acrescente a linha Rende: nesta receita."
             done
             test -z "$faltando"
   ```

2. Rode a verificação e publique a main:

   ```console
   $ check.sh 11
   ```

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 11"
   $ gh repo create actions-11 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

3. Crie uma branch e uma receita de café sem a linha `Rende:`. Use o conteúdo abaixo e salve:

   ```console
   $ git switch -c receita-de-cafe
   $ code receitas/cafe.md
   ```

   ```markdown title="receitas/cafe.md"
   # Café coado

   ## Ingredientes

   - 2 colheres de sopa de café em pó
   - 500 ml de água

   ## Modo de preparo

   1. Aqueça a água sem deixar ferver.
   2. Passe a água pelo filtro com o café.
   ```

4. Rode a verificação. `validar` falha e mostra a anotação. Envie mesmo assim e abra o PR:

   ```console
   $ check.sh 11
   $ git add receitas/cafe.md
   $ git commit -m "Adiciona receita de café"
   $ git push -u origin receita-de-cafe
   $ gh pr create --base main --fill
   $ gh pr view --web
   ```

5. No PR, abra **Files changed**. A anotação aparece na primeira linha de `cafe.md`. Para corrigir, acrescente a linha abaixo logo depois do título, com uma linha em branco antes e depois. Rode a verificação e envie:

   ```markdown title="linha nova em receitas/cafe.md"
   Rende: 4 xícaras
   ```

   ```console
   $ check.sh 11
   $ git add receitas/cafe.md
   $ git commit -m "Informa o rendimento do café"
   $ git push
   ```
:::

:::card Verificação
```console
$ check.sh 11
```

Aprova quando o job `validar` faz o checkout e gera `::error file=` para as receitas sem `Rende:`, e `testar` e `validar` ficam verdes em uma simulação de pull request.
:::

:::note Entrega
O link do PR, com a anotação na receita, o check vermelho e o verde depois da correção.
:::

:::card Missão extra · uma observação
```yaml title="acrescente no fim das etapas de validar"
      - name: Contar as receitas
        run: echo "::notice::O livro tem $(ls receitas/*.md | wc -l) receitas."
```

A observação aparece em **Annotations**, em azul, sem reprovar nada.
:::
