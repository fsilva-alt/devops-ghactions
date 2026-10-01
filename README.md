# Curso de GitHub Actions no GitHub Codespaces

Curso **introdutório, em pt-BR, com exatamente 7 exercícios e 3 horas de aula**. Você vai automatizar testes e publicar um pequeno site de cardápio. O código Python já está pronto: o foco é entender e escrever workflows.

**O GitHub Codespaces é obrigatório nos 7 exercícios.** É nele que você edita os arquivos e executa comandos. Os workflows rodam em outras máquinas: os runners do GitHub Actions.

Comece por [Antes da aula](#antes-da-aula) e depois siga a [Sequência da aula](#sequência-da-aula). O [guia do aluno](docs/guia-do-aluno.md) explica como acompanhar os exercícios e resolver problemas comuns. Consulte também a [ementa](docs/ementa.md), a [apresentação](https://fsilva-alt.github.io/devops-ghactions/), o [gabarito](docs/gabarito.md) e o [guia do professor](docs/guia-do-professor.md).

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

1. Entre na sua conta no [GitHub](https://github.com).
2. Crie um Codespace em branco: em [github.com/codespaces](https://github.com/codespaces), escolha o modelo **Blank**. Use esse mesmo Codespace durante toda a aula.
3. No VS Code que abrir no navegador, acesse **Terminal → New Terminal**. Cole o comando abaixo e pressione Enter:

   ```bash
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"
   ```

   O instalador baixa o material para `~/devops-ghactions`, instala o verificador de YAML e prepara os 7 laboratórios em `~/labs`. Também cria um atalho `labs` na pasta em que foi executado, para acessar os exercícios pelo explorador do VS Code, e disponibiliza os comandos `check.sh`, `reset.sh` e `setup.sh`. O símbolo `~` representa sua pasta pessoal no Codespace.

   Autorize o GitHub CLI com a conta que usará na aula. O instalador pede o escopo `workflow`, necessário para enviar arquivos de workflows. Se não abrir uma janela, siga o código exibido em [github.com/login/device](https://github.com/login/device). Um login salvo válido é reutilizado. Aguarde a mensagem **Curso de GitHub Actions instalado com sucesso!**.

   Se o login for interrompido, execute o instalador novamente. Os laboratórios serão preservados. A autenticação segue o mesmo procedimento do curso de Git: login pelo navegador, reutilização das credenciais salvas e configuração do Git com `gh auth setup-git`.

4. Abra **um terminal novo**, ou execute `source ~/.bashrc` no bash / `source ~/.zshrc` no zsh, para carregar os comandos e a autenticação. Execute os comandos abaixo, um por vez:

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

5. Pare o Codespace em [github.com/codespaces](https://github.com/codespaces): **⋯ → Stop codespace**. Reabra o mesmo ambiente no dia da aula. Codespaces e Actions têm franquias e cobrança separadas; confira sua disponibilidade de Codespaces antes do evento. A prática usa repositórios públicos e runners Linux padrão.

## Sequência da aula

Os tempos incluem explicação, demonstração, prática e conferência.

| # | Exercício | Conceito novo | Tempo |
|---|---|---|---:|
| [01](https://fsilva-alt.github.io/devops-ghactions/#exercicio-01) | Primeiro workflow | YAML, evento manual, job, runner e step | 15 min |
| [02](https://fsilva-alt.github.io/devops-ghactions/#exercicio-02) | Testes no push | `push`, `checkout`, `setup-python`, `run` × `uses` | 25 min |
| [03](https://fsilva-alt.github.io/devops-ghactions/#exercicio-03) | Checks no pull request | `pull_request`, logs, falhar e corrigir | 25 min |
| [04](https://fsilva-alt.github.io/devops-ghactions/#exercicio-04) | Variáveis e contextos | `env`, `inputs`, `github`, `vars`, `secrets` | 20 min |
| [05](https://fsilva-alt.github.io/devops-ghactions/#exercicio-05) | Jobs e dependências | `needs`, isolamento entre runners, build | 20 min |
| [06](https://fsilva-alt.github.io/devops-ghactions/#exercicio-06) | Artefatos do build | Salvar e baixar arquivos de uma execução | 20 min |
| [07](https://fsilva-alt.github.io/devops-ghactions/#exercicio-07) | Deploy no Pages | Publicação guiada, `permissions`, `environment` | 30 min |

Prática e explicações: **155 minutos**. Abertura: 10; intervalo: 10; encerramento: 5. Total: **180 minutos**.

## Como o ambiente funciona

### Primeiros passos no terminal e no editor

- **Executar um comando:** copie a linha para o terminal e pressione Enter. Aguarde o término antes de executar a próxima.
- **Editar um arquivo:** use `code nome-do-arquivo` na pasta do laboratório. Blocos de YAML vão no arquivo indicado, não no terminal. Salve com **Ctrl+S**, ou **Cmd+S** no Mac.
- **Mudar de pasta:** use `cd caminho`. `pwd` mostra a pasta atual, e `ls` lista os arquivos.
- **Usar os exemplos:** substitua `NN` pelo número do exercício. Por exemplo, `check.sh NN` vira `check.sh 02` no exercício 02.

### Onde ficam os arquivos

Cada exercício tem seu próprio repositório local em `~/labs/NN-nome` e um ponto de partida pronto. Assim você consegue acompanhar o próximo mesmo que não tenha terminado o anterior. Todos usam o mesmo projeto de cardápio. O exercício 04 é uma demonstração isolada de configuração; os seguintes retomam o projeto de testes e build.

| Local | Conteúdo |
|---|---|
| `~/devops-ghactions/` (`$CURSO_DIR`) | Material do curso: slides, scripts e documentos |
| [Site do curso](https://fsilva-alt.github.io/devops-ghactions/) | Slides HTML com os enunciados dos 7 exercícios |
| `~/devops-ghactions/docs/index.html` | Cópia local dos slides |
| `~/labs/NN-nome/` | Arquivos que você modifica e publica |
| `labs`, no explorador do VS Code | Atalho para `~/labs`, criado pelo instalador |
| `.github/workflows/ci.yml`, dentro de cada lab | Workflow do exercício |
| `$CURSO_DIR/docs/solucoes/` | Workflows completos para consulta depois da tentativa |

O instalador define `CURSO_DIR`, `LABS_DIR` e o `PATH` nos novos terminais bash/zsh. No Codespaces, remove `GH_TOKEN` e `GITHUB_TOKEN` desses terminais para que o `gh` use o login salvo, com acesso aos repositórios da prática.

| Comando | Função |
|---|---|
| `setup.sh` | Cria apenas laboratórios ausentes |
| `check.sh NN` | Analisa o YAML e alguns requisitos do exercício, sem acessar o GitHub |
| `reset.sh NN` | **Apaga o trabalho local desse laboratório** e recria o estado inicial |

Dentro de uma pasta de laboratório, `check.sh` e `reset.sh` descobrem o número automaticamente, inclusive pelo atalho `labs`. Após um reset, entre novamente na pasta com o `cd` do enunciado. Os enunciados ficam nos [slides HTML](https://fsilva-alt.github.io/devops-ghactions/); selecione o exercício no índice.

Você pode executar o instalador novamente: ele atualiza o material do curso e cria apenas os laboratórios ausentes. Para atualizar o ponto de partida de um laboratório existente, guarde o trabalho que deseja manter e use `reset.sh NN`. Os caminhos podem ser personalizados com `CURSO_DIR` e `LABS_DIR`; `CURSO_REPO` e `CURSO_RAMO` permitem usar outra origem ou branch do material.

**Um check local aprovado não comprova a execução na nuvem.** Conclua também a entrega indicada em cada enunciado: execução, logs, PR, artefato ou site publicado. O verificador não é um validador completo da linguagem do Actions.

### Publicar cada laboratório

Cada exercício usa um repositório público separado, `actions-01` a `actions-07`, na sua conta. Não crie outro Codespace: continue no Codespace Blank preparado antes da aula. Na pasta do laboratório, depois de salvar e verificar o workflow:

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

A configuração em `.devcontainer/` é destinada à manutenção deste repositório. O aluno usa o modelo Blank e o instalador remoto, sem precisar clonar o curso manualmente.

Em testes locais, `CURSO_AUTH_GITHUB=0` pula a autenticação, dispensa o `gh` e não habilita a remoção dos tokens nos terminais. Na instalação normal, o GitHub CLI é obrigatório e o primeiro login precisa de um terminal interativo. Fora do Codespaces, as variáveis de autenticação são mantidas.

A apresentação está em `docs/index.html`, com estilos em `docs/style.css`. Abra o HTML diretamente no navegador para revisar as aulas; a navegação e as perguntas expansíveis funcionam sem JavaScript. Para conferir apenas seu conteúdo e links, execute `python3 tests/apresentacao.py`.

```bash
bash tests/rodar.sh          # testes em ambiente temporário, sem conta GitHub
bash tests/rodar.sh --docker # mesma suíte em Ubuntu limpo, exige Docker
```

A suíte confere instalação via `curl` e `sh -c` em um workspace vazio, atualização do material, preservação dos labs e dos arquivos do workspace, atalho `labs`, autenticação simulada, YAMLs iniciais e resolvidos, erros comuns, links locais, os 7 enunciados, testes do projeto e build. `CURSO_MODO_TESTE=1` libera os scripts fora do Codespaces apenas para manutenção automatizada; a experiência do aluno continua obrigatoriamente no Codespaces. O modo de teste usa uma origem Git local e não cria repositórios no GitHub nem publica sites.

## Licença

[MIT](LICENSE).
