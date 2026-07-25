---
icon: list
---

# 全部 Provider 快速參考

本頁列出 Cherry Studio V2 目前內建的模型服務範本，方便你確認服務商名稱、預設介面和憑證入口。清單會隨版本更新；如果本頁與用戶端不一致，請以 `設定 → 模型服務 → 全部服務商` 中實際顯示的內容為準。

{% hint style="info" %}
這裡的「介面」表示 Cherry Studio 為該範本預設的連線方式，並不代表其中每個模型都支援相同能力。模型是否支援視覺、推理或工具呼叫，請以服務商的模型說明和實際測試為準。
{% endhint %}

## 如何使用這張表

1. 在下方找到你已有帳戶或準備連線的服務商；
2. 開啟**憑證入口**，依照服務商要求建立 API Key 或雲端帳戶憑證；
3. 返回 Cherry Studio 的 `設定 → 模型服務`，將左側篩選切換為**全部服務商**，並選擇同名服務商；
4. 依照[模型服務](README.md)中的步驟完成身分驗證、取得模型、啟用模型和連線檢查。

如果服務商不在清單中，但提供相容介面，請使用[自訂服務商](zi-ding-yi-fu-wu-shang.md)。

## 介面名稱說明

| 本頁簡稱 | 對應介面 |
|---|---|
| OpenAI Chat | OpenAI Chat Completions |
| OpenAI Responses | OpenAI Responses |
| Anthropic | Anthropic Messages |
| Gemini | Google Generate Content |
| Ollama | Ollama Chat |
| 專用連線 | 由 Cherry Studio 使用該雲端平台或服務的專用身分驗證與路由 |

左側清單中的 **支援 Agent** 篩選會顯示具有 Anthropic 相容端點的服務商。這只是連線方式篩選，不保證所有模型都能呼叫工具。

## 多介面範本

這些範本預設了兩種介面。你可以在同一個服務商下，為不同模型選擇合適的連線方式。

| Provider | 預設介面 | 憑證入口 | 專題 |
|---|---|---|---|
| CherryIN | Anthropic、OpenAI Chat | [取得憑證](https://open.cherryin.ai/console/token) | [設定](cherryin-1.md) |
| Silicon | Anthropic、OpenAI Chat | [取得憑證](https://cloud.siliconflow.cn/) | [設定](siliconcloud.md) |
| AiHubMix | Anthropic、OpenAI Chat | [取得憑證](https://aihubmix.com) | — |
| ZhiPu | Anthropic、OpenAI Chat | [取得憑證](https://open.bigmodel.cn/usercenter/apikeys) | — |
| deepseek | Anthropic、OpenAI Chat | [取得憑證](https://platform.deepseek.com/api_keys) | [設定](deepseek.md) |
| DMXAPI | Anthropic、OpenAI Chat | [取得憑證](https://www.dmxapi.cn/) | — |
| TokenFlux | Anthropic、OpenAI Chat | [取得憑證](https://api.tokenflux.ai/dashboard/api-keys) | — |
| 302.AI | Anthropic、OpenAI Chat | [取得憑證](https://dash.302.ai/apis/list) | — |
| Qiniu | Anthropic、OpenAI Chat | [取得憑證](https://portal.qiniu.com/ai-inference/api-key) | — |
| OpenRouter | Anthropic、OpenAI Chat | [取得憑證](https://openrouter.ai/settings/keys) | [設定](openrouter.md) |
| Ollama | Anthropic、Ollama | [官網](https://ollama.com/) | [設定](ollama.md) |
| New API | Anthropic、OpenAI Chat | [文件](https://docs.newapi.pro/) | [設定](newapi.md) |
| LM Studio | Anthropic、OpenAI Chat | [官網](https://lmstudio.ai/) | [設定](lm-studio.md) |
| Moonshot AI | Anthropic、OpenAI Chat | [取得憑證](https://platform.moonshot.cn/console/api-keys) | [設定](moonshot.md) |
| Bailian | Anthropic、OpenAI Chat | [取得憑證](https://bailian.console.aliyun.com/?tab=model#/api-key) | [設定](a-li-yun-bai-lian.md) |
| MiniMax | Anthropic、OpenAI Chat | [取得憑證](https://platform.minimaxi.com/user-center/basic-information/interface-key) | [設定](minimax.md) |
| ModelScope | Anthropic、OpenAI Chat | [取得憑證](https://modelscope.cn/my/myaccesstoken) | [設定](modelscope.md) |
| LongCat | Anthropic、OpenAI Chat | [取得憑證](https://longcat.chat/platform/api_keys) | — |
| Xiaomi MiMo | Anthropic、OpenAI Chat | [取得憑證](https://platform.xiaomimimo.com/#/console/usage) | — |
| zai | Anthropic、OpenAI Chat | [取得憑證](https://z.ai/manage-apikey/apikey-list) | — |
| minimax-global | Anthropic、OpenAI Chat | [取得憑證](https://platform.minimax.io/user-center/basic-information/interface-key) | — |

## 單一介面範本

| Provider | 預設介面 | 憑證入口 | 專題 |
|---|---|---|---|
| OpenVINO Model Server | OpenAI Chat | [官網](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html) | — |
| ocoolAI | OpenAI Chat | [取得憑證](https://one.ocoolai.com/token) | — |
| AlayaNew | OpenAI Chat | [官網](https://www.alayanew.com/) | — |
| AIOnly | OpenAI Chat | [取得憑證](https://maas.aiionly.com/keyApi) | — |
| BurnCloud | OpenAI Chat | [取得憑證](https://ai.burncloud.com/token) | — |
| Cephalon | OpenAI Chat | [取得憑證](https://cephalon.cloud/api) | — |
| LANYUN | OpenAI Chat | [取得憑證](https://maas.lanyun.net/#/system/apiKey) | — |
| PH8 | OpenAI Chat | [取得憑證](https://ph8.co/apiKey) | — |
| SophNet | OpenAI Chat | [取得憑證](https://sophnet.com/#/project/key) | — |
| PPIO | OpenAI Chat | [取得憑證](https://ppio.com/settings/key-management) | [設定](ppio.md) |
| Anthropic | Anthropic | [取得憑證](https://console.anthropic.com/settings/keys) | [設定](anthropic.md) |
| OpenAI | OpenAI Responses | [取得憑證](https://platform.openai.com/api-keys) | [設定](openai.md) |
| Gemini | Gemini | [取得憑證](https://aistudio.google.com/app/apikey) | [設定](google-gemini.md) |
| Github Models | OpenAI Chat | [取得憑證](https://github.com/settings/tokens) | — |
| Github Copilot | OpenAI Chat | [官網](https://github.com/features/copilot) | [設定](github-copilot.md) |
| Yi | OpenAI Chat | [取得憑證](https://platform.lingyiwanwu.com/apikeys) | — |
| BAICHUAN AI | OpenAI Chat | [取得憑證](https://platform.baichuan-ai.com/console/apikey) | — |
| StepFun | OpenAI Chat | [取得憑證](https://platform.stepfun.com/interface-key) | — |
| doubao | OpenAI Chat | [控制台](https://www.volcengine.com/experience/ark) | [設定](doubao.md) |
| Infini | OpenAI Chat | [取得憑證](https://cloud.infini-ai.com/iam/secret/key) | — |
| Groq | OpenAI Chat | [取得憑證](https://console.groq.com/keys) | [設定](groq.md) |
| Together | OpenAI Chat | [取得憑證](https://api.together.ai/settings/api-keys) | — |
| Fireworks | OpenAI Chat | [取得憑證](https://fireworks.ai/account/api-keys) | — |
| nvidia | OpenAI Chat | [控制台](https://build.nvidia.com/explore/discover) | — |
| Grok | OpenAI Chat | [官網](https://x.ai/) | [設定](grok.md) |
| Hyperbolic | OpenAI Chat | [取得憑證](https://app.hyperbolic.xyz/settings) | — |
| Mistral | OpenAI Chat | [取得憑證](https://console.mistral.ai/api-keys/) | — |
| Jina | OpenAI Chat | [官網](https://jina.ai) | — |
| Perplexity | OpenAI Chat | [取得憑證](https://www.perplexity.ai/settings/api) | — |
| Xirang | OpenAI Chat | [控制台](https://huiju.ctyun.cn/service/serviceGroup) | — |
| hunyuan | OpenAI Chat | [取得憑證](https://console.cloud.tencent.com/hunyuan/api-key) | — |
| Tencent Cloud TI | OpenAI Chat | [取得憑證](https://console.cloud.tencent.com/lkeap/api) | — |
| Baidu Cloud | OpenAI Chat | [取得憑證](https://console.bce.baidu.com/iam/#/iam/apikey/list) | — |
| VoyageAI | OpenAI Chat | [取得憑證](https://dashboard.voyageai.com/organization/api-keys) | — |
| Poe | OpenAI Chat | [取得憑證](https://poe.com/api/keys) | — |
| Hugging Face | OpenAI Responses | [取得憑證](https://huggingface.co/settings/tokens) | — |
| Vercel AI Gateway | OpenAI Chat | [官網](https://vercel.com/) | — |
| Cerebras AI | OpenAI Chat | [控制台](https://cloud.cerebras.ai) | — |

## 專用連線範本

這幾項不是一般的 API Key + Base URL 組合。請依照頁面欄位準備相應的雲端平台資訊。

| Provider | 身分驗證或連線方式 | 憑證入口 | 專題 |
|---|---|---|---|
| Azure OpenAI | Azure 憑證、API Version、部署資訊 | [Azure Portal](https://portal.azure.com/) | [設定](azure-openai.md) |
| VertexAI | Google Cloud 專案、區域與憑證 | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) | [設定](vertex-ai.md) |
| GPUStack | GPUStack 服務位址與憑證 | [官網](https://gpustack.ai/) | — |
| AWS Bedrock | AWS 區域與 IAM 或 Bedrock API Key | [IAM 文件](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html) | — |

{% hint style="warning" %}
服務商可能調整註冊位址、模型權限、地區限制和計費規則。建立憑證前，請閱讀該平台的最新說明；Cherry Studio 只負責連線，不會代替服務商提供帳戶或額度。
{% endhint %}

## 清單中沒有目標服務

- 自建 New API：使用 [New API](newapi.md) 範本；
- 自建 One API 或其他相容閘道：參考 [OneAPI](oneapi.md) 或[自訂服務商](zi-ding-yi-fu-wu-shang.md)；
- 只有 OpenAI、Anthropic、Gemini 或 OpenAI Responses 相容位址：直接建立[自訂服務商](zi-ding-yi-fu-wu-shang.md)，並填寫相應端點。

如果範本名稱存在，但你的部署位址與預設值不同，可以複製該服務商，再修改副本的位址和身分驗證設定。

遇到問題時，請先依照[模型服務](README.md#常見問題)檢查服務商開關、模型開關、API Key、Base URL 和介面類型。
