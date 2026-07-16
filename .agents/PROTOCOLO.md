# PROTOCOLO — Ciclo Operacional do Agente

> Este arquivo define o fluxo fixo de cada sessão de trabalho.
> Seguir este protocolo evita deriva fática, perda de contexto e desorganização acumulada.

---

## Início de Sessão (Retrieval)

1. Ler `_memoria/00-ENTRADA.md` para alinhar o mapa do workspace
2. Carregar os 4 arquivos de contexto:
   - `_memoria/empresa.md`
   - `_memoria/preferencias.md`
   - `_memoria/estrategia.md`
   - `identidade/design-guide.md`
3. Verificar RAG: `GET http://127.0.0.1:8799/health`
   - **Online:** consultar contexto relevante antes de cada engine
   - **Offline:** avisar em 1 linha e prosseguir com `_memoria/`
4. Identificar a tarefa. Se for complexa ou irreversível:
   - Escrever plano curto (< 1 tela)
   - Obter aprovação explícita antes de agir
5. Consultar o MOC relevante no Obsidian (`50-referencia/mocs/`) se existir

---

## Execução (Operation)

1. Usar wikilinks `[[basename]]` nas notas — nunca especificar pasta
2. Inserir fontes verificáveis em toda nota criada
3. Marcar afirmações sem fonte com `[VERIFICAR]`
4. Entregáveis de clientes finais → salvar em pasta separada, nunca no vault
5. Ao criar ou modificar notas importantes, rodar indexação incremental:
   ```bash
   python rag/rag_acervo.py index
   ```
6. Mostrar progresso ao usuário antes de finalizar tarefas longas

---

## Encerramento de Sessão (Consolidation)

Ao final de cada sessão relevante, executar ou instruir:

### 1. QA de Integridade (se houve notas criadas no Obsidian)
Verificar:
- `0 links quebrados`
- `0 notas órfãs` (sem links de entrada)
- `1 componente conexo` no grafo

### 2. Atualizar Memória
Se a sessão gerou decisões estratégicas, ajustes de oferta ou mudanças de foco:
- Atualizar `_memoria/estrategia.md` com o que mudou
- Se o tom ou estilo foi corrigido: atualizar `_memoria/preferencias.md`

### 3. Git Commit do Vault (se o Obsidian tiver git configurado)
```bash
git add .
git commit -m "Sessão: [resumo curto do que foi feito]"
```

### 4. Indexação Final do RAG
```bash
python rag/rag_acervo.py index
```
Garante que tudo criado nesta sessão já está disponível na próxima.

---

## Regras de Checkpoint

- Toda ação complexa ou irreversível: **parar, mostrar plano, aguardar aprovação**
- Nunca agir silenciosamente em arquivos críticos (`_memoria/`, `AGENTS.md`, `rag_config.json`)
- Aprendizados permanentes do usuário → sempre sugerir salvar em `_memoria/preferencias.md`

---

## Skill de Atalho

Use `/fechar-sessao` para executar automaticamente os passos de encerramento:
git commit + indexação do RAG + atualização de memória.
