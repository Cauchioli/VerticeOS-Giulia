---
name: research-engine
description: >
  Transforma comentários, reviews, posts e feedback do mercado em inteligência acionável para
  conteúdo, oferta e vendas. O usuário cola as fontes ou a skill busca no sistema. Saídas: frases
  reais para copy, gaps de concorrência, ideias de conteúdo e ajustes de oferta. Use quando o
  usuário disser "o que o mercado está falando", "pesquisa de mercado", "research engine",
  "o que meu cliente pensa", "análise de concorrente", ou /research-engine.
---

# /research-engine — Inteligência de Mercado (Vértice OS)

O mercado ensina continuamente quem está disposto a ouvir. O Research Engine transforma ruído de comentários e reviews em matéria-prima estratégica para conteúdo, oferta e vendas.

## Filosofia

As melhores headlines do mundo não foram inventadas — foram extraídas de frases reais que clientes disseram para descrever seu problema. O Research Engine faz exatamente isso de forma sistemática.

## Contexto Necessário (leitura automática)

- `_memoria/empresa.md` — nicho, avatar, produto
- `app/instagram_cache.json` — comentários e posts do próprio perfil (se existir)
- `dados/` — qualquer arquivo de feedback, formulários ou NPS

## Fontes de Pesquisa (o usuário fornece ou a skill busca)

O usuário pode fornecer (colar diretamente na conversa):
- Comentários do Instagram/LinkedIn/TikTok
- Reviews do Google Meu Negócio
- Respostas de formulários
- Conversas de WhatsApp (anonimizadas)
- Posts de grupos de Facebook/LinkedIn do nicho
- Conteúdo de concorrentes (URL ou texto)

Se o usuário não fornecer: solicitar que cole pelo menos uma fonte antes de prosseguir.

**Versão futura (automatizada):** integração com browser para busca em Reddit, grupos públicos, Google Reviews e comentários de concorrentes.

## Saídas — Pasta `dados/research/[mes-ano]/`

### 1. insights-mercado.md
Síntese dos principais padrões encontrados nas fontes:
- As 5 dores mais recorrentes (em linguagem do cliente, não do especialista)
- Os 3 desejos mais articulados
- As crenças limitantes mais comuns
- O vocabulário que o mercado usa (palavras exatas — ouro para copy)

### 2. ammunition.md
Biblioteca de frases reais de clientes/mercado:
- Frases de dor (para usar como gancho de conteúdo)
- Frases de desejo (para usar na promessa da oferta)
- Frases de objeção (para alimentar o sales-engine)
- Frases de transformação (depoimentos ou indicadores de sucesso)
Cada frase com a fonte de origem (anônima se necessário).

### 3. gaps-concorrente.md
O que o mercado critica ou sente falta nos concorrentes:
- Reclamação recorrente sobre [concorrente/categoria]
- Como o negócio atual pode se posicionar como o oposto
- Oportunidade de diferenciação identificada

### 4. ideias-conteudo.md
10 a 20 ideias de conteúdo nascidas das dores e linguagem reais do mercado. Para cada uma:
- Gancho (extraído de frase real)
- Formato recomendado (carrossel, reels, artigo)
- Por que vai performar (qual dor toca)

### 5. ideias-oferta.md
Ajustes de produto/serviço sugeridos com base no feedback:
- O que o mercado quer que não existe ainda
- O que existe mas poderia ser melhorado
- Uma nova oferta potencial (nome + promessa + formato)

## Princípios

1. Nunca inventar frases. Só usar o que foi dito literalmente pelo mercado.
2. Anonimizar fontes sensíveis sempre.
3. Atualizar a pesquisa pelo menos 1x por mês para o sistema não ficar desatualizado.
4. As frases de dor do `ammunition.md` devem alimentar diretamente o `messaging-engine`.

## Resumo Final para o Usuário

```
Research Engine concluído — [MÊS/ANO]

[N] fontes analisadas
[N] frases extraídas para ammunition
[N] ideias de conteúdo geradas

Arquivos criados em dados/research/[mes-ano]/:
✓ insights-mercado.md
✓ ammunition.md
✓ gaps-concorrente.md
✓ ideias-conteudo.md
✓ ideias-oferta.md

Próximo passo: usar ammunition.md como entrada do /messaging-engine ou /content-os.
```
