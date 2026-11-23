---
duration: 20
---

# Saídas e resumo

{.lead}
Passar um valor de um job para outro e escrever um **resumo** na página da execução, com o número de receitas e a lista do livro.

`$GITHUB_OUTPUT` `jobs.<job>.outputs` `needs.contar.outputs.total` `$GITHUB_STEP_SUMMARY`

::::columns
:::card Onde fazer
```console
$ code ~/labs/12-saidas-e-resumo
```

O laboratório começa com o workflow de testes no push e no pull request.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min · opcional

`módulo`
: Prática extra · Jobs

`verificação`
: `check.sh 12`

`entrega`
: execução com o resumo do livro, com 4 receitas

Faça depois da aula, em qualquer ordem.
:::
::::

<p class="eyebrow">Conceito</p>

## Como um valor passa de um job para outro

<div class="flow"><div class="node "><b>step contagem</b><small>escreve total=3 em $GITHUB_OUTPUT</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>job contar</b><small>outputs.total</small></div><div class="arr"><span class="a">→</span></div><div class="node ok"><b>job resumo</b><small>lê needs.contar.outputs.total</small></div></div>

| Expressão | Onde vale |
| --- | --- |
| `steps.<id>.outputs` | a saída de um step, lida no mesmo job; o step precisa de um id |
| `jobs.<job>.outputs` | o que o job oferece aos jobs seguintes |
| `needs.<job>.outputs` | a leitura, num job que espera o outro com needs |

::::columns
:::card $GITHUB\_OUTPUT é um arquivo
Cada linha `nome=valor` escrita nele vira uma saída do step. O `id: contagem` dá o nome usado em `steps.contagem.outputs.total`.
:::
:::card Por que needs?
Os jobs rodam em runners diferentes, e a variável de um não aparece no outro. O `resumo` lê a saída de `contar` porque espera por ele. Com `needs: [testar, contar]`, ele espera os dois, que rodam em paralelo.
:::
::::

<p class="eyebrow">Conceito</p>

## O resumo da execução

```text
# Em Summary, na página da execução, abaixo do grafo:
O livro tem 3 receitas.
Livro de receitas
• Bolo de cenoura (rende 8 porções)
• Brigadeiro (rende 30 unidades)
• Pão de queijo (rende 25 unidades)
```

<div class="flow"><div class="node "><b>testar + contar</b><small>em paralelo</small></div><div class="arr"><span class="a">→</span>needs</div><div class="node hi"><b>resumo</b><small>espera os dois</small></div></div>

::::columns
:::card $GITHUB\_STEP\_SUMMARY
O que um step escreve nesse arquivo aparece na página da execução, formatado como Markdown. Títulos, listas e tabelas funcionam.
:::
:::card O que o run escreve
O `tee -a` mostra a frase no log e também a acrescenta ao resumo. A saída do `receitas.py` já é Markdown, com um título sublinhado com `=` e uma lista com `-`, e vai direto para o arquivo.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `ls receitas/*.md \| wc -l` | conta as receitas no Codespace, como o job contar |
| `python3 receitas.py` | mostra a lista que vai para o resumo |
| `gh run view --web` | abre a execução escolhida no navegador, com o resumo |

:::card Documentação
{.links}
- [Passar informações entre jobs](https://docs.github.com/pt/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs)<small>outputs no job e needs nos jobs seguintes</small>
- [Comandos de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-commands)<small>::error, ::warning, GITHUB\_OUTPUT e GITHUB\_STEP\_SUMMARY</small>
- [Contextos](https://docs.github.com/pt/actions/reference/workflows-and-actions/contexts)<small>steps e needs, com as saídas de steps e jobs</small>
- [Como usar jobs em um workflow](https://docs.github.com/pt/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs)<small>needs e jobs em paralelo</small>
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Abra o laboratório no VS Code:

   ```console
   $ code ~/labs/12-saidas-e-resumo
   ```

   Na janela do laboratório, abra um terminal em **Terminal → New Terminal** e abra o workflow:

   ```console
   $ code .github/workflows/ci.yml
   ```

   Cole os jobs `contar` e `resumo` no **fim do arquivo**, alinhados com `testar:`. Salve:

   ```yaml title="acrescente no fim do arquivo, dentro de jobs"
     contar:
       runs-on: ubuntu-latest
       outputs:
         total: ${{ steps.contagem.outputs.total }}
       steps:
         - uses: actions/checkout@v5
         - name: Contar as receitas
           id: contagem
           run: echo "total=$(ls receitas/*.md | wc -l)" >> "$GITHUB_OUTPUT"
     resumo:
       needs: [testar, contar]
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
         - name: Escrever o resumo da execução
           env:
             TOTAL: ${{ needs.contar.outputs.total }}
           run: |
             echo "O livro tem $TOTAL receitas." | tee -a "$GITHUB_STEP_SUMMARY"
             python3 receitas.py >> "$GITHUB_STEP_SUMMARY"
   ```

2. Rode a verificação e procure **O livro tem 3 receitas.** no log do job `resumo`:

   ```console
   $ check.sh 12
   ```

3. Publique. No grafo, `testar` e `contar` rodam juntos e `resumo` espera os dois. Abra a execução e role até o resumo:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 12"
   $ gh repo create actions-12 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

   ```console
   $ gh run view --web
   ```

4. Acrescente uma receita de limonada. Crie o arquivo com o conteúdo abaixo e salve:

   ```console
   $ code receitas/limonada.md
   ```

   ```markdown title="receitas/limonada.md"
   # Limonada

   Rende: 4 copos

   ## Ingredientes

   - 2 limões
   - 1 litro de água gelada
   - Açúcar a gosto

   ## Modo de preparo

   1. Bata os limões com casca e a água no liquidificador.
   2. Coe, adoce e sirva.
   ```

5. Rode a verificação e envie. O resumo da nova execução mostra 4 receitas:

   ```console
   $ check.sh 12
   $ git add receitas/limonada.md
   $ git commit -m "Adiciona receita de limonada"
   $ git push
   ```
:::

:::card Verificação
```console
$ check.sh 12
```

Aprova quando o job `contar` expõe em `outputs` a saída `total` do step `contagem`, e o job `resumo` lê `needs.contar.outputs.total` e escreve em `$GITHUB_STEP_SUMMARY`. A frase também precisa aparecer no log da simulação.
:::

:::note Entrega
O link da execução com o resumo das 4 receitas.
:::

:::card Missão extra · a data no resumo
```text title="acrescente no fim do run do resumo"
          echo "Gerado em $(date +%d/%m/%Y)." >> "$GITHUB_STEP_SUMMARY"
```

A linha fica alinhada com as outras duas do `run`. A data é a do runner, em UTC.
:::
