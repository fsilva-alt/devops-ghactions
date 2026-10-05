---
duration: 20
---

# Anotações no pull request

{.lead}
Criar uma verificação para as receitas: um job confere se todas informam o rendimento e, quando uma não informa, marca o arquivo no pull request com uma **anotação** de erro.

`::error file=…` `job validar` `grep -L` `Files changed`

::::columns
:::card Onde fazer
No terminal do Codespace, na pasta do laboratório:

```console
$ cd ~/labs/11-anotacoes-no-pull-request
```

Ponto de partida: o workflow de testes no push e no pull request.
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

Exercício opcional: pode ser feito depois da aula, em qualquer ordem. O laboratório já vem com o ponto de partida.
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
No resumo da execução, em **Annotations**, e no pull request, na aba **Files changed**, ao lado da linha marcada. Quem revisa vê o problema sem abrir o log.
:::
:::card Comandos de workflow
Linhas que começam com `::` são lidas pelo runner como **comandos**, não como texto comum. O mesmo mecanismo cria saídas e resumos, no exercício 12.
:::
::::

:::note A anotação não reprova sozinha.
Quem faz a etapa falhar é o código de saída do comando; aqui, o `test -z` do fim.
:::

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
Sem `needs`, `validar` roda ao mesmo tempo que `testar`. No PR, cada um vira um check: um confere o código; o outro, o conteúdo do livro.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `check.sh 11` | confere o job validar e simula um pull request |
| `grep -L '^Rende:' receitas/*.md` | lista no Codespace as receitas sem rendimento |
| `git switch -c <branch>` | cria a branch da receita nova |
| `gh pr create --base main --fill` | abre o PR para a main |
| `gh pr checks` | mostra os checks testar e validar no terminal |

:::card Documentação
Links para consultar depois. A documentação do GitHub tem versão em português.

{.links}
- [Comandos de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-commands)<small>::error, ::warning, GITHUB\_OUTPUT e GITHUB\_STEP\_SUMMARY</small>
- [Como ler os logs de uma execução](https://docs.github.com/pt/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Comando · gh pr create](https://cli.github.com/manual/gh_pr_create)
- [Comando · gh pr checks](https://cli.github.com/manual/gh_pr_checks)
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Entre no laboratório e abra o workflow:

   ```console
   $ cd ~/labs/11-anotacoes-no-pull-request
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

2. Simule e publique a main:

   ```console
   $ check.sh 11
   ```

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 11"
   $ gh repo create actions-11 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

3. Crie uma branch e uma receita de café **sem** a linha `Rende:`. Crie o arquivo com o conteúdo abaixo e salve:

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

4. Simule: `validar` falha e mostra a anotação. Envie mesmo assim e abra o PR:

   ```console
   $ check.sh 11
   $ git add receitas/cafe.md
   $ git commit -m "Adiciona receita de café"
   $ git push -u origin receita-de-cafe
   $ gh pr create --base main --fill
   $ gh pr view --web
   ```

5. No PR, abra **Files changed**: a anotação aparece na primeira linha de `cafe.md`. Corrija: acrescente a linha abaixo logo depois do título, com uma linha em branco antes e depois. Confira e envie:

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

Aprova com o job `validar`, depois do checkout, gerando `::error file=` para as receitas sem `Rende:`, e com `testar` e `validar` verdes numa simulação de pull request.
:::

:::note
**Entrega:** o link do PR, com a anotação na receita, o check vermelho e o verde depois da correção.
:::

:::card Missão extra · uma observação
```yaml title="acrescente no fim das etapas de validar"
      - name: Contar as receitas
        run: echo "::notice::O livro tem $(ls receitas/*.md | wc -l) receitas."
```

A observação aparece em **Annotations**, em azul, sem reprovar nada.
:::
