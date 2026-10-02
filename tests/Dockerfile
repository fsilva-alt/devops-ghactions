FROM ubuntu:24.04

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      git curl ca-certificates python3 python3-venv zsh util-linux nodejs \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash aluno \
 && mkdir -p /tmp/opencode \
 && chown aluno:aluno /tmp/opencode
USER aluno
WORKDIR /home/aluno
