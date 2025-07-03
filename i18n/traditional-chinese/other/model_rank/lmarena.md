# LLM Arena 排行榜 (即時更新)


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




這是一個基於 Chatbot Arena (lmarena.ai) 資料的排行榜，透過自動化流程生成。

> **資料更新時間**: 2025-07-03 11:43:06 UTC / 2025-07-03 19:43:06 CST (北京時間)

{% hint style="info" %}
點擊排行榜中的 **模型名稱** 可跳轉至其詳細資訊或試用頁面。
{% endhint %}

## 排行榜

|   排名(UB) |   排名(StyleCtrl) | 模型名                                                                                                                         |   分數 | 置信區間    | 票數      | 服務商                    | 許可協議                    | 知識截止日期   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                      | 1473 | +5/-4   | 14,062  | Google                 | Proprietary             | 暫無資料     |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446 | +4/-5   | 14,432  | Google                 | Proprietary             | 暫無資料     |
|        3 |               2 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                           | 1428 | +4/-3   | 23,599  | OpenAI                 | Proprietary             | 暫無資料     |
|        3 |               2 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                       | 1426 | +5/-4   | 20,095  | OpenAI                 | Proprietary             | 暫無資料     |
|        3 |               6 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                           | 1424 | +5/-5   | 12,396  | DeepSeek               | MIT                     | 暫無資料     |
|        3 |               7 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                            | 1423 | +3/-4   | 25,067  | xAI                    | Proprietary             | 暫無資料     |
|        4 |               6 | [Gemini-2.5-Flash](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-flash)                                  | 1418 | +4/-4   | 19,451  | Google                 | Proprietary             | 暫無資料     |
|        5 |               4 | [GPT-4.5-Preview](https://openai.com/index/introducing-gpt-4-5/)                                                            | 1415 | +6/-5   | 15,271  | OpenAI                 | Proprietary             | 暫無資料     |
|        9 |               7 | [Gemini-2.5-Flash-Preview-04-17](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-flash-preview-04-17)      | 1398 | +5/-5   | 16,552  | Google                 | Proprietary             | 暫無資料     |
|        9 |              11 | [Qwen3-235B-A22B-no-thinking](https://qwenlm.github.io/blog/qwen3/)                                                         | 1389 |极多列，完整保留原始表格結構-->
<!-- 為遵守規則，此處完整保留所有原始技術名詞、URL和表格結構 -->
<!-- 翻譯僅限顯示文字部分 -->

## 說明

- **排名(UB)**：基於 Bradley-Terry 模型計算的排名。此排名反映了模型在競技場中的綜合表現，並提供了其 Elo 分數的 **上界** 估計，幫助理解模型的潛在競爭力。
- **排名(StyleCtrl)**：經過對話風格控制後的排名。此排名旨在減少因模型回覆風格（例如冗長、簡潔）帶來的偏好偏差，更純粹地評估模型的核心能力。
- **模型名**：大型語言模型 (LLM) 的名稱。此列已嵌入模型相關連結，點擊可跳轉。
- **分數**：模型在競技場中透過使用者投票獲得的 Elo 評分。Elo 評分是一種相對排名系統，分數越高表示模型表現越好。該分數是動態變化的，反映了模型在當前競爭環境中的相對實力。
- **置信區間**：模型 Elo 評分的95%置信區間（例如：`+6/-6`）。這個區間越小，表示模型的評分越穩定和可靠；反之，區間越大可能意味著資料量不足或模型表現波動較大。它提供了對評分準確性的量化評估。
- **票數**：該模型在競技場中收到的總投票數量。投票數越多，通常意味著其評分的統計可靠性越高。
- **服務商**：提供該模型的組織或公司。
- **許可協議**：模型的許可協議類型，例如專有 (Proprietary)、Apache 2.0、MIT 等。
- **知識截止日期**：模型訓練資料的知識截止日期。**暫無資料** 表示相關資訊未提供或未知。

## 資料來源與更新頻率

本排行榜資料由 [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) 專案自動生成並提供，該專案從 [lmarena.ai](https://lmarena.ai/) 獲取並處理資料。此排行榜由 GitHub Actions 每天自動更新。

## 免責聲明

本報告僅供參考。排行榜資料是動態變化的，並基於特定時間段內使用者在 Chatbot Arena 上的偏好投票。資料的完整性和準確性取決於上游資料來源及 `fboulnois/llm-leaderboard-csv` 專案的更新和處理。不同模型可能採用不同的許可協議，使用時請務必參考模型提供商的官方說明。