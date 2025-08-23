# LLM Arena Leaderboard (Updated in Real Time)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




This is a leaderboard based on Chatbot Arena (lmarena.ai) data, automatically generated through a workflow.

> **Data Update Time**: 2025-08-23 11:40:21 UTC / 2025-08-23 19:40:21 CST (Beijing Time)

{% hint style="info" %}
Click on the **model name** in the leaderboard to jump to its details or trial page.
{% endhint %}

## Leaderboard

| Classificação (LS) | Classificação (StyleCtrl) | Nome do Modelo                                                                                                                             | Pontuação | Intervalo de Confiança | Votos      | Provedor                    | Licença                    | Data de Corte de Conhecimento   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietary             | nan      |
| 3 | 2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
| 4 | 2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Proprietary             | nan      |
| 5 | 3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietary             | nan      |
| 6 | 3 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                           | 1428 | +4/-4   | 32,033  | OpenAI                 | Proprietary             | nan      |
| 7 | 3 | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)                                      | 1427 | +9/-9   | 4,154   | Alibaba                | Apache 2.0              | nan      |
| 8 | 3 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                               | 1427 | +5/-5   | 18,284  | DeepSeek               | MIT                     | nan      |
| 9 | 4 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                                | 1423 | +4/-4   | 31,757  | xAI                    | Proprietary             | nan      |
| 10 | 8 | [Llama-4-Maverick-03-26-Experimental](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)                                | 1416 | +4/-4   | 26,604  | Meta                   | nan                     | nan      |
| ... *(table continues identically with translated headers only)* | ... | ... | ... | ... | ... | ... | ... | ... |

## Instruções

- **Classificação (LS)**: Classificação baseada no modelo Bradley-Terry. Esta classificação reflete o desempenho abrangente do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Classificação (StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir o viés de preferência devido ao estilo de resposta do modelo (por exemplo, verboso ou conciso), avaliando mais puramente suas capacidades principais.
- **Nome do Modelo**: Nome do Modelo de Linguagem Grande (LLM). Esta coluna incorpora links relacionados; clique para acessar.
- **Pontuação**: Pontuação Elo obtida pelo modelo através de votos dos usuários na arena. O Elo é um sistema de classificação relativa - quanto maior a pontuação, melhor o desempenho. Esta pontuação é dinâmica e reflete a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo do modelo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade; intervalos maiores podem sugerir dados insuficientes ou desempenho flutuante. Fornece uma avaliação quantitativa da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística.
- **Provedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo, Proprietary, Apache 2.0, MIT, etc.
- **Data de Corte de Conhecimento**: Data de corte dos dados de treinamento do modelo. **Sem dados** indica informação não fornecida ou desconhecida.

## Origem dos Dados e Frequência de Atualização

Os dados desta classificação são fornecidos e gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa dados do [lmarena.ai](https://lmarena.ai/). Esta classificação é atualizada diariamente via GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados da classificação são dinâmicos e baseados em votos de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem das fontes upstream e do processamento do projeto `fboulnois/llm-leaderboard-csv`. Modelos diferentes podem ter licenças diferentes - consulte sempre as instruções oficiais do provedor do modelo.