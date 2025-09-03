# LLM Arena リーダーボード (リアルタイム更新)


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




これはChatbot Arena (lmarena.ai)のデータに基づくリーダーボードで、自動プロセスによって生成されています。

> **データ更新日時**: 2025-09-03 11:40:24 UTC / 2025-09-03 19:40:24 CST (北京時間)

{% hint style="info" %}
リーダーボードの **モデル名** をクリックすると、詳細情報または試用ページに移動できます。
{% endhint %}

## リーダーボード

| ランキング(UB) | ランキング(StyleCtrl) | モデル名                                                                                                                             | スコア | 信頼区間    | 票数      | サービスプロバイダー            | ライセンス                   | ナレッジカットオフ日 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietary             | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Proprietary             | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietary             | nan      |
|... (表中データは原文のまま維持) |


|      262 |             258 | [OpenAssistant-Pythia-12B](https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5)                               |  923 | +10/-10 | 6,368   | OpenAssistant          | Apache 2.0              | 2023/4   |
|      263 |             260 | [FastChat-T5-3B](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)                                                              |  901 | +12/-12 | 4,288   | LMSYS                  | Apache 2.0              | 2023/4   |
|      264 |             263 | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)                                           |  873 | +12/-12 | 3,336   | Stability AI           | CC-BY-NC-SA-4.0         | 2023/4   |
|      265 |             263 | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                  |  857 | +13/-13 | 3,480   | Databricks             | MIT                     | 2023/4   |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## 説明

- **ランキング(UB)**：Bradley-Terryモデルに基づくランキング。この順位はアリーナでのモデルの総合的なパフォーマンスを反映し、Eloスコアの**上界**推定値を提供して、モデルの潜在的な競争力を理解するのに役立ちます。
- **ランキング(StyleCtrl)**：対話スタイル制御後のランキング。この順位はモデルの返答スタイル（冗長さ、簡潔さなど）による選好バイアスを軽減し、モデルのコア能力をより純粋に評価することを目的としています。
- **モデル名**：大規模言語モデル(LLM)の名称。この列には関連リンクが埋め込まれており、クリックするとジャンプします。
- **スコア**：ユーザー投票を通じてアリーナで獲得したEloレーティング。Eloレーティングは相対評価システムで、スコアが高いほどパフォーマンスが優れていることを示します。このスコアは動的に変動し、現在の競争環境におけるモデルの相対的な強さを反映しています。
- **信頼区間**：Eloレーティングの95%信頼区間（例：`+6/-6`）。この区間が小さいほどスコアの信頼性と安定性が高く、大きい場合はデータ不足やパフォーマンスの変動を示唆しています。スコア精度の定量的評価を提供します。
- **票数**：アリーナで該当モデルが受けた総投票数。票数が多いほど統計的な信頼性が高まります。
- **サービスプロバイダー**：モデルを提供する組織または企業。
- **ライセンス**：モデルのライセンスタイプ（専有(Proprietary)、Apache 2.0、MITなど）。
- **ナレッジカットオフ日**：モデル訓練データの知識最終更新日。**データなし**は情報提供なしまたは不明を示します。

## データソースと更新頻度

本リーダーボードのデータは[fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv)プロジェクトで自動生成・提供され、[lmarena.ai](https://lmarena.ai/)から取得・処理されたデータを使用しています。このリーダーボードはGitHub Actionsにより毎日自動更新されます。

## 免責事項

本レポートは参考情報として提供されています。リーダーボードデータは動的に変化し、Chatbot Arena上での特定期間のユーザー嗜好投票に基づいています。データの完全性と正確性は、上流データソースおよび`fboulnois/llm-leaderboard-csv`プロジェクトの更新・処理に依存します。異なるモデルは様々なライセンスを採用している可能性があるため、使用時にはモデル提供者の公式説明を必ず参照してください。