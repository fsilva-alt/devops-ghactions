#!/usr/bin/env bash
# Biblioteca compartilhada pelos comandos do curso. Não execute este arquivo
# diretamente: ele é carregado (source) por setup.sh, check.sh e reset.sh.
set -euo pipefail

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CURSO_DIR="$(cd "$SCRIPTS_DIR/.." && pwd)"
LABS_DIR="${LABS_DIR:-$HOME/labs}"

# Nome de cada exercício, indexado pelo número. O 00 confere o ambiente e não tem pasta.
# Do 08 ao 14, os exercícios são opcionais, para praticar depois da aula.
LAB_NOMES=("ambiente-pronto" "primeiro-workflow" "testes-no-push" "checks-no-pull-request"
  "variaveis-e-contextos" "jobs-e-dependencias" "artefatos-do-build" "deploy-no-pages"
  "matriz-de-versoes" "cache-de-dependencias" "caminhos-e-agenda" "anotacoes-no-pull-request"
  "saidas-e-resumo" "acao-composta" "release-por-tag")
ULTIMO_LAB=$(( ${#LAB_NOMES[@]} - 1 ))
ULTIMO_NN="$(printf '%02d' "$ULTIMO_LAB")"

# O act executa os workflows no Codespace, cada job em um container Docker.
# A imagem imita o runner ubuntu-latest do GitHub; o setup.sh baixa as duas coisas.
# O digest fixa a versão testada da imagem: a tag act-latest muda com o tempo.
ACT_VERSAO=0.2.89
ACT_BIN="$CURSO_DIR/bin/act"
ACT_IMAGEM_NOME="catthehacker/ubuntu:act-latest"
ACT_IMAGEM="${CURSO_ACT_IMAGEM:-catthehacker/ubuntu@sha256:c58e2b364da03b0c804c7d660f2ecbedf2f221a382b9baa0b344b0144780ff43}"
export ACT_BIN ACT_IMAGEM ACT_IMAGEM_NOME

if [[ -t 1 ]]; then
  C_VERDE=$'\e[32m'; C_VERM=$'\e[31m'; C_AMAR=$'\e[33m'; C_AZUL=$'\e[34m'
  C_NEG=$'\e[1m'; C_FIM=$'\e[0m'
else
  C_VERDE=""; C_VERM=""; C_AMAR=""; C_AZUL=""; C_NEG=""; C_FIM=""
fi

info()  { printf '%s\n' "${C_AZUL}▶${C_FIM} $*"; }
ok()    { printf '%s\n' "${C_VERDE}✅${C_FIM} $*"; }
aviso() { printf '%s\n' "${C_AMAR}⚠️ ${C_FIM} $*"; }
erro()  { printf '%s\n' "${C_VERM}❌${C_FIM} $*" >&2; }

exigir_codespaces() {
  if [[ "${CODESPACES:-}" != true && "${CURSO_MODO_TESTE:-0}" != 1 ]]; then
    erro "Este curso usa obrigatoriamente o GitHub Codespaces. Crie um Codespace com o modelo Blank e siga a preparação do README."
    exit 2
  fi
}

# normalizar_num "5" | "05" | "05-nome" [mínimo]  ->  "05"
normalizar_num() {
  local n="${1%%-*}" minimo="${2:-1}"
  [[ "$n" =~ ^[0-9]{1,2}$ ]] || return 1
  (( 10#$n >= minimo && 10#$n <= ULTIMO_LAB )) || return 1
  printf '%02d' "$((10#$n))"
}

lab_nome() { printf '%s' "${LAB_NOMES[$((10#$1))]}"; }
lab_dir() { printf '%s/%s-%s' "$LABS_DIR" "$1" "$(lab_nome "$1")"; }

# resolver_lab [entrada] [mínimo]: sem entrada, descobre o número pela pasta atual.
resolver_lab() {
  local entrada="${1:-}" minimo="${2:-1}" rel nn pasta labs
  if [[ -z "$entrada" ]]; then
    pasta="$(pwd -P)"
    labs="$(cd "$LABS_DIR" 2>/dev/null && pwd -P)" || labs="$LABS_DIR"
    rel="${pasta#"$labs"/}"
    [[ "$rel" != "$pasta" ]] || { erro "Informe o exercício: check.sh 01 (de $(printf '%02d' "$minimo") a $ULTIMO_NN)."; return 1; }
    entrada="${rel%%/*}"
  fi
  nn="$(normalizar_num "$entrada" "$minimo")" || {
    erro "Exercício inválido: '$entrada'. Use $(printf '%02d' "$minimo") a $ULTIMO_NN."; return 1;
  }
  printf '%s' "$nn"
}

docker_ok() { command -v docker >/dev/null 2>&1 && timeout 20 docker info >/dev/null 2>&1; }
act_ok() { [[ -x "$ACT_BIN" ]] && "$ACT_BIN" --version 2>/dev/null | grep -qF "version $ACT_VERSAO"; }

# Baixa o act da página de versões do projeto e confere o arquivo pelo checksum publicado.
instalar_act() {
  act_ok && return 0
  local arq tmp base
  case "$(uname -m)" in
    x86_64|amd64) arq=x86_64 ;;
    aarch64|arm64) arq=arm64 ;;
    *) aviso "Arquitetura $(uname -m) sem act pronto para baixar."; return 1 ;;
  esac
  base="https://github.com/nektos/act/releases/download/v$ACT_VERSAO"
  tmp="$(mktemp -d)"
  if ! curl -fsSL -o "$tmp/act_Linux_$arq.tar.gz" "$base/act_Linux_$arq.tar.gz" \
    || ! curl -fsSL -o "$tmp/checksums.txt" "$base/checksums.txt"; then
    rm -rf -- "$tmp"; aviso "Não foi possível baixar o act $ACT_VERSAO. Confira a conexão e rode setup.sh de novo."; return 1
  fi
  if ! (cd "$tmp" && grep " act_Linux_$arq.tar.gz\$" checksums.txt | sha256sum -c --quiet >/dev/null 2>&1); then
    rm -rf -- "$tmp"; aviso "O arquivo do act não confere com o checksum publicado. Rode setup.sh de novo."; return 1
  fi
  tar -xzf "$tmp/act_Linux_$arq.tar.gz" -C "$tmp" act
  mkdir -p "$(dirname "$ACT_BIN")"
  mv "$tmp/act" "$ACT_BIN"
  rm -rf -- "$tmp"
}

g() { git -c commit.gpgsign=false -c core.hooksPath=/dev/null -c core.editor=true "$@"; }
