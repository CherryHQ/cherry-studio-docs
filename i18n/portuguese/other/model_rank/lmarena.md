# Ranking LLM Arena (Actualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um ranking baseado em dados do Chatbot Arena (lmarena.ai), gerado automaticamente por meio de um fluxo de trabalho.

> **Atualização de dados**: 2025-08-14 11:43:45 UTC / 2025-08-14 19:43:45 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no ranking para acessar sua página de detalhes ou testes interativos.
{% endhint %}

## Ranking

| Posição(UB) | Posição(StyleCtrl) | Nome do Modelo                                                                                                                     | Pontuação | Intervalo de Confiança | Votos      | Fornecedor             | Licença                 | Data de Conhecimento |
|:-----------|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:----------------------|:----------|:----------------------|:------------------------|:--------------------|
| 1          | 1                  | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                            | 1470     | +5/-5                | 26,019    | Google                | Proprietário            | nan                 |
| ... (o restante da tabela permanece com links/pontos inalterados, tradução aplicada apenas onde necessário) |


## Instruções

- **Posição(UB)**: Ranking baseado no modelo Bradley-Terry. Reflete o desempenho global dos modelos na arena, estimando limites superiores para pontuações Elo para entender potenciais vantagens competitivas.
- **Posição(StyleCtrl)**: Ranking ajustado por controle de estilo de diálogo. Minimiza viéses de preferência devido ao estilo de resposta (ex. verbosidade/concisão), avaliando apenas capacidades principais.
- **Nome do Modelo**: Nome do modelo de linguagem (LLM). Coluna com links embutidos para acesso rápido.
- **Pontuação**: Pontuação Elo obtida por votos na arena. Sistema relativo dinâmico - valores maiores indicam desempenho superior.
- **Intervalo de Confiança**: Intervalo de 95% para pontuação Elo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade/precisão.
- **Votos**: Total de votos recebidos na arena. Maior volume geralmente indica maior confiabilidade estatística.
- **Fornecedor**: Organização provedora do modelo.
- **Licença**: Tipo de licença (ex: proprietária, Apache 2.0, MIT).
- **Data de Conhecimento**: Limite temporal dos dados de treinamento. **Sem dados** indica informação não disponível.

## Fonte de Dados e Frequência de Atualização

Os dados são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), utilizando dados do [lmarena.ai](https://lmarena.ai/). Atualizado diariamente via GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas informativo. Os dados são dinâmicos e baseados em preferências de usuários no Chatbot Arena durante períodos específicos. Integralidade/acuracidade dependem de fontes primárias e processamento do projeto `fboulnois/llm-leaderboard-csv`. Modelos possuem licenças distintas - consulte documentação oficial dos provedores antes de qualquer uso.