---
duration: 25
---

# Checks no pull request

{.lead}
Fazer os testes rodarem em cada **pull request**, provocar uma falha de propósito, encontrar a causa no log e corrigir antes do merge.

`on: pull_request` `git switch -c` `gh pr create` `gh pr checks` `logs`

::::columns
:::card Onde fazer
No terminal do Codespace, na pasta do laboratório:

```console
$ cd ~/labs/03-checks-no-pull-request
```

Ponto de partida: o workflow de testes no push, com o cálculo correto.
:::
:::card Para este exercício
`⏱ tempo`
: 25 min

`módulo`
: Módulo 2 · Integração contínua

`verificação`
: `check.sh 03`

`entrega`
: PR com uma execução vermelha e uma verde
:::
::::

<p class="eyebrow">Conceito</p>

## Checks no pull request

<div class="flow"><div class="node "><b>branch teste-do-ci</b><small>a mudança proposta</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>pull request → main</b><small>evento pull_request</small></div><div class="arr"><span class="a">→</span></div><div class="node fail"><b>check testar</b><small>resultado no PR</small></div></div>

```yaml title="substitua só o bloco on"
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

::::columns
:::card O que é um check
Cada job que roda por um pull request aparece no PR como um **check**: verde, vermelho ou em andamento. Quem revisa vê o resultado dos testes antes de aprovar o merge.
:::
:::card branches indica o destino
Em `pull_request`, o filtro `branches: [main]` vale para PRs que **têm a main como destino**. Cada push na branch do PR atualiza o PR e gera um novo check.
:::
::::

:::note Um check vermelho impede o merge?
Só quando uma regra do repositório exige aquele check. Neste exercício, o objetivo é ler e interpretar o resultado.
:::

<p class="eyebrow">Conceito</p>

## Da falha à causa

```diff
# Falha proposital em receitas.py:
- return gramas_por_receita * receitas
+ return gramas_por_receita + receitas
```

```text
# No log da etapa Testar:
FAIL: test_tres_receitas_de_pao_de_queijo
    self.assertEqual(quantidade_para(500, 3), 1500)
AssertionError: 503 != 1500
```

<div class="flow"><div class="node fail"><b>check vermelho</b></div><div class="arr"><span class="a">→</span></div><div class="node "><b>corrigir + push</b><small>novo commit na branch</small></div><div class="arr"><span class="a">→</span></div><div class="node ok"><b>check verde</b></div></div>

:::card Como ler o erro
Abra o job e a etapa que falhou. Procure o nome do teste, a linha indicada e os dois valores comparados: o teste esperava **1500** e recebeu **503**.

O teste está certo: 3 receitas de 500 g são 1500 g. O código somou em vez de multiplicar.
:::

:::note Reexecutar não corrige.
Cada execução pertence a um commit. O botão *Re-run* repete o mesmo commit quebrado; a correção precisa de um novo commit e push.
:::

:::card Guarde as duas evidências
A execução antiga continua mostrando a falha, e a nova mostra a correção. Os dois links registram o problema e a solução.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `check.sh 03` | confere o YAML e simula um pull\_request para a main |
| `git switch -c <branch>` | cria uma branch e entra nela |
| `git push -u origin <branch>` | publica a branch e liga ao remoto |
| `gh pr create --base main --fill` | abre o PR para a main, com a mensagem do commit |
| `gh pr view --web` | abre o PR da branch atual no navegador |
| `gh pr checks` | mostra os checks do PR no terminal |
| `gh run view --log-failed` | mostra só o log das etapas que falharam |

:::card Documentação
Links para consultar depois. A documentação do GitHub tem versão em português.

{.links}
- [Eventos que disparam workflows](https://docs.github.com/pt/actions/reference/workflows-and-actions/events-that-trigger-workflows)<small>push, pull\_request, workflow\_dispatch, schedule…</small>
- [Como ler os logs de uma execução](https://docs.github.com/pt/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Comando · gh pr create](https://cli.github.com/manual/gh_pr_create)
- [Comando · gh pr checks](https://cli.github.com/manual/gh_pr_checks)
- [Comando · gh run view](https://cli.github.com/manual/gh_run_view)<small>--log, --log-failed</small>
:::

<p class="eyebrow">Tarefa · 25 min</p>

## O exercício

:::steps
1. Entre no laboratório e abra o workflow:

   ```console
   $ cd ~/labs/03-checks-no-pull-request
   $ code .github/workflows/ci.yml
   ```

   Troque o bloco `on` pelo bloco abaixo, que acrescenta `pull_request`. Mantenha `permissions` e `jobs` como estão e salve:

   ```yaml title="substitua só o bloco on"
   on:
     push:
       branches: [main]
     pull_request:
       branches: [main]
     workflow_dispatch:
   ```

2. Confira e publique a main:

   ```console
   $ check.sh 03
   ```

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 03"
   $ gh repo create actions-03 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

3. Crie a branch e provoque a falha: em `receitas.py`, troque `*` por `+` na conta e salve. O `check.sh` já mostra o erro; é esperado:

   ```console
   $ git switch -c teste-do-ci
   $ code receitas.py
   $ check.sh 03
   ```

4. Envie a falha mesmo assim e abra o PR:

   ```console
   $ git add receitas.py
   $ git commit -m "Demonstra falha no cálculo"
   $ git push -u origin teste-do-ci
   $ gh pr create --base main --fill
   $ gh pr view --web
   ```

5. Espere o check vermelho. Em **Checks → testar → Testar**, encontre `503 != 1500` e guarde o link da execução.

6. Volte a multiplicação, confira e envie a correção na mesma branch. O PR ganha um check verde:

   ```console
   $ check.sh 03
   $ git add receitas.py
   $ git commit -m "Corrige o cálculo da quantidade"
   $ git push
   ```
:::

:::card Verificação
```console
$ check.sh 03
```

Aprova com `push` e `pull_request` para a main e com os testes aprovados em uma simulação de PR. Com a falha proposital, reprova mostrando o mesmo erro do GitHub.
:::

:::note
**Entrega:** o link do PR e das execuções vermelha e verde, com uma frase explicando qual linha causava o erro. O PR pode ficar aberto.
:::

:::card Missão extra
```console
$ gh pr checks
$ gh run view --log-failed
```

Os mesmos resultados, no terminal. No segundo comando, escolha a execução vermelha da lista.
:::
