---
duration: 10
---

# Antes de começar

<p class="eyebrow">Introdução</p>

## Como acompanhar a aula

{.lead}
Você não precisa saber programar. O livro de receitas já vem pronto, com testes e um gerador de site. Na aula, você automatiza essas tarefas no GitHub.

::::columns
:::card Seu ambiente no navegador
O **Codespace** é um computador Linux acessado pela internet. Nele, o **VS Code** é o editor de arquivos, e o **terminal** é onde você digita comandos.

Abra o terminal em **Terminal → New Terminal**. A preparação completa está no [README do curso](https://github.com/fsilva-alt/devops-ghactions#antes-da-aula).
:::
:::card Comando ou conteúdo de arquivo?
Nos slides, o `$` marca uma linha de comando. Copie a linha sem esse símbolo, cole no terminal e pressione <kbd>Enter</kbd> para rodar. Use uma linha por vez.

Um bloco com o nome de um arquivo em cima, como `.github/workflows/ci.yml`, vai no editor. Salve com <kbd>Ctrl+S</kbd>, ou <kbd>Cmd+S</kbd> no Mac. Linhas que começam com `#` são comentários.
:::
:::card Como fazer os exercícios
Siga a tarefa na pasta indicada. Antes de publicar, rode `check.sh` com o número do exercício. Ele confere o YAML, simula o workflow no Codespace e mostra o que falta ajustar.

A entrega é o resultado no GitHub, como o link de uma execução. Os comandos de commit, branch e push estão completos nas tarefas. Os exercícios de 08 a 14 e a **Missão extra** são opcionais.
:::
::::

:::card Instale o material do curso
Todos os exercícios precisam do material instalado no Codespace. Rode esta linha uma vez no terminal e espere a mensagem **Curso de GitHub Actions instalado com sucesso!**:

```console
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"
```

O instalador prepara os laboratórios em `~/labs`, instala o simulador `act`, baixa a imagem que ele usa e faz o login do GitHub CLI. Depois, abra um terminal novo. Se você já instalou antes da aula, pule este passo.
:::

:::note Comandos para se localizar
`pwd` mostra em que pasta você está, `ls` lista o que há nela e `cd caminho` entra em outra pasta. O `~` é a sua pasta pessoal. Para abrir um arquivo no editor, use `code nome-do-arquivo`. Para abrir a pasta de um laboratório no VS Code, use `code ~/labs/NN-nome` e abra um terminal novo, que já começa nessa pasta.
:::

<p class="eyebrow">Introdução</p>

## O que é o GitHub Actions?

{.lead}
O **GitHub Actions** é o serviço de automação do GitHub. Em um arquivo do repositório, você descreve quais tarefas devem rodar quando acontece um evento, como um push, um pull request, um clique ou um horário agendado.

<figure class="anat" aria-label="Diagrama: um evento push dispara o workflow ci.yml; o workflow tem dois jobs, cada um em seu próprio runner; cada job tem steps, que são actions (uses) ou comandos (run)."><div class="camada ev"><div class="cab"><span class="peca ev">evento</span><b>push</b><small>um commit chega à main; o workflow declara em <code>on</code> quais eventos o iniciam</small></div></div><div class="seta"><span class="a">→</span>dispara</div><div class="camada wf"><div class="cab"><span class="peca wf">workflow</span><b>CI</b><code>.github/workflows/ci.yml</code></div><div class="runners"><div class="camada rn"><div class="cab"><span class="peca rn">runner</span><b>ubuntu-latest</b><small>uma máquina nova para este job</small></div><div class="camada jb"><div class="cab"><span class="peca jb">job</span><b>testar</b></div><ol><li><span class="peca st">step</span><code>uses: actions/checkout@v5</code><span class="peca ac">action</span></li><li><span class="peca st">step</span><code>uses: actions/setup-python@v6</code><span class="peca ac">action</span></li><li><span class="peca st">step</span><code>run: python -m unittest -v</code><span class="peca cm">comando</span></li></ol></div></div><div class="camada rn"><div class="cab"><span class="peca rn">runner</span><b>ubuntu-latest</b><small>outra máquina, só para este job</small></div><div class="camada jb"><div class="cab"><span class="peca jb">job</span><b>empacotar</b></div><ol><li><span class="peca st">step</span><code>uses: actions/checkout@v5</code><span class="peca ac">action</span></li><li><span class="peca st">step</span><code>run: python build.py</code><span class="peca cm">comando</span></li></ol></div></div></div></div></figure>

<ul class="anat-leg" aria-label="As peças de um workflow"><li><span class="peca ev">evento</span><span>o que inicia a execução; aparece em <code>on</code></span></li><li><span class="peca wf">workflow</span><span>o processo completo, descrito em um arquivo YAML</span></li><li><span class="peca jb">job</span><span>um grupo de etapas que roda em um runner</span></li><li><span class="peca st">step</span><span>uma etapa: um comando (<code>run</code>) ou uma action (<code>uses</code>)</span></li><li><span class="peca ac">action</span><span>um passo pronto e reutilizável, como baixar o código ou instalar o Python</span></li><li><span class="peca rn">runner</span><span>a máquina que executa o job; o GitHub fornece Linux, Windows e macOS</span></li></ul>

:::note O workflow fica no repositório
Ele é versionado como qualquer outro arquivo. Cada mudança na automação é um commit e pode ser revisada em um pull request.
:::

<p class="eyebrow">Introdução</p>

## Que problemas ele resolve?

{.lead}
Feitos à mão, os testes, o build e a publicação dependem de alguém lembrar de todos os passos, na ordem certa, a cada mudança. No Actions, os passos ficam escritos em um workflow, que roda automaticamente e registra cada execução.

::::columns
:::card Testes esquecidos
Os testes rodam a cada push e em cada pull request. O resultado aparece no PR como um **check** verde ou vermelho, antes de a mudança entrar na main.
:::
:::card Diferenças entre máquinas
Cada execução começa em um runner limpo, que instala só o que o workflow pede. Se o projeto depende de algo que só existe no seu computador, a execução falha e o erro fica no log.
:::
:::card Publicação feita à mão
O passo a passo da publicação fica escrito no YAML. O site sai sempre do commit que passou nos testes, e cada publicação registra quem fez e quando.
:::
:::card Tarefas repetitivas
O Actions também roda em horários marcados e reage a issues, pull requests e releases. Serve, por exemplo, para gerar relatórios ou atualizar dependências.
:::
::::

<p class="eyebrow">Introdução</p>

## O Actions em um processo de CI/CD

<div class="flow"><div class="node"><b>commit + push</b><small>uma mudança pequena</small></div><div class="arr"><span class="a">→</span>CI</div><div class="node hi"><b>testar</b><small>verifica cada mudança</small></div><div class="arr"><span class="a">→</span>build</div><div class="node hi"><b>empacotar</b><small>gera o resultado final</small></div><div class="arr"><span class="a">→</span>CD</div><div class="node hi"><b>publicar</b><small>entrega aos usuários</small></div></div>

::::columns
:::card CI · integração contínua
É a prática de integrar mudanças pequenas com frequência e verificar cada uma automaticamente. O workflow baixa o código, instala as dependências e roda os testes. O erro aparece minutos depois do push.
:::
:::card CD · entrega e implantação contínuas
Na **entrega contínua**, cada versão aprovada vira um pacote pronto para publicar. Na **implantação contínua**, a publicação também é automática. O site deste curso é publicado assim.
:::
:::card O papel do Actions
CI/CD é um conjunto de práticas de desenvolvimento. O Actions é a ferramenta que executa os passos. No curso, o módulo de integração contínua trata dos testes, e o de entrega contínua, do build e da publicação.
:::
::::

<p class="eyebrow">Introdução</p>

## Como ele é usado na prática?

{.lead}
Em uma equipe, os workflows acompanham o fluxo de trabalho com Git. Os testes rodam nos pull requests, e a publicação acontece quando a mudança chega à main.

<div class="flow"><div class="node "><b>branch</b><small>você trabalha em uma cópia da main</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>pull request</b><small>o Actions roda os testes: check</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>revisão</b><small>alguém lê o código e o check</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>merge na main</b><small>o Actions gera e publica</small></div></div>

:::note Regra de proteção
O repositório pode exigir checks verdes antes do merge. Assim, a main só recebe mudanças que passaram nos testes. No curso, os checks não bloqueiam o merge.
:::

<p class="eyebrow">Introdução</p>

## De onde veio o GitHub Actions?

{.lead}
A integração contínua é mais antiga que o GitHub Actions. O Actions levou a automação para dentro do repositório, ao lado do código, dos pull requests e das issues.

::::columns
:::card Integração contínua
<p class="up">Anos 2000</p>

Martin Fowler descreve a integração contínua. Servidores de build passam a testar cada mudança, em máquinas separadas.
:::
:::card Primeira versão do Actions
<p class="up">Outubro de 2018</p>

O GitHub apresenta o Actions, com automações configuradas no repositório e disparadas pelos eventos do GitHub.
:::
:::card Lançamento com CI/CD
<p class="up">Novembro de 2019</p>

O Actions é lançado com workflows em YAML, runners hospedados pelo GitHub e uso gratuito em repositórios públicos.
:::
::::

<p class="eyebrow">Introdução</p>

## O que ainda precisa de cuidado?

::::columns
:::card Minutos e custos
Em repositórios públicos, os runners padrão não têm custo. Os privados têm uma franquia de minutos por mês. A franquia do Codespace é separada.
:::
:::card Segredos
Senhas e tokens nunca vão no YAML, porque quem acessa o repositório lê o arquivo. Eles são cadastrados como **secrets** e chegam só às etapas que os pedem. Você pratica isso no exercício 4.
:::
:::card Permissões
Cada execução recebe uma credencial temporária, o `GITHUB_TOKEN`. O bloco `permissions` limita o que ela pode fazer. Nos exercícios, o workflow começa só com leitura.
:::
:::card Actions de terceiros
Passos comuns, como baixar o código, já existem como **actions** no Marketplace. Uma action é código de outra pessoa rodando no seu workflow. Prefira as oficiais ou verificadas e fixe a versão depois do `@`.
:::
:::card Limites dos testes
O workflow só verifica o que os testes cobrem. Um teste fraco passa mesmo com o programa errado, então você ainda precisa escrever bons testes.
:::
:::card Limites da simulação local
O act, usado pelo `check.sh`, não publica no Pages nem lê seus segredos. A entrega é sempre a execução no GitHub.
:::
::::

<p class="eyebrow">Introdução</p>

## Codespaces, Actions, act e Pages

<div class="flow"><div class="node"><b>Codespace</b><small>você edita, testa e simula com o act</small></div><div class="arr"><span class="a">→</span>git push</div><div class="node hi"><b>GitHub Actions</b><small>cria a execução e um runner para cada job</small></div><div class="arr"><span class="a">→</span>deploy</div><div class="node"><b>GitHub Pages</b><small>o site em uma URL pública</small></div></div>

`Codespace`
: É o computador da aula, onde ficam os laboratórios e rodam os comandos `check.sh`, `git` e `gh`.

`runner`
: É a máquina que o GitHub cria para cada job. Ela começa vazia e é descartada no fim da execução.

`act`
: É um programa que lê o mesmo YAML e roda os jobs em containers Docker no Codespace, para você ver os erros antes do push.

`GitHub Pages`
: É a hospedagem de sites do GitHub. No exercício 7, o workflow publica o livro de receitas nela.

:::note Para acompanhar
Você precisa de uma conta no GitHub e do Codespace preparado como explica o README. Cada exercício vai para um repositório público seu, de `actions-01` a `actions-07`, e os opcionais vão até `actions-14`.
:::

:::note Para ver a execução
A aba **Actions** do repositório lista as execuções. O comando `gh browse --actions` abre essa aba no navegador.
:::

:::card Para ler depois
A documentação do GitHub tem versão em português.

{.links}
- [Entender o GitHub Actions](https://docs.github.com/pt/actions/get-started/understand-github-actions)<small>eventos, workflows, jobs, actions e runners</small>
- [Integração contínua](https://docs.github.com/pt/actions/get-started/continuous-integration)<small>o que é CI e como o Actions ajuda</small>
- [Implantação contínua](https://docs.github.com/pt/actions/get-started/continuous-deployment)<small>o que é CD e como publicar com workflows</small>
- [Martin Fowler · Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)<small>o artigo que popularizou a prática · em inglês</small>
- [GitHub Blog · Actions passa a ter CI/CD](https://github.blog/news-insights/product-news/github-actions-now-supports-ci-cd/)<small>o anúncio de 2019 · em inglês</small>
- [act · executar workflows localmente](https://nektosact.com/)<small>o simulador usado pelo check.sh · em inglês</small>
:::
