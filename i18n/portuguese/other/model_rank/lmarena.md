# Ranking LLM Arena (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um ranking baseado em dados do Chatbot Arena (lmarena.ai), gerado automaticamente por processo automatizado.

> **Atualização de dados**: 2025-07-05 11:40:47 UTC / 2025-07-05 19:40:47 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no ranking para acessar sua página de detalhes ou experimentação.
{% endhint %}

## Ranking

| Posição(UB) | Posição(StyleCtrl) | Nome do Modelo                                                                                                                                                       | Pontuação | Intervalo de Confiança | Votos      | Provedor                    | Licença                     | Data de Corte de Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                                 | 1473 | +5/-4   | 14,062  | Google                 | Proprietária              | Dados indisponíveis      |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                                     | 1446 | +4/-5   | 14,432  | Google                 | Proprietária              | Dados indisponíveis      |
| 3 | 2 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                                    | 1428 | +4/-3   | 23,599  | OpenAI                 | Proprietária              | Dados indisponíveis      |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 208 | 205 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                                                |  817 | +12/-15 | 2,446   | Meta                   | Não comercial             | 2023/2   |

## Explicação

- **Posição(UB)**: Classificação calculada com base no modelo Bradley-Terry. Esta classificação reflete o desempenho global do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender sua competitividade potencial.
- **Posição(StyleCtrl)**: Classificação após controle de estilo de diálogo. Visa reduzir vieses de preferência decorrentes do estilo de resposta do modelo (por exemplo, verbosidade, concisão), avaliando de forma mais pura sua capacidade principal.
- **Nome do Modelo**: Nome do modelo de linguagem grande (LLM). Esta coluna possui links incorporados para modelos; clique para acessar.
- **Pontuação**: Pontuação Elo obtida pelo modelo através de votos dos usuários na arena. O Elo é um sistema de classificação relativa onde pontuações mais altas indicam melhor desempenho. Esta pontuação é dinâmica e reflete a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo (exemplo: `+6/-6`). Intervalos menores indicam pontuações mais estáveis e confiáveis; intervalos maiores podem sugerir dados insuficientes ou maior variação no desempenho. Fornece uma avaliação quantitativa da precisão da pontuação.
- **Votos**: Número total de votos recebidos por esse modelo na arena. Mais votos geralmente indicam maior confiabilidade estatística da pontuação.
- **Provedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo, proprietária (Proprietária), Apache 2.0, MIT, etc.
- **Data de Corte de Conhecimento**: Data de corte dos dados de treinamento do modelo. **Dados indisponíveis** significa que a informação não foi fornecida ou é desconhecida.

## Origem dos Dados e Frequência de Atualização

Os dados deste ranking são gerados e fornecidos automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este ranking é atualizado diariamente pelo GitHub Actions.

## Isenção de Responsabilidade

Este relatório destina-se apenas para fins informativos. Os dados do ranking são dinâmicos e baseiam-se nas preferências de voto dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem das fontes de dados upstream e do processamento/atualização do projeto `fboulnois/llm-leaderboard-csv`. Modelos diferentes podem empregar licenças distintas; ao usar, consulte sempre as instruções oficiais do provedor do modelo.