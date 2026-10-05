---
duration: 15
---

# Primeiro workflow

{.lead}
Escrever o primeiro workflow, executá-lo com um clique na aba **Actions** e encontrar, no log do runner, a mensagem que ele mostrou.

`on: workflow_dispatch` `runs-on: ubuntu-latest` `steps · run` `gh repo create` `Run workflow`

::::columns
:::card Onde fazer
No terminal do Codespace, na pasta do laboratório:

```console
$ cd ~/labs/01-primeiro-workflow
```

A pasta tem o livro de receitas pronto e a pasta `.github/workflows/` vazia. É nela que o GitHub procura os workflows.
:::
:::card Para este exercício
`⏱ tempo`
: 15 min

`módulo`
: Módulo 1 · Fundamentos

`verificação`
: `check.sh 01`

`entrega`
: link da execução manual verde
:::
::::

<p class="eyebrow">Conceito</p>

## Evento, workflow, job e step

<div class="flow"><div class="node "><b>workflow_dispatch</b><small>o evento: um clique em Run workflow</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>workflow Boas-vindas</b><small>o arquivo ci.yml</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>job boas-vindas</b><small>roda em um runner ubuntu-latest</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>step</b><small>echo "Olá, GitHub Actions!"</small></div></div>

::::columns
:::card O evento inicia a execução
`workflow_dispatch` é o evento manual: aparece como o botão **Run workflow** na aba Actions. Os próximos exercícios usam `push` e `pull_request`, que disparam o workflow automaticamente.
:::
:::card Jobs rodam em runners
Cada job recebe uma máquina nova. `runs-on: ubuntu-latest` pede um Linux hospedado pelo GitHub, com ferramentas comuns já instaladas.
:::
:::card Steps rodam em ordem
As etapas de um job executam uma depois da outra, na mesma máquina. Se uma falha, as seguintes não rodam e o job fica vermelho.
:::
::::

:::note O echo não roda no Codespace.
No Codespace você escreve e publica o arquivo. Quem executa o comando é o runner, em outra máquina; o resultado aparece no log da execução.
:::

<p class="eyebrow">Conceito</p>

## Como ler o YAML

```yaml title=".github/workflows/ci.yml"
name: Boas-vindas

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  boas-vindas:
    runs-on: ubuntu-latest
    steps:
      - name: Cumprimentar a turma
        run: echo "Olá, GitHub Actions!"
```

:::card Linha a linha
| Chave | O que define |
| --- | --- |
| `name` | o nome que aparece na aba Actions |
| `on` | os eventos que iniciam o workflow |
| `permissions` | o que a credencial da execução pode fazer: aqui, só ler o repositório |
| `jobs` | os jobs; `boas-vindas` é o nome deste |
| `runs-on` | o tipo de runner do job |
| `steps` | a lista de etapas; cada uma começa com um traço |
| `run` | o comando executado no runner |
:::

:::note A indentação faz parte do YAML.
Ela mostra o que pertence a quê: `runs-on` pertence ao job, que pertence a `jobs`. Use espaços, nunca tabulação.
:::

<p class="eyebrow">Conceito</p>

## Execuções, jobs e logs

<div class="flow"><div class="node "><b>aba Actions</b><small>todos os workflows do repositório</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>execução</b><small>cada vez que o workflow rodou · run</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>job</b><small>boas-vindas, com status e duração</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>step</b><small>Cumprimentar a turma</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>log</b><small>a saída do comando, linha a linha</small></div></div>

::::columns
:::card Cada clique é uma execução
Uma **execução** (run) registra o evento, o commit, quem a iniciou, a duração e o resultado de cada job. O link dela é a sua entrega neste exercício.
:::
:::card O botão Run workflow
Aparece quando o workflow com `workflow_dispatch` está na **branch padrão**, a `main`. Por isso o primeiro push vem antes do clique.
:::
:::card Verde, vermelho, amarelo
✓ verde: terminou sem erro. ✗ vermelho: alguma etapa falhou. ● amarelo: ainda em execução ou na fila, esperando um runner.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `code .github/workflows/ci.yml` | abre (ou cria, ao salvar) o arquivo do workflow no editor |
| `check.sh 01` | confere o YAML e simula o job com o act |
| `git add <arquivo>` | prepara o arquivo para o próximo commit |
| `git commit -m "<mensagem>"` | registra a versão com uma mensagem |
| `gh repo create <nome> --public --source=. --remote=origin --push` | cria o repositório no GitHub e envia o commit; uma vez por laboratório |
| `gh browse --actions` | abre a aba Actions do repositório no navegador |
| `gh run list` | lista as execuções no terminal |

:::card Documentação
Links para consultar depois. A documentação do GitHub tem versão em português.

{.links}
- [Entender o GitHub Actions](https://docs.github.com/pt/actions/get-started/understand-github-actions)<small>eventos, workflows, jobs, actions e runners</small>
- [Início rápido do GitHub Actions](https://docs.github.com/pt/actions/get-started/quickstart)<small>o primeiro workflow, passo a passo</small>
- [Sintaxe de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-syntax)<small>on, jobs, runs-on, steps, needs, if, permissions</small>
- [Executar um workflow manualmente](https://docs.github.com/pt/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)<small>o botão Run workflow e o gh workflow run</small>
- [Como ler os logs de uma execução](https://docs.github.com/pt/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Comando · gh repo create](https://cli.github.com/manual/gh_repo_create)
:::

<p class="eyebrow">Tarefa · 15 min</p>

## O exercício

:::steps
1. Entre no laboratório e abra o arquivo do workflow. Ele ainda não existe; o editor cria o arquivo ao salvar:

   ```console
   $ cd ~/labs/01-primeiro-workflow
   $ code .github/workflows/ci.yml
   ```

2. Copie o YAML abaixo para o editor e salve com <kbd>Ctrl+S</kbd>. É o mesmo do slide **Como ler o YAML**; mantenha os espaços no início das linhas:

   ```yaml title=".github/workflows/ci.yml"
   name: Boas-vindas

   on:
     workflow_dispatch:

   permissions:
     contents: read

   jobs:
     boas-vindas:
       runs-on: ubuntu-latest
       steps:
         - name: Cumprimentar a turma
           run: echo "Olá, GitHub Actions!"
   ```

3. Confira e simule. Procure **Olá, GitHub Actions!** na saída do job:

   ```console
   $ check.sh 01
   ```

4. Faça o commit e publique em um repositório novo:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 01"
   $ gh repo create actions-01 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

5. Na aba Actions, clique em **Boas-vindas → Run workflow**, deixe a branch `main` e confirme. Abra a execução, o job `boas-vindas` e a etapa **Cumprimentar a turma**. Guarde o link da execução.
:::

:::card Verificação
```console
$ check.sh 01
```

Aprova com o evento manual, `permissions` de leitura e a etapa da saudação, e quando a simulação mostra a mensagem no log.
:::

:::note
**Sem execução depois do push:** o resultado está correto, porque o único evento deste workflow é o manual. A execução começa no clique em Run workflow.
:::

:::card Missão extra
```yaml title="acrescente no fim de steps"
      - name: Listar arquivos
        run: ls -la
```

Rode `check.sh 01`: a lista sai vazia. O runner começa sem os arquivos do repositório; no exercício 2, `actions/checkout` resolve isso.
:::
