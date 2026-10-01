# Gabarito comentado

Consulte após tentar. Os arquivos em `solucoes/` são os workflows completos e executáveis dos **7 exercícios**. No Codespace, entre no laboratório correspondente e copie o YAML para `.github/workflows/ci.yml`; o projeto e os testes já foram gerados pelo instalador.

| Exercício | Laboratório | Solução |
|---|---|---|
| 01 | `~/labs/01-primeiro-workflow` | [01.yml](solucoes/01.yml) |
| 02 | `~/labs/02-testes-no-push` | [02.yml](solucoes/02.yml) |
| 03 | `~/labs/03-checks-no-pull-request` | [03.yml](solucoes/03.yml) |
| 04 | `~/labs/04-variaveis-e-contextos` | [04.yml](solucoes/04.yml) |
| 05 | `~/labs/05-jobs-e-dependencias` | [05.yml](solucoes/05.yml) |
| 06 | `~/labs/06-artefatos-do-build` | [06.yml](solucoes/06.yml) |
| 07 | `~/labs/07-deploy-no-pages` | [07.yml](solucoes/07.yml) |

Exemplo, **dentro do laboratório 02**:

```bash
cp "$CURSO_DIR/docs/solucoes/02.yml" .github/workflows/ci.yml
check.sh 02
git add .github/workflows/ci.yml
git commit -m "Adiciona testes no push"
gh repo create actions-02 --public --source=. --remote=origin --push
gh browse --actions
```

Se já criou o repositório, substitua `gh repo create ...` por `git push`. A cópia resolve apenas o arquivo YAML: conclua as ações e entregas no GitHub descritas abaixo.

## 01 — Primeiro workflow

`workflow_dispatch` habilita a execução manual. `runs-on: ubuntu-latest` escolhe o tipo de runner. `steps` é uma lista, e `run` executa um comando do shell. Depois do push para a branch padrão, abra **Actions → Boas-vindas → Run workflow → main → Run workflow** e leia a mensagem no log.

Resposta esperada: o Codespace foi usado para editar; o runner, para executar o `echo`.

## 02 — Testes no push

O evento `push` está filtrado para `main`. Checkout baixa o código no runner; setup-python escolhe a versão; pip instala as dependências; unittest executa os três testes. `uses` chama uma action e `run` chama um comando. A ordem é importante.

O primeiro push já deve gerar uma execução. Para outra, edite o título de `cardapio.md`, faça commit e push. Confira o evento e o hash na aba Actions.

## 03 — Checks no pull request

`pull_request.branches: [main]` seleciona a **branch de destino** do PR. Publique primeiro a solução na `main`. Depois:

```bash
git switch -c teste-do-ci
sed -i 's/return preco_centavos \* quantidade/return preco_centavos + quantidade/' app.py
git add app.py
git commit -m "Demonstra falha detectada pelo CI"
git push -u origin teste-do-ci
gh pr create --base main --title "Pratica checks do CI" --body "Demonstra uma falha e sua correção."
```

O teste de três unidades espera 1500 centavos e recebe 503; o teste de quantidade zero também falha. Abra **Checks**, leia a etapa Testar e registre o link da execução vermelha. Para corrigir:

```bash
sed -i 's/return preco_centavos + quantidade/return preco_centavos * quantidade/' app.py
git add app.py
git commit -m "Corrige o cálculo do total"
git push
```

O mesmo PR recebe uma nova execução. Confira que o hash mudou e que agora os três testes passam. O PR pode ficar aberto para avaliação. Checks só impedem merge quando há regras de proteção configuradas; neste curso basta observá-los.

## 04 — Variáveis e contextos

No repositório `actions-04`, cadastre `TURMA=turma-actions` em **Settings → Secrets and variables → Actions → Variables**. Na aba **Secrets**, cadastre `CURSO_TOKEN` com o valor fictício `somente-demonstracao`.

A solução passa as expressões para `env`; o shell usa `$MENSAGEM`, `$AUTOR`, `$TURMA` e `$TOKEN_DEMO`. Execute manualmente com uma mensagem própria. O log mostra mensagem, autor e turma; o segredo é apenas verificado como não vazio. `env.CURSO` está no arquivo; `vars.TURMA` está nas configurações; `secrets.CURSO_TOKEN` é tratado como segredo; `github.actor` vem da execução.

## 05 — Jobs e dependências

`empacotar` tem `needs: testar`. Checkout, Python e dependências são preparados novamente porque o segundo job usa outro runner. `python build.py` produz o site; `test -s dist/index.html` confirma que o arquivo existe e não está vazio.

Faça a mesma troca temporária de `*` por `+` em `app.py`, agora na `main`, e publique. `testar` falha; `empacotar` é pulado. Corrija `+` para `*` e faça novo push. Os dois jobs ficam verdes na execução nova.

## 06 — Artefatos do build

O upload vem depois do build e envia `dist/` com nome `site`. `if-no-files-found: error` evita sucesso sem arquivo. `retention-days: 7` limita a retenção solicitada; políticas da organização podem impor limites próprios.

Na página da execução concluída, baixe **Artifacts → site**. O ZIP contém `index.html`. Guardar esse arquivo não publica um site na web: esse é o próximo exercício.

## 07 — Deploy no Pages

Crie o repositório público com o estado inicial, habilite **Settings → Pages → Build and deployment → Source: GitHub Actions**, depois publique a solução. O workflow usa:

- Testes em push para `main` e em PRs destinados à `main`.
- Condição nos jobs de build/publicação para não publicar um PR ou outra branch.
- `configure-pages` e `upload-pages-artifact` para preparar o artefato esperado pelo Pages.
- `contents: read` e `pages: read` no build para ler o código e a configuração do site.
- `pages: write` e `id-token: write` somente no job de publicação.
- `environment: github-pages` com URL obtida de `steps.deploy.outputs.page_url`.
- `concurrency` para controlar execuções de publicação da mesma referência.

Para repetir manualmente, use **Actions → Publicar no Pages → Run workflow**, selecionando `main`. Aguarde todos os jobs terminarem e abra a URL do environment. Cadastre a URL pública e o link da execução como entrega. Não é necessário cadastrar um token pessoal como segredo para o deploy.
