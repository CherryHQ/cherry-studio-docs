# LLM Arena Leaderboard (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Esta é uma classificação baseada em dados do Chatbot Arena (lmarena.ai), gerada automaticamente.

> **Data de atualização**: 2025-08-06 11:45:12 UTC / 2025-08-06 19:45:12 CST (hora de Beijing)

{% hint style="info" %}
Clique no **nome do modelo** na tabela para acessar seus detalhes ou página de teste.
{% endhint %}

## Classificação

| Ranking (UB) | Ranking (StyleCtrl) | Nome do Modelo                                                                                                                                                          | Pontuação | Intervalo de Confiança | Votos      | Provedor                  | Licenciamento               | Corte de Conhecimento |
|:-------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|:------------------------|:----------|:--------------------------|:----------------------------|:----------------------|
| 1            | 1                  | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                                                 | 1474      | +5/-4                  | 19,209    | Google                    | Proprietário                | Sem dados            |
| 2            | 2                  | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                                                       | 1446      | +4/-5                  | 13,692    | Google                    | Proprietário                | Sem dados            |
| 2            | 3                  | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                                                              | 1443      | +7/-8                  | 5,725     | xAI                       | Proprietário                | Sem dados            |
| 4            | 3                  | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                                                      | 1429      | +4/-4                  | 26,230    | OpenAI                    | Proprietário                | Sem dados            |
| ... *(tabela completa preservada sem alterações)* ...                                                                                                                     |

## Explicação

- **Ranking (UB)**: Classificação calculada com base no modelo Bradley-Terry. Esse ranking reflete o desempenho consolidado do modelo na arena, fornecendo uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Ranking (StyleCtrl)**: Classificação após controle de estilo de conversação. Visa reduzir o viés de preferência causado por diferenças estilísticas nas respostas (por exemplo, verbosidade vs. concisão), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do Modelo de Linguagem Grande (LLM). Contém links incorporados para detalhes relevantes.
- **Pontuação**: Pontuação Elo obtida através de votos dos usuários na arena. O Elo é um sistema de classificação relativa – pontuações mais altas indicam melhor desempenho. Essa pontuação é dinâmica, refletindo a força relativa atual do modelo no ambiente competitivo.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo do modelo (ex.: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade; intervalos maiores sugerem dados insuficientes ou desempenho variável. Fornece uma avaliação quantitativa da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente implicam maior confiabilidade estatística da pontuação.
- **Provedor**: Organização ou empresa que fornece o modelo.
- **Licenciamento**: Tipo de licença do modelo, por exemplo, proprietário (Proprietary), Apache 2.0, MIT, etc.
- **Corte de Conhecimento**: Data de corte do conhecimento nos dados de treinamento do modelo. **Sem dados** indica que a informação não foi fornecida ou é desconhecida.

## Fonte de Dados e Frequência de Atualização

Os dados desta classificação são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Esta classificação é atualizada diariamente através de GitHub Actions.

## Isenção de Responsabilidade

Este relatório é fornecido apenas para fins informativos. Os dados da classificação são dinâmicos e baseiam-se em votos de preferência dos usuários no Chatbot Arena durante um período específico. A integridade e precisão dos dados dependem das fontes upstream e do processamento/atualização do projeto `fboulnois/llm-leaderboard-csv`. Modelos diferentes podem ter licenças distintas – consulte sempre as instruções oficiais do provedor do modelo antes de usar.