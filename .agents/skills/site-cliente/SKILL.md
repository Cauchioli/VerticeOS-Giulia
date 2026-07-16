---
name: site-cliente
description: Cria sites e landing pages premium para clientes da Vértice. Segue o fluxo briefing → wireframe → código final com as 20 filosofias de design do Huashu adaptadas ao padrão Vértice. Use quando o usuário pedir "criar site para [cliente]", "landing page para [nicho]", "página de vendas", "/site-cliente" ou descrever um projeto de site.
---

# Skill: /site-cliente
## Vértice — Protocolo de Criação de Sites Premium

> Você é um designer trabalhando com HTML. Não um programador.
> Seu produto é visual. Seu padrão é o de um portfólio de agência boutique.
> O usuário é o seu diretor criativo.

---

## Etapa 0 — Carregar Contexto

Antes de qualquer ação, ler:
- `_memoria/empresa.md` — quem é o Leo e o negócio dele
- `identidade/design-guide.md` — paleta, tipografia e padrões visuais da Vértice

---

## Etapa 1 — Briefing (5 perguntas em uma única mensagem)

```
1. Qual é o nome do projeto/cliente e o nicho de atuação?
2. Qual é o objetivo principal da página? (capturar lead, vender produto, institucional, portfólio...)
3. Existe alguma referência visual que o cliente admira? (site, marca, estilo)
4. Qual é a paleta de cores da marca do cliente, se existir? (ou sugiro uma)
5. Qual é o CTA principal da página? (ex: "Agendar consulta", "Comprar agora")
```

Aguardar respostas. Se o cliente não responder, avançar com assumptions documentados no código via comentários HTML `<!-- ASSUMPTION: ... -->`.

---

## Etapa 2 — Wireframe Textual

Gerar um wireframe em texto puro (sem código) descrevendo a estrutura de cada seção:

```
WIREFRAME — [Nome do Projeto]

[ HEADER ]
- Logo à esquerda | CTA button à direita

[ HERO ]
- Headline (máx. 8 palavras, UPPERCASE)
- Subheadline (1 frase, máx 15 palavras)
- CTA + prova social discreta

[ SEÇÃO X ]
- ...
```

Apresentar e perguntar: **"Quer ajustar alguma seção ou posso partir para o código?"**

---

## Etapa 3 — Código HTML Premium

### As 20 Filosofias de Design (Huashu + Vértice)

Ao gerar o código, as regras abaixo são **invioláveis**. São adaptadas das filosofias do Huashu Design para o contexto de sites de negócios brasileiros de alto padrão.

---

#### Filosofia 1 — Partir do Contexto Real, Nunca do Zero
Bom design nasce de contexto existente. Antes de criar qualquer coisa, vasculhar: há design system, logo, cores da marca, referências visuais que o cliente ama? Criar do zero sem referência alguma = garantia de output genérico.

#### Filosofia 2 — Junior Designer: Mostrar Antes de Finalizar
Nunca mergulhar e entregar de uma vez. Mostrar o wireframe antes, mostrar o layout em rascunho antes, mostrar o HTML com placeholders antes. **Iterar com validação** é mais rápido do que refazer tudo no final.

#### Filosofia 3 — Variações, Não "A Resposta Certa"
Sempre que possível, entregar 2-3 variações de seções chave (hero, CTA, tipografia) para o cliente escolher. Design não é uma resposta correta — é uma escolha entre alternativas qualificadas.

#### Filosofia 4 — Placeholder Honesto > Implementação Ruim
Sem ícone bom? Deixar um quadrado cinza com rótulo `[ícone: escudo]`. Sem imagem? Deixar `<!-- imagem do produto aqui -->`. **Um placeholder honesto é 10x melhor do que uma tentativa ruim** que vai precisar ser removida de qualquer forma.

#### Filosofia 5 — Sistema Primeiro, Não Preenchimento
Cada elemento deve justificar sua existência. Espaço em branco é uma decisão de composição, não ausência de conteúdo. Proibido:
- Stats decorativos inventados
- Ícones em todo título só para "encher"
- Gradientes em todos os fundos sem propósito

#### Filosofia 6 — Combater o "AI Slop" Ativamente

**O que é AI Slop**: o visual médio mais frequente no treinamento das IAs. Parece moderno mas não tem identidade de marca alguma.

**Proibido absolutamente:**
- Gradiente roxo/lavanda em fundo branco (o clichê padrão de SaaS)
- Emojis como ícones em contexto profissional
- Cartões com bordas arredondadas + accent lateral colorido (Tailwind-template style)
- SVG desenhado à mão tentando simular pessoas ou objetos reais
- Fundo escuro uniforme `#0D1117` + glow neon genérico
- Inter/Roboto/Arial como fonte de display principal

**Permitido (e incentivado):**
- Temas de IDE como inspiração de paleta (Dracula, Catppuccin, Tokyo Night)
- Estéticas culturais fortes: brutalismo editorial, japandi, art deco moderno, minimalismo suíço
- Combinações de tipografia inesperadas mas coerentes com o nicho
- Um background com textura, noise, ou gradiente radial com intenção

#### Filosofia 7 — Tipografia como Assinatura de Marca

**Proibido como fonte de display:** Arial, Inter, Roboto, System-UI genérico (são fontes de corpo, não de título)

**Combinações válidas por nicho:**
| Nicho | Título | Corpo |
|---|---|---|
| Direito / Consultoria Premium | Cormorant Garamond | Epilogue |
| Tech / SaaS / IA | Syne | DM Sans |
| Saúde / Bem-Estar | Playfair Display | Nunito |
| Varejo / Lifestyle | Fraunces | Outfit |
| Indústria / B2B | Bebas Neue | Lato |
| Arquitetura / Imóveis | Libre Baskerville | Jost |

Sempre carregar do Google Fonts. Usar `letter-spacing` ampliado em headlines uppercase. Peso 700-800 nos títulos.

#### Filosofia 8 — Cor com Intenção, Não Decoração

- Definir variáveis CSS antes de qualquer coisa: `--color-primary`, `--color-accent`, `--color-bg`, `--color-text`
- Uma cor dominante forte + 1-2 acentos nítidos > paleta pastosa com 8 tons equilibrados
- Usar `oklch()` quando for inventar uma cor — é mais previsível que hex puro
- A paleta deve poder ser descrita em 2 palavras: "preto-dourado", "verde-musgo + creme", "cinza-ardósia + coral"

#### Filosofia 9 — Fundo com Atmosfera, Não Cor Sólida

**Técnicas válidas:**
- Gradiente radial elíptico no topo (`ellipse 80% 50% at 50% -10%`) com opacidade entre 5-10%
- Grid de cruzinhas em SVG com opacidade 0.015
- Noise texture via `filter: url(#noise)` com SVG `feTurbulence`
- Formas geométricas grandes com baixíssima opacidade como elementos de fundo

#### Filosofia 10 — Uma Animação de Impacto, Não Mil Micro-animações

Priorizar **1 animação de entrada orquestrada** no carregamento com `animation-delay` escalonado (staggered reveal). Micro-interações cirúrgicas nos botões e cards. **Evitar:** animações em cada elemento sem hierarquia de atenção.

Usar `IntersectionObserver` para ativar animações ao rolar — nunca animar elementos que estão fora da viewport.

#### Filosofia 11 — Responsividade Mobile-First

- Estrutura base para mobile, desktop como exceção via `@media (min-width: 768px)`
- Nunca usar `px` fixo para font-size em corpo — usar `clamp()` para escalabilidade
- Testar mentalmente: "Como fica com 375px de largura?"

#### Filosofia 12 — Hierarquia Visual Clara

Cada página tem exatamente 1 elemento de máxima atenção (o H1 ou o CTA principal). Tudo o mais está hierarquicamente abaixo. A ordem de atenção deve ser:
1. Headline
2. Visual / widget de demonstração
3. CTA
4. Prova social / credenciais
5. Detalhes

#### Filosofia 13 — Prova Social Discreta mas Presente

Não exagerar: 1-2 números concretos ou depoimentos curtos. Nunca inventar. Se não há prova real, deixar placeholder honesto: `<!-- depoimento do cliente X aqui -->`.

#### Filosofia 14 — Cinco Perguntas Antes de Codar

Antes de escrever a primeira linha de CSS, responder internamente:
1. Qual é o papel narrativo desta página? (vender, informar, capturar lead, credenciar)
2. Quem está lendo e a que distância? (celular, desktop, projetor)
3. Qual é a temperatura visual? (fria/confiança, quente/energia, neutra/seriedade)
4. O conteúdo cabe na estrutura pensada? (fazer o teste mental do thumbnail)
5. Qual é o elemento visual único deste negócio que não apareceria em outro site?

#### Filosofia 15 — Velocidade de Carregamento é Design

- Tudo em arquivo único (`index.html`) com CSS no `<style>` e JS no `<script>` quando possível
- Imagens referenciadas por URL externa quando necessário, nunca base64 de arquivos grandes
- Sem frameworks CSS externos (Tailwind, Bootstrap) — vanilla CSS com variáveis é suficiente e mais rápido
- Carregar Google Fonts com `display=swap` para não bloquear renderização

#### Filosofia 16 — SEO é Parte do Design

Sempre incluir em todo HTML gerado:
- `<title>` descritivo com nome do negócio + proposta de valor
- `<meta name="description">` com 120-160 caracteres
- `lang="pt-BR"` no `<html>`
- Hierarquia correta de headings: 1 único `<h1>`, depois `<h2>`, `<h3>`
- IDs únicos em todos os elementos interativos (para rastreamento e acessibilidade)

#### Filosofia 17 — Densidade Certa para o Nicho

**Padrão para consultores, advogados, especialistas:**
- Alta qualidade visual, baixa densidade de informação por seção
- Espaço em branco como sinalizador de premium
- Máximo 3 pontos por seção

**Padrão para SaaS, tech, produtos digitais:**
- Pode ter mais densidade — mostrar o produto funcionando
- Cada seção com 3+ informações diferenciadas
- Dados e features explícitos

#### Filosofia 18 — Um Detalhe a 120%, o Resto a 80%

Não tentar fazer tudo perfeito. Escolher 1 elemento para ser o "detalhe memorável" da página:
- Uma animação de entrada no hero
- Um widget interativo
- Uma seção com tipografia editorial incomum
- Um efeito de glassmorphism bem aplicado

O resto pode ser sólido e limpo sem precisar ser extraordinário.

#### Filosofia 19 — Entrega Documentada

Ao finalizar o HTML, sempre:
1. Indicar onde salvar (`saidas/sites/[nome-cliente]/index.html`)
2. Listar as 3 principais decisões de design tomadas e o porquê
3. Marcar os placeholders que precisam de conteúdo real do cliente
4. Perguntar: "Quer ajustar paleta, tipografia ou alguma seção específica?"

#### Filosofia 20 — Nunca Inventar Fatos, Sempre Verificar

Se o cliente mencionar produto, empresa ou dados específicos que você não conhece com certeza:
- Não assumir — pedir confirmação
- Marcar dados inventados com `<!-- VERIFICAR: dado real aqui -->`
- Nunca criar estatísticas decorativas que possam ser interpretadas como reais

---

## Etapa 4 — Entrega

Após gerar o código:
1. Salvar em `saidas/sites/[nome-cliente]/index.html`
2. Listar as 3 decisões de design
3. Marcar placeholders pendentes
4. Abrir para iteração

---

## Quando NÃO usar esta skill
- Carrosséis de Instagram → `/carrossel`
- Propostas comerciais A4 → `/proposta-comercial`
- Artigos de blog → `/publicar-tema`
- Sistemas com backend, autenticação ou banco de dados → scope diferente, discutir separadamente
