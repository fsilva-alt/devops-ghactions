#!/usr/bin/env bash
# Testes de manutenção; o uso do curso pelos alunos exige Codespaces.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
case "${1:-}" in
  '') exec bash "$RAIZ/tests/solucoes.sh" ;;
  --docker)
    docker build -q -t curso-actions-testes -f "$RAIZ/tests/Dockerfile" "$RAIZ/tests"
    docker run --rm -v "$RAIZ:/curso:ro" curso-actions-testes bash /curso/tests/solucoes.sh
    ;;
  --act) exec bash "$RAIZ/tests/act.sh" ;;
  *) printf 'Uso: bash tests/rodar.sh [--docker | --act]\n' >&2; exit 2 ;;
esac
