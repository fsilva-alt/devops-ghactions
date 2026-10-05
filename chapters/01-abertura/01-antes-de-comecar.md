---
duration: 10
---

# Antes de começar

<p class="eyebrow">Introdução</p>

## Como acompanhar a aula

{.lead}
Você não precisa saber programar. O livro de receitas já vem pronto, com testes e um gerador de site. O curso trata da **automação** dessas tarefas no GitHub.

::::columns
:::card Seu ambiente no navegador
O **Codespace** é um computador Linux acessado pela internet. Nele, o **VS Code** é o editor de arquivos, e o **terminal** é a área onde você digita comandos.

Abra o terminal em **Terminal → New Terminal**. A preparação completa está no [README do curso](https://github.com/fsilva-alt/devops-ghactions#antes-da-aula).
:::
:::card Comando ou conteúdo de arquivo?
Nos slides, `$` marca uma linha para executar no terminal. Copie o comando sem esse símbolo e pressione <kbd>Enter</kbd>. Execute uma linha por vez.

Blocos com o nome de um arquivo em cima, como `.github/workflows/ci.yml`, vão **no editor**. Salve com <kbd>Ctrl+S</kbd> ou <kbd>Cmd+S</kbd> no Mac. Linhas com `#` são comentários.
:::
:::card Como fazer os exercícios
Leia o objetivo, consulte os comandos e siga a tarefa na pasta indicada. Antes de publicar, execute `check.sh` com o número do exercício: ele confere o YAML e **simula o workflow no Codespace**, mostrando o que ajustar.

A entrega de cada exercício é a execução no GitHub: um link, um log, um artefato ou o site publicado. Você precisa conhecer o básico de commit, branch e push; os comandos completos estão nas tarefas.

Os exercícios de 08 a 14 e a **Missão extra** de cada tarefa são **opcionais**, para praticar depois da aula.
:::
::::

:::card Instale o material do curso
Execute esta linha uma única vez no terminal do Codespace. O instalador prepara os laboratórios em `~/labs`, instala o simulador `act`, baixa a imagem que ele usa e faz o login do GitHub CLI.

```console
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"
```

Espere aparecer **Curso de GitHub Actions instalado com sucesso!** e abra um terminal novo antes de continuar. Se você já instalou antes da aula, pule esta etapa.
:::

:::note Comandos para se localizar:
`pwd` mostra a pasta atual; `ls` lista seu conteúdo; `cd caminho` entra em outra pasta. O símbolo `~` representa sua pasta pessoal. Para abrir um arquivo no editor, use `code nome-do-arquivo`.
:::

<p class="eyebrow">Introdução</p>

## O que é o GitHub Actions?

{.lead}
O **GitHub Actions** é o serviço de automação do GitHub. Você descreve, em um arquivo do próprio repositório, **quais tarefas executar** quando ocorre um evento: um push, um pull request, um clique ou um horário agendado.

<figure class="anat" aria-label="Diagrama: um evento push dispara o workflow ci.yml; o workflow tem dois jobs, cada um em seu próprio runner; cada job tem steps, que são actions (uses) ou comandos (run)."><div class="camada ev"><div class="cab"><span class="peca ev">evento</span><b>push</b><small>um commit chega à main; o workflow declara em <code>on</code> quais eventos o iniciam</small></div></div><div class="seta"><span class="a">→</span>dispara</div><div class="camada wf"><div class="cab"><span class="peca wf">workflow</span><b>CI</b><code>.github/workflows/ci.yml</code></div><div class="runners"><div class="camada rn"><div class="cab"><span class="peca rn">runner</span><b>ubuntu-latest</b><small>uma máquina nova para este job</small></div><div class="camada jb"><div class="cab"><span class="peca jb">job</span><b>testar</b></div><ol><li><span class="peca st">step</span><code>uses: actions/checkout@v5</code><span class="peca ac">action</span></li><li><span class="peca st">step</span><code>uses: actions/setup-python@v6</code><span class="peca ac">action</span></li><li><span class="peca st">step</span><code>run: python -m unittest -v</code><span class="peca cm">comando</span></li></ol></div></div><div class="camada rn"><div class="cab"><span class="peca rn">runner</span><b>ubuntu-latest</b><small>outra máquina, só para este job</small></div><div class="camada jb"><div class="cab"><span class="peca jb">job</span><b>empacotar</b></div><ol><li><span class="peca st">step</span><code>uses: actions/checkout@v5</code><span class="peca ac">action</span></li><li><span class="peca st">step</span><code>run: python build.py</code><span class="peca cm">comando</span></li></ol></div></div></div></div></figure>

<ul class="anat-leg" aria-label="As peças de um workflow"><li><span class="peca ev">evento</span><span>o que inicia a execução; aparece em <code>on</code></span></li><li><span class="peca wf">workflow</span><span>o processo completo, descrito em um arquivo YAML</span></li><li><span class="peca jb">job</span><span>um grupo de etapas que roda em um runner</span></li><li><span class="peca st">step</span><span>uma etapa: um comando (<code>run</code>) ou uma action (<code>uses</code>)</span></li><li><span class="peca ac">action</span><span>um passo pronto e reutilizável, como baixar o código ou instalar o Python</span></li><li><span class="peca rn">runner</span><span>a máquina que executa o job; o GitHub fornece Linux, Windows e macOS</span></li></ul>

:::note O workflow fica no repositório.
Como qualquer arquivo, ele é versionado: cada mudança na automação é um commit e pode ser revisada em um pull request.
:::

<p class="eyebrow">Introdução</p>

## Que problemas ele resolve?

{.lead}
Quando testes, build e publicação são feitos à mão, o resultado depende de alguém executar todos os passos, na ordem certa, a cada mudança. Com o Actions, esses passos ficam descritos em um workflow, que é **executado automaticamente** e registrado a cada vez.

::::columns
:::card Testes esquecidos
- Os testes rodam a cada push e em cada pull request
- Todos os commits passam pela mesma verificação
:::
:::card Diferenças entre máquinas
- Cada execução começa em um runner limpo
- O runner instala só o que o workflow pede
- Dependência que só existe no seu computador: a execução falha e o erro fica no log
:::
:::card Erros encontrados depois do merge
- O resultado aparece no pull request como um **check** verde ou vermelho
- O erro aparece antes de a mudança entrar na main
- Quem revisa vê os testes junto com o código
:::
:::card Publicação dependente de uma pessoa
- O passo a passo da publicação fica escrito no YAML
- Qualquer pessoa da equipe consegue ler, revisar e repetir
- Cada publicação registra quem, quando e qual commit
:::
:::card Publicação da versão errada
- O site é gerado a partir do commit que passou nos testes
- Sempre pelo mesmo processo
- Nenhuma cópia de arquivos feita à mão
:::
:::card Tarefas repetitivas
- Além de CI/CD: execuções em horários marcados
- Reações a issues, pull requests e releases
- Exemplos: gerar relatórios, organizar etiquetas, atualizar dependências
:::
::::

<p class="eyebrow">Introdução</p>

## O Actions em um processo de CI/CD

<div class="flow"><div class="node"><b>commit + push</b><small>uma mudança pequena</small></div><div class="arr"><span class="a">→</span>CI</div><div class="node hi"><b>testar</b><small>verifica cada mudança</small></div><div class="arr"><span class="a">→</span>build</div><div class="node hi"><b>empacotar</b><small>gera o resultado final</small></div><div class="arr"><span class="a">→</span>CD</div><div class="node hi"><b>publicar</b><small>entrega aos usuários</small></div></div>

::::columns
:::card CI · integração contínua
- Integrar mudanças pequenas, com frequência
- Verificar **cada uma automaticamente**: baixar o código, instalar as dependências, rodar os testes
- O erro aparece minutos depois do push, com a mudança ainda recente
:::
:::card CD · entrega e implantação contínuas
- **Entrega contínua**: cada versão aprovada vira um pacote pronto para publicar
- **Implantação contínua**: a publicação também é automática
- O site deste curso usa a implantação contínua
:::
:::card O papel do Actions
- CI/CD é um conjunto de **práticas** de desenvolvimento
- O Actions é a **ferramenta** que executa os passos do workflow
- A qualidade do resultado depende dos testes e do tamanho das mudanças
:::
::::

| Exercício | Parte do caminho |
| --- | --- |
| `02 · 03` | CI: testes a cada push e checks nos pull requests |
| `04` | configuração: variáveis, contextos e segredos |
| `05 · 06` | build: jobs em sequência e artefato com o site |
| `07` | CD: o site publicado no GitHub Pages a cada mudança na main |
| `08 a 14` | opcionais: matriz, cache, agendamento, anotações, saídas, ação composta e release |

<p class="eyebrow">Introdução</p>

## Como ele é usado na prática?

{.lead}
Em uma equipe, os workflows seguem o fluxo de trabalho com Git: os testes rodam nos **pull requests**, e a publicação acontece quando a mudança chega à **main**.

<div class="flow"><div class="node "><b>branch</b><small>você trabalha em uma cópia da main</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>pull request</b><small>o Actions roda os testes: check</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>revisão</b><small>alguém lê o código e o check</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>merge na main</b><small>o Actions gera e publica</small></div></div>

:::note
**Regra de proteção:** o repositório pode exigir checks verdes antes do merge. Assim, a main recebe apenas mudanças que passaram na verificação. No curso, os checks são observados, não obrigatórios.
:::

::::columns
:::card No pull request: verificar
Testes e verificações rápidas em cada atualização do PR. O resultado aparece na aba **Checks** e na lista de commits.
:::
:::card Na main: entregar
Depois do merge, o workflow gera o resultado e publica. Um **environment** identifica o destino, como produção, e pode exigir aprovação.
:::
:::card Actions prontas
Passos comuns, como baixar o código ou instalar o Python, já existem como **actions** prontas no Marketplace. O workflow só as chama com `uses`, com uma versão fixa.
:::
::::

<p class="eyebrow">Introdução</p>

## De onde veio o GitHub Actions?

{.lead}
A integração contínua é anterior ao GitHub Actions. Ele trouxe a automação para **dentro do repositório**, ao lado do código, dos pull requests e das issues.

::::columns
:::card Integração contínua
<p class="up">Anos 2000</p>

Martin Fowler descreve a integração contínua. Servidores de build passam a testar cada mudança, em máquinas separadas.
:::
:::card Nasce o Actions
<p class="up">Outubro de 2018</p>

O GitHub apresenta o Actions: automações configuradas no repositório, disparadas pelos eventos do GitHub.
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
- Repositórios públicos: runners padrão sem custo
- Repositórios privados: franquia de minutos por mês
- O Codespace tem uma franquia separada
:::
:::card Segredos
- Senhas e tokens nunca vão no YAML: quem acessa o repositório lê o arquivo
- Eles são cadastrados como **secrets**
- Chegam só às etapas que os pedem
- Na prática: exercício 4
:::
:::card Permissões
- Cada execução recebe uma credencial temporária: o `GITHUB_TOKEN`
- O bloco `permissions` limita o que ela pode fazer
- Nos exercícios, o workflow começa só com leitura
:::
:::card Actions de terceiros
- Uma action é código de outra pessoa rodando no seu workflow
- Prefira actions oficiais ou verificadas
- Fixe a versão depois do `@`
:::
:::card Limites dos testes
- O workflow só verifica o que os testes cobrem
- Um teste fraco passa mesmo com o programa errado
- Automatizar não substitui escrever bons testes
:::
:::card Limites da simulação local
- O `check.sh` usa o **act**: os jobs rodam em containers Docker no Codespace
- Não publica no Pages nem lê seus segredos
- A entrega é sempre a execução no GitHub
:::
::::

<p class="eyebrow">Introdução</p>

## Codespaces, Actions, act e Pages

<div class="flow"><div class="node"><b>Codespace</b><small>você edita, testa e simula com o act</small></div><div class="arr"><span class="a">→</span>git push</div><div class="node hi"><b>GitHub Actions</b><small>cria a execução e um runner para cada job</small></div><div class="arr"><span class="a">→</span>deploy</div><div class="node"><b>GitHub Pages</b><small>o site em uma URL pública</small></div></div>

`Codespace`
: O computador da aula. Nele ficam os laboratórios e rodam os comandos `check.sh`, `git` e `gh`.

`runner`
: A máquina criada pelo GitHub para cada job. Começa vazia e é descartada no fim da execução.

`act`
: Um programa que lê o mesmo YAML e executa os jobs em containers Docker no Codespace. Serve para ver erros antes do push.

`GitHub Pages`
: A hospedagem de sites do GitHub. No exercício 7, o próprio workflow publica o livro de receitas.

:::note
**Para acompanhar:** tenha sua conta no GitHub e o Codespace preparado conforme o README. Cada exercício é publicado em um repositório público seu, de `actions-01` a `actions-07`; os opcionais seguem até `actions-14`.
:::

:::note
**Para ver a execução:** a aba **Actions** do repositório lista as execuções. O comando `gh browse --actions` abre essa aba no navegador.
:::

:::card Para ler depois
Links para consultar depois. A documentação do GitHub tem versão em português.

{.links}
- [Entender o GitHub Actions](https://docs.github.com/pt/actions/get-started/understand-github-actions)<small>eventos, workflows, jobs, actions e runners</small>
- [Integração contínua](https://docs.github.com/pt/actions/get-started/continuous-integration)<small>o que é CI e como o Actions ajuda</small>
- [Implantação contínua](https://docs.github.com/pt/actions/get-started/continuous-deployment)<small>o que é CD e como publicar com workflows</small>
- [Martin Fowler · Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)<small>o artigo que popularizou a prática · em inglês</small>
- [GitHub Blog · Actions passa a ter CI/CD](https://github.blog/news-insights/product-news/github-actions-now-supports-ci-cd/)<small>o anúncio de 2019 · em inglês</small>
- [act · executar workflows localmente](https://nektosact.com/)<small>o simulador usado pelo check.sh · em inglês</small>
:::
