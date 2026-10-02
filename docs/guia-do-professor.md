# Guia do professor — GitHub Actions

Curso introdutório em pt-BR, com **7 exercícios e 180 minutos**, mais o exercício 00, feito antes da aula, e 7 exercícios opcionais, de 08 a 14, para depois da aula. Use a [ementa](ementa.md), os [slides](index.html) e o [gabarito](gabarito.md).

## Preparação

1. Publique este material em `fsilva-alt/devops-ghactions`, branch `main`, antes de distribuir os links. Se usar outro endereço, ajuste os links no README e na apresentação. Para hospedar os slides, configure o Pages com a pasta `/docs` da `main`.
2. Crie um Codespace com o modelo **Blank** e execute `sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"`. Conclua a autenticação, abra um terminal novo, crie `~/meu-arquivo.txt` no editor com a linha do slide e execute `check.sh 00`. Ele confere o material, os 14 laboratórios, o login com escopo `workflow`, o arquivo, o Docker, o act e a imagem do runner local.
3. Faça os 7 exercícios com uma conta de aluno, incluindo a criação dos repositórios públicos, a falha e a correção no PR e a configuração do Pages. Execute `bash tests/rodar.sh` e `bash tests/rodar.sh --act`; os testes verificam a parte local, mas não substituem essa passagem no GitHub.
4. Peça a preparação do README com um dia de antecedência. O instalador baixa cerca de 2 GB para a simulação; fazer isso antes evita esperas durante a aula. Confirme o acesso e a franquia de Codespaces de cada participante.
5. Combine onde os links de entrega serão registrados e como os monitores vão atuar. Para cerca de 100 pessoas, use como referência um monitor para cada 25.

## Modelo mental a repetir

```text
Codespace: editar → check.sh (YAML + act) → commit → push
                                                   ↓ evento no GitHub
Actions: workflow → um runner por job → etapas e logs
                                                   ↓
                                         artefato / Pages
```

Uma instalação feita no Codespace não instala pacotes no runner. Um arquivo criado em um job não aparece em outro. A simulação com o act não é uma execução no GitHub. Repita essas distinções nos exercícios 02, 05 e 06.

## Condução

- A apresentação está em um único arquivo HTML. Abra `docs/index.html` ou o site publicado e escolha um exercício no início. Use `→` e `←` para mudar de slide, `Esc` para voltar ao início e `F` para tela cheia. O seletor no canto superior direito alterna entre os temas claro e escuro. Cada slide tem um endereço direto, como `#/d/04/2`.
- A introdução tem oito slides: como acompanhar a aula, o que é o GitHub Actions, os problemas que ele resolve, CI/CD, o uso em equipe, o histórico, os cuidados necessários e o papel de cada ferramenta. Use os 10 minutos da abertura para esses slides.
- Digite o primeiro YAML ao vivo. Explique dois espaços por nível, `-` para os itens de uma lista e `|` para várias linhas. Os nomes das chaves ficam em inglês porque fazem parte da sintaxe.
- Em cada exercício, leia a capa com a turma: objetivo, pasta, ponto de partida e entrega. Os laboratórios são independentes; ninguém precisa copiar o resultado anterior.
- Mostre a saída do `check.sh` no primeiro uso. A análise do YAML vem antes; a simulação mostra cada etapa e o log dos comandos, como na aba Actions.
- No 03, mantenha o check vermelho visível e encontre a primeira mensagem útil no log: `503 != 1500`. O objetivo é corrigir o código e fazer push; reexecutar o commit com erro repete a falha.
- No 04, use apenas o valor fictício `somente-demonstracao` como segredo. Não peça tokens pessoais.
- No 05, provoque a falha temporária e mostre `empacotar` como **skipped**, primeiro na simulação e depois no GitHub.
- No 07, forneça o YAML guiado e explique uma parte por vez. A meta é reconhecer teste → build → publicação e localizar a URL, sem memorizar as actions do Pages.
- Em caso de atraso, use o gabarito como apoio para concluir os mesmos 7 exercícios. Reserve o bloco final inteiro para a configuração do Pages e a conferência do site.
- Nas tarefas, o YAML a copiar está no próprio slide do exercício, igual ao dos slides de conceito. Ninguém precisa voltar slides para copiar.
- Os exercícios de 08 a 14 são opcionais e não entram nos 180 minutos. Indique-os para quem terminar antes ou para depois da aula; cada um tem laboratório próprio, gabarito e `check.sh NN`.

## O que conferir nas entregas

| Exercício | Evidência no GitHub |
|---|---|
| 01 | Execução manual verde e log com a saudação |
| 02 | Execução disparada por `push`, com os três testes aprovados |
| 03 | Link do PR, execução vermelha e execução verde depois da correção |
| 04 | Execução com a receita escolhida, autor, turma e confirmação do segredo |
| 05 | Grafo testar → empacotar e uma execução com o build pulado |
| 06 | Artefato `site` com `index.html` e a receita de limonada |
| 07 | Execução de deploy, environment `github-pages` e URL pública |
| 08 · opcional | Execução com `testar (3.11)`, `testar (3.12)` e `testar (3.13)` verdes |
| 09 · opcional | `Cache restored` no job `empacotar` e a saída de `gh cache list` |
| 10 · opcional | Push do README sem execução e push da receita com execução |
| 11 · opcional | PR com a anotação em `cafe.md`, check vermelho e verde |
| 12 · opcional | Resumo da execução com 4 receitas |
| 13 · opcional | Execução verde com a etapa `./.github/actions/preparar` nos dois jobs |
| 14 · opcional | Release `v1.0.0` com `livro-de-receitas.zip` |

## Problemas comuns

| Sintoma | Como resolver |
|---|---|
| `check.sh: command not found` | Abrir um terminal novo ou executar `source ~/.bashrc`; também funciona `bash "$CURSO_DIR/scripts/check.sh" NN` |
| Instalador falhou | Ler a mensagem no terminal, corrigir a causa e executar novamente o comando de instalação |
| `Simulação com o act pulada` | Executar `check.sh 00`; se o Docker não responder, esperar um minuto ou reabrir o Codespace; se faltar o act ou a imagem, executar `setup.sh` |
| Simulação lenta | Na primeira execução, o act baixa as actions usadas no workflow; as seguintes levam segundos |
| `Author identity unknown` | Configurar `git config --global user.name` e `user.email` com os dados do aluno |
| Login informa token de ambiente | `unset GH_TOKEN GITHUB_TOKEN` antes de autenticar; abrir um terminal novo depois da instalação |
| Push recusado por falta de `workflow` | `gh auth refresh --hostname github.com --scopes workflow`, depois `gh auth setup-git` e repetir o push |
| Repositório já existe | Usar um nome novo; se o remoto já está configurado, usar apenas `git push` |
| Workflow não aparece | Conferir `.github/workflows/ci.yml`, o commit, o push e a permissão em Settings → Actions → General |
| Botão Run workflow ausente | O workflow precisa declarar `workflow_dispatch` e estar na branch padrão |
| `Invalid workflow file` | Conferir a indentação, as chaves duplicadas e a linha indicada na mensagem |
| `receitas.py` não encontrado | Falta o checkout no job |
| `No module named markdown` no build | Instalar o `requirements.txt` naquele job, mesmo que outro job já tenha instalado |
| `CURSO_TOKEN` vazio | Cadastrar o segredo no repositório `actions-04` |
| `check.sh 00` não aceita `meu-arquivo.txt` | Salvar no editor (sem o ● na aba) e conferir com `cat ~/meu-arquivo.txt`; o arquivo fica na pasta pessoal |
| Job `testar (3.1)` na matriz | Versão sem aspas: escrever `'3.10'` |
| `Can't find 'action.yml'` no exercício 13 | Faltou o checkout antes da ação ou o `git add .github` com a pasta da ação |
| Release não criado no exercício 14 | Conferir se a tag começa com `v`, se foi enviada com `git push origin v1.0.0` e o `contents: write` no job `lancar` |
| Segundo job pulado | Conferir o resultado do job listado em `needs` e corrigir a causa da falha |
| Artefato ausente | Verificar se o build terminou e se `path` aponta para `dist/`, com o upload depois do build |
| Pages retorna erro de configuração | Settings → Pages → Source: GitHub Actions; depois executar novamente na `main` |
| Deploy sem permissão | Conferir `pages: write`, `id-token: write` e o environment `github-pages` no job `publicar` |

## Manutenção

| Arquivo | Responsabilidade |
|---|---|
| `.devcontainer/devcontainer.json` | Ambiente opcional para a manutenção do repositório |
| `install.sh` | Download e atualização do curso, verificador, laboratórios, atalho, `PATH` e login |
| `scripts/lib.sh` | Nomes e números 00–14, caminhos, versão do act e digest da imagem do runner local |
| `scripts/setup.sh` | Gera os laboratórios ausentes, instala o act e baixa a imagem |
| `scripts/labs.sh` | Copia o projeto e o ponto de partida de cada exercício |
| `scripts/check.sh` | Exercício 00, com o arquivo do editor, e encadeamento da análise do YAML com a simulação |
| `scripts/checks.py` | Requisitos de cada exercício no YAML, com mensagens em português |
| `scripts/simular.py` | Execução com o act, evento de cada exercício e conferência dos jobs, do log e do artefato |
| `templates/projeto/` | Livro de receitas: receitas em Markdown, `receitas.py`, três testes e `build.py` |
| `docs/solucoes/` | YAMLs completos dos 14 exercícios e a ação do 13, usados também pelos geradores e pelos testes |
| `docs/index.html` | Slides, com estilos, navegação e seletor de tema no mesmo arquivo |
| `tests/` | Instalação isolada, casos negativos, soluções, slides e simulação real com o act |

`setup.sh` preserva as pastas existentes. `reset.sh NN` recria apenas uma pasta marcada com `.git/curso-actions/exercicio` e não apaga repositórios no GitHub.

O act tem versão fixa em `scripts/lib.sh`, e o download é conferido pelo checksum publicado. A imagem `catthehacker/ubuntu:act-latest` é mantida pela comunidade e está fixada por digest. Ao atualizar qualquer um dos dois, execute `bash tests/rodar.sh --act`.

Os workflows usam versões principais explícitas das actions, para facilitar a leitura. Ao atualizá-las, confira os requisitos de runner e faça uma execução real dos 14 exemplos no GitHub. Em projetos de produção, avalie fixar as actions por SHA.

## Encerramento

Receba os links, peça que expliquem o caminho do commit até a página publicada e oriente a turma a enviar as mudanças com push e parar o Codespace.
