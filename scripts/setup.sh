#!/usr/bin/env bash
# Gera somente os laboratórios ausentes e prepara o act; preserva todo o trabalho existente.
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
source "$SCRIPTS_DIR/labs.sh"
exigir_codespaces
[[ $# -eq 0 ]] || { erro "Uso: setup.sh. Para recomeçar um exercício, use reset.sh NN."; exit 2; }
mkdir -p "$LABS_DIR"
gerados=0
for (( n = 1; n <= ULTIMO_LAB; n++ )); do
  nn="$(printf '%02d' "$n")"
  dir="$(lab_dir "$nn")"
  if [[ -e "$dir" || -L "$dir" ]]; then
    info "Mantido: $dir"
  else
    gerar_lab "$nn"
    gerados=$((gerados + 1))
  fi
done
ok "$gerados laboratório(s) criado(s). Os $ULTIMO_LAB laboratórios ficam em $LABS_DIR; os de 08 a $ULTIMO_NN são opcionais."

# CURSO_SIMULAR=0 dispensa o act, por exemplo nos testes sem Docker.
[[ "${CURSO_SIMULAR:-1}" == 1 ]] || exit 0
if instalar_act; then
  ok "act $ACT_VERSAO pronto para simular os workflows no Codespace."
fi
if ! docker_ok; then
  aviso "O Docker não respondeu. Espere um minuto e rode setup.sh de novo; check.sh 00 mostra o que falta."
elif docker image inspect "$ACT_IMAGEM" >/dev/null 2>&1; then
  info "Imagem do runner local já disponível: $ACT_IMAGEM_NOME"
else
  info "Baixando a imagem do runner local ($ACT_IMAGEM_NOME, cerca de 2 GB). Na primeira vez leva alguns minutos..."
  if docker pull -q "$ACT_IMAGEM" >/dev/null; then
    ok "Imagem do runner local baixada."
  else
    aviso "Não foi possível baixar $ACT_IMAGEM_NOME. Rode setup.sh de novo antes da aula."
  fi
fi
