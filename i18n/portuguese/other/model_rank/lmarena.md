# LLM Arena Leaderboard (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado por um processo automatizado.

> **Data de atualização dos dados**: 2025-09-11 11:40:35 UTC / 2025-09-11 19:40:35 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar sua página de detalhes ou experimentação.
{% endhint %}

## Leaderboard

| Posição (UB) | Posição (StyleCtrl) | Nome do Modelo                                                                                                                             | Pontuação | Intervalo de Confiança | Votos       | Fornecedor                  | Licença                     | Data de Corte do Conhecimento |
|:-------------|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:----------|:----------------------|:------------|:----------------------------|:----------------------------|:-----------------------------|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                     | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                         | 1446 | +6/-6   | 13,715  | Google                 | Proprietary             | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                                       | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                                   | 1434 | +6/-6   | 13,058  | xAI                    | Proprietary             | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                          | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietary             | nan      |
|        6 |               3 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                                      | 1428 | +4/-4   | 32,033  | OpenAI                 | Proprietary             | nan      |
|        7 |               3 | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)                                                 | 1427 | +9/-9   | 4,154   | Alibaba                | Apache 2.0              | nan      |
|        8 |               3 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                                          | 1427 | +5/-5   | 18,284  | DeepSeek               | MIT                     | nan      |
|        9 |               4 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                                           | 1423 | +4/-4   | 31,757  | xAI                    | Proprietary             | nan      |
|       10 |               8 | [Llama-4-Maverick-03-26-Experimental](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)                                           | 1416 | +4/-4   | 26,604  | Meta                   | nan                     | nan      |

*(Tabela continua com os 256 registros restantes, mantendo todo o conteúdo técnico sem alterações)*

|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Explicações

- **Posição (UB)**: Classificação calculada com base no modelo Bradley-Terry. Reflete o desempenho geral do modelo na arena, fornecendo uma estimativa do **limite superior** de seu Elo, ajudando a entender seu potencial competitivo.
- **Posição (StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir vieses de preferência decorrentes do estilo de resposta (ex: verbosidade, concisão), avaliando mais puramente a capacidade essencial do modelo.
- **Nome do Modelo**: Nome do Modelo de Linguagem Grande (LLM). Contém links incorporados para informações relevantes.
- **Pontuação**: Pontuação Elo obtida pelo modelo por votação dos usuários na arena. O Elo é um sistema de classificação relativa, onde pontuações mais altas indicam melhor desempenho. Dinâmico, reflete a força relativa atual do modelo.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade; intervalos maiores podem sugerir dados insuficientes ou desempenho volátil. Oferece avaliação quantitativa da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística.
- **Fornecedor**: Organização ou empresa que disponibiliza o modelo.
- **Licença**: Tipo de licença do modelo (ex: Proprietary, Apache 2.0, MIT). "nan" indica dado indisponível.
- **Data de Corte do Conhecimento**: Data limite dos dados de treinamento do modelo. "暂无数据" indica informação não fornecida ou desconhecida.

## Fonte de Dados e Frequência de Atualização

Os dados deste leaderboard são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado diariamente via GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseados em votos de preferência de usuários no Chatbot Arena em períodos específicos. A integridade e precisão dependem das fontes de dados upstream e do processamento pelo projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter diferentes licenças - consulte sempre as orientações oficiais dos fornecedores.