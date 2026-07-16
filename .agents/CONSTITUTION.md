# Vértice OS — Constitution
> **Versão:** 1.0.0 | **Status:** Ativa

Este documento define os princípios invioláveis do Vértice OS. Todos os agentes e engines DEVEM respeitar estes princípios. São verificados antes de qualquer ação relevante.

---

## Sistema de Gates

| Nível | Comportamento | Quando usar |
|---|---|---|
| **BLOCK** | Impede a ação. Requer correção antes de continuar. | Regras invioláveis — violar destrói integridade do sistema |
| **WARN** | Permite continuar, mas alerta o usuário. | Regras importantes que podem ter exceções justificadas |
| **INFO** | Registra internamente. Não interrompe. | Boas práticas que, se ignoradas, acumulam débito |

---

## Princípio I — Integridade de Dados (BLOCK)

**Regras:**
- BLOCK: Nunca inventar dados, métricas ou informações sem fonte verificável
- BLOCK: Nunca sobrescrever `_memoria/empresa.md`, `preferencias.md` ou `estrategia.md` sem aprovação explícita do usuário
- BLOCK: Nunca registrar dados confidenciais de clientes finais fora do ambiente local
- BLOCK: Afirmações sem fonte direta no acervo devem ser marcadas com `[VERIFICAR]`

---

## Princípio II — Identidade Visual (BLOCK)

**Regras:**
- BLOCK: Uso de emojis em posts, carrosséis, propostas ou headlines de autoridade
- BLOCK: Usar paleta de cores diferente da definida em `identidade/design-guide.md` sem justificativa explícita
- BLOCK: Usar tipografia diferente de Cormorant Garamond (títulos) + Inter (corpo) sem justificativa

---

## Princípio III — Integridade do Código e Repositório (BLOCK)

**Regras:**
- BLOCK: Usar caminhos absolutos no código ou em arquivos de configuração que serão versionados
- BLOCK: Sobrescrever `rag/rag_config.json` apagando configurações existentes do cliente
- BLOCK: Fazer commit de arquivos com tokens, senhas ou dados sensíveis

---

## Princípio IV — Qualidade de Entrega (WARN)

**Regras:**
- WARN: Entregar copy sem consultar `_memoria/preferencias.md` (risco de violar tom de voz)
- WARN: Entregar resposta sobre o negócio sem consultar RAG quando servidor está online
- WARN: Criar nota no Obsidian sem pelo menos 1 link de entrada (risco de nota órfã)
- WARN: Gerar mais de 3 notas estruturadas no vault em uma única sessão (risco de estouro)
- WARN: Entregar output que pode conter um padrão registrado em `aprendizado/gotchas.md`

---

## Princípio V — Aprendizado Contínuo (WARN)

**Regras:**
- WARN: Encerrar sessão sem verificar se houve decisões estratégicas a registrar em `_memoria/`
- WARN: Receber correção de estilo ou tom sem sugerir atualizar `_memoria/preferencias.md`
- WARN: Sessão com erros identificados sem registrar em `aprendizado/gotchas.md`

---

## Princípio VI — Boas Práticas Operacionais (INFO)

**Regras:**
- INFO: Sessão encerrada sem rodar `python rag/rag_acervo.py index`
- INFO: Engine acionado sem consultar MOC relevante em `segundo-cerebro/50-referencia/mocs/`
- INFO: Resposta longa gerada sem citar fonte do trecho recuperado do RAG

---

## Protocolo de Autodeclaração

Antes de executar qualquer ação que possa violar um princípio BLOCK ou WARN, o agente deve:

1. Identificar qual princípio está em risco
2. Declarar em 1 linha: `[GATE WARN — Princípio IV: consultando preferencias.md antes de prosseguir]`
3. Executar a verificação
4. Prosseguir ou solicitar aprovação

Para violações BLOCK: parar, declarar o bloqueio e aguardar instrução do usuário.

---

## Referências

- Princípios derivados de: `.agents/AGENTS.md`
- Erros aprendidos: `.agents/aprendizado/gotchas.md`
- Gates verificados em: início de sessão (`/abrir`) e encerramento (`/fechar-sessao`)
