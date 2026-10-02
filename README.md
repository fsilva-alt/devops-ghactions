# Curso de GitHub Actions no GitHub Codespaces

Aula ao vivo de 3 horas, com 7 exercícios feitos no navegador. O ambiente é o GitHub Codespaces, um computador Linux acessado pela internet que já vem com editor de arquivos, terminal, Git, GitHub CLI e Docker. Cada pessoa usa o seu, chamado **Codespace**.

O projeto da aula é um livro de receitas: arquivos Markdown com as receitas, um programa Python com três testes e um gerador de site. O código vem pronto. O curso trata da automação: testar cada mudança, gerar o site e publicá-lo no GitHub Pages com workflows do GitHub Actions.

Comece por [Antes da aula](#antes-da-aula) e depois siga a [Sequência da aula](#sequência-da-aula). O [guia do aluno](docs/guia-do-aluno.md) reúne orientações para acompanhar os exercícios e resolver problemas comuns. Consulte também a [ementa](docs/ementa.md), os [slides](https://fsilva-alt.github.io/devops-ghactions/), o [gabarito](docs/gabarito.md) e o [guia do professor](docs/guia-do-professor.md).

## O que você vai aprender

- explicar o que é o GitHub Actions, que problemas ele resolve e como é usado em um processo de CI/CD;
- diferenciar evento, workflow, job, step, action e runner;
- ler e escrever workflows em YAML e escolher entre `run` e `uses`;
- executar testes a cada push e acompanhar os checks de um pull request;
- encontrar uma falha nos logs e corrigir sua causa;
- usar variáveis, contextos e um segredo de demonstração;
- ordenar jobs, guardar o resultado do build e publicar um site no GitHub Pages.

### Pré-requisitos

Conta pessoal no GitHub com acesso ao Codespaces, navegador atualizado e conexão à internet. É preciso conhecer o básico de terminal, commit, branch e push; os comandos completos estão nos enunciados. Não é preciso saber programar em Python nem ter experiência com CI/CD.

## Antes da aula

Faça esta preparação **pelo menos um dia antes**, para ter tempo de resolver algum problema de acesso.

1. Entre na sua conta no [GitHub](https://github.com).
2. Crie um Codespace em branco: em [github.com/codespaces](https://github.com/codespaces), escolha o modelo **Blank**. Use esse mesmo Codespace durante toda a aula.
3. No VS Code aberto no navegador, use o menu **Terminal → New Terminal**. Cole a linha abaixo e pressione Enter:

   ```bash
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"
   ```

   O instalador salva o material em `~/devops-ghactions`, prepara os 7 laboratórios em `~/labs` e instala o **act**, o programa que simula os workflows no Codespace. Ele também baixa a imagem Docker usada pelo act, com cerca de 2 GB, o que leva alguns minutos na primeira vez. Na pasta em que foi executado, cria o atalho `labs`, para acessar os exercícios pelo explorador do VS Code. O símbolo `~` representa sua pasta pessoal no Codespace.

   Em seguida, autorize o GitHub CLI com a conta que usará na aula. O login pede o escopo `workflow`, necessário para enviar arquivos de workflow. Se nenhuma janela abrir, siga o código exibido em [github.com/login/device](https://github.com/login/device). Um login salvo e válido é reutilizado. Aguarde a mensagem **Curso de GitHub Actions instalado com sucesso!**. Se o login for interrompido, execute o instalador novamente; os laboratórios são preservados.

4. Abra **um terminal novo**, para carregar os comandos do curso, e execute:

   ```bash
   check.sh 00
   ```

   O exercício 00 confere sua identidade no Git, o login do GitHub CLI, os laboratórios, o Docker e o act, e executa um workflow mínimo em um container. Se aparecer **concluído**, o ambiente está pronto. Se aparecer uma dica, siga a orientação e repita o comando. Se o nome ou o e-mail do Git estiverem vazios, configure-os com seus dados:

   ```bash
   git config --global user.name "Seu nome"
   git config --global user.email "seu-email-da-conta-github"
   ```

5. Pare o Codespace em [github.com/codespaces](https://github.com/codespaces): **⋯ → Stop codespace**. No dia da aula, abra o mesmo Codespace. Codespaces e Actions têm franquias separadas; confira sua disponibilidade de Codespaces antes da aula. Os exercícios usam repositórios públicos e runners Linux padrão.

## Como o ambiente funciona

### Primeiros passos no terminal e no editor

- **Executar um comando:** copie a linha para o terminal e pressione Enter. Aguarde o término antes de executar a próxima. Nos slides, o `$` no início da linha marca um comando e não deve ser copiado.
- **Editar um arquivo:** use `code nome-do-arquivo` na pasta do laboratório. Blocos de YAML vão no arquivo indicado acima deles, não no terminal. Salve com **Ctrl+S**, ou **Cmd+S** no Mac.
- **Mudar de pasta:** use `cd caminho`. `pwd` mostra a pasta atual, e `ls` lista os arquivos.
- **Usar os exemplos:** troque `NN` pelo número do exercício. Por exemplo, `check.sh NN` vira `check.sh 02` no exercício 02.

### Onde ficam os arquivos

Cada exercício tem seu próprio repositório local em `~/labs/NN-nome`, com um ponto de partida pronto. Assim, é possível acompanhar um exercício mesmo sem ter concluído o anterior. O exercício 04 é uma demonstração isolada de configuração; os seguintes retomam os testes e o build do livro de receitas.

| Local | Conteúdo |
|---|---|
| `~/devops-ghactions/` (`$CURSO_DIR`) | Material do curso: slides, scripts e documentos |
| [Site do curso](https://fsilva-alt.github.io/devops-ghactions/) | Slides com a introdução e os enunciados |
| `~/labs/NN-nome/` | Arquivos que você modifica e publica |
| `labs`, no explorador do VS Code | Atalho para `~/labs`, criado pelo instalador |
| `.github/workflows/ci.yml`, em cada laboratório | Workflow do exercício |
| `$CURSO_DIR/docs/solucoes/` | Workflows completos, para consulta depois da tentativa |

O instalador define `CURSO_DIR`, `LABS_DIR` e o `PATH` nos novos terminais bash e zsh. No Codespaces, remove `GH_TOKEN` e `GITHUB_TOKEN` desses terminais, para que o `gh` use o login salvo, com acesso aos repositórios da prática.

| Comando | Função |
|---|---|
| `check.sh NN` | Confere o YAML do exercício e simula o workflow com o act |
| `check.sh NN --sem-act` | Confere apenas o YAML, sem executar os jobs |
| `setup.sh` | Cria os laboratórios ausentes e baixa o act e a imagem do runner local |
| `reset.sh NN` | **Apaga o trabalho local desse laboratório** e recria o estado inicial |

Dentro de uma pasta de laboratório, `check.sh` e `reset.sh` descobrem o número automaticamente, inclusive pelo atalho `labs`. Depois de um reset, entre novamente na pasta com o `cd` do enunciado.

O instalador pode ser executado de novo: ele atualiza o material do curso e cria apenas os laboratórios ausentes. Para receber o ponto de partida atualizado de um laboratório, guarde o trabalho que deseja manter e use `reset.sh NN`. Os caminhos podem ser personalizados com `CURSO_DIR` e `LABS_DIR`; `CURSO_REPO` e `CURSO_RAMO` permitem usar outra origem ou branch do material.

### A simulação com o act

O `check.sh` trabalha em duas etapas. Primeiro, analisa o YAML e confere os requisitos do exercício. Depois, usa o [act](https://nektosact.com/) para executar os jobs no próprio Codespace: cada job roda em um container Docker criado a partir de uma imagem semelhante ao runner `ubuntu-latest` do GitHub. A saída mostra as etapas, o log dos comandos e o resultado de cada job, em poucos segundos e antes do push.

A simulação tem limites. O act não cria execuções no GitHub, não publica no Pages e não lê as variáveis e os segredos cadastrados no repositório; no exercício 04, o `check.sh` usa valores locais de demonstração. **A entrega de cada exercício é a execução no GitHub**: o link da execução, o log, o pull request, o artefato ou o site publicado.

Se o Docker não estiver disponível, o `check.sh` avisa, confere apenas o YAML e indica `check.sh 00` para diagnosticar o ambiente.

### Publicar cada laboratório

Cada exercício usa um repositório público separado, de `actions-01` a `actions-07`, na sua conta. Continue no Codespace Blank preparado antes da aula. Na pasta do laboratório, depois de salvar e verificar o workflow:

```bash
git add .github/workflows/ci.yml
git commit -m "Configura workflow do exercício NN"
# Troque NN pelo número do exercício, por exemplo actions-02.
gh repo create actions-NN --public --source=. --remote=origin --push
gh browse --actions
```

O comando `gh repo create` é usado **uma vez por laboratório**. Para as alterações seguintes, use `git add`, `git commit` e `git push`. Se um nome já existir na sua conta, escolha outro, como `actions-02-turma-b`.

O botão **Run workflow** só aparece quando o workflow com `workflow_dispatch` está na branch padrão, `main`.

### Retomar depois de resetar

`reset.sh` também remove a configuração de `origin`, mas não altera o GitHub. Para uma nova tentativa do zero, publique com **outro nome**, por exemplo `gh repo create actions-02-tentativa-2 --public --source=. --remote=origin --push`. Isso evita misturar o histórico inicial com a tentativa já publicada. Para recuperar o trabalho publicado, clone o repositório em outra pasta do mesmo Codespace.

### Se o push falhar por permissão

Confira `git remote -v` e `gh auth status --hostname github.com`. Para um login antigo, sem o escopo `workflow`, execute no terminal do Codespace:

```bash
unset GH_TOKEN GITHUB_TOKEN
gh auth refresh --hostname github.com --scopes workflow
gh auth setup-git --hostname github.com
git push -u origin main
```

Se a conta estiver incorreta, use `gh auth login --hostname github.com --git-protocol https --web --scopes workflow`. O `GITHUB_TOKEN` **dentro de um workflow** é outra credencial, fornecida automaticamente pelo Actions para cada execução.

## Sequência da aula

| # | Exercício | Conceito novo | Tempo |
|---|---|---|---:|
| [00](https://fsilva-alt.github.io/devops-ghactions/#/d/00/1) | O ambiente está pronto? | Git, GitHub CLI, Docker e act (antes da aula) | 5 min |
| [01](https://fsilva-alt.github.io/devops-ghactions/#/d/01/1) | Primeiro workflow | YAML, evento manual, job, runner e step | 15 min |
| [02](https://fsilva-alt.github.io/devops-ghactions/#/d/02/1) | Testes no push | `push`, `checkout`, `setup-python`, `run` × `uses` | 25 min |
| [03](https://fsilva-alt.github.io/devops-ghactions/#/d/03/1) | Checks no pull request | `pull_request`, logs, falha e correção | 25 min |
| [04](https://fsilva-alt.github.io/devops-ghactions/#/d/04/1) | Variáveis e contextos | `env`, `inputs`, `github`, `vars`, `secrets` | 20 min |
| [05](https://fsilva-alt.github.io/devops-ghactions/#/d/05/1) | Jobs e dependências | `needs`, um runner por job, build | 20 min |
| [06](https://fsilva-alt.github.io/devops-ghactions/#/d/06/1) | Artefatos do build | Guardar e baixar os arquivos de uma execução | 20 min |
| [07](https://fsilva-alt.github.io/devops-ghactions/#/d/07/1) | Deploy no Pages | Publicação guiada, `permissions`, `environment` | 30 min |

Exercícios 01 a 07, com explicações: **155 minutos**. Abertura e introdução: 10; intervalo: 10; encerramento: 5. Total: **180 minutos**. O exercício 00 é feito antes da aula.

Cada exercício nos slides tem uma capa com o objetivo e a pasta, de um a três slides de conceito, um slide de comandos e documentação e a tarefa com passos numerados.

## Ao final

Guarde os links pedidos nos 7 exercícios, em especial o pull request com falha e correção do exercício 03 e a URL do site do exercício 07. Faça push de tudo que deseja manter e pare o Codespace. Excluí-lo libera o armazenamento, mas apaga os arquivos locais não publicados.

## Desenvolvimento do material

Os geradores dos laboratórios ficam em `scripts/labs.sh`; a análise do YAML, em `scripts/checks.py`; a simulação com o act, em `scripts/simular.py`; e o projeto do livro de receitas, em `templates/projeto/`. Os YAMLs do [gabarito](docs/gabarito.md) também servem de ponto de partida dos laboratórios e de entrada para os testes.

A configuração em `.devcontainer/` é usada na manutenção deste repositório. O aluno usa o modelo Blank e o instalador remoto, sem clonar o curso manualmente.

Em testes locais, `CURSO_AUTH_GITHUB=0` pula a autenticação e `CURSO_SIMULAR=0` dispensa o act e o Docker. `CURSO_MODO_TESTE=1` libera os scripts fora do Codespaces apenas para manutenção automatizada.

A apresentação está em `docs/index.html`, em um único arquivo, com a mesma estrutura de slides e navegação por teclado (`→`, `←`, `Esc`, `F`) e um seletor de tema claro ou escuro no canto superior direito.

```bash
bash tests/rodar.sh          # instalação, verificador, slides e projeto, sem conta GitHub nem Docker
bash tests/rodar.sh --docker # a mesma suíte em um Ubuntu limpo, dentro de um container
bash tests/rodar.sh --act    # simulação real com o act para o 00 e as 7 soluções; exige Docker
```

A suíte confere a instalação via `curl` e `sh -c` em um workspace vazio, a atualização do material, a preservação dos laboratórios, o atalho `labs`, a autenticação simulada, os YAMLs iniciais e resolvidos, erros comuns, a estrutura dos slides (com Node.js), os testes do projeto e o build. O modo de teste usa uma origem Git local e não cria repositórios no GitHub nem publica sites.

## Licença

[MIT](LICENSE).
