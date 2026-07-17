# Contexto e Diagnóstico Comercial — Dra. Giulia Bonfá

## 1. Perfil do Escritório
* **Profissional:** Dra. Giulia Bonfá (advogada com OAB ativa desde 2025).
* **Estrutura:** Advocacia solo, escritório físico próprio em Itapetininga/SP, operando sem funcionários.
* **Foco de Atuação:** Previdenciário (Salário Maternidade, Auxílio-Acidente, Aposentadorias) como carro-chefe. Atuação secundária em Trabalhista, Família (Guarda) e Cível.
* **Meta de Renda:** R$ 10.000,00 líquidos por mês.

---

## 2. Gargalos Operacionais Mapeados (Bugs)
* **Gargalo 1: Parceria Desequilibrada (Leandro - Criminal):** 
  80% dos clientes atuais vêm da indicação do Leandro. O repasse contratado é de **50% sobre o valor bruto** recebido. Leandro realiza apenas a indicação física, sem atuar no processo. Este repasse consome toda a margem e inviabiliza o lucro (em um caso de R$ 12.000, o prejuízo operacional da Giulia é de ~R$ 4.200 por caso comparado à tabela de indicação justa de 10-15% sobre honorários líquidos).
* **Gargalo 2: Controle de Prazos Manual:** 
  Prazos processuais são controlados de forma manual em um caderninho físico, gerando risco alto e perda de tempo de validação diária.
* **Gargalo 3: Análise de Processos Volumosos & Barreiras de Usabilidade:** 
  A leitura de processos administrativos longos do INSS consome a maior parte do dia de trabalho. A cliente utiliza NotebookLM para resumos de processos, mas encontrou dificuldades operacionais ao tentar "arrastar e soltar" arquivos de downloads na I.A., estourando o limite de requisições por falta de direcionamento correto da pasta de trabalho.
* **Gargalo 4: Assinaturas Remotas:** 
  Dificuldade em fechar contratos de honorários com clientes distantes ou de salário maternidade, exigindo assinatura física desnecessária (ZapSign recomendada).

---

## 3. Soluções e Engenharia Comercial (Método Vértice OS)
* **Revisão de Parceria:** Renegociar o acordo com o Leandro para o padrão de mercado (10-15% sobre honorários líquidos) com base nas simulações financeiras da Vértice.
* **Unificação de Fluxo Operacional:** Integração do RAG local com pastas dedicadas para evitar o uso descentralizado de ChatGPT e Jusbrasil separadamente.
* **IA na Análise Processual:** Uso de inteligência artificial de leitura semântica local (ou NotebookLM) para triagem de CNIS, laudos médicos e recursos administrativos longos em poucos minutos.
* **Controle Digital de Prazos:** Automação de leitura de publicações enviadas por e-mail pelo SAGE para centralizar o controle.
* **ZapSign:** Instalação e uso de ferramenta digital gratuita de assinatura para contratos remotos.

---

## 4. Rede de Indicações e Expansão
* **Dra. Lilian (Colega de Escritório):** Possui 50 anos, tem interesse em implementar processos de IA no seu dia a dia e desenvolver um site profissional + otimização da Bio do Instagram.
* **Dra. Ana:** Demonstrou insatisfação com o site atual desenvolvido pelo Jusfy ("site horrível") e tem interesse em contratar o Leo para a estruturação de um novo site institucional no padrão Vértice OS.

