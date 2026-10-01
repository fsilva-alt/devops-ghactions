#!/usr/bin/env bash
# Validação estática: não executa o workflow nem consulta a conta no GitHub.
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
exigir_codespaces
[[ $# -le 1 ]] || { erro "Uso: check.sh [01–07]"; exit 2; }
nn="$(resolver_lab "${1:-}")" || exit 2
dir="$(lab_dir "$nn")"
[[ -d "$dir" ]] || { erro "Laboratório ausente. Rode setup.sh."; exit 2; }
python="$CURSO_DIR/.venv/bin/python"
[[ -x "$python" ]] || { erro "Verificador não instalado. Rode: sh \"$CURSO_DIR/install.sh\""; exit 2; }
exec "$python" "$SCRIPTS_DIR/checks.py" "$nn" "$dir"
