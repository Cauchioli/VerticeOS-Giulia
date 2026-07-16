# 02-PROTOCOLO — O Ciclo de Operação do Sistema

Todo ciclo de interação entre o usuário e o agente segue um ciclo fixo dividido em três fases: Início (Resgate), Execução (Construção) e Fechamento (Consolidação). Isso garante que o conhecimento gerado nunca se perca.

---

## 🏁 1. Início de Sessão (Retrieval)
1. O agente lê a nota [[00-ENTRADA]] para carregar o mapa do cérebro.
2. O agente puxa os arquivos de contexto estratégico da pasta `_memoria/` do Vértice OS para se alinhar com o momento atual do negócio do usuário.
3. Se a tarefa delegada for complexa, estrutural ou irreversível, o agente deve obrigatoriamente descrever um plano curto (< 1 tela) e solicitar aprovação no chat antes de começar a editar arquivos de código.

---

## ⚙️ 2. Execução (Grounding)
1. Para cada argumento ou texto produzido, o agente realiza buscas semânticas no RAG para encontrar notas-tese antigas, transcrições e playbooks.
2. Ao criar novas notas no cérebro, o agente deve conectá-las usando wikilinks por *basename* (ex: `[[Minha Nova Nota]]`) conectando o nó a um MOC (Map of Content) da pasta `50-referencia/` ou de outro MOC ativo para que a nota não fique órfã no grafo do Obsidian.
3. Toda nova informação crítica deve vir acompanhada da tag `#tipo/aprendizado` ou `#tipo/decisao` e do link do arquivo de origem na seção de metadados.

---

## 🏁 3. Encerramento (Consolidation)
Ao concluir uma sessão longa ou quando solicitado (via comando `/fechar-sessao`):
1. **QA de Integridade:** O agente audita o vault para garantir:
   * `0 links quebrados` (todos os wikilinks devem apontar para notas que existem).
   * `0 notas órfãs` (toda nota precisa ter pelo menos um link de entrada).
2. **Atualização da Memória Estratégica:** Se a sessão gerou novas decisões de marketing ou novos frentes de vendas, o agente atualiza o arquivo `estrategia.md` ou `preferencias.md` do Vértice OS.
3. **Commit do Histórico (Git):** O agente faz o commit do progresso da sessão para manter a rastreabilidade do histórico:
   `git add . && git commit -m "Sessão concluída: [resumo das melhorias]"`
4. **Indexação Semântica:** O agente dispara a indexação incremental do RAG local em background para indexar as novas notas e atualizações, garantindo que o cérebro comece a próxima sessão totalmente atualizado:
   `python rag/rag_acervo.py index`
