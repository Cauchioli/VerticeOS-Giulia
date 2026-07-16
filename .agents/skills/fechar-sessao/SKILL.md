---
name: fechar-sessao
description: >
  Encerra a sessão de trabalho corretamente: atualiza os arquivos de memória com
  o que mudou na sessão, faz git commit do vault Obsidian e roda a indexação
  incremental do RAG para que tudo fique disponível na próxima sessão.
  Use quando o usuário disser "fechar sessão", "encerrar", "salvar tudo",
  "/fechar-sessao" ou ao fim de uma sessão longa de trabalho.
---

# /fechar-sessao — Encerramento de Sessão

Fecha o ciclo da sessão. Garante que nada se perde e que a próxima sessão começa sabendo o que aconteceu.

---

## Etapa 1 — Digest da Sessão

Gerar um resumo interno da sessão (não mostrar ao usuário a menos que peça):

```
O que foi feito: [lista das ações principais]
Decisões tomadas: [mudanças de estratégia, oferta, posicionamento]
Arquivos criados/modificados: [lista]
O que ficou pendente: [tarefas abertas]
```

---

## Etapa 2 — Atualizar Memória

Verificar se alguma dessas condições ocorreu na sessão:

- **Mudança de estratégia ou foco** → atualizar `_memoria/estrategia.md`
- **Correção de tom ou estilo** → atualizar `_memoria/preferencias.md`
- **Novo serviço, preço ou oferta** → atualizar `_memoria/empresa.md`
- **Nova decisão de design** → atualizar `identidade/design-guide.md`

Só atualizar o que realmente mudou. Nunca sobrescrever informação correta com genérica.

---

## Etapa 2.5 — Captura de Aprendizado (Gotchas)

Perguntar ao usuário em 1 linha:
> "Houve alguma correção de estilo, tom ou fato nesta sessão que deve ser lembrada?"

- **Se sim:** Criar registro em `.agents/aprendizado/gotchas.md` com o padrão:
  ```
  ## GOTCHA-[N]
  - **Padrão problemático:** [o que foi feito de errado]
  - **Contexto:** [onde se aplica]
  - **Por que é um erro:** [a razão]
  - **Alternativa correta:** [o que fazer no lugar]
  - **Ocorrências:** 1
  - **Registrado em:** [data]
  - **Fonte:** [quem corrigiu]
  ```
- **Se não:** Pular silenciosamente.

---

## Etapa 3 — Criar Nota de Sessão no Obsidian (opcional)

Se o usuário quiser registrar a sessão no vault, criar nota em `90-historico/`:

```yaml
---
id: sessao-YYYY-MM-DD
tipo-no: sessao
tipo: procedimento
dominio: operacional
status: concluido
relaciona: []
fontes: []
---

# Sessão — [Data]

## O que foi feito
[digest resumido]

## Decisões
[decisões tomadas]

## Próximos passos
[o que ficou aberto]
```

---

## Etapa 4 — Git Commit do Vault

Ler `rag/rag_config.json` para obter o valor de `obsidian_vault_path`. Se o caminho existir e o vault tiver git configurado (`.git/` presente na pasta), rodar:

```bash
cd [obsidian_vault_path lido do rag_config.json]
git add .
git commit -m "Sessão [data]: [resumo de 1 linha]"
```

Se o `rag_config.json` não existir, o caminho for `./segundo-cerebro` (padrão relativo) ou o vault não tiver git, pular esta etapa silenciosamente e registrar no resumo: `vault sem git configurado — pulado`.

---

## Etapa 5 — Indexação Incremental do RAG

```bash
python rag/rag_acervo.py index
```

Apenas arquivos novos ou modificados são processados — é rápido nas próximas vezes.

---

## Etapa 6 — Confirmar ao Usuário

```
Sessão encerrada.

✓ Memória atualizada
✓ Vault commitado  [ou: vault sem git configurado — pulado]
✓ RAG indexado — [N] arquivos novos processados

Próxima sessão começa sabendo tudo que foi feito hoje.
```

---

## Regras

- Nunca inventar informações para preencher os arquivos de memória
- Se não houve mudanças relevantes, dizer isso claramente — não forçar atualização
- A indexação do RAG é sempre o último passo — garante que tudo criado na sessão já está disponível
