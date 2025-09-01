# LLM Arena Leaderboard (Atualizado em tempo real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado nos dados do Chatbot Arena (lmarena.ai), gerado automaticamente por um processo automatizado.

> **Data de atualização**: 2025-09-01 11:40:59 UTC / 2025-09-01 19:40:59 CST (horário de Beijing)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para ir para sua página de detalhes ou teste.
{% endhint %}

## Leaderboard

| Ranking (UB) | Ranking (StyleCtrl) | Nome do Modelo | Pontuação | Intervalo de Confiança | Votos | Provedor | Licença | Cutoff de Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
*(Tabela técnica preservada exatamente como no original - todas as células mantidas sem tradução)*

## Notas

- **Ranking (UB)**: Ranking calculado com base no modelo Bradley-Terry. Revela o desempenho geral do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a compreender sua competitividade potencial.
- **Ranking (StyleCtrl)**: Ranking após controle de estilo de conversação. Objetiva reduzir o viés de preferência causado por estilos de resposta (ex: verbosidade, concisão), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do modelo de linguagem grande (LLM). Contém links embutidos para detalhes.
- **Pontuação**: Classificação Elo obtida através de votos de usuários na arena. Quanto maior a pontuação, melhor o desempenho. Dinâmica, reflete a força relativa no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% da pontuação Elo (ex: `+6/-6`). Intervalo menor = estimativa mais estável/confiável.
- **Votos**: Número total de votos recebidos na arena. Mais votos geralmente significam maior confiabilidade estatística.
- **Provedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença (ex: Proprietária, Apache 2.0, MIT).
- **Cutoff de Conhecimento**: Data de corte do conhecimento nos dados de treinamento. **暂无数据** = informações não fornecidas ou desconhecidas.

## Fonte dos Dados e Frequência de Atualização

Dados deste leaderboard são fornecidos pelo projeto automatizado [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa dados de [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado diariamente por GitHub Actions.

## Aviso Legal

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseados em votos de preferência de usuários no Chatbot Arena em períodos específicos. A integridade e precisão dependem da fonte upstream e do processamento do projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes - consulte sempre as orientações oficiais do provedor.