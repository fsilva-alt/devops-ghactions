# Ementa — Curso de GitHub Actions no GitHub Codespaces

| Item | Definição |
|---|---|
| Formato | Aula ao vivo, com exercícios no Codespace de cada participante |
| Duração | 3 horas, com 7 exercícios |
| Público | Iniciantes em CI/CD; não é preciso saber programar |
| Pré-requisitos | Conta GitHub pessoal com acesso ao Codespaces e noções de terminal, commit, branch e push |
| Preparação | Seguir a seção “Antes da aula” do README: criar um Codespace em branco, executar o instalador e conferir o ambiente com `check.sh 00` |
| Execução dos workflows | Runners Linux hospedados pelo GitHub; simulação local com o act antes de cada publicação |
| Projeto | Livro de receitas em Markdown, com um programa Python, três testes e um gerador de site já prontos |

## Objetivos de aprendizagem

Ao longo dos exercícios, você aprende a:

- explicar o que é o GitHub Actions, que problemas ele resolve e onde ele entra em um processo de CI/CD;
- ler um workflow e reconhecer seus eventos, jobs, etapas, actions e runners;
- executar testes automaticamente a cada push e em cada pull request;
- ler os logs de uma execução, encontrar a causa de uma falha e corrigi-la com um novo commit;
- configurar uma execução com variáveis, contextos, entradas manuais e um segredo;
- ordenar jobs com `needs` e entender por que cada job prepara seu próprio ambiente;
- guardar o resultado do build como artefato e publicar um site no GitHub Pages.

**CI (integração contínua):** verificar automaticamente cada mudança antes de integrá-la. **Build:** gerar os arquivos finais a partir do projeto. **Deploy:** disponibilizar esses arquivos no destino. Os exercícios percorrem esses três passos com o mesmo projeto.

## Conteúdo por módulo

| Módulo | Conteúdo |
|---|---|
| Introdução | Como acompanhar a aula; o que é o GitHub Actions; problemas que ele resolve; CI, entrega contínua e implantação contínua; uso em equipe com pull requests e regras de proteção; breve história; cuidados com custos, segredos, permissões e actions de terceiros; Codespace, runner, act e Pages |
| Abertura | Exercício 00, antes da aula: Git, GitHub CLI com escopo `workflow`, Docker e act |
| 1. Fundamentos | Estrutura de um workflow em YAML: `name`, `on`, `permissions`, `jobs`, `runs-on`, `steps`, `run`; evento manual `workflow_dispatch`; execuções, jobs e logs na aba Actions |
| 2. Integração contínua | Evento `push` com filtro de branch; `uses`, `with` e `run`; `actions/checkout` e `actions/setup-python`; evento `pull_request`; checks; leitura de logs; falha e correção |
| 3. Configuração | `env`, `inputs`, contexto `github`, `vars` e `secrets`; `${{ }}` e variáveis do shell; segredos mascarados nos logs |
| 4. Entrega contínua | `needs` e jobs em paralelo; um runner por job; build do site; `actions/upload-artifact`; artefato, cache e deploy; GitHub Pages com `configure-pages`, `upload-pages-artifact` e `deploy-pages`; `permissions` por job; `environment`; condição para publicar só a `main` |

O projeto é um livro de receitas. As receitas ficam em arquivos Markdown na pasta `receitas/`; `receitas.py` lista as receitas e calcula a quantidade de um ingrediente para várias receitas; `build.py` gera o site em `dist/index.html`. O código vem pronto, e os enunciados guiam cada alteração.

## Cronograma

| Horário | Bloco | Evidência de aprendizagem |
|---|---|---|
| 0:00–0:10 | Abertura e introdução | Explicar o que o Actions automatiza e onde cada parte executa |
| 0:10–0:25 | **Exercício 01** · Primeiro workflow | Execução manual com a mensagem no log |
| 0:25–0:50 | **Exercício 02** · Testes no push | Push dispara os três testes aprovados |
| 0:50–1:15 | **Exercício 03** · Checks no pull request | PR com a falha identificada e corrigida |
| 1:15–1:25 | Intervalo | |
| 1:25–1:45 | **Exercício 04** · Variáveis e contextos | Receita do dia, autor e turma no log; segredo verificado sem exibir o valor |
| 1:45–2:05 | **Exercício 05** · Jobs e dependências | Grafo testar → empacotar; build pulado após a falha dos testes |
| 2:05–2:25 | **Exercício 06** · Artefatos do build | Artefato `site` baixado, com a receita nova |
| 2:25–2:55 | **Exercício 07** · Deploy no Pages | Site público e execução de deploy concluída |
| 2:55–3:00 | Encerramento | Links das entregas e Codespace parado |

Os tempos dos exercícios incluem explicação, demonstração e prática. Use cerca de um terço de cada bloco para os slides de conceito e o restante para a tarefa e a conferência.

### Distribuição do tempo

| Tipo de bloco | Minutos |
|---|---:|
| Exercícios 01 a 07, com explicações | 155 |
| Abertura e introdução | 10 |
| Intervalo | 10 |
| Encerramento | 5 |
| **Total** | **180** |

## Os exercícios

Cada exercício de 01 a 07 tem um laboratório em `~/labs/NN-nome/`, com o livro de receitas e o workflow de partida. Os laboratórios são independentes: é possível começar um exercício sem ter concluído o anterior.

| # | Exercício | Tempo | Estado inicial | Tarefa | Verificação local | Entrega no GitHub |
|---|---|---:|---|---|---|---|
| 00 | O ambiente está pronto? | 5 | Codespace com o curso instalado | Conferir Git, `gh`, Docker e act | Ferramentas presentes; workflow mínimo executado em um container | — |
| 01 | Primeiro workflow | 15 | `.github/workflows/` vazia | Workflow manual com uma saudação | YAML com `workflow_dispatch`; mensagem no log da simulação | Execução manual verde |
| 02 | Testes no push | 25 | Workflow de boas-vindas | Checkout, Python, dependências e testes no `push` | Três testes aprovados na simulação | Execução verde disparada por push |
| 03 | Checks no pull request | 25 | Workflow de testes no push | Acrescentar `pull_request`; provocar e corrigir uma falha | Testes aprovados em uma simulação de PR | PR com execução vermelha e verde |
| 04 | Variáveis e contextos | 20 | Workflow de boas-vindas | Input `receita`, `env.COZINHA`, `vars.TURMA`, `secrets.CURSO_TOKEN` | Simulação com valores locais de demonstração | Execução manual com a receita escolhida |
| 05 | Jobs e dependências | 20 | Workflow com push e PR | Job `empacotar` com `needs: testar` | Dois jobs verdes, na ordem do `needs` | Execução verde e outra com o build pulado |
| 06 | Artefatos do build | 20 | Workflow com testar e empacotar | Upload de `dist/` como `site`; receita de limonada | Artefato da simulação com `index.html` | Artefato com a receita nova |
| 07 | Deploy no Pages | 30 | Workflow com o artefato | Workflow guiado de publicação; título personalizado | Em um PR simulado, o deploy não roda | URL pública do livro de receitas |

## Avaliação

A conclusão de cada exercício exige a verificação local (`check.sh NN`) e a entrega no GitHub. No exercício 03, explique qual linha causava a falha; no 05, por que o segundo job prepara seu próprio ambiente; no 07, a diferença entre gerar, guardar e publicar um site.

## Continuidade

Próximos temas: cache de dependências, matrizes de versões, workflows reutilizáveis, regras de proteção de branches e environments com aprovação. Consulte a [documentação oficial em português](https://docs.github.com/pt/actions).
