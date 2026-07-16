---
name: messaging-engine
description: >
  Constrói toda a arquitetura de mensagem e identidade verbal de uma marca ou especialista.
  Lê o contexto já existente em _memoria/ e identidade/ e preenche automaticamente o manifesto,
  posicionamento, big ideas, vocabulário proprietário, analogias e objeções. Use quando o usuário
  disser "messaging", "cria minha mensagem", "quero meu posicionamento", "qual minha tese",
  "preciso de frases de autoridade", ou /messaging-engine.
---

# /messaging-engine — Arquitetura de Mensagem e Identidade Verbal

Constrói a camada de messaging da marca — o conjunto de ideias, vocabulário e narrativas que dão consistência a todo conteúdo, oferta e comunicação de vendas. Sem isso, carrosseis, propostas e emails falam línguas diferentes.

## Filosofia

Messaging não é slogan. É o sistema de crenças da marca. Quando bem feito, qualquer pessoa da empresa (ou a própria IA) consegue criar conteúdo novo que soa 100% autêntico ao dono.

## Contexto Necessário (leitura automática)

Antes de gerar qualquer saída, ler obrigatoriamente:
- `_memoria/empresa.md` — quem é, o que faz, para quem
- `_memoria/preferencias.md` — tom de voz, ranços, estilo
- `_memoria/estrategia.md` — foco atual, oferta ativa
- `identidade/design-guide.md` — se existir

Se algum arquivo estiver em branco ou com placeholders, fazer as perguntas mínimas necessárias antes de prosseguir (nunca inventar dados de negócio).

## Grounding RAG (segundo cérebro local)

**Antes de gerar qualquer saída**, verificar se o RAG local está ativo e consultar o acervo:

```bash
# Verificar servidor
curl http://127.0.0.1:8799/health

# Consultas de grounding
python rag/rag.py "posicionamento tese de marca" -k 6
python rag/rag.py "avatar cliente ideal perfil dores" -k 6
python rag/rag.py "promessa resultado transformação oferta" -k 5
```

Se o servidor estiver offline: avisar o usuário e prosseguir apenas com os arquivos `_memoria/`.
Incorporar os trechos retornados nas saídas e citar a fonte (ex: `Fonte: OP-Tese-Precificacao.md`).

**Após concluir**, indexar os arquivos gerados:
```bash
curl "http://127.0.0.1:8799/index?path=C:/Users/WINDOWS11/Documents/VerticeOS/identidade/messaging"
```


## Entradas Opcionais (se o usuário fornecer, usar; senão extrair do contexto)

- `avatar` — quem é o cliente ideal (dores, desejos, identidade)
- `promessa` — o resultado principal que o produto entrega
- `tese` — a crença central que diferencia o negócio
- `mecanismo` — como o resultado é alcançado (o "sistema próprio")

## Saídas — Pasta `identidade/messaging/`

Criar a pasta `identidade/messaging/` se não existir. Gerar cada arquivo abaixo:

### 1. manifesto.md
Texto de 2-3 parágrafos. Não é sobre o produto — é sobre a visão de mundo do fundador. Deve provocar, polarizar levemente e criar identificação imediata com o avatar certo. Evitar clichês.

### 2. posicionamento.md
Uma única declaração de posição no formato:
`"[MARCA] é o único [CATEGORIA] que [PROMESSA ÚNICA] para [AVATAR] que [CONDIÇÃO/CRENÇA]."`
Mais 3-5 linhas de contexto explicando o que NÃO é a marca (para clareza por contraste).

### 3. big-ideas.md
3 a 5 ideias grandes e repetíveis. Cada uma com:
- Título da ideia (máx 7 palavras)
- Explicação em 2-3 linhas
- 1 exemplo prático do nicho

Essas ideias são os "pilares de conteúdo" de verdade — nascem da tese, não de categorias genéricas.

### 4. analogias.md
Biblioteca de 10 a 20 analogias e metáforas proprietárias da marca. Para cada uma:
- A analogia (ex: "A consulta é o diagnóstico, não o remédio")
- O conceito que ela explica
- Onde usar (conteúdo / venda / onboarding)

### 5. frases-autoridade.md
25 frases originais de autoridade. Curtas. Sem motivação vazia. Baseadas na tese e nas big ideas. Prontas para usar como abertura de post, frase de rodapé de proposta ou legenda do Instagram.

### 6. objecoes.md
As 10 objeções mais comuns do avatar (inferidas do nicho + dados de _memoria/). Para cada uma:
- A objeção exata (como o cliente fala)
- O reframe (a virada de perspectiva)
- A resposta pronta (1-3 linhas, sem parecer script)

### 7. narrativa-marca.md
O arco de origem em 3 atos:
1. O antes (a dor ou a limitação que existia antes do negócio)
2. O momento de virada (o insight ou o evento que mudou tudo)
3. O depois (a missão atual e o que está sendo construído)

### 8. vocabulario.md
Lista de 15 a 30 termos proprietários da marca. Para cada um:
- O termo (ex: "Colisão de Dados", "Vértice OS", "Triagem Estratégica")
- Definição interna (como a marca usa o termo)
- Como NÃO usar (para preservar o sentido)

## Princípios de Geração

1. Nunca usar palavras de guru motivacional: "jornada", "transformação", "sonhos", "legado", "propósito".
2. Toda frase deve poder ser dita em voz alta por um fundador sério em uma reunião de board.
3. As analogias devem ser específicas do nicho — nunca genéricas (ex: "futebol" ou "construção civil" como metáfora universal).
4. Se o negócio for jurídico, respeitar o Provimento 205/2021 da OAB implicitamente — sem termos mercantilistas explícitos.
5. Salvar todos os arquivos em `identidade/messaging/` com nomes exatos listados acima.

## Resumo Final para o Usuário

Após gerar todos os arquivos, mostrar:
```
Messaging Engine concluído.

Arquivos criados em identidade/messaging/:
✓ manifesto.md
✓ posicionamento.md
✓ big-ideas.md
✓ analogias.md
✓ frases-autoridade.md
✓ objecoes.md
✓ narrativa-marca.md
✓ vocabulario.md

Próximo passo: rodar /content-os para usar essa base no calendário de conteúdo.
```
