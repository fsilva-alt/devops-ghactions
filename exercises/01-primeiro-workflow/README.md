# 01 — Primeiro workflow

**15 minutos · Ambiente obrigatório: GitHub Codespaces**

## Objetivo

Criar uma automação manual e identificar evento, workflow, job, runner e step.

## Onde e estado inicial

No terminal do Codespace do curso:

```bash
cd ~/labs-actions/01-primeiro-workflow
mkdir -p .github/workflows
code .github/workflows/ci.yml
```

O laboratório já é um repositório Git com o projeto do cardápio. Ainda não tem workflow. Não é necessário mexer no Python.

## Entenda antes de escrever

| Termo | O que significa |
|---|---|
| Evento | Algo que dispara uma automação; aqui, um clique manual |
| Workflow | Arquivo YAML que descreve a automação |
| Job | Grupo de etapas executadas em um runner |
| Runner | Máquina que executa um job |
| Step | Uma etapa; pode executar um comando ou uma action |

YAML usa indentação: use espaços, não tabulações. `-` inicia um item de lista. `name` é o nome exibido na interface; `boas-vindas` é o identificador do job.

## Tarefa

1. Escreva no arquivo aberto e salve:

   ```yaml
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

   `workflow_dispatch` permite execução manual. `ubuntu-latest` seleciona um runner Linux hospedado pelo GitHub. `permissions` limita o token da execução à leitura do conteúdo do repositório.

2. No terminal, confira e publique:

   ```bash
   check.sh 01
   git add .github/workflows/ci.yml
   git commit -m "Cria primeiro workflow"
   gh repo create actions-01 --public --source=. --remote=origin --push
   gh browse --actions
   ```

3. Na aba **Actions**, escolha **Boas-vindas → Run workflow → main → Run workflow**. O workflow precisa estar na branch padrão para esse botão aparecer.
4. Abra a execução, o job **boas-vindas** e a etapa **Cumprimentar a turma**. Localize a mensagem.

## Verificação e entrega

- `check.sh 01` aprova os requisitos locais.
- A execução manual fica verde e o log mostra `Olá, GitHub Actions!`.
- Entregue o link da execução. Explique: **o comando `echo` rodou no Codespace ou em um runner?**

Se não houver execução após o push, está correto: por enquanto o único evento é manual. Se o workflow não aparecer, confira o caminho, o commit, o push e a branch padrão.

[Próximo: testes no push →](../02-testes-no-push/README.md) · [Índice](../../README.md)
