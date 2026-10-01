# 05 — Jobs e dependências

**20 minutos · Ambiente obrigatório: GitHub Codespaces**

## Objetivo

Gerar o site somente depois que os testes passarem, usando dois jobs.

## Onde e estado inicial

```bash
cd ~/labs-actions/05-jobs-e-dependencias
code .github/workflows/ci.yml
```

O CI já testa pushes e PRs. `build.py` converte `cardapio.md` em `dist/index.html`. Esse processo de produzir o resultado distribuível é chamado de **build**.

## Tarefa

1. Preserve o job `testar`. Acrescente este segundo job **dentro de `jobs`, no mesmo nível de `testar`**:

   ```yaml
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

   O trecho acima não é um workflow inteiro: indente-o dois espaços abaixo de `jobs:`. `test -s` retorna sucesso se o arquivo existe e não está vazio.

2. Confira e publique:

   ```bash
   check.sh 05
   git add .github/workflows/ci.yml
   git commit -m "Gera o site depois dos testes"
   gh repo create actions-05 --public --source=. --remote=origin --push
   gh browse --actions
   ```

3. Abra o grafo da execução: `testar → empacotar`. O segundo job espera o primeiro terminar com sucesso.
4. Reproduza a falha do exercício 03: em `app.py`, troque o `*` do retorno por `+`, faça commit e push na `main`. Observe `testar` falhar e `empacotar` ficar **skipped** (pulado).
5. Corrija a linha para multiplicação, faça outro commit e push. Termine com os dois jobs verdes.

## Por que preparar o ambiente duas vezes?

Cada job recebe seu próprio runner. Os arquivos, o Python configurado e os pacotes de `testar` não são compartilhados automaticamente com `empacotar`. Já as etapas dentro de um mesmo job compartilham seus arquivos.

Sem `needs`, jobs podem rodar em paralelo. Com `needs: testar`, o build fica dependente do resultado dos testes.

## Verificação e entrega

`check.sh 05` aprova os requisitos locais. Entregue a execução final verde e a anterior com build pulado. Explique por que há checkout e instalação nos dois jobs.

O arquivo gerado ainda está somente no runner. No próximo exercício você vai guardá-lo depois da execução.

[Próximo: artefatos do build →](../06-artefatos-do-build/README.md) · [Índice](../../README.md)
