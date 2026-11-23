---
duration: 15
---

# Cache de dependências

{.lead}
Guardar os pacotes baixados pelo pip em um **cache**. O job `empacotar` e as próximas execuções instalam a partir da cópia guardada, em vez de baixar tudo de novo.

`actions/setup-python` `cache: pip` `Cache restored` `gh cache list`

::::columns
:::card Onde fazer
```console
$ code ~/labs/09-cache-de-dependencias
```

O laboratório começa com o workflow de `testar` e `empacotar` do exercício 5, que instala as dependências duas vezes.
:::
:::card Para este exercício
`⏱ tempo`
: 15 min · opcional

`módulo`
: Prática extra · Integração contínua

`verificação`
: `check.sh 09`

`entrega`
: execução com o cache restaurado no job empacotar

Faça depois da aula, em qualquer ordem.
:::
::::

<p class="eyebrow">Conceito</p>

## Como o cache funciona

<div class="flow"><div class="node "><b>testar</b><small>cache não encontrado · baixa e salva</small></div><div class="arr"><span class="a">→</span></div><div class="node hi"><b>cache do pip</b><small>guardado pelo GitHub</small></div><div class="arr"><span class="a">→</span></div><div class="node ok"><b>empacotar</b><small>cache restaurado · usa a cópia</small></div></div>

```yaml title="o setup-python de testar e de empacotar"
      - uses: actions/setup-python@v6
        with:
          python-version: '3.12'
          cache: pip
```

::::columns
:::card A chave do cache
O setup-python monta uma **chave** com o sistema, a versão do Python e um resumo (hash) do `requirements.txt`. Se o arquivo muda, a chave também muda. O cache antigo deixa de servir, e um novo é salvo no fim do job.
:::
:::card Diferença para o artefato
O artefato, do exercício 6, é o resultado de uma execução. O cache só acelera as próximas e pode ser apagado a qualquer momento, então o workflow precisa funcionar sem ele.
:::
::::

:::note O checkout vem antes
A chave depende do `requirements.txt`, que só existe no runner depois do `actions/checkout`.
:::

<p class="eyebrow">Conceito</p>

## Como conferir o cache

```text
# No log do setup-python, no job empacotar:
Cache restored from key: setup-python-Linux-x64-…-pip-…
# No log da instalação, o pip usa a cópia:
Using cached markdown-3.8.2-py3-none-any.whl
# No fim do job testar, na primeira execução:
Cache saved with the key: setup-python-Linux-x64-…-pip-…
```

```console
$ gh cache list
```

::::columns
:::card A primeira execução já usa o cache
`testar` não encontra cache, instala e salva um no fim do job. `empacotar`, que espera `testar` por causa do `needs`, já encontra e restaura esse cache.
:::
:::card Onde ficam e quanto duram
Os caches aparecem na aba **Actions**, em *Caches*, e em `gh cache list`. Os que ficam 7 dias sem uso são apagados, e cada repositório tem um limite de espaço. Um cache criado na main serve às outras branches, mas o de uma branch não serve à main.
:::
::::

<p class="eyebrow">Referência</p>

## Comandos e documentação

| Comando | Para quê |
| --- | --- |
| `gh run view --log` | mostra o log completo; procure Cache restored e Using cached |
| `gh cache list` | lista os caches do repositório, com chave e tamanho |
| `gh run rerun` | repete uma execução escolhida da lista |

:::card Documentação
{.links}
- [Cache de dependências](https://docs.github.com/pt/actions/reference/workflows-and-actions/dependency-caching)<small>chaves, restauração e limites do cache</small>
- [Action · actions/setup-python](https://github.com/actions/setup-python)
- [Comando · gh cache list](https://cli.github.com/manual/gh_cache_list)
- [Artefatos de workflow](https://docs.github.com/pt/actions/concepts/workflows-and-actions/workflow-artifacts)<small>guardar e baixar arquivos de uma execução</small>
:::

<p class="eyebrow">Tarefa · 15 min</p>

## O exercício

:::steps
1. Abra o laboratório no VS Code:

   ```console
   $ code ~/labs/09-cache-de-dependencias
   ```

   Na janela do laboratório, abra um terminal em **Terminal → New Terminal** e abra o workflow:

   ```console
   $ code .github/workflows/ci.yml
   ```

   Nos dois jobs, `testar` e `empacotar`, acrescente `cache: pip` ao `with` do setup-python, alinhado com `python-version`. Cada setup-python fica como abaixo. Salve:

   ```yaml title="o setup-python de testar e de empacotar"
         - uses: actions/setup-python@v6
           with:
             python-version: '3.12'
             cache: pip
   ```

2. Rode a verificação. Os dois jobs devem terminar verdes:

   ```console
   $ check.sh 09
   ```

3. Publique e abra a execução:

   ```console
   $ git add .github/workflows/ci.yml
   $ git commit -m "Configura workflow do exercício 09"
   $ gh repo create actions-09 --public --source=. --remote=origin --push
   $ gh browse --actions
   ```

4. No job `empacotar`, abra a etapa **Run actions/setup-python** e procure `Cache restored`. Na instalação, procure `Using cached`. Depois, liste os caches do repositório:

   ```console
   $ gh cache list
   ```
:::

:::card Verificação
```console
$ check.sh 09
```

Aprova quando o setup-python dos dois jobs tem `cache: pip`, depois do checkout, e os dois jobs ficam verdes na simulação.
:::

:::note Entrega
O link da execução em que `empacotar` restaura o cache e a saída de `gh cache list`.
:::

:::card Missão extra · repetir a execução
```console
$ gh run rerun
```

Escolha a execução da lista. Desta vez, `testar` também mostra `Cache restored`, porque o cache salvo na primeira tentativa continua disponível.
:::
