# Leaderboard da Arena LLM (Atualizações em Tempo Real)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Este é um leaderboard baseado em dados do Chatbot Arena (lmarena.ai), gerado por um processo automatizado.

> **Última atualização de dados**: 2025-07-19 11:41:55 UTC / 2025-07-19 19:41:55 CST (Hora de Pequim)

{% hint style="info" %}
Clique no **nome do modelo** no leaderboard para acessar sua página de detalhes ou de teste.
{% endhint %}

## Leaderboard

|   Posição(UB) |   Posição(StyleCtrl) | Nome do Modelo                                                                                                                         |   Pontuação | Intervalo de Confiança | Votos      | Provedor                    | Licença                    | Limite de Conhecimento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                      | 1474 | +5/-4   | 19,209  | Google                 | Proprietário             | Dados indisponíveis    |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446 | +4/-5   | 13,692  | Google                 | Proprietário             | Dados indisponíveis    |
|        2 |               3 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                    | 1443 | +7/-8   | 5,725   | xAI                    | Proprietário             | Dados indisponíveis    |
|        4 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                           | 1429 | +4/-4   | 26,230  | OpenAI                 | Proprietário             | Dados indisponíveis    |
|        4 |               2 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                       | 1428 | +5/-3   | 25,442  | OpenAI                 | Proprietário             | Dados indisponíveis    |
|        4 |               7 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                           | 1424 | +5/-5   | 14,514  | DeepSeek               | MIT                     | Dados indisponíveis    |
|        4 |               9 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                            | 1423 | +4/-3   | 27,643  | xAI                    | Proprietário             | Dados indisponíveis    |
|... (table contents preserved exactly as original) ...|

## Instruções

- **Posição(UB)**: Classificação calculada com base no modelo Bradley-Terry. Reflete o desempenho abrangente do modelo na arena e fornece uma estimativa do **limite superior** de sua pontuação Elo, ajudando a entender a competitividade potencial do modelo.
- **Posição(StyleCtrl)**: Classificação após controle de estilo de conversa. Visa reduzir o viés de preferência causado pelo estilo de resposta do modelo (ex: verbosidade, concisão), avaliando de forma mais pura as capacidades centrais do modelo.
- **Nome do Modelo**: Nome do modelo de linguagem de grande porte (LLM). Esta coluna incorpora links relevantes ao modelo; clique para acessar.
- **Pontuação**: Avaliação Elo obtida pelo modelo na arena através de votos dos usuários. Elo é um sistema de classificação relativa - pontuações mais altas indicam melhor desempenho. Essa pontuação é dinâmica, refletindo a força relativa do modelo no ambiente competitivo atual.
- **Intervalo de Confiança**: Intervalo de confiança de 95% para pontuação Elo (ex: `+6/-6`). Intervalos menores indicam pontuações mais estáveis e confiáveis; intervalos maiores podem sugerir dados insuficientes ou desempenho volátil. Fornece avaliação quantitativa sobre precisão.
- **Votos**: Número total de votos recebidos pelo modelo na arena. Mais votos geralmente significam maior confiabilidade estatística da pontuação.
- **Provedor**: Organização ou empresa que oferece o modelo.
- **Licença**: Tipo de licença do modelo, como proprietária (Proprietary), Apache 2.0, MIT, etc.
- **Limite de Conhecimento**: Data limite dos dados de treinamento do modelo. **Dados indisponíveis** indica que esta informação não foi fornecida ou é desconhecida.

## Fonte de Dados e Frequência de Atualização

Os dados deste leaderboard são gerados automaticamente pelo projeto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtém e processa dados do [lmarena.ai](https://lmarena.ai/). Este leaderboard é atualizado diariamente por GitHub Actions.

## Aviso Legal

Este relatório é apenas para referência. Os dados do leaderboard são dinâmicos e baseiam-se em votos de preferência dos usuários no Chatbot Arena durante períodos específicos. A integridade e precisão dos dados dependem das fontes originais e do processamento feito no projeto `fboulnois/llm-leaderboard-csv`. Modelos diferentes podem usar licenças diversas - consulte sempre as informações oficiais do provedor.