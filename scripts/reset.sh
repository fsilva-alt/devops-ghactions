#!/usr/bin/env bash
# Recria apenas o laboratório informado. Não altera o repositório no GitHub.
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
source "$SCRIPTS_DIR/labs.sh"
exigir_codespaces
[[ $# -le 1 ]] || { erro "Uso: reset.sh [01–$ULTIMO_NN]"; exit 2; }
nn="$(resolver_lab "${1:-}")" || exit 2
dir="$(lab_dir "$nn")"
if [[ -e "$dir" || -L "$dir" ]]; then
  [[ ! -L "$dir" && -f "$dir/.git/curso-actions/exercicio" ]] || {
    erro "A pasta não foi gerada por este curso: $dir"; exit 2;
  }
  [[ "$(cat "$dir/.git/curso-actions/exercicio")" == "$nn" ]] || exit 2
  cd "$LABS_DIR"
  rm -rf -- "$dir"
fi
gerar_lab "$nn"
ok "Exercício $nn recriado. Entre novamente: cd \"$dir\""
info "O remoto local foi removido; seu repositório no GitHub continua como estava. Veja a retomada no README do curso."
