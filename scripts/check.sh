#!/usr/bin/env bash
# Confere o exercício NN no Codespace e, se não estiver pronto, dá dicas.
#
# Uso:
#   check.sh 02            # analisa o YAML e simula o workflow com o act
#   check.sh               # dentro da pasta de um laboratório, detecta o exercício
#   check.sh 02 --sem-act  # só a análise do YAML, sem executar os jobs
#   check.sh 00            # confere se o ambiente está pronto para a aula
#
# Sai com 0 quando o exercício está pronto para publicar e 1 quando ainda não.
# Nada é enviado ao GitHub: a execução real continua sendo a da aba Actions.
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
exigir_codespaces

simular="${CURSO_SIMULAR:-1}"
args=()
for a in "$@"; do
  case "$a" in
    --sem-act) simular=0 ;;
    *) args+=("$a") ;;
  esac
done
[[ ${#args[@]} -le 1 ]] || { erro "Uso: check.sh [00–07] [--sem-act]"; exit 2; }
nn="$(resolver_lab "${args[0]:-}" 0)" || exit 2
python="$CURSO_DIR/.venv/bin/python"
[[ -x "$python" ]] || { erro "Verificador não instalado. Rode: sh \"$CURSO_DIR/install.sh\""; exit 2; }

FALHAS=()
falhar() { FALHAS+=("$1"$'\n   💡 '"$2"); }

# Exercício 00: as ferramentas da aula funcionam neste Codespace?
verificar_ambiente() {
  local nome email
  nome="$(git config user.name || true)"; email="$(git config user.email || true)"
  [[ -n "$nome" && -n "$email" ]] || falhar "O Git ainda não sabe seu nome e e-mail." \
    'git config --global user.name "Seu nome" e git config --global user.email "seu-email-da-conta-github"'
  if [[ "${CURSO_MODO_TESTE:-0}" != 1 ]]; then
    if ! command -v gh >/dev/null 2>&1; then
      falhar "O GitHub CLI (gh) não está instalado." "Use um Codespace com o modelo Blank, que já traz o gh."
    elif ! gh auth status --hostname github.com >/dev/null 2>&1; then
      falhar "O gh não está autenticado no GitHub." "Rode o instalador de novo: ele faz o login pelo navegador."
    elif ! gh auth status --hostname github.com 2>&1 | grep -q "'workflow'"; then
      falhar "O login do gh não tem o escopo workflow, necessário para enviar arquivos .github/workflows." \
        "gh auth refresh --hostname github.com --scopes workflow"
    fi
  fi
  local faltam=() n
  for n in {1..7}; do [[ -d "$(lab_dir "$(printf '%02d' "$n")")" ]] || faltam+=("$n"); done
  (( ${#faltam[@]} == 0 )) || falhar "Faltam laboratórios em $LABS_DIR: ${faltam[*]}." "setup.sh"
  if ! docker_ok; then
    falhar "O serviço do Docker não respondeu. O act precisa dele para criar os containers dos jobs." \
      "Num Codespace recém-aberto, espere um minuto e tente de novo."
  elif ! act_ok; then
    falhar "O act $ACT_VERSAO não está instalado em $ACT_BIN." "setup.sh"
  elif ! docker image inspect "$ACT_IMAGEM" >/dev/null 2>&1; then
    falhar "A imagem do runner local ($ACT_IMAGEM_NOME) ainda não foi baixada." "setup.sh"
  else
    info "Docker $(docker version -f '{{.Server.Version}}' 2>/dev/null) · act $ACT_VERSAO · imagem $ACT_IMAGEM_NOME"
    "$python" "$SCRIPTS_DIR/simular.py" 00 "$(mktemp -d)" || falhar \
      "O act não conseguiu executar um workflow mínimo." "Leia a mensagem acima. Se for a rede, pare e reabra o Codespace."
  fi
}

if [[ "$nn" == 00 ]]; then
  verificar_ambiente
  titulo="Exercício 00 — $(lab_nome 00)"
  if (( ${#FALHAS[@]} == 0 )); then
    ok "${C_NEG}$titulo${C_FIM}: concluído."
    exit 0
  fi
  erro "${C_NEG}$titulo${C_FIM}: ainda não. Encontrei ${#FALHAS[@]} ponto(s) para ajustar:"
  for f in "${FALHAS[@]}"; do printf '\n • %s\n' "$f"; done
  printf '\n'
  exit 1
fi

dir="$(lab_dir "$nn")"
[[ -d "$dir" ]] || { erro "A pasta do exercício $nn não existe ($dir)."; info "Gere com: setup.sh   (ou reset.sh $nn)"; exit 2; }
"$python" "$SCRIPTS_DIR/checks.py" "$nn" "$dir" || exit 1
if [[ "$simular" == 1 ]]; then
  "$python" "$SCRIPTS_DIR/simular.py" "$nn" "$dir" || exit 1
else
  info "Simulação com o act pulada (--sem-act): só o YAML foi conferido."
fi
ok "${C_NEG}Exercício $nn — $(lab_nome "$nn")${C_FIM}: pronto para publicar."
info "Publique e confira a entrega na aba Actions. A simulação local não substitui a execução no GitHub."
