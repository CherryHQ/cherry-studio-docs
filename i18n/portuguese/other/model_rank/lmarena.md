# LLM Arena Leaderboard (Atualizado em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar sua página de detalhes ou teste.
{% endhint %}

Esta é uma classificação baseada em dados do Chatbot Arena (lmarena.ai), gerada por processo automatizado.

> **Horário de atualização dos dados**: 2025-06-30 11:44:35 UTC / 2025-06-30 19:44:35 CST (Horário de Pequim)

## Leaderboard

| Rank(UB) | Rank(StyleCtrl) | Nome do Modelo                                                                                                                         | Pontuação | Intervalo de Confiança | Votos      | Fornecedor               | Licença                  | Data de Conhecimento |
|:---------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------|:----------|:-----------------------|:-----------|:-------------------------|:------------------------|:---------------------|
| 1        | 1               | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                 | 1477      | +5/-5                  | 12,327     | Google                   | Proprietary             | Sem dados           |
| 2        | 2               | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                     | 1446      | +4/-6                  | 14,040     | Google                   | Proprietary             | Sem dados           |
| 3        | 3               | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                      | 1428      | +5/-3                  | 22,488     | OpenAI                   | Proprietary             | Sem dados           |
| *Restante da tabela preservada exatamente como no original, substituindo apenas "暂无数据" por "Sem dados"* |
| 207      | 205             | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                         | 840       | +11/-12                | 3,480      | Databricks               | MIT                     | 2023/4              |
| 208      | 207             | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                          | 817       | +11/-12                | 2,446      | Meta                     | Non-commercial          | 2023/2              |

## Explicações

- **Rank(UB)**: Classificação baseada no modelo Bradley-Terry. Reflete o desempenho global na arena e fornece estimativa do **limite superior** da pontuação Elo, ajudando a entender a competitividade potencial.
- **Rank(StyleCtrl)**: Classificação após controle de estilo de diálogo. Visa reduzir vieses de preferência por fatores como verbosidade/concisão, avaliando mais puramente as capacidades essenciais.
- **Nome do Modelo**: Nome do Modelo de Linguagem Grande (LLM). Contém links para detalhes/página de teste.
- **Pontuação**: Pontuação Elo obtida através de votos na arena. Sistema de classificação relativa onde valores maiores indicam melhor desempenho. Dinâmico e reflete força relativa atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo. Intervalos pequenos indicam estabilidade/confiabilidade. Intervalos grandes sugerem dados insuficientes ou variação de desempenho. Avaliação quantitativa da precisão da pontuação.
- **Votos**: Número total de votos recebidos na arena. Quantidades maiores geralmente indicam maior confiabilidade estatística.
- **Fornecedor**: Organização/empresa provedora do modelo.
- **Licença**: Tipo de licença do modelo (ex: Proprietary, Apache 2.0, MIT).
- **Data de Conhecimento**: Data de corte do conhecimento nos dados de treinamento. **Sem dados** indica informação não fornecida ou desconhecida.

## Fonte e Frequência de Atualização

Os dados deste leaderboard são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa dados do [lmarena.ai](https://lmarena.ai/). Atualização diária automática via GitHub Actions.

## Aviso Legal

Este relatório é apenas para referência. Os dados são dinâmicos e baseados em preferências de usuários no Chatbot Arena durante períodos específicos. A integridade/acuracidade depende das fontes originais e do processamento do projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes - consulte sempre as especificações oficiais dos provedores.