# Module slides with commands and numbered exercises

**Session ID:** ses_f05f7400affeOznDfVP0IsrE3p
**Created:** 10/1/2026, 8:34:32 PM
**Updated:** 10/1/2026, 8:43:29 PM

---

## User

follow the same slide structure as in https://github.com/fsilva-alt/devops-git and https://github.com/fsilva-alt/devops-docker . each module has up to 3 slide with explanations of the concepts, one slide with with a list of usefull commands and links, and a last slide with the exercise. the last slide needs to have numbered steps for the exercicise completion

---

## Assistant (Build · GPT-6 Astra · 9.4s)

I’ll check the slide structure in both repositories, then update this project’s modules to match: up to three concept slides, one commands-and-links slide, and a final exercise slide with numbered steps.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Inspect project instructions, current slides, and the two reference repositories.",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Restructure each module into concept slides, commands and links, and a numbered exercise slide.",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Validate the updated slides and review the changes.",
      "status": "pending",
      "priority": "medium"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Inspect project instructions, current slides, and the two reference repositories.",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Restructure each module into concept slides, commands and links, and a numbered exercise slide.",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Validate the updated slides and review the changes.",
    "status": "pending",
    "priority": "medium"
  }
]
```

---

## Assistant (Build · GPT-6 Astra · 30.4s)

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions</path>
<type>directory</type>
<entries>
.devcontainer/
.git/
.gitignore
docs/
exercises/
install.sh
LICENSE
README.md
scripts/
templates/
tests/

(11 entries)
</entries>
```

**Tool: bash**

**Input:**
```json
{
  "command": "git status --short && git remote -v"
}
```

**Output:**
```
origin	https://github.com/fsilva-alt/devops-ghactions.git (fetch)
origin	https://github.com/fsilva-alt/devops-ghactions.git (push)

```

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/AGENTS.md",
  "path": "/home/lse/projects"
}
```

**Error:**
```
The user rejected permission to use this specific tool call.
```

**Tool: bash**

**Input:**
```json
{
  "command": "gh api repos/fsilva-alt/devops-git/contents"
}
```

**Output:**
```
zsh:1: command not found: gh

```

**Tool: bash**

**Input:**
```json
{
  "command": "gh api repos/fsilva-alt/devops-docker/contents"
}
```

**Output:**
```
zsh:1: command not found: gh

```

---

## User

continue

---

## Assistant (Build · GPT-6 Astra · 10.7s)

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/AGENTS.md"
}
```

**Output:**
```
No files found
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/docs"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/docs</path>
<type>directory</type>
<entries>
.nojekyll
ementa.md
gabarito.md
guia-do-aluno.md
guia-do-professor.md
index.html
solucoes/
style.css

(8 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/README.md"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/README.md</path>
<type>file</type>
<content>
1: # Curso de GitHub Actions no GitHub Codespaces
2: 
3: Curso **introdutório, em pt-BR, com exatamente 7 exercícios e 3 horas de aula**. Você vai automatizar testes e publicar um pequeno site de cardápio. O código Python já está pronto: o foco é entender e escrever workflows.
4: 
5: **O GitHub Codespaces é obrigatório nos 7 exercícios.** É nele que você edita os arquivos e executa comandos. Os workflows rodam em outras máquinas: os runners do GitHub Actions.
6: 
7: Comece por [Antes da aula](#antes-da-aula) e depois siga a [Sequência da aula](#sequência-da-aula). O [guia do aluno](docs/guia-do-aluno.md) explica como acompanhar os exercícios e resolver problemas comuns. Consulte também a [ementa](docs/ementa.md), a [apresentação](https://fsilva-alt.github.io/devops-ghactions/), o [gabarito](docs/gabarito.md) e o [guia do professor](docs/guia-do-professor.md).
8: 
9: ## O que você vai aprender
10: 
11: - Diferenciar evento, workflow, job, step, action e runner.
12: - Ler YAML e escolher entre `run` e `uses`.
13: - Executar testes a cada push e acompanhar checks de um pull request.
14: - Encontrar uma falha nos logs e corrigir sua causa.
15: - Usar variáveis, contextos e um segredo de demonstração.
16: - Ordenar jobs, guardar o resultado do build e publicar no GitHub Pages.
17: 
18: ### Pré-requisitos
19: 
20: Conta pessoal no GitHub com acesso ao Codespaces, navegador e conexão à internet. Você precisa conhecer o básico de arquivos, terminal, commit, branch e push; os comandos de publicação são fornecidos. Não é necessário saber programar em Python nem ter experiência em CI/CD.
21: 
22: ## Antes da aula
23: 
24: Faça a preparação pelo menos um dia antes.
25: 
26: 1. Entre na sua conta no [GitHub](https://github.com).
27: 2. Crie um Codespace em branco: em [github.com/codespaces](https://github.com/codespaces), escolha o modelo **Blank**. Use esse mesmo Codespace durante toda a aula.
28: 3. No VS Code que abrir no navegador, acesse **Terminal → New Terminal**. Cole o comando abaixo e pressione Enter:
29: 
30:    ```bash
31:    sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"
32:    ```
33: 
34:    O instalador baixa o material para `~/devops-ghactions`, instala o verificador de YAML e prepara os 7 laboratórios em `~/labs`. Também cria um atalho `labs` na pasta em que foi executado, para acessar os exercícios pelo explorador do VS Code, e disponibiliza os comandos `check.sh`, `reset.sh` e `setup.sh`. O símbolo `~` representa sua pasta pessoal no Codespace.
35: 
36:    Autorize o GitHub CLI com a conta que usará na aula. O instalador pede o escopo `workflow`, necessário para enviar arquivos de workflows. Se não abrir uma janela, siga o código exibido em [github.com/login/device](https://github.com/login/device). Um login salvo válido é reutilizado. Aguarde a mensagem **Curso de GitHub Actions instalado com sucesso!**.
37: 
38:    Se o login for interrompido, execute o instalador novamente. Os laboratórios serão preservados. A autenticação segue o mesmo procedimento do curso de Git: login pelo navegador, reutilização das credenciais salvas e configuração do Git com `gh auth setup-git`.
39: 
40: 4. Abra **um terminal novo**, ou execute `source ~/.bashrc` no bash / `source ~/.zshrc` no zsh, para carregar os comandos e a autenticação. Execute os comandos abaixo, um por vez:
41: 
42:    ```bash
43:    echo "$CODESPACES"
44:    gh auth status --hostname github.com
45:    git config user.name
46:    git config user.email
47:    check.sh 01
48:    ```
49: 
50:    O primeiro comando deve mostrar `true`. É esperado que `check.sh 01` peça o workflow que você ainda vai criar. Se o nome ou e-mail estiver vazio, configure sua autoria com seus próprios dados:
51: 
52:    ```bash
53:    git config --global user.name "Seu nome"
54:    git config --global user.email "seu-email-da-conta-github"
55:    ```
56: 
57: 5. Pare o Codespace em [github.com/codespaces](https://github.com/codespaces): **⋯ → Stop codespace**. Reabra o mesmo ambiente no dia da aula. Codespaces e Actions têm franquias e cobrança separadas; confira sua disponibilidade de Codespaces antes do evento. A prática usa repositórios públicos e runners Linux padrão.
58: 
59: ## Sequência da aula
60: 
61: Os tempos incluem explicação, demonstração, prática e conferência.
62: 
63: | # | Exercício | Conceito novo | Tempo |
64: |---|---|---|---:|
65: | [01](https://fsilva-alt.github.io/devops-ghactions/#exercicio-01) | Primeiro workflow | YAML, evento manual, job, runner e step | 15 min |
66: | [02](https://fsilva-alt.github.io/devops-ghactions/#exercicio-02) | Testes no push | `push`, `checkout`, `setup-python`, `run` × `uses` | 25 min |
67: | [03](https://fsilva-alt.github.io/devops-ghactions/#exercicio-03) | Checks no pull request | `pull_request`, logs, falhar e corrigir | 25 min |
68: | [04](https://fsilva-alt.github.io/devops-ghactions/#exercicio-04) | Variáveis e contextos | `env`, `inputs`, `github`, `vars`, `secrets` | 20 min |
69: | [05](https://fsilva-alt.github.io/devops-ghactions/#exercicio-05) | Jobs e dependências | `needs`, isolamento entre runners, build | 20 min |
70: | [06](https://fsilva-alt.github.io/devops-ghactions/#exercicio-06) | Artefatos do build | Salvar e baixar arquivos de uma execução | 20 min |
71: | [07](https://fsilva-alt.github.io/devops-ghactions/#exercicio-07) | Deploy no Pages | Publicação guiada, `permissions`, `environment` | 30 min |
72: 
73: Prática e explicações: **155 minutos**. Abertura: 10; intervalo: 10; encerramento: 5. Total: **180 minutos**.
74: 
75: ## Como o ambiente funciona
76: 
77: ### Primeiros passos no terminal e no editor
78: 
79: - **Executar um comando:** copie a linha para o terminal e pressione Enter. Aguarde o término antes de executar a próxima.
80: - **Editar um arquivo:** use `code nome-do-arquivo` na pasta do laboratório. Blocos de YAML vão no arquivo indicado, não no terminal. Salve com **Ctrl+S**, ou **Cmd+S** no Mac.
81: - **Mudar de pasta:** use `cd caminho`. `pwd` mostra a pasta atual, e `ls` lista os arquivos.
82: - **Usar os exemplos:** substitua `NN` pelo número do exercício. Por exemplo, `check.sh NN` vira `check.sh 02` no exercício 02.
83: 
84: ### Onde ficam os arquivos
85: 
86: Cada exercício tem seu próprio repositório local em `~/labs/NN-nome` e um ponto de partida pronto. Assim você consegue acompanhar o próximo mesmo que não tenha terminado o anterior. Todos usam o mesmo projeto de cardápio. O exercício 04 é uma demonstração isolada de configuração; os seguintes retomam o projeto de testes e build.
87: 
88: | Local | Conteúdo |
89: |---|---|
90: | `~/devops-ghactions/` (`$CURSO_DIR`) | Material do curso: slides, scripts e documentos |
91: | [Site do curso](https://fsilva-alt.github.io/devops-ghactions/) | Slides HTML com os enunciados dos 7 exercícios |
92: | `~/devops-ghactions/docs/index.html` | Cópia local dos slides |
93: | `~/labs/NN-nome/` | Arquivos que você modifica e publica |
94: | `labs`, no explorador do VS Code | Atalho para `~/labs`, criado pelo instalador |
95: | `.github/workflows/ci.yml`, dentro de cada lab | Workflow do exercício |
96: | `$CURSO_DIR/docs/solucoes/` | Workflows completos para consulta depois da tentativa |
97: 
98: O instalador define `CURSO_DIR`, `LABS_DIR` e o `PATH` nos novos terminais bash/zsh. No Codespaces, remove `GH_TOKEN` e `GITHUB_TOKEN` desses terminais para que o `gh` use o login salvo, com acesso aos repositórios da prática.
99: 
100: | Comando | Função |
101: |---|---|
102: | `setup.sh` | Cria apenas laboratórios ausentes |
103: | `check.sh NN` | Analisa o YAML e alguns requisitos do exercício, sem acessar o GitHub |
104: | `reset.sh NN` | **Apaga o trabalho local desse laboratório** e recria o estado inicial |
105: 
106: Dentro de uma pasta de laboratório, `check.sh` e `reset.sh` descobrem o número automaticamente, inclusive pelo atalho `labs`. Após um reset, entre novamente na pasta com o `cd` do enunciado. Os enunciados ficam nos [slides HTML](https://fsilva-alt.github.io/devops-ghactions/); selecione o exercício no índice.
107: 
108: Você pode executar o instalador novamente: ele atualiza o material do curso e cria apenas os laboratórios ausentes. Para atualizar o ponto de partida de um laboratório existente, guarde o trabalho que deseja manter e use `reset.sh NN`. Os caminhos podem ser personalizados com `CURSO_DIR` e `LABS_DIR`; `CURSO_REPO` e `CURSO_RAMO` permitem usar outra origem ou branch do material.
109: 
110: **Um check local aprovado não comprova a execução na nuvem.** Conclua também a entrega indicada em cada enunciado: execução, logs, PR, artefato ou site publicado. O verificador não é um validador completo da linguagem do Actions.
111: 
112: ### Publicar cada laboratório
113: 
114: Cada exercício usa um repositório público separado, `actions-01` a `actions-07`, na sua conta. Não crie outro Codespace: continue no Codespace Blank preparado antes da aula. Na pasta do laboratório, depois de salvar e verificar o workflow:
115: 
116: ```bash
117: git add .github/workflows
118: git commit -m "Configura workflow do exercício"
119: # Troque NN pelo número do exercício, por exemplo actions-02.
120: gh repo create actions-NN --public --source=. --remote=origin --push
121: gh browse --actions
122: ```
123: 
124: O comando `gh repo create` é usado **uma vez por laboratório**. Para alterações seguintes: `git add`, `git commit` e `git push`. Os nomes `actions-NN` são marcadores nos exemplos genéricos; cada exercício traz o nome pronto para copiar. Se um nome já existir na sua conta, escolha outro, como `actions-02-turma-b`.
125: 
126: Para o botão **Run workflow** aparecer, o workflow com `workflow_dispatch` precisa estar na branch padrão (`main`). Ao abrir um repositório de exercício, confirme que a branch padrão é `main`.
127: 
128: ### Retomar depois de resetar
129: 
130: `reset.sh` remove também a configuração de `origin`, mas não altera o GitHub. Para começar uma nova tentativa do zero, publique em **um novo nome**, por exemplo `gh repo create actions-02-tentativa-2 --public --source=. --remote=origin --push`. Isso evita misturar o histórico inicial com a tentativa já publicada. Para recuperar o trabalho publicado, clone aquele repositório em outra pasta no mesmo Codespace.
131: 
132: ### Se o push falhar por permissão
133: 
134: Confira `git remote -v` e `gh auth status --hostname github.com`. Para um login antigo sem escopo de workflow, no terminal do Codespace:
135: 
136: ```bash
137: unset GH_TOKEN GITHUB_TOKEN
138: gh auth refresh --hostname github.com --scopes workflow
139: gh auth setup-git --hostname github.com
140: git push -u origin main
141: ```
142: 
143: Se a conta estiver incorreta, use `gh auth login --hostname github.com --git-protocol https --web --scopes workflow`. O `GITHUB_TOKEN` **dentro de um workflow** é outra credencial, fornecida automaticamente pelo Actions para aquela execução.
144: 
145: ## Ao final
146: 
147: Compartilhe os links pedidos nos 7 exercícios. Guarde a URL do site do exercício 07 e o PR com falha e correção do exercício 03. Faça push de tudo que deseja guardar e pare o Codespace; excluí-lo libera o armazenamento, mas apaga arquivos locais não publicados.
148: 
149: ## Desenvolvimento do material
150: 
151: Os geradores ficam em `scripts/labs.sh`, o verificador em `scripts/checks.py`, e o projeto em `templates/projeto/`. Os YAMLs do [gabarito](docs/gabarito.md) também são usados como pontos de partida e nos testes.
152: 
153: A configuração em `.devcontainer/` é destinada à manutenção deste repositório. O aluno usa o modelo Blank e o instalador remoto, sem precisar clonar o curso manualmente.
154: 
155: Em testes locais, `CURSO_AUTH_GITHUB=0` pula a autenticação, dispensa o `gh` e não habilita a remoção dos tokens nos terminais. Na instalação normal, o GitHub CLI é obrigatório e o primeiro login precisa de um terminal interativo. Fora do Codespaces, as variáveis de autenticação são mantidas.
156: 
157: A apresentação está em `docs/index.html`, com estilos em `docs/style.css`. Abra o HTML diretamente no navegador para revisar as aulas; a navegação e as perguntas expansíveis funcionam sem JavaScript. Para conferir apenas seu conteúdo e links, execute `python3 tests/apresentacao.py`.
158: 
159: ```bash
160: bash tests/rodar.sh          # testes em ambiente temporário, sem conta GitHub
161: bash tests/rodar.sh --docker # mesma suíte em Ubuntu limpo, exige Docker
162: ```
163: 
164: A suíte confere instalação via `curl` e `sh -c` em um workspace vazio, atualização do material, preservação dos labs e dos arquivos do workspace, atalho `labs`, autenticação simulada, YAMLs iniciais e resolvidos, erros comuns, links locais, os 7 enunciados, testes do projeto e build. `CURSO_MODO_TESTE=1` libera os scripts fora do Codespaces apenas para manutenção automatizada; a experiência do aluno continua obrigatoriamente no Codespaces. O modo de teste usa uma origem Git local e não cria repositórios no GitHub nem publica sites.
165: 
166: ## Licença
167: 
168: [MIT](LICENSE).

(End of file - total 168 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/tests"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/tests</path>
<type>directory</type>
<entries>
apresentacao.py
Dockerfile
rodar.sh
solucoes.sh
verificar.py

(5 entries)
</entries>
```

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://github.com/fsilva-alt/devops-git",
  "format": "markdown"
}
```

**Output:**
```
                                                                                                                 GitHub - fsilva-alt/devops-git: devops-git · GitHub                                             

[Skip to content](#start-of-content)     

    

            

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Ffsilva-alt%2Fdevops-git)

Appearance settings

-   Platform
    
    -   AI CODE CREATION
        
        -   [GitHub CopilotWrite better code with AI](https://github.com/features/copilot)
        -   [GitHub Copilot appDirect agents from issue to merge](https://github.com/features/ai/github-app)
        -   [MCP RegistryIntegrate external tools](https://github.com/mcp)
        
    -   DEVELOPER WORKFLOWS
        
        -   [ActionsAutomate any workflow](https://github.com/features/actions)
        -   [CodespacesInstant dev environments](https://github.com/features/codespaces)
        -   [IssuesPlan and track work](https://github.com/features/issues)
        -   [Code ReviewManage code changes](https://github.com/features/code-review)
        -   [Code QualityEnforce quality at merge](https://github.com/features/code-quality)
        
    -   APPLICATION SECURITY
        
        -   [GitHub Advanced SecurityFind and fix vulnerabilities](https://github.com/security/advanced-security)
        -   [Code securitySecure your code as you build](https://github.com/security/advanced-security/code-security)
        -   [Secret protectionStop leaks before they start](https://github.com/security/advanced-security/secret-protection)
        
    -   EXPLORE
        
        -   [Why GitHub](https://github.com/why-github)
        -   [Documentation](https://docs.github.com)
        -   [Blog](https://github.blog)
        -   [Changelog](https://github.blog/changelog)
        -   [Marketplace](https://github.com/marketplace)
        
    
    [View all features](https://github.com/features)
    
-   Solutions
    
    -   BY COMPANY SIZE
        
        -   [Enterprises](https://github.com/enterprise)
        -   [Small and medium teams](https://github.com/team)
        -   [Startups](https://github.com/enterprise/startups)
        -   [Nonprofits](https://github.com/solutions/industry/nonprofits)
        
    -   BY USE CASE
        
        -   [App Modernization](https://github.com/solutions/use-case/app-modernization)
        -   [DevSecOps](https://github.com/solutions/use-case/devsecops)
        -   [DevOps](https://github.com/solutions/use-case/devops)
        -   [CI/CD](https://github.com/solutions/use-case/ci-cd)
        -   [View all use cases](https://github.com/solutions/use-case)
        
    -   BY INDUSTRY
        
        -   [Healthcare](https://github.com/solutions/industry/healthcare)
        -   [Financial services](https://github.com/solutions/industry/financial-services)
        -   [Manufacturing](https://github.com/solutions/industry/manufacturing)
        -   [Government](https://github.com/solutions/industry/government)
        -   [View all industries](https://github.com/solutions/industry)
        
    
    [View all solutions](https://github.com/solutions)
    
-   Resources
    
    -   EXPLORE BY TOPIC
        
        -   [AI](https://github.com/resources/articles?topic=ai)
        -   [Software Development](https://github.com/resources/articles?topic=software-development)
        -   [DevOps](https://github.com/resources/articles?topic=devops)
        -   [Security](https://github.com/resources/articles?topic=security)
        -   [View all topics](https://github.com/resources/articles)
        
    -   EXPLORE BY TYPE
        
        -   [Customer stories](https://github.com/customer-stories)
        -   [Events & webinars](https://github.com/resources/events)
        -   [Ebooks & reports](https://github.com/resources/whitepapers)
        -   [Business insights](https://github.com/solutions/executive-insights)
        -   [GitHub Skills](https://skills.github.com)
        
    -   SUPPORT & SERVICES
        
        -   [Documentation](https://docs.github.com)
        -   [Customer support](https://support.github.com)
        -   [Community forum](https://github.com/orgs/community/discussions)
        -   [Trust center](https://github.com/trust-center)
        -   [Partners](https://github.com/partners)
        
    
    [View all resources](https://github.com/resources)
    
-   Open Source
    
    -   COMMUNITY
        
        -   [GitHub SponsorsFund open source developers](https://github.com/open-source/sponsors)
        
    -   PROGRAMS
        
        -   [Security Lab](https://securitylab.github.com)
        -   [Maintainer Community](https://maintainers.github.com)
        -   [GitHub Stars](https://stars.github.com)
        -   [Archive Program](https://archiveprogram.github.com)
        
    -   REPOSITORIES
        
        -   [Topics](https://github.com/topics)
        -   [Trending](https://github.com/trending)
        -   [Collections](https://github.com/collections)
        
    
-   Enterprise
    
    -   ENTERPRISE SOLUTIONS
        
        -   [Enterprise platformAI-powered developer platform](https://github.com/enterprise)
        
    -   AVAILABLE ADD-ONS
        
        -   [GitHub Advanced SecurityEnterprise-grade security features](https://github.com/security/advanced-security)
        -   [Copilot for BusinessEnterprise-grade AI features](https://github.com/features/copilot/copilot-business)
        -   [Premium SupportEnterprise-grade 24/7 support](https://github.com/enterprise/premium-support)
        
    
-   [Pricing](https://github.com/pricing)

Search/

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Ffsilva-alt%2Fdevops-git)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=fsilva-alt%2Fdevops-git)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

[fsilva-alt](/fsilva-alt) / **[devops-git](/fsilva-alt/devops-git)** Public

-   [Notifications](/login?return_to=%2Ffsilva-alt%2Fdevops-git) You must be signed in to change notification settings
-   [Fork 0](/login?return_to=%2Ffsilva-alt%2Fdevops-git)
-   [Star 0](/login?return_to=%2Ffsilva-alt%2Fdevops-git)
    

-   [Code](/fsilva-alt/devops-git)
-   [Issues 0](/fsilva-alt/devops-git/issues)
-   [Pull requests 0](/fsilva-alt/devops-git/pulls)
-   [Actions](/fsilva-alt/devops-git/actions)
-   [Projects](/fsilva-alt/devops-git/projects)
-   [Security and quality 0](/fsilva-alt/devops-git/security)
-   [Insights](/fsilva-alt/devops-git/pulse)

Additional navigation options

-   [Code](/fsilva-alt/devops-git)
-   [Issues](/fsilva-alt/devops-git/issues)
-   [Pull requests](/fsilva-alt/devops-git/pulls)
-   [Actions](/fsilva-alt/devops-git/actions)
-   [Projects](/fsilva-alt/devops-git/projects)
-   [Security and quality](/fsilva-alt/devops-git/security)
-   [Insights](/fsilva-alt/devops-git/pulse)

 [](/fsilva-alt/devops-git)

main

[Branches](/fsilva-alt/devops-git/branches)[Tags](/fsilva-alt/devops-git/tags)

[](/fsilva-alt/devops-git/branches)[](/fsilva-alt/devops-git/tags)

Go to file

Code

Open more actions menu

## Latest commit

## History

[7 Commits](/fsilva-alt/devops-git/commits/main/)

[](/fsilva-alt/devops-git/commits/main/)7 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[docs](/fsilva-alt/devops-git/tree/main/docs "docs")

[docs](/fsilva-alt/devops-git/tree/main/docs "docs")

[exercises](/fsilva-alt/devops-git/tree/main/exercises "exercises")

[exercises](/fsilva-alt/devops-git/tree/main/exercises "exercises")

[scripts](/fsilva-alt/devops-git/tree/main/scripts "scripts")

[scripts](/fsilva-alt/devops-git/tree/main/scripts "scripts")

[tests](/fsilva-alt/devops-git/tree/main/tests "tests")

[tests](/fsilva-alt/devops-git/tree/main/tests "tests")

[LICENSE](/fsilva-alt/devops-git/blob/main/LICENSE "LICENSE")

[LICENSE](/fsilva-alt/devops-git/blob/main/LICENSE "LICENSE")

[README.md](/fsilva-alt/devops-git/blob/main/README.md "README.md")

[README.md](/fsilva-alt/devops-git/blob/main/README.md "README.md")

[install.sh](/fsilva-alt/devops-git/blob/main/install.sh "install.sh")

[install.sh](/fsilva-alt/devops-git/blob/main/install.sh "install.sh")

View all files

## Repository files navigation

-   [README](#)
-   [MIT license](#)

More items

# Curso de Git no GitHub Codespaces

[](#curso-de-git-no-github-codespaces)

Curso de Git para iniciantes, com 3 horas de aula ao vivo pelo Zoom e prática no Codespace individual de cada pessoa. Você faz os exercícios pelo navegador, sem instalar nada no computador.

> **Para alunos:** comece pela seção [Antes da aula](#antes-da-aula). No dia do curso, siga a [Sequência da aula](#sequ%C3%AAncia-da-aula). **Para professores e monitores:** consulte o [guia do professor](/fsilva-alt/devops-git/blob/main/docs/guia-do-professor.md).

## O que você vai aprender

[](#o-que-você-vai-aprender)

-   as três áreas do Git: diretório de trabalho, staging area e repositório;
-   fazer commits pequenos, com mensagens claras;
-   investigar o histórico: quem mudou o quê, quando e por quê;
-   desfazer mudanças com segurança, antes e depois do commit;
-   trabalhar com branches, fazer merge e resolver conflitos;
-   sincronizar com um remoto e abrir um pull request no GitHub;
-   fazer um fork, cloná-lo e contribuir com o projeto original por pull request.

A ementa completa, com cronograma, está em [docs/ementa.md](/fsilva-alt/devops-git/blob/main/docs/ementa.md).

## Antes da aula

[](#antes-da-aula)

Prepare o ambiente **pelo menos um dia antes** para ter tempo de resolver eventuais problemas de acesso.

1.  Tenha uma conta no [GitHub](https://github.com) e esteja logado.
    
2.  Crie um Codespace em branco: acesse [github.com/codespaces](https://github.com/codespaces) e clique em **New codespace** com o template **Blank**, ou vá direto em [codespaces/new](https://github.com/codespaces/new). A primeira criação leva de 1 a 3 minutos.
    
3.  Quando o VS Code abrir no navegador, cole no terminal e pressione Enter:
    
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-git/main/install.sh)"
    
    O instalador baixa o curso para `~/devops-git`, monta os laboratórios em `~/labs` e prepara a autenticação para publicar nos desafios 14–16. Se ainda não houver um login válido salvo, ele mostra um código e abre o navegador: autorize o **GitHub CLI com a conta que usará no curso**. Se o navegador não abrir, acesse `https://github.com/login/device` e informe o código exibido. Ao terminar, aparece **"Curso de Git instalado com sucesso!"**.
    
    Se o login for interrompido, rode o instalador novamente; ele preserva seus laboratórios e reutiliza um login salvo válido.
    
4.  Abra um terminal novo (ou rode `source ~/.bashrc` no bash / `source ~/.zshrc` no zsh) para carregar os comandos e a autenticação. No Codespaces, o bloco do curso nesses arquivos remove `GH_TOKEN` e `GITHUB_TOKEN` do terminal, permitindo usar o login salvo em vez do token automático limitado. Teste:
    
    check.sh 00
    
    O comando pode avisar que faltam seu nome e e-mail. Nesse caso, a verificação está funcionando; você vai configurar esses dados na aula.
    
5.  Pare o Codespace para poupar as horas de uso da sua franquia gratuita: em [github.com/codespaces](https://github.com/codespaces), **⋯ → Stop codespace**. No dia da aula, abra-o novamente; os arquivos continuam salvos.
    

## Como o ambiente funciona

[](#como-o-ambiente-funciona)

Caminho

Conteúdo

`~/devops-git/`

Este repositório: enunciados, scripts e documentos

`~/devops-git/exercises/NN-nome/README.md`

O enunciado de cada desafio

`~/labs/NN-nome/`

Um repositório Git independente para cada desafio de 1 a 14

`~/labs/16-contribua-com-um-fork/`

Clone do seu fork, criado por você no desafio 16

Comandos disponíveis no terminal:

Comando

Função

`check.sh NN`

Verifica os desafios 00 a 15 e responde ✅ ou uma dica

`reset.sh NN`

Recria um laboratório de 01 a 14 do zero e apaga o trabalho feito **apenas nesse laboratório**

`colega.sh NN`

Simula um colega publicando no remoto (desafios 12 e 13)

`setup.sh`

Gera os laboratórios que ainda não existem; o instalador já rodou isso

Dentro da pasta de um laboratório gerado pelo instalador, `check.sh` e `reset.sh` funcionam sem o número. O desafio 16 tem verificação manual pelo PR no GitHub. Para ler um enunciado no editor: `code ~/devops-git/exercises/05-detetive-do-historico/README.md`.

## Sequência da aula

[](#sequência-da-aula)

#

Desafio

Tema

[0](/fsilva-alt/devops-git/blob/main/exercises/00-configure-sua-identidade/README.md)

Configure sua identidade

`git config`

[1](/fsilva-alt/devops-git/blob/main/exercises/01-meu-primeiro-repositorio/README.md)

Meu primeiro repositório

`init`, `status`, `add`, `commit`

[2](/fsilva-alt/devops-git/blob/main/exercises/02-registrando-mudancas/README.md)

Registrando mudanças

`diff`, `diff --staged`, `log`

[3](/fsilva-alt/devops-git/blob/main/exercises/03-commit-cirurgico/README.md)

Commit cirúrgico

staging seletivo, `add -p`

[4](/fsilva-alt/devops-git/blob/main/exercises/04-ignorando-o-que-nao-importa/README.md)

Ignorando o que não importa ⏱

`.gitignore`, `check-ignore`, `rm --cached`

[5](/fsilva-alt/devops-git/blob/main/exercises/05-detetive-do-historico/README.md)

Detetive do histórico

`log`, `show`, `blame`, `log -S`

[6](/fsilva-alt/devops-git/blob/main/exercises/06-desfazendo-antes-do-commit/README.md)

Desfazendo antes do commit

`restore`, `restore --staged`

[7](/fsilva-alt/devops-git/blob/main/exercises/07-desfazendo-depois-do-commit/README.md)

Desfazendo depois do commit

`commit --amend`, `revert`

[8](/fsilva-alt/devops-git/blob/main/exercises/08-branch-de-funcionalidade/README.md)

Branch de funcionalidade

`switch -c`, merge fast-forward

[9](/fsilva-alt/devops-git/blob/main/exercises/09-caminhos-que-divergem/README.md)

Caminhos que divergem

merge de três vias, `branch -d`

[10](/fsilva-alt/devops-git/blob/main/exercises/10-guardando-para-depois/README.md)

Guardando para depois ⏱

`stash`

[11](/fsilva-alt/devops-git/blob/main/exercises/11-resolva-o-conflito/README.md)

Resolva o conflito

marcadores, `merge --abort`

[12](/fsilva-alt/devops-git/blob/main/exercises/12-o-colega-invisivel/README.md)

O colega invisível

`push` rejeitado, `pull`

[13](/fsilva-alt/devops-git/blob/main/exercises/13-conflito-com-o-colega/README.md)

Conflito com o colega

`fetch`, `main..origin/main`

[14](/fsilva-alt/devops-git/blob/main/exercises/14-publique-no-github/README.md)

Publique no GitHub

`remote add`, `push -u` para o GitHub

[15](/fsilva-alt/devops-git/blob/main/exercises/15-seu-primeiro-pull-request/README.md)

Seu primeiro pull request ⏱

branch, PR, merge na web, `pull`

[16](/fsilva-alt/devops-git/blob/main/exercises/16-contribua-com-um-fork/README.md)

Contribua com um fork

fork, `clone`, `origin`/`upstream`, PR para o projeto original

⏱ indica os desafios que podem ficar como tarefa para depois da aula, caso haja atraso.

## Ao final da aula

[](#ao-final-da-aula)

1.  Confira que seu trabalho está publicado: `check.sh 14` e `check.sh 15`. No desafio 16, compartilhe o link do PR em `fsilva-alt/receitas-de-pizza` com o professor ou monitor.
2.  **Pare ou exclua o Codespace.** Um Codespace parado continua ocupando armazenamento da franquia gratuita; um excluído não. Os laboratórios são descartáveis: o instalador recria tudo em outro Codespace a qualquer momento.
3.  O repositório `livro-de-receitas` que você publicou no desafio 14 continua na sua conta do GitHub, com o `aprendizados.md`, para revisar depois.

## Para desenvolver o curso

[](#para-desenvolver-o-curso)

Os laboratórios são gerados por `scripts/labs.sh` e verificados por `scripts/checks.sh`. A suíte de testes em `tests/` roda em um container Ubuntu limpo e precisa de Docker. Ela executa o `install.sh` como um aluno faria, simula o GitHub CLI para testar login, reutilização de credenciais e novos terminais sem acessar contas reais, e confere, para os desafios 0 a 15, se `check.sh` reprova o estado vazio, dá a dica correspondente a cada resposta errada e aprova a solução do gabarito. O desafio 16 é conferido manualmente no GitHub. Para rodar:

tests/rodar.sh

Em instalações automatizadas para testes locais, `CURSO_AUTH_GITHUB=0` pula a autenticação e dispensa o `gh`. Na instalação normal, o GitHub CLI é obrigatório (já vem no Codespaces); um primeiro login precisa de terminal interativo.

## Licença

[](#licença)

[MIT](/fsilva-alt/devops-git/blob/main/LICENSE).

## About

devops-git

[fsilva-alt.github.io/devops-git](https://fsilva-alt.github.io/devops-git)

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/fsilva-alt/devops-git/activity)

### Stars

**0** stars

### Watchers

**0** watching

### Forks

[**0** forks](/fsilva-alt/devops-git/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Ffsilva-alt%2Fdevops-git&report=fsilva-alt+%28user%29)

## Releases

## Packages

## Contributors

## Languages

## Footer

[](https://github.com)© 2026 GitHub, Inc.

### Footer navigation

-   [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
-   [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
-   [Security](https://github.com/security)
-   [Status](https://www.githubstatus.com/)
-   [Community](https://github.community/)
-   [Docs](https://docs.github.com/)
-   [Contact](https://support.github.com?tags=dotcom-footer)
-   Manage cookies
-   Do not share my personal information

You can’t perform that action at this time.
```

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://github.com/fsilva-alt/devops-docker",
  "format": "markdown"
}
```

**Output:**
```
                                                                                                                 GitHub - fsilva-alt/devops-docker: devops-docker · GitHub                                             

[Skip to content](#start-of-content)     

    

            

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Ffsilva-alt%2Fdevops-docker)

Appearance settings

-   Platform
    
    -   AI CODE CREATION
        
        -   [GitHub CopilotWrite better code with AI](https://github.com/features/copilot)
        -   [GitHub Copilot appDirect agents from issue to merge](https://github.com/features/ai/github-app)
        -   [MCP RegistryIntegrate external tools](https://github.com/mcp)
        
    -   DEVELOPER WORKFLOWS
        
        -   [ActionsAutomate any workflow](https://github.com/features/actions)
        -   [CodespacesInstant dev environments](https://github.com/features/codespaces)
        -   [IssuesPlan and track work](https://github.com/features/issues)
        -   [Code ReviewManage code changes](https://github.com/features/code-review)
        -   [Code QualityEnforce quality at merge](https://github.com/features/code-quality)
        
    -   APPLICATION SECURITY
        
        -   [GitHub Advanced SecurityFind and fix vulnerabilities](https://github.com/security/advanced-security)
        -   [Code securitySecure your code as you build](https://github.com/security/advanced-security/code-security)
        -   [Secret protectionStop leaks before they start](https://github.com/security/advanced-security/secret-protection)
        
    -   EXPLORE
        
        -   [Why GitHub](https://github.com/why-github)
        -   [Documentation](https://docs.github.com)
        -   [Blog](https://github.blog)
        -   [Changelog](https://github.blog/changelog)
        -   [Marketplace](https://github.com/marketplace)
        
    
    [View all features](https://github.com/features)
    
-   Solutions
    
    -   BY COMPANY SIZE
        
        -   [Enterprises](https://github.com/enterprise)
        -   [Small and medium teams](https://github.com/team)
        -   [Startups](https://github.com/enterprise/startups)
        -   [Nonprofits](https://github.com/solutions/industry/nonprofits)
        
    -   BY USE CASE
        
        -   [App Modernization](https://github.com/solutions/use-case/app-modernization)
        -   [DevSecOps](https://github.com/solutions/use-case/devsecops)
        -   [DevOps](https://github.com/solutions/use-case/devops)
        -   [CI/CD](https://github.com/solutions/use-case/ci-cd)
        -   [View all use cases](https://github.com/solutions/use-case)
        
    -   BY INDUSTRY
        
        -   [Healthcare](https://github.com/solutions/industry/healthcare)
        -   [Financial services](https://github.com/solutions/industry/financial-services)
        -   [Manufacturing](https://github.com/solutions/industry/manufacturing)
        -   [Government](https://github.com/solutions/industry/government)
        -   [View all industries](https://github.com/solutions/industry)
        
    
    [View all solutions](https://github.com/solutions)
    
-   Resources
    
    -   EXPLORE BY TOPIC
        
        -   [AI](https://github.com/resources/articles?topic=ai)
        -   [Software Development](https://github.com/resources/articles?topic=software-development)
        -   [DevOps](https://github.com/resources/articles?topic=devops)
        -   [Security](https://github.com/resources/articles?topic=security)
        -   [View all topics](https://github.com/resources/articles)
        
    -   EXPLORE BY TYPE
        
        -   [Customer stories](https://github.com/customer-stories)
        -   [Events & webinars](https://github.com/resources/events)
        -   [Ebooks & reports](https://github.com/resources/whitepapers)
        -   [Business insights](https://github.com/solutions/executive-insights)
        -   [GitHub Skills](https://skills.github.com)
        
    -   SUPPORT & SERVICES
        
        -   [Documentation](https://docs.github.com)
        -   [Customer support](https://support.github.com)
        -   [Community forum](https://github.com/orgs/community/discussions)
        -   [Trust center](https://github.com/trust-center)
        -   [Partners](https://github.com/partners)
        
    
    [View all resources](https://github.com/resources)
    
-   Open Source
    
    -   COMMUNITY
        
        -   [GitHub SponsorsFund open source developers](https://github.com/open-source/sponsors)
        
    -   PROGRAMS
        
        -   [Security Lab](https://securitylab.github.com)
        -   [Maintainer Community](https://maintainers.github.com)
        -   [GitHub Stars](https://stars.github.com)
        -   [Archive Program](https://archiveprogram.github.com)
        
    -   REPOSITORIES
        
        -   [Topics](https://github.com/topics)
        -   [Trending](https://github.com/trending)
        -   [Collections](https://github.com/collections)
        
    
-   Enterprise
    
    -   ENTERPRISE SOLUTIONS
        
        -   [Enterprise platformAI-powered developer platform](https://github.com/enterprise)
        
    -   AVAILABLE ADD-ONS
        
        -   [GitHub Advanced SecurityEnterprise-grade security features](https://github.com/security/advanced-security)
        -   [Copilot for BusinessEnterprise-grade AI features](https://github.com/features/copilot/copilot-business)
        -   [Premium SupportEnterprise-grade 24/7 support](https://github.com/enterprise/premium-support)
        
    
-   [Pricing](https://github.com/pricing)

Search/

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Ffsilva-alt%2Fdevops-docker)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=fsilva-alt%2Fdevops-docker)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

[fsilva-alt](/fsilva-alt) / **[devops-docker](/fsilva-alt/devops-docker)** Public

-   [Notifications](/login?return_to=%2Ffsilva-alt%2Fdevops-docker) You must be signed in to change notification settings
-   [Fork 0](/login?return_to=%2Ffsilva-alt%2Fdevops-docker)
-   [Star 0](/login?return_to=%2Ffsilva-alt%2Fdevops-docker)
    

-   [Code](/fsilva-alt/devops-docker)
-   [Issues 0](/fsilva-alt/devops-docker/issues)
-   [Pull requests 0](/fsilva-alt/devops-docker/pulls)
-   [Actions](/fsilva-alt/devops-docker/actions)
-   [Projects](/fsilva-alt/devops-docker/projects)
-   [Security and quality 0](/fsilva-alt/devops-docker/security)
-   [Insights](/fsilva-alt/devops-docker/pulse)

Additional navigation options

-   [Code](/fsilva-alt/devops-docker)
-   [Issues](/fsilva-alt/devops-docker/issues)
-   [Pull requests](/fsilva-alt/devops-docker/pulls)
-   [Actions](/fsilva-alt/devops-docker/actions)
-   [Projects](/fsilva-alt/devops-docker/projects)
-   [Security and quality](/fsilva-alt/devops-docker/security)
-   [Insights](/fsilva-alt/devops-docker/pulse)

 [](/fsilva-alt/devops-docker)

main

[Branches](/fsilva-alt/devops-docker/branches)[Tags](/fsilva-alt/devops-docker/tags)

[](/fsilva-alt/devops-docker/branches)[](/fsilva-alt/devops-docker/tags)

Go to file

Code

Open more actions menu

## Latest commit

## History

[7 Commits](/fsilva-alt/devops-docker/commits/main/)

[](/fsilva-alt/devops-docker/commits/main/)7 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[docs](/fsilva-alt/devops-docker/tree/main/docs "docs")

[docs](/fsilva-alt/devops-docker/tree/main/docs "docs")

[exercises](/fsilva-alt/devops-docker/tree/main/exercises "exercises")

[exercises](/fsilva-alt/devops-docker/tree/main/exercises "exercises")

[scripts](/fsilva-alt/devops-docker/tree/main/scripts "scripts")

[scripts](/fsilva-alt/devops-docker/tree/main/scripts "scripts")

[tests](/fsilva-alt/devops-docker/tree/main/tests "tests")

[tests](/fsilva-alt/devops-docker/tree/main/tests "tests")

[.gitignore](/fsilva-alt/devops-docker/blob/main/.gitignore ".gitignore")

[.gitignore](/fsilva-alt/devops-docker/blob/main/.gitignore ".gitignore")

[LICENSE](/fsilva-alt/devops-docker/blob/main/LICENSE "LICENSE")

[LICENSE](/fsilva-alt/devops-docker/blob/main/LICENSE "LICENSE")

[README.md](/fsilva-alt/devops-docker/blob/main/README.md "README.md")

[README.md](/fsilva-alt/devops-docker/blob/main/README.md "README.md")

[install.sh](/fsilva-alt/devops-docker/blob/main/install.sh "install.sh")

[install.sh](/fsilva-alt/devops-docker/blob/main/install.sh "install.sh")

View all files

## Repository files navigation

-   [README](#)
-   [MIT license](#)

More items

# Curso de Docker no GitHub Codespaces

[](#curso-de-docker-no-github-codespaces)

Aula ao vivo de 3 horas, pelo Zoom, com exercícios feitos no navegador. O ambiente é o GitHub Codespaces, um computador Linux acessado pela internet que já vem com editor de arquivos, terminal e Docker. Cada pessoa recebe o seu, chamado **Codespace**.

Não é preciso ter experiência com programação ou Docker. Os programas dos exercícios já vêm prontos: você aprende a executá-los em containers e faz pequenas alterações seguindo os exemplos.

Comece por [Antes da aula](#antes-da-aula) e depois siga a [Sequência da aula](#sequ%C3%AAncia-da-aula). O [guia do aluno](/fsilva-alt/devops-docker/blob/main/docs/guia-do-aluno.md) tem dicas para acompanhar os exercícios e resolver os problemas mais comuns.

## O que você vai aprender

[](#o-que-você-vai-aprender)

-   entender o que é um container: um ambiente isolado para executar um programa;
-   criar containers a partir de imagens, que reúnem o programa e os arquivos necessários para executá-lo;
-   iniciar, parar e remover containers e ler as mensagens que o programa escreve enquanto roda, chamadas logs;
-   escrever um `Dockerfile`, o arquivo com as instruções para construir uma imagem;
-   acessar um programa pelo navegador e ajustar suas configurações;
-   compartilhar pastas com um container e guardar dados mesmo depois de removê-lo;
-   executar um site e uma API, que fornece dados para outros programas;
-   usar o Docker Compose para iniciar o site e a API juntos;
-   remover os recursos criados durante a aula e liberar espaço.

A ementa completa, com cronograma, está em [docs/ementa.md](/fsilva-alt/devops-docker/blob/main/docs/ementa.md).

## Antes da aula

[](#antes-da-aula)

Faça esta preparação **pelo menos um dia antes**, para ter tempo de resolver algum problema de acesso.

1.  Crie uma conta no [GitHub](https://github.com), se ainda não tiver uma, e entre nela.
    
2.  Crie um Codespace em branco: em [github.com/codespaces](https://github.com/codespaces), escolha o modelo **Blank** (em branco). Outro caminho é a página [codespaces/new](https://github.com/codespaces/new). Na primeira vez, a criação costuma levar de 1 a 3 minutos.
    
3.  O editor VS Code abre no navegador. Nele, abra o menu **Terminal → New Terminal** (novo terminal). O terminal é a área onde você digita comandos para o computador executar. Cole nele a linha abaixo e pressione Enter:
    
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-docker/main/install.sh)"
    
    Esse comando baixa e executa o instalador do curso, que salva o material em `~/devops-docker`, baixa as imagens usadas na aula e prepara os arquivos dos exercícios em `~/labs` (o `~` representa sua pasta pessoal no Codespace). O instalador também cria um atalho `labs` na pasta em que foi executado, para você chegar a esses arquivos pelo explorador do VS Code. Espere aparecer a mensagem **"Curso de Docker instalado com sucesso!"**.
    
4.  Abra outro terminal pelo menu **Terminal → New Terminal** e execute os comandos abaixo, um por vez, pressionando Enter depois de cada linha:
    
    docker run hello-world
    check.sh 00
    
    O primeiro executa um container de teste; o segundo confere se o ambiente está pronto. Se aparecer **concluído**, está tudo certo. Se aparecer uma dica, faça o que ela sugere e tente de novo. O [exercício 0](/fsilva-alt/devops-docker/blob/main/exercises/00-docker-funciona/README.md) explica cada etapa.
    
5.  Pare o Codespace para não gastar sua franquia gratuita: em [github.com/codespaces](https://github.com/codespaces), use **⋯ → Stop codespace**. No dia da aula, abra o mesmo Codespace e continue de onde parou.
    

## Como o ambiente funciona

[](#como-o-ambiente-funciona)

### Primeiros passos no terminal e no editor

[](#primeiros-passos-no-terminal-e-no-editor)

-   **Executar um comando:** copie a linha para o terminal e pressione Enter. Espere um comando terminar antes de digitar o próximo. Alguns programas ficam rodando até você interrompê-los; quando for assim, o enunciado explica como sair.
-   **Ler os exemplos:** comandos vão no terminal. Blocos marcados como `Dockerfile`, Python ou YAML vão no arquivo indicado pelo enunciado. Nos slides, o `$` no início da linha marca um comando e não deve ser copiado. Linhas que começam com `#` são comentários.
-   **Entrar em uma pasta:** digite `cd` e o caminho, como em `cd ~/labs/04-meu-primeiro-dockerfile`. `pwd` mostra em que pasta você está, `ls` lista o que há nela e `cat nome-do-arquivo` mostra o conteúdo de um arquivo no terminal.
-   **Abrir ou criar um arquivo:** dentro da pasta do exercício, digite, por exemplo, `code Dockerfile`. O VS Code abre o arquivo para edição; se ele ainda não existir, será criado quando você salvar. Salve com **Ctrl+S**, ou **Cmd+S** no Mac.
-   **Usar os nomes dos exemplos:** use os mesmos nomes de arquivos, imagens e containers dos enunciados, porque a verificação procura exatamente esses nomes.

Nos exemplos genéricos, troque `NN` pelo número do exercício; para o 5, por exemplo, `check.sh NN` vira `check.sh 05`. Do mesmo modo, `<nome>` marca um valor que você substitui, e os sinais `<` e `>` não entram no comando. Nas tabelas de referência, `[comando]` indica uma parte opcional e `…` indica um exemplo abreviado. Para executar, use as linhas completas da seção **Tarefa**.

### Onde ficam os arquivos

[](#onde-ficam-os-arquivos)

Onde

O quê

`~/devops-docker/`

Este repositório: enunciados, scripts e documentos

`~/devops-docker/exercises/NN-nome/README.md`

O enunciado de cada exercício

`~/labs/NN-nome/`

Os arquivos de partida dos exercícios 4 a 14, 16 e 17 (código, Dockerfiles, site)

Os exercícios 0 a 3 e 15 não têm pasta própria. Os comandos deles funcionam em qualquer pasta do terminal, porque só consultam ou alteram o que o Docker gerencia.

Comandos disponíveis no terminal:

Comando

Faz

`check.sh NN`

Confere o resultado do exercício: mostra ✅ quando está concluído ou dá dicas do que ajustar

`reset.sh NN`

Recomeça o exercício: apaga as alterações na pasta dele e remove os containers, imagens, volumes e redes que ele cria

`setup.sh`

Baixa as imagens e gera os laboratórios que ainda não existem. O instalador já faz isso

`rede.sh`

Corrige um bloqueio de firewall de alguns Codespaces que faz a conexão entre containers expirar. Já roda sozinho na instalação, no `check.sh` e a cada terminal novo

Dentro da pasta de um laboratório, `check.sh` e `reset.sh` funcionam sem o número. Depois de um `reset.sh`, entre de novo na pasta com o `cd` do enunciado antes de continuar. Para abrir um enunciado no editor, use, por exemplo, `code ~/devops-docker/exercises/08-abrindo-portas/README.md`.

## Sequência da aula

[](#sequência-da-aula)

#

Exercício

Tema

[0](/fsilva-alt/devops-docker/blob/main/exercises/00-docker-funciona/README.md)

Docker funciona?

`docker version`, `run hello-world` (antes da aula)

[1](/fsilva-alt/devops-docker/blob/main/exercises/01-ola-container/README.md)

Olá, container

`docker run`, `ps -a`, `images`; imagem × container

[2](/fsilva-alt/devops-docker/blob/main/exercises/02-dentro-do-container/README.md)

Dentro do container

`-it`, `--rm`, `--name`; cada container tem o seu sistema de arquivos

[3](/fsilva-alt/devops-docker/blob/main/exercises/03-ciclo-de-vida/README.md)

Ciclo de vida

`-d`, `logs`, `stop`, `start`, `rm`

[4](/fsilva-alt/devops-docker/blob/main/exercises/04-meu-primeiro-dockerfile/README.md)

Meu primeiro Dockerfile

`FROM`, `COPY`, `CMD`, `build -t`, `tag`

[5](/fsilva-alt/devops-docker/blob/main/exercises/05-instalando-dependencias/README.md)

Instalando dependências

`WORKDIR`, `RUN pip install`, `requirements.txt`

[6](/fsilva-alt/devops-docker/blob/main/exercises/06-camadas-e-cache/README.md)

Camadas e cache · **opcional**

ordem das instruções, `history`

[7](/fsilva-alt/devops-docker/blob/main/exercises/07-o-que-nao-entra/README.md)

O que não entra na imagem · **opcional**

`.dockerignore`

[8](/fsilva-alt/devops-docker/blob/main/exercises/08-abrindo-portas/README.md)

Abrindo portas

`-p`, `EXPOSE`, aba PORTS, `/docs`

[9](/fsilva-alt/devops-docker/blob/main/exercises/09-configuracao-por-ambiente/README.md)

Configuração por ambiente

`ENV`, `-e`, `--env-file`, `exec`

[10](/fsilva-alt/devops-docker/blob/main/exercises/10-editando-ao-vivo/README.md)

Editando ao vivo

bind mount `-v "$PWD:/app"`

[11](/fsilva-alt/devops-docker/blob/main/exercises/11-dados-que-ficam/README.md)

Dados que ficam · **opcional**

`docker volume`, `ENTRYPOINT`

[12](/fsilva-alt/devops-docker/blob/main/exercises/12-site-estatico/README.md)

Site estático

`nginx:alpine` + HTML/JS

[13](/fsilva-alt/devops-docker/blob/main/exercises/13-containers-conversando/README.md)

Containers conversando

`network create`, DNS por nome

[14](/fsilva-alt/devops-docker/blob/main/exercises/14-docker-compose/README.md)

Docker Compose

`compose.yaml`, `up -d`, `ps`, `logs`, `down`

[16](/fsilva-alt/devops-docker/blob/main/exercises/16-compose-desenvolvimento/README.md)

Desenvolvimento com Compose · **opcional**

bind mount em YAML, recarga do código, `compose exec`

[17](/fsilva-alt/devops-docker/blob/main/exercises/17-compose-persistencia/README.md)

Persistência com Compose · **opcional**

volumes nomeados, `compose run --rm`, `down` × `down -v`

[15](/fsilva-alt/devops-docker/blob/main/exercises/15-faxina/README.md)

Faxina · **opcional**

`system df`, `prune`

A trilha principal é **0 → 1 → 2 → 3 → 4 → 5 → 8 → 9 → 10 → 12 → 13 → 14**, e o 10 (Editando ao vivo) faz parte dela. Ela vai dos primeiros containers até o site e a API rodando juntos com Compose. Os exercícios 6, 7, 11, 15, 16 e 17 são opcionais, e a seção **Missão extra** de cada enunciado também. O 16 e o 17 são práticas de Compose para depois da aula, com arquivos próprios. Faça a **faxina (15) por último**, depois das práticas que escolher.

O exemplo que acompanha a aula é um livro de receitas. Primeiro, um programa Python mostra as receitas no terminal. Depois, uma API fornece esses dados pela rede. Por fim, um site exibe a lista no navegador, e o Docker Compose inicia os containers do site e da API juntos.

## Ao final da aula

[](#ao-final-da-aula)

1.  Se ainda não fez a faxina (exercício 15), `docker ps -a` mostra os containers que sobraram.
2.  **Pare ou exclua o Codespace.** Mesmo parado, ele ocupa armazenamento da franquia gratuita. Se você excluí-lo, perde os arquivos e as alterações feitas nele. O instalador consegue preparar os arquivos iniciais do curso em outro Codespace, mas não recupera o seu trabalho.
3.  Para continuar estudando: o livro gratuito [Descomplicando Docker](https://livro.descomplicandodocker.com.br/), em português, e os guias [Docker concepts](https://docs.docker.com/get-started/docker-concepts/) da documentação oficial.

## Para desenvolver o curso

[](#para-desenvolver-o-curso)

`scripts/labs.sh` gera os arquivos iniciais dos laboratórios, e `scripts/checks.sh` verifica as respostas. Os testes ficam em `tests/` e rodam com o comando abaixo. Eles usam um container Docker-in-Docker, isto é, um container com outro Docker dentro, e precisam da opção `--privileged`. Os testes executam o `install.sh` e, para cada exercício, conferem se o `check.sh` aponta o que falta, orienta diante de respostas erradas e aprova a solução do gabarito:

tests/rodar.sh

## Licença

[](#licença)

[MIT](/fsilva-alt/devops-docker/blob/main/LICENSE).

## About

devops-docker

[fsilva-alt.github.io/devops-docker/](https://fsilva-alt.github.io/devops-docker/)

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/fsilva-alt/devops-docker/activity)

### Stars

**0** stars

### Watchers

**0** watching

### Forks

[**0** forks](/fsilva-alt/devops-docker/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Ffsilva-alt%2Fdevops-docker&report=fsilva-alt+%28user%29)

## Releases

## Packages

## Contributors

## Languages

## Footer

[](https://github.com)© 2026 GitHub, Inc.

### Footer navigation

-   [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
-   [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
-   [Security](https://github.com/security)
-   [Status](https://www.githubstatus.com/)
-   [Community](https://github.community/)
-   [Docs](https://docs.github.com/)
-   [Contact](https://support.github.com?tags=dotcom-footer)
-   Manage cookies
-   Do not share my personal information

You can’t perform that action at this time.
```

---

## Assistant (Build · GPT-6 Astra · 12.8s)

_Thinking:_

**Loading slide guidance**

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/docs/index.html"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/docs/index.html</path>
<type>file</type>
<content>
1: <!doctype html>
2: <html lang="pt-BR">
3: <head>
4:   <meta charset="utf-8">
5:   <meta name="viewport" content="width=device-width, initial-scale=1">
6:   <meta name="theme-color" content="#121016">
7:   <meta name="description" content="Introdução ao GitHub Actions em português: 7 exercícios, 3 horas e prática obrigatória no GitHub Codespaces. Testes, build e deploy no GitHub Pages.">
8:   <title>Curso de Github Action</title>
9:   <link rel="preconnect" href="https://fonts.googleapis.com">
10:   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
11:   <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
12:   <link rel="stylesheet" href="style.css">
13: </head>
14: <body>
15:   <a class="skip" href="#conteudo">Pular para o conteúdo</a>
16:   <header class="topbar">
17:     <a class="brand" href="#home" aria-label="GitHub Actions, início"><span class="brand-icon" aria-hidden="true">⌘</span><span>devops<span class="brand-slash"> / </span><strong>actions</strong></span></a>
18:     <nav aria-label="Navegação principal">
19:       <a href="https://github.com/fsilva-alt/devops-ghactions#antes-da-aula">Preparação <span aria-hidden="true">↗</span></a>
20:       <a href="https://github.com/fsilva-alt/devops-ghactions">Repositório <span aria-hidden="true">↗</span></a>
21:       <span class="language">PT-BR</span>
22:     </nav>
23:   </header>
24: 
25:   <main id="conteudo">
26:     <div id="home">
27:       <section class="hero" aria-labelledby="titulo">
28:         <div>
29:           <p class="eyebrow"><span class="status-dot"></span> INTRODUÇÃO AO GITHUB ACTIONS</p>
30:           <h1 id="titulo">Curso de Github Action</h1>
31:           <p class="hero-description">Aprenda os fundamentos da automação com Github Actions.</p>
32:           <div class="hero-actions">
33:             <a class="button primary" href="#intro">Iniciar o curso <span aria-hidden="true">→</span></a>
34:             <span class="small-note">Prática no GitHub Codespaces.</span>
35:           </div>
36:           <div class="stats" aria-label="Informações do curso">
37:             <div><strong>07</strong><span>exercícios guiados</span></div>
38:             <div><strong>03<span class="unit">h</span></strong><span>de teoria + prática</span></div>
39:             <div><strong>01</strong><span>site publicado no GitHub Pages</span></div>
40:           </div>
41:         </div>
42:         <div class="preview" aria-label="Ilustração do fluxo de integração e publicação">
43:           <div class="preview-bar"><span><i></i><i></i><i></i></span><span>.github/workflows/ci.yml</span><span>YAML</span></div>
44:           <div class="preview-code"><span class="line-number">01</span><span><b>name:</b> Meu primeiro CI</span><span class="line-number">02</span><span><b>on:</b> [push]</span><span class="line-number">03</span><span>&nbsp;</span><span class="line-number">04</span><span><b>jobs:</b></span><span class="line-number">05</span><span>  <b>testar:</b></span><span class="line-number">06</span><span>    <b>runs-on:</b> ubuntu-latest</span><span class="line-number">07</span><span>    <b>steps:</b></span><span class="line-number">08</span><span>      - <b>uses:</b> actions/checkout@v5</span><span class="line-number">09</span><span>      - <b>run:</b> python3 -m unittest -v</span></div>
45:           <div class="preview-flow"><span>✓ Testar</span><b>→</b><span>✓ Gerar</span><b>→</b><span class="last">✓ Publicar</span></div>
46:           <div class="preview-caption"><span class="status-dot"></span> Automação de testes, build e publicação.</div>
47:         </div>
48:       </section>
49: 
50:       <aside class="environment"><span class="environment-icon" aria-hidden="true">&gt;_</span><div><strong>Ambiente de prática: GitHub Codespaces.</strong><p>Você edita no <b>GitHub Codespaces</b>, acompanha os runners no <b>Actions</b> e abre o resultado no <b>Pages</b>. O código do projeto já está pronto.</p></div><a href="#intro">Ver a preparação <span aria-hidden="true">→</span></a></aside>
51: 
52:       <section class="curriculum" aria-labelledby="trilha-title">
53:         <div class="section-heading"><div><p class="eyebrow">CONTEÚDO DO CURSO</p><h2 id="trilha-title">Módulos e exercícios</h2></div><span class="level">Nível introdutório</span></div>
54:         <div id="exercicios" class="exercise-grid">
55:           <a class="exercise-card" href="#exercicio-01"><div class="card-top"><span class="card-number">Módulo 01</span><span class="card-time">15 min</span></div><div><h3>Primeiro workflow</h3><p>Crie um workflow de execução manual e identifique seus jobs, etapas e runner.</p></div><div class="card-bottom"><span>workflow · job · step</span><b aria-hidden="true">↗</b></div></a>
56:           <a class="exercise-card" href="#exercicio-02"><div class="card-top"><span class="card-number">Módulo 02</span><span class="card-time">25 min</span></div><div><h3>Testes no push</h3><p>Configure o ambiente do runner e a execução automática dos testes a cada push.</p></div><div class="card-bottom"><span>push · uses · run</span><b aria-hidden="true">↗</b></div></a>
57:           <a class="exercise-card" href="#exercicio-03"><div class="card-top"><span class="card-number">Módulo 03</span><span class="card-time">25 min</span></div><div><h3>Checks no pull request</h3><p>Veja um teste falhar, encontre a causa e corrija antes de integrar a mudança.</p></div><div class="card-bottom"><span>pull_request · logs · correção</span><b aria-hidden="true">↗</b></div></a>
58:           <a class="exercise-card" href="#exercicio-04"><div class="card-top"><span class="card-number">Módulo 04</span><span class="card-time">20 min</span></div><div><h3>Variáveis e contextos</h3><p>Use variáveis, entradas e segredos para configurar uma execução.</p></div><div class="card-bottom"><span>env · inputs · vars · secrets</span><b aria-hidden="true">↗</b></div></a>
59:           <a class="exercise-card" href="#exercicio-05"><div class="card-top"><span class="card-number">Módulo 05</span><span class="card-time">20 min</span></div><div><h3>Jobs e dependências</h3><p>Configure o build para executar somente após a aprovação dos testes.</p></div><div class="card-bottom"><span>needs · runner · build</span><b aria-hidden="true">↗</b></div></a>
60:           <a class="exercise-card" href="#exercicio-06"><div class="card-top"><span class="card-number">Módulo 06</span><span class="card-time">20 min</span></div><div><h3>Artefatos do build</h3><p>Armazene os arquivos gerados pelo build e baixe o artefato da execução.</p></div><div class="card-bottom"><span>upload-artifact · download</span><b aria-hidden="true">↗</b></div></a>
61:           <a class="exercise-card featured" href="#exercicio-07"><div class="card-top"><span class="card-number">Módulo 07</span><span class="card-time">30 min</span></div><div><h3>Deploy no Pages</h3><p>Publique o cardápio em uma URL pública no GitHub Pages com o workflow fornecido.</p></div><div class="card-bottom"><span>testar → gerar → publicar</span><b aria-hidden="true">↗</b></div></a>
62:         </div>
63:       </section>
64: 
65:       <section class="closing"><div><p class="eyebrow">EMENTA</p><h2>Objetivos do curso</h2></div><p>Ler e escrever workflows, investigar falhas nos logs e configurar testes, build e publicação no GitHub Pages. Cada exercício tem um objetivo, um exemplo e um resultado para conferir.</p><a href="https://github.com/fsilva-alt/devops-ghactions/blob/main/docs/ementa.md">Ver a ementa completa <span aria-hidden="true">↗</span></a></section>
66:     </div>
67: 
68:     <div id="deck">
69:       <section id="intro" class="lesson" aria-labelledby="intro-title" tabindex="-1">
70:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>Antes de começar</span></div>
71:         <p class="eyebrow">PREPARAÇÃO</p>
72:         <h2 id="intro-title">Ambiente de prática</h2>
73:         <div class="slide-columns">
74:           <div class="slide-stack">
75:             <p class="lead">Automatizar é transformar uma sequência de passos em um processo que você pode repetir e conferir.</p>
76:             <div class="box"><h3>O projeto já está pronto</h3><p>Um cardápio em Python, três testes e um gerador de HTML. Você vai aprender a descrever o processo em YAML. Precisa conhecer commit, branch e push; os comandos de publicação estão nos enunciados.</p></div>
77:             <div class="box"><h3>Preparação com install.sh</h3><ol class="task-list"><li>Em <a href="https://github.com/codespaces">github.com/codespaces</a>, crie um Codespace com o modelo <strong>Blank</strong>.</li><li>Abra <strong>Terminal → New Terminal</strong>, execute o comando abaixo e conclua o login do GitHub.</li><li>Aguarde a confirmação da instalação. Abra um <strong>terminal novo</strong> e execute <code>check.sh 01</code>. É esperado pedir o workflow que você ainda vai criar.</li></ol></div>
78:             <pre><code>sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"</code></pre>
79:             <p class="small-note">O material fica em <code>~/devops-ghactions</code> e os laboratórios em <code>~/labs</code>. O atalho <code>labs</code> permite acessar os arquivos pelo explorador do editor.</p>
80:             <a class="button primary" href="https://github.com/fsilva-alt/devops-ghactions#antes-da-aula">Abrir a preparação completa ↗</a>
81:           </div>
82:           <div class="slide-stack">
83:             <div class="flow"><span>Codespace</span><b aria-hidden="true">→</b><span>GitHub</span><b aria-hidden="true">→</b><span>Runner</span><b aria-hidden="true">→</b><span>Pages</span></div>
84:             <div class="box"><h3>Componentes do ambiente</h3><p><strong>Codespace:</strong> seu editor e terminal no navegador, obrigatório nos 7 exercícios.</p><p><strong>GitHub:</strong> recebe o push e cria uma execução a partir do evento.</p><p><strong>Runner:</strong> executa o job em outra máquina.</p><p><strong>Pages:</strong> hospeda o site em uma URL pública.</p></div>
85:             <div class="callout">CI verifica as mudanças. Build gera os arquivos finais. Deploy publica o resultado.</div>
86:           </div>
87:         </div>
88:         <details class="box lesson-details"><summary>Como acompanhar a prática</summary><ol class="task-list"><li>Selecione o exercício no índice dos slides, leia o enunciado e entre na pasta <code>~/labs/NN-nome</code>.</li><li>Edite e salve o workflow. Rode <code>check.sh NN</code> e ajuste o YAML.</li><li>Faça commit e publique um repositório por exercício, de <code>actions-01</code> a <code>actions-07</code>.</li><li>Abra Actions e confira a entrega pedida. Todos os laboratórios são feitos no mesmo Codespace.</li></ol><p>O check local analisa alguns requisitos do YAML. A execução na aba Actions mostra o resultado real. Consulte o <a href="guia-do-aluno.md">guia do aluno</a> para orientações sobre o ambiente.</p></details>
89:         <nav class="deck-bottom" aria-label="Navegação da introdução"><a class="button" href="#home">← Índice</a><a class="button primary" href="#exercicio-01">Primeiro exercício →</a></nav>
90:       </section>
91:       <section id="exercicio-01" class="lesson" aria-labelledby="titulo-01" tabindex="-1">
92:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>01 / 07 · 15 minutos</span></div>
93:         <p class="eyebrow">WORKFLOW · JOB · STEP</p>
94:         <h2 id="titulo-01">Primeiro workflow</h2>
95:         <div class="slide-columns">
96:           <div class="slide-stack">
97:             <p class="lead">Crie um workflow com execução manual e confira a mensagem nos logs.</p>
98:             <div class="box"><h3>As partes da automação</h3><p><strong>Workflow:</strong> arquivo YAML que descreve o processo.</p><p><strong>Evento:</strong> o que inicia a execução; aqui, <code>workflow_dispatch</code>, um clique manual.</p><p><strong>Job:</strong> grupo de etapas que executa em um runner.</p><p><strong>Runner:</strong> máquina que executa o job.</p><p><strong>Step:</strong> cada etapa da lista <code>steps</code>.</p></div>
99:             <div class="callout">YAML usa espaços para a indentação. O traço inicia um item da lista. Salve o arquivo em <code>.github/workflows/ci.yml</code>.</div>
100:           </div>
101:           <pre><code>name: Boas-vindas
102: 
103: on:
104:   workflow_dispatch:
105: 
106: permissions:
107:   contents: read
108: 
109: jobs:
110:   boas-vindas:
111:     runs-on: ubuntu-latest
112:     steps:
113:       - name: Cumprimentar a turma
114:         run: echo "Olá, GitHub Actions!"</code></pre>
115:         </div>
116:         <div class="lesson-practice slide-columns">
117:           <div class="slide-stack"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/01-primeiro-workflow
118: code .github/workflows/ci.yml
119: check.sh 01</code></pre><ol class="task-list"><li>Crie e salve o arquivo com o exemplo acima.</li><li>Confira com o check, faça commit e publique em <code>actions-01</code>.</li><li>Abra Actions → Boas-vindas → Run workflow. Selecione <code>main</code>.</li><li>Abra o job e a etapa para localizar a saudação no log.</li></ol></div>
120:           <div class="slide-stack"><div class="box"><h3>Sua entrega</h3><p>Link da execução manual verde e a mensagem <code>Olá, GitHub Actions!</code> no log.</p></div><details class="box"><summary>O echo executou no Codespace ou em um runner?</summary><p>Em um runner do Actions. O Codespace foi usado para escrever e publicar o workflow.</p></details><div class="callout">Se não houver execução após o push, está correto: neste exercício o único evento é manual. O botão aparece quando o workflow está na branch padrão.</div><a href="https://docs.github.com/pt/actions/get-started/understand-github-actions">Consultar a documentação oficial ↗</a></div>
121:         </div>
122:         <nav class="deck-bottom" aria-label="Navegação do exercício 01"><a class="button" href="#intro">← Introdução</a><a class="button primary" href="#exercicio-02">Testes no push →</a></nav>
123:       </section>
124:       <section id="exercicio-02" class="lesson" aria-labelledby="titulo-02" tabindex="-1">
125:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>02 / 07 · 25 minutos</span></div>
126:         <p class="eyebrow">PUSH · USES · RUN</p>
127:         <h2 id="titulo-02">Testes no push</h2>
128:         <div class="slide-columns">
129:           <div class="slide-stack"><p class="lead">Configure o ambiente do runner para executar os testes a cada push.</p><div class="box"><h3>Integração contínua</h3><p><strong>CI</strong> significa integração contínua: verificar mudanças automaticamente.</p><p><code>uses</code> chama uma action pronta, com versão explícita.</p><p><code>with</code> configura as entradas dessa action.</p><p><code>run</code> executa um comando no runner.</p></div><div class="callout">Checkout vem primeiro porque o runner precisa receber os arquivos do projeto. As etapas de um job executam em sequência.</div></div>
130:           <pre><code>name: CI
131: 
132: on:
133:   push:
134:     branches: [main]
135:   workflow_dispatch:
136: 
137: permissions:
138:   contents: read
139: 
140: jobs:
141:   testar:
142:     runs-on: ubuntu-latest
143:     steps:
144:       - uses: actions/checkout@v5
145:       - uses: actions/setup-python@v6
146:         with:
147:           python-version: '3.12'
148:       - run: python -m pip install -r requirements.txt
149:       - run: python -m unittest -v</code></pre>
150:         </div>
151:         <div class="lesson-practice slide-columns">
152:           <div class="slide-stack"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/02-testes-no-push
153: python3 -m unittest -v
154: code .github/workflows/ci.yml
155: check.sh 02</code></pre><ol class="task-list"><li>Execute os três testes prontos e procure <code>OK</code>.</li><li>Substitua a saudação pelo workflow acima.</li><li>Confira, faça commit e publique em <code>actions-02</code>.</li><li>Edite o título do cardápio, faça novo commit e push. Acompanhe outra execução.</li></ol></div>
156:           <div class="slide-stack"><div class="box"><h3>Sua entrega</h3><p>Uma execução verde disparada por <code>push</code>, com três testes aprovados. Localize o hash do commit na página da execução.</p></div><details class="box"><summary>Instalar no Codespace também instala no runner?</summary><p>Não. São máquinas separadas. O workflow precisa preparar seu próprio ambiente: código, Python e dependências.</p></details><div class="callout">Use <code>'3.12'</code> entre aspas: é uma versão, não um número decimal.</div><a href="https://docs.github.com/pt/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows">Consultar os eventos disponíveis ↗</a></div>
157:         </div>
158:         <nav class="deck-bottom" aria-label="Navegação do exercício 02"><a class="button" href="#exercicio-01">← Primeiro workflow</a><a class="button primary" href="#exercicio-03">Checks no PR →</a></nav>
159:       </section>
160:       <section id="exercicio-03" class="lesson" aria-labelledby="titulo-03" tabindex="-1">
161:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>03 / 07 · 25 minutos</span></div>
162:         <p class="eyebrow">PULL_REQUEST · LOGS · CORREÇÃO</p>
163:         <h2 id="titulo-03">Checks no pull request</h2>
164:         <div class="slide-columns">
165:           <div class="slide-stack"><p class="lead">Analise os logs de um teste com falha e corrija o código antes de integrar a mudança.</p><div class="box"><h3>Verificação de pull requests</h3><p><code>pull_request</code> executa os testes quando um PR é aberto ou atualizado. O filtro <code>branches</code> indica o <strong>destino</strong> do PR.</p><p>Abra a etapa que falhou. Compare o valor esperado com o recebido. O teste de três unidades espera 1500 centavos, mas a soma incorreta retorna 503.</p></div><div class="callout">Cada execução corresponde a uma revisão do código. Reexecutar um commit quebrado não aplica a correção que ainda está só no Codespace.</div></div>
166:           <div class="slide-stack"><pre><code># Substitua apenas o bloco on:
167: on:
168:   push:
169:     branches: [main]
170:   pull_request:
171:     branches: [main]
172:   workflow_dispatch:</code></pre><pre><code># Falha proposital em app.py:
173: return preco_centavos + quantidade
174: 
175: # Correção:
176: return preco_centavos * quantidade</code></pre></div>
177:         </div>
178:         <div class="lesson-practice slide-columns">
179:           <div class="slide-stack"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/03-checks-no-pull-request
180: code .github/workflows/ci.yml
181: check.sh 03</code></pre><ol class="task-list"><li>Acrescente o evento e publique a main em <code>actions-03</code>.</li><li>Crie a branch <code>teste-do-ci</code>. Troque a multiplicação por soma em <code>app.py</code>.</li><li>Faça commit, push e abra o PR para main. Leia o erro em Checks → testar → Testar.</li><li>Corrija a multiplicação. Faça novo commit e push na mesma branch e confira o novo check.</li></ol></div>
182:           <div class="slide-stack"><div class="box"><h3>Sua entrega</h3><p>Link do PR e das execuções vermelha e verde. Explique qual linha causava o erro. O PR pode ficar aberto para avaliação.</p></div><details class="box"><summary>Um check vermelho sempre impede o merge?</summary><p>Só quando regras do repositório exigem aquele check. Aqui aprendemos a observar e interpretar o resultado.</p></details><a href="https://docs.github.com/pt/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs">Consultar o guia de logs ↗</a></div>
183:         </div>
184:         <nav class="deck-bottom" aria-label="Navegação do exercício 03"><a class="button" href="#exercicio-02">← Testes no push</a><a class="button primary" href="#exercicio-04">Variáveis e contextos →</a></nav>
185:       </section>
186:       <section id="exercicio-04" class="lesson" aria-labelledby="titulo-04" tabindex="-1">
187:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>04 / 07 · 20 minutos</span></div>
188:         <p class="eyebrow">ENV · INPUTS · VARS · SECRETS</p>
189:         <h2 id="titulo-04">Variáveis e contextos</h2>
190:         <div class="slide-columns">
191:           <div class="slide-stack">
192:             <p class="lead">Configure uma execução manual com variáveis e contextos e identifique a origem dos valores usados.</p>
193:             <div class="box"><h3>Origem dos valores</h3><p><code>env</code> define variáveis no YAML, como o nome do curso.</p><p><code>inputs</code> recebe a mensagem digitada em Run workflow.</p><p><code>github</code> traz informações da execução, como quem a iniciou.</p><p><code>vars</code> lê variáveis das configurações do repositório.</p><p><code>secrets</code> lê valores cadastrados como segredos.</p></div>
194:             <div class="callout">O Actions avalia <code>${{ }}</code>; o shell lê <code>$VARIAVEL</code>. O exemplo passa a mensagem por <code>env</code> para tratá-la como texto, inclusive quando contém aspas.</div>
195:           </div>
196:           <div class="slide-stack">
197:             <p class="small-note">Trechos de duas etapas. Use o exemplo completo indicado na prática.</p>
198:             <pre><code># Na etapa Mostrar contexto:
199: env:
200:   MENSAGEM: ${{ inputs.mensagem }}
201:   AUTOR: ${{ github.actor }}
202:   TURMA: ${{ vars.TURMA }}
203: run: |
204:   printf '%s\n' "$MENSAGEM"
205:   printf '%s\n' "$AUTOR" "$TURMA"
206: 
207: # Em outra etapa, sem imprimir o segredo:
208: env:
209:   TOKEN_DEMO: ${{ secrets.CURSO_TOKEN }}
210: run: test -n "$TOKEN_DEMO"</code></pre>
211:             <div class="box"><h3>Um segredo de demonstração</h3><p>Cadastre <code>CURSO_TOKEN</code> com o valor fictício <code>somente-demonstracao</code>. O comando <code>test -n</code> verifica se o valor não está vazio, sem exibi-lo no log.</p></div>
212:           </div>
213:         </div>
214:         <div class="lesson-practice slide-columns">
215:           <div class="slide-stack"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/04-variaveis-e-contextos
216: cp "$CURSO_DIR/docs/solucoes/04.yml" .github/workflows/ci.yml
217: code .github/workflows/ci.yml
218: # Personalize e salve antes de conferir:
219: check.sh 04</code></pre><ol class="task-list"><li>Mude o <code>default</code> da entrada <code>mensagem</code> e localize <code>env.CURSO</code>.</li><li>Confira, faça commit e publique em <code>actions-04</code>.</li><li>Em Settings → Secrets and variables → Actions, crie a variável <code>TURMA</code> e o segredo fictício <code>CURSO_TOKEN</code>, nas respectivas abas.</li><li>Execute manualmente na main com uma mensagem sua. Leia os logs e a confirmação de presença do segredo.</li></ol></div>
220:           <div class="slide-stack"><div class="box"><h3>Sua entrega</h3><p>Uma execução manual verde com mensagem personalizada, autor, turma e segredo verificado sem exibir seu valor.</p></div><details class="box"><summary>Qual a diferença entre vars e secrets?</summary><p>Ambos vêm das configurações do repositório. Use <code>vars</code> para configurações comuns e <code>secrets</code> para valores sensíveis. No curso, o segredo é fictício e só verificamos sua presença.</p></details><div class="callout">O check local confere as referências no YAML. Se a última etapa falhar no Actions, confira o nome do segredo e o repositório em que foi cadastrado: um segredo ausente resulta em valor vazio.</div><a href="https://docs.github.com/pt/actions/learn-github-actions/contexts">Consultar a documentação de contextos ↗</a></div>
221:         </div>
222:         <nav class="deck-bottom" aria-label="Navegação do exercício 04"><a class="button" href="#exercicio-03">← Checks no PR</a><a class="button primary" href="#exercicio-05">Jobs e dependências →</a></nav>
223:       </section>
224:       <section id="exercicio-05" class="lesson" aria-labelledby="titulo-05" tabindex="-1">
225:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>05 / 07 · 20 minutos</span></div>
226:         <p class="eyebrow">NEEDS · RUNNER · BUILD</p>
227:         <h2 id="titulo-05">Jobs e dependências</h2>
228:         <div class="slide-columns">
229:           <div class="slide-stack">
230:             <p class="lead">Defina a dependência entre os jobs de testes e build e verifique o comportamento quando um teste falha.</p>
231:             <div class="flow"><span>testar</span><b aria-hidden="true">→</b><span>empacotar</span></div>
232:             <div class="box"><h3>Dependências entre jobs</h3><p>Etapas de um job executam em sequência. Jobs sem dependências podem executar em paralelo.</p><p><code>needs: testar</code> faz <code>empacotar</code> aguardar os testes e prosseguir somente se eles passarem.</p><p><strong>Build:</strong> neste projeto, <code>python build.py</code> transforma <code>cardapio.md</code> em <code>dist/index.html</code>.</p></div>
233:             <div class="callout">Cada job recebe seu próprio runner. Por isso, o build também precisa de checkout, Python e instalação das dependências.</div>
234:           </div>
235:           <div class="slide-stack"><p class="small-note">Acrescente dentro de jobs, no mesmo nível de testar, com dois espaços de indentação.</p><pre><code>empacotar:
236:   needs: testar
237:   runs-on: ubuntu-latest
238:   steps:
239:     - uses: actions/checkout@v5
240:     - uses: actions/setup-python@v6
241:       with:
242:         python-version: '3.12'
243:     - run: python -m pip install -r requirements.txt
244:     - run: python build.py
245:     - name: Conferir o arquivo gerado
246:       run: test -s dist/index.html</code></pre><div class="box"><h3>Conferir o build</h3><p><code>test -s</code> retorna sucesso quando o arquivo existe e não está vazio. O resultado ainda está somente no runner.</p></div></div>
247:         </div>
248:         <div class="lesson-practice slide-columns">
249:           <div class="slide-stack"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/05-jobs-e-dependencias
250: code .github/workflows/ci.yml
251: check.sh 05</code></pre><ol class="task-list"><li>Preserve <code>testar</code> e acrescente o job <code>empacotar</code>.</li><li>Confira, faça commit e publique em <code>actions-05</code>. Veja o grafo da execução.</li><li>Em <code>app.py</code>, troque temporariamente a multiplicação por soma. Faça commit e push na main. Observe o build como <strong>skipped</strong> (pulado).</li><li>Corrija a multiplicação, faça outro commit e push. Termine com os dois jobs verdes.</li></ol></div>
252:           <div class="slide-stack"><div class="box"><h3>Sua entrega</h3><p>Execução final verde e uma execução anterior com o build pulado após a falha dos testes.</p></div><details class="box"><summary>Os arquivos de testar aparecem em empacotar?</summary><p>Não. Jobs separados não compartilham automaticamente o sistema de arquivos. As etapas do mesmo job compartilham seus arquivos. <code>needs</code> define a dependência, mas não copia arquivos.</p></details><a href="https://docs.github.com/pt/actions/using-jobs/using-jobs-in-a-workflow">Consultar a documentação de jobs ↗</a></div>
253:         </div>
254:         <nav class="deck-bottom" aria-label="Navegação do exercício 05"><a class="button" href="#exercicio-04">← Variáveis e contextos</a><a class="button primary" href="#exercicio-06">Artefatos do build →</a></nav>
255:       </section>
256:       <section id="exercicio-06" class="lesson" aria-labelledby="titulo-06" tabindex="-1">
257:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>06 / 07 · 20 minutos</span></div>
258:         <p class="eyebrow">UPLOAD-ARTIFACT · DOWNLOAD</p>
259:         <h2 id="titulo-06">Artefatos do build</h2>
260:         <div class="slide-columns">
261:           <div class="slide-stack">
262:             <p class="lead">Armazene os arquivos gerados como artefatos para baixá-los após a execução.</p>
263:             <div class="box"><h3>Armazenamento de artefatos</h3><p>Um <strong>artefato</strong> guarda arquivos de uma execução para consulta ou distribuição. Pode ser um site, relatório ou pacote.</p><p>Aqui, <code>name: site</code> identifica o artefato e <code>path: dist/</code> escolhe os arquivos enviados.</p><p><code>retention-days: 7</code> solicita que o resultado fique disponível por sete dias.</p></div>
264:             <div class="callout">O upload vem depois do build. Guardar o ZIP como artefato ainda não publica o site na web.</div>
265:           </div>
266:           <div class="slide-stack"><p class="small-note">Última etapa de jobs.empacotar.steps. Alinhe o traço com o das outras etapas.</p><pre><code>- name: Guardar o site
267:   uses: actions/upload-artifact@v4
268:   with:
269:     name: site
270:     path: dist/
271:     if-no-files-found: error
272:     retention-days: 7</code></pre><div class="box"><h3>Quando nenhum arquivo é encontrado</h3><p><code>if-no-files-found: error</code> faz a etapa falhar se não houver arquivos para enviar. Confira se o build terminou e se a pasta é <code>dist/</code>.</p></div></div>
273:         </div>
274:         <div class="lesson-practice slide-columns">
275:           <div class="slide-stack"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/06-artefatos-do-build
276: code .github/workflows/ci.yml
277: check.sh 06</code></pre><ol class="task-list"><li>Adicione o upload no final das etapas de <code>empacotar</code>.</li><li>Confira, faça commit e publique em <code>actions-06</code>.</li><li>Depois da execução, encontre Artifacts → site no resumo. Logado no GitHub, baixe o ZIP e abra <code>index.html</code>.</li><li>No Codespace, personalize o título do cardápio, faça commit e push. Baixe o artefato da nova execução e compare o título.</li></ol></div>
278:           <div class="slide-stack"><div class="box"><h3>Sua entrega</h3><p>Link da execução final e confirmação de que o artefato <code>site</code> contém <code>index.html</code> com seu título atualizado.</p></div><details class="box"><summary>Onde procurar o artefato de uma versão anterior?</summary><p>Na execução daquele commit, enquanto o artefato não tiver expirado ou sido removido. Cada execução tem seu próprio resultado.</p></details><a href="https://docs.github.com/pt/actions/using-workflows/storing-workflow-data-as-artifacts">Consultar a documentação de artefatos ↗</a></div>
279:         </div>
280:         <nav class="deck-bottom" aria-label="Navegação do exercício 06"><a class="button" href="#exercicio-05">← Jobs e dependências</a><a class="button primary" href="#exercicio-07">Deploy no Pages →</a></nav>
281:       </section>
282:       <section id="exercicio-07" class="lesson" aria-labelledby="titulo-07" tabindex="-1">
283:         <div class="deck-top"><a href="#home" class="back">← Todos os exercícios</a><span>07 / 07 · 30 minutos</span></div>
284:         <p class="eyebrow">TESTAR → GERAR → PUBLICAR</p>
285:         <h2 id="titulo-07">Deploy no Pages</h2>
286:         <div class="slide-columns">
287:           <div class="slide-stack">
288:             <p class="lead">Publique o site no GitHub Pages com o workflow fornecido, que reúne testes, build e deploy.</p>
289:             <div class="flow"><span>testar</span><b aria-hidden="true">→</b><span>empacotar</span><b aria-hidden="true">→</b><span>publicar</span></div>
290:             <div class="box"><h3>Etapas de publicação</h3><p><code>testar</code> verifica o código. Se passar, <code>empacotar</code> gera o HTML, prepara o Pages com <code>actions/configure-pages</code> e envia o site com <code>actions/upload-pages-artifact</code>.</p><p><code>publicar</code> usa <code>actions/deploy-pages</code> para disponibilizar esse artefato no endereço do site.</p></div>
291:             <div class="callout">O job de publicação recebe <code>pages: write</code> e <code>id-token: write</code>. O GitHub fornece a credencial da execução; não é necessário cadastrar um token pessoal.</div>
292:           </div>
293:           <div class="slide-stack"><p class="small-note">Job final do exemplo. O arquivo completo também contém os testes e o build.</p><pre><code>publicar:
294:   needs: empacotar
295:   if: github.ref == 'refs/heads/main' &amp;&amp; github.event_name != 'pull_request'
296:   runs-on: ubuntu-latest
297:   permissions:
298:     pages: write
299:     id-token: write
300:   environment:
301:     name: github-pages
302:     url: ${{ steps.deploy.outputs.page_url }}
303:   steps:
304:     - name: Publicar
305:       id: deploy
306:       uses: actions/deploy-pages@v4</code></pre><div class="box"><h3>Publicar somente a main</h3><p>A condição <code>if</code> permite a publicação da main por push ou execução manual e exclui PRs. Os PRs continuam executando <code>testar</code>.</p><p>O environment <code>github-pages</code> identifica o destino e exibe a URL devolvida pela etapa <code>deploy</code>.</p></div></div>
307:         </div>
308:         <div class="lesson-practice slide-columns">
309:           <div class="slide-stack"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/07-deploy-no-pages
310: # Publique o estado inicial primeiro:
311: gh repo create actions-07 --public --source=. --remote=origin --push
312: gh browse</code></pre><ol class="task-list"><li>Em Settings → Pages → Build and deployment → Source, escolha <strong>GitHub Actions</strong>.</li><li>Volte ao Codespace e copie o workflow guiado com os comandos abaixo. Leia o fluxo com o professor.</li><li>Personalize o título de <code>cardapio.md</code>. Rode o check, faça commit e push.</li><li>Acompanhe os três jobs e abra a URL do environment <code>github-pages</code>.</li></ol><pre><code>cp "$CURSO_DIR/docs/solucoes/07.yml" .github/workflows/ci.yml
313: code .github/workflows/ci.yml
314: # Após editar e salvar o cardápio:
315: check.sh 07
316: git add .github/workflows/ci.yml cardapio.md
317: git commit -m "Publica o cardápio no GitHub Pages"
318: git push
319: gh browse --actions</code></pre></div>
320:           <div class="slide-stack"><div class="box"><h3>Sua entrega</h3><p>URL pública do cardápio com seu título e link da execução de deploy com os três jobs verdes.</p></div><details class="box"><summary>Qual é a diferença entre build, artefato e deploy?</summary><p><strong>Build</strong> gera os arquivos. <strong>Artefato</strong> guarda os arquivos. <strong>Deploy</strong> disponibiliza o resultado em seu destino, aqui o Pages.</p></details><details class="box"><summary>E se o site ainda não abrir?</summary><p>Aguarde alguns minutos após a publicação. Se o workflow falhou, confirme a configuração em Settings → Pages e compare <code>permissions</code> e <code>environment</code> com o exemplo. Após corrigir, use Actions → Publicar no Pages → Run workflow → main.</p></details><a href="https://docs.github.com/pt/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages">Consultar o guia de workflows do Pages ↗</a></div>
321:         </div>
322:         <aside class="box course-finish"><h3>Encerramento</h3><p>Salve os links das entregas, publique as mudanças que deseja manter e pare o Codespace em <a href="https://github.com/codespaces">github.com/codespaces</a> → ⋯ → Stop codespace. Seu site e seus repositórios publicados continuam no GitHub.</p></aside>
323:         <nav class="deck-bottom" aria-label="Navegação do exercício 07"><a class="button" href="#exercicio-06">← Artefatos do build</a><a class="button primary" href="#home">Concluir e voltar ao índice →</a></nav>
324:       </section>
325:     </div>
326:   </main>
327:   <footer><span>GitHub Actions <span class="brand-slash">/</span> Curso introdutório</span><div><a href="https://github.com/fsilva-alt/devops-ghactions/blob/main/docs/guia-do-professor.md">Guia do professor</a><a href="https://docs.github.com/pt/actions">Documentação oficial ↗</a></div></footer>
328: </body>
329: </html>

(End of file - total 329 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/docs/style.css"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/docs/style.css</path>
<type>file</type>
<content>
1: :root {
2:   color-scheme: dark;
3:   --bg: #121016;
4:   --panel: #1b1721;
5:   --panel-hover: #241e2e;
6:   --line: #352d40;
7:   --text: #f4f0f8;
8:   --secondary: #c6bdcf;
9:   --muted: #a297af;
10:   --accent: #c7a0ff;
11:   --accent-bright: #dbc2ff;
12:   --accent-dark: #211032;
13:   --green: #add4b5;
14:   --display: 'Space Grotesk', system-ui, sans-serif;
15:   --body: 'DM Sans', system-ui, sans-serif;
16:   --mono: 'IBM Plex Mono', monospace;
17: }
18: * { box-sizing: border-box; }
19: body { margin: 0; color: var(--text); background: var(--bg); font-family: var(--body); line-height: 1.65; }
20: a { color: var(--accent); text-underline-offset: 4px; }
21: a, summary { -webkit-tap-highlight-color: transparent; }
22: a:focus-visible, summary:focus-visible { outline: 2px solid var(--accent-bright); outline-offset: 5px; }
23: ::selection { background: var(--accent); color: var(--accent-dark); }
24: h1, h2, h3 { font-family: var(--display); line-height: 1.16; font-weight: 500; letter-spacing: -.04em; }
25: p, h1, h2, h3 { margin: 0; }
26: .topbar, main, footer { max-width: 1280px; margin-inline: auto; padding-inline: 40px; }
27: .topbar { height: 92px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); gap: 24px; }
28: .brand { display: flex; align-items: center; gap: 13px; font-family: var(--display); font-size: 20px; color: var(--secondary); text-decoration: none; }
29: .brand strong { color: var(--text); font-weight: 500; }
30: .brand-icon { border: 1px solid #6e548a; background: #251b31; color: var(--accent); border-radius: 10px; width: 37px; height: 37px; display: grid; place-items: center; font-size: 25px; }
31: .brand-slash { color: var(--accent); margin-inline: 5px; }
32: .topbar nav { display: flex; align-items: center; gap: 30px; font-size: 13px; }
33: .topbar nav a { color: var(--secondary); text-decoration: none; }
34: .topbar nav a:hover, footer a:hover { color: var(--accent); }
35: .language { font-family: var(--mono); font-size: 11px; border: 1px solid var(--line); border-radius: 5px; padding: 4px 8px; color: var(--muted); }
36: .hero { display: grid; grid-template-columns: 1.2fr 1fr; align-items: center; gap: 45px; padding-block: 84px 65px; }
37: .eyebrow { color: var(--accent); font-family: var(--mono); font-size: 11px; letter-spacing: .13em; display: flex; align-items: center; gap: 10px; margin-bottom: 23px; }
38: .status-dot { display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: var(--accent); flex-shrink: 0; }
39: h1 { font-size: clamp(36px, 4.2vw, 56px); }
40: h1 em { color: var(--accent); font-style: normal; }
41: .hero-description { color: var(--secondary); max-width: 480px; font-size: 16px; line-height: 1.8; margin-top: 25px; }
42: .hero-actions { display: flex; align-items: center; flex-wrap: wrap; gap: 18px; margin-top: 30px; }
43: .button { border: 1px solid var(--line); background: var(--panel); color: var(--text); border-radius: 7px; display: inline-flex; justify-content: center; gap: 24px; align-items: center; padding: 12px 19px; font: 500 14px/1.4 var(--body); cursor: pointer; text-decoration: none; transition: background .15s, border-color .15s; }
44: .button:hover { background: var(--panel-hover); border-color: var(--accent); }
45: .button.primary { color: var(--accent-dark); background: var(--accent); border-color: var(--accent); }
46: .button.primary:hover { background: var(--accent-bright); }
47: .small-note { color: var(--muted); font-size: 11px; }
48: .stats { display: flex; gap: 38px; margin-top: 39px; }
49: .stats div { display: flex; flex-direction: column; }
50: .stats strong { font-family: var(--display); font-size: 30px; line-height: 1.3; font-weight: 400; }
51: .stats span { color: var(--muted); font-size: 11px; }
52: .stats .unit { font-size: 21px; color: var(--secondary); margin-left: 3px; }
53: .preview { background: var(--panel); border: 1px solid #51405f; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 90px #0004, 0 0 90px #bc82ff08; transform: rotate(-1deg); min-width: 0; }
54: .preview-bar { background: #211b28; padding: 17px; display: flex; align-items: center; justify-content: space-between; font: 10px var(--mono); color: var(--muted); gap: 8px; border-bottom: 1px solid var(--line); }
55: .preview-bar i { display: inline-block; border-radius: 50%; background: #594664; width: 6px; height: 6px; margin-right: 4px; }
56: .preview-bar i:first-child { background: #a478b1; }
57: .preview-code { padding: 28px 16px; display: grid; grid-template-columns: 27px 1fr; column-gap: 14px; font: 11px/2.15 var(--mono); color: #dbd3e4; overflow-x: auto; }
58: .preview-code > span { white-space: pre; }
59: .preview-code b { color: var(--accent); font-weight: 400; }
60: .line-number { color: #8f7e9e; text-align: right; }
61: .preview-flow { display: flex; align-items: center; justify-content: center; gap: 9px; border-top: 1px solid var(--line); margin-inline: 22px; padding-top: 25px; font: 11px var(--mono); }
62: .preview-flow span { padding: 10px; border: 1px solid #51445c; border-radius: 6px; color: var(--secondary); }
63: .preview-flow .last { background: #30233d; color: var(--accent-bright); border-color: #735392; }
64: .preview-flow b { color: #927ea2; font-weight: 400; }
65: .preview-caption { display: flex; align-items: center; justify-content: center; gap: 8px; padding: 20px; font-size: 10px; color: var(--muted); }
66: .preview-caption .status-dot { background: var(--green); }
67: .environment { border: 1px solid var(--line); border-radius: 8px; padding: 24px; display: flex; gap: 20px; align-items: center; background: #18141d; }
68: .environment-icon { color: var(--accent); font: 19px var(--mono); padding: 10px; background: #282030; border-radius: 7px; flex-shrink: 0; }
69: .environment strong { font-weight: 500; font-size: 14px; }
70: .environment p { color: var(--muted); font-size: 12px; margin-top: 3px; max-width: 690px; }
71: .environment b { font-weight: 400; color: var(--secondary); }
72: .environment a { margin-left: auto; flex-shrink: 0; font-size: 12px; text-decoration: none; }
73: .curriculum { padding-top: 67px; }
74: .section-heading { display: flex; align-items: end; justify-content: space-between; gap: 20px; margin-bottom: 28px; }
75: .section-heading .eyebrow { margin-bottom: 12px; }
76: h2 { font-size: clamp(26px, 2.6vw, 34px); }
77: .level { border: 1px solid var(--line); border-radius: 30px; padding: 5px 12px; font: 10px var(--mono); color: var(--muted); white-space: nowrap; }
78: .exercise-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
79: .exercise-card { text-decoration: none; color: var(--text); background: var(--panel); border: 1px solid var(--line); border-radius: 9px; padding: 24px; display: flex; flex-direction: column; min-height: 228px; transition: border-color .15s, background .15s; }
80: .exercise-card:hover { border-color: #9271b2; background: var(--panel-hover); }
81: .card-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 26px; }
82: .card-number { color: var(--accent); font: 13px var(--mono); }
83: .card-time { color: var(--muted); font: 10px var(--mono); }
84: .exercise-card h3 { font-size: 21px; letter-spacing: -.03em; margin-bottom: 12px; }
85: .exercise-card p { color: var(--secondary); font-size: 13px; line-height: 1.65; margin-bottom: 23px; }
86: .card-bottom { margin-top: auto; padding-top: 14px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; align-items: center; color: var(--muted); font: 10px var(--mono); gap: 12px; }
87: .card-bottom b { color: var(--accent); font-size: 17px; font-weight: 400; }
88: .exercise-card.featured { grid-column: 1 / -1; min-height: auto; display: grid; grid-template-columns: 150px 1fr 230px; gap: 24px; align-items: center; border-color: #594166; background: #211929; }
89: .featured .card-top, .featured p { margin: 0; }
90: .featured .card-top { flex-direction: column; align-items: start; gap: 12px; }
91: .featured .card-number { font-size: 30px; }
92: .featured .card-bottom { margin: 0; border: 0; padding: 0; }
93: .closing { margin-top: 68px; padding-block: 38px 60px; border-top: 1px solid var(--line); display: grid; grid-template-columns: 1fr 1fr; gap: 20px 60px; }
94: .closing .eyebrow { margin-bottom: 14px; }
95: .closing > p { color: var(--secondary); font-size: 15px; align-self: end; }
96: .closing > a { grid-column: 2; font-size: 12px; text-decoration: none; }
97: footer { border-top: 1px solid var(--line); padding-block: 26px; display: flex; justify-content: space-between; gap: 20px; color: var(--muted); font-size: 11px; }
98: footer div { display: flex; gap: 28px; }
99: footer a { color: var(--muted); text-decoration: none; }
100: .skip { position: absolute; top: -100px; left: 16px; background: var(--accent); color: var(--accent-dark); padding: 10px; z-index: 5; }
101: .skip:focus { top: 16px; }
102: 
103: /* Apresentação: mesmos conceitos, com espaço para a demonstração ao vivo. */
104: .lesson { padding-bottom: 26px; scroll-margin-top: 16px; }
105: .lesson + .lesson { border-top: 1px solid var(--line); }
106: .lesson > .eyebrow { margin-top: 24px; }
107: .lesson h2 { font-size: clamp(30px, 4vw, 48px); margin-bottom: 30px; }
108: .lesson-practice { margin-block: 40px; padding-top: 32px; border-top: 1px solid var(--line); }
109: .lesson-practice h3 { font-size: 22px; }
110: .lesson a, .lesson summary { overflow-wrap: anywhere; }
111: .lesson-details, .course-finish { margin-block: 32px; }
112: summary { cursor: pointer; color: var(--accent); font-weight: 500; }
113: summary::marker { color: var(--accent); }
114: details[open] > summary { margin-bottom: 18px; }
115: .lesson-details > p { margin-top: 18px; }
116: 
117: /* Links de âncora nativos preservam o histórico e a navegação pelo teclado.
118:    Sem :has(), todas as aulas continuam legíveis em uma única página. */
119: @supports selector(:has(*)) {
120:   @media screen {
121:     #deck:not(:has(> .lesson:target)) { display: none; }
122:     #deck:has(> .lesson:target) > .lesson:not(:target) { display: none; }
123:     main:has(> #deck > .lesson:target) > #home { display: none; }
124:     .lesson:target { border-top: 0; }
125:   }
126: }
127: 
128: .deck-top { display: flex; justify-content: space-between; gap: 15px; align-items: center; padding-block: 24px; color: var(--muted); font: 12px var(--mono); }
129: .back { text-decoration: none; }
130: .slide-columns { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: start; }
131: .slide-columns > * { min-width: 0; }
132: .slide-stack { display: grid; gap: 20px; }
133: .lead { font-size: clamp(18px, 2vw, 23px); line-height: 1.6; color: var(--secondary); }
134: .box { border: 1px solid var(--line); border-radius: 8px; background: var(--panel); padding: 23px; }
135: .box h3 { color: var(--accent); font-size: 18px; margin-bottom: 12px; letter-spacing: -.02em; }
136: .box p, .box li { font-size: 15px; color: var(--secondary); }
137: .box p + p { margin-top: 12px; }
138: .callout { border-left: 3px solid var(--accent); padding: 12px 20px; background: #231b2b; color: var(--secondary); font-size: 15px; }
139: pre { border: 1px solid var(--line); background: #0e0b12; border-radius: 8px; padding: 22px; overflow-x: auto; font: 13px/1.8 var(--mono); margin: 0; color: #dfd3ed; }
140: code { font-family: var(--mono); }
141: p code, li code { color: var(--accent-bright); background: #2b2234; padding: 2px 5px; border-radius: 3px; font-size: .87em; overflow-wrap: anywhere; }
142: .flow { display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap; margin-block: 20px; }
143: .flow span { background: var(--panel); border: 1px solid #68517a; border-radius: 7px; padding: 16px; color: var(--accent); font: 14px var(--mono); }
144: .flow b { color: var(--muted); }
145: .task-list { padding-left: 24px; margin: 0; display: grid; gap: 14px; color: var(--secondary); }
146: .task-list li::marker { color: var(--accent); }
147: .deck-bottom { border-top: 1px solid var(--line); padding-block: 22px; display: flex; align-items: center; justify-content: space-between; gap: 20px; }
148: @media (max-width: 1050px) {
149:   .hero { gap: 26px; }
150:   .hero-actions { gap: 12px; }
151:   .stats { gap: 23px; }
152:   .preview-code { font-size: 10px; column-gap: 9px; }
153:   .environment a { display: none; }
154: }
155: @media (max-width: 800px) {
156:   .topbar, main, footer { padding-inline: 24px; }
157:   .hero { grid-template-columns: 1fr; padding-top: 50px; gap: 45px; }
158:   h1 { font-size: 46px; }
159:   .preview { max-width: 560px; transform: none; width: 100%; }
160:   .preview-code { font-size: 12px; }
161:   .exercise-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
162:   .exercise-card.featured { grid-template-columns: 70px 1fr; }
163:   .featured .card-bottom { grid-column: 2; }
164:   .slide-columns { grid-template-columns: 1fr; }
165:   .closing { column-gap: 25px; }
166: }
167: @media (max-width: 540px) {
168:   .topbar { height: 76px; }
169:   .topbar nav { gap: 12px; font-size: 11px; }
170:   .topbar nav a:first-child, .language { display: none; }
171:   .brand { font-size: 17px; gap: 8px; }
172:   h1 { font-size: 38px; }
173:   .hero { padding-block: 42px; }
174:   .hero .eyebrow { font-size: 9px; }
175:   .hero-description { font-size: 15px; }
176:   .stats { gap: 22px; }
177:   .stats span { font-size: 9px; }
178:   .preview-code { padding-inline: 8px; font-size: 9px; grid-template-columns: 19px 1fr; }
179:   .preview-bar { padding: 14px 10px; font-size: 8px; }
180:   .environment { padding: 18px; gap: 12px; align-items: start; }
181:   .environment-icon { font-size: 14px; padding: 6px; }
182:   .curriculum { padding-top: 45px; }
183:   .section-heading { display: block; }
184:   .section-heading h2 { margin-bottom: 20px; }
185:   .eyebrow { font-size: 9px; }
186:   .exercise-grid { grid-template-columns: 1fr; }
187:   .exercise-card { min-height: 210px; }
188:   .exercise-card.featured { grid-template-columns: 45px 1fr; gap: 15px; }
189:   .closing { grid-template-columns: 1fr; margin-top: 44px; padding-bottom: 40px; }
190:   .closing > a { grid-column: 1; }
191:   footer { flex-direction: column; }
192:   footer div { gap: 15px; }
193:   .deck-top { font-size: 10px; }
194:   .deck-top { flex-wrap: wrap; }
195:   .deck-bottom { flex-wrap: wrap; gap: 12px; }
196:   .deck-bottom .button { flex: 1 1 150px; text-align: center; }
197:   .deck-bottom .button { font-size: 12px; padding: 11px 14px; }
198:   pre { padding: 16px; font-size: 11px; }
199: }
200: @media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition: none !important; } }

(End of file - total 200 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/tests/apresentacao.py"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/tests/apresentacao.py</path>
<type>file</type>
<content>
1: """Confere o conteúdo estático e os destinos da navegação da apresentação."""
2: 
3: from html.parser import HTMLParser
4: from pathlib import Path
5: from urllib.parse import unquote, urlsplit
6: 
7: CURSO = Path(__file__).resolve().parent.parent
8: PAGINA = CURSO / "docs/index.html"
9: 
10: 
11: class Apresentacao(HTMLParser):
12:     def __init__(self):
13:         super().__init__()
14:         self.elementos = []
15:         self.pilha = []
16: 
17:     def handle_starttag(self, tag, attrs):
18:         elemento = {"tag": tag, "attrs": dict(attrs), "texto": ""}
19:         self.elementos.append(elemento)
20:         if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input",
21:                        "link", "meta", "param", "source", "track", "wbr"}:
22:             self.pilha.append(elemento)
23: 
24:     def handle_endtag(self, tag):
25:         assert self.pilha and self.pilha[-1]["tag"] == tag, f"Fechamento HTML incorreto: {tag}"
26:         self.pilha.pop()
27: 
28:     def handle_data(self, data):
29:         for elemento in self.pilha:
30:             elemento["texto"] += data
31: 
32:     def com_classe(self, classe):
33:         return [e for e in self.elementos if classe in e["attrs"].get("class", "").split()]
34: 
35: 
36: pagina = Apresentacao()
37: pagina.feed(PAGINA.read_text(encoding="utf-8"))
38: pagina.close()
39: assert not pagina.pilha, "Há elementos HTML sem fechamento."
40: ids = [e["attrs"]["id"] for e in pagina.elementos if "id" in e["attrs"]]
41: assert len(ids) == len(set(ids)), "IDs duplicados na apresentação."
42: assert not any(e["tag"] == "script" for e in pagina.elementos), "A apresentação deve funcionar sem scripts."
43: 
44: links = []
45: for elemento in pagina.elementos:
46:     attrs = elemento["attrs"]
47:     for referencia in attrs.get("aria-labelledby", "").split():
48:         assert referencia in ids, f"Título acessível inexistente: {referencia}"
49:     for atributo in ("href", "src"):
50:         if atributo not in attrs:
51:             continue
52:         link = attrs[atributo]
53:         links.append(link)
54:         url = urlsplit(link)
55:         if not url.scheme and not url.netloc:
56:             if url.path:
57:                 assert (PAGINA.parent / unquote(url.path)).is_file(), f"Arquivo ausente: {link}"
58:             elif url.fragment:
59:                 assert unquote(url.fragment) in ids, f"Âncora quebrada: {link}"
60: 
61: destinos = [f"exercicio-{n:02d}" for n in range(1, 8)]
62: aulas = pagina.com_classe("lesson")
63: assert [e["attrs"]["id"] for e in aulas] == ["intro", *destinos]
64: assert [e["attrs"]["href"] for e in pagina.com_classe("exercise-card")] == [f"#{d}" for d in destinos]
65: tempos = [int(e["texto"].removesuffix(" min")) for e in pagina.com_classe("card-time")]
66: assert len(tempos) == 7 and sum(tempos) == 155
67: for card, aula, tempo in zip(pagina.com_classe("exercise-card"), aulas[1:], tempos):
68:     titulo = next(e["texto"] for e in pagina.elementos if e["attrs"].get("id") == aula["attrs"]["aria-labelledby"])
69:     assert titulo in card["texto"] and "Codespaces" in aula["texto"]
70:     assert f"{tempo} minutos" in aula["texto"]
71: print("✅ Apresentação estática: 7 exercícios, 155 minutos, títulos e links de navegação válidos.")

(End of file - total 71 lines)
</content>
```

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://raw.githubusercontent.com/fsilva-alt/devops-git/main/docs/index.html",
  "format": "text"
}
```

**Output:**
```
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--ARTIFACT-START-->
<title>Git no Codespaces</title>
<meta name="description" content="Slides do curso de Git no GitHub Codespaces: 17 desafios, conceitos, diagramas e links de documentação.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  --bg:#0A0F1F; --panel:#0F162C; --panel-2:#141D38; --ink:#E9EDF8; --ink-2:#C3CBE3; --muted:#8792B3;
  --blue:#1428A0; --aqua:#3ED6E4; --aqua-ink:#062B33; --aqua-soft:rgba(62,214,228,.10);
  --line:#1F2946; --line-2:#2B3760; --amber:#F2B95C; --red:#F08A8A; --green:#7ADFB0;
  --display:"Manrope","IBM Plex Sans","Segoe UI",Helvetica,Arial,sans-serif;
  --body:"IBM Plex Sans","Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:"IBM Plex Mono","JetBrains Mono",Menlo,Consolas,monospace;
  --r:10px; --r-s:6px;
  --gutter:clamp(20px,4vw,56px);
  color-scheme:dark;
}
*{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:clamp(15px,1.12vw,18.5px);line-height:1.6;min-height:100vh;-webkit-font-smoothing:antialiased}
a{color:var(--aqua)}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--aqua);outline-offset:3px;border-radius:var(--r-s)}
code,pre,kbd{font-family:var(--mono)}
code{background:var(--panel-2);border-radius:4px;padding:.08em .4em;font-size:.9em;color:var(--aqua);white-space:nowrap}
h1,h2,h3{font-family:var(--display);font-weight:600;letter-spacing:-.015em;line-height:1.15;margin:0;text-wrap:balance}
p{margin:0}
strong{font-weight:600;color:var(--ink)}
::selection{background:var(--aqua);color:var(--aqua-ink)}
.mono{font-family:var(--mono)}
.up{font-family:var(--mono);text-transform:uppercase;letter-spacing:.1em;font-size:.7em;color:var(--muted)}
.hidden{display:none!important}

/* ---------- Home ---------- */
#home{padding:var(--gutter);padding-block:clamp(32px,6vh,80px);max-width:1280px;margin:0 auto}
.hero{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end;padding-bottom:clamp(24px,4vh,40px);border-bottom:1px solid var(--line)}
.hero h1{font-size:clamp(38px,5.5vw,72px);font-weight:700;line-height:1.02}
.hero h1 span{display:block;color:var(--aqua);font-weight:500}
.hero .sub{color:var(--ink-2);max-width:58ch;margin-top:18px;font-size:1.05em}
.hero .meta{display:flex;gap:28px;font-family:var(--mono);font-size:.78em;color:var(--muted);text-align:left}
.hero .meta b{display:block;color:var(--ink);font-size:1.9em;font-family:var(--display);font-weight:600;line-height:1.1;margin-bottom:2px}
.legend{display:flex;flex-wrap:wrap;gap:10px 28px;margin:24px 0 20px;font-family:var(--mono);font-size:.78em;color:var(--muted);align-items:center}
.legend .sw{display:inline-block;width:10px;height:10px;border-radius:3px;background:var(--line-2);vertical-align:0;margin-right:8px}
.legend .sw.el{background:var(--amber)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.tile{position:relative;display:grid;grid-template-rows:auto 1fr auto;gap:14px;border:1px solid var(--line);border-radius:var(--r);background:var(--panel);padding:20px;color:var(--ink);text-decoration:none;min-height:180px;transition:border-color .15s ease,background .15s ease}
.tile:hover,.tile:focus-visible{border-color:var(--aqua);background:var(--panel-2);outline:none}
.tile .num{font-family:var(--mono);font-size:.82em;color:var(--aqua);letter-spacing:.06em}
.tile .row{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.tile .mod{font-family:var(--mono);font-size:.68em;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);text-align:right;line-height:1.4}
.tile h3{font-size:clamp(18px,1.4vw,21px);font-weight:600;line-height:1.25}
.tile .cmds{font-family:var(--mono);font-size:.76em;color:var(--muted);line-height:1.6}
.tile .foot{display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:12px;font-family:var(--mono);font-size:.72em;color:var(--muted)}
.tile.el::after{content:"";position:absolute;top:22px;right:20px;width:8px;height:8px;border-radius:50%;background:var(--amber)}
.tile.el .mod{padding-right:16px}
.homefoot{margin-top:40px;display:flex;flex-wrap:wrap;gap:10px 32px;font-family:var(--mono);font-size:.76em;color:var(--muted);border-top:1px solid var(--line);padding-top:18px}
.homefoot a{color:var(--ink-2)}
kbd{display:inline-block;border:1px solid var(--line-2);border-radius:4px;padding:0 6px;font-size:.9em;color:var(--ink-2);line-height:1.6;margin:0 2px;background:var(--panel)}

/* ---------- Deck ---------- */
#deck{min-height:100vh;display:grid;grid-template-rows:auto 1fr auto;grid-template-columns:minmax(0,1fr)}
.rail{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px var(--gutter);border-bottom:1px solid var(--line);background:rgba(10,15,31,.92);backdrop-filter:blur(8px);font-family:var(--mono);font-size:.78em;position:sticky;top:0;z-index:5}
.rail.bottom{border-bottom:0;border-top:1px solid var(--line);position:sticky;bottom:0}
.rail .crumb{color:var(--muted);text-align:center;flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rail .crumb b{color:var(--ink-2);font-weight:500}
.btn{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line-2);border-radius:var(--r-s);background:transparent;color:var(--ink-2);font-family:var(--mono);font-size:1em;padding:8px 14px;cursor:pointer;text-decoration:none;transition:border-color .15s,color .15s,background .15s;white-space:nowrap}
.btn:hover{border-color:var(--aqua);color:var(--aqua)}
.btn.primary{background:var(--aqua);color:var(--aqua-ink);border-color:var(--aqua)}
.btn.primary:hover{background:#63E0EB;color:var(--aqua-ink)}
.btn[disabled]{opacity:.3;pointer-events:none}
.counter{font-variant-numeric:tabular-nums;color:var(--muted)}
.dots{display:flex;gap:6px}
.dots i{width:18px;height:3px;border-radius:2px;background:var(--line-2);display:block}
.dots i.on{background:var(--aqua)}
.slide{padding:clamp(28px,5vh,56px) var(--gutter);max-width:1200px;margin:0 auto;width:100%;animation:in .25s ease}
@keyframes in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.slide,.tile,.btn{animation:none;transition:none}}
.slide .eyebrow{font-family:var(--mono);font-size:.74em;text-transform:uppercase;letter-spacing:.12em;color:var(--aqua);margin-bottom:12px}
.slide h2{font-size:clamp(26px,3.4vw,44px);margin-bottom:clamp(20px,3.5vh,36px);font-weight:600}
.slide h3{font-size:clamp(15px,1.15vw,17px);font-weight:600;letter-spacing:0;margin-bottom:10px;color:var(--ink)}
.lead{font-size:clamp(17px,1.45vw,22px);max-width:60ch;line-height:1.5;color:var(--ink-2);font-weight:400}
.lead strong,.lead em{color:var(--ink)}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:clamp(16px,2vw,28px);align-items:start}
.cols.w2{grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))}
.cols.s2{grid-template-columns:minmax(0,1.2fr) minmax(0,1fr)}
@media (max-width:820px){.cols.s2{grid-template-columns:1fr}}
/* minmax(0,…) e min-width:0: uma linha longa de comando rola dentro do bloco em vez de alargar a coluna */
.cols>*{min-width:0}
.stack{display:grid;grid-template-columns:minmax(0,1fr);gap:clamp(14px,2vh,22px)}
.box{border:1px solid var(--line);border-radius:var(--r);background:var(--panel);padding:clamp(16px,1.6vw,22px)}
.box.lift{border-color:var(--line-2);background:var(--panel-2)}
.box.soft{background:transparent}
.box p{color:var(--ink-2)}
.box p+p{margin-top:.6em}
.callout{border-left:2px solid var(--aqua);padding:4px 0 4px 16px;color:var(--ink-2)}
.callout.warn{border-left-color:var(--amber)}
.callout.warn strong{color:var(--amber)}
.callout strong{color:var(--aqua)}
pre.cmd{margin:0;background:#070B18;border:1px solid var(--line);border-radius:var(--r-s);padding:14px 16px;font-size:clamp(13px,1vw,15.5px);line-height:1.6;overflow-x:auto;color:var(--ink)}
pre.cmd .p{color:var(--aqua);user-select:none}
pre.cmd .c{color:var(--muted)}
pre.cmd .o{color:var(--muted)}
pre.cmd .add{color:var(--green)}
pre.cmd .del{color:var(--red)}
pre.cmd .mk{color:var(--amber)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-family:var(--mono);font-size:.76em;border:1px solid var(--line-2);border-radius:999px;color:var(--ink-2);padding:4px 12px;background:transparent}
.chip.amber{border-color:var(--amber);color:var(--amber)}
.steps{list-style:none;margin:0;padding:0;display:grid;gap:14px;counter-reset:s}
.steps li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:12px;align-items:start;counter-increment:s}
.steps li::before{content:counter(s);font-family:var(--mono);font-size:.8em;color:var(--aqua);border:1px solid var(--line-2);border-radius:50%;width:24px;height:24px;display:grid;place-items:center;margin-top:3px}
.steps li .t{margin-bottom:8px;color:var(--ink-2)}
.steps li>div{color:var(--ink-2)}
.steps pre.cmd{padding:10px 14px}
table.kv{width:100%;border-collapse:collapse;font-size:.94em}
table.kv th,table.kv td{text-align:left;padding:10px 10px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2)}
table.kv tr:last-child td{border-bottom:0}
table.kv th{font-family:var(--mono);font-weight:400;text-transform:uppercase;letter-spacing:.1em;font-size:.7em;color:var(--muted)}
table.kv th:empty{padding:0;border:0}
table.kv td:first-child{font-family:var(--mono);color:var(--aqua);white-space:nowrap;font-size:.9em}
.tw{overflow-x:auto}
ul.links{list-style:none;margin:0;padding:0;display:grid;gap:10px}
ul.links li{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:baseline}
ul.links li::before{content:"↗";color:var(--muted);font-family:var(--mono);font-size:.9em}
ul.links a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line-2)}
ul.links a:hover{color:var(--aqua);border-bottom-color:var(--aqua)}
ul.links small{display:block;color:var(--muted);font-family:var(--mono);font-size:.76em;margin-top:2px}
ul.plain{margin:0;padding-left:1.1em;display:grid;gap:6px;color:var(--ink-2)}
.big{font-family:var(--mono);font-size:.8em;color:var(--aqua);letter-spacing:.1em}
.big::before{content:"Desafio "}
details{border:1px solid var(--line-2);border-radius:var(--r);padding:12px 16px}
details summary{cursor:pointer;font-family:var(--mono);color:var(--amber);letter-spacing:.04em;font-size:.8em}
details[open] summary{margin-bottom:10px}

/* Flow diagrams (three areas etc.) */
.flow{display:flex;flex-wrap:wrap;align-items:stretch;gap:10px;justify-content:center}
.flow .node{flex:1 1 150px;min-width:150px;border:1px solid var(--line-2);border-radius:var(--r);background:var(--panel);padding:14px;display:grid;gap:4px;align-content:center;text-align:center}
.flow .node b{font-family:var(--display);font-weight:600;font-size:.98em;color:var(--ink)}
.flow .node small{color:var(--muted);font-family:var(--mono);font-size:.72em;line-height:1.4}
.flow .node.hi{border-color:var(--aqua);background:var(--aqua-soft)}
.flow .node.dim{border-color:var(--line);color:var(--muted)}
.flow .arr{flex:0 0 auto;display:grid;place-items:center;font-family:var(--mono);font-size:.72em;color:var(--muted);text-align:center;padding:0 6px;gap:2px}
.flow .arr strong{color:var(--aqua);font-weight:500}
.flow .arr .a{font-size:1.6em;line-height:1;color:var(--aqua)}
.flow .arr.back .a{color:var(--amber)}
.flow.vert{flex-direction:column}
.flow.vert .node{flex-basis:auto}
@media (max-width:640px){.flow{flex-direction:column}.flow .arr .a{transform:rotate(90deg)}}

/* SVG commit graphs */
svg.graph{width:100%;height:auto;display:block;max-width:100%;font-family:var(--mono)}
svg.graph .e{stroke:var(--line-2);stroke-width:2;fill:none}
svg.graph .e.dim{stroke:var(--line);stroke-dasharray:5 6}
svg.graph .e.hi{stroke:var(--aqua)}
svg.graph .c circle{fill:var(--panel-2);stroke:var(--ink-2);stroke-width:2}
svg.graph .c.hi circle{fill:var(--aqua);stroke:var(--aqua)}
svg.graph .c.hi text{fill:var(--aqua-ink)}
svg.graph .c.ghost circle{stroke:var(--line-2);stroke-dasharray:4 4;fill:transparent}
svg.graph .c.ghost text{fill:var(--muted)}
svg.graph .c.bad circle{stroke:var(--amber)}
svg.graph .c.merge circle{fill:var(--blue);stroke:var(--blue)}
svg.graph .c text{fill:var(--ink);font-size:12.5px;text-anchor:middle;font-weight:500}
svg.graph .cap{fill:var(--muted);font-size:12px;text-anchor:middle}
svg.graph .ref rect{fill:var(--panel);stroke:var(--line-2);stroke-width:1;rx:6}
svg.graph .ref text{fill:var(--ink-2);font-size:12.5px;text-anchor:middle;font-weight:500}
svg.graph .ref.head rect{fill:var(--aqua);stroke:var(--aqua)}
svg.graph .ref.head text{fill:var(--aqua-ink)}
svg.graph .ref.remote rect{fill:var(--blue);stroke:var(--blue)}
svg.graph .ref.remote text{fill:var(--ink)}
svg.graph .ref.dead rect{stroke:var(--line);fill:transparent;stroke-dasharray:4 4}
svg.graph .ref.dead text{fill:var(--muted)}
svg.graph .ref line{stroke:var(--line-2);stroke-width:1.5}
svg.graph .ref.head line{stroke:var(--aqua)}
svg.graph .tag{fill:var(--amber);font-size:12px;text-anchor:middle;font-weight:500}
.gwrap{border:1px solid var(--line);border-radius:var(--r);background:var(--panel);padding:12px 14px}
.gwrap .cap{font-family:var(--mono);font-size:.72em;color:var(--muted);letter-spacing:.04em;margin-bottom:6px}
</style>
</head>
<body>
<main id="home"></main>
<main id="deck" class="hidden">
  <div class="rail">
    <a class="btn" href="#/" id="btnHome">← Desafios</a>
    <div class="crumb" id="crumb"></div>
    <div class="counter" id="counter"></div>
  </div>
  <section class="slide" id="slide"></section>
  <div class="rail bottom">
    <button class="btn" id="btnPrev">← Anterior</button>
    <div class="dots" id="dots"></div>
    <button class="btn primary" id="btnNext">Próximo →</button>
  </div>
</main>

<script>
/* ---------- helpers ---------- */
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');

// Command block: lines starting with "$ " become prompt lines; "# " comment lines; "+ "/"- " diff lines; "<<<"/"==="/">>>" markers.
function cmd(text){
  const lines = text.replace(/^\n/,'').replace(/\n\s*$/,'').split('\n');
  return '<pre class="cmd">' + lines.map(l=>{
    if (l.startsWith('$ ')) return '<span class="p">$ </span>' + esc(l.slice(2));
    if (/^\s*#/.test(l)) return '<span class="c">' + esc(l) + '</span>';
    if (/^(<<<<<<<|=======|>>>>>>>)/.test(l)) return '<span class="mk">' + esc(l) + '</span>';
    if (l.startsWith('+ ') || l.startsWith('+')) return '<span class="add">' + esc(l) + '</span>';
    if (l.startsWith('- ')) return '<span class="del">' + esc(l) + '</span>';
    if (l.startsWith('> ')) return '<span class="o">' + esc(l.slice(2)) + '</span>';
    return esc(l);
  }).join('\n') + '</pre>';
}

// Commit graph as SVG.
// spec = { commits:[{id,x,y,label?,cls?}], edges:[[child,parent,cls?]], refs:[{name,at,cls?,below?}], caps:[{at,text}], cap? }
function graph(spec){
  const CX=118, CY=88, R=17, PX=70, RH=26, GAP=8, STEP=RH+GAP;
  const cs = spec.commits, refs = spec.refs||[], caps = spec.caps||[], tags = spec.tags||[];
  const cols = Math.max(...cs.map(c=>c.x))+1, rows = Math.max(...cs.map(c=>c.y))+1;
  // how many labels stack above / below each commit, to size the padding and place captions
  const up = {}, down = {};
  for (const r of refs){ const k = r.at; if (r.below) down[k]=(down[k]||0)+1; else up[k]=(up[k]||0)+1; }
  const maxUp = Math.max(0, ...Object.values(up)), maxDown = Math.max(0, ...Object.values(down));
  const hasCap = caps.length || tags.length;
  const PT = 20 + R + (maxUp ? 10 + maxUp*STEP : 0);
  const PB = R + (maxDown ? 10 + maxDown*STEP : 0) + (hasCap ? 30 : 0) + 16;
  const W = PX*2 + (cols-1)*CX, H = PT + (rows-1)*CY + PB;
  const pos = id => { const c = cs.find(c=>c.id===id); return [PX + c.x*CX, PT + c.y*CY]; };
  let edges = '', nodes = '', lines = '', labels = '', text = '';
  for (const e of (spec.edges||[])){
    const [x1,y1]=pos(e[0]), [x2,y2]=pos(e[1]);
    const d = y1===y2 ? `M${x1},${y1} L${x2},${y2}` : `M${x1},${y1} C${(x1+x2)/2},${y1} ${(x1+x2)/2},${y2} ${x2},${y2}`;
    edges += `<path d="${d}" class="e ${e[2]||''}"/>`;
  }
  for (const c of cs){
    const [x,y]=pos(c.id);
    nodes += `<g class="c ${c.cls||''}"><circle cx="${x}" cy="${y}" r="${R}"/><text x="${x}" y="${y+5}">${esc(c.label||c.id)}</text></g>`;
  }
  // labels: connector lines go in their own layer, under every label box
  const seenUp = {}, seenDown = {};
  for (const r of refs){
    const [x,y]=pos(r.at), k = r.at;
    let top;
    if (r.below){ const i = seenDown[k]=(seenDown[k]||0); seenDown[k]++; top = y + R + 10 + i*STEP; }
    else { const i = seenUp[k]=(seenUp[k]||0); seenUp[k]++; top = y - R - 10 - RH - i*STEP; }
    const w = r.name.length*8 + 22;
    const ly1 = r.below ? y+R : y-R, ly2 = r.below ? top : top+RH;
    lines += `<g class="ref ${r.cls||''}"><line x1="${x}" y1="${ly1}" x2="${x}" y2="${ly2}"/></g>`;
    labels += `<g class="ref ${r.cls||''}"><rect x="${x-w/2}" y="${top}" width="${w}" height="${RH}"/><text x="${x}" y="${top+18}">${esc(r.name)}</text></g>`;
  }
  // captions sit under the commit, or under its lower labels when it has any
  const capY = k => { const [,y]=pos(k); return y + R + 20 + (down[k] ? 10 + down[k]*STEP - 8 : 0); };
  for (const c of caps) text += `<text class="cap" x="${pos(c.at)[0]}" y="${capY(c.at)}">${esc(c.text)}</text>`;
  for (const t of tags) text += `<text class="tag" x="${pos(t.at)[0]}" y="${capY(t.at)}">${esc(t.text)}</text>`;
  return `<div class="gwrap">${spec.cap?`<div class="cap">${spec.cap}</div>`:''}<svg class="graph" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(spec.alt||'Grafo de commits')}">${edges}${lines}${nodes}${labels}${text}</svg></div>`;
}

// Simple linear chain helper: ids in order, all on row y.
function chain(ids, y=0, x0=0){ return ids.map((id,i)=>({id, x:x0+i, y})); }
function link(ids){ const e=[]; for(let i=1;i<ids.length;i++) e.push([ids[i],ids[i-1]]); return e; }

function docs(items){
  return '<ul class="links">' + items.map(i=>`<li><div><a href="${i.href}" target="_blank" rel="noopener">${i.t}</a>${i.s?`<small>${i.s}</small>`:''}</div></li>`).join('') + '</ul>';
}
function kv(rows, head=['Comando','Para quê']){
  return `<div class="tw"><table class="kv"><thead><tr>${head.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>` +
    rows.map(r=>`<tr>${r.map((c,i)=>`<td>${i===0?`<code>${esc(c)}</code>`:c}</td>`).join('')}</tr>`).join('') + '</tbody></table></div>';
}
function steps(items){ return '<ol class="steps">' + items.map(i=>`<li><div>${i}</div></li>`).join('') + '</ol>'; }
function chips(list, cls=''){ return `<div class="chips">${list.map(c=>`<span class="chip ${cls}">${esc(c)}</span>`).join('')}</div>`; }

// Standard cover slide for a desafio.
function cover(d, objetivo, onde, extra=''){
  return `<div class="cols s2"><div class="stack">
    <div class="big">${String(d.n).padStart(2,'0')}</div>
    <p class="lead">${objetivo}</p>
    ${chips(d.cmds)}
    ${extra}
  </div><div class="stack">
    <div class="box lift"><h3>Onde</h3>${onde}</div>
    <div class="box soft"><h3>Ficha</h3>${kv([['⏱ tempo', `${d.time} min${d.el?' · <span class="chip amber">pode ficar para depois da aula</span>':''}`],['módulo', d.mod],['verificação', d.verificacao || `<code>check.sh ${String(d.n).padStart(2,'0')}</code>`]], ['',''])}</div>
  </div></div>`;
}
</script>
<script>
/* ---------- doc links (verificados) ---------- */
const PG = 'https://git-scm.com/book/pt-br/v2/';
const REF = c => `https://git-scm.com/docs/${c}/pt_BR`;
const GH = 'https://docs.github.com/pt/';
const L = {
  pg_vcs:      {t:'Pro Git · Sobre controle de versão', href:PG+'Primeiros-Passos-Sobre-Controle-de-Vers%c3%a3o', s:'git-scm.com/book · pt-br'},
  pg_oque:     {t:'Pro Git · O que é Git?', href:PG+'Primeiros-Passos-O-que-%c3%a9-Git%3F', s:'snapshots, integridade, os três estados'},
  pg_hist:     {t:'Pro Git · Uma breve história do Git', href:PG+'Primeiros-Passos-Uma-Breve-Hist%c3%b3ria-do-Git', s:'2005, kernel Linux, BitKeeper'},
  pg_config:   {t:'Pro Git · Configuração inicial do Git', href:PG+'Primeiros-Passos-Configura%c3%a7%c3%a3o-inicial-do-Git', s:'identidade, editor, níveis'},
  pg_obtendo:  {t:'Pro Git · Obtendo um repositório Git', href:PG+'Fundamentos-do-Git-Obtendo-um-Reposit%c3%b3rio-Git', s:'git init, git clone'},
  pg_gravando: {t:'Pro Git · Gravando alterações no repositório', href:PG+'Fundamentos-do-Git-Gravando-Altera%c3%a7%c3%b5es-no-Reposit%c3%b3rio', s:'status, add, diff, commit, .gitignore, rm'},
  pg_hist_c:   {t:'Pro Git · Visualizando o histórico de commits', href:PG+'Fundamentos-do-Git-Visualizando-o-Hist%c3%b3rico-de-Commits', s:'log e seus filtros'},
  pg_desfaz:   {t:'Pro Git · Desfazendo coisas', href:PG+'Fundamentos-do-Git-Desfazendo-Coisas', s:'amend, unstage, descartar mudanças'},
  pg_remotos:  {t:'Pro Git · Trabalhando com repositórios remotos', href:PG+'Fundamentos-do-Git-Trabalhando-com-Reposit%c3%b3rios-Remotos', s:'remote, fetch, pull, push'},
  pg_branch:   {t:'Pro Git · Branches em poucas palavras', href:PG+'Ramifica%c3%a7%c3%a3o-Branching-no-Git-Branches-em-Poucas-Palavras', s:'branch = ponteiro, HEAD'},
  pg_merge:    {t:'Pro Git · Branching e merging básicos', href:PG+'Ramifica%c3%a7%c3%a3o-Branching-no-Git-Ramifica%c3%a7%c3%a3o-Branching-e-Mesclagem-Merging-B%c3%a1sicas', s:'fast-forward, três vias, conflitos'},
  pg_gerbr:    {t:'Pro Git · Gerenciamento de branches', href:PG+'Ramifica%c3%a7%c3%a3o-Branching-no-Git-Gerenciamento-de-Branches', s:'branch -d, --merged'},
  pg_remotebr: {t:'Pro Git · Branches remotos', href:PG+'Ramifica%c3%a7%c3%a3o-Branching-no-Git-Branches-Remotos-Remote-Branches', s:'origin/main, tracking, upstream'},
  pg_stash:    {t:'Pro Git · Fazendo stash e limpando', href:PG+'Ferramentas-do-Git-Fazendo-Stash-e-Limpando', s:'stash push/pop/apply/list'},
  pg_stage:    {t:'Pro Git · Área de stage interativa', href:PG+'Ferramentas-do-Git-%c3%81rea-de-Stage-Interativa', s:'add -p, hunks'},
  pg_rev:      {t:'Pro Git · Seleção de revisão', href:PG+'Ferramentas-do-Git-Sele%c3%a7%c3%a3o-de-Revis%c3%a3o', s:'ranges: A..B, HEAD~, hashes'},
  pg_rewrite:  {t:'Pro Git · Reescrevendo o histórico', href:PG+'Ferramentas-do-Git-Reescrevendo-o-Hist%c3%b3rico', s:'por que amend é reescrita'},
  pg_refs:     {t:'Pro Git · Referências do Git (por dentro)', href:PG+'Git-Internals-Por-Dentro-do-Git-Refer%c3%aancias-do-Git', s:'.git/refs/heads/main é um arquivo com um hash'},
  pg_search:   {t:'Pro Git · Pesquisando (grep, log -S)', href:PG+'Ferramentas-do-Git-Pesquisando-Searching', s:'log -S, log -G, log -L'},
  pg_contrib:  {t:'Pro Git · GitHub: contribuindo para um projeto', href:PG+'GitHub-Contribuindo-para-um-Projeto', s:'fork, branch, pull request'},
  r_config:    {t:'Referência · git config', href:REF('git-config'), s:'manual, pt-BR'},
  r_init:      {t:'Referência · git init', href:REF('git-init')},
  r_status:    {t:'Referência · git status', href:REF('git-status')},
  r_add:       {t:'Referência · git add', href:REF('git-add'), s:'inclui -p / --patch'},
  r_commit:    {t:'Referência · git commit', href:REF('git-commit'), s:'-m, -a, --amend'},
  r_diff:      {t:'Referência · git diff', href:REF('git-diff'), s:'--staged'},
  r_log:       {t:'Referência · git log', href:REF('git-log'), s:'--oneline, --graph, -S, --author, -p, --stat'},
  r_show:      {t:'Referência · git show', href:REF('git-show')},
  r_blame:     {t:'Referência · git blame', href:REF('git-blame')},
  r_ignore:    {t:'Referência · gitignore', href:REF('gitignore'), s:'sintaxe dos padrões'},
  r_chk:       {t:'Referência · git check-ignore', href:REF('git-check-ignore')},
  r_rm:        {t:'Referência · git rm', href:REF('git-rm'), s:'--cached'},
  r_restore:   {t:'Referência · git restore', href:REF('git-restore'), s:'--staged, --source'},
  r_revert:    {t:'Referência · git revert', href:REF('git-revert')},
  r_branch:    {t:'Referência · git branch', href:REF('git-branch'), s:'-d, -D, -r, --merged'},
  r_switch:    {t:'Referência · git switch', href:REF('git-switch'), s:'-c'},
  r_merge:     {t:'Referência · git merge', href:REF('git-merge'), s:'--no-ff, --abort'},
  r_stash:     {t:'Referência · git stash', href:REF('git-stash')},
  r_fetch:     {t:'Referência · git fetch', href:REF('git-fetch')},
  r_pull:      {t:'Referência · git pull', href:REF('git-pull')},
  r_push:      {t:'Referência · git push', href:REF('git-push'), s:'-u / --set-upstream'},
  r_remote:    {t:'Referência · git remote', href:REF('git-remote'), s:'add, -v, set-url'},
  r_revs:      {t:'Referência · gitrevisions', href:REF('gitrevisions'), s:'A..B, HEAD~1, origin/main'},
  gh_about:    {t:'GitHub Docs · Sobre o Git', href:GH+'get-started/using-git/about-git', s:'Git vs GitHub, fluxo básico'},
  gh_email:    {t:'GitHub Docs · Definir o e-mail de commit', href:GH+'account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address'},
  gh_ignore:   {t:'GitHub Docs · Ignorando arquivos', href:GH+'get-started/git-basics/ignoring-files'},
  gh_tpl:      {t:'github/gitignore · modelos por linguagem', href:'https://github.com/github/gitignore', s:'Node, Python, Java…'},
  gh_newrepo:  {t:'GitHub Docs · Criar um novo repositório', href:GH+'repositories/creating-and-managing-repositories/creating-a-new-repository'},
  gh_addlocal: {t:'GitHub Docs · Adicionar código local ao GitHub', href:GH+'migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github', s:'remote add + push -u'},
  gh_conflict: {t:'GitHub Docs · Resolver conflito na linha de comando', href:GH+'pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line'},
  gh_pr:       {t:'GitHub Docs · Sobre pull requests', href:GH+'pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests'},
  gh_prnew:    {t:'GitHub Docs · Criar um pull request', href:GH+'pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request'},
  gh_prcom:    {t:'GitHub Docs · Comentar num pull request', href:GH+'pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request', s:'code review'},
  lgb:         {t:'Learn Git Branching (interativo, pt-BR)', href:'https://learngitbranching.js.org/?locale=pt_BR', s:'visualize branches e merges no navegador'},
  repo:        {t:'Repositório do curso', href:'https://github.com/fsilva-alt/devops-git', s:'enunciados, gabarito, guia do professor'},
};

/* ---------- three-areas diagram ---------- */
function areas(opts={}){
  const {hi=[], back=false} = opts;
  const n = (k,t,s)=>`<div class="node ${hi.includes(k)?'hi':''}"><b>${t}</b><small>${s}</small></div>`;
  return `<div class="flow">
    ${n('wd','Diretório de trabalho','os arquivos que você edita')}
    <div class="arr ${back?'back':''}"><span class="a">${back?'←':'→'}</span>${back?'git restore --staged':'git add'}</div>
    ${n('st','Staging area','o que entra no próximo commit')}
    <div class="arr ${back?'back':''}"><span class="a">${back?'←':'→'}</span>${back?'git restore':'git commit'}</div>
    ${n('repo','Repositório','.git — o histórico')}
  </div>`;
}

/* ---------- INTRO ---------- */
const INTRO = {
  n:'intro', key:'intro', title:'Antes de começar', short:'Introdução', mod:'Abertura', time:8, el:false, cmds:['história','o problema','Git ≠ GitHub'],
  slides:[
    {h:'O que é o Git?', eyebrow:'Introdução · 1 de 5', body:`
      <div class="cols s2"><div class="stack">
        <p class="lead">O Git é um sistema de <strong>controle de versão</strong>. Ele registra versões do projeto (<em>snapshots</em>), identifica quem fez cada mudança e quando, e permite que várias pessoas trabalhem no mesmo código.</p>
        <div class="box"><h3>Sem controle de versão</h3><pre class="cmd">relatorio.docx
relatorio-v2.docx
relatorio-v2-FINAL.docx
relatorio-v2-FINAL-revisado.docx
relatorio-v2-FINAL-revisado-AGORA-VAI.docx</pre></div>
      </div><div class="stack">
        <div class="box lift"><h3>Com Git</h3>${cmd(`$ git log --oneline
> 9f3e1a2 Corrige total da tabela 3
> 4b8c0d1 Adiciona seção de resultados
> 1a2b3c4 Cria esqueleto do relatório`)}
        <p style="margin-top:12px;color:var(--muted)">Cada linha representa um commit, com uma versão do projeto que você pode consultar depois.</p></div>
        <div class="callout"><strong>Distribuído</strong> significa que cada pessoa tem uma cópia completa do histórico na sua máquina e pode continuar trabalhando sem conexão com o servidor.</div>
      </div></div>`},
    {h:'Uma breve história', eyebrow:'Introdução · 2 de 5', body:`
      <div class="gwrap" style="margin-bottom:22px"><svg class="graph" viewBox="0 0 1000 150" role="img" aria-label="Linha do tempo: anos 1990 CVS e Subversion centralizados; 2002 kernel Linux adota BitKeeper; 2005 nasce o Git; 2008 GitHub; hoje padrão da indústria">
        <line x1="40" y1="80" x2="960" y2="80" class="e"/>
        <g class="c"><circle cx="110" cy="80" r="14"/><text x="110" y="85" style="font-size:11px">90s</text></g>
        <text class="cap" x="110" y="118">CVS · Subversion</text><text class="cap" x="110" y="134">centralizados</text>
        <g class="c"><circle cx="330" cy="80" r="14"/><text x="330" y="85" style="font-size:11px">02</text></g>
        <text class="cap" x="330" y="118">kernel Linux adota</text><text class="cap" x="330" y="134">o BitKeeper (proprietário)</text>
        <g class="c hi"><circle cx="550" cy="80" r="18"/><text x="550" y="85" style="font-size:12px">05</text></g>
        <text x="550" y="40" style="fill:var(--aqua);font-size:15px;font-weight:600;text-anchor:middle">abril de 2005 · nasce o Git</text>
        <text class="cap" x="550" y="120">licença do BitKeeper cai;</text><text class="cap" x="550" y="136">Linus escreve o Git em ~2 semanas</text>
        <g class="c"><circle cx="770" cy="80" r="14"/><text x="770" y="85" style="font-size:11px">08</text></g>
        <text class="cap" x="770" y="118">GitHub</text><text class="cap" x="770" y="134">hospedagem + pull requests</text>
        <g class="c merge"><circle cx="930" cy="80" r="14"/><text x="930" y="85" style="font-size:10px">hoje</text></g>
        <text class="cap" x="930" y="118">padrão de fato</text><text class="cap" x="930" y="134">da indústria</text>
      </svg></div>
      <div class="cols">
        <div class="box"><div class="up">até 2005</div><h3>Kernel Linux com BitKeeper</h3><p>O maior projeto de software livre do mundo usava uma ferramenta <em>proprietária</em> de graça. Em 2005 a empresa retirou a licença gratuita.</p></div>
        <div class="box lift"><div class="up">abril de 2005</div><h3>Linus Torvalds escreve o Git</h3><p>Em cerca de duas semanas, com três metas: ser <strong>rápido</strong>, ser <strong>distribuído</strong> e garantir a <strong>integridade</strong> do histórico (cada commit é identificado pelo hash do seu conteúdo).</p></div>
        <div class="box"><div class="up">2008 em diante</div><h3>GitHub e a adoção em massa</h3><p>Um site para hospedar repositórios Git e conversar sobre código (<em>pull requests</em>) transformou o Git no padrão de fato. Hoje é usado por praticamente toda a indústria.</p></div>
      </div>
      <div class="cols" style="margin-top:22px">
        <div class="callout"><strong>Curiosidade</strong> — "git" é gíria britânica para "pessoa desagradável". Linus disse que nomeia projetos em homenagem a si mesmo: primeiro o Linux, depois o Git.</div>
        <div class="callout"><strong>Sistemas centralizados</strong>, como CVS e Subversion, guardavam o histórico em um servidor e exigiam conexão para fazer commits. No Git, os commits são feitos localmente.</div>
      </div>`},
    {h:'Que problema o Git resolve', eyebrow:'Introdução · 3 de 5', body:`
      <div class="cols w2">
        <div class="box lift"><h3>Consultar o histórico</h3><p>O histórico registra quem mudou o quê e quando, junto com a mensagem de cada commit. Você pode recuperar as versões registradas enquanto esse histórico estiver disponível.</p></div>
        <div class="box"><h3>Trabalho em paralelo</h3><p>Com branches, várias pessoas podem trabalhar ao mesmo tempo, ou você pode manter tarefas separadas. Depois, as mudanças são integradas com <em>merge</em>.</p></div>
        <div class="box"><h3>Desfazer mudanças</h3><p>Você pode restaurar um arquivo ou reverter um commit ou merge, preservando o trabalho das outras pessoas.</p></div>
        <div class="box"><h3>Sincronizar máquinas</h3><p>Use <code>push</code>, <code>fetch</code> e <code>pull</code> para sincronizar seu repositório com o remoto. O trabalho local pode ser feito offline; a rede é necessária para a sincronização entre máquinas.</p></div>
      </div>`},
    {h:'O que o Git não resolve', eyebrow:'Introdução · 4 de 5', body:`
      <div class="cols w2">
        <div class="box"><h3>Uma cópia local não basta como backup</h3><p>Se o repositório só existe na sua máquina, você pode perder o histórico junto com ela. Mantenha uma cópia em outro lugar, como um remoto no GitHub.</p></div>
        <div class="box"><h3>Não entende o código</h3><p>O Git compara <strong>linhas de texto</strong>. Um merge sem conflito pode ainda assim quebrar o programa; quem garante que funciona são os testes e a revisão.</p></div>
        <div class="box"><h3>Conflitos exigem uma decisão</h3><p>Quando o Git não consegue integrar as alterações automaticamente, ele mostra as versões em conflito. Cabe à equipe decidir o conteúdo final.</p></div>
        <div class="box"><h3>Arquivos binários grandes</h3><p>Vídeos, PSDs e conjuntos de dados aumentam o tamanho do repositório e não geram diffs úteis. O Git foi projetado para texto; extensões como o Git LFS ajudam a lidar com arquivos grandes.</p></div>
        <div class="box"><h3>Publicação e execução dependem de outras ferramentas</h3><p>O <em>push</em>, por si só, não coloca um site no ar. Outras ferramentas fazem o deploy, o build e os testes, muitas vezes acionadas por mudanças no repositório.</p></div>
        <div class="box"><h3>Gestão do projeto</h3><p>Tarefas, prazos e prioridades são organizados em ferramentas como issues e quadros. O Git registra as versões dos arquivos do projeto.</p></div>
      </div>`},
    {h:'Git não é GitHub', eyebrow:'Introdução · 5 de 5', body:`
      <div class="cols s2">
        <div class="stack">
          <div class="flow">
            <div class="node hi"><b>Git</b><small>programa · roda no seu terminal · 2005 · software livre</small></div>
            <div class="arr"><span class="a">⇄</span>push / pull</div>
            <div class="node"><b>GitHub</b><small>site · hospeda repositórios Git · 2008 · empresa (Microsoft)</small></div>
          </div>
          ${kv([
            ['Git','Ferramenta de linha de comando que versiona arquivos. Funciona sem internet e sem GitHub.'],
            ['GitHub','Serviço na web que hospeda repositórios Git (os <em>remotos</em>) e oferece pull requests, revisão, issues, Actions, Pages e Codespaces.'],
            ['Alternativas','GitLab, Bitbucket, Gitea e Codeberg também hospedam repositórios Git. Os comandos Git continuam os mesmos ao trocar de serviço.'],
          ], ['','' ])}
        </div>
        <div class="stack">
          <div class="callout"><strong>Nesta aula</strong>, os desafios 1 a 13 usam o Git localmente no Codespace. No 14, você publica um repositório no GitHub; no 15, abre um pull request; no 16, contribui com outro projeto usando um fork.</div>
          <div class="callout"><strong>Codespace</strong> — é um VS Code com terminal Linux rodando num servidor do GitHub. Serve para não instalar nada; o Git que você usa lá é o mesmo do seu computador.</div>
          <div class="box soft"><h3>Para ler depois</h3>${docs([L.pg_vcs, L.pg_hist, L.pg_oque, L.gh_about])}</div>
        </div>
      </div>`},
  ]
};

/* ---------- DESAFIOS ---------- */
const D = [];

/* 0 */
D.push({n:0, key:'00', title:'Configure sua identidade', mod:'Abertura', time:3, el:false, cmds:['git config --global','user.name','user.email'],
  slides:[
    {h:'Configure sua identidade', body: cover({n:0,time:3,el:false,mod:'Abertura · feito junto com o professor',cmds:['git config --global user.name','git config --global user.email','git config --list --show-origin']},
      'Configurar o <strong>nome e o e-mail</strong> usados para identificar a autoria dos seus commits. O Git precisa desses dados para criar um commit.',
      '<p>Em <strong>qualquer pasta</strong>. A configuração é global: vale para todos os repositórios deste Codespace.</p>')},
    {h:'Três níveis de configuração', eyebrow:'Conceito', body:`
      <div class="cols s2"><div class="stack">
        <div class="flow vert">
          <div class="node dim"><b>--system</b><small>/etc/gitconfig · todos os usuários da máquina · quase nunca (precisa de sudo)</small></div>
          <div class="arr"><span class="a">↓</span>o mais específico tem prioridade</div>
          <div class="node hi"><b>--global</b><small>~/.gitconfig · todos os repositórios do seu usuário · <strong>o que vamos usar</strong></small></div>
          <div class="arr"><span class="a">↓</span></div>
          <div class="node"><b>--local</b><small>.git/config · só aquele repositório · outra identidade num projeto (e-mail do trabalho)</small></div>
        </div>
      </div><div class="stack">
        <div class="box"><h3>Ver de onde veio cada valor</h3>${cmd(`$ git config --list --show-origin
> file:/home/user/.gitconfig  user.name=Ana Lima
> file:/home/user/.gitconfig  user.email=ana@exemplo.pt
> file:.git/config            core.bare=false`)}</div>
        <div class="box soft"><h3>O instalador já deixou pronto</h3>${kv([
          ['init.defaultBranch=main','repositórios novos começam na branch <code>main</code>'],
          ['core.editor=code --wait','quando o Git precisa de uma mensagem, abre o VS Code em vez do Vim'],
          ['pull.rebase=false','<code>git pull</code> integra com um merge, como vamos aprender'],
          ['gh auth login / setup-git','login pelo navegador e credencial para publicar nos desafios 14–16'],
        ], ['Config','Para quê'])}</div>
      </div></div>`},
    {h:'Comandos & documentação', eyebrow:'Referência', body:`
      <div class="cols s2">
        ${kv([
          ['git config --global <chave> <valor>','grava no ~/.gitconfig'],
          ['git config <chave>','mostra o valor efetivo na pasta atual'],
          ['git config --global --list','lista a configuração global'],
          ['git config --list --show-origin','lista tudo, com o arquivo de origem'],
          ['git config --local --unset <chave>','remove uma chave do repositório'],
        ])}
        <div class="box soft"><h3>Documentação</h3>${docs([L.pg_config, L.r_config, L.gh_email])}</div>
      </div>`},
    {h:'O desafio', eyebrow:'Tarefa · 3 min', body:`
      <div class="cols s2"><div class="stack">${steps([
        `<div class="t">Nome (o seu, não o do exemplo):</div>${cmd('$ git config --global user.name "Fulano de Tal"')}`,
        `<div class="t">E-mail — <strong>o mesmo da conta GitHub</strong>, para os commits aparecerem no seu perfil:</div>${cmd('$ git config --global user.email fulanodetal@exemplo.pt')}`,
        `<div class="t">Confira o que ficou gravado:</div>${cmd('$ git config --global --list')}`,
      ])}</div><div class="stack">
        <div class="callout warn"><strong>A verificação recusa valores de exemplo:</strong> <code>Fulano de Tal</code>, <code>Seu Nome</code>, <code>voce@…</code>, <code>@exemplo.*</code>. Substitua esses valores pelos seus dados antes de executar os comandos.</div>
        <div class="box"><h3>Verificação</h3>${cmd('$ check.sh 00')}<p style="margin-top:10px;color:var(--muted)">Se errar o nome ou o e-mail, rode o comando de novo com o valor correto para substituir o anterior.</p></div>
        <div class="box soft"><h3>Missão extra · prioridade do --local</h3>${cmd(`$ git config --local user.email outro@exemplo.com
$ git config user.email          # sem nível: o que vale aqui
$ git config --global user.email # continua o seu
$ git config --local --unset user.email`)}</div>
      </div></div>`},
  ]});

/* 1 */
D.push({n:1, key:'01', title:'Meu primeiro repositório', mod:'Módulo 1 · Fundamentos', time:6, el:false, cmds:['git init','git status','git add','git commit'],
  slides:[
    {h:'Meu primeiro repositório', body: cover({n:1,time:6,el:false,mod:'Módulo 1 · Fundamentos',cmds:['git init','git status','git add','git commit -m','git log']},
      'Transformar uma pasta comum num repositório Git e fazer o primeiro commit. Você vai acompanhar os arquivos desde o estado <strong>não rastreado</strong>, passando pela <strong>staging area</strong>, até serem <strong>registrados no commit</strong>.',
      cmd('$ cd ~/labs/01-meu-primeiro-repositorio') + '<p style="margin-top:10px;color:var(--muted)">A pasta contém três receitas (<code>bolo-de-cenoura.md</code>, <code>brigadeiro.md</code>, <code>pao-de-queijo.md</code>). Ao executar <code>git status</code>, você verá que ela ainda não é um repositório.</p>')},
    {h:'Commit é uma foto', eyebrow:'Conceito · snapshots', body:`
      <div class="cols s2"><div class="stack">
        ${graph({cap:'cada commit aponta para o anterior (o pai)', commits:chain(['C1','C2','C3']), edges:link(['C1','C2','C3']),
          refs:[{name:'main',at:'C3'},{name:'HEAD',at:'C3',cls:'head'}],
          caps:[{at:'C1',text:'3 receitas'},{at:'C2',text:'+ canela'},{at:'C3',text:'+ sal'}]})}
        <p class="lead">Cada commit registra uma versão do projeto, como uma <strong>foto dos arquivos</strong> naquele instante. Também registra a autoria, a data, uma mensagem e a referência ao commit anterior.</p>
      </div><div class="stack">
        <div class="box"><h3>Anatomia de um commit</h3>${kv([
          ['hash','identificador calculado a partir do conteúdo (SHA-1, 40 caracteres; usamos os 7 primeiros)'],
          ['árvore','a foto: todos os arquivos daquele momento'],
          ['pai','o commit anterior (dois, se for um merge)'],
          ['autor · data','quem e quando — por isso o desafio 0'],
          ['mensagem','por que essa mudança existe'],
        ], ['Campo','O que é'])}</div>
        <div class="callout"><strong>Integridade</strong> — mudar um byte de qualquer coisa muda o hash. Um histórico Git não pode ser alterado sem deixar rastro.</div>
      </div></div>`},
    {h:'As três áreas', eyebrow:'Conceito · o modelo mental de toda a aula', body:`
      <div class="stack">
        ${areas({hi:['wd','st','repo']})}
        <div class="cols">
          <div class="box"><h3>Diretório de trabalho</h3><p>É a pasta em que você edita os arquivos. Eles podem estar <strong>untracked</strong> (não rastreados), <strong>modified</strong> (modificados) ou sem alterações em relação ao último commit.</p></div>
          <div class="box lift"><h3>Staging area</h3><p>É onde você prepara o próximo commit. <code>git add</code> copia o estado atual de um arquivo para essa área, permitindo escolher quais mudanças serão registradas.</p></div>
          <div class="box"><h3>Repositório</h3><p>A pasta <code>.git</code>: todos os commits, branches e configurações. <code>git commit</code> tira a foto do que está na staging.</p></div>
        </div>
        <div class="callout"><strong>Ciclo de vida de um arquivo</strong> — untracked → <code>add</code> → staged → <code>commit</code> → committed → você edita → modified → <code>add</code> → staged → …</div>
      </div>`},
    {h:'Comandos & documentação', eyebrow:'Referência', body:`
      <div class="cols s2">
        ${kv([
          ['git init','cria o .git na pasta atual; a pasta vira um repositório'],
          ['git status','o que está untracked, modified e staged'],
          ['git add <arquivo>','copia o arquivo para a staging area'],
          ['git add .','adiciona tudo o que mudou na pasta atual (e subpastas)'],
          ['git commit -m "msg"','tira a foto do que está na staging'],
          ['git log','o histórico, do mais novo para o mais antigo'],
        ])}
        <div class="box soft"><h3>Documentação</h3>${docs([L.pg_oque, L.pg_obtendo, L.pg_gravando, L.r_init, L.r_status, L.r_add, L.r_commit])}</div>
      </div>`},
    {h:'O desafio', eyebrow:'Tarefa · 6 min', body:`
      <div class="cols s2"><div class="stack">${steps([
        `<div class="t">Inicie o repositório e veja como o Git enxerga a pasta (três arquivos <em>untracked</em>):</div>${cmd('$ git init\n$ git status')}`,
        `<div class="t">Adicione <strong>um</strong> arquivo e rode <code>status</code> de novo: ele muda de seção.</div>${cmd('$ git add bolo-de-cenoura.md\n$ git status')}`,
        `<div class="t">Adicione os outros dois e faça o primeiro commit:</div>${cmd('$ git add .\n$ git commit -m "Cria o livro de receitas"')}`,
        `<div class="t">Árvore limpa e um commit no histórico:</div>${cmd('$ git status\n$ git log')}`,
      ])}</div><div class="stack">
        <div class="box"><h3>Verificação</h3>${cmd('$ check.sh 01')}<p style="margin-top:10px;color:var(--muted)">Aprova com ≥ 1 commit e árvore de trabalho limpa.</p></div>
        <div class="callout"><strong>Confira o <code>git status</code> depois de cada passo.</strong> Observe a passagem de <em>Untracked files</em> para <em>Changes to be committed</em> e, após o commit, a mensagem <em>nothing to commit</em>.</div>
        <div class="box soft"><h3>Missão extra</h3><p>Use <code>ls -a</code> para ver a pasta <code>.git</code>, que guarda os dados do repositório. Apagá-la deixa apenas os arquivos da pasta, sem o histórico Git. Mantenha-a para continuar o exercício.</p></div>
      </div></div>`},
  ]});

/* 2 */
D.push({n:2, key:'02', title:'Registrando mudanças', mod:'Módulo 2 · Registrando mudanças', time:6, el:false, cmds:['git diff','git diff --staged','git log --oneline'],
  slides:[
    {h:'Registrando mudanças', body: cover({n:2,time:6,el:false,mod:'Módulo 2 · Registrando mudanças',cmds:['git diff','git add','git diff --staged','git commit -m','git log --oneline']},
      'Praticar o ciclo <strong>editar → diff → add → diff --staged → commit</strong> e escrever mensagens que expliquem a mudança.',
      cmd('$ cd ~/labs/02-registrando-mudancas') + '<p style="margin-top:10px;color:var(--muted)">Um repositório com um único commit e as três receitas.</p>')},
    {h:'Dois diffs, duas perguntas', eyebrow:'Conceito', body:`
      <div class="stack">
        <div class="flow">
          <div class="node"><b>Diretório de trabalho</b><small>o que você editou</small></div>
          <div class="arr"><span class="a">⇄</span><strong>git diff</strong><br>"o que mudei e ainda não adicionei?"</div>
          <div class="node hi"><b>Staging area</b><small>o que vai para o commit</small></div>
          <div class="arr"><span class="a">⇄</span><strong>git diff --staged</strong><br>"o que exatamente vai entrar?"</div>
          <div class="node"><b>HEAD</b><small>o último commit</small></div>
        </div>
        <div class="cols s2">
          <div class="box">${cmd(`$ git diff
> diff --git a/bolo-de-cenoura.md b/bolo-de-cenoura.md
> @@ -8,3 +8,4 @@
>  - 2 xícaras de farinha de trigo
>  - 1 colher de sopa de fermento em pó
+ - 1 pitada de canela`)}</div>
          <div class="stack">
            <div class="callout"><strong>Depois do <code>git add</code></strong>, a mudança deste exemplo está na staging area: <code>git diff</code> fica vazio e <code>git diff --staged</code> passa a mostrá-la.</div>
            <div class="callout"><strong>Antes de fazer o commit</strong>, confira <code>git diff --staged</code> para revisar as mudanças que serão registradas.</div>
          </div>
        </div>
      </div>`},
    {h:'Mensagens que explicam', eyebrow:'Conceito · boa mensagem de commit', body:`
      <div class="cols s2"><div class="stack">
        <div class="box lift"><h3>Complete a frase "Este commit…"</h3><p class="lead"><em>Adiciona</em> canela ao bolo de cenoura<br><em>Corrige</em> temperatura do forno<br><em>Remove</em> ingrediente duplicado<br><em>Ajusta</em> porções do pão de queijo</p></div>
        ${kv([
          ['✓ curta e específica','primeira linha com até ~50 caracteres; o quê e, se couber, por quê'],
          ['✓ verbo no presente','"Adiciona", não "Adicionei" nem "Adicionando"'],
          ['✗ "ajustes"','não informa o que mudou e dificulta a consulta ao histórico'],
          ['✗ "wip", "teste", "asdf"','não descrevem a mudança; no desafio 5, você verá como isso dificulta a investigação'],
        ], ['','' ])}
      </div><div class="stack">
        <div class="box"><h3>Ver o histórico resumido</h3>${cmd(`$ git log --oneline
> 7d2e9b1 Ajusta tempo de forno do pão de queijo
> 3c4f8a0 Corrige quantidade de ovos
> a91b2c3 Adiciona canela ao bolo de cenoura
> 1f0e6d5 Cria o livro de receitas`)}</div>
        <div class="callout"><strong>Atalho</strong> — <code>git commit -am "..."</code> faz <code>add</code> e <code>commit</code> de uma vez, mas <strong>só para arquivos que o Git já rastreia</strong>. Arquivo novo continua precisando de <code>git add</code>.</div>
      </div></div>`},
    {h:'Comandos & documentação', eyebrow:'Referência', body:`
      <div class="cols s2">
        ${kv([
          ['git diff','diretório de trabalho × staging area'],
          ['git diff --staged','staging area × último commit (HEAD)'],
          ['git commit -m "msg"','commit do que está na staging'],
          ['git commit -am "msg"','add + commit, só de arquivos já rastreados'],
          ['git log --oneline','um commit por linha: hash curto + mensagem'],
          ['git log -p / --stat','com o diff completo / com o resumo por arquivo'],
        ])}
        <div class="box soft"><h3>Documentação</h3>${docs([L.pg_gravando, L.pg_hist_c, L.r_diff, L.r_commit, L.r_log])}</div>
      </div>`},
    {h:'O desafio', eyebrow:'Tarefa · 6 min', body:`
      <div class="cols s2"><div class="stack">${steps([

...84088 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to: /home/lse/.local/share/opencode/tool-output/tool_0fa09c3eb0019Dq3gSFg1oRrIG
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
```

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://raw.githubusercontent.com/fsilva-alt/devops-docker/main/docs/index.html",
  "format": "text"
}
```

**Output:**
```
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--ARTIFACT-START-->
<title>Docker no Codespaces</title>
<meta name="description" content="Aprenda Docker desde os primeiros comandos, com explicações em português e 18 exercícios no GitHub Codespaces. Não é preciso saber programar.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{
  --bg:#111214; --panel:#18191D; --panel-2:#1F2126; --ink:#F2F1EC; --ink-2:#C9C7BE; --muted:#8B8A82;
  --accent:#FF8C42; --accent-ink:#2A1200; --accent-soft:rgba(255,140,66,.12);
  --line:#2A2C33; --line-2:#3A3D46; --blue:#6FB1FF; --amber:#F2C14E; --red:#F07A7A; --green:#8FD9A8;
  --display:"Space Grotesk","Inter","Segoe UI",Helvetica,Arial,sans-serif;
  --body:"Inter","Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:"JetBrains Mono","IBM Plex Mono",Menlo,Consolas,monospace;
  --r:10px; --r-s:6px;
  --gutter:clamp(20px,4vw,56px);
  color-scheme:dark;
}
*{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:clamp(15px,1.12vw,18.5px);line-height:1.6;min-height:100vh;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:var(--r-s)}
code,pre,kbd{font-family:var(--mono)}
code{background:var(--panel-2);border-radius:4px;padding:.08em .4em;font-size:.9em;color:var(--accent);white-space:nowrap}
/* código longo (preparado em renderSlide) quebra só nos espaços em vez de vazar da caixa */
code.wrap{white-space:normal;-webkit-box-decoration-break:clone;box-decoration-break:clone}
code.wrap span{white-space:nowrap}
h1,h2,h3{font-family:var(--display);font-weight:600;letter-spacing:-.015em;line-height:1.15;margin:0;text-wrap:balance}
p{margin:0}
strong{font-weight:600;color:var(--ink)}
::selection{background:var(--accent);color:var(--accent-ink)}
.mono{font-family:var(--mono)}
.up{font-family:var(--mono);text-transform:uppercase;letter-spacing:.1em;font-size:.7em;color:var(--muted)}
.hidden{display:none!important}

/* ---------- Home ---------- */
#home{padding:var(--gutter);padding-block:clamp(32px,6vh,80px);max-width:1280px;margin:0 auto}
.hero{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end;padding-bottom:clamp(24px,4vh,40px);border-bottom:1px solid var(--line)}
.hero h1{font-size:clamp(38px,5.5vw,72px);font-weight:700;line-height:1.02}
.hero h1 span{display:block;color:var(--accent);font-weight:500}
.hero .sub{color:var(--ink-2);max-width:58ch;margin-top:18px;font-size:1.05em}
.hero .meta{display:flex;gap:28px;font-family:var(--mono);font-size:.78em;color:var(--muted);text-align:left}
.hero .meta b{display:block;color:var(--ink);font-size:1.9em;font-family:var(--display);font-weight:600;line-height:1.1;margin-bottom:2px}
.legend{display:flex;flex-wrap:wrap;gap:10px 28px;margin:24px 0 20px;font-family:var(--mono);font-size:.78em;color:var(--muted);align-items:center}
.legend .sw{display:inline-block;width:10px;height:10px;border-radius:3px;background:var(--line-2);vertical-align:0;margin-right:8px}
.legend .sw.el{background:var(--amber)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.tile{position:relative;display:grid;grid-template-rows:auto 1fr auto;gap:14px;border:1px solid var(--line);border-radius:var(--r);background:var(--panel);padding:20px;color:var(--ink);text-decoration:none;min-height:180px;transition:border-color .15s ease,background .15s ease}
.tile:hover,.tile:focus-visible{border-color:var(--accent);background:var(--panel-2);outline:none}
.tile .num{font-family:var(--mono);font-size:.82em;color:var(--accent);letter-spacing:.06em}
.tile .row{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.tile .mod{font-family:var(--mono);font-size:.68em;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);text-align:right;line-height:1.4}
.tile h3{font-size:clamp(18px,1.4vw,21px);font-weight:600;line-height:1.25}
.tile .cmds{font-family:var(--mono);font-size:.76em;color:var(--muted);line-height:1.6}
.tile .foot{display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:12px;font-family:var(--mono);font-size:.72em;color:var(--muted)}
.tile .optional{color:var(--amber)}
.homefoot{margin-top:40px;display:flex;flex-wrap:wrap;gap:10px 32px;font-family:var(--mono);font-size:.76em;color:var(--muted);border-top:1px solid var(--line);padding-top:18px}
.homefoot a{color:var(--ink-2)}
kbd{display:inline-block;border:1px solid var(--line-2);border-radius:4px;padding:0 6px;font-size:.9em;color:var(--ink-2);line-height:1.6;margin:0 2px;background:var(--panel)}

/* ---------- Deck ---------- */
#deck{min-height:100vh;display:grid;grid-template-rows:auto 1fr auto;grid-template-columns:minmax(0,1fr)}
.rail{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px var(--gutter);border-bottom:1px solid var(--line);background:rgba(17,18,20,.92);backdrop-filter:blur(8px);font-family:var(--mono);font-size:.78em;position:sticky;top:0;z-index:5}
.rail.bottom{border-bottom:0;border-top:1px solid var(--line);position:sticky;bottom:0}
.rail .crumb{color:var(--muted);text-align:center;flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rail .crumb b{color:var(--ink-2);font-weight:500}
.btn{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line-2);border-radius:var(--r-s);background:transparent;color:var(--ink-2);font-family:var(--mono);font-size:1em;padding:8px 14px;cursor:pointer;text-decoration:none;transition:border-color .15s,color .15s,background .15s;white-space:nowrap}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn.primary:hover{background:#FFA366;color:var(--accent-ink)}
.btn[disabled]{opacity:.3;pointer-events:none}
.counter{font-variant-numeric:tabular-nums;color:var(--muted)}
.dots{display:flex;gap:6px}
.dots i{width:18px;height:3px;border-radius:2px;background:var(--line-2);display:block}
.dots i.on{background:var(--accent)}
.slide{padding:clamp(28px,5vh,56px) var(--gutter);max-width:1200px;margin:0 auto;width:100%;animation:in .25s ease}
@keyframes in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.slide,.tile,.btn{animation:none;transition:none}}
.slide .eyebrow{font-family:var(--mono);font-size:.74em;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);margin-bottom:12px}
.slide h2{font-size:clamp(26px,3.4vw,44px);margin-bottom:clamp(20px,3.5vh,36px);font-weight:600}
.slide h3{font-size:clamp(15px,1.15vw,17px);font-weight:600;letter-spacing:0;margin-bottom:10px;color:var(--ink)}
.lead{font-size:clamp(17px,1.45vw,22px);max-width:60ch;line-height:1.5;color:var(--ink-2);font-weight:400}
.lead strong,.lead em{color:var(--ink)}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:clamp(16px,2vw,28px);align-items:start}
.cols.w2{grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))}
.cols.s2{grid-template-columns:minmax(0,1.2fr) minmax(0,1fr)}
@media (max-width:820px){.cols.s2{grid-template-columns:1fr}}
/* minmax(0,…) e min-width:0: uma linha longa de comando rola dentro do bloco em vez de alargar a coluna */
.cols>*{min-width:0}
.stack{display:grid;grid-template-columns:minmax(0,1fr);gap:clamp(14px,2vh,22px)}
.box{border:1px solid var(--line);border-radius:var(--r);background:var(--panel);padding:clamp(16px,1.6vw,22px)}
.box.lift{border-color:var(--line-2);background:var(--panel-2)}
.box.soft{background:transparent}
.box p{color:var(--ink-2)}
.box p+p{margin-top:.6em}
.callout{border-left:2px solid var(--accent);padding:4px 0 4px 16px;color:var(--ink-2)}
.callout.warn{border-left-color:var(--amber)}
.callout.warn strong{color:var(--amber)}
.callout strong{color:var(--accent)}
pre.cmd{margin:0;background:#0B0C0E;border:1px solid var(--line);border-radius:var(--r-s);padding:14px 16px;font-size:clamp(13px,1vw,15.5px);line-height:1.6;overflow-x:auto;color:var(--ink)}
pre.cmd .p{color:var(--accent);user-select:none}
pre.cmd .c{color:var(--muted)}
pre.cmd .o{color:var(--muted)}
pre.cmd .add{color:var(--green)}
pre.cmd .del{color:var(--red)}
pre.cmd .mk{color:var(--amber)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-family:var(--mono);font-size:.76em;border:1px solid var(--line-2);border-radius:999px;color:var(--ink-2);padding:4px 12px;background:transparent}
.chip.amber{border-color:var(--amber);color:var(--amber)}
.steps{list-style:none;margin:0;padding:0;display:grid;gap:14px;counter-reset:s}
.steps li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:12px;align-items:start;counter-increment:s}
.steps li::before{content:counter(s);font-family:var(--mono);font-size:.8em;color:var(--accent);border:1px solid var(--line-2);border-radius:50%;width:24px;height:24px;display:grid;place-items:center;margin-top:3px}
.steps li .t{margin-bottom:8px;color:var(--ink-2)}
.steps li>div{color:var(--ink-2)}
.steps pre.cmd{padding:10px 14px}
table.kv{width:100%;border-collapse:collapse;font-size:.94em}
table.kv th,table.kv td{text-align:left;padding:10px 10px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2)}
table.kv tr:last-child td{border-bottom:0}
table.kv th{font-family:var(--mono);font-weight:400;text-transform:uppercase;letter-spacing:.1em;font-size:.7em;color:var(--muted)}
table.kv th:empty{padding:0;border:0}
table.kv td:first-child{font-family:var(--mono);color:var(--accent);white-space:nowrap;font-size:.9em}
.tw{overflow-x:auto}
ul.links{list-style:none;margin:0;padding:0;display:grid;gap:10px}
ul.links li{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:baseline}
ul.links li::before{content:"↗";color:var(--muted);font-family:var(--mono);font-size:.9em}
ul.links a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line-2)}
ul.links a:hover{color:var(--accent);border-bottom-color:var(--accent)}
ul.links small{display:block;color:var(--muted);font-family:var(--mono);font-size:.76em;margin-top:2px}
ul.plain{margin:0;padding-left:1.1em;display:grid;gap:6px;color:var(--ink-2)}
.big{font-family:var(--mono);font-size:.8em;color:var(--accent);letter-spacing:.1em}
.big::before{content:"Exercício "}
details{border:1px solid var(--line-2);border-radius:var(--r);padding:12px 16px}
details summary{cursor:pointer;font-family:var(--mono);color:var(--amber);letter-spacing:.04em;font-size:.8em}
details[open] summary{margin-bottom:10px}

/* Flow diagrams (imagem → container, portas, redes) */
.flow{display:flex;flex-wrap:wrap;align-items:stretch;gap:10px;justify-content:center}
.flow .node{flex:1 1 150px;min-width:150px;border:1px solid var(--line-2);border-radius:var(--r);background:var(--panel);padding:14px;display:grid;gap:4px;align-content:center;text-align:center}
.flow .node b{font-family:var(--display);font-weight:600;font-size:.98em;color:var(--ink)}
.flow .node small{color:var(--muted);font-family:var(--mono);font-size:.72em;line-height:1.4}
.flow .node.hi{border-color:var(--accent);background:var(--accent-soft)}
.flow .node.blue{border-color:var(--blue)}
.flow .node.dim{border-color:var(--line);color:var(--muted)}
.flow .node.warn{border-color:var(--amber);border-style:dashed}
.flow .arr{flex:0 0 auto;display:grid;place-items:center;font-family:var(--mono);font-size:.72em;color:var(--muted);text-align:center;padding:0 6px;gap:2px}
.flow .arr strong{color:var(--accent);font-weight:500}
.flow .arr .a{font-size:1.6em;line-height:1;color:var(--accent)}
.flow .arr.back .a{color:var(--amber)}
.flow.vert{flex-direction:column}
.flow.vert .node{flex-basis:auto}
@media (max-width:640px){.flow{flex-direction:column}.flow .arr .a{transform:rotate(90deg)}}
/* a caixa "rede": um grupo de nós com borda tracejada e rótulo */
.netbox{border:1px dashed var(--line-2);border-radius:var(--r);padding:26px 14px 14px;position:relative;margin-top:10px}
.netbox::before{content:attr(data-label);position:absolute;top:-10px;left:14px;background:var(--bg);padding:0 8px;font-family:var(--mono);font-size:.72em;color:var(--accent);letter-spacing:.08em;text-transform:uppercase}

/* Camadas de imagem empilhadas */
.layers{border:1px solid var(--line);border-radius:var(--r);background:var(--panel);padding:12px 14px}
.layers .cap{font-family:var(--mono);font-size:.72em;color:var(--muted);letter-spacing:.04em;margin-bottom:8px}
.layers .stk{display:grid;gap:4px}
.layer{border:1px solid var(--line-2);border-radius:var(--r-s);background:var(--panel-2);padding:9px 14px;display:flex;justify-content:space-between;gap:12px;align-items:baseline}
.layer b{font-family:var(--mono);font-size:.84em;color:var(--ink);font-weight:500;white-space:nowrap}
.layer small{color:var(--muted);font-family:var(--mono);font-size:.7em;text-align:right;line-height:1.35}
.layer.hi{border-color:var(--accent);background:var(--accent-soft)}
.layer.rw{border-style:dashed;border-color:var(--amber);background:transparent}
.layer.rw b{color:var(--amber)}
.layer.dim{opacity:.55}
.layer .tg{font-family:var(--mono);font-size:.66em;padding:1px 8px;border-radius:999px;border:1px solid var(--line-2);color:var(--muted);letter-spacing:.06em;white-space:nowrap}
.layer .tg.ok{border-color:var(--green);color:var(--green)}
.layer .tg.redo{border-color:var(--red);color:var(--red)}
.layers .base{font-family:var(--mono);font-size:.7em;color:var(--muted);text-align:center;margin-top:6px;letter-spacing:.06em}

/* Linha do tempo (introdução) */
.timeline{list-style:none;margin:clamp(28px,5vh,48px) 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px}
.timeline li{border-top:2px solid var(--line-2);padding-top:20px;min-width:0}
.timeline .date{display:block;font-family:var(--mono);font-size:.8em;color:var(--muted);margin-bottom:20px}
.timeline h3{font-size:clamp(20px,2vw,26px);margin-bottom:12px}
.timeline p{color:var(--ink-2);max-width:32ch}
.timeline .hi{border-color:var(--accent)}
.timeline .hi .date{color:var(--accent)}
@media (max-width:700px){.timeline{grid-template-columns:1fr;gap:24px}.timeline li{border-top:0;border-left:2px solid var(--line-2);padding:0 0 0 20px}.timeline .date{margin-bottom:8px}.timeline p{max-width:none}}
</style>
</head>
<body>
<main id="home"></main>
<main id="deck" class="hidden">
  <div class="rail">
    <a class="btn" href="#/" id="btnHome">← Exercícios</a>
    <div class="crumb" id="crumb"></div>
    <div class="counter" id="counter"></div>
  </div>
  <section class="slide" id="slide"></section>
  <div class="rail bottom">
    <button class="btn" id="btnPrev">← Anterior</button>
    <div class="dots" id="dots"></div>
    <button class="btn primary" id="btnNext">Próximo →</button>
  </div>
</main>

<script>
/* ---------- helpers ---------- */
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');

// Command block: lines starting with "$ " become prompt lines; "# " comment lines; "+ "/"- " diff lines; "> " output lines.
function cmd(text){
  const lines = text.replace(/^\n/,'').replace(/\n\s*$/,'').split('\n');
  return '<pre class="cmd">' + lines.map(l=>{
    if (l.startsWith('$ ')) return '<span class="p">$ </span>' + esc(l.slice(2));
    if (/^\s*#/.test(l)) return '<span class="c">' + esc(l) + '</span>';
    if (l.startsWith('+ ')) return '<span class="add">' + esc(l) + '</span>';
    if (l.startsWith('- ')) return '<span class="del">' + esc(l) + '</span>';
    if (l.startsWith('> ')) return '<span class="o">' + esc(l.slice(2)) + '</span>';
    return esc(l);
  }).join('\n') + '</pre>';
}

// Camadas de uma imagem, empilhadas: a primeira da lista fica em cima.
// items: [{t:'COPY . .', s:'o seu código', cls:'hi'|'rw'|'dim', tag:'CACHED', tagCls:'ok'|'redo'}]
function layers(items, cap='', base=''){
  return `<div class="layers">${cap?`<div class="cap">${cap}</div>`:''}<div class="stk">` +
    items.map(i=>`<div class="layer ${i.cls||''}"><b>${esc(i.t)}</b>${i.tag?`<span class="tg ${i.tagCls||''}">${esc(i.tag)}</span>`:''}${i.s?`<small>${i.s}</small>`:''}</div>`).join('') +
    `</div>${base?`<div class="base">${base}</div>`:''}</div>`;
}

// navegador → Codespace:host → container:cont
function ports(host, cont, o={}){
  const {app='uvicorn', quem='navegador ou curl'} = o;
  return `<div class="flow">
    <div class="node"><b>${quem}</b><small>curl: localhost:${host} · navegador: endereço da aba PORTS</small></div>
    <div class="arr"><span class="a">→</span><strong>-p ${host}:${cont}</strong></div>
    <div class="node hi"><b>Codespace :${host}</b><small>porta da máquina que executa o Docker</small></div>
    <div class="arr"><span class="a">→</span>encaminha</div>
    <div class="node"><b>container :${cont}</b><small>${app} recebe os pedidos nesta porta</small></div>
  </div>`;
}

// registro → imagem → container
function imgflow(o={}){
  const {hi='cont', pull='docker pull · baixa a imagem', run='docker run · cria e inicia'} = o;
  const n=(k,t,s)=>`<div class="node ${hi===k?'hi':''}"><b>${t}</b><small>${s}</small></div>`;
  return `<div class="flow">
    ${n('reg','Registro','Docker Hub · onde as imagens ficam publicadas')}
    <div class="arr"><span class="a">→</span>${pull}</div>
    ${n('img','Imagem','programa e arquivos prontos para criar containers')}
    <div class="arr"><span class="a">→</span>${run}</div>
    ${n('cont','Container','ambiente criado a partir da imagem para executar o programa')}
  </div>`;
}

function docs(items){
  return '<p style="margin-bottom:14px;color:var(--muted)">Links para consultar depois. A documentação do Docker está em inglês.</p><ul class="links">' + items.map(i=>`<li><div><a href="${i.href}" target="_blank" rel="noopener">${i.t}</a>${i.s?`<small>${i.s}</small>`:''}</div></li>`).join('') + '</ul>';
}
function kv(rows, head=['Comando','Para quê']){
  return `<div class="tw"><table class="kv"><thead><tr>${head.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>` +
    rows.map(r=>`<tr>${r.map((c,i)=>`<td>${i===0?`<code>${esc(c)}</code>`:c}</td>`).join('')}</tr>`).join('') + '</tbody></table></div>';
}
function steps(items){ return '<ol class="steps">' + items.map(i=>`<li><div>${i}</div></li>`).join('') + '</ol>'; }
function chips(list, cls=''){ return `<div class="chips">${list.map(c=>`<span class="chip ${cls}">${esc(c)}</span>`).join('')}</div>`; }

// Standard cover slide for a exercício.
function cover(d, objetivo, onde, extra=''){
  return `<div class="cols s2"><div class="stack">
    <div class="big">${String(d.n).padStart(2,'0')}</div>
    <p class="lead">${objetivo}</p>
    ${chips(d.cmds)}
    ${extra}
  </div><div class="stack">
    <div class="box lift"><h3>Onde fazer</h3>${onde}</div>
    <div class="box soft"><h3>Para este exercício</h3>${kv([['⏱ tempo', `${d.time} min${d.el?' · opcional':''}`],['módulo', d.mod],['verificação', `<code>check.sh ${String(d.n).padStart(2,'0')}</code>`]], ['',''])}${d.el?'<p style="margin-top:12px">Pode ser feito depois da aula.</p>':''}</div>
  </div></div>`;
}
const qualquer = '<p>No terminal do Codespace, em <strong>qualquer pasta</strong>. Estes comandos usam recursos gerenciados pelo Docker e não dependem de arquivos da pasta atual.</p>';
</script>
<script>
/* ---------- doc links ---------- */
const DD = 'https://docs.docker.com/';
const CLI = c => DD + 'reference/cli/docker/' + c + '/';
const HUB = i => 'https://hub.docker.com/_/' + i;
const L = {
  ov:        {t:'Visão geral do Docker', href:DD+'get-started/docker-overview/', s:'documentação oficial · em inglês'},
  c_cont:    {t:'O que é um container?', href:DD+'get-started/docker-concepts/the-basics/what-is-a-container/', s:'documentação oficial · em inglês'},
  c_img:     {t:'O que é uma imagem?', href:DD+'get-started/docker-concepts/the-basics/what-is-an-image/', s:'documentação oficial · em inglês'},
  c_reg:     {t:'Onde as imagens são publicadas?', href:DD+'get-started/docker-concepts/the-basics/what-is-a-registry/', s:'Docker Hub e outros registros · em inglês'},
  c_df:      {t:'Como escrever um Dockerfile', href:DD+'get-started/docker-concepts/building-images/writing-a-dockerfile/', s:'em inglês'},
  c_layers:  {t:'Como funcionam as camadas de uma imagem', href:DD+'get-started/docker-concepts/building-images/understanding-image-layers/', s:'em inglês'},
  c_cache:   {t:'Como reutilizar etapas da construção: cache', href:DD+'get-started/docker-concepts/building-images/using-the-build-cache/', s:'em inglês'},
  c_ports:   {t:'Como publicar portas', href:DD+'get-started/docker-concepts/running-containers/publishing-ports/', s:'em inglês'},
  c_over:    {t:'Como mudar a configuração de um container', href:DD+'get-started/docker-concepts/running-containers/overriding-container-defaults/', s:'-e, -p, --name e comando · em inglês'},
  c_persist: {t:'Como guardar dados em volumes', href:DD+'get-started/docker-concepts/running-containers/persisting-container-data/', s:'em inglês'},
  c_share:   {t:'Como compartilhar arquivos com containers', href:DD+'get-started/docker-concepts/running-containers/sharing-local-files/', s:'bind mounts · em inglês'},
  c_multi:   {t:'Como usar vários containers em uma aplicação', href:DD+'get-started/docker-concepts/running-containers/multi-container-applications/', s:'redes e Compose · em inglês'},
  df:        {t:'Referência · Dockerfile', href:DD+'reference/dockerfile/', s:'todas as instruções'},
  df_from:   {t:'Dockerfile · FROM', href:DD+'reference/dockerfile/#from'},
  df_copy:   {t:'Dockerfile · COPY', href:DD+'reference/dockerfile/#copy'},
  df_run:    {t:'Dockerfile · RUN', href:DD+'reference/dockerfile/#run'},
  df_cmd:    {t:'Dockerfile · CMD', href:DD+'reference/dockerfile/#cmd'},
  df_entry:  {t:'Dockerfile · ENTRYPOINT', href:DD+'reference/dockerfile/#entrypoint', s:'e a diferença para CMD'},
  df_wd:     {t:'Dockerfile · WORKDIR', href:DD+'reference/dockerfile/#workdir'},
  df_env:    {t:'Dockerfile · ENV', href:DD+'reference/dockerfile/#env'},
  df_expose: {t:'Dockerfile · EXPOSE', href:DD+'reference/dockerfile/#expose'},
  best:      {t:'Recomendações para construir imagens', href:DD+'build/building/best-practices/', s:'ordem das instruções, .dockerignore e tamanho · em inglês'},
  cache:     {t:'Cache de construção de imagens', href:DD+'build/cache/', s:'em inglês'},
  ctx:       {t:'Contexto de construção e .dockerignore', href:DD+'build/concepts/context/#dockerignore-files', s:'em inglês'},
  run_guide: {t:'Guia para executar containers', href:DD+'engine/containers/run/', s:'opções de docker run · em inglês'},
  r_run:     {t:'Comando · docker run', href:CLI('container/run'), s:'-d, -it, --rm, --name, -p, -e, -v, --network'},
  r_ps:      {t:'Comando · docker ps', href:CLI('container/ls'), s:'-a, --filter, --format'},
  r_exec:    {t:'Comando · docker exec', href:CLI('container/exec')},
  r_logs:    {t:'Comando · docker logs', href:CLI('container/logs'), s:'-f, --tail'},
  r_stop:    {t:'Comando · docker stop', href:CLI('container/stop')},
  r_start:   {t:'Comando · docker start', href:CLI('container/start'), s:'-ai'},
  r_rm:      {t:'Comando · docker rm', href:CLI('container/rm'), s:'-f'},
  r_cp:      {t:'Comando · docker cp', href:CLI('container/cp')},
  r_port:    {t:'Comando · docker port', href:CLI('container/port')},
  r_cprune:  {t:'Comando · docker container prune', href:CLI('container/prune')},
  r_build:   {t:'Comando · docker build', href:CLI('buildx/build'), s:'-t, --no-cache, -f'},
  r_images:  {t:'Comando · docker images', href:CLI('image/ls')},
  r_tag:     {t:'Comando · docker tag', href:CLI('image/tag')},
  r_hist:    {t:'Comando · docker history', href:CLI('image/history')},
  r_iprune:  {t:'Comando · docker image prune', href:CLI('image/prune'), s:'-a'},
  r_vol:     {t:'Comando · docker volume create', href:CLI('volume/create')},
  r_net:     {t:'Comando · docker network create', href:CLI('network/create')},
  vols:      {t:'Como usar volumes', href:DD+'engine/storage/volumes/'},
  binds:     {t:'Como usar bind mounts', href:DD+'engine/storage/bind-mounts/'},
  net:       {t:'Redes entre containers', href:DD+'engine/network/', s:'comunicação pelo nome em redes criadas por você · em inglês'},
  bridge:    {t:'Redes do tipo bridge', href:DD+'engine/network/drivers/bridge/', s:'em inglês'},
  compose:   {t:'Guia do Docker Compose', href:DD+'compose/'},
  cfile:     {t:'Referência do arquivo Compose', href:DD+'reference/compose-file/', s:'services, build, ports, environment, volumes · em inglês'},
  c_up:      {t:'Comando · docker compose up', href:CLI('compose/up'), s:'-d, --build'},
  c_ps:      {t:'Comando · docker compose ps', href:CLI('compose/ps')},
  c_logs:    {t:'Comando · docker compose logs', href:CLI('compose/logs')},
  c_down:    {t:'Comando · docker compose down', href:CLI('compose/down'), s:'-v, --rmi'},
  c_run:     {t:'Comando · docker compose run', href:CLI('compose/run'), s:'executa um serviço em um container temporário'},
  sdf:       {t:'Comando · docker system df', href:CLI('system/df')},
  sprune:    {t:'Comando · docker system prune', href:CLI('system/prune'), s:'-a, --volumes'},
  h_python:  {t:'Docker Hub · python', href:HUB('python'), s:'tags: 3.12-slim, 3.12-alpine…'},
  h_nginx:   {t:'Docker Hub · nginx', href:HUB('nginx'), s:'onde colocar os arquivos do site'},
  h_alpine:  {t:'Docker Hub · alpine', href:HUB('alpine'), s:'a imagem Linux de 5 MB'},
  h_hello:   {t:'Docker Hub · hello-world', href:HUB('hello-world')},
  gh_ports:  {t:'GitHub Docs · Encaminhar portas no Codespace', href:'https://docs.github.com/pt/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace', s:'a aba PORTS · pt-br'},
  livro:     {t:'Descomplicando Docker (livro gratuito)', href:'https://livro.descomplicandodocker.com.br/', s:'pt-br'},
  repo:      {t:'Repositório do curso', href:'https://github.com/fsilva-alt/devops-docker', s:'enunciados, gabarito, guia do aluno'},
};

/* ---------- INTRO ---------- */
const INTRO = {
  n:'intro', key:'intro', title:'Antes de começar', short:'Comece por aqui', mod:'Abertura', time:8, el:false, cmds:['como acompanhar','imagem e container','para que serve o Docker'],
  slides:[
    {h:'Como acompanhar a aula', eyebrow:'Introdução · 1 de 6', body:`
      <div class="stack">
        <p class="lead">Você não precisa saber programar. Os programas do curso já estão prontos; vamos usá-los para aprender Docker, um passo de cada vez.</p>
        <div class="cols">
          <div class="box"><h3>Seu ambiente no navegador</h3><p>O <strong>Codespace</strong> é um computador Linux acessado pela internet. Nele, o <strong>VS Code</strong> é o editor de arquivos, e o <strong>terminal</strong> é a área onde você digita comandos.</p><p>Abra o terminal em <strong>Terminal → New Terminal</strong>. A preparação completa está no <a href="https://github.com/fsilva-alt/devops-docker#antes-da-aula" target="_blank" rel="noopener">README do curso</a>.</p></div>
          <div class="box lift"><h3>Comando ou conteúdo de arquivo?</h3><p>Nos slides, <code>$</code> marca uma linha para executar no terminal. Copie o comando sem esse símbolo e pressione <kbd>Enter</kbd>. Execute uma linha por vez.</p><p>Quando a instrução pedir um arquivo, copie o conteúdo no editor e salve com <kbd>Ctrl+S</kbd> ou <kbd>Cmd+S</kbd> no Mac. Linhas com <code>#</code> são comentários.</p></div>
          <div class="box"><h3>Como fazer os exercícios</h3><p>Leia o objetivo, consulte os comandos e siga a tarefa na pasta indicada. Ao terminar, execute <code>check.sh</code> com o número do exercício: ele confirma o resultado ou mostra o que ajustar.</p><p>Os marcados como <strong>opcionais</strong> e a <strong>Missão extra</strong> podem ficar para depois. Para executar os comandos, use os exemplos completos da tarefa. Nas tabelas de consulta, <code>&lt;nome&gt;</code> indica um valor a substituir, <code>[opção]</code> indica algo opcional, e <code>…</code> indica um exemplo abreviado.</p></div>
        </div>
        <div class="box lift"><h3>Instale o material do curso</h3><p>Execute esta linha uma única vez no terminal do Codespace. O instalador baixa as imagens da aula, prepara os arquivos dos exercícios em <code>~/labs</code> e disponibiliza os comandos <code>check.sh</code> e <code>reset.sh</code>.</p>${cmd('$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-docker/main/install.sh)"')}<p style="margin-top:10px">Espere aparecer <strong>Curso de Docker instalado com sucesso!</strong> e abra um terminal novo antes de continuar. Se você já instalou antes da aula, pule esta etapa.</p></div>
        <div class="callout"><strong>Comandos para se localizar:</strong> <code>pwd</code> mostra a pasta atual; <code>ls</code> lista seu conteúdo; <code>cd caminho</code> entra em outra pasta. O símbolo <code>~</code> representa sua pasta pessoal. Para abrir um arquivo no editor, use <code>code nome-do-arquivo</code>.</div>
      </div>`},
    {h:'O que é um container?', eyebrow:'Introdução · 2 de 6', body:`
      <div class="cols s2"><div class="stack">
        <p class="lead">Um <strong>container</strong> é um ambiente isolado para executar um programa. Ele tem seus próprios arquivos e configurações, mas compartilha o núcleo do sistema operacional com a máquina em que está rodando.</p>
        <div class="box"><h3>Por que isso ajuda?</h3><p>Um programa pode precisar de uma versão específica do Python e de outros pacotes de software, chamados <strong>dependências</strong>. Se faltar um deles, aparece um erro como este:</p>${cmd(`$ python app.py
> ModuleNotFoundError: No module named 'fastapi'
# A mensagem diz que o pacote fastapi não foi encontrado.`)}</div>
      </div><div class="stack">
        <div class="box lift"><h3>Imagem e container</h3>${kv([
          ['imagem','reúne o programa, suas dependências e os arquivos necessários. Serve de base para criar containers'],
          ['container','é criado a partir de uma imagem para executar o programa. Cada container tem seu próprio estado e pode ser iniciado, parado ou removido'],
          ['registro','é um serviço que armazena e distribui imagens, como o Docker Hub'],
        ], ['','' ])}</div>
        <div class="callout"><strong>Uma imagem, vários containers.</strong> Você pode usar a mesma imagem em ambientes compatíveis, levando junto as versões do programa e de suas dependências. Isso reduz diferenças entre o ambiente de quem desenvolve e o de quem executa.</div>
      </div></div>`},
    {h:'De onde veio o Docker?', eyebrow:'Introdução · 3 de 6', body:`
      <p class="lead">Containers já existiam. O Docker tornou mais simples <strong>construir, compartilhar e executar</strong> esses ambientes.</p>
      <ol class="timeline" aria-label="Três marcos da história do Docker">
        <li><span class="date">Antes de 2013</span><h3>Isolamento no Linux</h3><p>O Linux já permitia separar programas e limitar seu uso de recursos.</p></li>
        <li class="hi"><span class="date">Março de 2013</span><h3>Nasce o Docker</h3><p>Solomon Hykes apresenta o Docker na PyCon: uma forma mais acessível de usar containers.</p></li>
        <li><span class="date">2015 em diante</span><h3>Padrões abertos</h3><p>Surge a OCI, iniciativa para padronizar imagens e sua execução entre ferramentas compatíveis.</p></li>
      </ol>`},
    {h:'Para que vamos usar o Docker?', eyebrow:'Introdução · 4 de 6', body:`
      <div class="cols w2">
        <div class="box lift"><h3>Reutilizar um ambiente preparado</h3><p>A imagem guarda o programa, as bibliotecas que ele usa e a versão do Python. A mesma imagem serve para desenvolver, testar e entregar o programa a outras pessoas.</p></div>
        <div class="box"><h3>Instalar dependências na imagem</h3><p>Vamos instalar o FastAPI durante a construção da imagem, chamada de <strong>build</strong>. Depois, cada container criado a partir dela já terá esse pacote disponível.</p></div>
        <div class="box"><h3>Criar e remover ambientes de teste</h3><p>Dá para criar um container, experimentar um programa nele e removê-lo ao terminar, sem instalar esse programa no sistema do Codespace.</p></div>
        <div class="box"><h3>Separar projetos</h3><p>Dois projetos podem usar versões diferentes do Python, cada um em seu container. Os arquivos e as dependências de um não substituem os do outro.</p></div>
      </div>
      <p class="lead" style="margin-top:22px;color:var(--muted)">Na prática, usaremos um livro de receitas: primeiro no terminal, depois como uma API que fornece dados e, por fim, como um site no navegador.</p>`},
    {h:'O que ainda precisa de cuidado?', eyebrow:'Introdução · 5 de 6', body:`
      <div class="cols w2">
        <div class="box"><h3>Compatibilidade do sistema</h3><p>Os containers desta aula usam o kernel Linux do Codespace. A imagem precisa ser compatível com o sistema e a arquitetura que vão executá-la; ela não simula um computador completo.</p></div>
        <div class="box"><h3>Armazenamento dos dados</h3><p>Remover um container apaga os arquivos guardados apenas na camada própria dele. O exercício opcional 11 usa <strong>volumes</strong> para manter dados fora dessa camada. Um volume não substitui uma cópia de segurança.</p></div>
        <div class="box"><h3>Várias máquinas</h3><p>Nesta aula, os containers rodam em um único Codespace. Distribuí-los entre várias máquinas exige outras ferramentas, como Kubernetes. Esse gerenciamento é chamado de <strong>orquestração</strong>.</p></div>
        <div class="box"><h3>Funcionamento do programa</h3><p>A imagem reúne o que o programa precisa para executar, mas não corrige erros no código. Ainda é necessário testar se o programa produz o resultado esperado.</p></div>
        <div class="box"><h3>Arquivos incluídos na imagem</h3><p>Arquivos desnecessários aumentam o tamanho da imagem e o tempo de transferência. O exercício opcional 7 mostra como escolher o que fica de fora usando <code>.dockerignore</code>.</p></div>
        <div class="box"><h3>Senhas e outras informações privadas</h3><p>Quem tem acesso à imagem pode ler os arquivos que ela contém. Senhas devem ser fornecidas na execução, nunca durante a construção da imagem. O exercício 9 mostra como passar configurações na execução.</p></div>
      </div>`},
    {h:'Docker, Docker Hub e Docker Desktop', eyebrow:'Introdução · 6 de 6', body:`
      <div class="cols s2">
        <div class="stack">
          <div class="flow">
            <div class="node hi"><b>Docker Engine</b><small>constrói imagens e executa containers no Codespace</small></div>
            <div class="arr"><span class="a">⇄</span>baixar e publicar imagens</div>
            <div class="node"><b>Docker Hub</b><small>serviço de armazenamento e distribuição de imagens</small></div>
          </div>
          ${kv([
            ['Docker Engine','É o Docker instalado no Codespace. Depois de obter uma imagem, ele pode criar containers com ela sem baixá-la novamente.'],
            ['Docker Hub','É de onde vêm as imagens <code>python</code>, <code>nginx</code> e <code>alpine</code> usadas no curso. Nesta aula, você não precisa criar uma conta no Docker Hub.'],
            ['Docker Desktop','É um aplicativo para usar Docker no computador pessoal. Não é preciso instalá-lo: o curso usa o Docker que já está no Codespace.'],
          ], ['','' ])}
        </div>
        <div class="stack">
          <div class="callout"><strong>Para acompanhar:</strong> tenha sua conta no GitHub e o Codespace preparado conforme o README. Os comandos da aula serão executados no terminal desse ambiente.</div>
          <div class="callout"><strong>Para abrir o site:</strong> a aba PORTS (portas), ao lado de TERMINAL no VS Code, mostra o endereço para acessar pelo navegador. Você vai usá-la a partir do exercício 8.</div>
          <div class="box soft"><h3>Para ler depois</h3>${docs([L.ov, L.c_cont, L.c_img, L.c_reg, L.livro])}</div>
        </div>
      </div>`},
  ]
};

/* ---------- EXERCÍCIOS ---------- */
const D = [];

/* 0 */
D.push({n:0, key:'00', title:'Docker funciona?', mod:'Abertura', time:3, el:false, cmds:['docker version','docker run hello-world','docker compose version'],
  slides:[
    {h:'Docker funciona?', body: cover({n:0,time:3,el:false,mod:'Abertura · feito antes da aula, logo depois do instalador',cmds:['docker version','docker run hello-world','docker compose version','check.sh 00']},
      'Antes da aula, execute seu <strong>primeiro container</strong> e confira se o ambiente está pronto para os exercícios. Fazer esta etapa com antecedência dá tempo para se familiarizar com o terminal e pedir ajuda se aparecer algum erro.',
      qualquer)},
    {h:'O comando e o serviço do Docker', eyebrow:'Conceito', body:`
      <div class="cols s2"><div class="stack">
        <div class="flow">
          <div class="node"><b>docker</b><small>o <strong>cliente</strong>: o comando que você digita</small></div>
          <div class="arr"><span class="a">→</span>pede</div>
          <div class="node hi"><b>dockerd</b><small>o <strong>daemon</strong>: serviço que recebe e executa os pedidos</small></div>
          <div class="arr"><span class="a">→</span>administra</div>
          <div class="node"><b>containers · imagens · volumes · redes</b><small>tudo o que a aula vai criar</small></div>
        </div>
        <div class="box"><h3>A mensagem do primeiro container</h3>${cmd(`$ docker run hello-world
> Hello from Docker!
> To generate this message, Docker took the following steps:
>  1. The Docker client contacted the Docker daemon.
>  2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
>  3. The Docker daemon created a new container from that image…
>  4. The Docker daemon streamed that output to the Docker client…`)}<p style="margin-top:10px">O texto explica que o cliente fez um pedido, o serviço obteve a imagem, criou o container e mostrou a mensagem no terminal. Se a imagem já estiver disponível, não precisa ser baixada novamente.</p></div>
      </div><div class="stack">
        <div class="box lift"><h3>Como saber se está funcionando</h3><p><code>docker version</code> mostra as seções <strong>Client</strong> (cliente) e <strong>Server</strong> (serviço). Se aparecer <em>Cannot connect to the Docker daemon</em>, o cliente não conseguiu acessar o serviço.</p><p>Em um Codespace recém-aberto, espere um minuto e tente novamente.</p></div>
        <div class="callout"><strong>No modelo Blank</strong>, o Docker e o Compose já vêm instalados. O instalador do curso confere o ambiente, baixa as imagens e prepara os arquivos dos exercícios.</div>
      </div></div>`},
    {h:'Comandos e documentação', eyebrow:'Referência', body:`
      <div class="cols s2">
        ${kv([
          ['docker version','mostra as versões do cliente e do serviço Docker'],
          ['docker info','mostra informações do serviço: containers, imagens e armazenamento'],
          ['docker run hello-world','cria e executa um container de teste; baixa a imagem se ela não estiver disponível'],
          ['docker compose version','mostra a versão do Compose instalado'],
        ])}
        <div class="box soft"><h3>Documentação</h3>${docs([L.ov, L.h_hello, L.r_run, L.repo])}</div>
      </div>`},
    {h:'O exercício', eyebrow:'Tarefa · 3 min', body:`
      <div class="cols s2"><div class="stack">${steps([
        `<div class="t">Confira se aparecem as versões de <strong>Client</strong> e <strong>Server</strong>. Isso indica que o comando conseguiu acessar o serviço:</div>${cmd('$ docker version')}`,
        `<div class="t">Execute o container de teste e procure a mensagem <strong>Hello from Docker!</strong>:</div>${cmd('$ docker run hello-world')}`,
        `<div class="t">Confira a versão do Compose, a ferramenta que inicia o site e a API juntos no exercício 14:</div>${cmd('$ docker compose version')}`,
      ])}</div><div class="stack">
        <div class="box"><h3>Verificação</h3>${cmd('$ check.sh 00')}<p style="margin-top:10px;color:var(--muted)">Confere as quatro imagens-base (<code>hello-world</code>, <code>alpine</code>, <code>python:3.12-slim</code>, <code>nginx:alpine</code>) e testa se dois containers conversam pelo nome em uma rede temporária. Os recursos desse teste são removidos ao terminar. Faltou alguma imagem? Execute <code>setup.sh</code>.</p></div>
        <div class="callout warn"><strong>Depois, pare o Codespace</strong> para não gastar a franquia. Em github.com/codespaces, clique em ⋯ e escolha <em>Stop codespace</em>. No dia da aula, basta abrir de novo; imagens e laboratórios continuam lá.</div>
        <div class="box soft"><h3>Missão extra · opcional</h3><p>Execute <code>docker info</code> para consultar um resumo do serviço Docker. Procure a linha <code>Containers:</code>: ela mostra o total de containers, incluindo os parados. O <code>hello-world</code> deve estar nessa contagem.</p></div>
      </div></div>`},
  ]});

/* 1 */
D.push({n:1, key:'01', title:'Olá, container', mod:'Módulo 1 · Fundamentos', time:5, el:false, cmds:['docker run','docker ps -a','docker images'],
  slides:[
    {h:'Olá, container', body: cover({n:1,time:5,el:false,mod:'Módulo 1 · Fundamentos',cmds:['docker run <imagem> <comando>','docker ps','docker ps -a','docker images']},
      'Executar um programa Python <strong>dentro de um container</strong> e comparar a imagem usada como base com os containers criados a partir dela.',
      qualquer + '<p style="margin-top:10px;color:var(--muted)">Faça depois de concluir o exercício 0. Não é preciso preparar nenhum arquivo.</p>')},
    {h:'Qual é a diferença entre imagem e container?', eyebrow:'Conceito', body:`
      <div class="stack">
        ${imgflow()}
        <div class="cols s2">
          ${layers([
            {t:'camada gravável', s:'arquivos próprios do container · apagados ao removê-lo', cls:'rw'},
            {t:'python:3.12-slim', s:'Python 3.12 instalado', cls:'hi'},
            {t:'debian:bookworm-slim', s:'um Debian mínimo'},
          ], 'arquivos do container: base da imagem e alterações próprias', 'a imagem-base pode ser usada por vários containers')}
          <div class="stack">
            <div class="box lift"><h3>Como ler o comando</h3>${cmd('$ docker run python:3.12-slim python -c \'print("Olá, Docker!")\'\n#          └── imagem ──────┘ └──── comando executado lá dentro ────┘')}<p style="margin-top:10px"><code>python</code> é o nome da imagem; <code>3.12-slim</code> é a <strong>tag</strong>, um rótulo de versão ou variante. Sem tag, o Docker usa <code>latest</code>.</p><p>Python é uma linguagem de programação. Neste exemplo, <code>-c</code> pede que ela execute o texto entre aspas, e <code>print</code> mostra a mensagem na tela. Mantenha as <strong>aspas simples por fora</strong>: elas impedem que o Bash interprete o <code>!</code> como uma consulta ao histórico.</p></div>
            <div class="callout"><strong>docker run sempre cria um container novo.</strong> Rodou três vezes, três containers. Quando o comando termina, o container <em>para</em>, mas continua existindo (<code>docker ps -a</code>) até ser removido.</div>
          </div>
        </div>
      </div>`},
    {h:'Comandos e documentação', eyebrow:'Referência', body:`
      <div class="cols s2">
        ${kv([
          ['docker run <imagem> [comando]','cria um container novo e roda o comando (ou o padrão da imagem)'],
          ['docker ps','containers rodando agora'],
          ['docker ps -a','todos, inclusive os parados'],
          ['docker images','imagens baixadas ou construídas nesta máquina'],
          ['docker pull <imagem>','só baixa, sem rodar (o run faz isso sozinho na primeira vez)'],
          ['docker rm <container>','remove um container parado (exercício 3)'],
        ])}
        <div class="box soft"><h3>Documentação</h3>${docs([L.c_img, L.c_cont, L.c_reg, L.r_run, L.r_ps, L.r_images, L.h_python])}</div>
      </div>`},
    {h:'O exercício', eyebrow:'Tarefa · 5 min', body:`
      <div class="cols s2"><div class="stack">${steps([
        `<div class="t">Execute o teste novamente. Como a imagem já está disponível, não devem aparecer mensagens de download, como <em>Pulling</em>. O Docker cria um novo container:</div>${cmd('$ docker run hello-world')}`,
        `<div class="t">Crie um container com Python. Copie também as aspas simples externas, que protegem o <code>!</code> da interpretação do Bash:</div>${cmd('$ docker run python:3.12-slim python -c \'print("Olá, Docker!")\'')}`,
        `<div class="t">Liste os containers em execução e, depois, todos os containers. Os dois programas já terminaram, mas seus containers aparecem na segunda lista:</div>${cmd('$ docker ps\n$ docker ps -a')}`,
        `<div class="t">Agora liste as imagens disponíveis:</div>${cmd('$ docker images')}`,
      ])}</div><div class="stack">
        <div class="box"><h3>Verificação</h3>${cmd('$ check.sh 01')}<p style="margin-top:10px;color:var(--muted)">Aprova com um container do <code>hello-world</code> e um do <code>python:3.12-slim</code> rodando um <code>print</code>.</p></div>
        <div class="callout"><strong>Como ler a lista:</strong> IMAGE é a imagem; COMMAND, o comando; STATUS, o estado; e NAMES, o nome. <code>Exited (0)</code> significa que o programa terminou sem erro. Cada <code>docker run</code> acrescenta um container.</div>
        <div class="box soft"><h3>Missão extra</h3>${cmd('$ docker run python:3.12-slim cat /etc/os-release\n$ cat /etc/os-release')}<p style="margin-top:8px;color:var(--muted)"><code>cat</code> mostra o conteúdo do arquivo. Compare as distribuições Linux do container e do Codespace: seus arquivos podem ser diferentes, mesmo compartilhando o kernel.</p></div>
      </div></div>`},
  ]});

/* 2 */
D.push({n:2, key:'02', title:'Dentro do container', mod:'Módulo 1 · Fundamentos', time:5, el:false, cmds:['docker run -it','--rm','--name','docker start -ai'],
  slides:[
    {h:'Dentro do container', body: cover({n:2,time:5,el:false,mod:'Módulo 1 · Fundamentos',cmds:['docker run -it --rm','docker run -it --name','exit','docker start -ai']},
      'Dentro de um container, você digita comandos e cria um arquivo. Depois, confere que esse arquivo <strong>não aparece em outro container</strong> criado a partir da mesma imagem.',
      qualquer)},
    {h:'Cada container, seu sistema de arquivos', eyebrow:'Conceito', body:`
      <div class="stack">
        <div class="cols w2">
          ${layers([
            {t:'explorador · camada gravável', s:'/marca.txt está aqui', cls:'rw'},
            {t:'python:3.12-slim', s:'só leitura', cls:'dim'},
          ], 'container "explorador"')}
          ${layers([
            {t:'outro container · camada gravável', s:'vazia: /marca.txt não existe', cls:'rw'},
            {t:'python:3.12-slim', s:'a mesma imagem, compartilhada', cls:'dim'},
          ], 'docker run --rm python:3.12-slim cat /marca.txt')}
        </div>
        <div class="cols">
          <div class="box lift"><h3>As opções de hoje</h3>${kv([
            ['-i','permite enviar o que você digita para o programa no container'],
            ['-t','fornece um terminal para essa interação; aqui, as duas vão juntas: -it'],
            ['--rm','remove o container assim que ele terminar; bom para testes rápidos'],
            ['--name x','nome fixo em vez de um aleatório, para usar nos comandos seguintes'],
          ], ['Opção','Efeito'])}</div>
          <div class="stack">
            <div class="callout"><strong>Parar e remover são ações diferentes.</strong> Sem <code>--rm</code>, sair com <code>exit</code> para o container e mantém seus arquivos. <code>docker start -ai explorador</code> inicia o mesmo container e permite interagir com ele novamente.</div>
            <div class="callout"><strong>Para sair neste exercício:</strong> use <code>exit()</code> no Python e <code>exit</code> no Bash. Para desconectar o terminal sem parar um container interativo, use <kbd>Ctrl+P</kbd> e depois <kbd>Ctrl+Q</kbd>.</div>
          </div>
        </div>
      </div>`},
    {h:'Comandos e documentação', eyebrow:'Referência', body:`
      <div class="cols s2">
        ${kv([
          ['docker run -it --rm <imagem> bash','abre o Bash, se disponível na imagem, em um container temporário'],
          ['docker run -it --name <nome> <imagem> <cmd>','interativo, com nome, e fica depois de sair'],
          ['docker start -ai <nome>','inicia um container parado e permite interagir com ele pelo terminal'],
          ['docker exec -it <nome> bash','abre outro Bash em um container que já está rodando (exercício 9)'],
          ['docker cp <nome>:/arquivo .','copia um arquivo de dentro do container (mesmo parado)'],
        ])}
        <div class="box soft"><h3>Documentação</h3>${docs([L.c_cont, L.r_run, L.r_start, L.r_exec, L.r_cp])}</div>
      </div>`},
    {h:'O exercício', eyebrow:'Tarefa · 5 min', body:`
      <div class="cols s2"><div class="stack">${steps([
        `<div class="t">Abra o Python interativo. Quando aparecer <code>&gt;&gt;&gt;</code>, digite <code>import platform; platform.platform()</code> para ver informações do sistema. Saia com <code>exit()</code>. De volta ao Codespace, <code>docker ps -a</code> confirma que <code>--rm</code> removeu esse container.</div>${cmd('$ docker run -it --rm python:3.12-slim')}`,
        `<div class="t">Abra o <strong>Bash</strong>, um interpretador de comandos, também chamado de <em>shell</em>. Depois da primeira linha, os comandos serão executados <strong>dentro do container</strong>:</div>${cmd('$ docker run -it --name explorador python:3.12-slim bash\n$ cat /etc/os-release\n$ ls /\n$ hostname\n$ python --version')}`,
        `<div class="t">Ainda dentro do container, crie um arquivo e saia. O símbolo <code>&gt;</code> grava o texto produzido por <code>echo</code> no arquivo indicado:</div>${cmd('$ echo "eu estive aqui" > /marca.txt\n$ exit')}`,
        `<div class="t">De volta ao Codespace, tente ler o arquivo em <strong>outro</strong> container. O erro <em>No such file or directory</em> é esperado: o arquivo existe apenas no <code>explorador</code>.</div>${cmd('$ docker run --rm python:3.12-slim cat /marca.txt')}`,
      ])}</div><div class="stack">

...87954 bytes truncated...

The tool call succeeded but the output was truncated. Full output saved to: /home/lse/.local/share/opencode/tool-output/tool_0fa09c21a001H16qoKAaJCJW4G
Use the Task tool to have explore agent process this file with Grep and Read (with offset/limit). Do NOT read the full file yourself - delegate to save context.
```

---

## Assistant (Build · GPT-6 Astra · 11.3s)

_Thinking:_

**Checking support materials**

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/docs/guia-do-aluno.md"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/docs/guia-do-aluno.md</path>
<type>file</type>
<content>
1: # Guia do aluno
2: 
3: ## Antes da aula
4: 
5: 1. Siga a seção [Antes da aula](../README.md#antes-da-aula) para criar um Codespace com o modelo **Blank** e executar o instalador.
6: 2. Conclua o login do GitHub CLI com a conta que usará para publicar os exercícios.
7: 3. Abra um terminal novo, execute `gh auth status --hostname github.com` e depois `check.sh 01`. Antes do exercício 01, é esperado que o verificador informe a ausência do workflow.
8: 4. Pare o Codespace em [github.com/codespaces](https://github.com/codespaces), em **⋯ → Stop codespace**. No dia da aula, reabra o mesmo ambiente.
9: 
10: ## Como acompanhar os exercícios
11: 
12: - Siga a sequência **01 → 02 → 03 → 04 → 05 → 06 → 07**.
13: - Leia o objetivo e o estado inicial, entre na pasta indicada e execute uma etapa por vez.
14: - Comandos dos blocos `bash` vão no terminal. O conteúdo dos blocos `yaml` vai no arquivo `.github/workflows/ci.yml` do laboratório.
15: - Salve os arquivos com **Ctrl+S**, ou **Cmd+S** no Mac, antes de executar o verificador ou fazer commit.
16: - Execute `check.sh NN`, substituindo `NN` pelo número do exercício. Corrija o que for indicado e verifique novamente.
17: - Publique o laboratório no GitHub e confira a entrega descrita no enunciado. Um check local aprovado não comprova que o workflow executou corretamente no Actions.
18: 
19: Cada laboratório tem seu próprio estado inicial. Você pode iniciar o próximo exercício mesmo que não tenha concluído o anterior. O exercício 04 demonstra variáveis e contextos; os exercícios 05 a 07 retomam testes, build e publicação.
20: 
21: ## Onde você está trabalhando?
22: 
23: | Lugar | O que fazer ali |
24: |---|---|
25: | Terminal do Codespace | Executar `git`, `gh`, `cd`, `check.sh` e os comandos dos enunciados |
26: | Editor do VS Code | Criar e salvar workflows e alterações no projeto |
27: | Aba Actions, no GitHub | Acompanhar execuções, consultar logs e baixar artefatos |
28: | Aba Pull requests, no GitHub | Consultar os checks da proposta de alteração |
29: | GitHub Pages | Abrir o site publicado no exercício 07 |
30: 
31: O **runner** é a máquina que executa o workflow. Ele é separado do Codespace: arquivos e pacotes instalados no Codespace não aparecem automaticamente no runner.
32: 
33: `pwd` mostra a pasta atual, `ls` lista seu conteúdo e `cd caminho` muda de pasta. Para abrir um arquivo no editor, use `code nome-do-arquivo`.
34: 
35: O material fica em `~/devops-ghactions`, e os arquivos da prática ficam em `~/labs`. O atalho `labs`, criado na pasta em que o instalador foi executado, aponta para os mesmos arquivos. Os enunciados estão nos [slides HTML](https://fsilva-alt.github.io/devops-ghactions/); selecione o exercício no índice. A cópia local está em `~/devops-ghactions/docs/index.html`.
36: 
37: ## Comandos de apoio
38: 
39: | Comando | Quando usar |
40: |---|---|
41: | `check.sh NN` | Conferir o YAML do laboratório e receber orientações de correção |
42: | `setup.sh` | Criar os laboratórios que ainda não existem |
43: | `reset.sh NN` | Apagar o trabalho local de um laboratório e recriar seus arquivos iniciais |
44: 
45: Dentro de um laboratório, `check.sh` e `reset.sh` funcionam sem o número. Após um reset, execute novamente o `cd` do enunciado.
46: 
47: O instalador pode ser executado novamente para atualizar o material. Ele preserva os laboratórios existentes. Para receber um novo estado inicial, guarde as alterações que deseja manter e execute `reset.sh NN` depois da atualização. O reset remove também o remoto local `origin`, mas não apaga o repositório publicado no GitHub. Consulte [Retomar depois de resetar](../README.md#retomar-depois-de-resetar).
48: 
49: ## Publicação dos exercícios
50: 
51: Cada laboratório é publicado em um repositório público separado, de `actions-01` a `actions-07`. Execute `gh repo create` apenas na primeira publicação de cada laboratório. Para as alterações seguintes, use `git add`, `git commit` e `git push`, conforme o enunciado.
52: 
53: Continue no mesmo Codespace Blank durante toda a aula. Os repositórios publicados não precisam de outros Codespaces.
54: 
55: ## Problemas comuns
56: 
57: | Mensagem ou situação | Como resolver |
58: |---|---|
59: | `check.sh: command not found` | Abra um terminal novo ou execute `source ~/.bashrc`. No zsh, use `source ~/.zshrc`. |
60: | Instalador interrompido | Corrija a causa indicada no terminal e execute novamente o comando de instalação do README. |
61: | `Author identity unknown` | Configure seu nome e e-mail conforme a preparação do README. |
62: | Push recusado por permissão | Consulte [Se o push falhar por permissão](../README.md#se-o-push-falhar-por-permissão) e confira a conta e o escopo `workflow`. |
63: | Repositório já existe | Se já publicou esse laboratório, use `git push`. Para uma nova tentativa, escolha outro nome. |
64: | Botão Run workflow ausente | Confirme que o workflow contém `workflow_dispatch` e foi publicado na branch padrão `main`. |
65: | `Invalid workflow file` | Confira a linha indicada, a indentação com espaços e as chaves do YAML. |
66: | Correção não aparece no Actions | Salve o arquivo, faça commit e push. Reexecutar um commit antigo usa o código daquele commit. |
67: | `CURSO_TOKEN` ausente | Cadastre o segredo fictício no repositório `actions-04`, em Settings → Secrets and variables → Actions. |
68: | Pasta não encontrada após `reset.sh` | Entre novamente na pasta com o `cd` do enunciado. |
69: | Site do exercício 07 não abre | Aguarde o deploy e confira Settings → Pages → Source: GitHub Actions. Leia os logs se houver falha. |
70: 
71: Ao pedir ajuda, informe o exercício, o comando executado e a mensagem completa do terminal ou o link da execução no Actions.
72: 
73: ## Ao terminar
74: 
75: 1. Salve os links das entregas e faça push das alterações que deseja manter.
76: 2. Pare o Codespace. Mesmo parado, ele ocupa armazenamento; excluí-lo apaga arquivos locais que não foram publicados.
77: 3. Para revisar, consulte o [gabarito](gabarito.md) e a [documentação oficial do GitHub Actions](https://docs.github.com/pt/actions).

(End of file - total 77 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/docs/guia-do-professor.md"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/docs/guia-do-professor.md</path>
<type>file</type>
<content>
1: # Guia do professor — GitHub Actions
2: 
3: Curso introdutório em pt-BR, com **7 exercícios e 180 minutos**. Use a [ementa](ementa.md), os [slides](index.html) e o [gabarito](gabarito.md).
4: 
5: ## Preparação
6: 
7: 1. Publique este material em `fsilva-alt/devops-ghactions`, branch `main`, antes de distribuir os links. Se usar outro endereço, ajuste os links no README e na apresentação. Para hospedar os slides, configure Pages para a pasta `/docs` da `main`.
8: 2. Crie um Codespace com o modelo **Blank** e execute `sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"`. Conclua a autenticação e abra um terminal novo. Verifique o material em `~/devops-ghactions`, os 7 laboratórios em `~/labs`, o atalho `labs` no explorador e o escopo `workflow` do login.
9: 3. Teste os 7 exercícios com uma conta de aluno, incluindo criação dos repositórios públicos, falha/correção no PR e configuração do Pages. Execute `bash tests/rodar.sh`; ela verifica a parte local, mas não substitui essa passagem no GitHub.
10: 4. Peça a preparação do README com um dia de antecedência. Confirme acesso e franquia de Codespaces: ele é o ambiente obrigatório. Se o acesso estiver bloqueado, resolva a permissão com a conta ou organização antes da aula.
11: 5. Combine o local de entrega dos links e a atuação dos monitores. Para cerca de 100 pessoas, use como referência um monitor para cada 25.
12: 
13: ## Modelo mental a repetir
14: 
15: ```text
16: Codespace: editar → commit → push
17:                             ↓ evento no GitHub
18: Actions: workflow → job em um runner → etapas e logs
19:                             ↓
20:                       artefato / Pages
21: ```
22: 
23: Uma instalação feita no Codespace não instala pacotes no runner. Um arquivo criado em um job não aparece automaticamente em outro. Um check local não é uma execução no GitHub. Repita essas distinções nos exercícios 02, 05 e 06.
24: 
25: ## Condução
26: 
27: - A apresentação usa HTML/CSS e funciona sem JavaScript. Abra `docs/index.html` ou o site publicado, escolha um exercício no índice e use os links ao final de cada aula. Clique nas perguntas para expandir as respostas; pelo teclado, use Tab e Enter. Cada aula tem um endereço direto, como `#exercicio-04`.
28: - Comece definindo CI, build e deploy em linguagem simples. Mostre um exemplo, depois nomeie suas partes.
29: - Digite o primeiro YAML ao vivo. Explique dois espaços por nível, `-` para itens da lista e `|` para várias linhas. Os nomes das chaves permanecem em inglês porque fazem parte da linguagem.
30: - Em cada bloco, leia o estado inicial com a turma. Os laboratórios são independentes; ninguém precisa copiar o resultado anterior. Cada um publica `actions-01` a `actions-07` na própria conta, sempre a partir do mesmo Codespace.
31: - No 03, mantenha o check vermelho visível e encontre a primeira mensagem útil no log. Corrigir o código e fazer push é o objetivo; apenas reexecutar o commit quebrado repete a falha.
32: - No 04, use apenas um valor fictício como segredo. Explique a diferença entre variável visível e segredo protegido; não solicite tokens pessoais para esse exercício.
33: - No 05, provoque uma falha temporária e observe `empacotar` como **skipped**. Depois corrija e rode novamente.
34: - No 07, forneça o YAML guiado e explique uma parte por vez. A meta é reconhecer teste → build → publicação e acompanhar a URL, sem exigir memorização das ações do Pages.
35: - Se houver atraso, use o gabarito como apoio para concluir os mesmos 7 exercícios. Reserve o bloco final inteiro para configurar Pages e conferir o site.
36: 
37: ## O que conferir nas entregas
38: 
39: | Exercício | Evidência no GitHub |
40: |---|---|
41: | 01 | Execução manual verde e log com a saudação |
42: | 02 | Execução cujo evento é `push`, com os três testes passando |
43: | 03 | Link do PR, execução vermelha anterior e verde após correção |
44: | 04 | Execução com input próprio, autor, turma e confirmação de presença do segredo |
45: | 05 | Grafo testar → empacotar; exemplo de build pulado quando testar falha |
46: | 06 | Artefato `site` e presença de `index.html` no ZIP baixado |
47: | 07 | Execução de deploy, environment `github-pages` e URL pública funcional |
48: 
49: ## Problemas comuns
50: 
51: | Sintoma | Como resolver |
52: |---|---|
53: | `check.sh: command not found` | Abrir terminal novo ou carregar `source ~/.bashrc`; também funciona `bash "$CURSO_DIR/scripts/check.sh" NN` |
54: | Instalador falhou | Ler a mensagem no terminal, corrigir a causa e executar novamente o comando de instalação do README |
55: | `Author identity unknown` | Configurar `git config --global user.name` e `user.email` com dados do aluno |
56: | Login informa token de ambiente | `unset GH_TOKEN GITHUB_TOKEN` antes de autenticar; abrir terminal novo após a instalação |
57: | Push recusado por falta de `workflow` | `gh auth refresh --hostname github.com --scopes workflow`, depois `gh auth setup-git` e repetir push |
58: | Repositório já existe | Usar nome novo; se já está configurado, usar apenas `git push`, não `gh repo create` |
59: | Workflow não aparece | Conferir `.github/workflows/ci.yml`, commit, push, YAML e permissão em Settings → Actions → General |
60: | Botão Run workflow ausente | O workflow precisa declarar `workflow_dispatch` e estar na branch padrão |
61: | `Invalid workflow file` | Conferir indentação, chaves duplicadas, tipo do valor e mensagem com número da linha |
62: | `app.py` não encontrado | Falta checkout no job; conferir se está na raiz do projeto |
63: | `No module named markdown` no build | Instalar `requirements.txt` naquele job, mesmo que outro job já tenha instalado |
64: | `CURSO_TOKEN` vazio | Cadastrar em Settings → Secrets and variables → Actions → Secrets, no repositório do exercício 04 |
65: | Segundo job pulado | Conferir o resultado do job listado em `needs`; corrigir a causa da falha |
66: | Artefato ausente | Verificar se o build terminou e se `path` aponta para `dist/`, com upload após o build |
67: | Pages retorna erro de configuração | Settings → Pages → Source: GitHub Actions; depois executar novamente na `main` |
68: | Deploy sem permissão | Conferir `pages: write`, `id-token: write` e environment `github-pages` no job publicar |
69: | Site demora a aparecer | Aguardar o deploy terminar e usar a URL da execução; pode levar alguns minutos |
70: 
71: ## Manutenção
72: 
73: | Arquivo | Responsabilidade |
74: |---|---|
75: | `.devcontainer/devcontainer.json` | Ambiente opcional para manutenção do repositório |
76: | `install.sh` | Download e atualização do curso, dependência do verificador, geração dos labs, atalho, PATH e login |
77: | `scripts/lib.sh` | Nomes e números 01–07; caminhos e requisito de Codespaces |
78: | `scripts/labs.sh` | Copia o projeto e o ponto de partida de cada exercício |
79: | `scripts/checks.py` | Requisitos didáticos do YAML, com mensagens em português |
80: | `templates/projeto/` | Aplicação, três testes e build do site |
81: | `docs/guia-do-aluno.md` | Uso do ambiente e resolução de problemas comuns |
82: | `docs/solucoes/` | YAMLs completos, também usados pelos geradores e testes |
83: | `docs/index.html` e `docs/style.css` | Apresentação estática, navegação por âncoras e tema violeta |
84: | `tests/` | Instalação isolada, casos negativos, soluções e consistência do material |
85: 
86: `setup.sh` preserva pastas existentes. `reset.sh NN` recria apenas uma pasta com o marcador `.git/curso-actions/exercicio`; não apaga repositórios no GitHub. O login salvo é reutilizado, mas um login antigo pode exigir ampliação do escopo `workflow`, conforme o README.
87: 
88: Os exemplos usam versões principais explícitas das actions para facilitar a leitura. Ao atualizar essas versões, confira seus requisitos de runner e faça uma execução real dos 7 exemplos. Em projetos de produção, avalie fixar actions a SHAs revisados.
89: 
90: ## Encerramento
91: 
92: Receba os links, peça que expliquem o caminho do commit até a página publicada e oriente a salvar as mudanças com push e parar o Codespace.

(End of file - total 92 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/scripts/labs.sh"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/scripts/labs.sh</path>
<type>file</type>
<content>
1: #!/usr/bin/env bash
2: # Cada exercício recebe um projeto independente e um ponto de partida pronto.
3: # Carregado por setup.sh e reset.sh.
4: gerar_lab() (
5:   local nn="$1" dir base=""
6:   dir="$(lab_dir "$nn")"
7:   [[ ! -e "$dir" && ! -L "$dir" ]] || { erro "A pasta já existe: $dir"; return 1; }
8:   mkdir -p "$dir"
9:   cp -R "$CURSO_DIR/templates/projeto/." "$dir/"
10:   mkdir -p "$dir/.github/workflows"
11:   case "$nn" in
12:     02|04) base=01 ;;
13:     03) base=02 ;;
14:     05) base=03 ;;
15:     06) base=05 ;;
16:     07) base=06 ;;
17:   esac
18:   if [[ -n "$base" ]]; then
19:     cp "$CURSO_DIR/docs/solucoes/$base.yml" "$dir/.github/workflows/ci.yml"
20:   fi
21:   cd "$dir"
22:   g init -q -b main
23:   g add -A
24:   GIT_AUTHOR_DATE='2026-09-01T09:00:00Z' GIT_COMMITTER_DATE='2026-09-01T09:00:00Z' \
25:     g -c user.name='Equipe do curso' -c user.email='curso@example.com' \
26:     commit -q -m "Prepara exercício $nn de GitHub Actions"
27:   mkdir -p .git/curso-actions
28:   printf '%s\n' "$nn" > .git/curso-actions/exercicio
29: )

(End of file - total 29 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/docs/solucoes/04.yml"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/docs/solucoes/04.yml</path>
<type>file</type>
<content>
1: name: Variáveis e contextos
2: 
3: on:
4:   workflow_dispatch:
5:     inputs:
6:       mensagem:
7:         description: Mensagem para a turma
8:         required: true
9:         type: string
10:         default: Olá, turma!
11: 
12: permissions:
13:   contents: read
14: 
15: env:
16:   CURSO: GitHub Actions
17: 
18: jobs:
19:   apresentar:
20:     runs-on: ubuntu-latest
21:     steps:
22:       - name: Mostrar contexto
23:         env:
24:           MENSAGEM: ${{ inputs.mensagem }}
25:           AUTOR: ${{ github.actor }}
26:           TURMA: ${{ vars.TURMA }}
27:         run: |
28:           printf 'Curso: %s\nAutor: %s\nTurma: %s\nMensagem: %s\n' "$CURSO" "$AUTOR" "$TURMA" "$MENSAGEM"
29:       - name: Verificar segredo sem exibir o valor
30:         env:
31:           TOKEN_DEMO: ${{ secrets.CURSO_TOKEN }}
32:         run: |
33:           test -n "$TOKEN_DEMO" || { echo "Cadastre CURSO_TOKEN em Settings > Secrets and variables > Actions"; exit 1; }
34:           echo "Segredo disponível para esta etapa."

(End of file - total 34 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/docs/solucoes/07.yml"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/docs/solucoes/07.yml</path>
<type>file</type>
<content>
1: name: Publicar no Pages
2: 
3: on:
4:   push:
5:     branches: [main]
6:   pull_request:
7:     branches: [main]
8:   workflow_dispatch:
9: 
10: permissions:
11:   contents: read
12: 
13: concurrency:
14:   group: pages-${{ github.ref }}
15:   cancel-in-progress: false
16: 
17: jobs:
18:   testar:
19:     runs-on: ubuntu-latest
20:     steps:
21:       - uses: actions/checkout@v5
22:       - uses: actions/setup-python@v6
23:         with:
24:           python-version: '3.12'
25:       - run: python -m pip install -r requirements.txt
26:       - run: python -m unittest -v
27:   empacotar:
28:     needs: testar
29:     if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'
30:     runs-on: ubuntu-latest
31:     permissions:
32:       contents: read
33:       pages: read
34:     steps:
35:       - uses: actions/checkout@v5
36:       - uses: actions/setup-python@v6
37:         with:
38:           python-version: '3.12'
39:       - run: python -m pip install -r requirements.txt
40:       - run: python build.py
41:       - uses: actions/configure-pages@v5
42:       - uses: actions/upload-pages-artifact@v3
43:         with:
44:           path: dist/
45:   publicar:
46:     needs: empacotar
47:     if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'
48:     runs-on: ubuntu-latest
49:     permissions:
50:       pages: write
51:       id-token: write
52:     environment:
53:       name: github-pages
54:       url: ${{ steps.deploy.outputs.page_url }}
55:     steps:
56:       - name: Publicar
57:         id: deploy
58:         uses: actions/deploy-pages@v4

(End of file - total 58 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/tests/verificar.py",
  "limit": 240
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/tests/verificar.py</path>
<type>file</type>
<content>
1: """Casos de integração do verificador e consistência do material didático."""
2: 
3: import copy
4: import json
5: import os
6: import re
7: import subprocess
8: import sys
9: from pathlib import Path
10: from urllib.parse import unquote
11: 
12: import yaml
13: 
14: CURSO = Path(os.environ["CURSO_DIR"])
15: LABS = Path(os.environ["LABS_DIR"])
16: sys.path.insert(0, str(CURSO / "scripts"))
17: from checks import WorkflowLoader  # noqa: E402
18: 
19: 
20: def check(numero, sucesso, dica=""):
21:     resultado = subprocess.run(
22:         ["bash", str(CURSO / "scripts/check.sh"), f"{numero:02d}"],
23:         text=True, capture_output=True,
24:     )
25:     saida = resultado.stdout + resultado.stderr
26:     assert (resultado.returncode == 0) == sucesso, saida
27:     assert "Traceback" not in saida, saida
28:     assert dica in saida, saida
29: 
30: 
31: def mutacao(numero, original, mudar, dica):
32:     alterado = copy.deepcopy(original)
33:     mudar(alterado)
34:     arquivo = next(LABS.glob(f"{numero:02d}-*")) / ".github/workflows/ci.yml"
35:     arquivo.write_text(yaml.safe_dump(alterado, allow_unicode=True, sort_keys=False), encoding="utf-8")
36:     check(numero, False, dica)
37: 
38: 
39: for numero in range(1, 8):
40:     check(numero, False)
41:     texto = (CURSO / f"docs/solucoes/{numero:02d}.yml").read_text(encoding="utf-8")
42:     arquivo = next(LABS.glob(f"{numero:02d}-*")) / ".github/workflows/ci.yml"
43:     arquivo.write_text(texto, encoding="utf-8")
44:     check(numero, True)
45:     original = yaml.load(texto, Loader=WorkflowLoader)
46:     mutacao(numero, original, lambda w: w.pop("jobs"), "Crie jobs")
47:     mutacao(numero, original, lambda w: w.update(permissions="write-all"), "permissions")
48:     if numero == 1:
49:         mutacao(numero, original, lambda w: w.update(on={"push": None}), "workflow_dispatch")
50:     if numero in (2, 3, 5, 6, 7):
51:         mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"].pop(0), "checkout")
52:         mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"][1]["with"].update({"python-version": 3.12}), "entre aspas")
53:         mutacao(numero, original, lambda w: w["jobs"]["testar"]["steps"][-1].update({"continue-on-error": True}), "Deixe o teste falhar")
54:     if numero == 3:
55:         mutacao(numero, original, lambda w: w["on"].pop("pull_request"), "pull_request")
56:     if numero == 4:
57:         mutacao(numero, original, lambda w: w["jobs"]["apresentar"]["steps"][1]["env"].update(TOKEN_DEMO="valor-em-texto"), "secrets.CURSO_TOKEN")
58:     if numero >= 5:
59:         mutacao(numero, original, lambda w: w["jobs"]["empacotar"].pop("needs"), "needs: testar")
60:         mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"].pop(0), "checkout")
61:     if numero == 6:
62:         mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"][-1]["with"].update(path="build/"), "Envie dist/")
63:         mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"][-1]["with"].update(path=123), "Envie dist/")
64:         mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"].insert(0, w["jobs"]["empacotar"]["steps"].pop()), "antes de enviar")
65:     if numero == 7:
66:         mutacao(numero, original, lambda w: w["jobs"]["publicar"].pop("if"), "exclua pull_request")
67:         mutacao(numero, original, lambda w: w["jobs"]["publicar"]["permissions"].pop("id-token"), "id-token")
68:         mutacao(numero, original, lambda w: w["jobs"]["empacotar"]["steps"][-1].update(uses="actions/upload-artifact@v4"), "upload-pages-artifact")
69:     # YAML inválido, chaves duplicadas e formatos errados devem dar uma dica.
70:     for invalido in ["name: [\n", "name: um\nname: dois\n", "- lista\n", "jobs: []\non: null\n"]:
71:         arquivo.write_text(invalido, encoding="utf-8")
72:         check(numero, False)
73:     arquivo.write_text(texto, encoding="utf-8")
74:     check(numero, True)
75:     print(f"✅ {numero:02d}: início reprovado, solução aprovada e erros detectados.")
76: 
77: for arquivo in [CURSO / "README.md", *CURSO.glob("docs/*.md")]:
78:     texto = arquivo.read_text(encoding="utf-8")
79:     for link in re.findall(r"\]\(([^)]+)\)", texto):
80:         if link.startswith(("https://", "http://", "#")):
81:             continue
82:         destino = unquote(link.split("#")[0])
83:         assert (arquivo.parent / destino).exists(), f"Link quebrado: {arquivo}: {link}"
84: config = json.loads((CURSO / ".devcontainer/devcontainer.json").read_text())
85: assert "scripts/requirements.txt" in config["postCreateCommand"]
86: assert len(list((CURSO / "docs/solucoes").glob("*.yml"))) == 7
87: subprocess.run([sys.executable, str(CURSO / "tests/apresentacao.py")], check=True)
88: print("✅ Exatamente 7 exercícios no site, links locais e configuração do Codespace.")

(End of file - total 88 lines)
</content>
```

---

## Assistant (Build · GPT-6 Astra · 28.0s)

_Thinking:_

**Choosing slide structure**

_Thinking:_

**Estruturo a navegação dos slides**

_Thinking:_

**Ajusto os testes existentes**

Both reference decks use separate concept slides, a commands-and-documentation slide, and a numbered exercise slide. This project currently combines those into one long page per module.

I’ll split each of the seven modules into four slides: two concept slides, one reference slide, and one exercise slide. The existing exercise URLs will open the final practice slide, while the module cards will start with the concepts.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Inspect project instructions, current slides, and the two reference repositories.",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Restructure each module into concept slides, commands and links, and a numbered exercise slide.",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Validate the updated slides and review the changes.",
      "status": "pending",
      "priority": "medium"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Inspect project instructions, current slides, and the two reference repositories.",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Restructure each module into concept slides, commands and links, and a numbered exercise slide.",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Validate the updated slides and review the changes.",
    "status": "pending",
    "priority": "medium"
  }
]
```

---

## Assistant (Build · GPT-6 Astra · 361.3s)

_Thinking:_

**Agrupo etapas e defino colunas**

_Thinking:_

**Edito páginas e estilos**

**Tool: apply_patch**

**Input:**
```json
{
  "patchText": "*** Begin Patch\n*** Update File: /home/lse/projects/ocean/devops-ghactions/docs/index.html\n@@\n-          <a class=\"exercise-card\" href=\"#exercicio-01\"><div class=\"card-top\"><span class=\"card-number\">Módulo 01</span><span class=\"card-time\">15 min</span></div><div><h3>Primeiro workflow</h3><p>Crie um workflow de execução manual e identifique seus jobs, etapas e runner.</p></div><div class=\"card-bottom\"><span>workflow · job · step</span><b aria-hidden=\"true\">↗</b></div></a>\n-          <a class=\"exercise-card\" href=\"#exercicio-02\"><div class=\"card-top\"><span class=\"card-number\">Módulo 02</span><span class=\"card-time\">25 min</span></div><div><h3>Testes no push</h3><p>Configure o ambiente do runner e a execução automática dos testes a cada push.</p></div><div class=\"card-bottom\"><span>push · uses · run</span><b aria-hidden=\"true\">↗</b></div></a>\n-          <a class=\"exercise-card\" href=\"#exercicio-03\"><div class=\"card-top\"><span class=\"card-number\">Módulo 03</span><span class=\"card-time\">25 min</span></div><div><h3>Checks no pull request</h3><p>Veja um teste falhar, encontre a causa e corrija antes de integrar a mudança.</p></div><div class=\"card-bottom\"><span>pull_request · logs · correção</span><b aria-hidden=\"true\">↗</b></div></a>\n-          <a class=\"exercise-card\" href=\"#exercicio-04\"><div class=\"card-top\"><span class=\"card-number\">Módulo 04</span><span class=\"card-time\">20 min</span></div><div><h3>Variáveis e contextos</h3><p>Use variáveis, entradas e segredos para configurar uma execução.</p></div><div class=\"card-bottom\"><span>env · inputs · vars · secrets</span><b aria-hidden=\"true\">↗</b></div></a>\n-          <a class=\"exercise-card\" href=\"#exercicio-05\"><div class=\"card-top\"><span class=\"card-number\">Módulo 05</span><span class=\"card-time\">20 min</span></div><div><h3>Jobs e dependências</h3><p>Configure o build para executar somente após a aprovação dos testes.</p></div><div class=\"card-bottom\"><span>needs · runner · build</span><b aria-hidden=\"true\">↗</b></div></a>\n-          <a class=\"exercise-card\" href=\"#exercicio-06\"><div class=\"card-top\"><span class=\"card-number\">Módulo 06</span><span class=\"card-time\">20 min</span></div><div><h3>Artefatos do build</h3><p>Armazene os arquivos gerados pelo build e baixe o artefato da execução.</p></div><div class=\"card-bottom\"><span>upload-artifact · download</span><b aria-hidden=\"true\">↗</b></div></a>\n-          <a class=\"exercise-card featured\" href=\"#exercicio-07\"><div class=\"card-top\"><span class=\"card-number\">Módulo 07</span><span class=\"card-time\">30 min</span></div><div><h3>Deploy no Pages</h3><p>Publique o cardápio em uma URL pública no GitHub Pages com o workflow fornecido.</p></div><div class=\"card-bottom\"><span>testar → gerar → publicar</span><b aria-hidden=\"true\">↗</b></div></a>\n+          <a class=\"exercise-card\" href=\"#modulo-01\"><div class=\"card-top\"><span class=\"card-number\">Módulo 01</span><span class=\"card-time\">15 min</span></div><div><h3>Primeiro workflow</h3><p>Crie um workflow de execução manual e identifique seus jobs, etapas e runner.</p></div><div class=\"card-bottom\"><span>workflow · job · step</span><b aria-hidden=\"true\">↗</b></div></a>\n+          <a class=\"exercise-card\" href=\"#modulo-02\"><div class=\"card-top\"><span class=\"card-number\">Módulo 02</span><span class=\"card-time\">25 min</span></div><div><h3>Testes no push</h3><p>Configure o ambiente do runner e a execução automática dos testes a cada push.</p></div><div class=\"card-bottom\"><span>push · uses · run</span><b aria-hidden=\"true\">↗</b></div></a>\n+          <a class=\"exercise-card\" href=\"#modulo-03\"><div class=\"card-top\"><span class=\"card-number\">Módulo 03</span><span class=\"card-time\">25 min</span></div><div><h3>Checks no pull request</h3><p>Veja um teste falhar, encontre a causa e corrija antes de integrar a mudança.</p></div><div class=\"card-bottom\"><span>pull_request · logs · correção</span><b aria-hidden=\"true\">↗</b></div></a>\n+          <a class=\"exercise-card\" href=\"#modulo-04\"><div class=\"card-top\"><span class=\"card-number\">Módulo 04</span><span class=\"card-time\">20 min</span></div><div><h3>Variáveis e contextos</h3><p>Use variáveis, entradas e segredos para configurar uma execução.</p></div><div class=\"card-bottom\"><span>env · inputs · vars · secrets</span><b aria-hidden=\"true\">↗</b></div></a>\n+          <a class=\"exercise-card\" href=\"#modulo-05\"><div class=\"card-top\"><span class=\"card-number\">Módulo 05</span><span class=\"card-time\">20 min</span></div><div><h3>Jobs e dependências</h3><p>Configure o build para executar somente após a aprovação dos testes.</p></div><div class=\"card-bottom\"><span>needs · runner · build</span><b aria-hidden=\"true\">↗</b></div></a>\n+          <a class=\"exercise-card\" href=\"#modulo-06\"><div class=\"card-top\"><span class=\"card-number\">Módulo 06</span><span class=\"card-time\">20 min</span></div><div><h3>Artefatos do build</h3><p>Armazene os arquivos gerados pelo build e baixe o artefato da execução.</p></div><div class=\"card-bottom\"><span>upload-artifact · download</span><b aria-hidden=\"true\">↗</b></div></a>\n+          <a class=\"exercise-card featured\" href=\"#modulo-07\"><div class=\"card-top\"><span class=\"card-number\">Módulo 07</span><span class=\"card-time\">30 min</span></div><div><h3>Deploy no Pages</h3><p>Publique o cardápio em uma URL pública no GitHub Pages com o workflow fornecido.</p></div><div class=\"card-bottom\"><span>testar → gerar → publicar</span><b aria-hidden=\"true\">↗</b></div></a>\n@@\n-      <section class=\"closing\"><div><p class=\"eyebrow\">EMENTA</p><h2>Objetivos do curso</h2></div><p>Ler e escrever workflows, investigar falhas nos logs e configurar testes, build e publicação no GitHub Pages. Cada exercício tem um objetivo, um exemplo e um resultado para conferir.</p><a href=\"https://github.com/fsilva-alt/devops-ghactions/blob/main/docs/ementa.md\">Ver a ementa completa <span aria-hidden=\"true\">↗</span></a></section>\n+      <section class=\"closing\"><div><p class=\"eyebrow\">EMENTA</p><h2>Objetivos do curso</h2></div><p>Ler e escrever workflows, investigar falhas nos logs e configurar testes, build e publicação no GitHub Pages. Cada módulo tem dois slides de conceitos, um de comandos e links e um exercício com passos numerados.</p><a href=\"https://github.com/fsilva-alt/devops-ghactions/blob/main/docs/ementa.md\">Ver a ementa completa <span aria-hidden=\"true\">↗</span></a></section>\n@@\n-        <nav class=\"deck-bottom\" aria-label=\"Navegação da introdução\"><a class=\"button\" href=\"#home\">← Índice</a><a class=\"button primary\" href=\"#exercicio-01\">Primeiro exercício →</a></nav>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação da introdução\"><a class=\"button\" href=\"#home\">← Índice</a><a class=\"button primary\" href=\"#modulo-01\">Primeiro módulo →</a></nav>\n       </section>\n-      <section id=\"exercicio-01\" class=\"lesson\" aria-labelledby=\"titulo-01\" tabindex=\"-1\">\n-        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os exercícios</a><span>01 / 07 · 15 minutos</span></div>\n-        <p class=\"eyebrow\">WORKFLOW · JOB · STEP</p>\n+      <section id=\"modulo-01\" class=\"lesson\" data-module=\"01\" data-kind=\"concept\" aria-labelledby=\"titulo-01\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 01 · 15 minutos · Slide 1 / 4</span></div>\n+        <p class=\"eyebrow\">CONCEITO · WORKFLOW · JOB · STEP</p>\n         <h2 id=\"titulo-01\">Primeiro workflow</h2>\n         <div class=\"slide-columns\">\n           <div class=\"slide-stack\">\n-            <p class=\"lead\">Crie um workflow com execução manual e confira a mensagem nos logs.</p>\n-            <div class=\"box\"><h3>As partes da automação</h3><p><strong>Workflow:</strong> arquivo YAML que descreve o processo.</p><p><strong>Evento:</strong> o que inicia a execução; aqui, <code>workflow_dispatch</code>, um clique manual.</p><p><strong>Job:</strong> grupo de etapas que executa em um runner.</p><p><strong>Runner:</strong> máquina que executa o job.</p><p><strong>Step:</strong> cada etapa da lista <code>steps</code>.</p></div>\n-            <div class=\"callout\">YAML usa espaços para a indentação. O traço inicia um item da lista. Salve o arquivo em <code>.github/workflows/ci.yml</code>.</div>\n+            <p class=\"lead\">Um workflow descreve uma automação. Um evento inicia sua execução no GitHub Actions.</p>\n+            <div class=\"flow\"><span>Evento</span><b aria-hidden=\"true\">→</b><span>Workflow</span><b aria-hidden=\"true\">→</b><span>Job → Steps</span></div>\n+            <div class=\"callout\">No Codespaces você escreve e publica o arquivo. O runner do Actions executa os comandos em outra máquina.</div>\n           </div>\n+          <div class=\"box\"><h3>As partes da automação</h3><p><strong>Workflow:</strong> arquivo YAML em <code>.github/workflows/</code> que descreve o processo.</p><p><strong>Evento:</strong> o que inicia a execução; aqui, <code>workflow_dispatch</code>, um clique manual.</p><p><strong>Job:</strong> grupo de etapas que executa em um runner.</p><p><strong>Runner:</strong> máquina que executa o job; <code>ubuntu-latest</code> escolhe um ambiente Linux hospedado pelo GitHub.</p><p><strong>Step:</strong> cada etapa da lista <code>steps</code>.</p></div>\n+        </div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 01, slide 1\"><a class=\"button\" href=\"#intro\">← Introdução</a><a class=\"button primary\" href=\"#modulo-01-exemplo\">Ler o YAML →</a></nav>\n+      </section>\n+      <section id=\"modulo-01-exemplo\" class=\"lesson\" data-module=\"01\" data-kind=\"concept\" aria-labelledby=\"yaml-01\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 01 · 15 minutos · Slide 2 / 4</span></div>\n+        <p class=\"eyebrow\">CONCEITO · LENDO O YAML</p>\n+        <h2 id=\"yaml-01\">Do arquivo à primeira execução</h2>\n+        <div class=\"slide-columns\">\n+          <div class=\"slide-stack\"><p class=\"lead\">A indentação mostra quais configurações pertencem ao workflow, ao job e à etapa.</p><div class=\"box\"><h3>Como ler o exemplo</h3><p><code>name</code> dá um nome ao workflow. <code>on</code> define os eventos.</p><p><code>jobs</code> contém o job <code>boas-vindas</code>. Dentro dele, <code>runs-on</code> escolhe o runner e <code>steps</code> lista as etapas.</p><p><code>run</code> executa o comando da saudação. <code>permissions: contents: read</code> limita o acesso ao conteúdo do repositório à leitura.</p></div><div class=\"callout\">Use espaços, não tabulações. O traço inicia um item da lista. Salve este YAML em <code>.github/workflows/ci.yml</code>.</div></div>\n           <pre><code>name: Boas-vindas\n@@\n-        <div class=\"lesson-practice slide-columns\">\n-          <div class=\"slide-stack\"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/01-primeiro-workflow\n-code .github/workflows/ci.yml\n-check.sh 01</code></pre><ol class=\"task-list\"><li>Crie e salve o arquivo com o exemplo acima.</li><li>Confira com o check, faça commit e publique em <code>actions-01</code>.</li><li>Abra Actions → Boas-vindas → Run workflow. Selecione <code>main</code>.</li><li>Abra o job e a etapa para localizar a saudação no log.</li></ol></div>\n-          <div class=\"slide-stack\"><div class=\"box\"><h3>Sua entrega</h3><p>Link da execução manual verde e a mensagem <code>Olá, GitHub Actions!</code> no log.</p></div><details class=\"box\"><summary>O echo executou no Codespace ou em um runner?</summary><p>Em um runner do Actions. O Codespace foi usado para escrever e publicar o workflow.</p></details><div class=\"callout\">Se não houver execução após o push, está correto: neste exercício o único evento é manual. O botão aparece quando o workflow está na branch padrão.</div><a href=\"https://docs.github.com/pt/actions/get-started/understand-github-actions\">Consultar a documentação oficial ↗</a></div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 01, slide 2\"><a class=\"button\" href=\"#modulo-01\">← Conceitos</a><a class=\"button primary\" href=\"#modulo-01-referencia\">Comandos e links →</a></nav>\n+      </section>\n+      <section id=\"modulo-01-referencia\" class=\"lesson\" data-module=\"01\" data-kind=\"reference\" aria-labelledby=\"referencia-01\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 01 · 15 minutos · Slide 3 / 4</span></div>\n+        <p class=\"eyebrow\">REFERÊNCIA · PRIMEIRO WORKFLOW</p>\n+        <h2 id=\"referencia-01\">Comandos úteis e links</h2>\n+        <div class=\"slide-columns\">\n+          <div class=\"table-wrap\"><table class=\"command-table\"><thead><tr><th scope=\"col\">Comando</th><th scope=\"col\">Para quê</th></tr></thead><tbody>\n+            <tr><td><code>code .github/workflows/ci.yml</code></td><td>Abrir o workflow no editor.</td></tr>\n+            <tr><td><code>check.sh 01</code></td><td>Conferir o YAML e os requisitos locais.</td></tr>\n+            <tr><td><code>git add .github/workflows/ci.yml</code></td><td>Preparar o arquivo para o commit.</td></tr>\n+            <tr><td><code>git commit -m \"Cria workflow\"</code></td><td>Registrar a versão do workflow.</td></tr>\n+            <tr><td><code>gh repo create actions-01 --public --source=. --remote=origin --push</code></td><td>Criar o repositório e enviar o primeiro commit.</td></tr>\n+            <tr><td><code>gh browse --actions</code></td><td>Abrir a aba Actions no navegador.</td></tr>\n+          </tbody></table></div>\n+          <div class=\"slide-stack\"><div class=\"box\"><h3>Documentação</h3><ul class=\"resource-links\"><li><a href=\"https://docs.github.com/pt/actions/get-started/understand-github-actions\">Entender o GitHub Actions</a></li><li><a href=\"https://cli.github.com/manual/gh_repo_create\">GitHub CLI: criar um repositório</a></li><li><a href=\"https://cli.github.com/manual/gh_browse\">GitHub CLI: abrir no navegador</a></li><li><a href=\"guia-do-aluno.md\">Guia do aluno e problemas comuns</a></li></ul></div><div class=\"callout\">Execute <code>gh repo create</code> uma vez por laboratório. Nas alterações seguintes, use <code>git add</code>, <code>git commit</code> e <code>git push</code>.</div></div>\n         </div>\n-        <nav class=\"deck-bottom\" aria-label=\"Navegação do exercício 01\"><a class=\"button\" href=\"#intro\">← Introdução</a><a class=\"button primary\" href=\"#exercicio-02\">Testes no push →</a></nav>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 01, slide 3\"><a class=\"button\" href=\"#modulo-01-exemplo\">← YAML</a><a class=\"button primary\" href=\"#exercicio-01\">O exercício →</a></nav>\n       </section>\n-      <section id=\"exercicio-02\" class=\"lesson\" aria-labelledby=\"titulo-02\" tabindex=\"-1\">\n-        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os exercícios</a><span>02 / 07 · 25 minutos</span></div>\n-        <p class=\"eyebrow\">PUSH · USES · RUN</p>\n+      <section id=\"exercicio-01\" class=\"lesson\" data-module=\"01\" data-kind=\"exercise\" aria-labelledby=\"tarefa-01\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 01 · 15 minutos · Slide 4 / 4</span></div>\n+        <p class=\"eyebrow\">EXERCÍCIO 01 · PRATIQUE NO CODESPACES</p>\n+        <h2 id=\"tarefa-01\">Primeiro workflow: sua vez</h2>\n+        <div class=\"slide-columns exercise-columns\">\n+          <ol class=\"task-list\">\n+            <li><p>No terminal do Codespaces, entre no laboratório e abra o arquivo:</p><pre><code>cd ~/labs/01-primeiro-workflow\n+code .github/workflows/ci.yml</code></pre></li>\n+            <li>Escreva o <a href=\"#modulo-01-exemplo\">YAML de boas-vindas</a> no editor e salve com <strong>Ctrl+S</strong> ou <strong>Cmd+S</strong>.</li>\n+            <li><p>Confira o arquivo. Depois de o check aprovar, faça commit e publique:</p><pre><code>check.sh 01\n+git add .github/workflows/ci.yml\n+git commit -m \"Cria workflow de boas-vindas\"\n+gh repo create actions-01 --public --source=. --remote=origin --push\n+gh browse --actions</code></pre></li>\n+            <li>No GitHub, abra <strong>Boas-vindas → Run workflow</strong>, selecione <code>main</code> e confirme a execução.</li>\n+            <li>Aguarde o resultado verde. Abra o job e a etapa <strong>Cumprimentar a turma</strong>, localize a saudação e guarde o link da execução.</li>\n+          </ol>\n+          <div class=\"slide-stack\"><div class=\"box\"><h3>Ponto de partida</h3><p>Projeto pronto e pasta <code>.github/workflows/</code> vazia. Você cria o primeiro YAML neste laboratório.</p></div><div class=\"box\"><h3>Sua entrega</h3><p>Link da execução manual verde e a mensagem <code>Olá, GitHub Actions!</code> no log.</p></div><details class=\"box\"><summary>O echo executou no Codespace ou em um runner?</summary><p>Em um runner do Actions. O Codespace foi usado para escrever e publicar o workflow.</p></details><div class=\"callout\">Se não houver execução após o push, está correto: o único evento é manual. O botão aparece quando o workflow está na branch padrão <code>main</code>.</div></div>\n+        </div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 01, slide 4\"><a class=\"button\" href=\"#modulo-01-referencia\">← Comandos e links</a><a class=\"button primary\" href=\"#modulo-02\">Testes no push →</a></nav>\n+      </section>\n+      <section id=\"modulo-02\" class=\"lesson\" data-module=\"02\" data-kind=\"concept\" aria-labelledby=\"titulo-02\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 02 · 25 minutos · Slide 1 / 4</span></div>\n+        <p class=\"eyebrow\">CONCEITO · INTEGRAÇÃO CONTÍNUA</p>\n         <h2 id=\"titulo-02\">Testes no push</h2>\n         <div class=\"slide-columns\">\n-          <div class=\"slide-stack\"><p class=\"lead\">Configure o ambiente do runner para executar os testes a cada push.</p><div class=\"box\"><h3>Integração contínua</h3><p><strong>CI</strong> significa integração contínua: verificar mudanças automaticamente.</p><p><code>uses</code> chama uma action pronta, com versão explícita.</p><p><code>with</code> configura as entradas dessa action.</p><p><code>run</code> executa um comando no runner.</p></div><div class=\"callout\">Checkout vem primeiro porque o runner precisa receber os arquivos do projeto. As etapas de um job executam em sequência.</div></div>\n+          <div class=\"slide-stack\"><p class=\"lead\">CI significa integração contínua: verificar as mudanças automaticamente quando chegam ao repositório.</p><div class=\"flow\"><span>Commit + push</span><b aria-hidden=\"true\">→</b><span>Runner</span><b aria-hidden=\"true\">→</b><span>Testes</span></div><div class=\"box\"><h3>O evento push</h3><p><code>push</code> inicia uma execução quando commits são enviados ao GitHub. O filtro <code>branches: [main]</code> limita o evento à main.</p><p>O resultado pertence à revisão que iniciou a execução. O hash do commit permite identificar qual versão foi testada.</p></div></div>\n+          <div class=\"slide-stack\"><div class=\"box\"><h3>Preparar o runner</h3><p>O runner começa separado do seu Codespaces: precisa receber o código, configurar o Python e instalar as dependências antes dos testes.</p><p><code>actions/checkout</code> obtém os arquivos do repositório. <code>actions/setup-python</code> configura a versão do Python.</p></div><details class=\"box\"><summary>Instalar no Codespace também instala no runner?</summary><p>Não. São máquinas separadas. O workflow precisa preparar seu próprio ambiente.</p></details><div class=\"callout\">As etapas de um job executam em sequência: checkout → Python → dependências → testes.</div></div>\n+        </div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 02, slide 1\"><a class=\"button\" href=\"#exercicio-01\">← Exercício 01</a><a class=\"button primary\" href=\"#modulo-02-exemplo\">Actions e comandos →</a></nav>\n+      </section>\n+      <section id=\"modulo-02-exemplo\" class=\"lesson\" data-module=\"02\" data-kind=\"concept\" aria-labelledby=\"yaml-02\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 02 · 25 minutos · Slide 2 / 4</span></div>\n+        <p class=\"eyebrow\">CONCEITO · USES · WITH · RUN</p>\n+        <h2 id=\"yaml-02\">Actions prontas e comandos do projeto</h2>\n+        <div class=\"slide-columns\">\n+          <div class=\"slide-stack\"><div class=\"box\"><h3>Três chaves para ler as etapas</h3><p><code>uses</code> chama uma action pronta. A parte depois de <code>@</code> indica sua versão.</p><p><code>with</code> configura as entradas dessa action, como a versão do Python.</p><p><code>run</code> executa um comando no runner, como instalar pacotes ou rodar os testes.</p></div><p class=\"lead\">Neste workflow, o job <code>testar</code> executa os três testes que já vêm com o projeto.</p><div class=\"callout\">Use <code>'3.12'</code> entre aspas: é uma versão, não um número decimal. Substitua todo o workflow de boas-vindas por este exemplo.</div></div>\n@@\n-        <div class=\"lesson-practice slide-columns\">\n-          <div class=\"slide-stack\"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/02-testes-no-push\n-python3 -m unittest -v\n-code .github/workflows/ci.yml\n-check.sh 02</code></pre><ol class=\"task-list\"><li>Execute os três testes prontos e procure <code>OK</code>.</li><li>Substitua a saudação pelo workflow acima.</li><li>Confira, faça commit e publique em <code>actions-02</code>.</li><li>Edite o título do cardápio, faça novo commit e push. Acompanhe outra execução.</li></ol></div>\n-          <div class=\"slide-stack\"><div class=\"box\"><h3>Sua entrega</h3><p>Uma execução verde disparada por <code>push</code>, com três testes aprovados. Localize o hash do commit na página da execução.</p></div><details class=\"box\"><summary>Instalar no Codespace também instala no runner?</summary><p>Não. São máquinas separadas. O workflow precisa preparar seu próprio ambiente: código, Python e dependências.</p></details><div class=\"callout\">Use <code>'3.12'</code> entre aspas: é uma versão, não um número decimal.</div><a href=\"https://docs.github.com/pt/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows\">Consultar os eventos disponíveis ↗</a></div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 02, slide 2\"><a class=\"button\" href=\"#modulo-02\">← CI e runner</a><a class=\"button primary\" href=\"#modulo-02-referencia\">Comandos e links →</a></nav>\n+      </section>\n+      <section id=\"modulo-02-referencia\" class=\"lesson\" data-module=\"02\" data-kind=\"reference\" aria-labelledby=\"referencia-02\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 02 · 25 minutos · Slide 3 / 4</span></div>\n+        <p class=\"eyebrow\">REFERÊNCIA · TESTES NO PUSH</p>\n+        <h2 id=\"referencia-02\">Comandos úteis e links</h2>\n+        <div class=\"slide-columns\">\n+          <div class=\"table-wrap\"><table class=\"command-table\"><thead><tr><th scope=\"col\">Comando</th><th scope=\"col\">Para quê</th></tr></thead><tbody>\n+            <tr><td><code>python3 -m unittest -v</code></td><td>Executar os três testes no Codespace.</td></tr>\n+            <tr><td><code>python -m pip install -r requirements.txt</code></td><td>Instalar as dependências no ambiente do Python.</td></tr>\n+            <tr><td><code>check.sh 02</code></td><td>Conferir o workflow de testes.</td></tr>\n+            <tr><td><code>git diff</code></td><td>Revisar mudanças antes de adicioná-las.</td></tr>\n+            <tr><td><code>git push</code></td><td>Enviar novos commits e disparar o CI na main.</td></tr>\n+            <tr><td><code>gh run list</code></td><td>Listar execuções e seus resultados.</td></tr>\n+            <tr><td><code>gh browse --actions</code></td><td>Abrir execuções, etapas e logs no navegador.</td></tr>\n+          </tbody></table></div>\n+          <div class=\"box\"><h3>Documentação</h3><ul class=\"resource-links\"><li><a href=\"https://docs.github.com/pt/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows\">Eventos que disparam workflows</a></li><li><a href=\"https://github.com/actions/checkout\">Action: checkout</a></li><li><a href=\"https://github.com/actions/setup-python\">Action: setup-python</a></li><li><a href=\"https://cli.github.com/manual/gh_run_list\">GitHub CLI: listar execuções</a></li></ul></div>\n         </div>\n-        <nav class=\"deck-bottom\" aria-label=\"Navegação do exercício 02\"><a class=\"button\" href=\"#exercicio-01\">← Primeiro workflow</a><a class=\"button primary\" href=\"#exercicio-03\">Checks no PR →</a></nav>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 02, slide 3\"><a class=\"button\" href=\"#modulo-02-exemplo\">← Actions e comandos</a><a class=\"button primary\" href=\"#exercicio-02\">O exercício →</a></nav>\n       </section>\n-      <section id=\"exercicio-03\" class=\"lesson\" aria-labelledby=\"titulo-03\" tabindex=\"-1\">\n-        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os exercícios</a><span>03 / 07 · 25 minutos</span></div>\n-        <p class=\"eyebrow\">PULL_REQUEST · LOGS · CORREÇÃO</p>\n+      <section id=\"exercicio-02\" class=\"lesson\" data-module=\"02\" data-kind=\"exercise\" aria-labelledby=\"tarefa-02\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 02 · 25 minutos · Slide 4 / 4</span></div>\n+        <p class=\"eyebrow\">EXERCÍCIO 02 · PRATIQUE NO CODESPACES</p>\n+        <h2 id=\"tarefa-02\">Testes no push: sua vez</h2>\n+        <div class=\"slide-columns exercise-columns\">\n+          <ol class=\"task-list\">\n+            <li><p>Entre no laboratório, execute os testes e procure <code>OK</code>:</p><pre><code>cd ~/labs/02-testes-no-push\n+python3 -m unittest -v\n+code .github/workflows/ci.yml</code></pre></li>\n+            <li>Substitua o workflow de saudação pelo <a href=\"#modulo-02-exemplo\">exemplo de CI</a> e salve o arquivo.</li>\n+            <li><p>Confira, faça commit e publique o laboratório:</p><pre><code>check.sh 02\n+git add .github/workflows/ci.yml\n+git commit -m \"Executa testes no push\"\n+gh repo create actions-02 --public --source=. --remote=origin --push\n+gh browse --actions</code></pre></li>\n+            <li>Abra a execução iniciada por <code>push</code>. No job <code>testar</code>, confira as quatro etapas e os três testes aprovados.</li>\n+            <li><p>No Codespace, abra <code>code cardapio.md</code>, personalize o título e salve. Envie a alteração e confira outra execução verde, com o hash do novo commit:</p><pre><code>git add cardapio.md\n+git commit -m \"Personaliza título do cardápio\"\n+git push</code></pre></li>\n+          </ol>\n+          <div class=\"slide-stack\"><div class=\"box\"><h3>Ponto de partida</h3><p>Projeto com três testes prontos e o workflow manual de saudação. Este laboratório é independente do exercício 01.</p></div><div class=\"box\"><h3>Sua entrega</h3><p>Link de uma execução verde disparada por <code>push</code>, com três testes aprovados. Localize o hash do commit na página da execução.</p></div><div class=\"callout\">O check local analisa o YAML. A aprovação dos testes no Actions confirma que o runner executou o projeto.</div></div>\n+        </div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 02, slide 4\"><a class=\"button\" href=\"#modulo-02-referencia\">← Comandos e links</a><a class=\"button primary\" href=\"#modulo-03\">Checks no PR →</a></nav>\n+      </section>\n+      <section id=\"modulo-03\" class=\"lesson\" data-module=\"03\" data-kind=\"concept\" aria-labelledby=\"titulo-03\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 03 · 25 minutos · Slide 1 / 4</span></div>\n+        <p class=\"eyebrow\">CONCEITO · PULL_REQUEST</p>\n         <h2 id=\"titulo-03\">Checks no pull request</h2>\n         <div class=\"slide-columns\">\n-          <div class=\"slide-stack\"><p class=\"lead\">Analise os logs de um teste com falha e corrija o código antes de integrar a mudança.</p><div class=\"box\"><h3>Verificação de pull requests</h3><p><code>pull_request</code> executa os testes quando um PR é aberto ou atualizado. O filtro <code>branches</code> indica o <strong>destino</strong> do PR.</p><p>Abra a etapa que falhou. Compare o valor esperado com o recebido. O teste de três unidades espera 1500 centavos, mas a soma incorreta retorna 503.</p></div><div class=\"callout\">Cada execução corresponde a uma revisão do código. Reexecutar um commit quebrado não aplica a correção que ainda está só no Codespace.</div></div>\n+          <div class=\"slide-stack\"><p class=\"lead\">Um check mostra o resultado dos testes de uma proposta de mudança antes do merge.</p><div class=\"box\"><h3>Verificação de pull requests</h3><p><code>pull_request</code> executa os testes quando um PR é aberto ou atualizado. O filtro <code>branches</code> indica o <strong>destino</strong> do PR, aqui a main.</p><p>O push na branch <code>teste-do-ci</code> atualiza o PR aberto e produz um novo check, sem precisar integrar a mudança.</p></div><details class=\"box\"><summary>Um check vermelho sempre impede o merge?</summary><p>Só quando regras do repositório exigem aquele check. Aqui aprendemos a observar e interpretar o resultado.</p></details></div>\n           <div class=\"slide-stack\"><pre><code># Substitua apenas o bloco on:\n@@\n-  workflow_dispatch:</code></pre><pre><code># Falha proposital em app.py:\n+  workflow_dispatch:</code></pre><div class=\"callout\">Mantenha o job <code>testar</code>. A mudança aqui é quando ele executa: na main por push e nos PRs que têm a main como destino.</div></div>\n+        </div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 03, slide 1\"><a class=\"button\" href=\"#exercicio-02\">← Exercício 02</a><a class=\"button primary\" href=\"#modulo-03-exemplo\">Ler a falha →</a></nav>\n+      </section>\n+      <section id=\"modulo-03-exemplo\" class=\"lesson\" data-module=\"03\" data-kind=\"concept\" aria-labelledby=\"logs-03\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 03 · 25 minutos · Slide 2 / 4</span></div>\n+        <p class=\"eyebrow\">CONCEITO · LOGS · CORREÇÃO</p>\n+        <h2 id=\"logs-03\">Da falha à causa</h2>\n+        <div class=\"slide-columns\">\n+          <div class=\"slide-stack\"><p class=\"lead\">Abra o job e a etapa que falhou. Procure o teste, a linha indicada e os valores comparados.</p><div class=\"box\"><h3>O erro do nosso exemplo</h3><p>O teste de três unidades de 500 centavos espera <strong>1500</strong>. A soma incorreta retorna <strong>503</strong>.</p><p>O teste está correto: o código precisa multiplicar o preço pela quantidade. O log ajuda a localizar essa causa.</p></div><div class=\"callout\">Cada execução corresponde a uma revisão do código. Reexecutar um commit quebrado não aplica a correção que ainda está só no Codespace.</div></div>\n+          <div class=\"slide-stack\"><pre><code># Falha proposital em app.py:\n return preco_centavos + quantidade\n \n # Correção:\n-return preco_centavos * quantidade</code></pre></div>\n+return preco_centavos * quantidade</code></pre><div class=\"flow\"><span>Check vermelho</span><b aria-hidden=\"true\">→</b><span>Corrigir + push</span><b aria-hidden=\"true\">→</b><span>Novo check</span></div><div class=\"box\"><h3>Preserve a evidência</h3><p>A execução antiga continua mostrando a falha; a nova mostra a correção. Guarde os dois links para explicar o que mudou.</p></div></div>\n         </div>\n-        <div class=\"lesson-practice slide-columns\">\n-          <div class=\"slide-stack\"><h3>Pratique no Codespaces</h3><pre><code>cd ~/labs/03-checks-no-pull-request\n-code .github/workflows/ci.yml\n-check.sh 03</code></pre><ol class=\"task-list\"><li>Acrescente o evento e publique a main em <code>actions-03</code>.</li><li>Crie a branch <code>teste-do-ci</code>. Troque a multiplicação por soma em <code>app.py</code>.</li><li>Faça commit, push e abra o PR para main. Leia o erro em Checks → testar → Testar.</li><li>Corrija a multiplicação. Faça novo commit e push na mesma branch e confira o novo check.</li></ol></div>\n-          <div class=\"slide-stack\"><div class=\"box\"><h3>Sua entrega</h3><p>Link do PR e das execuções vermelha e verde. Explique qual linha causava o erro. O PR pode ficar aberto para avaliação.</p></div><details class=\"box\"><summary>Um check vermelho sempre impede o merge?</summary><p>Só quando regras do repositório exigem aquele check. Aqui aprendemos a observar e interpretar o resultado.</p></details><a href=\"https://docs.github.com/pt/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs\">Consultar o guia de logs ↗</a></div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 03, slide 2\"><a class=\"button\" href=\"#modulo-03\">← Checks no PR</a><a class=\"button primary\" href=\"#modulo-03-referencia\">Comandos e links →</a></nav>\n+      </section>\n+      <section id=\"modulo-03-referencia\" class=\"lesson\" data-module=\"03\" data-kind=\"reference\" aria-labelledby=\"referencia-03\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 03 · 25 minutos · Slide 3 / 4</span></div>\n+        <p class=\"eyebrow\">REFERÊNCIA · CHECKS NO PULL REQUEST</p>\n+        <h2 id=\"referencia-03\">Comandos úteis e links</h2>\n+        <div class=\"slide-columns\">\n+          <div class=\"table-wrap\"><table class=\"command-table\"><thead><tr><th scope=\"col\">Comando</th><th scope=\"col\">Para quê</th></tr></thead><tbody>\n+            <tr><td><code>check.sh 03</code></td><td>Conferir o evento pull_request e o job de testes.</td></tr>\n+            <tr><td><code>git switch -c teste-do-ci</code></td><td>Criar e entrar na branch da mudança.</td></tr>\n+            <tr><td><code>git push -u origin teste-do-ci</code></td><td>Publicar a branch e configurar seu remoto.</td></tr>\n+            <tr><td><code>gh pr create --base main --fill</code></td><td>Abrir o PR para main usando a mensagem do commit.</td></tr>\n+            <tr><td><code>gh pr view --web</code></td><td>Abrir o PR da branch atual no navegador.</td></tr>\n+            <tr><td><code>gh pr checks</code></td><td>Consultar os checks do PR.</td></tr>\n+            <tr><td><code>gh run view --log-failed</code></td><td>Selecionar uma execução e ler os logs com falha.</td></tr>\n+          </tbody></table></div>\n+          <div class=\"box\"><h3>Documentação</h3><ul class=\"resource-links\"><li><a href=\"https://docs.github.com/pt/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs\">Como ler os logs de uma execução</a></li><li><a href=\"https://cli.github.com/manual/gh_pr_create\">GitHub CLI: criar um pull request</a></li><li><a href=\"https://cli.github.com/manual/gh_pr_checks\">GitHub CLI: consultar checks</a></li><li><a href=\"https://cli.github.com/manual/gh_run_view\">GitHub CLI: consultar execuções e logs</a></li></ul></div>\n         </div>\n-        <nav class=\"deck-bottom\" aria-label=\"Navegação do exercício 03\"><a class=\"button\" href=\"#exercicio-02\">← Testes no push</a><a class=\"button primary\" href=\"#exercicio-04\">Variáveis e contextos →</a></nav>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 03, slide 3\"><a class=\"button\" href=\"#modulo-03-exemplo\">← Logs e correção</a><a class=\"button primary\" href=\"#exercicio-03\">O exercício →</a></nav>\n+      </section>\n+      <section id=\"exercicio-03\" class=\"lesson\" data-module=\"03\" data-kind=\"exercise\" aria-labelledby=\"tarefa-03\" tabindex=\"-1\">\n+        <div class=\"deck-top\"><a href=\"#home\" class=\"back\">← Todos os módulos</a><span>Módulo 03 · 25 minutos · Slide 4 / 4</span></div>\n+        <p class=\"eyebrow\">EXERCÍCIO 03 · PRATIQUE NO CODESPACES</p>\n+        <h2 id=\"tarefa-03\">Checks no pull request: sua vez</h2>\n+        <div class=\"slide-columns exercise-columns\">\n+          <ol class=\"task-list\">\n+            <li><p>Abra o workflow, acrescente <a href=\"#modulo-03\">o evento pull_request</a> ao bloco <code>on</code> e salve:</p><pre><code>cd ~/labs/03-checks-no-pull-request\n+code .github/workflows/ci.yml</code></pre></li>\n+            <li><p>Confira e publique a main antes de criar a branch:</p><pre><code>check.sh 03\n+git add .github/workflows/ci.yml\n+git commit -m \"Verifica pull requests\"\n+gh repo create actions-03 --public --source=. --remote=origin --push</code></pre></li>\n+            <li><p>Crie a branch. Em <code>app.py</code>, troque <code>preco_centavos * quantidade</code> por <code>preco_centavos + quantidade</code> e salve:</p><pre><code>git switch -c teste-do-ci\n+code app.py</code></pre></li>\n+            <li><p>Envie a falha proposital e abra o PR:</p><pre><code>git add app.py\n+git commit -m \"Demonstra falha no cálculo\"\n+git push -u origin teste-do-ci\n+gh pr create --base main --fill\n+gh pr view --web</code></pre></li>\n+            <li>Aguarde o check vermelho. Em <strong>Checks → testar</strong>, abra a etapa dos testes, encontre a comparação entre 503 e 1500 e guarde o link da execução.</li>\n+            <li><p>Restaure a multiplicação em <code>app.py</code>, salve e envie a correção na mesma branch. Confira o novo check verde e guarde os links:</p><pre><code>python3 -m unittest -v\n+git add app.py\n+git commit -m \"Corrige cálculo do total\"\n+git push</code></pre></li>\n+          </ol>\n+          <div class=\"slide-stack\"><div class=\"box\"><h3>Ponto de partida</h3><p>Workflow de testes no push pronto, com o cálculo correto. Você adiciona a verificação de PRs e provoca uma falha temporária no código.</p></div><div class=\"box\"><h3>Sua entrega</h3><p>Link do PR e das execuções vermelha e verde. Explique qual linha causava o erro. O PR pode ficar aberto para avaliação.</p></div><div class=\"callout\">Corrija o código e faça um novo push. O botão de reexecução do commit antigo apenas repete a mesma falha.</div></div>\n+        </div>\n+        <nav class=\"deck-bottom\" aria-label=\"Navegação do módulo 03, slide 4\"><a class=\"button\" href=\"#modulo-03-referencia\">← Comandos e links</a><a class=\"button primary\" href=\"#modulo-04\">Variáveis e contextos →</a></nav>\n       </section>\n*** End Patch"
}
```

**Output:**
```
Success. Updated the following files:
M docs/index.html
```

---

## User

maybe the check script can use nektos/act to simulate the github actions behavior

---

## User

the codespaces has docker available

---

## User

use nos exercicios a mesma temática das receitas utilizadas nos repos de referencia

---

## Assistant (Build · GPT-6 Astra · 17.8s)

_Thinking:_

**Scoping optional act checks**

_Thinking:_

**Alinho os exercícios do livro**

Vou usar o livro de receitas como tema dos sete exercícios, seguindo os repositórios de referência.

Com Docker disponível no Codespaces, o `act` pode executar localmente os jobs de testes e build. Vou verificar como integrá-lo ao `check.sh`; a publicação no Pages e os checks de PR ainda precisam ser conferidos no GitHub.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Inspect project instructions, current slides, and the two reference repositories.",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Restructure all seven modules into concept, reference, and numbered exercise slides using the recipe-book theme.",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Align lab templates, solutions, and supporting material with the recipes used in the reference courses.",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Integrate nektos/act into local checking for supported jobs in Docker-enabled Codespaces.",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Validate slide navigation, recipe labs, and local workflow checking; review the changes.",
      "status": "pending",
      "priority": "medium"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Inspect project instructions, current slides, and the two reference repositories.",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Restructure all seven modules into concept, reference, and numbered exercise slides using the recipe-book theme.",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Align lab templates, solutions, and supporting material with the recipes used in the reference courses.",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Integrate nektos/act into local checking for supported jobs in Docker-enabled Codespaces.",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Validate slide navigation, recipe labs, and local workflow checking; review the changes.",
    "status": "pending",
    "priority": "medium"
  }
]
```

---

## Assistant (Build · GPT-6 Astra · 15.7s)

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/scripts/check.sh"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/scripts/check.sh</path>
<type>file</type>
<content>
1: #!/usr/bin/env bash
2: # Validação estática: não executa o workflow nem consulta a conta no GitHub.
3: source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
4: exigir_codespaces
5: [[ $# -le 1 ]] || { erro "Uso: check.sh [01–07]"; exit 2; }
6: nn="$(resolver_lab "${1:-}")" || exit 2
7: dir="$(lab_dir "$nn")"
8: [[ -d "$dir" ]] || { erro "Laboratório ausente. Rode setup.sh."; exit 2; }
9: python="$CURSO_DIR/.venv/bin/python"
10: [[ -x "$python" ]] || { erro "Verificador não instalado. Rode: sh \"$CURSO_DIR/install.sh\""; exit 2; }
11: exec "$python" "$SCRIPTS_DIR/checks.py" "$nn" "$dir"

(End of file - total 11 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/install.sh"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/install.sh</path>
<type>file</type>
<content>
1: #!/bin/sh
2: # Num Codespace criado com o modelo Blank, execute:
3: # sh -c "$(curl -fsSL https://raw.githubusercontent.com/fsilva-alt/devops-ghactions/main/install.sh)"
4: #
5: # Baixa ou atualiza o curso, prepara os laboratórios, cria o atalho labs,
6: # autentica o GitHub CLI e configura os comandos nos novos terminais.
7: # Pode ser executado novamente sem apagar o trabalho nos laboratórios.
8: # Variáveis opcionais: CURSO_REPO, CURSO_RAMO, CURSO_DIR e LABS_DIR.
9: # CURSO_AUTH_GITHUB=0 pula a autenticação em testes locais.
10: set -eu
11: falha() { printf '❌ %s\n' "$*" >&2; exit 1; }
12: if [ "${CODESPACES:-}" != true ] && [ "${CURSO_MODO_TESTE:-0}" != 1 ]; then
13:   falha "Crie um ambiente no GitHub Codespaces com o modelo Blank em https://github.com/codespaces e execute o instalador no terminal."
14: fi
15: PASTA_INICIAL="$(pwd -P)"
16: CURSO_REPO="${CURSO_REPO:-https://github.com/fsilva-alt/devops-ghactions.git}"
17: CURSO_RAMO="${CURSO_RAMO:-main}"
18: CURSO_DIR="${CURSO_DIR:-$HOME/devops-ghactions}"
19: LABS_DIR="${LABS_DIR:-$HOME/labs}"
20: CURSO_AUTH_GITHUB="${CURSO_AUTH_GITHUB:-1}"
21: export CURSO_DIR LABS_DIR
22: case "$CURSO_DIR" in /*) ;; *) falha "CURSO_DIR deve ser um caminho absoluto." ;; esac
23: case "$LABS_DIR" in /*) ;; *) falha "LABS_DIR deve ser um caminho absoluto." ;; esac
24: case "$CURSO_AUTH_GITHUB" in 0|1) ;; *) falha "CURSO_AUTH_GITHUB deve ser 0 ou 1." ;; esac
25: for comando in git bash python3; do
26:   command -v "$comando" >/dev/null 2>&1 || falha "Falta $comando. Use um Codespace com o modelo Blank, que inclui as ferramentas do curso."
27: done
28: if [ "$CURSO_AUTH_GITHUB" = 1 ]; then
29:   command -v gh >/dev/null 2>&1 || falha "Falta o GitHub CLI (gh). Use um Codespace com o modelo Blank ou instale-o em https://cli.github.com."
30: fi
31: 
32: if [ -d "$CURSO_DIR/.git" ]; then
33:   printf '▶ Atualizando o curso em %s\n' "$CURSO_DIR"
34:   git -C "$CURSO_DIR" pull -q --ff-only \
35:     || falha "Não foi possível atualizar $CURSO_DIR. Confira a conexão e as alterações locais nessa pasta antes de tentar novamente."
36: else
37:   printf '▶ Baixando o curso para %s\n' "$CURSO_DIR"
38:   git clone -q --depth 1 --branch "$CURSO_RAMO" -- "$CURSO_REPO" "$CURSO_DIR" \
39:     || falha "Não foi possível clonar $CURSO_REPO em $CURSO_DIR. Confira a conexão, o endereço e se a pasta de destino está vazia."
40: fi
41: 
42: printf '▶ Preparando o verificador de YAML...\n'
43: python3 -m venv "$CURSO_DIR/.venv" || falha "Não foi possível criar o ambiente Python. Confira se python3-venv está instalado e execute o instalador novamente."
44: "$CURSO_DIR/.venv/bin/python" -m pip install --disable-pip-version-check -q -r "$CURSO_DIR/scripts/requirements.txt"
45: chmod +x "$CURSO_DIR"/scripts/*.sh
46: bash "$CURSO_DIR/scripts/setup.sh"
47: 
48: # Disponibiliza os laboratórios no explorador do editor sem substituir arquivos.
49: ATALHO_LABS="$PASTA_INICIAL/labs"
50: if [ "$PASTA_INICIAL" != "$(CDPATH='' cd -- "$LABS_DIR" && pwd -P)" ] && [ ! -e "$ATALHO_LABS" ] && [ ! -L "$ATALHO_LABS" ]; then
51:   ln -s "$LABS_DIR" "$ATALHO_LABS"
52:   printf '▶ Atalho para os laboratórios criado em %s\n' "$ATALHO_LABS"
53: fi
54: 
55: if [ "$CURSO_AUTH_GITHUB" = 1 ]; then
56:   printf '▶ Preparando o acesso ao GitHub para publicar os exercícios\n'
57:   # Como no curso de Git, usa o login salvo em vez do token do Codespace.
58:   unset GH_TOKEN GITHUB_TOKEN
59:   if gh auth status --active --hostname github.com >/dev/null 2>&1; then
60:     printf '▶ Reutilizando o login salvo no GitHub CLI\n'
61:   else
62:     [ -t 0 ] || falha "Para autenticar, execute o instalador novamente no terminal interativo do Codespace. Os laboratórios já estão prontos."
63:     printf '\nAutorize o GitHub CLI com a conta que usará no curso.\n'
64:     printf 'Siga o código e o endereço exibidos abaixo para entrar pelo navegador.\n'
65:     printf 'O escopo workflow permite publicar os arquivos de GitHub Actions.\n\n'
66:     gh auth login --hostname github.com --git-protocol https --web --scopes workflow \
67:       || falha "Login interrompido. Execute o instalador novamente para continuar; seus laboratórios serão preservados."
68:   fi
69:   gh auth setup-git --hostname github.com \
70:     || falha "Não foi possível configurar o Git para usar o login do gh. Execute o instalador novamente."
71:   gh auth status --active --hostname github.com \
72:     || falha "O login no GitHub não está válido. Execute o instalador novamente para autenticar."
73: fi
74: 
75: # Caminhos são escapados para poderem ser carregados por bash e zsh.
76: shell_quote() { printf "'%s'" "$(printf '%s' "$1" | sed "s/'/'\\\\''/g")"; }
77: AUTH_LINHA='if [ "${CODESPACES:-}" = true ]; then unset GH_TOKEN GITHUB_TOKEN; fi'
78: for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
79:   # Como nas referências, cria .bashrc e só altera .zshrc se ele já existir.
80:   if [ ! -f "$rc" ] && [ "$rc" != "$HOME/.bashrc" ]; then continue; fi
81:   [ -f "$rc" ] || touch "$rc"
82:   configurar_auth="$CURSO_AUTH_GITHUB"
83:   # Pular o login numa reinstalação não remove uma configuração já habilitada.
84:   if grep -qxF "$AUTH_LINHA" "$rc"; then configurar_auth=1; fi
85:   bloco="$(
86:     printf '# >>> curso de github actions >>>\n'
87:     printf 'export CURSO_DIR=%s\n' "$(shell_quote "$CURSO_DIR")"
88:     printf 'export LABS_DIR=%s\n' "$(shell_quote "$LABS_DIR")"
89:     printf 'export PATH="$CURSO_DIR/scripts:$PATH"\n'
90:     if [ "$configurar_auth" = 1 ]; then printf '%s\n' "$AUTH_LINHA"; fi
91:     printf '# <<< curso de github actions <<<\n'
92:   )"
93:   atual="$(sed -n '/^# >>> curso de github actions >>>$/,/^# <<< curso de github actions <<<$/p' "$rc")"
94:   [ "$atual" = "$bloco" ] && continue
95:   sed -i '/^# >>> curso de github actions >>>$/,/^# <<< curso de github actions <<<$/{d;}' "$rc"
96:   printf '\n%s\n' "$bloco" >> "$rc"
97: done
98: 
99: printf '\n✅ Curso de GitHub Actions instalado com sucesso!\n'
100: printf 'Material do curso: %s\n' "$CURSO_DIR"
101: printf 'Laboratórios: %s\n' "$LABS_DIR"
102: printf 'Abra um terminal novo para carregar os comandos e o login salvo.\n'
103: printf 'Ou execute: source ~/.bashrc (bash) / source ~/.zshrc (zsh).\n'
104: printf 'Comece pelo exercício 01 em https://fsilva-alt.github.io/devops-ghactions/#exercicio-01\n'
105: printf 'Verificação local: check.sh 01 (é esperado reprovar antes de criar o workflow).\n'
106: if [ "$CURSO_AUTH_GITHUB" = 0 ]; then
107:   printf 'Preparação concluída sem login. Antes da aula, execute o instalador sem CURSO_AUTH_GITHUB=0 para autenticar.\n'
108: fi

(End of file - total 108 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/templates/projeto"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/templates/projeto</path>
<type>directory</type>
<entries>
.gitignore
app.py
build.py
cardapio.md
README.md
requirements.txt
test_app.py

(7 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/tests/rodar.sh"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/tests/rodar.sh</path>
<type>file</type>
<content>
1: #!/usr/bin/env bash
2: # Testes de manutenção; o uso do curso pelos alunos exige Codespaces.
3: set -euo pipefail
4: RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
5: case "${1:-}" in
6:   '') exec bash "$RAIZ/tests/solucoes.sh" ;;
7:   --docker)
8:     docker build -q -t curso-actions-testes -f "$RAIZ/tests/Dockerfile" "$RAIZ/tests"
9:     docker run --rm -v "$RAIZ:/curso:ro" curso-actions-testes bash /curso/tests/solucoes.sh
10:     ;;
11:   *) printf 'Uso: bash tests/rodar.sh [--docker]\n' >&2; exit 2 ;;
12: esac

(End of file - total 12 lines)
</content>
```

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://raw.githubusercontent.com/fsilva-alt/devops-docker/main/scripts/labs.sh",
  "format": "text"
}
```

**Output:**
```
#!/usr/bin/env bash
# Geradores dos laboratórios. Carregado por setup.sh e reset.sh.
#
# Cada função gerar_NN cria a pasta do exercício já no estado inicial descrito em
# exercises/NN-nome/README.md. Cada limpar_NN remove o que o exercício criou no
# Docker (containers, imagens, volumes, redes), para o reset.sh recomeçar do zero.

# ---------------------------------------------------------------------------
# Conteúdo do projeto que você coloca em containers: um livro de
# receitas, primeiro como script, depois como API em FastAPI e como site.
# ---------------------------------------------------------------------------

receitas_py() {
cat <<'EOF'
"""Livro de receitas: lista as receitas disponíveis."""

RECEITAS = [
    ("Bolo de cenoura", "8 porções"),
    ("Brigadeiro", "30 unidades"),
    ("Pão de queijo", "25 unidades"),
]

print("Livro de receitas")
print("=================")
for nome, rende in RECEITAS:
    print(f"- {nome} (rende {rende})")
EOF
}

# app_py [env] [reload]
#   env    -> lê a variável de ambiente COZINHA (exercícios 9 em diante)
#   reload -> uvicorn com reload=True, que reinicia quando o arquivo muda (exercício 10)
app_py() {
  local env=0 reload=0 a
  for a in "$@"; do
    [[ "$a" == env ]] && env=1
    [[ "$a" == reload ]] && reload=1
  done
  printf '"""Livro de receitas: uma API mínima em FastAPI."""\n\n'
  if (( env )); then printf 'import os\n\n'; fi
  printf 'import uvicorn\nfrom fastapi import FastAPI\n\napp = FastAPI(title="Livro de receitas")\n\n'
  if (( env )); then
    printf '# O nome da cozinha vem de fora, pela variável de ambiente COZINHA.\n'
    printf 'COZINHA = os.environ.get("COZINHA", "Cozinha sem nome")\n\n'
  fi
  cat <<'EOF'
RECEITAS = [
    {"nome": "Bolo de cenoura", "rende": "8 porções"},
    {"nome": "Brigadeiro", "rende": "30 unidades"},
    {"nome": "Pão de queijo", "rende": "25 unidades"},
]


@app.get("/")
def inicio():
EOF
  if (( env )); then
    printf '    return {"mensagem": f"Livro de receitas da {COZINHA}", "receitas": "/receitas"}\n'
  else
    printf '    return {"mensagem": "Livro de receitas", "receitas": "/receitas"}\n'
  fi
  cat <<'EOF'


@app.get("/receitas")
def receitas():
    return RECEITAS


if __name__ == "__main__":
EOF
  printf '    # 127.0.0.1 é o loopback: recebe pedidos apenas deste container.\n'
  printf '    # 0.0.0.0 faz o servidor escutar em todas as interfaces IPv4 do container,\n'
  printf '    # permitindo pedidos de outros containers ou de uma porta publicada com -p.\n'
  if (( reload )); then
    printf '    # reload=True: o uvicorn reinicia sozinho quando app.py muda.\n'
    printf '    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)\n'
  else
    printf '    uvicorn.run(app, host="0.0.0.0", port=8000)\n'
  fi
}

requirements_txt() { printf 'fastapi==0.115.6\nuvicorn==0.34.0\n'; }

# dockerfile_api <ingenuo|bom> [expose] [env]
#   ingenuo -> COPY . . antes do pip install (exercício 6 corrige)
#   bom     -> requirements.txt primeiro, para o cache funcionar
dockerfile_api() {
  local ordem="$1"; shift
  local expose=0 env=0 a
  for a in "$@"; do
    [[ "$a" == expose ]] && expose=1
    [[ "$a" == env ]] && env=1
  done
  printf 'FROM python:3.12-slim\n\nWORKDIR /app\n\n'
  if [[ "$ordem" == ingenuo ]]; then
    printf 'COPY . .\nRUN pip install --no-cache-dir -r requirements.txt\n'
  else
    printf 'COPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\nCOPY . .\n'
  fi
  if (( env )); then printf '\nENV COZINHA="Cozinha do Curso"\n'; fi
  if (( expose )); then printf '\nEXPOSE 8000\n'; fi
  printf '\nCMD ["python", "app.py"]\n'
}

bloco_py() {
cat <<'EOF'
"""Bloco de notas: guarda cada nota em /dados/notas.txt e mostra todas."""

import sys
from pathlib import Path

ARQUIVO = Path("/dados/notas.txt")

# Se veio uma nota na linha de comando, acrescenta ao arquivo.
if len(sys.argv) > 1:
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    with ARQUIVO.open("a", encoding="utf-8") as f:
        f.write(" ".join(sys.argv[1:]) + "\n")

if ARQUIVO.exists():
    print("Notas guardadas:")
    for i, linha in enumerate(ARQUIVO.read_text(encoding="utf-8").splitlines(), 1):
        print(f"{i}. {linha}")
else:
    print("Nenhuma nota ainda.")
EOF
}

dockerfile_bloco() {
cat <<'EOF'
FROM python:3.12-slim

COPY bloco.py /app/bloco.py

# ENTRYPOINT é o programa; o que vier depois de "docker run <imagem>" vira argumento dele.
ENTRYPOINT ["python", "/app/bloco.py"]
EOF
}

cliente_py() {
cat <<'EOF'
"""Cliente: busca as receitas na API chamando o container pelo nome."""

import json
import sys
import time
import urllib.error
import urllib.request

URL = sys.argv[1] if len(sys.argv) > 1 else "http://receitas:8000/receitas"
# A comunicação é direta na rede Docker; não deve passar por um proxy HTTP externo.
cliente = urllib.request.build_opener(urllib.request.ProxyHandler({}))

# -d libera o terminal antes de o servidor estar pronto. Espere por um tempo limitado.
for tentativa in range(1, 9):
    try:
        with cliente.open(URL, timeout=2) as resposta:
            receitas = json.load(resposta)
        break
    except urllib.error.HTTPError as erro:
        raise SystemExit(f"A API em {URL} respondeu HTTP {erro.code}. Confira o caminho /receitas.")
    except (urllib.error.URLError, TimeoutError, ConnectionError) as erro:
        if tentativa == 8:
            raise SystemExit(
                f"Não foi possível acessar {URL} após 8 tentativas: {erro}.\n"
                "Confira os logs da API e se os dois containers estão na mesma rede.\n"
                "Se o nome resolve, mas a conexão expira, execute rede.sh e tente novamente."
            )
        print(f"Aguardando a API em {URL} (tentativa {tentativa}/8)...", file=sys.stderr, flush=True)
        time.sleep(1)
    except (ValueError, UnicodeError) as erro:
        raise SystemExit(f"A resposta de {URL} não é um JSON válido: {erro}.")

if not isinstance(receitas, list) or not all(
    isinstance(r, dict) and "nome" in r and "rende" in r for r in receitas
):
    raise SystemExit(f"A resposta de {URL} não contém a lista de receitas esperada.")

print(f"A API em {URL} respondeu com {len(receitas)} receitas:")
for r in receitas:
    print(f"- {r['nome']} (rende {r['rende']})")
EOF
}

# --- site estático (HTML/JS) --------------------------------------------------

site_index_html() {
cat <<'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Livro de receitas</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <h1>Livro de receitas</h1>
    <p id="origem">Carregando…</p>
    <ul id="receitas"></ul>
  </main>
  <script src="app.js"></script>
</body>
</html>
EOF
}

site_style_css() {
cat <<'EOF'
body { font-family: system-ui, sans-serif; background: #fff8f0; color: #333; margin: 0; }
main { max-width: 32rem; margin: 3rem auto; padding: 0 1rem; }
h1 { color: #c2410c; }
#origem { color: #777; font-size: 0.9rem; }
li { padding: 0.4rem 0; border-bottom: 1px solid #eee; }
EOF
}

# site_app_js <url>   (receitas.json no exercício 12; /api/receitas no 14)
site_app_js() {
cat <<EOF
// Busca a lista de receitas e desenha na página.
const URL_RECEITAS = "$1";

async function carregar() {
  const lista = document.getElementById("receitas");
  const origem = document.getElementById("origem");
  try {
    const resposta = await fetch(URL_RECEITAS);
    const receitas = await resposta.json();
    origem.textContent = \`\${receitas.length} receitas vindas de \${URL_RECEITAS}\`;
    lista.innerHTML = "";
    for (const r of receitas) {
      const item = document.createElement("li");
      item.textContent = \`\${r.nome} — rende \${r.rende}\`;
      lista.appendChild(item);
    }
  } catch (erro) {
    origem.textContent = \`Não consegui carregar \${URL_RECEITAS}: \${erro.message}\`;
  }
}

carregar();
EOF
}

site_receitas_json() {
cat <<'EOF'
[
  {"nome": "Bolo de cenoura", "rende": "8 porções"},
  {"nome": "Brigadeiro", "rende": "30 unidades"},
  {"nome": "Pão de queijo", "rende": "25 unidades"}
]
EOF
}

nginx_conf() {
cat <<'EOF'
server {
    listen 80;

    # Os arquivos do site
    location / {
        root  /usr/share/nginx/html;
        index index.html;
    }

    # Tudo o que começa com /api/ é repassado ao container "api", pelo nome.
    # O "resolver" é o DNS interno do Docker: assim o nginx procura o "api" de
    # novo a cada poucos segundos e continua achando se o container for recriado.
    location /api/ {
        resolver 127.0.0.11 valid=5s;
        set $api "http://api:8000";
        rewrite ^/api/(.*)$ /$1 break;
        proxy_pass $api;
    }
}
EOF
}

dockerfile_web() {
cat <<'EOF'
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/
EOF
}

# gerar_site DIR URL  — os quatro arquivos do site em DIR
gerar_site() {
  mkdir -p "$1"
  site_index_html   > "$1/index.html"
  site_style_css    > "$1/style.css"
  site_app_js "$2"  > "$1/app.js"
  site_receitas_json > "$1/receitas.json"
}

# ---------------------------------------------------------------------------
# Exercícios 1 a 3 — sem pasta: só containers
# ---------------------------------------------------------------------------
limpar_01() {
  local id
  for id in $(containers_de hello-world); do rm_container "$id"; done
  for id in $(containers_de python:3.12-slim); do
    [[ "$(container_cmd "$id")" == *print* ]] && rm_container "$id"
  done
  return 0
}

limpar_02() {
  local id
  rm_container explorador
  for id in $(containers_de python:3.12-slim); do
    [[ "$(container_cmd "$id")" == python3 ]] && rm_container "$id"
  done
  return 0
}

limpar_03() { rm_container relogio descartavel; }

# ---------------------------------------------------------------------------
# Exercício 4 — Meu primeiro Dockerfile
# ---------------------------------------------------------------------------
gerar_04() {
  local dir; dir="$(lab_dir 04)"
  mkdir -p "$dir"
  receitas_py > "$dir/receitas.py"
}
limpar_04() { rm_imagem receitas:1.0 receitas:latest; }

# ---------------------------------------------------------------------------
# Exercício 5 — Instalando dependências
# ---------------------------------------------------------------------------
gerar_05() {
  local dir; dir="$(lab_dir 05)"
  mkdir -p "$dir"
  app_py > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
}
limpar_05() { rm_imagem receitas-api:1.0; }

# ---------------------------------------------------------------------------
# Exercício 6 — Camadas e cache
# ---------------------------------------------------------------------------
gerar_06() {
  local dir; dir="$(lab_dir 06)"
  mkdir -p "$dir"
  app_py > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
  dockerfile_api ingenuo > "$dir/Dockerfile"
}
limpar_06() { rm_imagem receitas-api:1.1; }

# ---------------------------------------------------------------------------
# Exercício 7 — O que não entra na imagem
# ---------------------------------------------------------------------------
gerar_07() {
  local dir; dir="$(lab_dir 07)"
  mkdir -p "$dir"
  app_py > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
  dockerfile_api bom > "$dir/Dockerfile"
  # Lixo que costuma existir na pasta de um projeto e não deve ir para a imagem:
  # um ambiente virtual do Python (grande e inútil dentro do container)...
  mkdir -p "$dir/.venv/bin" "$dir/.venv/lib/python3.12/site-packages/fastapi"
  printf '#!/bin/sh\necho "python de mentira"\n' > "$dir/.venv/bin/python"
  head -c 3000000 /dev/zero > "$dir/.venv/lib/python3.12/site-packages/fastapi/__init__.py"
  # ...cache do Python...
  mkdir -p "$dir/__pycache__"
  head -c 2000 /dev/zero > "$dir/__pycache__/app.cpython-312.pyc"
  # ...um segredo e anotações pessoais...
  printf 'SENHA_DO_BANCO=batata123\n' > "$dir/.env"
  printf 'Lembrar de comprar cenouras.\nSenha do wifi: batata123\n' > "$dir/notas-pessoais.md"
  # ...e fotos, que nada têm a ver com a API.
  mkdir -p "$dir/fotos"
  head -c 2000000 /dev/zero > "$dir/fotos/bolo-de-cenoura.jpg"
}
limpar_07() { rm_imagem receitas-api:1.2; }

# ---------------------------------------------------------------------------
# Exercício 8 — Abrindo portas
# ---------------------------------------------------------------------------
gerar_08() {
  local dir; dir="$(lab_dir 08)"
  mkdir -p "$dir"
  app_py > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
  dockerfile_api bom > "$dir/Dockerfile"       # acrescente EXPOSE neste exercício
  printf '__pycache__/\n.venv/\n.env\n' > "$dir/.dockerignore"
}
limpar_08() { rm_container api; rm_imagem receitas-api:1.3; }

# ---------------------------------------------------------------------------
# Exercício 9 — Configuração por ambiente
# ---------------------------------------------------------------------------
gerar_09() {
  local dir; dir="$(lab_dir 09)"
  mkdir -p "$dir"
  app_py env > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
  dockerfile_api bom expose > "$dir/Dockerfile"   # acrescente ENV neste exercício
  printf '__pycache__/\n.venv/\n.env\n' > "$dir/.dockerignore"
  printf '# Um valor por linha, sem aspas nem espaços em volta do =\nCOZINHA=Cozinha da Vovó\n' > "$dir/cozinha.env"
}
limpar_09() { rm_container cozinha; rm_imagem receitas-api:1.4; }

# ---------------------------------------------------------------------------
# Exercício 10 — Editando ao vivo
# ---------------------------------------------------------------------------
gerar_10() {
  local dir; dir="$(lab_dir 10)"
  mkdir -p "$dir"
  app_py env reload > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
  dockerfile_api bom expose env > "$dir/Dockerfile"
  printf '__pycache__/\n.venv/\n.env\n' > "$dir/.dockerignore"
}
limpar_10() { rm_container dev; rm_imagem receitas-api:1.5; }

# ---------------------------------------------------------------------------
# Exercício 11 — Dados que ficam
# ---------------------------------------------------------------------------
gerar_11() {
  local dir; dir="$(lab_dir 11)"
  mkdir -p "$dir"
  bloco_py > "$dir/bloco.py"
  dockerfile_bloco > "$dir/Dockerfile"
}
limpar_11() { rm_imagem bloco:1.0; rm_volume notas; }

# ---------------------------------------------------------------------------
# Exercício 12 — Site estático
# ---------------------------------------------------------------------------
gerar_12() {
  local dir; dir="$(lab_dir 12)"
  gerar_site "$dir/site" receitas.json
}
limpar_12() { rm_container web; rm_imagem receitas-web:1.0; }

# ---------------------------------------------------------------------------
# Exercício 13 — Containers conversando
# ---------------------------------------------------------------------------
gerar_13() {
  local dir; dir="$(lab_dir 13)"
  mkdir -p "$dir"
  app_py env > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
  dockerfile_api bom expose env > "$dir/Dockerfile"
  printf '__pycache__/\n.venv/\n.env\n' > "$dir/.dockerignore"
  cliente_py > "$dir/cliente.py"
}
limpar_13() { rm_container receitas; rm_rede cozinha; rm_imagem receitas-api:1.6; }

# ---------------------------------------------------------------------------
# Exercício 14 — Docker Compose
# ---------------------------------------------------------------------------
gerar_14() {
  local dir; dir="$(lab_dir 14)"
  mkdir -p "$dir/api" "$dir/web"
  app_py env > "$dir/api/app.py"
  requirements_txt > "$dir/api/requirements.txt"
  dockerfile_api bom expose env > "$dir/api/Dockerfile"
  printf '__pycache__/\n.venv/\n.env\n' > "$dir/api/.dockerignore"
  dockerfile_web > "$dir/web/Dockerfile"
  nginx_conf > "$dir/web/nginx.conf"
  gerar_site "$dir/web/site" /api/receitas
}
limpar_projeto_compose() {
  local dir="$1" f
  for f in compose.yaml compose.yml docker-compose.yaml docker-compose.yml; do
    if [[ -f "$dir/$f" ]]; then
      ( cd "$dir" && docker compose down --rmi local -v --remove-orphans >/dev/null 2>&1 ) || true
      break
    fi
  done
  # Se o compose.yaml sumiu, os containers ainda podem existir com o nome do projeto
  local id
  for id in $(docker ps -aq --filter "label=com.docker.compose.project=$(basename "$dir")" 2>/dev/null || true); do
    rm_container "$id"
  done
  rm_rede "$(basename "$dir")_default"
  rm_imagem "$(basename "$dir")-api" "$(basename "$dir")-web"
}
limpar_14() { limpar_projeto_compose "$(lab_dir 14)"; }

# ---------------------------------------------------------------------------
# Exercício 16 — Desenvolvimento com Compose (opcional)
# ---------------------------------------------------------------------------
gerar_16() {
  local dir; dir="$(lab_dir 16)"
  mkdir -p "$dir"
  app_py env reload > "$dir/app.py"
  requirements_txt > "$dir/requirements.txt"
  dockerfile_api bom expose env > "$dir/Dockerfile"
  printf '__pycache__/\n.venv/\n.env\n' > "$dir/.dockerignore"
}
limpar_16() {
  limpar_projeto_compose "$(lab_dir 16)"
  rm_imagem receitas-api:dev
}

# ---------------------------------------------------------------------------
# Exercício 17 — Persistência com Compose (opcional)
# ---------------------------------------------------------------------------
gerar_17() {
  local dir; dir="$(lab_dir 17)"
  mkdir -p "$dir"
  bloco_py > "$dir/bloco.py"
  dockerfile_bloco > "$dir/Dockerfile"
}
limpar_17() {
  limpar_projeto_compose "$(lab_dir 17)"
  rm_volume 17-compose-persistencia_notas
  rm_imagem receitas-notas:1.0
}

# ---------------------------------------------------------------------------
# gerar_lab NN — recria o exercício NN (apaga a pasta e o que ele criou no Docker)
# ---------------------------------------------------------------------------
gerar_lab() {
  local nn="$1"
  if declare -F "limpar_$nn" >/dev/null; then "limpar_$nn"; fi
  if lab_tem_pasta "$nn"; then
    local dir; dir="$(lab_dir "$nn")"
    mkdir -p "$LABS_DIR"
    cd "$LABS_DIR"    # o diretório atual pode ser justamente o que vai ser apagado
    rm -rf "$dir"
    "gerar_$nn"
  fi
}

```

**Tool: bash**

**Input:**
```json
{
  "command": "command -v docker; command -v act; command -v chromium; command -v node; python3 -c 'import importlib.util; print({m: importlib.util.find_spec(m) is not None for m in [\"yaml\", \"playwright\"]})'"
}
```

**Output:**
```
/usr/bin/docker
/run/user/1000/fnm_multishells/13587_1790881249447/bin/node
{'yaml': True, 'playwright': False}

```

---

## Assistant (Build · GPT-6 Astra · 16.4s)

_Thinking:_

**Preparing recipe data**

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/templates/projeto/app.py"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/templates/projeto/app.py</path>
<type>file</type>
<content>
1: """Regras do cardápio: preços em centavos para evitar arredondamento."""
2: 
3: 
4: def total(preco_centavos, quantidade):
5:     if preco_centavos < 0 or quantidade < 0:
6:         raise ValueError("Preço e quantidade devem ser não negativos")
7:     return preco_centavos * quantidade

(End of file - total 7 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/templates/projeto/build.py"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/templates/projeto/build.py</path>
<type>file</type>
<content>
1: """Gera o site estático usado como artefato e no GitHub Pages."""
2: 
3: from pathlib import Path
4: 
5: import markdown
6: 
7: conteudo = markdown.markdown(
8:     Path("cardapio.md").read_text(encoding="utf-8"), extensions=["tables"]
9: )
10: destino = Path("dist")
11: destino.mkdir(exist_ok=True)
12: (destino / "index.html").write_text(
13:     '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
14:     '<meta name="viewport" content="width=device-width, initial-scale=1">'
15:     '<title>Cardápio da comunidade</title>'
16:     '<style>body{max-width:48rem;margin:3rem auto;padding:0 1rem;'
17:     'font:1.1rem/1.6 system-ui}table{border-collapse:collapse}'
18:     'td,th{padding:.5rem 1rem;border:1px solid #ccc}</style>'
19:     f'</head><body>{conteudo}</body></html>',
20:     encoding="utf-8",
21: )
22: print("Site gerado em dist/index.html")

(End of file - total 22 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/templates/projeto/test_app.py"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/templates/projeto/test_app.py</path>
<type>file</type>
<content>
1: import unittest
2: 
3: from app import total
4: 
5: 
6: class TestCardapio(unittest.TestCase):
7:     def test_total_de_varias_unidades(self):
8:         self.assertEqual(total(500, 3), 1500)
9: 
10:     def test_carrinho_vazio(self):
11:         self.assertEqual(total(500, 0), 0)
12: 
13:     def test_rejeita_valores_negativos(self):
14:         for preco, quantidade in [(-1, 2), (500, -1)]:
15:             with self.subTest(preco=preco, quantidade=quantidade):
16:                 with self.assertRaises(ValueError):
17:                     total(preco, quantidade)
18: 
19: 
20: if __name__ == "__main__":
21:     unittest.main()

(End of file - total 21 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/tests/solucoes.sh"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/tests/solucoes.sh</path>
<type>file</type>
<content>
1: #!/usr/bin/env bash
2: # Integração em HOME descartável: nunca usa conta GitHub nem labs do usuário.
3: set -euo pipefail
4: RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
5: TEMP_BASE="${TMPDIR:-/tmp/opencode}"
6: mkdir -p "$TEMP_BASE"
7: TEMP="$(mktemp -d "$TEMP_BASE/curso-actions.XXXXXX")"
8: trap 'rm -rf -- "$TEMP"' EXIT
9: export HOME="$TEMP/home"
10: unset CURSO_DIR LABS_DIR CURSO_RAMO
11: export CURSO_MODO_TESTE=1 CURSO_AUTH_GITHUB=0 CODESPACES=false
12: export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$HOME/.gitconfig"
13: export PYTHONDONTWRITEBYTECODE=1
14: unset GH_TOKEN GITHUB_TOKEN
15: mkdir -p "$HOME" "$TEMP/origem" "$TEMP/bin" "$TEMP/workspace"
16: printf '# Configuração existente do aluno\n' > "$HOME/.zshrc"
17: tar -C "$RAIZ" --exclude=.git --exclude=.venv --exclude=__pycache__ -cf - . | tar -C "$TEMP/origem" -xf -
18: git -C "$TEMP/origem" init -q -b main
19: git -C "$TEMP/origem" add .
20: git -C "$TEMP/origem" -c user.name=Teste -c user.email=teste@example.com commit -qm 'Material do curso'
21: export CURSO_REPO="file://$TEMP/origem"
22: printf '\n▶ Instalação via curl e sh -c em um workspace vazio, sem autenticação\n'
23: (
24:   cd "$TEMP/workspace"
25:   sh -c "$(curl -fsSL "file://$TEMP/origem/install.sh")"
26: )
27: export CURSO_DIR="$HOME/devops-ghactions" LABS_DIR="$HOME/labs"
28: export PATH="$CURSO_DIR/scripts:$TEMP/bin:$PATH"
29: cd "$TEMP/workspace"
30: [[ -d "$CURSO_DIR/.git" && -x "$CURSO_DIR/.venv/bin/python" ]]
31: [[ $(readlink "$TEMP/workspace/labs") == "$LABS_DIR" ]]
32: [[ $(find "$LABS_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l) -eq 7 ]]
33: touch "$LABS_DIR/01-primeiro-workflow/trabalho-preservado"
34: printf 'Atualização do material\n' > "$TEMP/origem/atualizacao.txt"
35: git -C "$TEMP/origem" add atualizacao.txt
36: git -C "$TEMP/origem" -c user.name=Teste -c user.email=teste@example.com commit -qm 'Atualiza material'
37: (
38:   cd "$TEMP/workspace"
39:   sh -c "$(curl -fsSL "file://$TEMP/origem/install.sh")"
40: ) > "$TEMP/reinstalacao.log"
41: [[ -f "$CURSO_DIR/atualizacao.txt" ]]
42: [[ -f "$LABS_DIR/01-primeiro-workflow/trabalho-preservado" ]]
43: [[ $(grep -c '^# >>> curso de github actions >>>' "$HOME/.bashrc") -eq 1 ]]
44: grep -q '^# Configuração existente do aluno$' "$HOME/.zshrc"
45: bash -c 'source "$HOME/.bashrc"; command -v check.sh; command -v reset.sh; command -v setup.sh' >/dev/null
46: CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
47:   bash -c 'source "$HOME/.bashrc"; test "$GH_TOKEN" = simulado; test "$GITHUB_TOKEN" = simulado'
48: if command -v zsh >/dev/null; then
49:   zsh -c 'source "$HOME/.zshrc"; command -v check.sh' >/dev/null
50: fi
51: printf '✅ Instalação remota, atualização, preservação dos laboratórios, atalho e PATH.\n'
52: 
53: # Não substitui uma pasta nem um link preexistente chamado labs no workspace.
54: mkdir -p "$TEMP/com-pasta/labs" "$TEMP/com-link"
55: touch "$TEMP/com-pasta/labs/trabalho-preservado"
56: ln -s "$TEMP/destino-ausente" "$TEMP/com-link/labs"
57: for pasta in com-pasta com-link; do
58:   (cd "$TEMP/$pasta"; sh "$CURSO_DIR/install.sh") > "$TEMP/$pasta.log"
59: done
60: [[ -f "$TEMP/com-pasta/labs/trabalho-preservado" ]]
61: [[ $(readlink "$TEMP/com-link/labs") == "$TEMP/destino-ausente" ]]
62: printf '✅ Arquivos e links existentes no workspace preservados.\n'
63: 
64: # A instalação fora do Codespaces só é liberada explicitamente para manutenção.
65: if CURSO_MODO_TESTE=0 sh "$CURSO_DIR/install.sh" > "$TEMP/fora.log" 2>&1; then
66:   printf '❌ Instalador aceitou uso normal fora do Codespaces.\n'; exit 1
67: fi
68: grep -q Codespaces "$TEMP/fora.log"
69: 
70: # GitHub CLI simulado: exige que tokens automáticos tenham sido removidos.
71: export MOCK_GH_DIR="$TEMP/gh"
72: mkdir -p "$MOCK_GH_DIR"
73: cat > "$TEMP/bin/gh" <<'MOCK'
74: #!/bin/sh
75: set -eu
76: [ -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}" ] || exit 90
77: printf '%s\n' "$*" >> "$MOCK_GH_DIR/chamadas"
78: case "$*" in
79:   'auth status --active --hostname github.com') test -f "$MOCK_GH_DIR/login" ;;
80:   'auth login --hostname github.com --git-protocol https --web --scopes workflow')
81:     test -t 0
82:     touch "$MOCK_GH_DIR/login"
83:     ;;
84:   'auth setup-git --hostname github.com') test -f "$MOCK_GH_DIR/login" ;;
85:   *) exit 91 ;;
86: esac
87: MOCK
88: chmod +x "$TEMP/bin/gh"
89: if CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
90:   sh "$CURSO_DIR/install.sh" < /dev/null > "$TEMP/sem-terminal.log" 2>&1; then
91:   printf '❌ Login sem terminal interativo foi aceito.\n'; exit 1
92: fi
93: grep -q 'terminal interativo' "$TEMP/sem-terminal.log"
94: if command -v script >/dev/null; then
95:   CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
96:     script -qec 'sh "$CURSO_DIR/install.sh"' /dev/null < /dev/null > "$TEMP/login.log"
97:   grep -q -- '--scopes workflow' "$MOCK_GH_DIR/chamadas"
98: else
99:   touch "$MOCK_GH_DIR/login"
100: fi
101: CURSO_AUTH_GITHUB=1 CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
102:   sh "$CURSO_DIR/install.sh" < /dev/null > "$TEMP/login-salvo.log"
103: grep -q 'Reutilizando o login salvo' "$TEMP/login-salvo.log"
104: if command -v script >/dev/null; then
105:   [[ $(grep -c 'auth login' "$MOCK_GH_DIR/chamadas") -eq 1 ]]
106: fi
107: CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
108:   bash -c 'source "$HOME/.bashrc"; test -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}"'
109: CODESPACES=false GH_TOKEN=simulado GITHUB_TOKEN=simulado \
110:   bash -c 'source "$HOME/.bashrc"; test "$GH_TOKEN" = simulado; test "$GITHUB_TOKEN" = simulado'
111: if command -v zsh >/dev/null; then
112:   CODESPACES=true GH_TOKEN=simulado GITHUB_TOKEN=simulado \
113:     zsh -c 'source "$HOME/.zshrc"; test -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}"'
114: fi
115: printf '✅ Autenticação simulada: login com escopo workflow, reutilização e novos terminais.\n'
116: 
117: printf '\n▶ Exercícios: estados iniciais, erros comuns e soluções\n'
118: "$CURSO_DIR/.venv/bin/python" "$CURSO_DIR/tests/verificar.py"
119: 
120: # Conferência de inferência de número, reset isolado e limites de entrada.
121: (
122:   cd "$TEMP/workspace/labs/02-testes-no-push/.github/workflows"
123:   check.sh >/dev/null
124: )
125: (
126:   cd "$TEMP/workspace/labs/02-testes-no-push"
127:   reset.sh >/dev/null
128: )
129: [[ -f "$LABS_DIR/01-primeiro-workflow/trabalho-preservado" ]]
130: if check.sh 02 >/dev/null 2>&1; then exit 1; fi
131: for numero in 00 08 99 abc ../01; do
132:   if check.sh "$numero" >/dev/null 2>&1; then exit 1; fi
133:   if reset.sh "$numero" >/dev/null 2>&1; then exit 1; fi
134: done
135: printf '✅ Inferência de exercício, reset isolado e números inválidos.\n'
136: 
137: printf '\n▶ Testes reais do projeto e geração do site\n'
138: "$CURSO_DIR/.venv/bin/python" -m pip install --disable-pip-version-check -q -r "$CURSO_DIR/templates/projeto/requirements.txt"
139: (
140:   cd "$LABS_DIR/07-deploy-no-pages"
141:   "$CURSO_DIR/.venv/bin/python" -m unittest -v
142:   "$CURSO_DIR/.venv/bin/python" build.py
143:   test -s dist/index.html
144:   grep -q '<table>' dist/index.html
145:   # O erro apresentado na aula deve realmente quebrar os testes.
146:   sed -i 's/return preco_centavos \* quantidade/return preco_centavos + quantidade/' app.py
147:   if "$CURSO_DIR/.venv/bin/python" -m unittest > "$TEMP/teste-com-erro.log" 2>&1; then
148:     printf '❌ O bug da aula não foi detectado.\n'; exit 1
149:   fi
150:   grep -q FAILED "$TEMP/teste-com-erro.log"
151: )
152: printf '\n✅ Suíte concluída. A publicação real no Actions/Pages é conferida na conta do aluno.\n'

(End of file - total 152 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/scripts/checks.py"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/scripts/checks.py</path>
<type>file</type>
<content>
1: """Verifica requisitos didáticos do YAML, sem executar comandos do aluno."""
2: 
3: import copy
4: import re
5: import sys
6: from pathlib import Path
7: 
8: import yaml
9: 
10: 
11: class WorkflowLoader(yaml.SafeLoader):
12:     # YAML 1.1 interpreta `on` como booleano. Actions usa essa chave como texto.
13:     yaml_implicit_resolvers = copy.deepcopy(yaml.SafeLoader.yaml_implicit_resolvers)
14: 
15: 
16: for letra, resolvers in WorkflowLoader.yaml_implicit_resolvers.items():
17:     WorkflowLoader.yaml_implicit_resolvers[letra] = [
18:         (tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:bool"
19:     ]
20: WorkflowLoader.add_implicit_resolver(
21:     "tag:yaml.org,2002:bool", re.compile(r"^(?:true|false)$", re.I), list("tTfF")
22: )
23: 
24: 
25: def mapping_unico(loader, node, deep=False):
26:     resultado = {}
27:     for key_node, value_node in node.value:
28:         key = loader.construct_object(key_node, deep=deep)
29:         if not isinstance(key, str):
30:             raise ValueError("As chaves do workflow devem ser texto.")
31:         if key in resultado:
32:             raise ValueError(f"Chave duplicada: {key} (linha {key_node.start_mark.line + 1}).")
33:         resultado[key] = loader.construct_object(value_node, deep=deep)
34:     return resultado
35: 
36: 
37: WorkflowLoader.add_constructor("tag:yaml.org,2002:map", mapping_unico)
38: 
39: 
40: def mapa(valor):
41:     return valor if isinstance(valor, dict) else {}
42: 
43: 
44: def lista(valor):
45:     return valor if isinstance(valor, list) else [valor] if valor is not None else []
46: 
47: 
48: def expressao(valor):
49:     return re.sub(r"\s+", "", str(valor))
50: 
51: 
52: class Verificador:
53:     def __init__(self, workflow):
54:         self.w = workflow
55:         self.jobs = mapa(workflow.get("jobs"))
56:         self.falhas = []
57: 
58:     def exigir(self, condicao, dica):
59:         if not condicao:
60:             self.falhas.append(dica)
61: 
62:     def steps(self, job):
63:         return [mapa(s) for s in lista(mapa(self.jobs.get(job)).get("steps"))]
64: 
65:     def action(self, job, nome):
66:         return next((s for s in self.steps(job) if str(s.get("uses", "")).startswith(nome + "@")), {})
67: 
68:     def comandos(self, job):
69:         return "\n".join(str(s.get("run", "")) for s in self.steps(job))
70: 
71:     def evento(self, evento):
72:         eventos = self.w.get("on", {})
73:         return evento in (eventos if isinstance(eventos, (dict, list)) else [eventos])
74: 
75:     def base(self):
76:         self.exigir(bool(self.w.get("name")), "Dê um name ao workflow.")
77:         self.exigir(bool(self.w.get("on")), "Defina os eventos em on.")
78:         self.exigir(bool(self.jobs), "Crie jobs com runs-on e steps.")
79:         self.exigir(mapa(self.w.get("permissions")).get("contents") == "read",
80:                     "Use permissions: contents: read no nível do workflow.")
81:         for nome, valor in self.jobs.items():
82:             job = mapa(valor)
83:             self.exigir(job.get("runs-on") == "ubuntu-latest", f"{nome}: use runs-on: ubuntu-latest.")
84:             self.exigir(isinstance(job.get("steps"), list) and bool(self.steps(nome)), f"{nome}: steps deve ser uma lista de etapas.")
85:             for step in self.steps(nome):
86:                 self.exigir(bool(step.get("uses")) != bool(step.get("run")),
87:                             f"{nome}: cada etapa deve ter uses ou run, apenas um deles.")
88:             for dependencia in lista(job.get("needs")):
89:                 self.exigir(isinstance(dependencia, str) and dependencia in self.jobs and dependencia != nome,
90:                             f"{nome}: needs deve apontar para outro job existente.")
91: 
92:     def testes(self, pr=False):
93:         for evento in (["push", "pull_request"] if pr else ["push"]):
94:             self.exigir(self.evento(evento), f"Acrescente o evento {evento} em on.")
95:             config = mapa(mapa(self.w.get("on")).get(evento))
96:             self.exigir(config.get("branches") == ["main"], f"{evento}: filtre branches: [main].")
97:         self.python("testar")
98:         self.exigir("python -m unittest" in self.comandos("testar"),
99:                     "No job testar, execute python -m unittest -v.")
100:         for step in self.steps("testar"):
101:             if "unittest" in str(step.get("run", "")):
102:                 self.exigir(not step.get("continue-on-error") and "|| true" not in step["run"],
103:                             "Deixe o teste falhar: remova continue-on-error ou || true.")
104: 
105:     def python(self, job):
106:         steps = self.steps(job)
107:         checkout = self.action(job, "actions/checkout")
108:         setup = self.action(job, "actions/setup-python")
109:         self.exigir(bool(checkout), f"{job}: adicione actions/checkout antes de ler os arquivos.")
110:         self.exigir(mapa(setup.get("with")).get("python-version") == "3.12",
111:                     f"{job}: configure actions/setup-python com python-version: '3.12' (entre aspas).")
112:         instalar = next((s for s in steps if "python -m pip install -r requirements.txt" in str(s.get("run", ""))), {})
113:         self.exigir(bool(instalar), f"{job}: instale com python -m pip install -r requirements.txt.")
114:         if checkout and setup and instalar:
115:             self.exigir(steps.index(checkout) < steps.index(setup) < steps.index(instalar),
116:                         f"{job}: a ordem é checkout, setup-python e instalação.")
117:             for step in steps:
118:                 if any(cmd in str(step.get("run", "")) for cmd in ["python -m unittest", "python build.py"]):
119:                     self.exigir(steps.index(instalar) < steps.index(step),
120:                                 f"{job}: instale as dependências antes de testar ou gerar o site.")
121: 
122:     def build(self):
123:         self.testes(pr=True)
124:         self.python("empacotar")
125:         self.exigir("testar" in lista(mapa(self.jobs.get("empacotar")).get("needs")),
126:                     "No job empacotar, use needs: testar.")
127:         self.exigir("python build.py" in self.comandos("empacotar"),
128:                     "No job empacotar, gere o site com python build.py.")
129: 
130:     def verificar(self, n):
131:         self.base()
132:         if n == 1:
133:             self.exigir(self.evento("workflow_dispatch"), "Use on: workflow_dispatch para executar manualmente.")
134:             self.exigir(any("Olá, GitHub Actions!" in self.comandos(j) for j in self.jobs),
135:                         'Adicione uma etapa run que mostre "Olá, GitHub Actions!".')
136:         elif n in (2, 3):
137:             self.testes(pr=n == 3)
138:         elif n == 4:
139:             dispatch = mapa(mapa(self.w.get("on")).get("workflow_dispatch"))
140:             mensagem = mapa(mapa(dispatch.get("inputs")).get("mensagem"))
141:             self.exigir(mensagem.get("type") == "string", "Defina o input mensagem como type: string em workflow_dispatch.")
142:             self.exigir(mapa(self.w.get("env")).get("CURSO") == "GitHub Actions", "Defina env: CURSO: GitHub Actions no workflow.")
143:             envs = [mapa(s.get("env")) for j in self.jobs for s in self.steps(j)]
144:             for chave, referencia in [("MENSAGEM", "inputs.mensagem"), ("AUTOR", "github.actor"),
145:                                       ("TURMA", "vars.TURMA"), ("TOKEN_DEMO", "secrets.CURSO_TOKEN")]:
146:                 self.exigir(any(expressao(e.get(chave)) == "${{" + referencia + "}}" for e in envs),
147:                             f"Passe {referencia} para {chave} usando env na etapa.")
148:         else:
149:             self.build()
150:             if n == 6:
151:                 upload = self.action("empacotar", "actions/upload-artifact")
152:                 config = mapa(upload.get("with"))
153:                 self.exigir(config.get("name") == "site" and str(config.get("path", "")).rstrip("/") == "dist",
154:                             "Envie dist/ com actions/upload-artifact e name: site.")
155:                 self.exigir(config.get("if-no-files-found") == "error" and config.get("retention-days") == 7,
156:                             "No upload, use if-no-files-found: error e retention-days: 7.")
157:                 if upload:
158:                     steps = self.steps("empacotar")
159:                     self.exigir(any("python build.py" in str(s.get("run", "")) for s in steps[:steps.index(upload)]),
160:                                 "Gere o site antes de enviar o artefato.")
161:             elif n == 7:
162:                 self.pages()
163:         return self.falhas
164: 
165:     def pages(self):
166:         publicar = mapa(self.jobs.get("publicar"))
167:         leitura = mapa(mapa(self.jobs.get("empacotar")).get("permissions"))
168:         self.exigir(leitura.get("contents") == "read" and leitura.get("pages") == "read",
169:                     "No job empacotar, conceda contents: read e pages: read para consultar o site.")
170:         self.exigir("empacotar" in lista(publicar.get("needs")), "publicar precisa de needs: empacotar.")
171:         permissoes = mapa(publicar.get("permissions"))
172:         self.exigir(permissoes.get("pages") == "write" and permissoes.get("id-token") == "write",
173:                     "No job publicar, conceda pages: write e id-token: write.")
174:         self.exigir(mapa(publicar.get("environment")).get("name") == "github-pages",
175:                     "Use environment: name: github-pages no job publicar.")
176:         for job in ["empacotar", "publicar"]:
177:             condicao = expressao(mapa(self.jobs.get(job)).get("if", ""))
178:             self.exigir("github.ref=='refs/heads/main'" in condicao and "github.event_name!='pull_request'" in condicao,
179:                         f"{job}: limite o deploy à main e exclua pull_request com a condição do enunciado.")
180:         self.exigir(bool(self.action("empacotar", "actions/configure-pages")), "Adicione actions/configure-pages no build.")
181:         upload = self.action("empacotar", "actions/upload-pages-artifact")
182:         self.exigir(str(mapa(upload.get("with")).get("path", "")).rstrip("/") == "dist",
183:                     "Envie dist/ usando actions/upload-pages-artifact.")
184:         deploy = self.action("publicar", "actions/deploy-pages")
185:         self.exigir(bool(deploy) and deploy.get("id") == "deploy", "Use actions/deploy-pages com id: deploy.")
186:         url = mapa(publicar.get("environment")).get("url")
187:         self.exigir(expressao(url) == "${{steps.deploy.outputs.page_url}}", "Use a saída steps.deploy.outputs.page_url na URL do environment.")
188: 
189: 
190: def main():
191:     n = int(sys.argv[1])
192:     arquivo = Path(sys.argv[2]) / ".github/workflows/ci.yml"
193:     try:
194:         workflow = yaml.load(arquivo.read_text(encoding="utf-8"), Loader=WorkflowLoader)
195:         if not isinstance(workflow, dict):
196:             raise ValueError("O workflow deve ser um mapa YAML, com name, on e jobs.")
197:         falhas = Verificador(workflow).verificar(n)
198:     except (OSError, ValueError, yaml.YAMLError) as exc:
199:         print(f"❌ Não consegui ler {arquivo}: {exc}\n💡 Confira o nome do arquivo, a indentação e as chaves do YAML.")
200:         return 1
201:     if falhas:
202:         print(f"❌ Exercício {n:02d}: ajuste os seguintes pontos:")
203:         for dica in falhas:
204:             print(f"  💡 {dica}")
205:         return 1
206:     print(f"✅ Exercício {n:02d}: requisitos locais atendidos.")
207:     print("Confira também a execução e a entrega pedida na aba Actions; esta análise é estática.")
208:     return 0
209: 
210: 
211: if __name__ == "__main__":
212:     sys.exit(main())

(End of file - total 212 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/scripts/lib.sh"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/scripts/lib.sh</path>
<type>file</type>
<content>
1: #!/usr/bin/env bash
2: # Biblioteca compartilhada pelos comandos do curso.
3: set -euo pipefail
4: 
5: SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
6: CURSO_DIR="$(cd "$SCRIPTS_DIR/.." && pwd)"
7: LABS_DIR="${LABS_DIR:-$HOME/labs}"
8: LAB_NOMES=("" "primeiro-workflow" "testes-no-push" "checks-no-pull-request"
9:   "variaveis-e-contextos" "jobs-e-dependencias" "artefatos-do-build" "deploy-no-pages")
10: 
11: info() { printf '▶ %s\n' "$*"; }
12: ok() { printf '✅ %s\n' "$*"; }
13: erro() { printf '❌ %s\n' "$*" >&2; }
14: 
15: exigir_codespaces() {
16:   if [[ "${CODESPACES:-}" != true && "${CURSO_MODO_TESTE:-0}" != 1 ]]; then
17:     erro "Este curso usa obrigatoriamente o GitHub Codespaces. Crie um Codespace com o modelo Blank e siga a preparação do README."
18:     exit 2
19:   fi
20: }
21: 
22: normalizar_num() {
23:   local n="${1%%-*}"
24:   [[ "$n" =~ ^[0-9]{1,2}$ ]] || return 1
25:   (( 10#$n >= 1 && 10#$n <= 7 )) || return 1
26:   printf '%02d' "$((10#$n))"
27: }
28: 
29: lab_nome() { printf '%s' "${LAB_NOMES[$((10#$1))]}"; }
30: lab_dir() { printf '%s/%s-%s' "$LABS_DIR" "$1" "$(lab_nome "$1")"; }
31: 
32: resolver_lab() {
33:   local entrada="${1:-}" rel nn pasta labs
34:   if [[ -z "$entrada" ]]; then
35:     pasta="$(pwd -P)"
36:     labs="$(cd "$LABS_DIR" && pwd -P)"
37:     rel="${pasta#"$labs"/}"
38:     [[ "$rel" != "$pasta" ]] || { erro "Informe o exercício: check.sh 01 (de 01 a 07)."; return 1; }
39:     entrada="${rel%%/*}"
40:   fi
41:   nn="$(normalizar_num "$entrada")" || { erro "Exercício inválido: '$entrada'. Use 01 a 07."; return 1; }
42:   printf '%s' "$nn"
43: }
44: 
45: g() { git -c commit.gpgsign=false -c core.hooksPath=/dev/null -c core.editor=true "$@"; }

(End of file - total 45 lines)
</content>
```

---

## Assistant (Build · GPT-6 Astra · 19.7s)

_Thinking:_

**Designing act mode**

_Thinking:_

**Checking act artifact support**

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://nektosact.com/usage/index.html",
  "format": "markdown"
}
```

**Output:**
```
 Usage guide - act - User Guide | Manual | Docs | Documentation                       

1.  [**1.** Introduction](../introduction.html)
2.  [**2.** Installation](../installation/index.html)
3.  1.  [**2.1.** Arch](../installation/arch.html)
    2.  [**2.2.** Chocolatey](../installation/chocolatey.html)
    3.  [**2.3.** COPR](../installation/copr.html)
    4.  [**2.4.** GitHub CLI](../installation/gh.html)
    5.  [**2.5.** Homebrew](../installation/homebrew.html)
    6.  [**2.6.** MacPorts](../installation/macports.html)
    7.  [**2.7.** Nix](../installation/nix.html)
    8.  [**2.8.** Scoop](../installation/scoop.html)
    9.  [**2.9.** WinGet](../installation/winget.html)
4.  [**3.** Usage guide](../usage/index.html)
5.  1.  [**3.1.** Runners](../usage/runners.html)
    2.  [**3.2.** Custom container engine](../usage/custom_engine.html)
    3.  [**3.3.** GitHub Enterprise](../usage/github_enterprise.html)
    4.  [**3.4.** Schema](../usage/schema.html)
6.  [**4.** Unsupported functionality](../not_supported.html)
7.  1.  **4.1.** Support matrix
        
    2.  [**4.2.** Docker context](../missing_functionality/docker_context.html)
8.  [**5.** Known issues](../known_issues/index.html)
9.  1.  [**5.1.** MODULE\_NOT\_FOUND](../known_issues/module_not_found.html)
10.  [**6.** Integrations](../integrations.html)

-   Light (default)
-   Rust
-   Coal
-   Navy
-   Ayu

# act - User Guide | Manual | Docs | Documentation

[](../print.html "Print this book")[](https://github.com/nektos/act-docs "Git repository")[](https://github.com/nektos/act-docs/edit/main/src/usage/index.md "Suggest an edit")

# [Usage guide](#usage-guide)

## [Events](#events)

-   `act` has basic event support, it will try to get as much information from local repository as possible, although this might be not enough for certain event types.
-   Running `act` without any event name specified will run with event `push`.
-   For a list of event names, please see [events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows "events-that-trigger-workflows").

---

-   `push`:

```shell=sh
act push
```

> Runs all workflows with `push` event

-   `pull_request`:

```shell=sh
act pull_request
```

-   `schedule`:

```shell=sh
act schedule
```

To list all workflows for a given event, use `-l`/`--list`:

```shell=sh
act -l pull_request
```

### [Using event file to provide complete event payload](#using-event-file-to-provide-complete-event-payload)

If your workflow relies on passed event properties, you will have to provide the required properties in the event file, example:

> To partially simulate `pull_request` event, you have to provide at least `head_ref` and `base_ref`. This values can be later accessed via `${{ github.event.pull_request.<...> }}`

```json
{
  "pull_request": {
    "head": {
      "ref": "sample-head-ref"
    },
    "base": {
      "ref": "sample-base-ref"
    }
  }
}
```

> To partially simulate `push` event with a tag, you need to provide `ref` which will be accessible via `${{ github.event.ref }}`

```json
{
  "ref": "refs/tags/this-is-a-tag"
}
```

## [Workflows](#workflows)

> By default `act` will run **all** workflows in `.github/workflows`.

You can override that behaviour with `-W`/`--workflows` flag by specifying the directory containing workflow files.

```shell=sh
act -W '.github/workflows/'
```

> This example will run **all jobs** in **all workflows** in the directory `.github/workflows` but only if the trigger event is `push`

---

or by specifying the exact workflow file to run

```shell=sh
act -W '.github/workflows/checks.yml'
```

> This example will run **all jobs** in `.github/workflows/checks.yml` workflow file but only if its trigger event is `push`

## [Jobs](#jobs)

> By default `act` will run **all jobs** in **all workflows** that are triggered by `push` event

```shell=sh
act -j 'test'
```

> This example will run **all jobs** named `test` in **all workflows** that trigger on `push` event

## [Configuration file](#configuration-file)

Act can be configured using `.actrc` files. All found arguments will be parsed and appended to a list, in order of: .actrc as per the XDG spec, .actrc in HOME directory, .actrc in invocation directory, cli arguments.

Format: One argument per line, no comments supported.

Example:

```
--container-architecture=linux/amd64
--action-offline-mode
```

# [Vars](#vars)

To run `act` with repository variables that are accessible inside the workflow via `${{ vars.VARIABLE }}`, you can enter them interactively or load them from a file. The following options are available for providing github repository variables:

-   `act --var VARIABLE=some-value` - use `some-value` as the value for `VARIABLE`.
-   `act --var-file my.variables` - load variables values from `my.variables` file.
-   The variables file format is the same as `.env` format

## [Secrets](#secrets)

To run `act` with secrets, you can enter them interactively, supply them as environment variables or load them from a file. The following options are available for providing secrets:

---

## [**⚠ WARNING ⚠**](#-warning-)

When inserting sensitive data in your terminal, it might be saved as plain text to history file provided by your shell. To mitigate that, prefix `act ...` command with a space (not all shells respect that) or use secure input (explained below) to insert data.

---

-   `act -s MY_SECRET=some-value` - use `some-value` as the value for `MY_SECRET`.
-   `act -s MY_SECRET` - check for an environment variable named `MY_SECRET` and use it if it exists. If the environment variable is not defined, prompt the user for a value. **This is recommended way of typing/pasting a secret into terminal, as `act` will provide secure input prompt for you to type/paste your secret which will not be saved in your shell history file.**
-   `act --secret-file my.secrets` - load secrets values from `my.secrets` file.
    -   secrets file format is the same as `.env` format

### [`GITHUB_TOKEN`](#github_token)

GitHub [automatically provides](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#about-the-github_token-secret) a `GITHUB_TOKEN` secret when running workflows inside GitHub. If your workflow fails with an error about `token`, it most likely requires `GITHUB_TOKEN` to be set up. If your workflow depends on this token, you need to create a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and pass it to `act` as a secret:

```bash
act -s GITHUB_TOKEN=[insert token or leave blank and omit equals for secure input]
```

If [GitHub CLI](https://cli.github.com/) is installed, the [`gh auth token`](https://cli.github.com/manual/gh_auth_token) command can be used to automatically pass the token to act

```bash
act -s GITHUB_TOKEN="$(gh auth token)"
```

**WARNING**: `GITHUB_TOKEN` will be logged in shell history if not inserted through secure input or (depending on your shell config) the command is prefixed with a whitespace.

## [`.env`/`.secrets` files structure](#envsecrets-files-structure)

`.env` and `.secrets` files are using Ruby's gem [`dotenv`](https://github.com/bkeepers/dotenv) format through [`godotenv`](https://github.com/joho/godotenv) library

Example:

```shell
export MY_ENV='value'
PRIV_KEY="---...\nrandom text\n...---"
JSON="{\n\"name\": \"value\"\n}"
SOME_VAR=SOME_VALUE
```

To see more examples, go to [https://github.com/joho/godotenv/tree/v1.4.0/fixtures](https://github.com/joho/godotenv/tree/v1.4.0/fixtures)

## [Skipping jobs](#skipping-jobs)

You cannot use the `env` context in job level if conditions, but you can add a custom event property to the `github` context. You can use this method also on step level if conditions.

```yml
on: push
jobs:
  deploy:
    if: ${{ !github.event.act }} # skip during local actions testing
    runs-on: ubuntu-latest
    steps:
    - run: exit 0
```

And use this `event.json` file with act otherwise the Job will run:

```json
{
    "act": true
}
```

Run act like

```sh
act -e event.json
```

*Hint: you can add / append `-e event.json` as a line into `./.actrc`*

## [Skipping steps](#skipping-steps)

Act adds a special environment variable `ACT` that can be used to skip a step that you don't want to run locally. E.g. a step that posts a Slack message or bumps a version number. **You cannot use this method in job level if conditions, see [Skipping jobs](#skipping-jobs)**

```yml
- name: Some step
  if: ${{ !env.ACT }}
  run: |
    ...
```

## [Pass Inputs to Manually Triggered Workflows](#pass-inputs-to-manually-triggered-workflows)

Example workflow file

```yaml
on:
  workflow_dispatch:
    inputs:
      NAME:
        description: "A random input name for the workflow"
        type: string
      SOME_VALUE:
        description: "Some other input to pass"
        type: string
jobs:
  test:
    name: Test
    runs-on: ubuntu-latest
    steps:
      - name: Test with inputs
        run: |
          echo "Hello ${{ github.event.inputs.NAME }} and ${{ github.event.inputs.SOME_VALUE }}!"
```

### [via input or input-file flag](#via-input-or-input-file-flag)

-   `act --input NAME=some-value` - use `some-value` as the value for `NAME` input.
-   `act --input-file my.input` - load input values from `my.input` file.
    -   input file format is the same as `.env` format

### [via JSON](#via-json)

Example JSON payload file conveniently named `payload.json`

```json
{
  "inputs": {
    "NAME": "Manual Workflow",
    "SOME_VALUE": "ABC"
  }
}
```

Command for triggering the workflow

```sh
act workflow_dispatch -e payload.json
```

## [Specifying Matrix](#specifying-matrix)

You can selectively choose a subset of matrix options to run by specifying the `--matrix` flag. It will only run those matrix configurations which include your specified values.

Example workflow file

```yaml
name: matrix-with-user-inclusions
on: push
jobs:
  build:
    name: Matrix
    runs-on: ubuntu-latest
    steps:
      - run: echo ${NODE_VERSION}
        env:
          NODE_VERSION: ${{ matrix.node }}
    strategy:
      matrix:
        os: [ubuntu-18.04, macos-latest]
        node: [4, 6, 8, 10]
        exclude:
          - os: macos-latest
            node: 4
        include:
          - os: ubuntu-16.04
            node: 10
```

In this case if we only wanted to run this workflow for node 8, then we would run `act push --matrix node:8`

This will trigger the workflow to use the following matrix configurations only:

-   `os: ubuntu-18.04, node: 8`
-   `os: macos-latest, node: 8`

Similarly if we just wanted to trigger this workflow for node 10 and macos-latest then we would run `act push --matrix node:10 --matrix os:macos-latest`.

This will trigger the workflow to use the following matrix configurations only:

-   `os: macos-latest, node 10`

Note that using the `--matrix` flag you can't add new values (for e.g. running the above workflow for node 20). It will simply ignore it. Moreover, the `exclude` field in the workflow will take precedence over the `--matrix` flag (for e.g. running the above workflow for only macos-latest and node 4 will result in no matrix configuration being used)

## [Action Offline Mode](#action-offline-mode)

If you want to speed up running act and using cached actions and container images you can enable this mode.

-   stops pulling existing images
-   stops failing if an action has been cached and you cannot connect to GitHub
-   pulls nonexistent actions and images
-   act will work offline if it has at least ran once while you are online
-   get rid of unnecessary timeouts when you have an unstable connection to GitHub or Container registries
-   work around rate limit problems

```sh
  act --action-offline-mode
```

or a `.actrc` file in your cwd like

```
--action-offline-mode
```

## [Action Artifacts](#action-artifacts)

**Currently the artifacts server is not started automatically with act**, this means the following env variables are blank by default.

-   `ACTIONS_RUNTIME_URL`
-   `ACTIONS_RUNTIME_TOKEN`
-   `ACTIONS_RESULTS_URL`

to enable this feature use the cli flag `--artifact-server-path $PWD/.artifacts`.

While enabled these values are also available in `run` steps, which doesn't match `actions/runner` aka GitHub Actions where they are blank.

Currently `actions/upload-artifact@v3` and `actions/upload-artifact@v4` together with `actions/download-artifact@v3` and `actions/download-artifact@v4` should be able to upload and download their artifacts within the current workflow run.

Not supported v4 features are to download artifacts from a different run, workflow or repository by providing a GitHub Token.

[](../installation/winget.html "Previous chapter")[](../usage/runners.html "Next chapter")

[](../installation/winget.html "Previous chapter")[](../usage/runners.html "Next chapter")
```

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://nektosact.com/not_supported.html",
  "format": "markdown"
}
```

**Output:**
```
 Unsupported functionality - act - User Guide | Manual | Docs | Documentation                       

1.  [**1.** Introduction](introduction.html)
2.  [**2.** Installation](installation/index.html)
3.  1.  [**2.1.** Arch](installation/arch.html)
    2.  [**2.2.** Chocolatey](installation/chocolatey.html)
    3.  [**2.3.** COPR](installation/copr.html)
    4.  [**2.4.** GitHub CLI](installation/gh.html)
    5.  [**2.5.** Homebrew](installation/homebrew.html)
    6.  [**2.6.** MacPorts](installation/macports.html)
    7.  [**2.7.** Nix](installation/nix.html)
    8.  [**2.8.** Scoop](installation/scoop.html)
    9.  [**2.9.** WinGet](installation/winget.html)
4.  [**3.** Usage guide](usage/index.html)
5.  1.  [**3.1.** Runners](usage/runners.html)
    2.  [**3.2.** Custom container engine](usage/custom_engine.html)
    3.  [**3.3.** GitHub Enterprise](usage/github_enterprise.html)
    4.  [**3.4.** Schema](usage/schema.html)
6.  [**4.** Unsupported functionality](not_supported.html)
7.  1.  **4.1.** Support matrix
        
    2.  [**4.2.** Docker context](missing_functionality/docker_context.html)
8.  [**5.** Known issues](known_issues/index.html)
9.  1.  [**5.1.** MODULE\_NOT\_FOUND](known_issues/module_not_found.html)
10.  [**6.** Integrations](integrations.html)

-   Light (default)
-   Rust
-   Coal
-   Navy
-   Ayu

# act - User Guide | Manual | Docs | Documentation

[](print.html "Print this book")[](https://github.com/nektos/act-docs "Git repository")[](https://github.com/nektos/act-docs/edit/main/src/not_supported.md "Suggest an edit")

# [Unsupported functionality](#unsupported-functionality)

While we try to implement all features of GitHub Runners, due to design choices and manpower available it's not possible to make `act` completely compatible.

Here is a list of features that is (yet) to be implemented or is decided as not going to be worked on by `act` maintainers.

## [Planned](#planned)

-   `concurrency` is ignored
-   `run-name` is ignored
-   Step summary not processed
    -   Values written in each step to the file pointed by `GITHUB_STEP_SUMMARY`, `$GITHUB_STEP_SUMMARY` and `$env:GITHUB_STEP_SUMMARY` are discarded, each step has its own empty step summary file at the beginning
-   Problem matcher ignored
-   Annotations ignored
-   Incomplete `github` context
-   Run steps cancellation not implemented
-   `job.permissions` ignored
-   `job.timeout-minutes` ignored
-   `job.continue-on-error` ignored
-   `PATH` of container / of act must contain node for nodejs actions, github runner has their own copy for both container and host
-   Openid Connect url is not defined
-   `job.environment` ignored and scoping secrets by deployment environment is not supported

## [Functionality that is not going to be worked on](#functionality-that-is-not-going-to-be-worked-on)

-   [Docker context](./missing_functionality/docker_context.html) ([#583](https://github.com/nektos/act/issues/583))

[](usage/schema.html "Previous chapter")[](missing_functionality/docker_context.html "Next chapter")

[](usage/schema.html "Previous chapter")[](missing_functionality/docker_context.html "Next chapter")
```

**Tool: bash**

**Input:**
```json
{
  "command": "docker info --format '{{.ServerVersion}}'",
  "timeout": 10000
}
```

**Output:**
```
29.3.0

```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/templates/projeto/README.md"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/templates/projeto/README.md</path>
<type>file</type>
<content>
1: # Cardápio da comunidade
2: 
3: Projeto de prática do curso de GitHub Actions. Edite e execute os comandos no
4: **GitHub Codespaces**. Os workflows executam em runners hospedados pelo GitHub.
5: 
6: ## Executar no terminal do Codespace
7: 
8: ```bash
9: python3 -m venv .venv
10: source .venv/bin/activate
11: python -m pip install -r requirements.txt
12: python -m unittest -v
13: python build.py
14: ```
15: 
16: O build gera `dist/index.html`. Os preços em `app.py` são expressos em centavos.
17: Os exercícios ficam no [site do curso](https://fsilva-alt.github.io/devops-ghactions/).

(End of file - total 17 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/home/lse/projects/ocean/devops-ghactions/templates/projeto/cardapio.md"
}
```

**Output:**
```
<path>/home/lse/projects/ocean/devops-ghactions/templates/projeto/cardapio.md</path>
<type>file</type>
<content>
1: # Cardápio da comunidade
2: 
3: Site publicado durante o curso de GitHub Actions.
4: 
5: | Receita | Preço |
6: |---|---:|
7: | Bolo de cenoura | R$ 40,00 |
8: | Brigadeiro | R$ 3,00 |
9: | Pão de queijo | R$ 5,00 |

(End of file - total 9 lines)
</content>
```

---

## Assistant (Build · GPT-6 Astra · 40.4s)

---

