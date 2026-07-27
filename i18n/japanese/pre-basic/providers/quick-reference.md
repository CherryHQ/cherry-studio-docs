---
icon: list
---

# すべてのモデルプロバイダー：クイックリファレンス

このページでは、Cherry Studio V2 に現在組み込まれているモデルプロバイダーのテンプレートを一覧にしています。プロバイダー名、設定済みの API、認証情報の取得先を確認するときに使用してください。この一覧はバージョンに応じて更新されます。ページの内容がアプリと異なる場合は、`設定 → モデルプロバイダー → すべてのプロバイダー` に実際に表示される内容を優先してください。

{% hint style="info" %}
ここでいう「API」は、Cherry Studio が各テンプレートに設定した接続方法です。そのテンプレート内のすべてのモデルが同じ機能に対応するという意味ではありません。ビジョン、推論、ツール呼び出しへの対応は、プロバイダーのモデル説明と実際のテスト結果を確認してください。
{% endhint %}

## この表の使い方

1. 利用中または接続予定のプロバイダーを下の表から探します。
2. **認証情報の取得先**を開き、プロバイダーの要件に従って API Key またはクラウドアカウントの認証情報を作成します。
3. Cherry Studio の `設定 → モデルプロバイダー` に戻り、左側のフィルターを **すべてのプロバイダー** に切り替えて、同名のプロバイダーを選択します。
4. [モデルプロバイダー](README.md)の手順に従って、認証、モデルリストの取得、モデルの有効化、接続チェックを完了します。

プロバイダーが一覧になくても互換 API を提供している場合は、[カスタムプロバイダー](zi-ding-yi-fu-wu-shang.md)を使用してください。

## API 名の説明

| このページでの略称 | 対応する API |
|---|---|
| OpenAI Chat | OpenAI Chat Completions |
| OpenAI Responses | OpenAI Responses |
| Anthropic | Anthropic Messages |
| Gemini | Google Generate Content |
| Ollama | Ollama Chat |
| 専用接続 | Cherry Studio が、そのクラウドプラットフォームまたはサービス専用の認証とルーティングを使用 |

左側のリストで **Agent** フィルターを選ぶと、Anthropic 互換エンドポイントを持つプロバイダーが表示されます。これは接続方法によるフィルターであり、すべてのモデルがツールを呼び出せることを保証するものではありません。

## 複数 API テンプレート

次のテンプレートには 2 種類の API が設定されています。同じプロバイダー内でも、モデルに合った接続方法を選択できます。

| Provider | 設定済み API | 認証情報の取得先 | ガイド |
|---|---|---|---|
| CherryIN | Anthropic、OpenAI Chat | [認証情報を取得](https://open.cherryin.ai/console/token) | [設定](cherryin-1.md) |
| Silicon | Anthropic、OpenAI Chat | [認証情報を取得](https://cloud.siliconflow.cn/) | [設定](siliconcloud.md) |
| AiHubMix | Anthropic、OpenAI Chat | [認証情報を取得](https://aihubmix.com) | — |
| ZhiPu | Anthropic、OpenAI Chat | [認証情報を取得](https://open.bigmodel.cn/usercenter/apikeys) | — |
| deepseek | Anthropic、OpenAI Chat | [認証情報を取得](https://platform.deepseek.com/api_keys) | [設定](deepseek.md) |
| DMXAPI | Anthropic、OpenAI Chat | [認証情報を取得](https://www.dmxapi.cn/) | — |
| TokenFlux | Anthropic、OpenAI Chat | [認証情報を取得](https://api.tokenflux.ai/dashboard/api-keys) | — |
| 302.AI | Anthropic、OpenAI Chat | [認証情報を取得](https://dash.302.ai/apis/list) | — |
| Qiniu | Anthropic、OpenAI Chat | [認証情報を取得](https://portal.qiniu.com/ai-inference/api-key) | — |
| OpenRouter | Anthropic、OpenAI Chat | [認証情報を取得](https://openrouter.ai/settings/keys) | [設定](openrouter.md) |
| Ollama | Anthropic、Ollama | [公式サイト](https://ollama.com/) | [設定](ollama.md) |
| New API | Anthropic、OpenAI Chat | [ドキュメント](https://docs.newapi.pro/) | [設定](newapi.md) |
| LM Studio | Anthropic、OpenAI Chat | [公式サイト](https://lmstudio.ai/) | [設定](lm-studio.md) |
| Moonshot AI | Anthropic、OpenAI Chat | [認証情報を取得](https://platform.moonshot.cn/console/api-keys) | [設定](moonshot.md) |
| Bailian | Anthropic、OpenAI Chat | [認証情報を取得](https://bailian.console.aliyun.com/?tab=model#/api-key) | [設定](a-li-yun-bai-lian.md) |
| MiniMax | Anthropic、OpenAI Chat | [認証情報を取得](https://platform.minimaxi.com/user-center/basic-information/interface-key) | [設定](minimax.md) |
| ModelScope | Anthropic、OpenAI Chat | [認証情報を取得](https://modelscope.cn/my/myaccesstoken) | [設定](modelscope.md) |
| LongCat | Anthropic、OpenAI Chat | [認証情報を取得](https://longcat.chat/platform/api_keys) | — |
| Xiaomi MiMo | Anthropic、OpenAI Chat | [認証情報を取得](https://platform.xiaomimimo.com/#/console/usage) | — |
| zai | Anthropic、OpenAI Chat | [認証情報を取得](https://z.ai/manage-apikey/apikey-list) | — |
| minimax-global | Anthropic、OpenAI Chat | [認証情報を取得](https://platform.minimax.io/user-center/basic-information/interface-key) | — |

## 単一 API テンプレート

| Provider | 設定済み API | 認証情報の取得先 | ガイド |
|---|---|---|---|
| OpenVINO Model Server | OpenAI Chat | [公式サイト](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html) | — |
| ocoolAI | OpenAI Chat | [認証情報を取得](https://one.ocoolai.com/token) | — |
| AlayaNew | OpenAI Chat | [公式サイト](https://www.alayanew.com/) | — |
| AIOnly | OpenAI Chat | [認証情報を取得](https://maas.aiionly.com/keyApi) | — |
| BurnCloud | OpenAI Chat | [認証情報を取得](https://ai.burncloud.com/token) | — |
| Cephalon | OpenAI Chat | [認証情報を取得](https://cephalon.cloud/api) | — |
| LANYUN | OpenAI Chat | [認証情報を取得](https://maas.lanyun.net/#/system/apiKey) | — |
| PH8 | OpenAI Chat | [認証情報を取得](https://ph8.co/apiKey) | — |
| SophNet | OpenAI Chat | [認証情報を取得](https://sophnet.com/#/project/key) | — |
| PPIO | OpenAI Chat | [認証情報を取得](https://ppio.com/settings/key-management) | [設定](ppio.md) |
| Anthropic | Anthropic | [認証情報を取得](https://console.anthropic.com/settings/keys) | [設定](anthropic.md) |
| OpenAI | OpenAI Responses | [認証情報を取得](https://platform.openai.com/api-keys) | [設定](openai.md) |
| Gemini | Gemini | [認証情報を取得](https://aistudio.google.com/app/apikey) | [設定](google-gemini.md) |
| Github Models | OpenAI Chat | [認証情報を取得](https://github.com/settings/tokens) | — |
| Github Copilot | OpenAI Chat | [公式サイト](https://github.com/features/copilot) | [設定](github-copilot.md) |
| Yi | OpenAI Chat | [認証情報を取得](https://platform.lingyiwanwu.com/apikeys) | — |
| BAICHUAN AI | OpenAI Chat | [認証情報を取得](https://platform.baichuan-ai.com/console/apikey) | — |
| StepFun | OpenAI Chat | [認証情報を取得](https://platform.stepfun.com/interface-key) | — |
| doubao | OpenAI Chat | [コンソール](https://www.volcengine.com/experience/ark) | [設定](doubao.md) |
| Infini | OpenAI Chat | [認証情報を取得](https://cloud.infini-ai.com/iam/secret/key) | — |
| Groq | OpenAI Chat | [認証情報を取得](https://console.groq.com/keys) | [設定](groq.md) |
| Together | OpenAI Chat | [認証情報を取得](https://api.together.ai/settings/api-keys) | — |
| Fireworks | OpenAI Chat | [認証情報を取得](https://fireworks.ai/account/api-keys) | — |
| nvidia | OpenAI Chat | [コンソール](https://build.nvidia.com/explore/discover) | — |
| Grok | OpenAI Chat | [公式サイト](https://x.ai/) | [設定](grok.md) |
| Hyperbolic | OpenAI Chat | [認証情報を取得](https://app.hyperbolic.xyz/settings) | — |
| Mistral | OpenAI Chat | [認証情報を取得](https://console.mistral.ai/api-keys/) | — |
| Jina | OpenAI Chat | [公式サイト](https://jina.ai) | — |
| Perplexity | OpenAI Chat | [認証情報を取得](https://www.perplexity.ai/settings/api) | — |
| Xirang | OpenAI Chat | [コンソール](https://huiju.ctyun.cn/service/serviceGroup) | — |
| hunyuan | OpenAI Chat | [認証情報を取得](https://console.cloud.tencent.com/hunyuan/api-key) | — |
| Tencent Cloud TI | OpenAI Chat | [認証情報を取得](https://console.cloud.tencent.com/lkeap/api) | — |
| Baidu Cloud | OpenAI Chat | [認証情報を取得](https://console.bce.baidu.com/iam/#/iam/apikey/list) | — |
| VoyageAI | OpenAI Chat | [認証情報を取得](https://dashboard.voyageai.com/organization/api-keys) | — |
| Poe | OpenAI Chat | [認証情報を取得](https://poe.com/api/keys) | — |
| Hugging Face | OpenAI Responses | [認証情報を取得](https://huggingface.co/settings/tokens) | — |
| Vercel AI Gateway | OpenAI Chat | [公式サイト](https://vercel.com/) | — |
| Cerebras AI | OpenAI Chat | [コンソール](https://cloud.cerebras.ai) | — |

## 専用接続テンプレート

次の項目は、通常の API Key と Base URL の組み合わせではありません。画面の各フィールドに合わせて、対象クラウドプラットフォームの情報を準備してください。

| Provider | 認証または接続方法 | 認証情報の取得先 | ガイド |
|---|---|---|---|
| Azure OpenAI | Azure の認証情報、API Version、デプロイ情報 | [Azure Portal](https://portal.azure.com/) | [設定](azure-openai.md) |
| VertexAI | Google Cloud のプロジェクト、リージョン、認証情報 | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) | [設定](vertex-ai.md) |
| GPUStack | GPUStack のサービスアドレスと認証情報 | [公式サイト](https://gpustack.ai/) | — |
| AWS Bedrock | AWS リージョンと IAM または Bedrock API Key | [IAM ドキュメント](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html) | — |

{% hint style="warning" %}
プロバイダーは登録先、モデル権限、地域制限、料金ルールを変更する場合があります。認証情報を作成する前に、プラットフォームの最新情報を確認してください。Cherry Studio は接続だけを行い、プロバイダーに代わってアカウントや利用枠を提供するものではありません。
{% endhint %}

## 目的のサービスが一覧にない場合

- セルフホストした New API：[New API](newapi.md) テンプレートを使用します。
- セルフホストした One API またはその他の互換ゲートウェイ：[OneAPI](oneapi.md)または[カスタムプロバイダー](zi-ding-yi-fu-wu-shang.md)を参照してください。
- OpenAI、Anthropic、Gemini、OpenAI Responses の互換アドレスだけがある場合：[カスタムプロバイダー](zi-ding-yi-fu-wu-shang.md)を直接作成し、対応するエンドポイントを入力します。

テンプレート名は存在していても、デプロイ先が既定のアドレスと異なる場合は、そのプロバイダーを複製して、複製した項目のアドレスと認証設定を変更できます。

問題が発生した場合は、まず[モデルプロバイダー](README.md#よくある質問)に従って、プロバイダーのスイッチ、モデルのスイッチ、API Key、Base URL、API タイプを確認してください。
