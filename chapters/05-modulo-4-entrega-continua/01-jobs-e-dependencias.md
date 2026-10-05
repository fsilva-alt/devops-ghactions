---
duration: 20
---

# Jobs e dependências

{.lead}
Acrescentar um segundo job, que gera o site do livro de receitas, e fazê-lo **esperar os testes**: se eles falharem, o build não começa.

`needs: testar` `python build.py` `test -s` `skipped`

::::columns
:::card Onde fazer
No terminal do Codespace, na pasta do laboratório:

```console
$ cd ~/labs/05-jobs-e-dependencias
```

Ponto de partida: o workflow com testes no push e no pull request.
:::
:::card Para este exercício
`⏱ tempo`
: 20 min

`módulo`
: Módulo 4 · Entrega contínua

`verificação`
: `check.sh 05`

`entrega`
: execução verde e uma com o build pulado
:::
::::

<p class="eyebrow">Conceito</p>

## Jobs em sequência

::::columns
:::column
### Testes aprovados

<div class="flow"><div class="node ok"><b>testar</b><small>3 testes</small></div><div class="arr"><span class="a">→</span>needs</div><div class="node ok"><b>empacotar</b><small>gera o site</small></div></div>
:::
:::column
### Testes reprovados

<div class="flow"><div class="node fail"><b>testar</b><small>503 != 1500</small></div><div class="arr"><span class="a">→</span>needs</div><div class="node skip"><b>empacotar</b><small>skipped · pulado</small></div></div>
:::
::::

::::columns
:::card needs cria a ordem
Sem `needs`, os jobs de um workflow rodam **ao mesmo tempo**. Com `needs: testar`, o job `empacotar` espera e só começa se `testar` terminar com sucesso.
:::
:::card Cada job, um runner novo
Jobs não compartilham arquivos: o `empacotar` recebe outra máquina vazia. Por isso ele repete checkout, Python e dependências. `needs` define a ordem, mas não copia nada.
:::
:::card Pulado não é falha
Quando um job anterior falha, os dependentes aparecem como **skipped**. O grafo da execução mostra os dois estados lado a lado.
:::
::::

<p class="eyebrow">Conceito</p>

## O build do livro

```yaml title="dentro de jobs, no mesmo nível de testar"
  empacotar:
    needs: testar
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-python@v6
        with:
          python-version: '3.12'
      - run: python -m pip install -r requirements.txt
      - run: python build.py
      - name: Conferir o arquivo gerado
        run: test -s dist/index.html
```

<div class="flow"><div class="node "><b>livro.md + receitas/*.md</b><small>os textos do livro</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>build.py</b><small>Markdown → HTML</small></div><div class="arr"><span class="a">→</span></div><div class="node "><b>dist/index.html</b><small>o site pronto</small></div></div>

:::card O que é o build
**Build** é gerar o resultado final a partir dos arquivos do projeto. Aqui, `build.py` junta o título de `livro.md` e as receitas da pasta `receitas/` em uma página HTML.
:::

:::note
**test -s** retorna sucesso quando o arquivo existe e não está vazio. O site ainda fica só no runner, que é descartado no fim; o exercício 6 guarda esse resultado.
:::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `check.sh 05` | confere o YAML e simula os dois jobs, na ordem do needs |
| `python build.py` | gera dist/index.html (precisa do Markdown instalado) |
| `python -m http.server -d dist 8000` | serve o site gerado na porta 8000 do Codespace |
| `gh run view` | mostra os jobs de uma execução e seus estados |
| `git push` | envia o commit e dispara a execução |

:::card Documentação
Links para consultar depois. A documentação do GitHub tem versão em português.

{.links}
- [Como usar jobs em um workflow](https://docs.github.com/pt/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs)<small>needs e jobs em paralelo</small>
- [Sintaxe de workflow](https://docs.github.com/pt/actions/reference/workflows-and-actions/workflow-syntax)<small>on, jobs, runs-on, steps, needs, if, permissions</small>
- [Integração contínua](https://docs.github.com/pt/actions/get-started/continuous-integration)<small>o que é CI e como o Actions ajuda</small>
- [Comando · gh run view](https://cli.github.com/manual/gh_run_view)<small>--log, --log-failed</small>
:::

<p class="eyebrow">Tarefa · 20 min</p>

## O exercício

:::steps
1. Entre no laboratório e abra o workflow:

   ```console
   $ cd ~/labs/05-jobs-e-dependencias
   $ code .github/workflows/ci.yml
   ```

   Cole o job `empacotar` abaixo no **fim do arquivo**, sem apagar `testar`. A linha `empacotar:` começa com dois espaços, alinhada com `testar:`. Salve:

   ```yaml title="acrescente no fim do arquivo, dentro de jobs"
     empacotar:
       needs: testar
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
         - uses: actions/setup-python@v6
           with:
             python-version: '3.12'
         - run: python -m pip install -r requirements.txt
         - run: python build.py
         - name: Conferir o arquivo gerado
           run: test -s dist/index.html
   ```

2. Simule; o log mostra `testar` e depois `empacotar`:

   ```console
   $ check.sh 05
   ```

3. Publique e abra o grafo da execução:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 05"
   $ gh repo create actions-05 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

4. Quebre o cálculo de propósito: em `receitas.py`, troque `*` por `+`. Simule: `testar` falha e `empacotar` é pulado. Envie mesmo assim e veja o mesmo no GitHub:

   ```console
   $ code receitas.py
   $ check.sh 05
   $ git add receitas.py
   $ git commit -m "Demonstra o build pulado"
   $ git push
   ```

5. Volte a multiplicação, confira e envie. A execução termina com os dois jobs verdes:

   ```console
   $ check.sh 05
   $ git add receitas.py
   $ git commit -m "Corrige o cálculo da quantidade"
   $ git push
   ```
:::

:::card Verificação
```console
$ check.sh 05
```

Aprova com `needs: testar`, o build depois das dependências e os dois jobs verdes na simulação. Com o erro, mostra o build pulado, como o GitHub.
:::

:::note
**Entrega:** o link da execução final verde e o da execução com `empacotar` pulado.
:::

:::card Missão extra · o site no navegador
```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
$ python build.py
$ python -m http.server -d dist 8000
```

Abra o endereço da porta 8000 na aba PORTS, ao lado de TERMINAL. <kbd>Ctrl+C</kbd> para o servidor.
:::
