# 06 — Artefatos do build

**20 minutos · Ambiente obrigatório: GitHub Codespaces**

## Objetivo

Guardar o site gerado como artefato e baixá-lo pela página da execução.

## Onde e estado inicial

```bash
cd ~/labs-actions/06-artefatos-do-build
code .github/workflows/ci.yml
```

O workflow já tem os jobs `testar` e `empacotar`, com `needs`. O site é gerado, mas seus arquivos não são preservados para download.

Um **artefato** é um conjunto de arquivos associado a uma execução: pode ser um site, relatório ou pacote. O runner é temporário; salvar o artefato permite recuperar o resultado depois.

## Tarefa

1. No final de `jobs.empacotar.steps`, **depois do build**, acrescente:

   ```yaml
   - name: Guardar o site
     uses: actions/upload-artifact@v4
     with:
       name: site
       path: dist/
       if-no-files-found: error
       retention-days: 7
   ```

   Alinhe o `-` com as outras etapas. `name` é o nome do artefato; `path` é a pasta que será enviada. O workflow falha se nenhum arquivo for encontrado. A retenção solicitada é de 7 dias.

2. Verifique e publique:

   ```bash
   check.sh 06
   git add .github/workflows/ci.yml
   git commit -m "Salva o site como artefato"
   gh repo create actions-06 --public --source=. --remote=origin --push
   gh browse --actions
   ```

3. Aguarde a execução terminar. Na página de resumo da execução, localize **Artifacts → site** e baixe o ZIP. Você precisa estar logado no GitHub.
4. Abra o ZIP e confira a presença de `index.html`. Abra o HTML no navegador: o cardápio deve aparecer.
5. No Codespace, altere o título do cardápio, faça commit e push. Baixe o artefato da **nova** execução e compare o título. Cada execução tem seu próprio artefato.

## Verificação e entrega

`check.sh 06` confere a configuração do upload. Entregue a URL da execução final, o nome `site` e confirme que o ZIP contém a página com o título atualizado.

**Build, artefato e deploy são etapas diferentes:** gerar o HTML, guardar o HTML e disponibilizá-lo em um endereço público. O upload de artefato não coloca o site no ar.

Se não houver artefato, confira se o build foi concluído, se o upload vem depois dele e se a pasta é `dist/`.

[Próximo: deploy no Pages →](../07-deploy-no-pages/README.md) · [Índice](../../README.md)
