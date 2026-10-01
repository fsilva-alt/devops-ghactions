# Guia do aluno

## Antes da aula

1. Siga a seção [Antes da aula](../README.md#antes-da-aula) para criar um Codespace com o modelo **Blank** e executar o instalador.
2. Conclua o login do GitHub CLI com a conta que usará para publicar os exercícios.
3. Abra um terminal novo, execute `gh auth status --hostname github.com` e depois `check.sh 01`. Antes do exercício 01, é esperado que o verificador informe a ausência do workflow.
4. Pare o Codespace em [github.com/codespaces](https://github.com/codespaces), em **⋯ → Stop codespace**. No dia da aula, reabra o mesmo ambiente.

## Como acompanhar os exercícios

- Siga a sequência **01 → 02 → 03 → 04 → 05 → 06 → 07**.
- Leia o objetivo e o estado inicial, entre na pasta indicada e execute uma etapa por vez.
- Comandos dos blocos `bash` vão no terminal. O conteúdo dos blocos `yaml` vai no arquivo `.github/workflows/ci.yml` do laboratório.
- Salve os arquivos com **Ctrl+S**, ou **Cmd+S** no Mac, antes de executar o verificador ou fazer commit.
- Execute `check.sh NN`, substituindo `NN` pelo número do exercício. Corrija o que for indicado e verifique novamente.
- Publique o laboratório no GitHub e confira a entrega descrita no enunciado. Um check local aprovado não comprova que o workflow executou corretamente no Actions.

Cada laboratório tem seu próprio estado inicial. Você pode iniciar o próximo exercício mesmo que não tenha concluído o anterior. O exercício 04 demonstra variáveis e contextos; os exercícios 05 a 07 retomam testes, build e publicação.

## Onde você está trabalhando?

| Lugar | O que fazer ali |
|---|---|
| Terminal do Codespace | Executar `git`, `gh`, `cd`, `check.sh` e os comandos dos enunciados |
| Editor do VS Code | Criar e salvar workflows e alterações no projeto |
| Aba Actions, no GitHub | Acompanhar execuções, consultar logs e baixar artefatos |
| Aba Pull requests, no GitHub | Consultar os checks da proposta de alteração |
| GitHub Pages | Abrir o site publicado no exercício 07 |

O **runner** é a máquina que executa o workflow. Ele é separado do Codespace: arquivos e pacotes instalados no Codespace não aparecem automaticamente no runner.

`pwd` mostra a pasta atual, `ls` lista seu conteúdo e `cd caminho` muda de pasta. Para abrir um arquivo no editor, use `code nome-do-arquivo`.

O material fica em `~/devops-ghactions`, e os arquivos da prática ficam em `~/labs`. O atalho `labs`, criado na pasta em que o instalador foi executado, aponta para os mesmos arquivos. Os enunciados estão nos [slides HTML](https://fsilva-alt.github.io/devops-ghactions/); selecione o exercício no índice. A cópia local está em `~/devops-ghactions/docs/index.html`.

## Comandos de apoio

| Comando | Quando usar |
|---|---|
| `check.sh NN` | Conferir o YAML do laboratório e receber orientações de correção |
| `setup.sh` | Criar os laboratórios que ainda não existem |
| `reset.sh NN` | Apagar o trabalho local de um laboratório e recriar seus arquivos iniciais |

Dentro de um laboratório, `check.sh` e `reset.sh` funcionam sem o número. Após um reset, execute novamente o `cd` do enunciado.

O instalador pode ser executado novamente para atualizar o material. Ele preserva os laboratórios existentes. Para receber um novo estado inicial, guarde as alterações que deseja manter e execute `reset.sh NN` depois da atualização. O reset remove também o remoto local `origin`, mas não apaga o repositório publicado no GitHub. Consulte [Retomar depois de resetar](../README.md#retomar-depois-de-resetar).

## Publicação dos exercícios

Cada laboratório é publicado em um repositório público separado, de `actions-01` a `actions-07`. Execute `gh repo create` apenas na primeira publicação de cada laboratório. Para as alterações seguintes, use `git add`, `git commit` e `git push`, conforme o enunciado.

Continue no mesmo Codespace Blank durante toda a aula. Os repositórios publicados não precisam de outros Codespaces.

## Problemas comuns

| Mensagem ou situação | Como resolver |
|---|---|
| `check.sh: command not found` | Abra um terminal novo ou execute `source ~/.bashrc`. No zsh, use `source ~/.zshrc`. |
| Instalador interrompido | Corrija a causa indicada no terminal e execute novamente o comando de instalação do README. |
| `Author identity unknown` | Configure seu nome e e-mail conforme a preparação do README. |
| Push recusado por permissão | Consulte [Se o push falhar por permissão](../README.md#se-o-push-falhar-por-permissão) e confira a conta e o escopo `workflow`. |
| Repositório já existe | Se já publicou esse laboratório, use `git push`. Para uma nova tentativa, escolha outro nome. |
| Botão Run workflow ausente | Confirme que o workflow contém `workflow_dispatch` e foi publicado na branch padrão `main`. |
| `Invalid workflow file` | Confira a linha indicada, a indentação com espaços e as chaves do YAML. |
| Correção não aparece no Actions | Salve o arquivo, faça commit e push. Reexecutar um commit antigo usa o código daquele commit. |
| `CURSO_TOKEN` ausente | Cadastre o segredo fictício no repositório `actions-04`, em Settings → Secrets and variables → Actions. |
| Pasta não encontrada após `reset.sh` | Entre novamente na pasta com o `cd` do enunciado. |
| Site do exercício 07 não abre | Aguarde o deploy e confira Settings → Pages → Source: GitHub Actions. Leia os logs se houver falha. |

Ao pedir ajuda, informe o exercício, o comando executado e a mensagem completa do terminal ou o link da execução no Actions.

## Ao terminar

1. Salve os links das entregas e faça push das alterações que deseja manter.
2. Pare o Codespace. Mesmo parado, ele ocupa armazenamento; excluí-lo apaga arquivos locais que não foram publicados.
3. Para revisar, consulte o [gabarito](gabarito.md) e a [documentação oficial do GitHub Actions](https://docs.github.com/pt/actions).
