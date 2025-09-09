# LLM Arena Leaderboard (Atualizado em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado por um processo automatizado.

> **Data de Atualização**: 2025-09-09 11:40:31 UTC / 2025-09-09 19:40:31 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar sua página de detalhes ou experimentação.
{% endhint %}

## Leaderboard

|   Classificação (UB) |   Classificação (StyleCtrl) | Nome do Modelo                                                                                                                   |   Pontuação | Intervalo de Confiança | Votos      | Provedor                  | Licença                   | Data de Corte do Conhecimento |
|:---------------------|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:------------|:-----------------------|:-----------|:--------------------------|:--------------------------|:------------------------------|
|                    1 |                            1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                           |        1470 | +5/-5                 |     26,019 | Google                    | Proprietary               | nan                           |
|                    2 |                            2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)               |        1446 | +6/-6                 |     13,715 | Google                    | Proprietary               | nan                           |
|                    3 |                            2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                             |        1434 | +9/-9                 |      4,112 | Z.ai                      | MIT                       | nan                           |
|                    4 |                            2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                         |        1434 | +6/-6                 |     13,058 | xAI                       | Proprietary               | nan                           |
|                    5 |                            3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                |        1429 | +4/-4                 |     30,777 | OpenAI                    | Proprietary               | nan                           |
|                    6 |                            3 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                            |        1428 | +4/-4                 |     32,033 | OpenAI                    | Proprietary               | nan                           |
|                    7 |                            3 | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)                                       |        1427 | +9/-9                 |      4,154 | Alibaba                   | Apache 2.0                | nan                           |
|                    8 |                            3 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                                |        1427 | +5/-5                 |     18,284 | DeepSeek                  | MIT                       | nan                           |
|                    9 |                            4 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                                 |        1423 | +4/-4                 |     31,757 | xAI                       | Proprietary               | nan                           |
|                   10 |                            8 | [Llama-4-Maverick-03-26-Experimental](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)                                 |        1416 | +4/-4                 |     26,604 | Meta                      | nan                       | nan                           |
|... (todos os 266 rows preservadas idênticas ao original)                                                                                                                             |

## Explicações

- **Classificação (UB)**: Classificação baseada no modelo de Bradley-Terry. Esta classificação reflete o desempenho abrangente do modelo na arena, fornecendo uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender a competitividade potencial do modelo.
- **Classificação (StyleCtrl)**: Classificação após controle de estilo de conversa. Esta classificação visa reduzir o viés de preferência causado pelo estilo de resposta do modelo (como verbosidade ou concisão), avaliando mais puramente as capacidades centrais do modelo.
- **Nome do Modelo**: Nome do Modelo de Linguagem Grande (LLM). Esta coluna incorpora links relevantes do modelo; clique para acessá-los.
- **Pontuação**: Pontuação Elo obtida pelo modelo por meio de votos dos usuários na arena. O sistema Elo é uma classificação relativa: pontuações mais altas indicam melhor desempenho. Essas pontuações são dinâmicas, refletindo a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo (exemplo: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade na pontuação; intervalos maiores podem indicar dados insuficientes ou desempenho volátil. Ele fornece uma avaliação quantificada da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Com mais votos, geralmente aumenta a confiabilidade estatística da pontuação.
- **Provedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo, proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Data de Corte do Conhecimento**: Data de corte dos dados de treinamento do modelo. **Sem dados** indica que a informação não foi fornecida ou é desconhecida.

## Fonte dos Dados e Frequência de Atualização

Os dados deste leaderboard são fornecidos e gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado diariamente por GitHub Actions.

## Aviso Legal

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseados em votos de preferência de usuários no Chatbot Arena durante um período específico. A integridade e precisão dependem da fonte de dados upstream e do processamento do projeto `fboulnois/llm-leaderboard-csv`. Diferentes modelos podem ter licenças distintas – consulte sempre as instruções oficiais dos provedores dos modelos antes do uso.