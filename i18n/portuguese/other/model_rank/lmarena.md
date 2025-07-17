# Classificação LLM Arena (Atualizada em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




{% hint style="info" %}
Clique no **nome do modelo** no quadro de classificação para acessar os detalhes ou página experimental.
{% endhint %}

## Quadro de Classificação

| Classificação (UB) | Classificação (StyleCtrl) | Nome do Modelo                                                                                                               | Pontuação | Intervalo de Confiança | Votos      | Provedor                 | Licença                    | Atualização do Conhecimento |
|:------------------|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:----------|:----------------------|:-----------|:------------------------|:--------------------------|:---------------------------|
| 1                 | 1                         | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                      | 1474      | +4/-4                 | 18,297     | Google                  | Proprietária              | Nenhum dado disponível     |
| 2                 | 2                         | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446      | +5/-6                 | 13,694     | Google                  | Proprietária              | Nenhum dado disponível     |
| 2                 | 3                         | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                    | 1440      | +9/-9                 | 4,227      | xAI                     | Proprietária              | Nenhum dado disponível     |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Explicações

- **Classificação (UB)**: Classificação baseada no modelo Bradley-Terry. Esta classificação reflete o desempenho abrangente na arena e fornece uma estimativa do **limite superior** da pontuação Elo, ajudando a entender a competitividade potencial.
- **Classificação (StyleCtrl)**: Classificação após controle de estilo de conversação. Visa reduzir vieses de preferências relacionados ao estilo de resposta (ex: verbosidade, concisão) para avaliar melhor a capacidade central.
- **Nome do modelo**: Nome do LLM. Links incorporados levam a informações ou demonstrações.
- **Pontuação**: Classificação Elo obtida por votação na arena. Sistema relativo onde maiores valores indicam melhor desempenho (dinâmico).
- **Intervalo de confiança**: Intervalo de confiança de 95% para a pontuação Elo. Intervalos menores indicam maior estabilidade.
- **Votos**: Total de votos recebidos na arena (reliabilidade estatística).
- **Provedor**: Organização que fornece o modelo.
- **Licença**: Tipo de licença como proprietária, Apache 2.0 ou MIT.
- **Atualização do Conhecimento**: Expiração dos dados de treinamento. **Nenhum dado disponível** significa informação desconhecida.

## Fonte dos Dados e Frequência de Atualização

Os dados deste quadro são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta dados do [lmarena.ai](https://lmarena.ai/). Atualizado diariamente via GitHub Actions.

## Aviso Legal

Esta classificação é apenas informativa. Os dados são dinâmicos e baseados em votos de usuários no Chatbot Arena durante períodos específicos. Integridade e precisão dependem das fontes principais e do processamento do projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes - consulte documentação oficial dos provedores.