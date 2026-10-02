#!/bin/sh
# Num Codespace criado com o modelo Blank, execute:
# sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"
#
# Baixa ou atualiza o curso, prepara os laboratórios, instala o act (que simula os
# workflows em containers Docker), cria o atalho labs, autentica o GitHub CLI e
# configura os comandos nos novos terminais.
# Pode ser executado novamente sem apagar o trabalho nos laboratórios.
# Variáveis opcionais: CURSO_REPO, CURSO_RAMO, CURSO_DIR e LABS_DIR.
# CURSO_AUTH_GITHUB=0 pula a autenticação e CURSO_SIMULAR=0 dispensa o act em testes locais.
set -eu
falha() { printf '❌ %s\n' "$*" >&2; exit 1; }
if [ "${CODESPACES:-}" != true ] && [ "${CURSO_MODO_TESTE:-0}" != 1 ]; then
  falha "Crie um ambiente no GitHub Codespaces com o modelo Blank em https://github.com/codespaces e execute o instalador no terminal."
fi
PASTA_INICIAL="$(pwd -P)"
CURSO_REPO="${CURSO_REPO:-https://github.com/fsilva-alt/devops-ghactions.git}"
CURSO_RAMO="${CURSO_RAMO:-main}"
CURSO_DIR="${CURSO_DIR:-$HOME/devops-ghactions}"
LABS_DIR="${LABS_DIR:-$HOME/labs}"
CURSO_AUTH_GITHUB="${CURSO_AUTH_GITHUB:-1}"
export CURSO_DIR LABS_DIR
case "$CURSO_DIR" in /*) ;; *) falha "CURSO_DIR deve ser um caminho absoluto." ;; esac
case "$LABS_DIR" in /*) ;; *) falha "LABS_DIR deve ser um caminho absoluto." ;; esac
case "$CURSO_AUTH_GITHUB" in 0|1) ;; *) falha "CURSO_AUTH_GITHUB deve ser 0 ou 1." ;; esac
for comando in git bash python3; do
  command -v "$comando" >/dev/null 2>&1 || falha "Falta $comando. Use um Codespace com o modelo Blank, que inclui as ferramentas do curso."
done
if [ "$CURSO_AUTH_GITHUB" = 1 ]; then
  command -v gh >/dev/null 2>&1 || falha "Falta o GitHub CLI (gh). Use um Codespace com o modelo Blank ou instale-o em https://cli.github.com."
fi

if [ -d "$CURSO_DIR/.git" ]; then
  printf '▶ Atualizando o curso em %s\n' "$CURSO_DIR"
  git -C "$CURSO_DIR" pull -q --ff-only \
    || falha "Não foi possível atualizar $CURSO_DIR. Confira a conexão e as alterações locais nessa pasta antes de tentar novamente."
else
  printf '▶ Baixando o curso para %s\n' "$CURSO_DIR"
  git clone -q --depth 1 --branch "$CURSO_RAMO" -- "$CURSO_REPO" "$CURSO_DIR" \
    || falha "Não foi possível clonar $CURSO_REPO em $CURSO_DIR. Confira a conexão, o endereço e se a pasta de destino está vazia."
fi

printf '▶ Preparando o verificador do curso...\n'
python3 -m venv "$CURSO_DIR/.venv" || falha "Não foi possível criar o ambiente Python. Confira se python3-venv está instalado e execute o instalador novamente."
"$CURSO_DIR/.venv/bin/python" -m pip install --disable-pip-version-check -q -r "$CURSO_DIR/scripts/requirements.txt"
chmod +x "$CURSO_DIR"/scripts/*.sh
bash "$CURSO_DIR/scripts/setup.sh"

# Disponibiliza os laboratórios no explorador do editor sem substituir arquivos.
ATALHO_LABS="$PASTA_INICIAL/labs"
if [ "$PASTA_INICIAL" != "$(CDPATH='' cd -- "$LABS_DIR" && pwd -P)" ] && [ ! -e "$ATALHO_LABS" ] && [ ! -L "$ATALHO_LABS" ]; then
  ln -s "$LABS_DIR" "$ATALHO_LABS"
  printf '▶ Atalho para os laboratórios criado em %s\n' "$ATALHO_LABS"
fi

if [ "$CURSO_AUTH_GITHUB" = 1 ]; then
  printf '▶ Preparando o acesso ao GitHub para publicar os exercícios\n'
  # Como no curso de Git, usa o login salvo em vez do token do Codespace.
  unset GH_TOKEN GITHUB_TOKEN
  if gh auth status --active --hostname github.com >/dev/null 2>&1; then
    printf '▶ Reutilizando o login salvo no GitHub CLI\n'
  else
    [ -t 0 ] || falha "Para autenticar, execute o instalador novamente no terminal interativo do Codespace. Os laboratórios já estão prontos."
    printf '\nAutorize o GitHub CLI com a conta que usará no curso.\n'
    printf 'Siga o código e o endereço exibidos abaixo para entrar pelo navegador.\n'
    printf 'O escopo workflow permite publicar os arquivos de GitHub Actions.\n\n'
    gh auth login --hostname github.com --git-protocol https --web --scopes workflow \
      || falha "Login interrompido. Execute o instalador novamente para continuar; seus laboratórios serão preservados."
  fi
  gh auth setup-git --hostname github.com \
    || falha "Não foi possível configurar o Git para usar o login do gh. Execute o instalador novamente."
  gh auth status --active --hostname github.com \
    || falha "O login no GitHub não está válido. Execute o instalador novamente para autenticar."
fi

# Caminhos são escapados para poderem ser carregados por bash e zsh.
shell_quote() { printf "'%s'" "$(printf '%s' "$1" | sed "s/'/'\\\\''/g")"; }
AUTH_LINHA='if [ "${CODESPACES:-}" = true ]; then unset GH_TOKEN GITHUB_TOKEN; fi'
for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
  # Como nas referências, cria .bashrc e só altera .zshrc se ele já existir.
  if [ ! -f "$rc" ] && [ "$rc" != "$HOME/.bashrc" ]; then continue; fi
  [ -f "$rc" ] || touch "$rc"
  configurar_auth="$CURSO_AUTH_GITHUB"
  # Pular o login numa reinstalação não remove uma configuração já habilitada.
  if grep -qxF "$AUTH_LINHA" "$rc"; then configurar_auth=1; fi
  bloco="$(
    printf '# >>> curso de github actions >>>\n'
    printf 'export CURSO_DIR=%s\n' "$(shell_quote "$CURSO_DIR")"
    printf 'export LABS_DIR=%s\n' "$(shell_quote "$LABS_DIR")"
    printf 'export PATH="$CURSO_DIR/scripts:$CURSO_DIR/bin:$PATH"\n'
    if [ "$configurar_auth" = 1 ]; then printf '%s\n' "$AUTH_LINHA"; fi
    printf '# <<< curso de github actions <<<\n'
  )"
  atual="$(sed -n '/^# >>> curso de github actions >>>$/,/^# <<< curso de github actions <<<$/p' "$rc")"
  [ "$atual" = "$bloco" ] && continue
  sed -i '/^# >>> curso de github actions >>>$/,/^# <<< curso de github actions <<<$/{d;}' "$rc"
  printf '\n%s\n' "$bloco" >> "$rc"
done

printf '\n✅ Curso de GitHub Actions instalado com sucesso!\n'
printf 'Material do curso: %s\n' "$CURSO_DIR"
printf 'Laboratórios: %s\n' "$LABS_DIR"
printf 'Abra um terminal novo para carregar os comandos e o login salvo.\n'
printf 'Ou execute: source ~/.bashrc (bash) / source ~/.zshrc (zsh).\n'
printf 'Confira o ambiente: check.sh 00 (exercício 00, antes da aula).\n'
printf 'Slides e exercícios: https://fsilva-alt.github.io/devops-ghactions/\n'
if [ "$CURSO_AUTH_GITHUB" = 0 ]; then
  printf 'Preparação concluída sem login. Antes da aula, execute o instalador sem CURSO_AUTH_GITHUB=0 para autenticar.\n'
fi
