# Leaderboard LLM Arena (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado por um processo automatizado.

> **Data de Atualização**: 2025-06-26 11:42:56 UTC / 2025-06-26 19:42:56 CST (Horário de Beijing)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar sua página de detalhes ou teste.
{% endhint %}

## Leaderboard

| Rank(UB) | Rank(StyleCtrl) | Nome do Modelo | Pontuação | Intervalo de Confiança | Votos | Fornecedor | Licença | Corte de Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro) | 1477 | +5/-5 | 12,327 | Google | Proprietária | Sem dados |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06) | 1446 | +4/-6 | 14,040 | Google | Proprietária | Sem dados |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 208 | 207 | [LLaMA-13B](https://arxiv.org/abs/2302.13971) | 817 | +11/-12 | 2,446 | Meta | Não comercial | 2023/2 |

## Notas Explicativas

- **Rank(UB)**: Classificação baseada no modelo Bradley-Terry. Reflete o desempenho global do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Rank(StyleCtrl)**: Classificação após controle de estilo de conversação. Visa reduzir o viés de preferência causado por estilos de resposta (ex: verbosidade, concisão), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do modelo de linguagem grande (LLM). Inclui links para detalhes/página de teste.
- **Pontuação**: Pontuação Elo obtida através de votos dos usuários na arena. Quanto maior a pontuação, melhor o desempenho do modelo. Valor dinâmico que reflete a força relativa no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo (ex: Proprietária, Apache 2.0, MIT).
- **Corte de Conhecimento**: Data de corte dos dados de treinamento. **Sem dados** indica informação não fornecida ou desconhecida.

## Fonte de Dados e Frequência de Atualização

Os dados deste leaderboard são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado diariamente via GitHub Actions.

## Isenção de Responsabilidade

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseados em votos de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem da fonte upstream e do processamento do projeto `fboulnois/llm-leaderboard-csv`. Diferentes modelos podem usar licenças distintas – consulte sempre as orientações oficiais dos provedores.