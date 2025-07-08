# Leaderboard LLM Arena (Atualização em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado automaticamente através de um processo automatizado.

> **Data de Atualização**: 2025-07-08 11:43:23 UTC / 2025-07-08 19:43:23 CST (Horário de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar seus detalhes ou página de teste.
{% endhint %}

## Leaderboard

| Posição (UB) | Posição (StyleCtrl) | Nome do Modelo | Pontuação | Intervalo de Confiança | Votos | Fornecedor | Licença | Data de Corte do Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro) | 1477 | +5/-5 | 15,769 | Google | Proprietária | Dados indisponíveis |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06) | 1446 | +4/-5 | 13,997 | Google | Proprietária | Dados indisponíveis |
| 3 | 3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135) | 1429 | +4/-4 | 24,237 | OpenAI | Proprietária | Dados indisponíveis |
| 3 | 2 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/) | 1427 | +3/-4 | 21,965 | OpenAI | Proprietária | Dados indisponíveis |
| 3 | 6 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528) | 1425 | +4/-5 | 12,847 | DeepSeek | MIT | Dados indisponíveis |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 212 | 210 | [LLaMA-13B](https://arxiv.org/abs/2302.13971) | 815 | +14/-9 | 2,446 | Meta | Não comercial | 2023/2 |

## Explicações

- **Posição (UB)**: Classificação calculada com base no modelo Bradley-Terry. Reflete o desempenho abrangente do modelo na arena e fornece uma estimativa do **limite superior** da pontuação Elo, ajudando a entender a competitividade potencial do modelo.
- **Posição (StyleCtrl)**: Classificação após controle de estilo de conversação. Busca reduzir o viés de preferência devido ao estilo de resposta do modelo (por exemplo, extenso ou conciso), avaliando mais puramente a capacidade central do modelo.
- **Nome do Modelo**: Nome do Modelo de Linguagem Grande (LLM). Esta coluna contém links incorporados para os modelos - clique para acessar.
- **Pontuação**: Pontuação Elo obtida pelo modelo através de votos dos usuários na arena. O Elo é um sistema de classificação relativa, onde pontuações mais altas indicam melhor desempenho. Esta pontuação é dinâmica e reflete a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para a pontuação Elo do modelo (por exemplo: `+6/-6`). Intervalos menores indicam pontuações mais estáveis e confiáveis; intervalos maiores podem sugerir dados insuficientes ou desempenho volátil. Fornece avaliação quantitativa da precisão da pontuação.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente significam maior confiabilidade estatística da pontuação.
- **Fornecedor**: Organização ou empresa que fornece o modelo.
- **Licença**: Tipo de licença do modelo, por exemplo proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Data de Corte do Conhecimento**: Data de corte dos dados de treinamento do modelo. **Dados indisponíveis** indica que as informações não foram fornecidas ou são desconhecidas.

## Origem dos Dados e Frequência de Atualização

Os dados deste leaderboard são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado automaticamente diariamente via GitHub Actions.

## Aviso Legal

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseados em votos de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem da fonte upstream e do processamento pelo projeto `fboulnois/llm-leaderboard-csv`. Diferentes modelos podem ter licenças distintas - sempre consulte as instruções oficiais do fornecedor do modelo.