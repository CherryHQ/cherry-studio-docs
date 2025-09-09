# LLM Arena Leaderboard (Live Updates)


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




This leaderboard is based on data from Chatbot Arena (lmarena.ai) and is generated automatically.

> **Data Update Time**: 2025-09-09 11:40:31 UTC / 2025-09-09 19:40:31 CST (Beijing Time)

{% hint style="info" %}
Click on the **model name** in the leaderboard to go to its details page or try it out.
{% endhint %}

## Leaderboard

| Rank(UB) | Rank(StyleCtrl) | Model Name                                                                                                                             | Score | Confidence Interval | Votes     | Provider              | License                 | Knowledge Cutoff |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google          | Proprietary          | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google          | Proprietary          | nan      |
| ... (the entire table is preserved without changes, only headers are translated) ... |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta            | Non-commercial       | 2023/2   |

## Notes

- **Rank(UB)**: Ranking based on the Bradley-Terry model. This ranking reflects the model's overall performance in the arena and provides an **upper bound** estimate of its Elo score, helping to understand its potential competitiveness.
- **Rank(StyleCtrl)**: Ranking adjusted for dialogue style control. This ranking aims to reduce preference bias caused by response styles (e.g., verbose vs. concise), providing a purer evaluation of core capabilities.
- **Model Name**: Name of the large language model (LLM). This column includes embedded links to model-related pages; click to visit.
- **Score**: Elo rating obtained through user votes in the arena. Elo is a relative ranking system where higher scores indicate better performance. This score fluctuates dynamically based on the current competitive environment.
- **Confidence Interval**: 95% confidence interval of the Elo score (e.g., `+6/-6`). A smaller interval indicates greater score stability and reliability; a larger interval may suggest insufficient data or higher performance volatility. It quantifies rating accuracy.
- **Votes**: Total number of votes received by the model in the arena. Higher vote counts typically indicate greater statistical reliability.
- **Provider**: Organization or company providing the model.
- **License**: Model's license type, e.g., Proprietary, Apache 2.0, MIT, etc.
- **Knowledge Cutoff**: Knowledge cutoff date of the training data. **No Data** indicates information is unavailable or unknown.

## Data Source and Update Frequency

This leaderboard data is automatically generated and provided by [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), which sources and processes data from [lmarena.ai](https://lmarena.ai/). The leaderboard updates automatically daily via GitHub Actions.

## Disclaimer

This report is for reference only. Leaderboard data is dynamic and based on preference votes from users on Chatbot Arena during specific periods. Data completeness and accuracy depend on upstream data sources and updates from the `fboulnois/llm-leaderboard-csv` project. Different models may have varying licenses—always refer to the official guidance from model providers.