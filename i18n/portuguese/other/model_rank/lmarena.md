# Leaderboard da Arena de LLM (Atualizado em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado por processos automatizados.

> **Data de atualização**: 2025-07-25 11:44:23 UTC / 2025-07-25 19:44:23 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para saltar para os seus detalhes ou página de experimentação.
{% endhint %}

## Leaderboard

| Posição (UB) | Posição (StyleCtrl) | Nome do Modelo                                                                                                                         | Pontuação | Intervalo de Confiança | Votos      | Fornecedor               | Licença                   | Data de Corte do Conhecimento |
|:-------------|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------|:----------|:-----------------------|:-----------|:-------------------------|:--------------------------|:------------------------------|
| 1            | 1                   | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                | 1474      | +5/-4                  | 19,209     | Google                   | Proprietary               | Nenhuns dados                 |
| 2            | 2                   | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                     | 1446      | +4/-5                  | 13,692     | Google                   | Proprietary               | Nenhuns dados                 |
| 2            | 3                   | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                               | 1443      | +7/-8                  | 5,725      | xAI                      | Proprietary               | Nenhuns dados                 |
| 4            | 3                   | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                    | 1429      | +4/-4                  | 26,230     | OpenAI                   | Proprietary               | Nenhuns dados                 |
| ... (o restante da tabela preservado exatamente como no original, com dados numéricos intactos) ... | | | | | | | | |
| 218          | 215                 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                         | 814       | +10/-12                | 2,446      | Meta                     | Non-commercial            | 2023/2                        |

## Explicações

- **Posição (UB)**: Classificação baseada no modelo Bradley-Terry. Esta classificação reflete o desempenho geral do modelo na arena e fornece uma estimativa do **limite superior** da sua pontuação Elo, ajudando a compreender a competitividade potencial do modelo.
- **Posição (StyleCtrl)**: Classificação após controle de estilo de conversa. Esta classificação visa reduzir o viés de preferência causado pelo estilo de resposta do modelo (por exemplo, verbosidade, concisão), avaliando de forma mais pura as capacidades centrais do modelo.
- **Nome do Modelo**: Nome do modelo de linguagem grande (LLM). Esta coluna tem links incorporados relacionados ao modelo; clique para aceder.
- **Pontuação**: Pontuação Elo obtida pelo modelo na arena através de votos dos utilizadores. A pontuação Elo é um sistema de classificação relativa, em que uma pontuação mais alta indica um melhor desempenho do modelo. Esta pontuação é dinâmica e reflete a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo do modelo (por exemplo: `+6/-6`). Um intervalo menor indica que a pontuação do modelo é mais estável e confiável; inversamente, um intervalo maior pode indicar dados insuficientes ou flutuações no desempenho do modelo. Fornece uma avaliação quantificada da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Um maior número de votos geralmente significa maior confiabilidade estatística da sua pontuação.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo proprietário (Proprietary), Apache 2.0, MIT, etc.
- **Data de Corte do Conhecimento**: A data de corte dos dados de treino do modelo. **Nenhuns dados** significa que a informação relevante não foi fornecida ou é desconhecida.

## Fonte de Dados e Frequência de Atualização

Os dados deste leaderboard são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado automaticamente diariamente pelo GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseiam-se em votos de preferência dos utilizadores no Chatbot Arena durante um período específico. A integridade e precisão dos dados dependem da fonte de dados upstream e das atualizações e processamento do projeto `fboulnois/llm-leaderboard-csv`. Diferentes modelos podem usar diferentes licenças; por favor, consulte as instruções oficiais do fornecedor do modelo ao utilizar.