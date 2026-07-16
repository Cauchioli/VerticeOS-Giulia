# Vértice OS — Dra. Giulia Bonfá (Previdenciário & Cível)

Este é o seu **Vértice OS personalizado**: um sistema operacional inteligente instalado diretamente na sua máquina física, projetado para eliminar o trabalho manual do seu escritório, analisar processos judiciais volumosos e organizar toda a sua base de contratos, contatos e petições.

O sistema roda localmente, garantindo **100% de privacidade e conformidade com a LGPD** (seus dados e documentos de clientes não são enviados para terceiros).

---

## ⚡ Guia Rápido: Como Usar no Dia a Dia

Para que a inteligência do sistema funcione, o computador precisa estar conectado à memória do seu escritório. Toda vez que você ligar o computador para trabalhar, siga estes passos simples:

### Passo 1: Ligar o Servidor de Memória (RAG)
1. Abra a pasta do projeto no seu computador.
2. Vá até a pasta `rag/` e dê um **clique duplo** no arquivo:
   👉 **`iniciar_rag.bat`**
3. Uma tela preta de terminal vai abrir e deve ser mantida aberta em segundo plano enquanto você trabalha. Ela indica que a memória local da IA está ativa.

### Passo 2: Alimentar a IA com Novos Arquivos
* A pasta **`dados/`** na raiz do projeto é o cérebro do seu escritório.
* Sempre que receber um novo processo volumoso em PDF, documentos de clientes, CNIS ou atas de reuniões, jogue os arquivos diretamente dentro dessa pasta `dados/`.

### Passo 3: Atualizar a Memória da IA
* Sempre que você colocar novos arquivos na pasta `dados/` ou fizer anotações novas no seu Segundo Cérebro (Obsidian), você precisa avisar o sistema para ler as novidades.
* Dê um **clique duplo** no arquivo:
   👉 **`indexar_agora.bat`** (dentro da pasta `rag/`)
* O terminal lerá os novos documentos em segundos e fechará automaticamente. A memória do seu sistema já está atualizada.

---

## 🚀 Setup Inicial (Como instalar na primeira vez)

Se este é o seu primeiro acesso ao sistema, siga este roteiro de instalação simplificado:

### 1. Instalar o Motor de Busca (Python)
1. Certifique-se de que o **Python** está instalado na sua máquina (caso não esteja, baixe o instalador oficial para Windows).
2. Na pasta raiz do Vértice OS, dê um **clique duplo** no arquivo:
   👉 **`install_rag.py`**
3. O script instalará silenciosamente todas as dependências leves necessárias (incluindo o banco de dados LanceDB local).

### 2. Ativar o Seu Agente
1. Abra o seu editor ou chat de I.A. (como o Claude Code ou ChatGPT local conectado ao diretório).
2. Digite o comando de onboarding:
   👉 **`/instalar`**
3. O seu agente previdenciário lerá o diagnóstico comercial que o Leo Cauchioli preparou e iniciará uma breve entrevista de validação com você para calibrar o tom de voz do sistema.

---

## 🗺️ O que está dentro do seu Sistema Operacional?

*   **`_memoria/`** — As regras de negócio do seu escritório (metas financeiras, custos fixos, margens de Salário Maternidade e a renegociação de parcerias).
*   **`.agents/`** — As regras de comportamento do robô (configurado para chamá-la de Dra. Giulia e focar em praticidade total).
*   **`app/`** — O seu painel visual de controle (onde você gerencia prazos e visualiza o CRM).
*   **`dados/`** — A pasta de entrada onde você joga os PDFs e documentos de clientes para indexação.
*   **`saidas/`** — Onde o sistema salvará as propostas de honorários e petições geradas.
*   **`templates/`** — Os modelos de design premium (propostas e contratos no formato off-white Vértice OS).

---

## 🎭 Seus Comandos e Atalhos Úteis

Sempre que conversar com o agente de I.A. no sistema, use os atalhos abaixo para ativar automações imediatas:

*   **`/abrir`** — Carrega toda a memória do seu escritório no início de cada dia de trabalho.
*   **`/proposta-comercial`** — Cria uma proposta de honorários premium no padrão Vértice OS.
*   **`/carrossel`** — Gera ideias e roteiros de carrosséis visuais para o seu Instagram.
*   **`/growth-engine`** — Analisa a performance financeira da sua semana e aponta gargalos.

---

*Menos trabalho manual. Mais advocacia.*
**Até o próximo bug.**
