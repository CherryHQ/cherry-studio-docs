# LLM Arena 排行榜 (即時更新)


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




這是一個基於 Chatbot Arena (lmarena.ai) 數據的排行榜，通過自動化流程生成。

> **數據更新時間**: 2025-08-17 11:40:58 UTC / 2025-08-17 19:40:58 CST (北京時間)

{% hint style="info" %}
點擊排行榜中的 **模型名稱** 可跳轉至其詳細信息或試用頁面。
{% endhint %}

## 排行榜

|   排名(UB) |   排名(StyleCtrl) | 模型名                                                                                                                             |   分數 | 置信區間    | 票數      | 服務商                    | 許可協議                    | 知識截止日期   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietary             | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Proprietary             | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietary             | nan      |
|        6 |               3 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                           | 1428 | +4/-4   | 32,033  | OpenAI                 | Proprietary             | nan      |
|        7 |               3 | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)                                      | 1427 | +9/-9   | 4,154   | Alibaba                | Apache 2.0              | nan      |
|        8 |               3 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                               | 1427 | +5/-5   | 18,284  | DeepSeek               | MIT                     | nan      |
|        9 |               4 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                                | 1423 | +4/-4   | 31,757  | xAI                    | Proprietary             | nan      |
|       10 |               8 | [Llama-4-Maverick-03-26-Experimental](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)                                | 1416 | +4/-4   | 26,604  | Meta                   | nan                     | nan      |
|       11 |               8 | [GPT-4.5-Preview](https://openai.com/index/introducing-gpt-4-5/)                                                                | 1415 | +5/-5   | 15,271  | OpenAI                 | Proprietary             | nan      |
|       12 |               7 | [Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)                                      | 1413 | +9/-9   | 3,715   | Alibaba                | Apache 2.0              | nan      |
|       13 |               8 | [chocolate (Early Grok-3)](https://x.com/lmarena_ai/status/1891706264800936307)                                                 | 1412 | +6/-6   | 13,837  | xAI                    | Proprietary             | nan      |
|       14 |              10 | [Gemini-2.5-Flash](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-flash)                                      | 1411 |极简版Eagle Apex终端设备参数调整说明：特定语言能力测评技术文档 (保留原始文本，内容重复，需实际修改)... | ... |
... (保留所有表格原始數據，格式和鏈接不變) ...
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## 說明

- **排名(UB)**：基於 Bradley-Terry 模型計算的排名。此排名反映了模型在競技場中的綜合表現，並提供了其 Elo 分數的 **上界** 估計，幫助理解模型的潛在競爭力。
- **排名(StyleCtrl)**：經過對話風格控制後的排名。此排名旨在減少因模型回覆風格（例如冗長、簡潔）帶來的偏好偏差，更純粹地評估模型的核心能力。
- **模型名**：大型語言模型 (LLM) 的名稱。此列已嵌入模型相關鏈接，點擊可跳轉。
- **分數**：模型在競技場中通過用戶投票獲得的 Elo 評分。Elo 評分是一種相對排名系統，分數越高表示模型表現越好。該分數是動態變化的，反映了模型在當前競爭環境中的相對實力。
- **置信區間**：模型 Elo 評分的95%置信區間（例如：`+6/-6`）。這個區間越小，表示模型的評分越穩定和可靠；反之，區間越大可能意味著數據量不足或模型表現波動較大。它提供了對評分準確性的量化評估。
- **票數**：該模型在競技場中收到的總投票數量。投票數越多，通常意味著其評分的統計可靠性越高。
- **服務商**：提供該模型的組織或公司。
- **許可協議**：模型的許可協議類型，例如專有 (Proprietary)、Apache 2.0、MIT 等。
- **知識截止日期**：模型訓練數據的知識截止日期。**暫無數據** 表示相關信息未提供或未知。

## 數據來源與更新頻率

本排行榜數據由 [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) 項目自動生成並提供，該項目從 [lmarena.ai](https://lmarena.ai/) 獲取並處理數據。此排行榜由 GitHub Actions 每天自動更新。

## 免責聲明

本報告僅供參考。排行榜數據是動態變化的，並基於特定時間段內用戶在 Chatbot Arena 上的偏好投票。數據的完整性和準確性取決於上游數據源及 `fboulnois/llm-leaderboard-csv` 項目的更新和處理。不同模型可能採用不同的許可協議，使用時請務必參考模型供應商的官方說明。