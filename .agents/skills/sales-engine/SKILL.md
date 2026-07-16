---
name: sales-engine
description: >
  Constrói o sistema completo de vendas: diagnóstico, roteiro de call, SPIN adaptado, respostas a
  objeções, cadência de follow-up, expansão e indicação. Lê automaticamente o contexto da oferta e
  avatar em _memoria/. Use quando o usuário disser "roteiro de vendas", "como fechar esse cliente",
  "script de call", "follow-up", "objeções", "sales engine", ou /sales-engine.
---

# /sales-engine — Sistema Completo de Vendas (Vértice OS)

Transforma o processo de vendas em um sistema replicável. Um funcionário novo ou o próprio dono deve conseguir fechar usando esse roteiro.

## Filosofia

Venda não é convencer. É ajudar a pessoa a tomar uma decisão que já está na cabeça dela. O Sales Engine estrutura as perguntas certas e os momentos certos — não um script decorado.

## Contexto Necessário (leitura automática)

Antes de gerar qualquer saída, ler obrigatoriamente:
- `_memoria/empresa.md` — produto, ticket, avatar, diferenciais
- `_memoria/estrategia.md` — oferta ativa
- `identidade/messaging/objecoes.md` — se existir
- `identidade/messaging/posicionamento.md` — se existir

Se `identidade/messaging/` não existir: prosseguir inferindo objeções típicas do nicho a partir de `empresa.md`.

## Entradas Opcionais

- `avatar` — perfil detalhado do comprador se não estiver em empresa.md
- `oferta` — produto/serviço específico se houver múltiplos
- `ticket` — valor do produto (muda o tom e a abordagem do roteiro)
- `objecoes-comuns` — objeções específicas que o dono já ouviu

## Saídas — Pasta `vendas/`

Criar a pasta `vendas/` se não existir.

### 1. diagnostico.md
Formulário de diagnóstico pré-call (para o lead preencher ou o vendedor aplicar no início da conversa). 8-12 perguntas que qualificam:
- Urgência do problema
- Capacidade financeira (indiretamente)
- Maturidade de decisão
- Fit com o produto

### 2. roteiro-call.md
Roteiro completo da reunião/call de vendas em 5 fases:
1. Abertura e rapport (2-3 min)
2. Diagnóstico (SPIN — 10-15 min)
3. Apresentação da solução (5-7 min)
4. Manejo de objeções (conforme surgem)
5. Fechamento e próximos passos (2-3 min)

Para cada fase: o que dizer, o que ouvir, o que NÃO fazer.

### 3. spin-adaptado.md
Banco de perguntas SPIN adaptado ao nicho do negócio:
- **S**ituação: perguntas para entender o contexto atual
- **P**roblema: perguntas que revelam a dor real
- **I**mplicação: perguntas que amplificam o custo da inação
- **N**ecessidade de solução: perguntas que fazem o cliente articular o valor da solução

Mínimo 5 perguntas por categoria.

### 4. objecoes-respostas.md
As 10 objeções mais comuns com:
- A objeção exata (como o cliente fala)
- O que está por baixo dela (medo real)
- O reframe (virada de perspectiva)
- A resposta pronta (máx 4 linhas, conversacional)
- A pergunta de retorno (para continuar o diálogo)

### 5. followup-cadencia.md
Cadência de follow-up para leads que não fecharam na call:
- D+1: [mensagem de consolidação]
- D+3: [mensagem de valor adicional]
- D+7: [mensagem de urgência suave]
- D+14: [mensagem de breakup]
Para cada mensagem: canal (WhatsApp/email), texto pronto, tom.

### 6. expansao-upsell.md
Roteiro para oferecer upgrade ou serviço adicional para cliente ativo:
- Quando oferecer (sinais de maturidade do cliente)
- Como introduzir sem parecer oportunista
- A oferta de expansão recomendada para cada produto

### 7. indicacao.md
Script de pedido de indicação no momento de maior satisfação do cliente:
- Quando pedir (milestone ou quick win)
- Como pedir (mensagem pronta, tom humano)
- Como facilitar (template de mensagem para o cliente encaminhar)

## Princípios

1. O roteiro é um guia, não um script. Frases devem soar naturais — não decoradas.
2. Nunca pressionar no fechamento. Criar urgência real baseada nas consequências da inação.
3. Para produtos de alto ticket: mais diagnóstico, menos apresentação.
4. Respeitar o Provimento 205/2021 da OAB se o nicho for jurídico — adaptar linguagem.

## Resumo Final para o Usuário

```
Sales Engine concluído.

Arquivos criados em vendas/:
✓ diagnostico.md
✓ roteiro-call.md
✓ spin-adaptado.md
✓ objecoes-respostas.md
✓ followup-cadencia.md
✓ expansao-upsell.md
✓ indicacao.md

Próximo passo: /client-success para estruturar a entrega após o fechamento.
```
