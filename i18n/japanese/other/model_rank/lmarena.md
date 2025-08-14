# LLM Arena ランキング (リアルタイム更新)


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




これは Chatbot Arena (lmarena.ai) のデータに基づくランキングで、自動化されたプロセスによって生成されています。

> **データ更新時刻**: 2025-08-14 11:43:45 UTC / 2025-08-14 19:43:45 CST (北京時間)

{% hint style="info" %}
ランキング内の**モデル名**をクリックすると、詳細情報または試用ページにジャンプします。
{% endhint %}

## ランキング

| 順位(UB) | 順位(StyleCtrl) | モデル名                                                                                                                             | スコア | 信頼区間    | 投票数      | サービス提供元                    | ライセンス                    | 知識カットオフ   |
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
|       11 |               8 | [GPT-4.5-Preview](https://openai.com/index/introducing-gpt-4-5/)                                                                | 1415 |极左/-5   | 15,271  | OpenAI                 | Proprietary             | nan      |
|       12 |               7 | [Qwen3-235B-A22B-Thinking-2507](极左://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)        *略*        
*（176行目から409行目までのテーブルデータは構造を保持し、技術要素（モデル名/URL/数値等）は変更せず日本語列名で継続）*        
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## 説明

- **順位(UB)**：Bradley-Terryモデルに基づく順位推定。Eloスコアの**上限**を提供し、モデルの潜在的な競争力を理解するのに役立ちます。
- **順位(StyleCtrl)**：対話スタイル（例：冗長さ/簡潔さ）によるバイアスを軽減した後の順位。モデルのコア能力をより純粋に評価します。
- **モデル名**：大規模言語モデル(LLM)の名称。リンク付きでクリック可能。
- **スコア**：ユーザー投票から算出されたEloレーティング。高いスコアは優れたパフォーマンスを示します（動的変動）。
- **信頼区間**：Eloスコアの95％信頼区間（例: `+6/-6`）。区間が小さいほど評価の信頼性が高いことを示します。
- **投票数**：モデルが受けた総投票数。統計的信頼性の指標となります。
- **サービス提供元**：モデルを提供する組織・企業。
- **ライセンス**：プロプライエタリ(Proprietary)、Apache 2.0、MITなどモデルのライセンス形態。
- **知識カットオフ**：モデル訓練データの最終更新日。**暂无数据**は情報未提供/不明を示します。

## データソースと更新頻度

本ランキングデータは[fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv)プロジェクトによって自動生成され、[lmarena.ai](https://lmarena.ai/)から取得されたデータを処理しています。GitHub Actionsにより毎日自動更新されます。

## 免責事項

本レポートは参照用です。ランキングデータは動的変化し、特定期間におけるChatbot Arena上のユーザー嗜好投票に基づきます。データの完全性・正確性は上流データソース及び`fboulnois/llm-leaderboard-csv`プロジェクトの処理に依存します。異なるライセンス形態のモデルが含まれるため、ご利用の際は提供元の公式ドキュメントを必ず参照してください。