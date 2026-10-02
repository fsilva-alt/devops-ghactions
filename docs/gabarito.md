# Gabarito

Aqui estão os workflows e comandos completos de cada exercício; as explicações ficam nos slides. Tente resolver primeiro e consulte depois, para conferir o resultado ou descobrir o que faltou.

## Como usar

- Entre primeiro na pasta do laboratório indicada na capa do exercício, por exemplo `cd ~/labs/02-testes-no-push`.
- Os arquivos em [`solucoes/`](solucoes/) são os workflows completos dos 7 exercícios. Para usar um deles, copie-o para `.github/workflows/ci.yml` do laboratório.
- Execute `check.sh NN` antes de publicar. Ele confere o YAML e simula o workflow com o act.
- A cópia resolve apenas o YAML. Conclua também as ações e a entrega no GitHub descritas abaixo.

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
git commit -m "Executa os testes no push"
gh repo create actions-02 --public --source=. --remote=origin --push
gh browse --actions
```

Se o repositório já foi criado, troque `gh repo create ...` por `git push`.

## Exercício 00 — O ambiente está pronto?

```bash
git config user.name
git config user.email
gh auth status --hostname github.com
docker version
act --version
check.sh 00
```

Se algum item faltar, execute `setup.sh` e repita `check.sh 00`. Para acrescentar o escopo `workflow` a um login existente, use `gh auth refresh --hostname github.com --scopes workflow`.

## Exercício 01 — Primeiro workflow

`workflow_dispatch` habilita a execução manual. `runs-on: ubuntu-latest` escolhe o tipo de runner. `steps` é uma lista, e `run` executa um comando do shell. Depois do push para a branch padrão, abra **Actions → Boas-vindas → Run workflow**, selecione `main` e leia a mensagem no log da etapa **Cumprimentar a turma**.

O Codespace foi usado para escrever e publicar o workflow; o `echo` foi executado pelo runner.

## Exercício 02 — Testes no push

O evento `push` está filtrado para a `main`. `actions/checkout` baixa o código no runner; `actions/setup-python` instala o Python 3.12; o `pip` instala as dependências; o `unittest` executa os três testes. `uses` chama uma action e `run` executa um comando.

O primeiro push já gera uma execução. Para gerar outra, personalize o título em `livro.md` e envie:

```bash
code livro.md
git add livro.md
git commit -m "Personaliza o título do livro"
git push
```

Confira o evento e o hash do commit na página da execução.

## Exercício 03 — Checks no pull request

`pull_request.branches: [main]` seleciona os PRs cuja **branch de destino** é a `main`. Publique primeiro a solução na `main`. Depois, provoque a falha em uma branch:

```bash
git switch -c teste-do-ci
sed -i 's/return gramas_por_receita \* receitas/return gramas_por_receita + receitas/' receitas.py
check.sh 03
git add receitas.py
git commit -m "Demonstra falha no cálculo"
git push -u origin teste-do-ci
gh pr create --base main --fill
```

O `check.sh 03` já mostra a falha. No GitHub, o teste das três receitas de pão de queijo espera 1500 g e recebe 503; o teste com zero receitas também falha. Abra **Checks → testar → Testar** e guarde o link da execução vermelha. Para corrigir:

```bash
sed -i 's/return gramas_por_receita + receitas/return gramas_por_receita * receitas/' receitas.py
check.sh 03
git add receitas.py
git commit -m "Corrige o cálculo da quantidade"
git push
```

O mesmo PR recebe uma nova execução, com outro hash e os três testes aprovados. O PR pode ficar aberto para avaliação. Um check só impede o merge quando uma regra de proteção do repositório o exige.

## Exercício 04 — Variáveis e contextos

Copie a solução, troque o `default` do input `receita` e publique. Depois, cadastre a variável e o segredo fictício no repositório `actions-04`:

```bash
gh variable set TURMA --body "turma-de-actions"
gh secret set CURSO_TOKEN --body "somente-demonstracao"
```

O mesmo cadastro pode ser feito em **Settings → Secrets and variables → Actions**, nas abas **Variables** e **Secrets**.

Execute manualmente com uma receita à sua escolha. O log mostra cozinha, receita, autor e turma; o segredo é apenas verificado como não vazio. Origem de cada valor: `env.COZINHA` está no arquivo; `inputs.receita` vem do formulário do Run workflow; `github.actor` vem da execução; `vars.TURMA` e `secrets.CURSO_TOKEN` vêm das configurações do repositório. As expressões chegam ao shell por `env`, como `$RECEITA` e `$TOKEN_DEMO`.

Na simulação local, o `check.sh 04` usa `TURMA=turma-local` e um segredo de demonstração, porque o act não lê as configurações do repositório.

## Exercício 05 — Jobs e dependências

`empacotar` tem `needs: testar`. Checkout, Python e dependências são preparados de novo porque o segundo job roda em outro runner. `python build.py` gera o site; `test -s dist/index.html` confirma que o arquivo existe e não está vazio.

Para ver o build pulado, faça a mesma troca de `*` por `+` em `receitas.py`, agora na `main`, rode `check.sh 05` e publique. `testar` falha e `empacotar` aparece como **skipped**, no Codespace e no GitHub. Volte o `*`, faça um novo commit e push: os dois jobs ficam verdes.

## Exercício 06 — Artefatos do build

O upload vem depois do build e envia `dist/` com o nome `site`. `if-no-files-found: error` faz a etapa falhar se não houver arquivos. `retention-days: 7` define a retenção pedida; políticas da organização podem impor outros limites.

Para a segunda execução, crie `receitas/limonada.md`:

```markdown
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

```bash
python3 receitas.py
check.sh 06
git add receitas/limonada.md
git commit -m "Adiciona receita de limonada"
git push
```

Na página da nova execução, baixe **Artifacts → site** ou use `gh run download --name site --dir site-baixado`. O `index.html` deve listar a limonada. Guardar o artefato não publica o site; isso é feito no exercício 07.

## Exercício 07 — Deploy no Pages

Publique o estado inicial, habilite **Settings → Pages → Build and deployment → Source: GitHub Actions** e só então envie o workflow:

```bash
gh repo create actions-07 --public --source=. --remote=origin --push
cp "$CURSO_DIR/docs/solucoes/07.yml" .github/workflows/ci.yml
code livro.md
check.sh 07
git add .github/workflows/ci.yml livro.md
git commit -m "Publica o livro de receitas no GitHub Pages"
git push
```

Como alternativa à tela de configurações, `gh api -X POST "repos/{owner}/{repo}/pages" -f build_type=workflow` habilita o Pages com a fonte GitHub Actions.

O workflow usa:

- testes no push para a `main` e nos PRs destinados à `main`;
- condição nos jobs `empacotar` e `publicar` para não publicar a partir de um PR ou de outra branch;
- `configure-pages` e `upload-pages-artifact` para preparar o artefato esperado pelo Pages;
- `contents: read` e `pages: read` no build;
- `pages: write` e `id-token: write` somente no job `publicar`;
- `environment: github-pages`, com a URL lida de `steps.deploy.outputs.page_url`;
- `concurrency` para impedir dois deploys simultâneos da mesma referência.

O `check.sh 07` simula um pull request: só `testar` roda, e a simulação falha se `empacotar` ou `publicar` também rodarem. Para repetir o deploy, use **Actions → Publicar no Pages → Run workflow** na `main`. A entrega é a URL pública e o link da execução. Não é preciso cadastrar um token pessoal.
