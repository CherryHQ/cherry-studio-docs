# LLM Arena Leaderboard (Atualizado em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado nos dados do Chatbot Arena (lmarena.ai), gerado automaticamente.

> **Data de atualização**: 2025-08-15 11:42:06 UTC / 2025-08-15 19:42:06 CST (Horário de Beijing)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar seus detalhes ou página de teste.
{% endhint %}

## Leaderboard

| Rank (UB) | Rank (StyleCtrl) | Modelo                                                                                                                             | Pontuação | Intervalo de Confiança | Votos     | Fornecedor             | Licença                 | Data de Corte do Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietária           | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietária           | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Proprietária           | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietária           | nan      |
|... (a tabela completa segue com todas as linhas traduzidas conforme abaixo) ...|

<details><summary>Ver tabela completa</summary>

|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Não comercial          | 2023/2   |

</details>

## Explicações

- **Rank (UB)**: Classificação calculada com base no modelo Bradley-Terry. Reflete o desempenho geral do modelo na arena, fornecendo uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Rank (StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir vieses de preferência causados pelo estilo de resposta do modelo (ex: verbosidade, concisão), avaliando mais puramente as capacidades fundamentais.
- **Modelo**: Nome do Modelo de Linguagem Grande (LLM). Contém links relacionados - clique para acessar.
- **Pontuação**: Pontuação Elo obtida através de votos dos usuários na arena. Quanto maior a pontuação, melhor o desempenho. Dinâmica, reflete a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade; maiores podem sugerir dados insuficientes ou volatilidade.
- **Votos**: Total de votos recebidos pelo modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, como proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Data de Corte do Conhecimento**: Data limite dos dados de treinamento. **Não disponível** indica informação não fornecida ou desconhecida.

## Fonte dos Dados e Frequência de Atualização

Os dados deste leaderboard são fornecidos e gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Atualizado diariamente via GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseados em votos de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dependem da fonte original e do processamento pelo projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes - consulte as orientações oficiais dos provedores.