#!/bin/sh
# Execute na raiz do repositório aberto no GitHub Codespaces: sh install.sh
set -eu
falha() { printf '❌ %s\n' "$*" >&2; exit 1; }
if [ "${CODESPACES:-}" != true ] && [ "${CURSO_MODO_TESTE:-0}" != 1 ]; then
  falha "Abra este repositório no GitHub Codespaces (Code > Codespaces > Create codespace on main)."
fi
CURSO_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
LABS_DIR="${LABS_DIR:-$HOME/labs-actions}"
CURSO_AUTH_GITHUB="${CURSO_AUTH_GITHUB:-1}"
export LABS_DIR
case "$LABS_DIR" in /*) ;; *) falha "LABS_DIR deve ser um caminho absoluto." ;; esac
case "$CURSO_AUTH_GITHUB" in 0|1) ;; *) falha "CURSO_AUTH_GITHUB deve ser 0 ou 1." ;; esac
for comando in git bash python3; do
  command -v "$comando" >/dev/null 2>&1 || falha "Falta $comando. Reconstrua o Codespace usando .devcontainer/devcontainer.json."
done
if [ "$CURSO_AUTH_GITHUB" = 1 ]; then
  command -v gh >/dev/null 2>&1 || falha "Falta o GitHub CLI. Reconstrua o Codespace."
fi

printf '▶ Preparando o verificador de YAML...\n'
python3 -m venv "$CURSO_DIR/.venv" || falha "Não foi possível criar o ambiente Python. Reconstrua o Codespace."
"$CURSO_DIR/.venv/bin/python" -m pip install --disable-pip-version-check -q -r "$CURSO_DIR/scripts/requirements.txt"
chmod +x "$CURSO_DIR"/scripts/*.sh
bash "$CURSO_DIR/scripts/setup.sh"

# Caminhos são escapados para poderem ser carregados por bash e zsh.
shell_quote() { printf "'%s'" "$(printf '%s' "$1" | sed "s/'/'\\\\''/g")"; }
for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
  [ -f "$rc" ] || touch "$rc"
  sed -i '/^# >>> curso de github actions >>>$/,/^# <<< curso de github actions <<<$/{d;}' "$rc"
  {
    printf '\n# >>> curso de github actions >>>\n'
    printf 'export CURSO_DIR=%s\n' "$(shell_quote "$CURSO_DIR")"
    printf 'export LABS_DIR=%s\n' "$(shell_quote "$LABS_DIR")"
    printf 'export PATH="$CURSO_DIR/scripts:$PATH"\n'
    printf 'if [ "${CODESPACES:-}" = true ]; then unset GH_TOKEN GITHUB_TOKEN; fi\n'
    printf '# <<< curso de github actions <<<\n'
  } >> "$rc"
done

if [ "$CURSO_AUTH_GITHUB" = 1 ]; then
  # O token automático do Codespace não cobre necessariamente os 7 novos repos.
  unset GH_TOKEN GITHUB_TOKEN
  if ! gh auth status --active --hostname github.com >/dev/null 2>&1; then
    [ -t 0 ] || falha "Para autenticar, rode sh install.sh no terminal interativo do Codespace. Os laboratórios já estão prontos."
    gh auth login --hostname github.com --git-protocol https --web --scopes workflow \
      || falha "Login interrompido. Rode sh install.sh novamente para continuar."
  fi
  gh auth setup-git --hostname github.com
  gh auth status --active --hostname github.com
fi

printf '\n✅ Curso de GitHub Actions instalado com sucesso!\n'
printf 'Abra um terminal novo para carregar os comandos e o login salvo.\n'
printf 'Comece pelo exercício 01 em https://fsilva-alt.github.io/devops-ghactions/#exercicio-01\n'
printf 'Verificação local: check.sh 01 (é esperado reprovar antes de criar o workflow).\n'
if [ "$CURSO_AUTH_GITHUB" = 0 ]; then
  printf 'Preparação concluída sem login. Antes da aula, rode sh install.sh para autenticar.\n'
fi
