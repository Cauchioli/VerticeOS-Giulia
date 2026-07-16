# 03-SCHEMA — O Padrão de Metadados e Tags das Notas

Todas as notas criadas ou atualizadas no vault Obsidian do usuário devem seguir rigorosamente o padrão abaixo. Isso garante que o motor de RAG consiga indexar por categorias e que plugins como o Dataview consigam construir listas automáticas.

---

## 📄 Estrutura Padrão de Metadados (Frontmatter YAML)

Toda nota precisa começar com o bloco de cabeçalho YAML delimitado por `---`:

```yaml
---
id: nome-da-nota-em-kebab-case
tipo-no: frente | entidade | metodologia | manual | referencia | estado | sessao
tipo: caso | cliente | principio | procedimento | indice | template | aprendizado
dominio: comercial | marketing | juridico | operacional | pessoal | financeiro
status: ativo | encerrado | prospect | rascunho
relaciona:
  - "[[outro-id]]"
  - "[[outro-id-2]]"
fontes:
  - "[FONTE: link, e-mail, ou caminho do arquivo original]"
---
```

### Explicação dos Metadados:
* **id:** Nome único da nota, em minúsculas e sem acentos, com hifens separando palavras (ex: `playbook-marketing-ia`).
* **tipo-no:** Pasta/eixo em que a nota se enquadra (ex: `manual` se morar na pasta `40-manuais/`).
* **tipo:** Classificação funcional da nota.
* **dominio:** Área de negócio que a nota impacta.
* **relaciona:** Array de wikilinks em formato string para que o parser de RAG rastreie conexões no grafo.
* **fontes:** Rastreabilidade física de onde veio aquela informação.

---

## 🏷️ Vocabulário Fechado de Tags

Utilize apenas as tags padronizadas abaixo. Evite criar novas tags sem necessidade:

* `#tipo/ideia` — Insights, teses e conceitos em rascunho.
* `#tipo/decisao` — Decisões estratégicas tomadas em sessões de trabalho.
* `#tipo/aprendizado` — Sumarizações de livros, cursos ou análises de mercado.
* `#tipo/procedimento` — SOPs operacionais e scripts passo a passo.
* `#tipo/caso` — Notas sobre casos de clientes, benchmarks ou diagnósticos comerciais.
* `#status/ativo` — Conhecimento vivo ou projeto em execução ativa.
* `#status/concluido` — Projetos ou sessões concluídas e arquivadas.
* `#status/rascunho` — Notas que ainda precisam de grounding ou verificação de fontes.
* `#verificar` — Informações que dependem de checagem ou validação física do usuário.
