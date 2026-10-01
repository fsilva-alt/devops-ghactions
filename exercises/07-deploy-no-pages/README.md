# 07 — Deploy no Pages

**30 minutos · Ambiente obrigatório: GitHub Codespaces · Prática guiada**

## Objetivo

Conectar teste, build e publicação para disponibilizar o cardápio em uma URL pública.

## Onde e estado inicial

```bash
cd ~/labs-actions/07-deploy-no-pages
```

O workflow inicial testa, gera o site e guarda um artefato comum. Neste exercício, você usa as actions próprias do Pages para publicar esse resultado. O exemplo completo é fornecido para você concentrar a atenção no fluxo.

## Tarefa

1. Publique o **estado inicial** para conseguir configurar o repositório:

   ```bash
   gh repo create actions-07 --public --source=. --remote=origin --push
   gh browse
   ```

2. No GitHub, abra **Settings → Pages → Build and deployment → Source** e selecione **GitHub Actions**. O repositório público permite acompanhar esta prática em conta pessoal com GitHub Free.
3. Volte ao terminal do Codespace. Copie e abra o workflow guiado:

   ```bash
   cp "$CURSO_DIR/docs/solucoes/07.yml" .github/workflows/ci.yml
   code .github/workflows/ci.yml
   ```

4. Leia o arquivo junto com o professor:

   | Parte | Por que está ali |
   |---|---|
   | `testar` | Impede que um código com testes falhos seja publicado |
   | `empacotar`, com `needs: testar` | Prepara o HTML depois dos testes |
   | `actions/configure-pages` | Prepara as informações necessárias para o Pages |
   | `actions/upload-pages-artifact` | Envia o site no formato esperado pelo Pages |
   | `publicar`, com `needs: empacotar` | Publica o artefato usando `actions/deploy-pages` |
   | `environment: github-pages` | Identifica o destino da publicação e exibe sua URL |
   | `permissions` no job publicar | Autoriza a publicação e a emissão do token de identidade da execução |
   | `concurrency` | Controla execuções simultâneas para a mesma referência |

   O job de publicação tem `pages: write` e `id-token: write`. O GitHub fornece a credencial; não é necessário cadastrar um token pessoal. O job de testes tem `contents: read`; o build também recebe `pages: read` para consultar a configuração do site.

5. Localize a condição dos jobs `empacotar` e `publicar`:

   ```yaml
   if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'
   ```

   Ela permite publicar a `main`, por push ou execução manual, e exclui PRs. PRs ainda executam o job `testar`. A sintaxe de condição será aprofundada depois; agora reconheça seu propósito.

6. Personalize o título de `cardapio.md`, salve e publique:

   ```bash
   check.sh 07
   git add .github/workflows/ci.yml cardapio.md
   git commit -m "Publica o cardápio no GitHub Pages"
   git push
   gh browse --actions
   ```

7. Abra a execução **Publicar no Pages** e acompanhe `testar → empacotar → publicar`. Depois de concluir, abra a URL do environment `github-pages`. Aguarde alguns minutos se a página ainda estiver sendo disponibilizada.

## Verificação e entrega

- `check.sh 07` aprova os requisitos locais.
- Os três jobs terminam com sucesso na execução da `main`.
- O endereço público abre o cardápio com seu título.
- Entregue a URL do site e o link da execução de deploy. Explique a diferença entre **build**, **artefato** e **deploy**.

Se o Pages ainda não estava configurado, conclua o passo 2 e use **Actions → Publicar no Pages → Run workflow → main** para tentar novamente. Se houver erro de permissão, compare `permissions` e `environment` com o exemplo.

## Fechamento do curso

Você completou os 7 exercícios. Salve os links das entregas e pare o Codespace. Seu site e os repositórios publicados continuam disponíveis no GitHub.

[Voltar ao índice](../../README.md)
