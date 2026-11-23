---
duration: 15
---

# Caminhos e agendamento

{.lead}
Escolher quando o workflow roda. Ele passa a ignorar os commits que só mudam o README e a rodar os testes toda segunda-feira, mesmo sem push, com um **agendamento**.

`paths-ignore` `schedule` `cron: 0 9 * * 1` `gh run list`

::::columns
:::card Onde fazer
```console
$ cd ~/labs/10-caminhos-e-agenda
```

O laboratório começa com o workflow de testes no push e no pull request.
:::
:::card Para este exercício
`⏱ tempo`
: 15 min · opcional

`módulo`
: Prática extra · Eventos

`verificação`
: `check.sh 10`

`entrega`
: push do README sem execução e push da receita com execução

Faça depois da aula, em qualquer ordem.
:::
::::

<p class="eyebrow">Conceito</p>

## Filtros de caminho

```yaml title="o evento push, dentro de on"
  push:
    branches: [main]
    paths-ignore:
      - 'README.md'
```

<div class="flow"><div class="node "><b>commit</b><small>muda só README.md</small></div><div class="arr"><span class="a">→</span></div><div class="node skip"><b>sem execução</b><small>todos os arquivos estão em paths-ignore</small></div></div>

<div class="flow"><div class="node "><b>commit</b><small>muda receitas/brigadeiro.md</small></div><div class="arr"><span class="a">→</span></div><div class="node ok"><b>execução</b><small>algum arquivo ficou fora da lista</small></div></div>

::::columns
:::card paths e paths-ignore
Com `paths`, o workflow só roda se o commit mudar algum dos arquivos listados. Com `paths-ignore`, ele roda sempre, a não ser que todos os arquivos mudados estejam na lista.
:::
:::card Padrões
Os dois aceitam padrões. `docs/**` é tudo dentro de `docs`, e `'*.md'` são os Markdown da raiz. Já `'**.md'` ignoraria também as receitas, que são Markdown.
:::
::::

:::note Use só um dos dois
No mesmo evento, use `paths` ou `paths-ignore`, nunca os dois.
:::

<p class="eyebrow">Conceito</p>

## Agendamento com cron

```yaml title="dentro de on"
  schedule:
    - cron: '0 9 * * 1'
```

| Campo | Significado |
| --- | --- |
| `0` | minuto |
| `9` | hora, em UTC |
| `*` | dia do mês: qualquer um |
| `*` | mês: qualquer um |
| `1` | dia da semana: segunda-feira (0 é domingo) |

::::columns
:::card Por que agendar testes?
Pacotes e imagens do runner mudam mesmo sem commits no repositório. Uma execução semanal mostra se algo deixou de funcionar.
:::
:::card O horário é UTC
9h em UTC são 6h em Brasília. O agendamento roda na branch padrão, a `main`, e pode atrasar alguns minutos em horários de muito uso.
:::
::::

:::warning O GitHub desativa agendamentos sem uso
Em um repositório público sem atividade por 60 dias, o `schedule` é desativado. Um botão na aba Actions reativa o agendamento.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `git log --stat -1` | mostra os arquivos mudados no último commit |
| `git push` | envia o commit; com paths-ignore, pode não gerar execução |
| `gh run list --limit 3` | lista as últimas execuções, com o evento de cada uma |

:::card Documentação
{.links}
- [Eventos que disparam workflows](https://docs.github.com/pt/actions/reference/workflows-and-actions/events-that-trigger-workflows)<small>push, pull\_request, workflow\_dispatch, schedule…</small>
- [Sintaxe de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-syntax)<small>on, jobs, runs-on, steps, needs, if, permissions</small>
- [crontab.guru · expressões cron](https://crontab.guru/)<small>confira o horário de um schedule · em inglês</small>
- [Comando · gh run list](https://cli.github.com/manual/gh_run_list)
:::

<p class="eyebrow">Tarefa · 15 min</p>

## O exercício

:::steps
1. Entre no laboratório e abra o workflow:

   ```console
   $ cd ~/labs/10-caminhos-e-agenda
   $ code .github/workflows/ci.yml
   ```

   Troque o bloco `on` pelo bloco abaixo, que acrescenta `paths-ignore` ao push e o evento `schedule`. Mantenha `permissions` e `jobs` como estão e salve:

   ```yaml title="substitua só o bloco on"
   on:
     push:
       branches: [main]
       paths-ignore:
         - 'README.md'
     pull_request:
       branches: [main]
     schedule:
       - cron: '0 9 * * 1'
     workflow_dispatch:
   ```

2. Rode a verificação. O `check.sh` simula o evento `schedule`, como o GitHub fará na segunda-feira:

   ```console
   $ check.sh 10
   ```

3. Publique. O primeiro push muda muitos arquivos e gera uma execução:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 10"
   $ gh repo create actions-10 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

4. Mude só o `README.md`, por exemplo acrescentando uma linha no fim, e envie. Nenhuma execução nova aparece:

   ```console
   $ code README.md
   $ git add README.md
   $ git commit -m "Atualiza o README"
   $ git push
   $ gh run list --limit 3
   ```

5. Agora mude uma receita, como o rendimento do brigadeiro, e envie. Este push gera uma execução:

   ```console
   $ code receitas/brigadeiro.md
   $ git add receitas/brigadeiro.md
   $ git commit -m "Ajusta o rendimento do brigadeiro"
   $ git push
   $ gh run list --limit 3
   ```
:::

:::card Verificação
```console
$ check.sh 10
```

Aprova quando o push tem `paths-ignore` com `README.md`, o `schedule` tem um cron de cinco campos e os testes ficam verdes em uma simulação do evento schedule.
:::

:::note Entrega
A aba Actions, ou a saída de `gh run list`, mostrando que o commit do README não gerou execução e o da receita gerou.
:::

:::card Missão extra · outro horário
```yaml title="troque a linha do cron"
    - cron: '0 15 * * *'
```

Essa expressão roda todo dia às 12h de Brasília. Confira a leitura dela em crontab.guru, nos links da referência, e envie com `git push`.
:::
