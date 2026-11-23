---
duration: 20
---

# Artefatos do build

{.lead}
Guardar o site gerado pelo build como um **artefato** da execução, baixar esse artefato e conferir que cada commit produz o seu próprio resultado.

`actions/upload-artifact` `name: site` `path: dist/` `gh run download`

::::columns
:::card Onde fazer
```console
$ cd ~/labs/06-artefatos-do-build
```

O laboratório começa com o workflow dos jobs `testar` e `empacotar`.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min

`módulo`
: Entrega contínua

`verificação`
: `check.sh 06`

`entrega`
: artefato site com a receita nova
:::
::::

<p class="eyebrow">Conceito</p>

## Guardar o resultado

<div class="flow"><div class="node "><b>python build.py</b><small>gera dist/</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>upload-artifact</b><small>compacta e envia</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>artefato site</b><small>ZIP ligado à execução</small></div></div>

```yaml title="última etapa de jobs.empacotar.steps"
      - name: Guardar o site
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: dist/
          if-no-files-found: error
          retention-days: 7
```

:::card O que é um artefato
É um arquivo ou uma pasta que a execução guarda depois que o runner é descartado, como um site ou um relatório. Ele aparece em **Artifacts**, no resumo da execução.
:::

| Entrada | O que define |
| --- | --- |
| `name` | o nome do artefato na página da execução |
| `path` | o que enviar; aqui, a pasta do site |
| `if-no-files-found` | error faz a etapa falhar se a pasta estiver vazia |
| `retention-days` | por quantos dias guardar |

<p class="eyebrow">Conceito</p>

## Artefato, cache e deploy

::::columns
:::card Artefato
É o resultado de uma execução, para baixar ou passar a outro job. O artefato de um commit antigo continua disponível até expirar.
:::
:::card Cache
São arquivos guardados para acelerar as próximas execuções, como dependências já baixadas. Pode ser apagado a qualquer momento, então não serve como entrega.
:::
:::card Deploy
É a publicação do resultado no destino final, como um site no ar. Guardar o ZIP ainda não publica nada. O deploy fica para o exercício 7.
:::
::::

| Etapa | Para quê | Neste curso |
| --- | --- | --- |
| `Build` | gera os arquivos | python build.py |
| `Artefato` | guarda os arquivos | actions/upload-artifact |
| `Deploy` | disponibiliza aos usuários | actions/deploy-pages |

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `python3 receitas.py` | confere as receitas que vão para o site |
| `gh run list` | lista as execuções, para achar a mais recente |
| `gh run download --name site --dir site-baixado` | baixa o artefato da execução escolhida |
| `unzip <arquivo>.zip` | descompacta um ZIP baixado pelo navegador |

:::card Documentação
{.links}
- [Artefatos de workflow](https://docs.github.com/pt/actions/concepts/workflows-and-actions/workflow-artifacts)<small>guardar e baixar arquivos de uma execução</small>
- [Action · actions/upload-artifact](https://github.com/actions/upload-artifact)<small>name, path, retention-days</small>
- [Comando · gh run download](https://cli.github.com/manual/gh_run_download)
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Entre no laboratório e abra o workflow:

   ```console
   $ cd ~/labs/06-artefatos-do-build
   $ code .github/workflows/ci.yml
   ```

   Cole a etapa abaixo no **fim do arquivo**, depois de `python build.py`, que é a última etapa de `empacotar`. O traço fica alinhado com os das outras etapas, seis espaços depois da margem. Salve:

   ```yaml title="acrescente no fim das etapas de empacotar"
         - name: Guardar o site
           uses: actions/upload-artifact@v4
           with:
             name: site
             path: dist/
             if-no-files-found: error
             retention-days: 7
   ```

2. Rode a verificação e procure a linha **artefato site: index.html**:

   ```console
   $ check.sh 06
   ```

3. Publique. No resumo da execução, em **Artifacts → site**, baixe o ZIP e abra o `index.html`:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 06"
   $ gh repo create actions-06 --public --source=. --remote=origin --push
   $ gh browse --actions
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

5. Rode a verificação e envie. Depois, baixe o artefato da nova execução e procure a limonada:

   ```console
   $ python3 receitas.py
   $ check.sh 06
   $ git add receitas/limonada.md
   $ git commit -m "Adiciona receita de limonada"
   $ git push
   ```
:::

:::card Verificação
```console
$ check.sh 06
```

Aprova quando o upload de `dist/` como `site` vem depois do build, com `if-no-files-found: error` e `retention-days: 7`, e o artefato da simulação contém `index.html`.
:::

:::note Entrega
O link da execução final e a confirmação de que o artefato `site` traz a limonada.
:::

:::card Missão extra
```console
$ gh run download --name site --dir site-baixado
$ ls site-baixado
```

O comando baixa o artefato direto no Codespace. Escolha a execução na lista. Depois, apague a pasta, para ela não entrar no próximo commit.
:::
