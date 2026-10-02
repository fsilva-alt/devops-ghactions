# Guia do aluno

## Antes da aula

1. Siga a seção [Antes da aula](../README.md#antes-da-aula) do README para criar um Codespace com o modelo **Blank** e executar o instalador.
2. Conclua o login do GitHub CLI com a conta que usará para publicar os exercícios.
3. Abra um terminal novo e execute `check.sh 00`. Se aparecer uma dica, siga a orientação e repita o comando. Ao pedir ajuda, envie o comando executado e a mensagem completa do terminal.
4. Pare o Codespace em [github.com/codespaces](https://github.com/codespaces), no menu **⋯ → Stop codespace**. No dia da aula, abra o mesmo Codespace.

## Como acompanhar os exercícios

- Comece pelo slide **Como acompanhar a aula**. Ele apresenta o terminal, o editor, o instalador e a diferença entre um comando e o conteúdo de um arquivo.
- Siga a sequência **01 → 02 → 03 → 04 → 05 → 06 → 07**. Cada exercício tem uma capa, slides de conceito, um slide de comandos e documentação e a tarefa com passos numerados.
- Em cada exercício, leia o objetivo, entre na pasta indicada e execute uma etapa por vez.
- Nos slides, o `$` marca um comando: copie a linha sem esse símbolo. Blocos com o nome de um arquivo em cima, como `.github/workflows/ci.yml`, vão no editor.
- Salve os arquivos com **Ctrl+S**, ou **Cmd+S** no Mac, antes de executar o `check.sh` ou fazer commit.
- Antes de publicar, execute `check.sh NN`, trocando `NN` pelo número do exercício. Corrija o que for indicado e repita.
- Publique o laboratório e confira a entrega descrita na tarefa. A simulação local não substitui a execução no GitHub.

Cada laboratório tem seu próprio estado inicial, e é possível começar um exercício sem ter concluído o anterior. O exercício 04 é uma demonstração de configuração; os exercícios 05 a 07 retomam os testes, o build e a publicação do livro de receitas.

## Onde você está trabalhando?

| Lugar | O que fazer ali |
|---|---|
| Terminal do Codespace | Executar `git`, `gh`, `cd`, `check.sh` e os comandos das tarefas |
| Editor do VS Code | Criar e salvar workflows, receitas e alterações em `livro.md` e `receitas.py` |
| Aba Actions, no GitHub | Acompanhar execuções, ler logs e baixar artefatos |
| Aba Pull requests, no GitHub | Consultar os checks de uma proposta de mudança |
| GitHub Pages | Abrir o site publicado no exercício 07 |

O **runner** é a máquina que executa os jobs no GitHub. Ele é separado do Codespace: arquivos e pacotes instalados no Codespace não aparecem no runner.

O **act** executa os mesmos jobs no Codespace, em containers Docker, quando você roda `check.sh`. Ele serve para encontrar erros antes do push. Não publica no Pages nem lê as variáveis e os segredos cadastrados no repositório.

`pwd` mostra a pasta atual, `ls` lista seu conteúdo e `cd caminho` muda de pasta. Para abrir um arquivo no editor, use `code nome-do-arquivo`.

O material fica em `~/devops-ghactions`, e os arquivos da prática ficam em `~/labs`. O atalho `labs`, criado na pasta em que o instalador foi executado, aponta para os mesmos arquivos. Os enunciados estão nos [slides](https://fsilva-alt.github.io/devops-ghactions/); a cópia local fica em `~/devops-ghactions/docs/index.html`.

## Comandos de apoio

| Comando | Quando usar |
|---|---|
| `check.sh NN` | Conferir o YAML, simular o workflow e receber orientações de correção |
| `check.sh NN --sem-act` | Conferir apenas o YAML, sem executar os jobs |
| `check.sh 00` | Diagnosticar o ambiente: Git, `gh`, Docker, act e laboratórios |
| `setup.sh` | Criar os laboratórios que ainda não existem e baixar o act e sua imagem |
| `reset.sh NN` | Apagar o trabalho local de um laboratório e recriar seus arquivos iniciais |

Dentro de um laboratório, `check.sh` e `reset.sh` funcionam sem o número. Depois de um reset, execute de novo o `cd` do enunciado.

O instalador pode ser executado novamente para atualizar o material; ele preserva os laboratórios existentes. Para receber um novo estado inicial, guarde as alterações que deseja manter e execute `reset.sh NN`. O reset também remove o remoto local `origin`, mas não apaga o repositório publicado no GitHub. Consulte [Retomar depois de resetar](../README.md#retomar-depois-de-resetar).

## Publicação dos exercícios

Cada laboratório é publicado em um repositório público separado, de `actions-01` a `actions-07`. Execute `gh repo create` apenas na primeira publicação de cada laboratório. Para as alterações seguintes, use `git add`, `git commit` e `git push`, conforme a tarefa.

Use o mesmo Codespace Blank durante toda a aula.

## Problemas comuns

| Mensagem ou situação | Como resolver |
|---|---|
| `check.sh: command not found` | Abra um terminal novo ou execute `source ~/.bashrc`. No zsh, use `source ~/.zshrc`. |
| Instalador interrompido | Corrija a causa indicada no terminal e execute novamente o comando de instalação do README. |
| `Simulação com o act pulada` | O Docker ou o act não estão disponíveis. Execute `check.sh 00` e siga as dicas; em um Codespace recém-aberto, espere um minuto. |
| Simulação demorada na primeira vez | O act baixa a imagem do runner local, com cerca de 2 GB, e as actions usadas pelo workflow. As execuções seguintes levam poucos segundos. |
| Simulação aprovada e falha no GitHub | Abra a etapa com falha no log da execução. A entrega considerada é a do GitHub. |
| `Author identity unknown` | Configure seu nome e e-mail conforme a preparação do README. |
| Push recusado por permissão | Consulte [Se o push falhar por permissão](../README.md#se-o-push-falhar-por-permissão) e confira a conta e o escopo `workflow`. |
| Repositório já existe | Se esse laboratório já foi publicado, use `git push`. Para uma nova tentativa, escolha outro nome. |
| Botão Run workflow ausente | Confirme que o workflow contém `workflow_dispatch` e foi publicado na branch padrão, `main`. |
| `Invalid workflow file` | Confira a linha indicada, a indentação com espaços e as chaves do YAML. |
| Correção não aparece no Actions | Salve o arquivo, faça commit e push. Reexecutar um commit antigo usa o código daquele commit. |
| `CURSO_TOKEN` ausente | Cadastre o segredo fictício no repositório `actions-04` com `gh secret set CURSO_TOKEN --body "somente-demonstracao"`. |
| Pasta não encontrada depois de `reset.sh` | Entre novamente na pasta com o `cd` do enunciado. |
| Site do exercício 07 não abre | Aguarde o fim do deploy e confira **Settings → Pages → Source: GitHub Actions**. Se houver falha, leia o log. |

Ao pedir ajuda, informe o exercício, o comando executado e a mensagem completa do terminal ou o link da execução no Actions.

## Ao terminar

1. Guarde os links das entregas e faça push das alterações que deseja manter.
2. Pare o Codespace. Mesmo parado, ele ocupa armazenamento; excluí-lo apaga os arquivos locais que não foram publicados.
3. Para revisar, consulte o [gabarito](gabarito.md) e a [documentação oficial do GitHub Actions](https://docs.github.com/pt/actions).
