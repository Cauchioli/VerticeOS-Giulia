---
name: growth-engine
description: >
  Funciona como CEO virtual. Analisa as métricas atuais do negócio, identifica o gargalo principal
  e define as 3 alavancas de alto impacto para os próximos 90 dias. Lê automaticamente dados de
  _memoria/, analisar-dados e relatorio-ads. Use quando o usuário disser "onde investir energia",
  "qual o gargalo", "crescimento", "growth engine", "CEO virtual", "próximos passos do negócio",
  ou /growth-engine.
---

# /growth-engine — CEO Virtual de Crescimento (Vértice OS)

Diagnostica o estado atual do negócio e define a prioridade de crescimento. Não tenta fazer tudo — identifica o 1 gargalo que, resolvido, desbloqueia os outros.

## Filosofia

A maioria dos empresários trabalha no lugar errado. O Growth Engine aplica a lógica de restrições (Teoria das Restrições de Goldratt): encontrar o gargalo, atacá-lo com foco total, repetir.

## Contexto Necessário (leitura automática)

- `_memoria/empresa.md` — produto, ticket, modelo de receita
- `_memoria/estrategia.md` — metas e prioridades atuais
- `dados/` — se existir, ler arquivos de métricas
- `marketing/relatorios/` — se existir, ler últimos relatórios de ads
- `instagram_cache.json` — se existir, métricas de engajamento

Se dados insuficientes: fazer as perguntas-chave antes de diagnosticar (ver seção abaixo).

## Perguntas de Diagnóstico (fazer se dados não estiverem no sistema)

O Growth Engine deve perguntar ao usuário:
1. Qual foi a receita dos últimos 30 dias?
2. Quantos leads entraram? (WhatsApp, formulário, direto)
3. Quantas reuniões/calls aconteceram?
4. Quantas fecharam? (taxa de conversão)
5. Qual o ticket médio atual?
6. Quantos clientes ativos hoje?
7. Qual o LTV médio (quanto tempo o cliente fica)?
8. O que mais consome tempo hoje (operação, vendas, conteúdo)?

## Saídas — Pasta `dados/growth/[mes-ano]/`

### 1. diagnostico-gargalo.md
Análise do estado atual com:
- Funil atual (leads → reuniões → fechamentos → LTV)
- Onde está o maior vazamento
- Identificação do gargalo principal (UM único ponto de foco)
- Por que esse e não outro

### 2. alavancas-priorizadas.md
Análise das 6 alavancas possíveis com pontuação de impacto:
| Alavanca | Impacto Potencial | Esforço | Recomendação |
- Aumentar ticket médio
- Aumentar taxa de conversão
- Aumentar volume de leads
- Aumentar LTV / retenção
- Lançar novo produto
- Contratar / delegar

Concluir com: "Foque APENAS em [ALAVANCA X] nos próximos 90 dias."

### 3. plano-acao-90-dias.md
3 iniciativas de alto impacto com:
- A iniciativa
- Por que vai mover a alavanca escolhida
- Passos concretos (semana a semana)
- Métrica de sucesso (como saber se está funcionando)
- Prazo

### 4. hiring-plan.md
Análise de quando e quem contratar:
- O papel que mais libera o fundador hoje
- O perfil ideal para esse papel
- O que delegar antes de contratar (processo + treinamento)
- Quando contratar faz sentido (receita mínima sugerida)

### 5. decisao-produto.md
Framework de decisão de portfólio:
- Lançar novo produto? (critérios e timing)
- Escalar o atual? (o que está travando)
- Pivotar? (sinais de alerta que indicam pivô)
Concluir com uma recomendação clara.

## Princípios

1. Um gargalo por vez. Não distribuir energia — concentrá-la.
2. Métricas > opiniões. Se não tem número, estimar com o usuário antes de recomendar.
3. Contratar resolve problemas de operação — nunca de estratégia.
4. Novo produto só depois de escalar o atual ou em caso de sinal claro de saturação.

## Resumo Final para o Usuário

```
Growth Engine concluído — [MÊS/ANO]

Gargalo identificado: [DESCRIÇÃO EM 1 LINHA]
Alavanca recomendada: [ALAVANCA]

Arquivos criados em dados/growth/[mes-ano]/:
✓ diagnostico-gargalo.md
✓ alavancas-priorizadas.md
✓ plano-acao-90-dias.md
✓ hiring-plan.md
✓ decisao-produto.md

Revisitar em: 30 dias ou quando a métrica-chave mudar significativamente.
```
