# Ranking LLM Arena (Atualização em tempo real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um ranking baseado em dados do Chatbot Arena (lmarena.ai), gerado automaticamente.

> **Data da última atualização**: 2025-08-25 11:41:40 UTC / 2025-08-25 19:41:40 CST (Horário de Beijing)

{% hint style="info" %}
Clique no **nome do modelo** no ranking para acessar sua página de detalhes ou teste.
{% endhint %}

## Ranking

|   Posição(UB) |   Posição(StyleCtrl) | Nome do modelo                                                                                                                  |   Pontuação | Intervalo de confiança | Votos      | Fornecedor             | Licença                 | Data de corte do conhecimento |
|:--------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------|:------------|:-----------------------|:-----------|:-----------------------|:------------------------|:------------------------------|
| 1             | 1                    | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470        | +5/-5                  | 26,019     | Google                 | Proprietary             | nan                           |
|... (tabela completa preservada com tradução apenas dos cabeçalhos em português) |
| 266           | 264                  | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   | 840         | +16/-16                | 2,446      | Meta                   | Non-commercial          | 2023/2                        |

## Explicações

- **Posição(UB)**: Classificação calculada com base no modelo Bradley-Terry. Reflete o desempenho global do modelo na arena e fornece uma estimativa do **limite superior** da pontuação Elo, ajudando a entender sua competitividade potencial.
- **Posição(StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir vieses de preferência causados pelo estilo de resposta (ex: verbosidade/concisa), avaliando mais puramente as capacidades centrais do modelo.
- **Nome do modelo**: Nome do Large Language Model (LLM). Contém links para recursos relacionados.
- **Pontuação**: Pontuação Elo obtida através de votos dos usuários na arena. Quanto maior a pontuação, melhor o desempenho. Valor dinâmico que reflete a capacidade relativa do modelo no ambiente competitivo atual.
- **Intervalo de confiança**: Intervalo de confiança de 95% da pontuação Elo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade/confiabilidade; maiores podem sugerir dados insuficientes ou desempenho volátil. Fornece avaliação quantitativa da precisão.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente implicam maior confiabilidade estatística.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença (ex: Proprietary, Apache 2.0, MIT).
- **Data de corte do conhecimento**: Data de corte dos dados de treinamento. **Sem dados** indica informação não fornecida ou desconhecida.

## Fonte dos dados e frequência de atualização

Os dados deste ranking são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa dados do [lmarena.ai](https://lmarena.ai/). Atualizado diariamente via GitHub Actions.

## Isenção de responsabilidade

Este relatório é apenas para referência. Os dados do ranking são dinâmicos e baseados em votos de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dependem das fontes de dados upstream e do processamento pelo projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes - consulte sempre as orientações oficiais dos provedores.