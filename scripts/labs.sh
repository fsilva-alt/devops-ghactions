#!/usr/bin/env bash
# Cada exercício recebe um projeto independente e um ponto de partida pronto.
# Carregado por setup.sh e reset.sh.
gerar_lab() (
  local nn="$1" dir base=""
  dir="$(lab_dir "$nn")"
  [[ ! -e "$dir" && ! -L "$dir" ]] || { erro "A pasta já existe: $dir"; return 1; }
  mkdir -p "$dir"
  cp -R "$CURSO_DIR/templates/projeto/." "$dir/"
  mkdir -p "$dir/.github/workflows"
  case "$nn" in
    02|04) base=01 ;;
    03) base=02 ;;
    05|08|10|11|12) base=03 ;;
    06|09|13) base=05 ;;
    07|14) base=06 ;;
  esac
  if [[ -n "$base" ]]; then
    cp "$CURSO_DIR/docs/solucoes/$base.yml" "$dir/.github/workflows/ci.yml"
  fi
  cd "$dir"
  g init -q -b main
  g add -A
  GIT_AUTHOR_DATE='2026-09-01T09:00:00Z' GIT_COMMITTER_DATE='2026-09-01T09:00:00Z' \
    g -c user.name='Equipe do curso' -c user.email='curso@example.com' \
    commit -q -m "Prepara exercício $nn de GitHub Actions"
  mkdir -p .git/curso-actions
  printf '%s\n' "$nn" > .git/curso-actions/exercicio
)
