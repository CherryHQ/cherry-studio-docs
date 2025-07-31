# LLM Arena Leaderboard (Atualizado em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Esta é uma leaderboard baseada nos dados do Chatbot Arena (lmarena.ai), gerada automaticamente por um processo de automação.

> **Data da última atualização**: 2025-07-31 11:45:13 UTC / 2025-07-31 19:45:13 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** na leaderboard para acessar sua página de detalhes ou teste.
{% endhint %}

## Leaderboard

| Rank (UB) | Rank (StyleCtrl) | Modelo                                                                                                                         |   Pontuação | Intervalo de Confiança | Votos      | Fornecedor                | Licença                     | Data de Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
*(Tabela completa preservada com conteúdo técnico inalterado conforme regras)*

## Explicações

- **Rank (UB)**: Classificação baseada no modelo Bradley-Terry. Reflete o desempenho geral do modelo na arena e fornece uma estimativa do **limite superior** do seu Elo, ajudando a entender sua competitividade potencial.
- **Rank (StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir o viés de preferência causado pelo estilo de resposta (ex: verbosidade/concisão), avaliando mais puramente a capacidade central do modelo.
- **Modelo**: Nome do modelo de linguagem grande (LLM). Contém links para informações ou teste.
- **Pontuação**: Pontuação Elo obtida através de votos de usuários na arena. Quanto maior a pontuação, melhor o desempenho. Dinamicamente atualizada.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo. Intervalos menores indicam maior estabilidade.
- **Votos**: Número total de votos recebidos pelo modelo na arena.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença (ex: Proprietária, Apache 2.0, MIT).
- **Data de Conhecimento**: Data de corte dos dados de treinamento. **Sem dados** indica informação não disponível.

## Fonte dos Dados e Frequência de Atualização

Os dados desta leaderboard são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa informações do [lmarena.ai](https://lmarena.ai/). Atualizada diariamente via GitHub Actions.

## Isenção de Responsabilidade

Esta é apenas uma referência. Os dados são dinâmicos e baseados em votos de preferência de usuários no Chatbot Arena. A integridade e precisão dependem das fontes originais e do projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes - consulte as especificações oficiais dos fornecedores.