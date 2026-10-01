# 04 — Variáveis e contextos

**20 minutos · Ambiente obrigatório: GitHub Codespaces**

## Objetivo

Personalizar uma execução manual e reconhecer de onde vêm as informações do workflow.

## Onde e estado inicial

```bash
cd ~/labs-actions/04-variaveis-e-contextos
code .github/workflows/ci.yml
```

Este laboratório retoma a saudação manual. É uma prática isolada de configuração; não depende dos PRs anteriores.

| Origem | Exemplo | Quem define |
|---|---|---|
| `env` | Nome do curso | O próprio YAML |
| `inputs` | Mensagem digitada no botão Run workflow | Quem inicia a execução |
| `github` | Usuário que iniciou a execução | GitHub |
| `vars` | Nome da turma | Configurações do repositório |
| `secrets` | Valor que não deve aparecer no arquivo ou log | Configurações de segredos |

## Tarefa guiada

1. Para focar nas expressões, copie o exemplo comentado pelo professor e abra-o:

   ```bash
   cp "$CURSO_DIR/docs/solucoes/04.yml" .github/workflows/ci.yml
   code .github/workflows/ci.yml
   ```

2. Localize `workflow_dispatch.inputs.mensagem`. Mude o `default` para uma saudação sua. Localize `env.CURSO`: essa variável estará disponível nas etapas como `$CURSO`.
3. Na etapa **Mostrar contexto**, identifique:

   ```yaml
   env:
     MENSAGEM: ${{ inputs.mensagem }}
     AUTOR: ${{ github.actor }}
     TURMA: ${{ vars.TURMA }}
   ```

   `${{ }}` é uma expressão avaliada pelo Actions. No comando `run`, `$MENSAGEM` é uma variável lida pelo shell. Passar a entrada por `env` permite tratá-la como texto, inclusive com aspas e outros caracteres.

4. Verifique e publique:

   ```bash
   check.sh 04
   git add .github/workflows/ci.yml
   git commit -m "Personaliza a execução manual"
   gh repo create actions-04 --public --source=. --remote=origin --push
   gh browse
   ```

5. No GitHub, abra **Settings → Secrets and variables → Actions**:
   - Na aba **Variables**, crie a variável de repositório `TURMA`, valor `turma-actions`.
   - Na aba **Secrets**, crie o segredo de repositório `CURSO_TOKEN`, valor fictício `somente-demonstracao`. Não use uma credencial real.
6. Vá a **Actions → Variáveis e contextos → Run workflow**. Digite uma mensagem diferente do valor padrão e execute na `main`.
7. Leia os logs: curso, autor, turma e sua mensagem aparecem. A última etapa usa `test -n "$TOKEN_DEMO"` para conferir que o segredo não está vazio, sem imprimir seu conteúdo.

## Verificação e entrega

Entregue uma execução manual verde com sua mensagem e a confirmação de presença do segredo. `check.sh 04` confere referências no YAML; o valor salvo em Settings só é conferido na execução.

Explique a diferença entre `vars.TURMA` e `secrets.CURSO_TOKEN`. Um segredo não cadastrado resulta em valor vazio; confira o nome e o repositório se a última etapa falhar.

[Próximo: jobs e dependências →](../05-jobs-e-dependencias/README.md) · [Índice](../../README.md)
