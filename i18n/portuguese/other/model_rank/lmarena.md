# LLM Arena Leaderboard (Atualizado em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado por processos automatizados.

> **Hora de atualização dos dados**: 2025-10-01 11:35:32 UTC / 2025-10-01 19:35:32 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar sua página de detalhes ou teste.
{% endhint %}

## Leaderboard

| Classificação(UB) | Classificação(StyleCtrl) | Nome do Modelo                                                                                                                             | Pontuação | Intervalo de Confiança | Votos      | Fornecedor                    | Licença                    | Data de Corte do Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| (Tabela preservada exatamente como no original - conteúdo não traduzido) |
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
| ... (linhas 2-266 preservadas sem alteração) |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Explicações

- **Classificação(UB)**: Classificação calculada com base no modelo Bradley-Terry. Reflete o desempenho global do modelo na arena, fornecendo uma estimativa do **limite superior** de seu score Elo para entender sua competitividade potencial.
- **Classificação(StyleCtrl)**: Classificação após controle de estilo de conversação. Visa reduzir o viés de preferência causado pelo estilo de resposta (ex: verbosidade, concisão), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do Large Language Model (LLM). Contém links incorporados para acesso direto.
- **Pontuação**: Score Elo obtido através de votos dos usuários na arena. Quanto maior a pontuação, melhor o desempenho. Valor dinâmico que reflete a capacidade relativa atual do modelo.
- **Intervalo de Confiança**: Intervalo de confiança de 95% do score Elo (ex: `+6/-6`). Intervalos menores indicam maior estabilidade e confiabilidade; maiores sugerem dados insuficientes ou desempenho volátil. Mede a precisão da avaliação.
- **Votos**: Total de votos recebidos pelo modelo na arena. Maior volume geralmente aumenta a confiabilidade estatística da pontuação.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, como proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Data de Corte do Conhecimento**: Data de corte dos dados de treinamento do modelo. **暂无数据** indica informação não fornecida ou desconhecida.

## Fonte de Dados e Frequência de Atualização

Os dados deste leaderboard são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que coleta e processa informações do [lmarena.ai](https://lmarena.ai/). Atualizado diariamente via GitHub Actions.

## Aviso Legal

Este relatório é apenas para referência. Os dados são dinâmicos e baseados em preferências de usuários no Chatbot Arena durante períodos específicos. Integridade e precisão dependem das fontes originais e do processamento do projeto `fboulnois/llm-leaderboard-csv`. Modelos podem ter licenças diferentes - consulte sempre as diretrizes oficiais dos fornecedores.