# Leaderboard da LLM Arena (Atualizado em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um ranking baseado em dados do Chatbot Arena (lmarena.ai), gerado por processos automatizados.

> **Data de atualização**: 2025-08-19 11:41:20 UTC / 2025-08-19 19:41:20 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **Nome do Modelo** na tabela para acessar detalhes ou uma página de demonstração.
{% endhint %}

## Leaderboard

| Posição (UB) | Posição (StyleCtrl) | Nome do Modelo                                                                                                                             |   Pontuação | Intervalo de Confiança | Votos      | Fornecedor                    | Licença                    | Data de Conhecimento   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietária             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietária             | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Proprietária             | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietária             | nan      |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
|      265 |             263 | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                  |  857 | +13/-13 | 3,480   | Databricks             | MIT                     | 2023/4   |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Não comercial          | 2023/2   |

*(Nota: Por questões de espaço, apenas as primeiras 5 e últimas 2 entradas estão representadas. A estrutura completa da tabela com 266 linhas é mantida no conteúdo original.)*

## Explicação

- **Posição (UB)**: Classificação calculada com base no modelo Bradley-Terry. Esta posição reflete o desempenho geral do modelo na arena e fornece uma estimativa do **limite superior** de sua avaliação Elo, ajudando a entender sua competitividade potencial.
- **Posição (StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir vieses de preferência decorrentes do estilo de resposta do modelo (ex: verbosidade, concisão), avaliando mais puramente sua capacidade central.
- **Nome do Modelo**: Nome do modelo de linguagem grande (LLM). Esta coluna contém links incorporados para acesso rápido.
- **Pontuação**: Avaliação Elo obtida através de votos dos usuários na arena. O Elo é um sistema de classificação relativa, onde pontuações mais altas indicam melhor desempenho. Esta pontuação é dinâmica, refletindo a força relativa atual do modelo.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade; intervalos maiores sugerem dados insuficientes ou alta volatilidade. Quantifica a precisão da avaliação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística.
- **Fornecedor**: Organização ou empresa que disponibiliza o modelo.
- **Licença**: Tipo de licenciamento do modelo, como proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Data de Conhecimento**: Data de corte dos dados de treinamento. **Nenhum dado** indica informação não fornecida ou desconhecida.

## Fonte de Dados e Frequência de Atualização

Estes dados são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa dados do [lmarena.ai](https://lmarena.ai/). O ranking é atualizado diariamente via GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados do ranking são dinâmicos e baseados em preferências de votação dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dependem das fontes de dados de origem e do processamento pelo projeto `fboulnois/llm-leaderboard-csv`. Modelos diferentes podem usar licenças distintas – consulte sempre as diretrizes oficiais dos provedores.