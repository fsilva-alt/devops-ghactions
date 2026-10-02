#!/usr/bin/env bash
# Integração em HOME descartável: nunca usa conta GitHub nem labs do usuário.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMP_BASE="${TMPDIR:-/tmp/opencode}"
mkdir -p "$TEMP_BASE"
TEMP="$(mktemp -d "$TEMP_BASE/curso-actions.XXXXXX")"
trap 'rm -rf -- "$TEMP"' EXIT
export HOME="$TEMP/home"
unset CURSO_DIR LABS_DIR CURSO_RAMO
# CURSO_SIMULAR=0: sem Docker aqui; a simulação real com o act fica em tests/act.sh.
export CURSO_MODO_TESTE=1 CURSO_AUTH_GITHUB=0 CURSO_SIMULAR=0 CODESPACES=false
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$HOME/.gitconfig"
export PYTHONDONTWRITEBYTECODE=1
unset GH_TOKEN GITHUB_TOKEN
mkdir -p "$HOME" "$TEMP/origem" "$TEMP/bin" "$TEMP/workspace"
printf '# Configuração existente do aluno\n' > "$HOME/.zshrc"
tar -C "$RAIZ" --exclude=.git --exclude=.venv --exclude=__pycache__ -cf - . | tar -C "$TEMP/origem" -xf -
git -C "$TEMP/origem" init -q -b main
git -C "$TEMP/origem" add .
git -C "$TEMP/origem" -c user.name=Teste -c user.email=teste@example.com commit -qm 'Material do curso'
export CURSO_REPO="file://$TEMP/origem"
printf '\n▶ Instalação via curl e sh -c em um workspace vazio, sem autenticação\n'
(
  cd "$TEMP/workspace"
  sh -c "$(curl -fsSL "file://$TEMP/origem/install.sh")"
)
export CURSO_DIR="$HOME/devops-ghactions" LABS_DIR="$HOME/labs"
export PATH="$CURSO_DIR/scripts:$TEMP/bin:$PATH"
cd "$TEMP/workspace"
[[ -d "$CURSO_DIR/.git" && -x "$CURSO_DIR/.venv/bin/python" ]]
[[ $(readlink "$TEMP/workspace/labs") == "$LABS_DIR" ]]
[[ $(find "$LABS_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l) -eq 14 ]]
touch "$LABS_DIR/01-primeiro-workflow/trabalho-preservado"
printf 'Atualização do material\n' > "$TEMP/origem/atualizacao.txt"
git -C "$TEMP/origem" add atualizacao.txt
git -C "$TEMP/origem" -c user.name=Teste -c user.email=teste@example.com commit -qm 'Atualiza material'
(
  cd "$TEMP/workspace"
  sh -c "$(curl -fsSL "file://$TEMP/origem/install.sh")"
) > "$TEMP/reinstalacao.log"
[[ -f "$CURSO_DIR/atualizacao.txt" ]]
[[ -f "$LABS_DIR/01-primeiro-workflow/trabalho-preservado" ]]
[[ $(grep -c '^# >>> curso de github actions >>>' "$HOME/.bashrc") -eq 1 ]]
grep -q '^# Configuração existente do aluno$' "$HOME/.zshrc"
bash -c 'source "$HOME/.bashrc"; command -v check.sh; command -v reset.sh; command -v setup.sh' >/dev/null
CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  bash -c 'source "$HOME/.bashrc"; test "$GH_TOKEN" = simulado; test "$GITHUB_TOKEN" = simulado'
if command -v zsh >/dev/null; then
  zsh -c 'source "$HOME/.zshrc"; command -v check.sh' >/dev/null
fi
printf '✅ Instalação remota, atualização, preservação dos laboratórios, atalho e PATH.\n'

# Não substitui uma pasta nem um link preexistente chamado labs no workspace.
mkdir -p "$TEMP/com-pasta/labs" "$TEMP/com-link"
touch "$TEMP/com-pasta/labs/trabalho-preservado"
ln -s "$TEMP/destino-ausente" "$TEMP/com-link/labs"
for pasta in com-pasta com-link; do
  (cd "$TEMP/$pasta"; sh "$CURSO_DIR/install.sh") > "$TEMP/$pasta.log"
done
[[ -f "$TEMP/com-pasta/labs/trabalho-preservado" ]]
[[ $(readlink "$TEMP/com-link/labs") == "$TEMP/destino-ausente" ]]
printf '✅ Arquivos e links existentes no workspace preservados.\n'

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
if CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  sh "$CURSO_DIR/install.sh" < /dev/null > "$TEMP/sem-terminal.log" 2>&1; then
  printf '❌ Login sem terminal interativo foi aceito.\n'; exit 1
fi
grep -q 'terminal interativo' "$TEMP/sem-terminal.log"
if command -v script >/dev/null; then
  CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
    script -qec 'sh "$CURSO_DIR/install.sh"' /dev/null < /dev/null > "$TEMP/login.log"
  grep -q -- '--scopes workflow' "$MOCK_GH_DIR/chamadas"
else
  touch "$MOCK_GH_DIR/login"
fi
CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  sh "$CURSO_DIR/install.sh" < /dev/null > "$TEMP/login-salvo.log"
grep -q 'Reutilizando o login salvo' "$TEMP/login-salvo.log"
if command -v script >/dev/null; then
  [[ $(grep -c 'auth login' "$MOCK_GH_DIR/chamadas") -eq 1 ]]
fi
CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  bash -c 'source "$HOME/.bashrc"; test -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}"'
CODESPACES=false GH_TOKEN=simulado GITHUB_TOKEN=simulado \
  bash -c 'source "$HOME/.bashrc"; test "$GH_TOKEN" = simulado; test "$GITHUB_TOKEN" = simulado'
if command -v zsh >/dev/null; then
  CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
    zsh -c 'source "$HOME/.zshrc"; test -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}"'
fi
printf '✅ Autenticação simulada: login com escopo workflow, reutilização e novos terminais.\n'

printf '\n▶ Exercícios: estados iniciais, erros comuns e soluções\n'
"$CURSO_DIR/.venv/bin/python" "$CURSO_DIR/tests/verificar.py"

# Conferência de inferência de número, reset isolado e limites de entrada.
(
  cd "$TEMP/workspace/labs/02-testes-no-push/.github/workflows"
  check.sh >/dev/null
)
(
  cd "$TEMP/workspace/labs/02-testes-no-push"
  reset.sh >/dev/null
)
[[ -f "$LABS_DIR/01-primeiro-workflow/trabalho-preservado" ]]
if check.sh 02 >/dev/null 2>&1; then exit 1; fi
for numero in 15 99 abc ../01; do
  if check.sh "$numero" >/dev/null 2>&1; then exit 1; fi
  if reset.sh "$numero" >/dev/null 2>&1; then exit 1; fi
done
# O 00 confere o ambiente e não tem laboratório. Sem Docker e act, reprova com dicas.
if reset.sh 00 >/dev/null 2>&1; then exit 1; fi
if check.sh 00 > "$TEMP/ambiente.log" 2>&1; then exit 1; fi
grep -q 'Exercício 00 — ambiente-pronto' "$TEMP/ambiente.log"
grep -q 'setup.sh\|Docker' "$TEMP/ambiente.log"
# O arquivo do editor: ausente, vazio, com texto errado e, por fim, correto.
grep -q 'meu-arquivo.txt ainda não existe' "$TEMP/ambiente.log"
: > "$HOME/meu-arquivo.txt"
check.sh 00 > "$TEMP/ambiente.log" 2>&1 || true
grep -q 'meu-arquivo.txt está vazio' "$TEMP/ambiente.log"
printf 'Estou pronto\n' > "$HOME/meu-arquivo.txt"
check.sh 00 > "$TEMP/ambiente.log" 2>&1 || true
grep -q 'não confere. Encontrei: Estou pronto' "$TEMP/ambiente.log"
printf 'Estou pronto para a aula de GitHub Actions!  \r\n\n' > "$HOME/meu-arquivo.txt"
check.sh 00 > "$TEMP/ambiente.log" 2>&1 || true
if grep -q 'meu-arquivo' "$TEMP/ambiente.log"; then cat "$TEMP/ambiente.log"; exit 1; fi
printf '✅ Inferência de exercício, reset isolado, exercício 00 com o arquivo do editor e números inválidos.\n'

printf '\n▶ Testes reais do projeto e geração do site\n'
"$CURSO_DIR/.venv/bin/python" -m pip install --disable-pip-version-check -q -r "$CURSO_DIR/templates/projeto/requirements.txt"
(
  cd "$LABS_DIR/07-deploy-no-pages"
  "$CURSO_DIR/.venv/bin/python" -m unittest -v
  "$CURSO_DIR/.venv/bin/python" build.py
  test -s dist/index.html
  for receita in 'Bolo de cenoura' 'Brigadeiro' 'Pão de queijo'; do grep -q "$receita" dist/index.html; done
  "$CURSO_DIR/.venv/bin/python" receitas.py | grep -q 'Pão de queijo (rende 25 unidades)'
  # O erro apresentado na aula deve realmente quebrar os testes, com os valores dos slides.
  sed -i 's/return gramas_por_receita \* receitas/return gramas_por_receita + receitas/' receitas.py
  if "$CURSO_DIR/.venv/bin/python" -m unittest > "$TEMP/teste-com-erro.log" 2>&1; then
    printf '❌ O bug da aula não foi detectado.\n'; exit 1
  fi
  grep -q FAILED "$TEMP/teste-com-erro.log"
  grep -q '503 != 1500' "$TEMP/teste-com-erro.log"
)
printf '\n✅ Suíte concluída. A publicação real no Actions/Pages é conferida na conta do aluno.\n'
