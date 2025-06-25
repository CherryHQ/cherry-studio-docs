# Leaderboard LLM Arena (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado automaticamente.

> **Data de atualização dos dados**: 2025-06-25 11:42:53 UTC / 2025-06-25 19:42:53 CST (Horário de Beijing)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar seus detalhes ou página de teste.
{% endhint %}

## Leaderboard

| Rank (UB) | Rank (StyleCtrl) | Nome do Modelo                                                                                                                         | Pontuação | Intervalo de Confiança | Votos     | Fornecedor                   | Licença                     | Data de Conhecimento |
|:----------|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------|:----------|:-----------------------|:----------|:-----------------------------|:----------------------------|:---------------------|
| 1         | 1                | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                      | 1477      | +5/-5                  | 12,327    | Google                       | Proprietária             | Dados não disponíveis     |
| 2         | 2                | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446      | +4/-6                  | 14,040    | Google                       | Proprietária             | Dados não disponíveis     |
| 3         | 3                | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                           | 1428      | +5/-3                  | 22,488    | OpenAI                       | Proprietária             | Dados não disponíveis     |
| ...       | ...              | ...                                                                                                                                   | ...       | ...                    | ...       | ...                          | ...                         | ...                  |

## Explicação

- **Rank (UB)**: Classificação calculada com base no modelo Bradley-Terry. Esta classificação reflete o desempenho global do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender a competitividade potencial do modelo.
- **Rank (StyleCtrl)**: Classificação após controle de estilo de conversa. Esta classificação visa reduzir o viés de preferência causado pelo estilo de resposta do modelo (por exemplo, verbosidade, concisão), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do modelo de linguagem grande (LLM). Esta coluna contém links relacionados aos modelos; clique para acessar.
- **Pontuação**: Pontuação Elo obtida pelo modelo na arena por meio de votos dos usuários. O Elo é um sistema de classificação relativa; quanto maior a pontuação, melhor o desempenho do modelo. Esta pontuação é dinâmica, refletindo a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo do modelo (por exemplo: `+6/-6`). Quanto menor o intervalo, mais estável e confiável é a pontuação; inversamente, um intervalo maior pode indicar dados insuficientes ou desempenho volátil do modelo. Fornece uma avaliação quantificada da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Geralmente, mais votos indicam maior confiabilidade estatística da pontuação.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo: Proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Data de Conhecimento**: Data de corte dos dados de treinamento do modelo. **Dados não disponíveis** indica que as informações não foram fornecidas ou são desconhecidas.

## Fonte de Dados e Frequência de Atualização

Os dados deste leaderboard são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado automaticamente diariamente pelo GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseados em votos de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem da fonte upstream e das atualizações/processamento do projeto `fboulnois/llm-leaderboard-csv`. Diferentes modelos podem ter licenças distintas; ao usar, consulte sempre as instruções oficiais do fornecedor do modelo.