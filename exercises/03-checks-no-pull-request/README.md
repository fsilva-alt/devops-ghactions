# 03 — Checks no pull request

**25 minutos · Ambiente obrigatório: GitHub Codespaces**

## Objetivo

Testar uma mudança antes de integrá-la à `main`, encontrar uma falha no log e corrigi-la.

## Onde e estado inicial

```bash
cd ~/labs-actions/03-checks-no-pull-request
code .github/workflows/ci.yml
```

O laboratório já tem o CI do exercício 02: testa pushes para `main`, mas não PRs.

## Tarefa

1. Acrescente o evento `pull_request`, no mesmo nível de `push`, preservando o restante do arquivo:

   ```yaml
   on:
     push:
       branches: [main]
     pull_request:
       branches: [main]
     workflow_dispatch:
   ```

   Em `pull_request`, `branches` filtra o **destino do PR**. Ao abrir ou atualizar um PR para `main`, o GitHub executa os testes. Não é necessário fazer merge para receber o resultado.

2. Publique primeiro o workflow na `main`:

   ```bash
   check.sh 03
   git add .github/workflows/ci.yml
   git commit -m "Testa pull requests destinados à main"
   gh repo create actions-03 --public --source=. --remote=origin --push
   ```

3. Crie uma branch e introduza uma falha proposital. Em `app.py`, troque **apenas** `return preco_centavos * quantidade` por `return preco_centavos + quantidade`:

   ```bash
   git switch -c teste-do-ci
   code app.py
   # Depois de salvar a troca de * por +:
   git add app.py
   git commit -m "Demonstra erro no cálculo"
   git push -u origin teste-do-ci
   gh pr create --base main --title "Pratica checks do CI" --body "Vou observar uma falha e corrigi-la."
   gh pr view --web
   ```

4. No PR, abra **Checks → testar → Testar**. Leia o erro e registre o link da execução vermelha. Qual resultado o teste esperava? Qual recebeu?
5. No Codespace, corrija a soma para multiplicação e publique na **mesma branch**:

   ```bash
   python3 -m unittest -v
   git add app.py
   git commit -m "Corrige o cálculo do total"
   git push
   ```

6. Volte ao mesmo PR. Uma nova execução deve ficar verde. Compare os hashes dos commits nas duas execuções. O PR pode ficar aberto para a avaliação.

## Verificação e entrega

`check.sh 03` valida a configuração, não o histórico de falhas. Entregue o link do PR e das execuções vermelha e verde. Explique qual linha causava a falha.

**Reexecutar não corrige código:** repetir a execução do commit quebrado mantém o erro. Um check falho só bloqueia merge se o repositório tiver regras exigindo aquele check; aqui o objetivo é acompanhar o resultado.

[Próximo: variáveis e contextos →](../04-variaveis-e-contextos/README.md) · [Índice](../../README.md)
