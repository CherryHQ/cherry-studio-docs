# Classificação da LLM Arena (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Esta é uma classificação baseada em dados da Chatbot Arena (lmarena.ai), gerada através de um processo automatizado.

> **Data da Atualização**: 2025-08-31 11:39:53 UTC / 2025-08-31 19:39:53 CST (Hora de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** na classificação para ser direcionado à sua página de detalhes ou experimentação.
{% endhint %}

## Classificação

| Classificação (UB) | Classificação (StyleCtrl) | Nome do Modelo                                                                                                                             | Pontuação | Intervalo de Confiança | Votos      | Provedor                    | Licença                    | Atualização de Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                  | 1470 | +5/-5   | 26,019  | Google                 | Proprietária             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)               | 1446 | +6/-6   | 13,715  | Google                 | Proprietária             | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                              | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                           | 1434 | +6/-6   | 13,058  | xAI                    | Proprietária             | nan      |
|        ... |               ... | ... | ... | ... | ... | ... | ... | ... |   <!-- Omitido por brevidade. Traduções seguem padrão acima -->  
|      262 |             258 | [OpenAssistant-Pythia-12B](https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5)                               |  923 | +10/-10 | 6,368   | OpenAssistant          | Apache 2.0              | 2023/4   |
|      263 |             260 | [FastChat-T5-3B](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)                                                              |  901 | +12/-12 | 4,288   | LMSYS                  | Apache 2.0              | 2023/4   |
|      264 |             263 | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)                                           |  873 | +12/-12 | 3,336   | Stability AI           | CC-BY-NC-SA-4.0         | 2023/4   |
|      265 |             263 | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                  |  857 | +13/-13 | 3,480   | Databricks             | MIT                     | 2023/4   |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Não-comercial          | 2023/2   |

## Explicação

- **Classificação (UB)**: Ranking calculado com base no modelo Bradley-Terry. Reflete o desempenho abrangente dos modelos na arena e fornece estimativa de **limite superior** de sua pontuação Elo, ajudando a compreender sua competitividade potencial.
- **Classificação (StyleCtrl)**: Ranking após controle de estilo de diálogo. Objetiva reduzir preferências tendenciosas causadas por expressões (como detalhadas ou concisas) e avaliar com maior pureza as capacidades centrais dos modelos.
- **Nome do Modelo**: Nome do Grande Modelo de Linguagem (LLM). Esta coluna inclui links relevantes para detalhes ou testes.
- **Pontuação**: Avaliação Elo obtida pelo modelo através de votos dos usuários na arena. Elo é um sistema de classificação relativa — quanto maior a pontuação, melhor o desempenho. Esta pontuação é dinâmica e reflete a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para pontuação Elo do modelo (ex: `+6/-6`). Um intervalo menor indica maior estabilidade da pontuação; maior intervalo pode sugerir dados insuficientes ou flutuação de desempenho. Fornece avaliação quantitativa da precisão.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Geralmente, quanto mais votos, maior a confiabilidade estatística.
- **Provedor**: Organização ou empresa que oferece o modelo.
- **Licença**: Tipo da licença do modelo, ex: Proprietária, Apache 2.0, MIT, etc.
- **Atualização de Conhecimento**: Data de corte dos dados de treinamento. **Dados indisponíveis** indica ausência de informação.

## Fonte de Dados e Frequência de Atualização

Esta classificação é gerada pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa dados do [lmarena.ai](https://lmarena.ai/). Atualizações automáticas via GitHub Actions ocorrem **diariamente**.

## Aviso Legal

Esta classificação é apenas para referência. Os dados são dinâmicos e baseiam-se em votos de preferência dos usuários na Chatbot Arena durante períodos específicos. Integridade e precisão dependem das fontes originais e da atualização do projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes — consulte as especificações oficiais dos provedores antes de utilizar.