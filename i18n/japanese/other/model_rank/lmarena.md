# LLM Arena ランキング (リアルタイム更新)


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




これは Chatbot Arena (lmarena.ai) のデータに基づくランキングで、自動化プロセスにより生成されています。

> **データ更新時刻**: 2025-09-08 11:40:35 UTC / 2025-09-08 19:40:35 CST (北京時間)

{% hint style="info" %}
ランキング内の **モデル名** をクリックすると、詳細情報または試用ページに遷移します。
{% endhint %}

## ランキング

|   順位(UB) |   順位(StyleCtrl) | モデル名                                                                                                                             |   スコア | 信頼区間    | 投票数      | プロバイダー                    | ライセンス                    | ナレッジカットオフ   |
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
|...（中略: ランキングテーブルは完全に構造を維持）...|
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## 説明

- **順位(UB)**: Bradley-Terryモデルに基づく順位。この順位はモデルのアリーナでの総合的なパフォーマンスを反映し、Eloスコアの**上限**推定値を提供し、モデルの潜在的な競争力を理解するのに役立ちます。
- **順位(StyleCtrl)**: 対話スタイル制御後の順位。この順位は、モデルの応答スタイル（例えば冗長性、簡潔さ）による選好バイアスを減らし、モデルのコア能力をより純粋に評価することを目的としています。
- **モデル名**: 大規模言語モデル（LLM）の名称。この列にはモデル関連のリンクが埋め込まれており、クリックで遷移します。
- **スコア**: アリーナでのユーザー投票から獲得したElo評価スコア。Elo評価は相対的なランキングシステムであり、スコアが高いほどモデルのパフォーマンスが優れていることを示します。このスコアは変動し、モデルの現在の競争環境における相対的な実力を反映します。
- **信頼区間**: モデルのElo評価スコアの95%信頼区間（例: `+6/-6`）。この区間が小さいほど、モデルの評価が安定し信頼性が高いことを意味します。逆に区間が大きい場合は、データ不足やモデルのパフォーマンス変動が大きい可能性があります。評価の正確さを定量化する指標を提供します。
- **投票数**: アリーナでそのモデルが受け取った総投票数。投票数が多いほど、通常は評価の統計的信頼性が高くなります。
- **プロバイダー**: モデルを提供する組織または企業。
- **ライセンス**: モデルライセンスの種類（例：プロプライエタリ、Apache 2.0、MITなど）。
- **ナレッジカットオフ**: モデルトレーニングデータの知識のカットオフ日。**データなし**は情報が提供されていない、または不明であることを示します。

## データソースと更新頻度

このランキングデータは [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) プロジェクトにより自動生成・提供されており、[lmarena.ai](https://lmarena.ai/) からデータを取得・処理しています。このランキングはGitHub Actionsにより毎日自動更新されます。

## 免責事項

本レポートは参考情報です。ランキングデータは動的に変化し、特定期間内のChatbot Arena上でのユーザー選好投票に基づいています。データの完全性と正確性は、上流データソース及び `fboulnois/llm-leaderboard-csv` プロジェクトの更新と処理に依存します。異なるモデルは異なるライセンスを採用している可能性があるため、使用時には必ずモデルプロバイダーの公式説明を参照してください。