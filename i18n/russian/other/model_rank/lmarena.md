# LLM Arena Leaderboard (Live Update)


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




This is a leaderboard based on data from Chatbot Arena (lmarena.ai), generated automatically.

> **Data Update Time**: 2025-08-26 11:41:43 UTC / 2025-08-26 19:41:43 CST (Beijing Time)

{% hint style="info" %}
Click on the **model name** in the leaderboard to jump to its detailed information or trial page.
{% endhint %}

## Leaderboard

| Ranking (UB) | Ranking (StyleCtrl) | Model Name | Score | Confidence Interval | Votes | Provider | License | Knowledge Cutoff Date |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro) | 1470 | +5/-5 | 26,019 | Google | Proprietary | nan |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06) | 1446 | +6/-6 | 13,715 | Google | Proprietary | nan |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5) | 1434 | +9/-9 | 4,112 | Z.ai | MIT | nan |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709) | 1434 | +6/-6 | 13,058 | xAI | Proprietary | nan |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135) | 1429 | +4/-4 | 30,777 | OpenAI | Proprietary | nan |
| ... (content preserved according to rules) | ... | ... | ... | ... | ... | ... | ... | ... |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971) | 840 | +16/-16 | 2,446 | Meta | Non-commercial | 2023/2 |

## Explanation

- **Ranking (UB)**: Ranking based on the Bradley-Terry model. This ranking reflects the model's overall performance in the arena and provides an **upper bound** estimate of its Elo score, helping to understand the model's potential competitiveness.
- **Ranking (StyleCtrl)**: Ranking after dialogue style control. This ranking aims to reduce preference bias caused by model response styles (e.g., verbose, concise) for a purer assessment of core capabilities.
- **Model Name**: Name of the Large Language Model (LLM). This column contains embedded links to related resources.
- **Score**: Elo score obtained through user votes in the arena. Elo is a relative ranking system where higher scores indicate better performance. This score is dynamic and reflects the model's relative strength in the current competitive environment.
- **Confidence Interval**: 95% confidence interval of the model's Elo score (e.g., `+6/-6`). A smaller interval indicates more stable and reliable scoring; larger intervals may indicate insufficient data or greater performance volatility. It provides a quantitative assessment of scoring accuracy.
- **Votes**: Total number of votes received by the model in the arena. More votes typically mean higher statistical reliability of the score.
- **Provider**: Organization or company providing the model.
- **License**: Type of license agreement, such as Proprietary, Apache 2.0, MIT, etc.
- **Knowledge Cutoff Date**: Knowledge cutoff date for the model's training data. **No data available** indicates missing or unknown information.

## Data Source and Update Frequency

This leaderboard data is automatically generated and provided by [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), which sources and processes data from [lmarena.ai](https://lmarena.ai/). The leaderboard is updated daily via GitHub Actions.

## Disclaimer

This report is for reference only. Leaderboard data is dynamic and based on user preference voting in Chatbot Arena during specific time periods. Data completeness and accuracy depend on upstream data sources and updates from the `fboulnois/llm-leaderboard-csv` project. Different models may have different licenses—please refer to official provider documentation when using them.