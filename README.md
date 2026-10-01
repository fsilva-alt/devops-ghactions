# GitHub Actions: primeiros passos no Codespaces

Curso **introdutório, em pt-BR, com exatamente 7 exercícios e 3 horas de aula**. Você vai automatizar testes e publicar um pequeno site de cardápio. O código Python já está pronto: o foco é entender e escrever workflows.

**O GitHub Codespaces é obrigatório nos 7 exercícios.** É nele que você edita os arquivos e executa comandos. Os workflows rodam em outras máquinas: os runners do GitHub Actions.

**Comece por [Antes da aula](#antes-da-aula).** Professor e monitores: [guia de condução](docs/guia-do-professor.md). Consulte também a [ementa](docs/ementa.md), a [apresentação navegável](https://fsilva-alt.github.io/devops-ghactions/) e o [gabarito comentado](docs/gabarito.md).

## O que você vai aprender

- Diferenciar evento, workflow, job, step, action e runner.
- Ler YAML e escolher entre `run` e `uses`.
- Executar testes a cada push e acompanhar checks de um pull request.
- Encontrar uma falha nos logs e corrigir sua causa.
- Usar variáveis, contextos e um segredo de demonstração.
- Ordenar jobs, guardar o resultado do build e publicar no GitHub Pages.

### Pré-requisitos

Conta pessoal no GitHub com acesso ao Codespaces, navegador e conexão à internet. Você precisa conhecer o básico de arquivos, terminal, commit, branch e push; os comandos de publicação são fornecidos. Não é necessário saber programar em Python nem ter experiência em CI/CD.

## Antes da aula

Faça a preparação pelo menos um dia antes.

1. Abra [o repositório do curso](https://github.com/fsilva-alt/devops-ghactions) e selecione **Code → Codespaces → Create codespace on main**. Use o Codespace desse repositório para toda a aula. O arquivo `.devcontainer/devcontainer.json` instala Python, GitHub CLI e as extensões do editor; a preparação automática cria os laboratórios sem pedir login.
2. Aguarde a criação e a preparação terminarem. Em **Terminal → New Terminal**, na raiz do curso, execute:

   ```bash
   sh install.sh
   ```

   Autorize o GitHub CLI com a conta que usará na aula. O instalador pede o escopo `workflow`, necessário para enviar arquivos de workflows. Se não abrir uma janela, siga o código exibido em [github.com/login/device](https://github.com/login/device). Um login salvo válido é reutilizado.

3. Abra **um terminal novo**. Confira:

   ```bash
   echo "$CODESPACES"
   gh auth status --hostname github.com
   git config user.name
   git config user.email
   check.sh 01
   ```

   O primeiro comando deve mostrar `true`. É esperado que `check.sh 01` peça o workflow que você ainda vai criar. Se o nome ou e-mail estiver vazio, configure sua autoria com seus próprios dados:

   ```bash
   git config --global user.name "Seu nome"
   git config --global user.email "seu-email-da-conta-github"
   ```

4. Pare o Codespace em [github.com/codespaces](https://github.com/codespaces): **⋯ → Stop codespace**. Reabra o mesmo ambiente no dia da aula. Codespaces e Actions têm franquias e cobrança separadas; confira sua disponibilidade de Codespaces antes do evento. A prática usa repositórios públicos e runners Linux padrão.

## Os 7 exercícios

Os tempos incluem explicação, demonstração, prática e conferência.

| # | Exercício | Conceito novo | Tempo |
|---|---|---|---:|
| [01](exercises/01-primeiro-workflow/README.md) | Primeiro workflow | YAML, evento manual, job, runner e step | 15 min |
| [02](exercises/02-testes-no-push/README.md) | Testes no push | `push`, `checkout`, `setup-python`, `run` × `uses` | 25 min |
| [03](exercises/03-checks-no-pull-request/README.md) | Checks no pull request | `pull_request`, logs, falhar e corrigir | 25 min |
| [04](exercises/04-variaveis-e-contextos/README.md) | Variáveis e contextos | `env`, `inputs`, `github`, `vars`, `secrets` | 20 min |
| [05](exercises/05-jobs-e-dependencias/README.md) | Jobs e dependências | `needs`, isolamento entre runners, build | 20 min |
| [06](exercises/06-artefatos-do-build/README.md) | Artefatos do build | Salvar e baixar arquivos de uma execução | 20 min |
| [07](exercises/07-deploy-no-pages/README.md) | Deploy no Pages | Publicação guiada, `permissions`, `environment` | 30 min |

Prática e explicações: **155 minutos**. Abertura: 10; intervalo: 10; encerramento: 5. Total: **180 minutos**.

## Como os laboratórios funcionam

Cada exercício tem seu próprio repositório local em `~/labs-actions/NN-nome` e um ponto de partida pronto. Assim você consegue acompanhar o próximo mesmo que não tenha terminado o anterior. Todos usam o mesmo projeto de cardápio. O exercício 04 é uma demonstração isolada de configuração; os seguintes retomam o projeto de testes e build.

| Local | Conteúdo |
|---|---|
| `$CURSO_DIR` | Repositório do curso aberto no Codespace, normalmente `/workspaces/devops-ghactions` |
| `$CURSO_DIR/exercises/` | Os 7 enunciados |
| `~/labs-actions/NN-nome/` | Arquivos que você modifica e publica |
| `.github/workflows/ci.yml`, dentro de cada lab | Workflow do exercício |
| `$CURSO_DIR/docs/solucoes/` | Workflows completos para consulta depois da tentativa |

O instalador define `CURSO_DIR`, `LABS_DIR` e o `PATH` nos novos terminais bash/zsh. No Codespaces, remove `GH_TOKEN` e `GITHUB_TOKEN` desses terminais para que o `gh` use o login salvo, com acesso aos repositórios da prática.

| Comando | Função |
|---|---|
| `setup.sh` | Cria apenas laboratórios ausentes |
| `check.sh NN` | Analisa o YAML e alguns requisitos do exercício, sem acessar o GitHub |
| `reset.sh NN` | **Apaga o trabalho local desse laboratório** e recria o estado inicial |

Dentro de uma pasta de laboratório, `check.sh` e `reset.sh` descobrem o número automaticamente. Exemplo para ler um enunciado: `code "$CURSO_DIR/exercises/02-testes-no-push/README.md"`.

**Um check local aprovado não comprova a execução na nuvem.** Conclua também a entrega indicada em cada enunciado: execução, logs, PR, artefato ou site publicado. O verificador não é um validador completo da linguagem do Actions.

### Publicar cada laboratório

Cada exercício usa um repositório público separado, `actions-01` a `actions-07`, na sua conta. Não crie outro Codespace: continue no ambiente do curso. Na pasta do laboratório, depois de salvar e verificar o workflow:

```bash
git add .github/workflows
git commit -m "Configura workflow do exercício"
# Troque NN pelo número do exercício, por exemplo actions-02.
gh repo create actions-NN --public --source=. --remote=origin --push
gh browse --actions
```

O comando `gh repo create` é usado **uma vez por laboratório**. Para alterações seguintes: `git add`, `git commit` e `git push`. Os nomes `actions-NN` são marcadores nos exemplos genéricos; cada exercício traz o nome pronto para copiar. Se um nome já existir na sua conta, escolha outro, como `actions-02-turma-b`.

Para o botão **Run workflow** aparecer, o workflow com `workflow_dispatch` precisa estar na branch padrão (`main`). Ao abrir um repositório de exercício, confirme que a branch padrão é `main`.

### Retomar depois de resetar

`reset.sh` remove também a configuração de `origin`, mas não altera o GitHub. Para começar uma nova tentativa do zero, publique em **um novo nome**, por exemplo `gh repo create actions-02-tentativa-2 --public --source=. --remote=origin --push`. Isso evita misturar o histórico inicial com a tentativa já publicada. Para recuperar o trabalho publicado, clone aquele repositório em outra pasta no mesmo Codespace.

### Se o push falhar por permissão

Confira `git remote -v` e `gh auth status --hostname github.com`. Para um login antigo sem escopo de workflow, no terminal do Codespace:

```bash
unset GH_TOKEN GITHUB_TOKEN
gh auth refresh --hostname github.com --scopes workflow
gh auth setup-git --hostname github.com
git push -u origin main
```

Se a conta estiver incorreta, use `gh auth login --hostname github.com --git-protocol https --web --scopes workflow`. O `GITHUB_TOKEN` **dentro de um workflow** é outra credencial, fornecida automaticamente pelo Actions para aquela execução.

## Ao final

Compartilhe os links pedidos nos 7 exercícios. Guarde a URL do site do exercício 07 e o PR com falha e correção do exercício 03. Faça push de tudo que deseja guardar e pare o Codespace; excluí-lo libera o armazenamento, mas apaga arquivos locais não publicados.

## Desenvolvimento do material

Os geradores ficam em `scripts/labs.sh`, o verificador em `scripts/checks.py`, e o projeto em `templates/projeto/`. Os YAMLs do [gabarito](docs/gabarito.md) também são usados como pontos de partida e nos testes.

```bash
bash tests/rodar.sh          # testes em ambiente temporário, sem conta GitHub
bash tests/rodar.sh --docker # mesma suíte em Ubuntu limpo, exige Docker
```

A suíte confere instalação, preservação dos labs, YAMLs iniciais e resolvidos, erros comuns, links locais, os 7 enunciados, testes do projeto e build. `CURSO_MODO_TESTE=1` libera os scripts fora do Codespaces apenas para manutenção automatizada; a experiência do aluno continua obrigatoriamente no Codespaces. O modo de teste usa `CURSO_AUTH_GITHUB=0` e não cria repositórios nem publica sites.

## Licença

[MIT](LICENSE).
