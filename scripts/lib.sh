#!/usr/bin/env bash
# Biblioteca compartilhada pelos comandos do curso.
set -euo pipefail

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CURSO_DIR="$(cd "$SCRIPTS_DIR/.." && pwd)"
LABS_DIR="${LABS_DIR:-$HOME/labs}"
LAB_NOMES=("" "primeiro-workflow" "testes-no-push" "checks-no-pull-request"
  "variaveis-e-contextos" "jobs-e-dependencias" "artefatos-do-build" "deploy-no-pages")

info() { printf '▶ %s\n' "$*"; }
ok() { printf '✅ %s\n' "$*"; }
erro() { printf '❌ %s\n' "$*" >&2; }

exigir_codespaces() {
  if [[ "${CODESPACES:-}" != true && "${CURSO_MODO_TESTE:-0}" != 1 ]]; then
    erro "Este curso usa obrigatoriamente o GitHub Codespaces. Crie um Codespace com o modelo Blank e siga a preparação do README."
    exit 2
  fi
}

normalizar_num() {
  local n="${1%%-*}"
  [[ "$n" =~ ^[0-9]{1,2}$ ]] || return 1
  (( 10#$n >= 1 && 10#$n <= 7 )) || return 1
  printf '%02d' "$((10#$n))"
}

lab_nome() { printf '%s' "${LAB_NOMES[$((10#$1))]}"; }
lab_dir() { printf '%s/%s-%s' "$LABS_DIR" "$1" "$(lab_nome "$1")"; }

resolver_lab() {
  local entrada="${1:-}" rel nn pasta labs
  if [[ -z "$entrada" ]]; then
    pasta="$(pwd -P)"
    labs="$(cd "$LABS_DIR" && pwd -P)"
    rel="${pasta#"$labs"/}"
    [[ "$rel" != "$pasta" ]] || { erro "Informe o exercício: check.sh 01 (de 01 a 07)."; return 1; }
    entrada="${rel%%/*}"
  fi
  nn="$(normalizar_num "$entrada")" || { erro "Exercício inválido: '$entrada'. Use 01 a 07."; return 1; }
  printf '%s' "$nn"
}

g() { git -c commit.gpgsign=false -c core.hooksPath=/dev/null -c core.editor=true "$@"; }
