#!/usr/bin/env bash
# Simulação real com o act: instala o curso em um HOME descartável, baixa o act e a
# imagem do runner local, e confere o exercício 00, as 7 soluções e as falhas da aula.
# Exige Docker e acesso à internet; não usa conta GitHub.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docker info >/dev/null 2>&1 || { printf '❌ Este teste precisa do Docker.\n' >&2; exit 2; }
TEMP="$(mktemp -d "${TMPDIR:-/tmp}/curso-actions-act.XXXXXX")"
trap 'rm -rf -- "$TEMP"' EXIT
export HOME="$TEMP/home"
unset CURSO_DIR LABS_DIR CURSO_RAMO CURSO_SIMULAR GH_TOKEN GITHUB_TOKEN
export CURSO_MODO_TESTE=1 CURSO_AUTH_GITHUB=0 CODESPACES=false
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$HOME/.gitconfig"
mkdir -p "$HOME" "$TEMP/origem" "$TEMP/workspace"
git config --global user.name 'Teste do act'
git config --global user.email 'teste@example.com'
tar -C "$RAIZ" --exclude=.git --exclude=.venv --exclude=bin --exclude=__pycache__ -cf - . | tar -C "$TEMP/origem" -xf -
git -C "$TEMP/origem" init -q -b main
git -C "$TEMP/origem" add .
git -C "$TEMP/origem" commit -qm 'Material do curso'
export CURSO_REPO="file://$TEMP/origem"

printf '▶ Instalação com o act e a imagem do runner local\n'
(cd "$TEMP/workspace" && sh "$TEMP/origem/install.sh")
export CURSO_DIR="$HOME/devops-ghactions" LABS_DIR="$HOME/labs"
export PATH="$CURSO_DIR/scripts:$CURSO_DIR/bin:$PATH"
act --version | grep -q 'act version'

saida="$TEMP/saida.log"
aprovar() { check.sh "$1" > "$saida" 2>&1 || { cat "$saida"; printf '❌ check.sh %s deveria aprovar.\n' "$1"; exit 1; }; }
reprovar() { if check.sh "$1" > "$saida" 2>&1; then cat "$saida"; printf '❌ check.sh %s deveria reprovar.\n' "$1"; exit 1; fi; }
contem() { grep -qF -- "$1" "$saida" || { cat "$saida"; printf '❌ Saída sem: %s\n' "$1"; exit 1; }; }

aprovar 00; contem 'Olá do runner local!'
printf '✅ 00: workflow mínimo executado em um container.\n'

reprovar 02; contem 'Acrescente o evento push'
for n in 1 2 3 4 5 6 7; do
  nn="$(printf '%02d' "$n")"
  cp "$CURSO_DIR/docs/solucoes/$nn.yml" "$(echo "$LABS_DIR/$nn"-*)/.github/workflows/ci.yml"
  aprovar "$nn"
  contem 'Simulação concluída'
  case "$nn" in
    01) contem 'Olá, GitHub Actions!' ;;
    02|03) contem 'Ran 3 tests' ;;
    04) contem 'Receita do dia: Brigadeiro'; contem 'Turma: turma-local'; contem 'Segredo disponível' ;;
    05) contem 'Site gerado em dist/index.html com 3 receitas' ;;
    06) contem 'artefato site: index.html' ;;
    07) contem 'empacotar e publicar não rodaram' ;;
  esac
  printf '✅ %s: solução aprovada na simulação.\n' "$nn"
done

# As falhas provocadas na aula aparecem na simulação como aparecem no GitHub.
for nn in 03 05; do
  lab="$(echo "$LABS_DIR/$nn"-*)"
  sed -i 's/return gramas_por_receita \* receitas/return gramas_por_receita + receitas/' "$lab/receitas.py"
  reprovar "$nn"; contem '503 != 1500'
  [[ "$nn" == 05 ]] && contem 'O job empacotar foi pulado'
  git -C "$lab" checkout -q receitas.py
done
printf '✅ 03 e 05: a falha proposital reprova a simulação com 503 != 1500.\n'

# Sem needs no 07, o if continua barrando o deploy no PR; sem o if, a simulação reprova.
lab="$LABS_DIR/07-deploy-no-pages"
sed -i '/^  publicar:$/,/^    runs-on/{/^    if:/d}' "$lab/.github/workflows/ci.yml"
check.sh 07 --sem-act > "$saida" 2>&1 && { cat "$saida"; exit 1; }
contem 'exclua pull_request'
printf '\n✅ Simulação com o act concluída.\n'
