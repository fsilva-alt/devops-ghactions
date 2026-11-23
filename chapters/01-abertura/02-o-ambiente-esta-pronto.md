---
duration: 7
---

# O ambiente está pronto?

{.lead}
Confirmar que o Codespace tem o que a aula usa: o Git com a sua identidade, o GitHub CLI com permissão para enviar workflows, o Docker e o **act**, que simula os workflows. Faça antes da aula, para ter tempo de pedir ajuda.

`git config user.name` `gh auth status` `docker version` `act --version` `code meu-arquivo.txt` `check.sh 00`

::::columns
:::card Onde fazer
No terminal do Codespace, em qualquer pasta, logo depois de rodar o [instalador](01-antes-de-comecar.md#como-acompanhar-a-aula).

Só o arquivo `meu-arquivo.txt` tem lugar certo. Ele fica na sua pasta pessoal, `~`, onde o `check.sh 00` procura por ele.
:::
:::card Para este exercício
`⏱ tempo`
: 7 min · antes da aula

`módulo`
: Abertura

`verificação`
: `check.sh 00`

`entrega`
: `check.sh 00` concluído
:::
::::

<p class="eyebrow">Conceito</p>

## Onde o workflow roda

<div class="flow"><div class="node"><b>Codespace</b><small>onde você escreve o workflow</small></div><div class="arr"><span class="a">→</span>git push</div><div class="node hi"><b>GitHub</b><small>recebe o push e cria a execução</small></div><div class="arr"><span class="a">→</span>para cada job</div><div class="node"><b>runner</b><small>máquina nova, que roda as etapas</small></div></div>

<div class="netbox" data-label="no Codespace · check.sh"><div class="flow"><div class="node "><b>act</b><small>lê .github/workflows/ci.yml</small></div><div class="arr"><span class="a">→</span>cria</div><div class="node hi"><b>container Docker</b><small>imagem parecida com ubuntu-latest</small></div><div class="arr"><span class="a">→</span>cria</div><div class="node "><b>etapas</b><small>os mesmos comandos do runner</small></div></div></div>

:::card Por que simular?
Uma execução no GitHub só começa depois do push e leva alguns minutos. Com o act, o `check.sh` cria um **container** para cada job no próprio Codespace e roda as mesmas etapas. Um erro de digitação aparece em segundos.

A imagem do runner local tem cerca de 2 GB e é baixada uma vez pelo instalador.
:::

:::note O que o act não faz
Ele não cria execuções no GitHub, não publica no Pages e não lê os segredos cadastrados no repositório. No lugar dos segredos, o `check.sh` usa valores de demonstração.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `git config user.name` | mostra o nome que vai nos seus commits; vazio quer dizer que falta configurar |
| `gh auth status --hostname github.com` | mostra a conta conectada e os escopos do login |
| `gh auth refresh --hostname github.com --scopes workflow` | acrescenta o escopo workflow, necessário para enviar arquivos .github/workflows |
| `docker version` | mostra as seções Client e Server: o comando e o serviço do Docker |
| `act --version` | mostra a versão do simulador instalada pelo curso |
| `act -l` | lista os jobs e eventos dos workflows da pasta atual |
| `code meu-arquivo.txt` | abre o arquivo no editor; se ele não existir, é criado ao salvar |
| `cat meu-arquivo.txt` | mostra no terminal o conteúdo salvo do arquivo |
| `setup.sh` | cria os laboratórios ausentes e baixa o act e a imagem do runner local |

:::card Documentação
{.links}
- [Comando · gh auth status](https://cli.github.com/manual/gh_auth_status)
- [Visão geral do GitHub Codespaces](https://docs.github.com/pt/codespaces/overview)
- [act · executar workflows localmente](https://nektosact.com/)<small>o simulador usado pelo check.sh · em inglês</small>
- [Repositório do curso](https://github.com/fsilva-alt/devops-ghactions)<small>gabarito, guia do aluno e scripts</small>
:::

<p class="eyebrow">Tarefa · 7 min</p>

## O exercício

:::steps
1. Confira sua identidade no Git. Se algum valor vier vazio, configure com seus dados:

   ```console
   $ git config user.name
   $ git config user.email
   $ git config --global user.name "Seu nome"
   ```

2. Confira o login do GitHub CLI. Procure sua conta e o escopo `'workflow'` em *Token scopes*:

   ```console
   $ gh auth status --hostname github.com
   ```

3. Confira o Docker. Devem aparecer as seções **Client** e **Server**:

   ```console
   $ docker version
   ```

4. Confira o act, instalado pelo curso:

   ```console
   $ act --version
   ```

5. Pratique o editor, que você vai usar em todos os exercícios. Na sua pasta pessoal, abra `meu-arquivo.txt`. O arquivo ainda não existe, e o editor o cria quando você salva:

   ```console
   $ cd ~
   $ code meu-arquivo.txt
   ```

   Copie a linha abaixo para o editor, sem mudar nada, e salve com <kbd>Ctrl+S</kbd>. Confira no terminal:

   ```text title="~/meu-arquivo.txt"
   Estou pronto para a aula de GitHub Actions!
   ```

   ```console
   $ cat meu-arquivo.txt
   ```
:::

:::card Verificação
```console
$ check.sh 00
```

Confere o Git, o login do `gh` com o escopo workflow, os 14 laboratórios, o Docker, o act, a imagem do runner local e o conteúdo de `~/meu-arquivo.txt`. Depois roda um workflow mínimo em um container e procura a mensagem **Olá do runner local!**. Se faltar algo, siga a dica e repita.
:::

:::note Arquivo não salvo?
Um **●** na aba do editor indica alterações que ainda não foram salvas. Salve antes de rodar o `check.sh`.
:::

:::warning Depois, pare o Codespace
Assim você não gasta a franquia. Em github.com/codespaces, clique em ⋯ e escolha *Stop codespace*. No dia da aula, abra o mesmo Codespace. O act, a imagem e os laboratórios continuam nele.
:::

:::card Missão extra · opcional
```console
$ code ~/labs/02-testes-no-push
```

O VS Code abre a pasta do laboratório. Nessa janela, abra um terminal em **Terminal → New Terminal**, que já começa na pasta:

```console
$ act -l
```

O act lista o job `boas-vindas` e o evento `workflow_dispatch` do workflow inicial desse laboratório. No exercício 2, você troca esse workflow pelo de testes.
:::
