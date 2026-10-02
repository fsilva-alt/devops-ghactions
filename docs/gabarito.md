# Gabarito

Aqui estão os workflows e comandos completos de cada exercício; as explicações ficam nos slides. Tente resolver primeiro e consulte depois, para conferir o resultado ou descobrir o que faltou.

## Como usar

- Entre primeiro na pasta do laboratório indicada na capa do exercício, por exemplo `cd ~/labs/02-testes-no-push`.
- Os arquivos em [`solucoes/`](solucoes/) são os workflows completos dos 7 exercícios da aula e dos 7 opcionais. Para usar um deles, copie-o para `.github/workflows/ci.yml` do laboratório. O exercício 13 tem também a ação composta, em `13-acao.yml`.
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
| 08 · opcional | `~/labs/08-matriz-de-versoes` | [08.yml](solucoes/08.yml) |
| 09 · opcional | `~/labs/09-cache-de-dependencias` | [09.yml](solucoes/09.yml) |
| 10 · opcional | `~/labs/10-caminhos-e-agenda` | [10.yml](solucoes/10.yml) |
| 11 · opcional | `~/labs/11-anotacoes-no-pull-request` | [11.yml](solucoes/11.yml) |
| 12 · opcional | `~/labs/12-saidas-e-resumo` | [12.yml](solucoes/12.yml) |
| 13 · opcional | `~/labs/13-acao-composta` | [13.yml](solucoes/13.yml) e [13-acao.yml](solucoes/13-acao.yml) |
| 14 · opcional | `~/labs/14-release-por-tag` | [14.yml](solucoes/14.yml) |

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
cd ~
code meu-arquivo.txt
check.sh 00
```

No editor, `~/meu-arquivo.txt` deve ter uma única linha, salva com **Ctrl+S**:

```text
Estou pronto para a aula de GitHub Actions!
```

O `check.sh 00` aceita espaços sobrando no fim da linha e o fim de linha do Windows, mas não outro texto. `cat ~/meu-arquivo.txt` mostra o que foi salvo.

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

## Exercícios opcionais

Os exercícios de 08 a 14 ficam para depois da aula e podem ser feitos em qualquer ordem. Cada laboratório já começa com um workflow da aula; publique cada um em seu repositório, de `actions-08` a `actions-14`.

## Exercício 08 — Matriz de versões

`strategy.matrix.python-version: ['3.11', '3.12', '3.13']` cria uma cópia do job `testar` para cada versão, e `python-version: ${{ matrix.python-version }}` passa a versão de cada cópia ao setup-python. As versões vão entre aspas: sem elas, `3.10` vira o número `3.1`. `fail-fast: false` deixa todas as cópias terminarem quando uma falha.

O `check.sh 08` simula as três cópias; a primeira vez baixa os três Pythons. A entrega é a execução com `testar (3.11)`, `testar (3.12)` e `testar (3.13)` verdes.

## Exercício 09 — Cache de dependências

`cache: pip`, no `with` do setup-python dos dois jobs, guarda os pacotes baixados pelo pip. A chave inclui o sistema, a versão do Python e um hash do `requirements.txt`. Na primeira execução, `testar` não encontra cache e salva um no fim do job; `empacotar`, que roda depois por causa do `needs`, já mostra `Cache restored` e `Using cached`.

```bash
gh cache list
```

A entrega é o link da execução com o cache restaurado em `empacotar` e a saída de `gh cache list`.

## Exercício 10 — Caminhos e agendamento

`paths-ignore: ['README.md']` no `push` evita execuções quando o commit muda só o README. `schedule` com `cron: '0 9 * * 1'` roda os testes toda segunda-feira às 9h em UTC, 6h em Brasília, na branch padrão. O `check.sh 10` simula o evento `schedule`.

```bash
code README.md
git add README.md
git commit -m "Atualiza o README"
git push
gh run list --limit 3          # nenhuma execução nova
code receitas/brigadeiro.md
git add receitas/brigadeiro.md
git commit -m "Ajusta o rendimento do brigadeiro"
git push
gh run list --limit 3          # uma execução nova, evento push
```

## Exercício 11 — Anotações no pull request

O job `validar` lista com `grep -L '^Rende:'` as receitas sem a linha de rendimento, escreve uma anotação `::error file=…,line=1,…::` para cada uma e falha com `test -z` se a lista não estiver vazia. Publique a solução na `main` e crie a receita sem rendimento em uma branch:

```bash
git switch -c receita-de-cafe
code receitas/cafe.md          # receita sem a linha Rende:
check.sh 11                    # validar falha e mostra a anotação
git add receitas/cafe.md
git commit -m "Adiciona receita de café"
git push -u origin receita-de-cafe
gh pr create --base main --fill
```

Em **Files changed**, a anotação aparece na primeira linha de `cafe.md`. Para corrigir, acrescente `Rende: 4 xícaras` depois do título, faça o commit e o push. A entrega é o link do PR com o check vermelho, a anotação e o check verde.

## Exercício 12 — Saídas e resumo

O step `contagem` escreve `total=3` em `$GITHUB_OUTPUT`; o job `contar` expõe esse valor em `outputs.total`; o job `resumo`, com `needs: [testar, contar]`, lê `needs.contar.outputs.total` por `env` e escreve em `$GITHUB_STEP_SUMMARY`. O `check.sh 12` procura `O livro tem 3 receitas.` no log.

Depois da primeira execução, crie `receitas/limonada.md`, com o conteúdo do exercício 06, e envie. A entrega é o link da execução cujo resumo mostra 4 receitas.

## Exercício 13 — Ação composta

Crie a ação e troque, nos dois jobs, o setup-python e a instalação por `uses: ./.github/actions/preparar`, depois do checkout:

```bash
mkdir -p .github/actions/preparar
cp "$CURSO_DIR/docs/solucoes/13-acao.yml" .github/actions/preparar/action.yml
cp "$CURSO_DIR/docs/solucoes/13.yml" .github/workflows/ci.yml
check.sh 13
git add .github
git commit -m "Configura workflow do exercício 13"
gh repo create actions-13 --public --source=. --remote=origin --push
```

Numa ação composta, `runs.using` é `composite`, `name` e `description` são obrigatórios e cada `run` precisa de `shell: bash`. O commit leva a pasta `.github` inteira: sem `action.yml`, o job falha no GitHub.

## Exercício 14 — Release por tag

`tags: ['v*']` no `push` dispara o workflow quando uma tag que começa com `v` é enviada. O job `lancar` roda só nesse caso, com `if: startsWith(github.ref, 'refs/tags/v')`, e é o único com `contents: write`. Ele baixa o artefato `site`, compacta e cria o release com `gh release create`, usando `GH_TOKEN: ${{ github.token }}`.

O `check.sh 14` simula um push na `main`: `testar` e `empacotar` rodam, e `lancar` fica de fora. Depois de publicar:

```bash
git tag v1.0.0
git push origin v1.0.0
gh run watch
gh release view v1.0.0 --web
```

A entrega é o link do release `v1.0.0`, com `livro-de-receitas.zip`.
