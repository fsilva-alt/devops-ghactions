#!/usr/bin/env bash
# Integração em HOME descartável: nunca usa conta GitHub nem labs do usuário.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMP_BASE="${TMPDIR:-/tmp/opencode}"
mkdir -p "$TEMP_BASE"
TEMP="$(mktemp -d "$TEMP_BASE/curso-actions.XXXXXX")"
trap 'rm -rf -- "$TEMP"' EXIT
export HOME="$TEMP/home"
export LABS_DIR="$HOME/labs-actions"
export CURSO_MODO_TESTE=1 CURSO_AUTH_GITHUB=0 CODESPACES=false
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$HOME/.gitconfig"
export PYTHONDONTWRITEBYTECODE=1
unset GH_TOKEN GITHUB_TOKEN
mkdir -p "$HOME" "$TEMP/curso" "$TEMP/bin"
tar -C "$RAIZ" --exclude=.git --exclude=.venv --exclude=__pycache__ -cf - . | tar -C "$TEMP/curso" -xf -
CURSO_DIR="$TEMP/curso"
export CURSO_DIR
printf '\n▶ Instalação isolada, sem autenticação\n'
sh "$CURSO_DIR/install.sh"
export PATH="$CURSO_DIR/scripts:$TEMP/bin:$PATH"
[[ $(find "$LABS_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l) -eq 7 ]]
touch "$LABS_DIR/01-primeiro-workflow/trabalho-preservado"
sh "$CURSO_DIR/install.sh" > "$TEMP/reinstalacao.log"
[[ -f "$LABS_DIR/01-primeiro-workflow/trabalho-preservado" ]]
[[ $(grep -c '^# >>> curso de github actions >>>' "$HOME/.bashrc") -eq 1 ]]
bash -c 'source "$HOME/.bashrc"; command -v check.sh' >/dev/null
if command -v zsh >/dev/null; then
  zsh -c 'source "$HOME/.zshrc"; command -v check.sh' >/dev/null
fi
printf '✅ Instalação e reinstalação preservam os laboratórios e configuram o PATH.\n'

# A instalação fora do Codespaces só é liberada explicitamente para manutenção.
if CURSO_MODO_TESTE=0 sh "$CURSO_DIR/install.sh" > "$TEMP/fora.log" 2>&1; then
  printf '❌ Instalador aceitou uso normal fora do Codespaces.\n'; exit 1
fi
grep -q Codespaces "$TEMP/fora.log"

# GitHub CLI simulado: exige que tokens automáticos tenham sido removidos.
export MOCK_GH_DIR="$TEMP/gh"
mkdir -p "$MOCK_GH_DIR"
cat > "$TEMP/bin/gh" <<'MOCK'
#!/bin/sh
set -eu
[ -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}" ] || exit 90
printf '%s\n' "$*" >> "$MOCK_GH_DIR/chamadas"
case "$*" in
  'auth status --active --hostname github.com') test -f "$MOCK_GH_DIR/login" ;;
  'auth login --hostname github.com --git-protocol https --web --scopes workflow')
    test -t 0
    touch "$MOCK_GH_DIR/login"
    ;;
  'auth setup-git --hostname github.com') test -f "$MOCK_GH_DIR/login" ;;
  *) exit 91 ;;
esac
MOCK
chmod +x "$TEMP/bin/gh"
if command -v script >/dev/null; then
  CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
    script -qec 'sh "$CURSO_DIR/install.sh"' /dev/null < /dev/null > "$TEMP/login.log"
  grep -q -- '--scopes workflow' "$MOCK_GH_DIR/chamadas"
else
  touch "$MOCK_GH_DIR/login"
fi
CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  sh "$CURSO_DIR/install.sh" < /dev/null > "$TEMP/login-salvo.log"
CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  bash -c 'source "$HOME/.bashrc"; test -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}"'
CODESPACES=false GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  bash -c 'source "$HOME/.bashrc"; test "$GH_TOKEN" = simulado; test "$GITHUB_TOKEN" = simulado'
printf '✅ Autenticação simulada: login com escopo workflow, reutilização e novos terminais.\n'

printf '\n▶ Exercícios: estados iniciais, erros comuns e soluções\n'
"$CURSO_DIR/.venv/bin/python" "$CURSO_DIR/tests/verificar.py"

# Conferência de inferência de número, reset isolado e limites de entrada.
(
  cd "$LABS_DIR/02-testes-no-push/.github/workflows"
  check.sh >/dev/null
)
reset.sh 02 >/dev/null
[[ -f "$LABS_DIR/01-primeiro-workflow/trabalho-preservado" ]]
if check.sh 02 >/dev/null 2>&1; then exit 1; fi
for numero in 00 08 99 abc ../01; do
  if check.sh "$numero" >/dev/null 2>&1; then exit 1; fi
  if reset.sh "$numero" >/dev/null 2>&1; then exit 1; fi
done
printf '✅ Inferência de exercício, reset isolado e números inválidos.\n'

printf '\n▶ Testes reais do projeto e geração do site\n'
"$CURSO_DIR/.venv/bin/python" -m pip install --disable-pip-version-check -q -r "$CURSO_DIR/templates/projeto/requirements.txt"
(
  cd "$LABS_DIR/07-deploy-no-pages"
  "$CURSO_DIR/.venv/bin/python" -m unittest -v
  "$CURSO_DIR/.venv/bin/python" build.py
  test -s dist/index.html
  grep -q '<table>' dist/index.html
  # O erro apresentado na aula deve realmente quebrar os testes.
  sed -i 's/return preco_centavos \* quantidade/return preco_centavos + quantidade/' app.py
  if "$CURSO_DIR/.venv/bin/python" -m unittest > "$TEMP/teste-com-erro.log" 2>&1; then
    printf '❌ O bug da aula não foi detectado.\n'; exit 1
  fi
  grep -q FAILED "$TEMP/teste-com-erro.log"
)
printf '\n✅ Suíte concluída. A publicação real no Actions/Pages é conferida na conta do aluno.\n'
