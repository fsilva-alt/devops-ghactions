---
duration: 7
---

# O ambiente está pronto?

{.lead}
Antes da aula, confira se o Codespace tem tudo: o Git com sua identidade, o GitHub CLI com permissão para enviar workflows, o Docker funcionando e o **act**, que simula os workflows. Também pratique o editor, criando um arquivo com um texto combinado. Fazer esta etapa com antecedência dá tempo de pedir ajuda.

`git config user.name` `gh auth status` `docker version` `act --version` `code meu-arquivo.txt` `check.sh 00`

::::columns
:::card Onde fazer
No terminal do Codespace, em **qualquer pasta**. Estes comandos conferem as ferramentas do Codespace e não dependem de arquivos da pasta atual.

A exceção é o arquivo `meu-arquivo.txt`: ele fica na sua pasta pessoal, `~`, onde o `check.sh 00` procura por ele.
:::
:::card Para este exercício
`⏱ tempo`
: 7 min · antes da aula

`módulo`
: Abertura · feito antes da aula, logo depois do instalador

`verificação`
: `check.sh 00`

`entrega`
: `check.sh 00` concluído
:::
::::

<p class="eyebrow">Conceito</p>

## Duas máquinas e um simulador

<div class="flow"><div class="node"><b>Codespace</b><small>onde você escreve o workflow</small></div><div class="arr"><span class="a">→</span>git push</div><div class="node hi"><b>GitHub</b><small>recebe o push e cria a execução</small></div><div class="arr"><span class="a">→</span>para cada job</div><div class="node"><b>runner</b><small>máquina nova, que roda as etapas</small></div></div>

<div class="netbox" data-label="no Codespace · check.sh"><div class="flow"><div class="node "><b>act</b><small>lê .github/workflows/ci.yml</small></div><div class="arr"><span class="a">→</span>cria</div><div class="node hi"><b>container Docker</b><small>imagem parecida com ubuntu-latest</small></div><div class="arr"><span class="a">→</span>cria</div><div class="node "><b>etapas</b><small>os mesmos comandos do runner</small></div></div></div>

:::card Por que simular?
Uma execução no GitHub leva alguns minutos e só começa depois do push. O `check.sh` usa o act para criar, no próprio Codespace, um **container** para cada job e rodar as etapas. Um erro de digitação aparece em segundos.

A imagem do runner local tem cerca de 2 GB; o instalador a baixa uma vez.
:::

:::note
**O que o act não faz:** não cria execuções no GitHub, não publica no Pages e não lê os segredos cadastrados no repositório. O `check.sh` usa valores de demonstração no lugar deles.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `git config user.name` | mostra o nome que vai nos seus commits; vazio significa não configurado |
| `gh auth status --hostname github.com` | mostra a conta conectada e os escopos do login |
| `gh auth refresh --hostname github.com --scopes workflow` | acrescenta o escopo workflow, necessário para enviar arquivos .github/workflows |
| `docker version` | mostra as seções Client e Server: o comando e o serviço do Docker |
| `act --version` | mostra a versão do simulador instalada pelo curso |
| `act -l` | lista os jobs e eventos dos workflows da pasta atual |
| `code meu-arquivo.txt` | abre o arquivo no editor; se ele não existir, é criado ao salvar |
| `cat meu-arquivo.txt` | mostra no terminal o conteúdo salvo do arquivo |
| `setup.sh` | cria os laboratórios ausentes e baixa o act e a imagem do runner local |

:::card Documentação
Links para consultar depois. A documentação do GitHub tem versão em português.

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

5. Pratique o editor, que você vai usar em todos os exercícios. Vá para a sua pasta pessoal e abra o arquivo `meu-arquivo.txt`. Ele ainda não existe; o editor cria o arquivo ao salvar:

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

6. Rode a verificação. Ela confere o arquivo, executa um workflow mínimo em um container e procura a mensagem **Olá do runner local!**:

   ```console
   $ check.sh 00
   ```
:::

:::card Verificação
```console
$ check.sh 00
```

Confere Git, login do `gh` com o escopo workflow, os 14 laboratórios, o Docker, o act, a imagem do runner local e o conteúdo de `~/meu-arquivo.txt`. Faltou algo? Siga a dica, execute `setup.sh` se ela pedir, e repita.
:::

:::note Arquivo não salvo?
Um **●** na aba do editor indica alterações que ainda não foram gravadas. Salve antes de rodar o `check.sh`.
:::

:::warning
**Depois, pare o Codespace** para não gastar a franquia. Em github.com/codespaces, clique em ⋯ e escolha *Stop codespace*. No dia da aula, basta abrir de novo; o act, a imagem e os laboratórios continuam lá.
:::

:::card Missão extra · opcional
```console
$ cd ~/labs/02-testes-no-push
$ act -l
```

O act lista o job `boas-vindas` e o evento `workflow_dispatch` do workflow inicial desse laboratório. No exercício 2, você troca esse workflow pelo de testes.
:::
