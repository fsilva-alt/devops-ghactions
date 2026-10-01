#!/usr/bin/env bash
# Gera somente os laboratórios ausentes; preserva todo o trabalho existente.
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
source "$SCRIPTS_DIR/labs.sh"
exigir_codespaces
[[ $# -eq 0 ]] || { erro "Uso: setup.sh. Para recomeçar um exercício, use reset.sh NN."; exit 2; }
mkdir -p "$LABS_DIR"
gerados=0
for n in {1..7}; do
  nn="$(printf '%02d' "$n")"
  dir="$(lab_dir "$nn")"
  if [[ -e "$dir" || -L "$dir" ]]; then
    info "Mantido: $dir"
  else
    gerar_lab "$nn"
    gerados=$((gerados + 1))
  fi
done
ok "$gerados laboratório(s) criado(s). Os 7 exercícios ficam em $LABS_DIR."
