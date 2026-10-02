#!/usr/bin/env bash
# Simulação real com o act: instala o curso em um HOME descartável, baixa o act e a
# imagem do runner local, e confere o exercício 00, as 14 soluções e as falhas da aula.
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

reprovar 00; contem 'meu-arquivo.txt ainda não existe'
printf 'Estou pronto para a aula de GitHub Actions!\n' > "$HOME/meu-arquivo.txt"
aprovar 00; contem 'Olá do runner local!'
printf '✅ 00: arquivo do editor conferido e workflow mínimo executado em um container.\n'

reprovar 02; contem 'Acrescente o evento push'
for n in $(seq 1 14); do
  nn="$(printf '%02d' "$n")"
  lab="$(echo "$LABS_DIR/$nn"-*)"
  cp "$CURSO_DIR/docs/solucoes/$nn.yml" "$lab/.github/workflows/ci.yml"
  if [[ "$nn" == 13 ]]; then
    mkdir -p "$lab/.github/actions/preparar"
    cp "$CURSO_DIR/docs/solucoes/13-acao.yml" "$lab/.github/actions/preparar/action.yml"
  fi
  aprovar "$nn"
  contem 'Simulação concluída'
  case "$nn" in
    01) contem 'Olá, GitHub Actions!' ;;
    02|03|10) contem 'Ran 3 tests' ;;
    04) contem 'Receita do dia: Brigadeiro'; contem 'Turma: turma-local'; contem 'Segredo disponível' ;;
    05|09|13) contem 'Site gerado em dist/index.html com 3 receitas' ;;
    06) contem 'artefato site: index.html' ;;
    07) contem 'empacotar e publicar não rodaram' ;;
    08) contem 'testar (3.11)'; contem 'testar (3.13)'; contem '3 cópias do job testar' ;;
    11) contem 'Ran 3 tests' ;;
    12) contem 'O livro tem 3 receitas.'; contem 'resumo ✅ Escrever o resumo da execução' ;;
    14) contem 'lancar não rodou' ;;
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

# 11: uma receita sem Rende: reprova o job validar e aparece como anotação.
lab="$LABS_DIR/11-anotacoes-no-pull-request"
printf '# Café coado\n\n## Ingredientes\n\n- 500 ml de água\n' > "$lab/receitas/cafe.md"
reprovar 11; contem '::error file=receitas/cafe.md'; contem 'O job validar falhou'
rm "$lab/receitas/cafe.md"
printf '✅ 11: a receita sem rendimento reprova a simulação com a anotação.\n'

# Sem needs no 07, o if continua barrando o deploy no PR; sem o if, a simulação reprova.
lab="$LABS_DIR/07-deploy-no-pages"
sed -i '/^  publicar:$/,/^    runs-on/{/^    if:/d}' "$lab/.github/workflows/ci.yml"
check.sh 07 --sem-act > "$saida" 2>&1 && { cat "$saida"; exit 1; }
contem 'exclua pull_request'
printf '\n✅ Simulação com o act concluída.\n'
