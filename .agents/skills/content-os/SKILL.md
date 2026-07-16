---
name: content-os
description: >
  Sistema de conteúdo completo. Lê o contexto já existente (_memoria/, identidade/messaging/) e
  monta um calendário estratégico de 30 dias com pilares, sequência de posts, roteiros de Reels,
  stories, lives e emails — tudo conectado à oferta ativa do mês. Use quando o usuário disser
  "calendário de conteúdo", "planejamento do mês", "o que postar", "content os", "plano de posts",
  ou /content-os.
---

# /content-os — Sistema de Conteúdo Estratégico (Vértice OS)

Não é um gerador de posts. É um sistema que transforma o objetivo do mês em uma sequência estratégica de conteúdo onde cada peça alimenta a próxima e todas convergem para a oferta.

## Filosofia

Conteúdo sem estratégia é entretenimento. Content OS transforma o feed em uma máquina de qualificação e aquecimento de leads — cada post faz uma das 3 coisas: Atrair, Qualificar ou Converter.

## Contexto Necessário (leitura automática)

Antes de gerar qualquer saída, ler obrigatoriamente:
- `_memoria/empresa.md` — produto, avatar, diferenciais
- `_memoria/estrategia.md` — objetivo e oferta ativa do mês
- `_memoria/preferencias.md` — tom de voz e ranços
- `identidade/messaging/big-ideas.md` — se existir (pilares reais)
- `identidade/messaging/vocabulario.md` — se existir (termos proprietários)

Se `identidade/messaging/` não existir: avisar que rodar `/messaging-engine` primeiro vai melhorar muito a qualidade do calendário, mas prosseguir mesmo assim com o que tiver.

## Entradas Opcionais (se não estiverem em _memoria/)

- `objetivo-mes` — ex: "fechar 3 clientes DFY" ou "lançar produto de entrada"
- `oferta` — o produto/serviço principal a ser promovido no mês
- `avatar` — quem é o cliente ideal se não estiver em empresa.md

## Saídas — Pasta `marketing/content-os/[mes-ano]/`

### 1. pilares.md
3 a 5 pilares de conteúdo com:
- Nome do pilar
- Objetivo (atrair / qualificar / converter / reter)
- % de frequência no calendário
- Tipos de formato ideais para esse pilar

### 2. calendario-30-dias.md
Tabela completa com:
| Semana | Dia | Formato | Pilar | Tema/Gancho | CTA | Status |
Cada linha é um post planejado. O calendário deve ter sequência estratégica:
- Semana 1: Atração (posts de consciência do problema)
- Semana 2: Qualificação (posts de autoridade e mecanismo)
- Semana 3: Aquecimento (posts de prova e objeções)
- Semana 4: Conversão (oferta direta e CTA de fechamento)

### 3. sequencia-reels.md
5 a 8 roteiros completos de Reels (30-60 segundos). Para cada um:
- Gancho (primeiros 3 segundos)
- Corpo (desenvolvimento em 3-5 pontos visuais)
- CTA final
- Sugestão de legenda (2-3 linhas)

### 4. sequencia-stories.md
Roteiro semanal de stories (Seg a Sex). Para cada dia:
- Tema do story
- Formato sugerido (enquete, caixa de perguntas, antes/depois, bastidor)
- Texto de apoio ou pergunta

### 5. sequencia-emails.md
Cadência de emails do mês (1 por semana mínimo). Para cada email:
- Assunto (3 opções de A/B test)
- Estrutura (abertura, corpo, CTA)
- Momento de envio recomendado

### 6. ideias-lives.md
3 a 5 temas para lives com:
- Título
- Estrutura de 30 min (abertura, conteúdo, Q&A, pitch)
- Melhor dia/horário para o nicho

## Princípios

1. Cada post deve ter papel claro: não existe post "neutro" no sistema.
2. O calendário deve ter progressão — o post de sexta deve ser mais próximo da venda do que o de segunda.
3. Nunca sugerir conteúdo genérico de nicho (ex: "dicas de advocacia"). Sempre partir da tese e do vocabulário proprietário.
4. Salvar todos os arquivos em `marketing/content-os/[mes-ano]/` com os nomes exatos listados.

## Resumo Final para o Usuário

Após gerar todos os arquivos, mostrar:
```
Content OS do mês [MÊS/ANO] concluído.

Arquivos criados em marketing/content-os/[mes-ano]/:
✓ pilares.md
✓ calendario-30-dias.md
✓ sequencia-reels.md
✓ sequencia-stories.md
✓ sequencia-emails.md
✓ ideias-lives.md

Total de peças planejadas: [N]
Próximo passo: escolher qual peça executar primeiro com /carrossel ou /publicar-tema.
```
