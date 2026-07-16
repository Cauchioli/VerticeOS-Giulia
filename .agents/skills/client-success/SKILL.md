---
name: client-success
description: >
  Monta o sistema completo de entrega e sucesso do cliente: onboarding, milestones, quick wins,
  plano de 90 dias, NPS, expansão e geração de cases. Lê o contexto do produto e cliente no
  sistema. Use quando o usuário disser "onboarding", "plano de entrega", "success do cliente",
  "client success", "como entregar", "plano 90 dias", ou /client-success.
---

# /client-success — Sistema de Entrega e Sucesso do Cliente (Vértice OS)

Estrutura o que acontece depois que o cliente fecha. Retenção, expansão e cases nascem aqui.

## Filosofia

O cliente que tem resultado vira fã, vira case e indica 3 outros. O client success não é suporte — é a engenharia do resultado. Cada etapa é projetada para o cliente sentir que fez o melhor investimento da vida.

## Contexto Necessário (leitura automática)

- `_memoria/empresa.md` — produto vendido, resultado prometido, avatar
- `_memoria/estrategia.md` — prazo e prioridades atuais
- `vendas/` — se existir, ler contexto da oferta e promessa feita na venda

## Entradas (via conversa se não estiverem no contexto)

- `nome-cliente` — nome da empresa ou pessoa
- `produto-vendido` — qual produto/serviço foi contratado
- `objetivo-final` — o resultado que o cliente quer alcançar
- `prazo` — tempo contratado (ex: 3 meses, 6 meses)

## Saídas — Pasta `clientes/[nome-cliente]/success/`

Criar a estrutura de pastas se não existir.

### 1. onboarding.md
Checklist dos primeiros 7 dias com:
- Reunião de kickoff (pauta e objetivos)
- Documentos e acessos a coletar
- Primeiras entregas (o que o cliente vai ver logo)
- Comunicação inicial (tom, frequência, canal)
- O que NÃO fazer na primeira semana (erros comuns de onboarding)

### 2. plano-90-dias.md
Linha do tempo semana a semana com:
| Semana | Milestone | Entregável | Responsável | Status |
Estruturado em 3 fases:
- Mês 1: Diagnóstico e fundação
- Mês 2: Implementação e ajustes
- Mês 3: Consolidação e expansão

### 3. quick-wins.md
3 a 5 vitórias rápidas que o cliente pode ter nas primeiras 2 semanas. Para cada uma:
- A ação concreta
- O resultado esperado (mensurável)
- Por que isso importa psicologicamente (momentum)

### 4. pesquisa-nps.md
Formulário de NPS em 3 momentos:
- D+30 (primeira impressão)
- D+60 (progresso)
- D+90 (resultado)
Para cada momento: as 3-5 perguntas certas e como interpretar as respostas.

### 5. expansao-playbook.md
Guia de quando e como propor expansão:
- Sinais de que o cliente está pronto (comportamentos, comentários, resultados)
- A oferta de expansão recomendada
- Como apresentar sem parecer oportunista

### 6. template-case.md
Estrutura para transformar o resultado do cliente em case de vendas:
- Situação anterior (antes)
- O problema central (a dor)
- A solução aplicada (o mecanismo)
- Os resultados (em números sempre que possível)
- A frase de depoimento sugerida (para o cliente validar)

## Princípios

1. Quick wins são obrigatórios — cliente sem resultado rápido cancela rápido.
2. Nunca deixar o cliente 15 dias sem uma interação ou atualização.
3. O case deve ser criado com o cliente, não sobre o cliente.

## Resumo Final para o Usuário

```
Client Success Engine concluído para [NOME DO CLIENTE].

Arquivos criados em clientes/[nome]/success/:
✓ onboarding.md
✓ plano-90-dias.md
✓ quick-wins.md
✓ pesquisa-nps.md
✓ expansao-playbook.md
✓ template-case.md

Próximo passo: executar o onboarding e agendar kickoff.
```
