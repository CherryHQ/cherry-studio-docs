
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Leaderboard da Arena LLM (Atualização em Tempo Real)

Este é um leaderboard gerado automaticamente com base nos dados do Chatbot Arena (lmarena.ai).

> **Atualização dos dados**: 2025-06-22 11:41:35 UTC / 2025-06-22 19:41:35 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar sua página de detalhes ou experimentação.
{% endhint %}

## Leaderboard

| Classificação(UB) | Classificação(StyleCtrl) | Nome do Modelo                                                                                                                                       | Pontuação | Intervalo de Confiança | Votos      | Provedor                    | Licença                    | Data de Corte de Conhecimento |
|:-------------------|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:----------|:-----------------------|:----------|:---------------------------|:---------------------------|:------------------------------|
| 1                  | 1                         | [Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)                                  | 1480      | +6/-6                  | 8,825     | Google                     | Proprietary                | Dados não disponíveis         |
| 2                  | 2                         | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                                  | 1446      | +5/-5                  | 13,025    | Google                     | Proprietary                | Dados não disponíveis         |
| 3                  | 2                         | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                                               | 1427      | +4/-4                  | 16,019    | OpenAI                     | Proprietary                | Dados não disponíveis         |
| ...                | ...                       | ...                                                                                                                                                 | ...       | ...                    | ...       | ...                        | ...                        | ...                           |

## Explicação

- **Classificação(UB)**: Classificação calculada com base no modelo Bradley-Terry. Reflete o desempenho geral do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Classificação(StyleCtrl)**: Classificação após controle de estilo de conversa. Busca reduzir vieses de preferência decorrentes de diferenças de estilo de resposta (ex: verbosidade, concisão), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do Modelo de Linguagem de Grande Porte (LLM). Esta coluna contém links clicáveis para os modelos.
- **Pontuação**: Pontuação Elo obtida pelo modelo através de votos dos usuários na arena. O Elo é um sistema de classificação relativa onde pontuações mais altas indicam melhor desempenho. Esta pontuação é dinâmica, refletindo a força relativa atual do modelo no ambiente competitivo.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo do modelo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade da pontuação, enquanto intervalos maiores sugerem dados insuficientes ou desempenho volátil.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística da pontuação.
- **Provedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo (ex: Proprietary, Apache 2.0, MIT).
- **Data de Corte de Conhecimento**: Data limite dos dados de treinamento do modelo. **Dados não disponíveis** indica informação não fornecida ou desconhecida.

## Fonte de Dados e Frequência de Atualização

Os dados deste leaderboard são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado diariamente via GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para fins informativos. Os dados do leaderboard são dinâmicos e baseados nas preferências de votação dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem das fontes originais e do processamento pelo projeto `fboulnois/llm-leaderboard-csv`. Modelos diferentes podem ter licenças distintas - consulte sempre as orientações oficiais do provedor do modelo.