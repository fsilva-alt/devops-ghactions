# Guia do professor — GitHub Actions

Curso introdutório em pt-BR, com **7 exercícios e 180 minutos**. Use a [ementa](ementa.md), os [slides](index.html) e o [gabarito](gabarito.md).

## Preparação

1. Publique este material em `fsilva-alt/devops-ghactions`, branch `main`, antes de distribuir os links. Se usar outro endereço, ajuste os links no README e na apresentação. Para hospedar os slides, configure Pages para a pasta `/docs` da `main`.
2. Crie um Codespace novo desse repositório. Aguarde o `postCreateCommand`, rode `sh install.sh` para autenticar e abra um terminal novo. Verifique os 7 labs em `~/labs-actions` e o escopo `workflow` do login.
3. Teste os 7 exercícios com uma conta de aluno, incluindo criação dos repositórios públicos, falha/correção no PR e configuração do Pages. Execute `bash tests/rodar.sh`; ela verifica a parte local, mas não substitui essa passagem no GitHub.
4. Peça a preparação do README com um dia de antecedência. Confirme acesso e franquia de Codespaces: ele é o ambiente obrigatório. Se o acesso estiver bloqueado, resolva a permissão com a conta ou organização antes da aula.
5. Combine o local de entrega dos links e a atuação dos monitores. Para cerca de 100 pessoas, use como referência um monitor para cada 25.

## Modelo mental a repetir

```text
Codespace: editar → commit → push
                            ↓ evento no GitHub
Actions: workflow → job em um runner → etapas e logs
                            ↓
                      artefato / Pages
```

Uma instalação feita no Codespace não instala pacotes no runner. Um arquivo criado em um job não aparece automaticamente em outro. Um check local não é uma execução no GitHub. Repita essas distinções nos exercícios 02, 05 e 06.

## Condução

- A apresentação usa HTML/CSS e funciona sem JavaScript. Abra `docs/index.html` ou o site publicado, escolha um exercício no índice e use os links ao final de cada aula. Clique nas perguntas para expandir as respostas; pelo teclado, use Tab e Enter. Cada aula tem um endereço direto, como `#exercicio-04`.
- Comece definindo CI, build e deploy em linguagem simples. Mostre um exemplo, depois nomeie suas partes.
- Digite o primeiro YAML ao vivo. Explique dois espaços por nível, `-` para itens da lista e `|` para várias linhas. Os nomes das chaves permanecem em inglês porque fazem parte da linguagem.
- Em cada bloco, leia o estado inicial com a turma. Os laboratórios são independentes; ninguém precisa copiar o resultado anterior. Cada um publica `actions-01` a `actions-07` na própria conta, sempre a partir do mesmo Codespace.
- No 03, mantenha o check vermelho visível e encontre a primeira mensagem útil no log. Corrigir o código e fazer push é o objetivo; apenas reexecutar o commit quebrado repete a falha.
- No 04, use apenas um valor fictício como segredo. Explique a diferença entre variável visível e segredo protegido; não solicite tokens pessoais para esse exercício.
- No 05, provoque uma falha temporária e observe `empacotar` como **skipped**. Depois corrija e rode novamente.
- No 07, forneça o YAML guiado e explique uma parte por vez. A meta é reconhecer teste → build → publicação e acompanhar a URL, sem exigir memorização das ações do Pages.
- Se houver atraso, use o gabarito como apoio para concluir os mesmos 7 exercícios. Reserve o bloco final inteiro para configurar Pages e conferir o site.

## O que conferir nas entregas

| Exercício | Evidência no GitHub |
|---|---|
| 01 | Execução manual verde e log com a saudação |
| 02 | Execução cujo evento é `push`, com os três testes passando |
| 03 | Link do PR, execução vermelha anterior e verde após correção |
| 04 | Execução com input próprio, autor, turma e confirmação de presença do segredo |
| 05 | Grafo testar → empacotar; exemplo de build pulado quando testar falha |
| 06 | Artefato `site` e presença de `index.html` no ZIP baixado |
| 07 | Execução de deploy, environment `github-pages` e URL pública funcional |

## Problemas comuns

| Sintoma | Como resolver |
|---|---|
| `check.sh: command not found` | Abrir terminal novo ou carregar `source ~/.bashrc`; também funciona `bash "$CURSO_DIR/scripts/check.sh" NN` |
| Preparação automática falhou | Ler o log de criação do Codespace e executar `sh install.sh` na raiz do curso para retomar |
| `Author identity unknown` | Configurar `git config --global user.name` e `user.email` com dados do aluno |
| Login informa token de ambiente | `unset GH_TOKEN GITHUB_TOKEN` antes de autenticar; abrir terminal novo após a instalação |
| Push recusado por falta de `workflow` | `gh auth refresh --hostname github.com --scopes workflow`, depois `gh auth setup-git` e repetir push |
| Repositório já existe | Usar nome novo; se já está configurado, usar apenas `git push`, não `gh repo create` |
| Workflow não aparece | Conferir `.github/workflows/ci.yml`, commit, push, YAML e permissão em Settings → Actions → General |
| Botão Run workflow ausente | O workflow precisa declarar `workflow_dispatch` e estar na branch padrão |
| `Invalid workflow file` | Conferir indentação, chaves duplicadas, tipo do valor e mensagem com número da linha |
| `app.py` não encontrado | Falta checkout no job; conferir se está na raiz do projeto |
| `No module named markdown` no build | Instalar `requirements.txt` naquele job, mesmo que outro job já tenha instalado |
| `CURSO_TOKEN` vazio | Cadastrar em Settings → Secrets and variables → Actions → Secrets, no repositório do exercício 04 |
| Segundo job pulado | Conferir o resultado do job listado em `needs`; corrigir a causa da falha |
| Artefato ausente | Verificar se o build terminou e se `path` aponta para `dist/`, com upload após o build |
| Pages retorna erro de configuração | Settings → Pages → Source: GitHub Actions; depois executar novamente na `main` |
| Deploy sem permissão | Conferir `pages: write`, `id-token: write` e environment `github-pages` no job publicar |
| Site demora a aparecer | Aguardar o deploy terminar e usar a URL da execução; pode levar alguns minutos |

## Manutenção

| Arquivo | Responsabilidade |
|---|---|
| `.devcontainer/devcontainer.json` | Ambiente obrigatório do aluno |
| `install.sh` | Dependência do verificador, geração dos labs, PATH e login |
| `scripts/lib.sh` | Nomes e números 01–07; caminhos e requisito de Codespaces |
| `scripts/labs.sh` | Copia o projeto e o ponto de partida de cada exercício |
| `scripts/checks.py` | Requisitos didáticos do YAML, com mensagens em português |
| `templates/projeto/` | Aplicação, três testes e build do site |
| `docs/solucoes/` | YAMLs completos, também usados pelos geradores e testes |
| `docs/index.html` e `docs/style.css` | Apresentação estática, navegação por âncoras e tema violeta |
| `tests/` | Instalação isolada, casos negativos, soluções e consistência do material |

`setup.sh` preserva pastas existentes. `reset.sh NN` recria apenas uma pasta com o marcador `.git/curso-actions/exercicio`; não apaga repositórios no GitHub. O login salvo é reutilizado, mas um login antigo pode exigir ampliação do escopo `workflow`, conforme o README.

Os exemplos usam versões principais explícitas das actions para facilitar a leitura. Ao atualizar essas versões, confira seus requisitos de runner e faça uma execução real dos 7 exemplos. Em projetos de produção, avalie fixar actions a SHAs revisados.

## Encerramento

Receba os links, peça que expliquem o caminho do commit até a página publicada e oriente a salvar as mudanças com push e parar o Codespace.
