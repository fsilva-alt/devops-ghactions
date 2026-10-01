# Ementa — Introdução ao GitHub Actions

| Item | Definição |
|---|---|
| Nível | Introdutório; nenhuma experiência prévia em CI/CD |
| Duração | 3 horas, com 7 exercícios |
| Formato | Aula ao vivo com demonstração e prática individual |
| Ambiente obrigatório | GitHub Codespaces, criado a partir do repositório do curso |
| Execução dos workflows | Runners Linux hospedados pelo GitHub Actions |
| Pré-requisitos | Conta GitHub, acesso ao Codespaces, noções de terminal, commit, branch e push |
| Projeto | Cardápio em Python, com testes e gerador de site já fornecidos |

## Objetivos

Ao final, a pessoa consegue ler um workflow pequeno, reconhecer seus eventos, jobs e etapas, automatizar testes, investigar logs, parametrizar uma execução, ordenar jobs, recuperar um artefato e acompanhar um deploy guiado no GitHub Pages.

**CI (integração contínua)**: verificar mudanças automaticamente antes de integrá-las. **Build**: produzir arquivos prontos para distribuição. **Deploy**: disponibilizar esses arquivos para quem vai usar o sistema. O curso conecta esses três passos com exemplos pequenos.

## Cronograma de 180 minutos

| Horário | Atividade | Evidência de aprendizagem |
|---|---|---|
| 0:00–0:10 | Abertura: localizar Codespace, labs e aba Actions | Explicar onde edita e onde o workflow executa |
| 0:10–0:25 | 01 — Primeiro workflow | Execução manual com mensagem nos logs |
| 0:25–0:50 | 02 — Testes no push | Push dispara testes aprovados |
| 0:50–1:15 | 03 — Checks no pull request | PR com falha identificada e corrigida |
| 1:15–1:25 | Intervalo | |
| 1:25–1:45 | 04 — Variáveis e contextos | Mensagem personalizada, autor e turma; segredo presente |
| 1:45–2:05 | 05 — Jobs e dependências | Grafo testar → empacotar; build bloqueado por teste falho |
| 2:05–2:25 | 06 — Artefatos do build | Arquivo `site.zip` baixado e `index.html` inspecionado |
| 2:25–2:55 | 07 — Deploy no Pages | Site público e execução de deploy bem-sucedida |
| 2:55–3:00 | Encerramento | Links de entrega e Codespace parado |

As durações dos exercícios incluem explicação e prática. Use aproximadamente um terço de cada bloco para demonstrar e o restante para praticar e conferir. A preparação de login e ambiente acontece antes da aula, sem um exercício adicional.

## Conteúdo dos 7 exercícios

1. **Primeiro workflow:** indentação YAML, `name`, `on`, `workflow_dispatch`, `jobs`, `runs-on`, `steps`, `run`; aba Actions.
2. **Testes no push:** eventos, filtro de branch, `uses`, `with`, checkout, versão do Python, instalação e testes; saída de comandos.
3. **Checks no pull request:** branch de trabalho, filtro da branch de destino, check associado a um commit, logs, correção da causa e nova execução.
4. **Variáveis e contextos:** `env`, entrada manual, `${{ }}`, contexto `github`, variável de repositório e segredo fictício; passagem para o shell por variáveis de ambiente.
5. **Jobs e dependências:** etapas sequenciais, jobs paralelos por padrão, `needs`, runner separado para cada job, geração do site.
6. **Artefatos:** persistência de arquivos gerados, `upload-artifact`, caminho, nome, retenção e download pela interface.
7. **Deploy guiado:** Pages como destino, teste antes de publicar, artefato específico do Pages, permissões do token, environment e condição para publicar somente a `main`.

## Avaliação

Cada enunciado contém um check local e uma entrega na interface do GitHub. A conclusão exige ambos. No exercício 03, explique por que o teste falhou; no 05, por que o segundo job precisa preparar seu próprio ambiente; no 07, diferencie gerar, guardar e publicar um site.

## Continuidade após o curso

Com esses fundamentos consolidados, próximos temas são cache, matrizes de versões, workflows reutilizáveis e regras de proteção de branches. Consulte a [documentação oficial em português](https://docs.github.com/pt/actions).
