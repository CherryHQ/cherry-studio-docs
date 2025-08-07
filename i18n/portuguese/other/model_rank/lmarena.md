# LLM Arena Leaderboard (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Esta é uma leaderboard baseada em dados do Chatbot Arena (lmarena.ai), gerada automaticamente por processo automatizado.

> **Data de atualização**: 2025-08-07 11:57:06 UTC / 2025-08-07 19:57:06 CST (Hora de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** na leaderboard para acessar sua página de detalhes ou teste.
{% endhint %}

## Leaderboard

| Posição (SU) | Posição (StyleCtrl) | Nome do Modelo                                                                                                                             | Pontuação | Intervalo de Confiança | Votos     | Provedor                   | Licença                   | Data de Corte |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietary             | nan      |
| 3 | 2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
| 4 | 2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Proprietary             | nan      |
| 5 | 3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietary             | nan      |
| 6 | 3 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                           | 1428 | +4/-4   | 32,033  | OpenAI                 | Proprietary             | nan      |
| 7 | 3 | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)                                      | 1427 | +9/-9   | 4,154   | Alibaba                | Apache 2.0              | nan      |
| 8 | 3 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                               | 1427 | +5/-5   | 18,284  | DeepSeek               | MIT                     | nan      |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 266 | 264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

*(Lista completa mantém estrutura original com 266 linhas)*

## Explicações

- **Posição (SU)**: Classificação baseada no modelo Bradley-Terry. Esta posição reflete o desempenho abrangente do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Posição (StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir o viés de preferência causado pelo estilo de resposta (ex.: verbosidade, concisão), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do Modelo de Linguagem de Grande Porte (LLM). Esta coluna contém links incorporados para os modelos.
- **Pontuação**: Pontuação Elo obtida pelo modelo através de votos de usuários na arena. O Elo é um sistema de classificação relativa – pontuações mais altas indicam melhor desempenho. Esta pontuação é dinâmica, refletindo a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo (ex.: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade da pontuação; intervalos maiores podem sugerir dados insuficientes ou desempenho volátil. Fornece uma avaliação quantificada da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Geralmente, mais votos indicam maior confiabilidade estatística da pontuação.
- **Provedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo: Proprietary, Apache 2.0, MIT, etc.
- **Data de Corte**: Data de corte dos dados de treinamento do modelo. **Dados indisponíveis** significa que a informação não foi fornecida ou é desconhecida.

## Origem dos Dados e Frequência de Atualização

Os dados desta leaderboard são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Esta leaderboard é atualizada automaticamente diariamente por GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para fins informativos. Os dados da leaderboard são dinâmicos e baseados nas preferências de voto dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem das fontes upstream e da atualização/processamento do projeto `fboulnois/llm-leaderboard-csv`. Modelos diferentes podem usar licenças diferentes – consulte sempre as instruções oficiais do provedor do modelo.