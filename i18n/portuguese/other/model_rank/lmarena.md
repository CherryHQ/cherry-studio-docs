# LLM Arena Leaderboard (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um ranking baseado em dados do Chatbot Arena (lmarena.ai), gerado automaticamente por meio de um processo automatizado.

> **Última atualização de dados**: 2025-08-16 11:40:33 UTC / 2025-08-16 19:40:33 CST (Horário de Beijing)

{% hint style="info" %}
Clique no **nome do modelo** no ranking para ir para sua página de detalhes ou teste.
{% endhint %}

## Classificação

| Rank(UB) | Rank(StyleCtrl) | Modelo                                                                                                                             | Pontuação | Intervalo de Confiança | Votos      | Fornecedor              | Licença                    | Data Limite de Conhecimento |
|:--------|:---------------|:---------------------------------------------------------------------------------------------------------------------------------|:----------|:----------------------|:----------|:-----------------------|:--------------------------|:----------------------------|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
|... (restante da tabela preservada com conteúdo original sem alteração)...|
| 266 | 264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Explicação

- **Rank(UB)**: Classificação calculada com base no modelo Bradley-Terry. Este ranking reflete o desempenho abrangente do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Rank(StyleCtrl)**: Classificação após controle de estilo de conversação. Este ranking visa reduzir o viés de preferência causado pelo estilo de resposta dos modelos (por exemplo, verbosidade, concisão), avaliando de forma mais pura as capacidades centrais do modelo.
- **Modelo**: Nome do modelo de linguagem grande (LLM). Esta coluna contém links incorporados para os modelos relevantes - clique para acessar.
- **Pontuação**: Pontuação Elo obtida pelo modelo através de votos dos usuários na arena. O Elo é um sistema de classificação relativa onde pontuações mais altas indicam melhor desempenho. Esta pontuação é dinâmica e reflete a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo do modelo (exemplo: `+6/-6`). Intervalos menores indicam pontuações mais estáveis e confiáveis, enquanto intervalos maiores podem sugerir dados insuficientes ou maior variação no desempenho. Fornece uma avaliação quantitativa da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística da pontuação.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo: proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Data Limite de Conhecimento**: Data de corte do conhecimento nos dados de treinamento do modelo. **Sem dados** indica que as informações não foram fornecidas ou são desconhecidas.

## Origem dos Dados e Frequência de Atualização

Os dados deste ranking são fornecidos e gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este ranking é atualizado automaticamente diariamente pelo GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados do ranking são dinâmicos e baseados nas votações de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem da fonte upstream e do processamento/atualização do projeto `fboulnois/llm-leaderboard-csv`. Diferentes modelos podem ter licenças distintas - consulte sempre as instruções oficiais dos fornecedores dos modelos.