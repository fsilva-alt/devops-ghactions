'use strict';

const REPO = 'https://github.com/fsilva-alt/devops-ghactions';
const esc = text => String(text).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const code = text => `<pre><code>${esc(text)}</code></pre>`;
const box = (title, text) => `<div class="box"><h3>${title}</h3>${text}</div>`;
const list = items => `<ol class="task-list">${items.map(item => `<li>${item}</li>`).join('')}</ol>`;
const cols = (left, right) => `<div class="slide-columns"><div class="slide-stack">${left}</div><div class="slide-stack">${right}</div></div>`;
const flow = items => `<div class="flow">${items.map(item => `<span>${item}</span>`).join('<b aria-hidden="true">→</b>')}</div>`;

const exercicios = [
  {id:'01', slug:'primeiro-workflow', title:'Primeiro workflow', time:15, tags:'workflow · job · step',
    description:'Escreva uma automação, aperte o play e descubra onde cada etapa acontece.',
    conceito:'Um evento dá início a tudo.',
    explicacao:'Um <strong>workflow</strong> descreve a automação em YAML. Dentro dele, cada <strong>job</strong> executa em um <strong>runner</strong>. Cada item de <code>steps</code> é uma etapa desse job.',
    exemplo:'name: Boas-vindas\n\non:\n  workflow_dispatch:\n\npermissions:\n  contents: read\n\njobs:\n  boas-vindas:\n    runs-on: ubuntu-latest\n    steps:\n      - run: echo "Olá, GitHub Actions!"',
    destaque:'YAML usa espaços para a indentação. O traço inicia um item de lista. O arquivo precisa estar em .github/workflows/ci.yml.',
    tarefas:['Crie <code>.github/workflows/ci.yml</code> com o exemplo e salve no Codespace.', 'Execute <code>check.sh 01</code>, faça commit e publique em <code>actions-01</code>.', 'Abra Actions → Boas-vindas → Run workflow. Selecione <code>main</code>.', 'Abra o job e localize a saudação no log.'],
    entrega:'Link da execução manual verde e a mensagem no log.',
    pergunta:'O echo executou no seu Codespace ou em um runner?',
    resposta:'Em um runner do Actions. O Codespace é o ambiente em que você escreveu e publicou o arquivo.',
    doc:'https://docs.github.com/pt/actions/get-started/understand-github-actions'},
  {id:'02', slug:'testes-no-push', title:'Testes no push', time:25, tags:'push · uses · run',
    description:'Prepare o ambiente e deixe o GitHub executar os testes a cada mudança.',
    conceito:'O mesmo teste, a cada push.',
    explicacao:'<strong>CI</strong> significa integração contínua: verificar mudanças automaticamente. <code>uses</code> chama uma action pronta; <code>run</code> executa um comando no runner. <code>with</code> configura uma action.',
    exemplo:"on:\n  push:\n    branches: [main]\n  workflow_dispatch:\n\n# Etapas do job testar:\nsteps:\n  - uses: actions/checkout@v5\n  - uses: actions/setup-python@v6\n    with:\n      python-version: '3.12'\n  - run: python -m pip install -r requirements.txt\n  - run: python -m unittest -v",
    destaque:'Trechos de YAML: o enunciado contém o workflow completo. Checkout vem primeiro porque o runner precisa receber os arquivos do projeto.',
    tarefas:['Entre no laboratório e rode <code>python3 -m unittest -v</code>. São três testes prontos.', 'Siga o enunciado para trocar a saudação por checkout, Python, instalação e testes.', 'Confira com <code>check.sh 02</code> e publique em <code>actions-02</code>.', 'Mude o título do cardápio, faça commit e push. Acompanhe a nova execução.'],
    entrega:'Execução verde disparada por push, com três testes aprovados.',
    pergunta:'Instalar uma dependência no Codespace a instala também no runner?',
    resposta:'Não. São máquinas separadas. O workflow precisa preparar seu próprio ambiente.',
    doc:'https://docs.github.com/pt/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows'},
  {id:'03', slug:'checks-no-pull-request', title:'Checks no pull request', time:25, tags:'pull_request · logs · correção',
    description:'Veja um teste falhar, encontre a causa e corrija antes de integrar a mudança.',
    conceito:'Uma falha é informação útil.',
    explicacao:'<code>pull_request</code> testa uma proposta de mudança. O filtro de branch indica o <strong>destino</strong> do PR. Abra a etapa que falhou e procure o resultado esperado e o recebido.',
    exemplo:'on:\n  push:\n    branches: [main]\n  pull_request:\n    branches: [main]\n  workflow_dispatch:\n\n# Falha proposital em app.py:\n# return preco_centavos + quantidade\n\n# Correção:\n# return preco_centavos * quantidade',
    destaque:'Cada execução corresponde a uma revisão do código. Reexecutar um commit quebrado não aplica a correção que ainda está só no Codespace.',
    tarefas:['Acrescente o evento <code>pull_request</code> ao workflow e publique a main em <code>actions-03</code>.', 'Crie a branch <code>teste-do-ci</code>. Troque a multiplicação por soma em <code>app.py</code>.', 'Faça commit, push e abra o PR. Leia o erro em Checks → testar → Testar.', 'Corrija para multiplicação, faça novo commit e push na mesma branch. Confira o novo check.'],
    entrega:'PR com links de uma execução vermelha e outra verde após a correção.',
    pergunta:'Um check vermelho sempre impede o merge?',
    resposta:'Só quando regras do repositório exigem aquele check. Aqui aprendemos a observar e interpretar o resultado.',
    doc:'https://docs.github.com/pt/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs'},
  {id:'04', slug:'variaveis-e-contextos', title:'Variáveis e contextos', time:20, tags:'env · inputs · vars · secrets',
    description:'Personalize uma execução e descubra de onde vêm seus valores.',
    conceito:'Cada informação tem uma origem.',
    explicacao:'<code>env</code> define variáveis no arquivo. <code>inputs</code> recebe a entrada manual. <code>github</code> traz dados da execução. <code>vars</code> e <code>secrets</code> vêm das configurações do repositório.',
    exemplo:'# Dentro de uma etapa:\nenv:\n  MENSAGEM: ${{ inputs.mensagem }}\n  AUTOR: ${{ github.actor }}\n  TURMA: ${{ vars.TURMA }}\nrun: |\n  printf "%s\\n" "$MENSAGEM"\n  printf "%s\\n" "$AUTOR" "$TURMA"\n\n# Em outra etapa, sem imprimir o segredo:\nenv:\n  TOKEN_DEMO: ${{ secrets.CURSO_TOKEN }}\nrun: test -n "$TOKEN_DEMO"',
    destaque:'São trechos de duas etapas. O Actions avalia ${{ }}; o shell lê $VARIAVEL. O exemplo completo passa a entrada por env e usa um segredo fictício.',
    tarefas:['Copie o exemplo 04 indicado no enunciado e personalize o valor padrão da mensagem.', 'Publique em <code>actions-04</code>. Nas configurações, crie a variável <code>TURMA</code>.', 'Cadastre <code>CURSO_TOKEN</code> com o valor fictício <code>somente-demonstracao</code>.', 'Execute manualmente com uma mensagem sua. Observe autor, turma e a confirmação de presença do segredo.'],
    entrega:'Execução verde com mensagem personalizada e segredo verificado sem exibir seu valor.',
    pergunta:'Qual a diferença entre a expressão do Actions e a variável do shell?',
    resposta:'A expressão consulta um contexto do Actions. A variável de ambiente entrega esse valor ao comando que executa no runner.',
    doc:'https://docs.github.com/pt/actions/learn-github-actions/contexts'},
  {id:'05', slug:'jobs-e-dependencias', title:'Jobs e dependências', time:20, tags:'needs · runner · build',
    description:'Conecte os testes ao build e observe o que acontece quando algo falha.',
    conceito:'Teste primeiro. Gere depois.',
    explicacao:'Etapas de um job executam em sequência. Jobs podem executar em paralelo. <code>needs: testar</code> faz o job de build aguardar os testes e só prosseguir se eles passarem.',
    exemplo:"# Segundo job, dentro de jobs:\nempacotar:\n  needs: testar\n  runs-on: ubuntu-latest\n  steps:\n    - uses: actions/checkout@v5\n    - uses: actions/setup-python@v6\n      with:\n        python-version: '3.12'\n    - run: python -m pip install -r requirements.txt\n    - run: python build.py\n    - run: test -s dist/index.html",
    destaque:'Cada job usa outro runner. Por isso, o build também precisa de checkout, Python e instalação das dependências.',
    tarefas:['Acrescente <code>empacotar</code> no mesmo nível de <code>testar</code>, dentro de <code>jobs</code>.', 'Confira com <code>check.sh 05</code> e publique em <code>actions-05</code>. Veja o grafo da execução.', 'Troque temporariamente * por + no retorno de app.py e publique. Observe o build como skipped.', 'Corrija a multiplicação e publique novamente. Termine com os dois jobs verdes.'],
    entrega:'Execução final verde e exemplo anterior com o build pulado.',
    pergunta:'O arquivo criado por testar aparece automaticamente em empacotar?',
    resposta:'Não. Jobs separados não compartilham o sistema de arquivos. Já as etapas do mesmo job compartilham seus arquivos.',
    doc:'https://docs.github.com/pt/actions/using-jobs/using-jobs-in-a-workflow'},
  {id:'06', slug:'artefatos-do-build', title:'Artefatos do build', time:20, tags:'upload-artifact · download',
    description:'Guarde o resultado da execução e baixe seu primeiro pacote de site.',
    conceito:'O runner termina. O resultado fica.',
    explicacao:'Um <strong>artefato</strong> guarda arquivos de uma execução para consulta ou distribuição. Aqui vamos guardar a pasta <code>dist/</code>, que contém o site gerado pelo build.',
    exemplo:'# Última etapa de empacotar:\n- name: Guardar o site\n  uses: actions/upload-artifact@v4\n  with:\n    name: site\n    path: dist/\n    if-no-files-found: error\n    retention-days: 7',
    destaque:'O upload deve vir depois do build. Guardar um ZIP como artefato ainda não publica o site na web.',
    tarefas:['Adicione o upload no final das etapas do job <code>empacotar</code>.', 'Confira com <code>check.sh 06</code> e publique em <code>actions-06</code>.', 'Após a execução, encontre Artifacts → site. Baixe e inspecione o ZIP.', 'Personalize o título do cardápio e publique outra execução. Compare o novo artefato.'],
    entrega:'Link da execução final e confirmação de index.html com o título atualizado dentro do ZIP.',
    pergunta:'Onde procurar um artefato de uma versão anterior?',
    resposta:'Na execução daquele commit, enquanto o artefato não tiver expirado ou sido removido.',
    doc:'https://docs.github.com/pt/actions/using-workflows/storing-workflow-data-as-artifacts'},
  {id:'07', slug:'deploy-no-pages', title:'Deploy no Pages', time:30, tags:'testar → gerar → publicar',
    description:'Junte os fundamentos em uma publicação guiada. Seu cardápio, agora com endereço público.',
    conceito:'Seu primeiro site no ar.',
    explicacao:'O <strong>deploy</strong> disponibiliza o resultado para outras pessoas. O Pages recebe um artefato próprio e publica seu HTML. O workflow completo é fornecido e explicado passo a passo.',
    exemplo:"# Job final do exemplo guiado:\npublicar:\n  needs: empacotar\n  if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'\n  runs-on: ubuntu-latest\n  permissions:\n    pages: write\n    id-token: write\n  environment:\n    name: github-pages\n    url: ${{ steps.deploy.outputs.page_url }}\n  steps:\n    - id: deploy\n      uses: actions/deploy-pages@v4",
    destaque:'O exemplo completo também testa, gera e envia o artefato específico do Pages. Não é necessário cadastrar um token pessoal para publicar.',
    tarefas:['Publique o estado inicial em <code>actions-07</code>. Em Settings → Pages, escolha Source: GitHub Actions.', 'No Codespace, copie o workflow guiado 07 e leia testar → empacotar → publicar.', 'Personalize o título do cardápio, rode <code>check.sh 07</code>, faça commit e push.', 'Acompanhe o deploy e abra a URL do environment github-pages.'],
    entrega:'URL pública do site e link da execução bem-sucedida de deploy.',
    pergunta:'Qual é a diferença entre build, artefato e deploy?',
    resposta:'Build gera os arquivos. Artefato guarda os arquivos. Deploy disponibiliza o resultado em seu destino, aqui o Pages.',
    doc:'https://docs.github.com/pt/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages'},
];

const introducao = [
  {title:'Um Codespace. Sete descobertas.', label:'ANTES DE COMEÇAR', body:cols(
    '<p class="lead">Automatizar é transformar uma sequência de passos em um processo que você pode repetir e conferir.</p>' + box('O projeto já está pronto', '<p>Um cardápio em Python, três testes e um gerador de HTML. Você vai aprender a descrever o processo no YAML, sem precisar programar a aplicação.</p>'),
    box('Preparação obrigatória', '<p>Crie o Codespace a partir do repositório do curso. Aguarde a preparação, execute <code>sh install.sh</code>, faça o login e abra um terminal novo.</p><p>Você precisa de noções de commit, branch e push. Os comandos de publicação estão nos enunciados.</p>') + '<a class="button primary" href="'+REPO+'#antes-da-aula">Abrir a preparação completa ↗</a>')},
  {title:'Saiba onde cada coisa acontece.', label:'SEU AMBIENTE', body:
    flow(['Codespace', 'GitHub', 'Runner', 'Pages']) + cols(
      box('Codespace: seu ambiente de trabalho', '<p>VS Code e terminal no navegador. Aqui você edita, salva, faz commit e push. É obrigatório nos 7 exercícios.</p>') + box('GitHub: código e eventos', '<p>Recebe o push, armazena o workflow e cria uma execução quando um evento corresponde à configuração.</p>'),
      box('Runner: execução do job', '<p>Uma máquina preparada pelo Actions executa as etapas. Ela não herda os arquivos e instalações do Codespace.</p>') + box('Pages: destino do site', '<p>Hospeda o HTML do último exercício em uma URL pública. Você acessa o resultado no navegador.</p>'))},
  {title:'Seu ciclo de aprendizagem.', label:'COMO ACOMPANHAR', body:cols(
    list(['Leia o enunciado e entre na pasta <code>~/labs-actions/NN-nome</code>.', 'Edite o workflow no Codespace. Salve antes de testar.', 'Rode <code>check.sh NN</code>. Leia as dicas e ajuste o YAML.', 'Faça commit e publique o laboratório na sua conta.', 'Abra Actions e confira a entrega pedida no enunciado.']),
    box('Sete pontos de partida independentes', '<p>Cada laboratório já traz os arquivos necessários. Use um repositório público por exercício, actions-01 a actions-07, sem abrir outro Codespace.</p>') + '<div class="callout">O check local analisa alguns requisitos do YAML. A execução na aba Actions é que mostra o resultado real.</div>' + box('Três conceitos para levar', '<p><strong>CI:</strong> verificar mudanças automaticamente.<br><strong>Build:</strong> gerar os arquivos finais.<br><strong>Deploy:</strong> publicar o resultado.</p>'))},
];

function slides(exercicio) {
  const enunciado = `${REPO}/blob/main/exercises/${exercicio.id}-${exercicio.slug}/README.md`;
  return [
    {title:exercicio.title, label:`EXERCÍCIO ${exercicio.id} · ${exercicio.time} MINUTOS`, body:cols(
      `<p class="lead">${exercicio.description}</p>` + flow(exercicio.tags.split(' · ')),
      box('No terminal do Codespace', code(`cd ~/labs-actions/${exercicio.id}-${exercicio.slug}\ncode .github/workflows/ci.yml`)) + `<a class="button primary" href="${enunciado}" target="_blank" rel="noopener">Abrir o enunciado completo ↗</a>` + '<p class="small-note">A duração inclui explicação, demonstração e prática.</p>')},
    {title:exercicio.conceito, label:'ENTENDA O FUNDAMENTO', body:cols(
      `<p class="lead">${exercicio.explicacao}</p><div class="callout">${exercicio.destaque}</div>`, code(exercicio.exemplo))},
    {title:'Agora é com você.', label:`PRÁTICA GUIADA · ${exercicio.id}`, body:cols(
      list(exercicio.tarefas), box('Conferir no Codespace', code(`check.sh ${exercicio.id}`)) + box('Conferir no GitHub', `<p>${exercicio.entrega}</p>`) + `<a href="${enunciado}" target="_blank" rel="noopener">Comandos e instruções de cada passo ↗</a>`)},
    {title:'Conecte o que você aprendeu.', label:'CONFERÊNCIA E REFLEXÃO', body:cols(
      `<p class="lead">${exercicio.pergunta}</p><details class="box"><summary>Ver a explicação</summary><p>${exercicio.resposta}</p></details>`,
      box('Sua entrega', `<p>${exercicio.entrega}</p>`) + `<a href="${exercicio.doc}" target="_blank" rel="noopener">Consultar a documentação oficial ↗</a>` + (exercicio.id === '07' ? '<div class="callout">Você concluiu os 7 exercícios! Guarde seus links, publique as mudanças que deseja manter e pare o Codespace.</div>' : '<p class="small-note">O próximo exercício começa em outro laboratório já preparado.</p>'))},
  ];
}

const grid = document.getElementById('exercicios');
grid.innerHTML = exercicios.map(e => `<a class="exercise-card ${e.id === '07' ? 'featured' : ''}" href="#/${e.id}"><div class="card-top"><span class="card-number">${e.id}</span><span class="card-time">${e.time} min</span></div><div><h3>${e.title}</h3><p>${e.description}</p></div><div class="card-bottom"><span>${e.tags}</span><b aria-hidden="true">↗</b></div></a>`).join('');

const grupos = [{id:'intro', title:'Antes de começar', slides:introducao}, ...exercicios.map(e => ({id:e.id, title:e.title, slides:slides(e)}))];
let atual = null;

function navegar(direcao) {
  if (!atual) return;
  let {grupo, pagina} = atual;
  pagina += direcao;
  if (pagina >= grupos[grupo].slides.length) { grupo++; pagina = 0; }
  if (pagina < 0) { grupo--; pagina = grupos[grupo]?.slides.length - 1; }
  location.hash = grupos[grupo] ? `#/${grupos[grupo].id}/${pagina + 1}` : '#/';
}

function render() {
  const match = location.hash.match(/^#\/(intro|0[1-7])(?:\/([1-9][0-9]*))?$/);
  const home = document.getElementById('home');
  const deck = document.getElementById('deck');
  if (!match) {
    atual = null;
    home.hidden = false;
    deck.hidden = true;
    document.title = 'GitHub Actions · Do primeiro workflow ao deploy';
    window.scrollTo(0, 0);
    return;
  }
  const grupo = grupos.findIndex(g => g.id === match[1]);
  const pagina = Math.min(Number(match[2] || 1) - 1, grupos[grupo].slides.length - 1);
  atual = {grupo, pagina};
  const slide = grupos[grupo].slides[pagina];
  home.hidden = true;
  deck.hidden = false;
  document.title = `${grupos[grupo].title} · GitHub Actions`;
  document.getElementById('deck-label').textContent = grupos[grupo].title;
  document.getElementById('counter').textContent = `${pagina + 1} / ${grupos[grupo].slides.length}`;
  document.getElementById('progress-bar').style.width = `${100 * (pagina + 1) / grupos[grupo].slides.length}%`;
  const article = document.getElementById('slide');
  article.innerHTML = `<p class="eyebrow">${slide.label}</p><h2>${slide.title}</h2>${slide.body}`;
  document.getElementById('previous').disabled = grupo === 0 && pagina === 0;
  document.getElementById('next').textContent = grupo === grupos.length - 1 && pagina === grupos[grupo].slides.length - 1 ? 'Concluir →' : 'Próximo →';
  article.focus({preventScroll:true});
  window.scrollTo(0, 0);
}

document.getElementById('previous').addEventListener('click', () => navegar(-1));
document.getElementById('next').addEventListener('click', () => navegar(1));
document.addEventListener('keydown', event => {
  if (!atual || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || /INPUT|TEXTAREA|SELECT/.test(event.target.tagName) || event.target.isContentEditable) return;
  if (event.key === 'ArrowRight') { event.preventDefault(); navegar(1); }
  if (event.key === 'ArrowLeft') { event.preventDefault(); if (!(atual.grupo === 0 && atual.pagina === 0)) navegar(-1); }
  if (event.key === 'Escape') { event.preventDefault(); location.hash = '#/'; }
});
window.addEventListener('hashchange', render);
render();
