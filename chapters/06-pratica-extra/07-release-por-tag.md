---
duration: 20
---

# Release por tag

{.lead}
Publicar versões numeradas do livro. Quando você envia uma tag como `v1.0.0`, o workflow testa, gera o site e cria um **release** no GitHub, com o site compactado para baixar.

`tags: ['v*']` `git tag v1.0.0` `actions/download-artifact` `gh release create`

::::columns
:::card Onde fazer
```console
$ code ~/labs/14-release-por-tag
```

O laboratório começa com o workflow do artefato `site`, do exercício 6.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min · opcional

`módulo`
: Prática extra · Entrega contínua

`verificação`
: `check.sh 14`

`entrega`
: release v1.0.0 com o site compactado

Faça depois da aula, em qualquer ordem.
:::
::::

<p class="eyebrow">Conceito</p>

## Tags e releases

<div class="flow"><div class="node "><b>git tag v1.0.0</b><small>um nome fixo para o commit</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>push da tag</b><small>evento push · refs/tags/v1.0.0</small></div><div class="arr"><span class="a">→</span></div><div class="node ok"><b>testar → empacotar → lancar</b><small>os três jobs</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>release v1.0.0</b><small>notas + livro-de-receitas.zip</small></div></div>

::::columns
:::card Tag
É um nome fixo para um commit, como `v1.0.0`. Diferente de uma branch, a tag não muda quando chegam novos commits.
:::
:::card Release
É a página de uma versão no GitHub, com notas e arquivos para baixar. A opção `--generate-notes` escreve as notas a partir dos commits e PRs desde a versão anterior.
:::
:::card O filtro de tags
```yaml title="substitua só o bloco on"
on:
  push:
    branches: [main]
    tags: ['v*']
  pull_request:
    branches: [main]
  workflow_dispatch:
```

Com `branches` e `tags`, o workflow roda nos pushes para a main e também nos pushes de tags que começam com `v`.
:::
::::

<p class="eyebrow">Conceito</p>

## Quando o job lancar roda

```yaml title="o último job do workflow"
  lancar:
    needs: empacotar
    if: startsWith(github.ref, 'refs/tags/v')
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: site
          path: site
      - name: Compactar o site
        run: zip -r livro-de-receitas.zip site
      - name: Criar o release
        env:
          GH_TOKEN: ${{ github.token }}
        run: gh release create "$GITHUB_REF_NAME" livro-de-receitas.zip --repo "$GITHUB_REPOSITORY" --generate-notes
```

::::columns
:::card A condição
`startsWith(github.ref, 'refs/tags/v')` só é verdadeira no push de uma tag que começa com `v`. Em um push na main, `testar` e `empacotar` rodam, e `lancar` fica de fora.
:::
:::card Permissão de escrita só no lancar
Criar um release escreve no repositório, por isso só `lancar` recebe `contents: write`. O `GITHUB_TOKEN` da execução chega ao `gh` pela variável `GH_TOKEN`.
:::
:::card O artefato entre jobs
`lancar` roda em outro runner. Por isso `actions/download-artifact` baixa o `site` guardado por `empacotar`, o mesmo artefato do exercício 6.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `git tag v1.0.0` | cria a tag no commit atual |
| `git push origin v1.0.0` | envia a tag e dispara o workflow |
| `gh release view v1.0.0 --web` | abre o release no navegador |
| `gh release download v1.0.0` | baixa os arquivos do release |

:::card Documentação
{.links}
- [Sobre releases](https://docs.github.com/pt/repositories/releasing-projects-on-github/about-releases)<small>versões com notas e arquivos para baixar</small>
- [Comando · gh release create](https://cli.github.com/manual/gh_release_create)<small>--generate-notes, arquivos anexos</small>
- [Comando · gh release view](https://cli.github.com/manual/gh_release_view)
- [Action · actions/download-artifact](https://github.com/actions/download-artifact)
- [O GITHUB\_TOKEN](https://docs.github.com/pt/actions/concepts/security/github_token)<small>a credencial de cada execução e o bloco permissions</small>
- [Contextos](https://docs.github.com/pt/actions/reference/workflows-and-actions/contexts)<small>github, env, inputs, vars, secrets, steps</small>
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Abra o laboratório no VS Code:

   ```console
   $ code ~/labs/14-release-por-tag
   ```

   Na janela do laboratório, abra um terminal em **Terminal → New Terminal** e abra o workflow:

   ```console
   $ code .github/workflows/ci.yml
   ```

   Troque o bloco `on` pelo bloco abaixo, que acrescenta as tags:

   ```yaml title="substitua só o bloco on"
   on:
     push:
       branches: [main]
       tags: ['v*']
     pull_request:
       branches: [main]
     workflow_dispatch:
   ```

2. Cole o job `lancar` no **fim do arquivo**, alinhado com `testar:` e `empacotar:`. Salve:

   ```yaml title="acrescente no fim do arquivo, dentro de jobs"
     lancar:
       needs: empacotar
       if: startsWith(github.ref, 'refs/tags/v')
       runs-on: ubuntu-latest
       permissions:
         contents: write
       steps:
         - uses: actions/download-artifact@v4
           with:
             name: site
             path: site
         - name: Compactar o site
           run: zip -r livro-de-receitas.zip site
         - name: Criar o release
           env:
             GH_TOKEN: ${{ github.token }}
           run: gh release create "$GITHUB_REF_NAME" livro-de-receitas.zip --repo "$GITHUB_REPOSITORY" --generate-notes
   ```

3. Rode a verificação. Em um push na main, só `testar` e `empacotar` rodam:

   ```console
   $ check.sh 14
   ```

4. Publique. Na execução da main, `lancar` aparece como pulado:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 14"
   $ gh repo create actions-14 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

5. Crie a tag `v1.0.0` e envie. Acompanhe os três jobs e abra o release:

   ```console
   $ git tag v1.0.0
   $ git push origin v1.0.0
   $ gh run watch
   $ gh release view v1.0.0 --web
   ```
:::

:::card Verificação
```console
$ check.sh 14
```

Aprova quando o push tem `tags` com `v*` e o job `lancar` tem `needs: empacotar`, a condição da tag, `contents: write` só nele e `gh release create` com `GH_TOKEN`. Na simulação de um push na main, `lancar` precisa ficar de fora.
:::

:::note Entrega
O link do release `v1.0.0`, com o arquivo `livro-de-receitas.zip`.
:::

:::card Missão extra · a versão 1.1.0
Acrescente uma receita em `receitas/`, faça o commit e envie com uma nova tag:

```console
$ git push
$ git tag v1.1.0
$ git push origin v1.1.0
```

As notas do release `v1.1.0` listam só o que mudou desde a `v1.0.0`.
:::
