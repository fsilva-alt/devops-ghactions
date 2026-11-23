---
duration: 30
---

# Deploy no Pages

{.lead}
Publicar o livro de receitas no **GitHub Pages** com um workflow que testa, gera e publica. Cada mudança na main que passa nos testes gera uma nova versão do site.

`actions/configure-pages` `actions/upload-pages-artifact` `actions/deploy-pages` `environment: github-pages`

::::columns
:::card Onde fazer
```console
$ cd ~/labs/07-deploy-no-pages
```

O laboratório começa com o workflow do artefato do build. O workflow guiado vem pronto em `$CURSO_DIR/docs/solucoes/07.yml`.
:::
:::card Para este exercício
`⏱ tempo`
: 30 min

`módulo`
: Entrega contínua

`verificação`
: `check.sh 07`

`entrega`
: URL pública do livro de receitas
:::
::::

<p class="eyebrow">Conceito</p>

## Como o site chega ao Pages

<div class="flow"><div class="node ok"><b>testar</b><small>os três testes</small></div><div class="arr"><span class="a">→</span>needs</div><div class="node ok"><b>empacotar</b><small>build + configure-pages + upload-pages-artifact</small></div><div class="arr"><span class="a">→</span>needs</div><div class="node hi"><b>publicar</b><small>deploy-pages · URL do site</small></div></div>

::::columns
:::card empacotar
Gera o site, prepara o Pages com `actions/configure-pages` e envia a pasta `dist/` como um artefato especial com `actions/upload-pages-artifact`.
:::
:::card publicar
`actions/deploy-pages` coloca esse artefato no ar e devolve a URL. Ela aparece no grafo da execução e na página do repositório.
:::
:::card Somente a main
A condição `if` dos dois jobs só permite publicar a partir da main, por push ou clique, e nunca em um pull request. Os PRs continuam rodando `testar`.

A condição lê os contextos `github.ref` e `github.event_name`, como no exercício 4.
:::
::::

<p class="eyebrow">Conceito</p>

## Permissões e environment

```yaml title="o último job do workflow"
  publicar:
    needs: empacotar
    if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deploy.outputs.page_url }}
    steps:
      - name: Publicar
        id: deploy
        uses: actions/deploy-pages@v4
```

::::columns
:::card Permissões só no job publicar
O workflow inteiro tem `contents: read`. Só o job `publicar` recebe `pages: write`, para publicar, e `id-token: write`, para provar ao Pages qual execução está publicando. Não é preciso cadastrar nenhum token.
:::
:::card O environment github-pages
Um **environment** representa o destino de uma publicação. Ele guarda o histórico de deploys e mostra a URL, lida da saída da etapa `deploy`.
:::
::::

:::note O bloco concurrency
No topo do arquivo, ele evita dois deploys ao mesmo tempo na mesma branch. O segundo espera o primeiro terminar.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `cp "$CURSO_DIR/docs/solucoes/07.yml" .github/workflows/ci.yml` | copia o workflow guiado de publicação |
| `gh api -X POST "repos/{owner}/{repo}/pages" -f build_type=workflow` | liga o Pages com a fonte GitHub Actions, sem abrir Settings |
| `gh browse --settings` | abre as configurações do repositório |
| `gh run watch` | acompanha os três jobs no terminal |
| `gh pr merge --merge` | integra o PR na main e dispara o deploy (missão extra) |

:::card Documentação
{.links}
- [Workflows personalizados com o GitHub Pages](https://docs.github.com/pt/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Implantação contínua](https://docs.github.com/pt/actions/get-started/continuous-deployment)<small>o que é CD e como publicar com workflows</small>
- [Implantações e environments](https://docs.github.com/pt/actions/reference/workflows-and-actions/deployments-and-environments)
- [O GITHUB\_TOKEN](https://docs.github.com/pt/actions/concepts/security/github_token)<small>a credencial de cada execução e o bloco permissions</small>
- [Contextos](https://docs.github.com/pt/actions/reference/workflows-and-actions/contexts)<small>github.ref e github.event\_name no if; steps.deploy.outputs na URL</small>
- [Action · actions/configure-pages](https://github.com/actions/configure-pages)
- [Action · actions/upload-pages-artifact](https://github.com/actions/upload-pages-artifact)
- [Action · actions/deploy-pages](https://github.com/actions/deploy-pages)
:::

<p class="eyebrow">Tarefa · 30 min</p>

## O exercício

:::steps
1. Publique o estado inicial e abra as configurações:

   ```console
   $ cd ~/labs/07-deploy-no-pages
   $ gh repo create actions-07 --public --source=. --remote=origin --push
   $ gh browse --settings
   ```

2. Em **Pages → Build and deployment → Source**, escolha **GitHub Actions**.

3. Copie o workflow guiado e leia o fluxo com o professor. Personalize o título em `livro.md`:

   ```console
   $ cp "$CURSO_DIR/docs/solucoes/07.yml" .github/workflows/ci.yml
   $ code .github/workflows/ci.yml
   $ code livro.md
   ```

4. Rode a verificação. Ela simula um pull request, então só `testar` roda. `empacotar` e `publicar` ficam de fora:

   ```console
   $ check.sh 07
   ```

5. Envie e acompanhe os três jobs. No fim, abra a URL mostrada no job `publicar`:

   ```console
   $ git add .github/workflows/ci.yml livro.md
   $ git commit -m "Publica o livro de receitas no GitHub Pages"
   $ git push
   $ gh browse --actions
   ```
:::

:::card Verificação
```console
$ check.sh 07
```

Aprova quando as permissões do Pages estão só no job `publicar`, o `environment` tem a URL do deploy e a condição exclui PRs. A simulação confirma que um PR não publica.
:::

:::note O site não abriu?
Aguarde alguns minutos. Se o workflow falhou, confira *Settings → Pages* e compare o seu arquivo com o guiado. O comando `diff "$CURSO_DIR/docs/solucoes/07.yml" .github/workflows/ci.yml` mostra só as linhas diferentes. Depois de corrigir, use **Run workflow** na main.
:::

:::card Missão extra · o fluxo completo
```console
$ git switch -c nova-receita
```

Crie uma receita em `receitas/` e faça o commit. Depois, envie a branch, abra o PR e faça o merge:

```console
$ git push -u origin nova-receita
$ gh pr create --base main --fill
$ gh pr merge --merge
```

No PR, só `testar` roda. Depois do merge, o workflow da main publica a receita nova.
:::

:::warning Ao terminar a aula
Guarde os links das entregas e pare o Codespace em github.com/codespaces → ⋯ → *Stop codespace*. Os repositórios e o site continuam no GitHub. Para praticar mais, faça os exercícios opcionais, de 08 a 14.
:::
