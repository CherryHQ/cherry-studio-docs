---
icon: list
---

# 全部 Provider 快速参考

本页列出 Cherry Studio V2 当前内置的模型服务模板，方便你确认服务商名称、预设接口和凭证入口。列表会随版本更新；如果本页与客户端不一致，请以 `设置 → 模型服务 → 全部` 中实际显示的内容为准。

{% hint style="info" %}
这里的“接口”表示 Cherry Studio 为该模板预设的连接方式，并不等同于其中每个模型都支持相同能力。模型是否支持视觉、推理或工具调用，请以服务商的模型说明和实际测试为准。
{% endhint %}

## 怎么使用这张表

1. 在下面找到已有账户或准备接入的服务商；
2. 打开**凭证入口**，根据服务商要求创建 API Key 或云账户凭证；
3. 返回 Cherry Studio 的 `设置 → 模型服务`，将左侧筛选切换为**全部**并选择同名服务商；
4. 按[模型服务](README.md)中的步骤完成鉴权、同步模型、启用模型和连接检查。

如果服务商不在列表中，但提供兼容接口，请使用[自定义服务商](zi-ding-yi-fu-wu-shang.md)。

## 接口名称说明

| 本页简称 | 对应接口 |
|---|---|
| OpenAI Chat | OpenAI Chat Completions |
| OpenAI Responses | OpenAI Responses |
| Anthropic | Anthropic Messages |
| Gemini | Google Generate Content |
| Ollama | Ollama Chat |
| 专用接入 | 由 Cherry Studio 使用该云平台或服务的专用鉴权与路由 |

左侧列表中的 **Agent** 筛选会显示具有 Anthropic 兼容端点的服务商。它只是连接方式筛选，不保证所有模型都能调用工具。

## 多接口模板

这些模板预设了两种接口。你可以在同一服务商下为不同模型选择合适的连接方式。

| Provider | 预设接口 | 凭证入口 | 专题 |
|---|---|---|---|
| CherryIN | Anthropic、OpenAI Chat | [获取凭证](https://open.cherryin.ai/console/token) | [配置](cherryin-1.md) |
| Silicon | Anthropic、OpenAI Chat | [获取凭证](https://cloud.siliconflow.cn/) | [配置](siliconcloud.md) |
| AiHubMix | Anthropic、OpenAI Chat | [获取凭证](https://aihubmix.com) | — |
| ZhiPu | Anthropic、OpenAI Chat | [获取凭证](https://open.bigmodel.cn/usercenter/apikeys) | — |
| deepseek | Anthropic、OpenAI Chat | [获取凭证](https://platform.deepseek.com/api_keys) | [配置](deepseek.md) |
| DMXAPI | Anthropic、OpenAI Chat | [获取凭证](https://www.dmxapi.cn/) | — |
| TokenFlux | Anthropic、OpenAI Chat | [获取凭证](https://api.tokenflux.ai/dashboard/api-keys) | — |
| 302.AI | Anthropic、OpenAI Chat | [获取凭证](https://dash.302.ai/apis/list) | — |
| Qiniu | Anthropic、OpenAI Chat | [获取凭证](https://portal.qiniu.com/ai-inference/api-key) | — |
| OpenRouter | Anthropic、OpenAI Chat | [获取凭证](https://openrouter.ai/settings/keys) | [配置](openrouter.md) |
| Ollama | Anthropic、Ollama | [官网](https://ollama.com/) | [配置](ollama.md) |
| New API | Anthropic、OpenAI Chat | [文档](https://docs.newapi.pro/) | [配置](newapi.md) |
| LM Studio | Anthropic、OpenAI Chat | [官网](https://lmstudio.ai/) | [配置](lm-studio.md) |
| Moonshot AI | Anthropic、OpenAI Chat | [获取凭证](https://platform.moonshot.cn/console/api-keys) | [配置](moonshot.md) |
| Bailian | Anthropic、OpenAI Chat | [获取凭证](https://bailian.console.aliyun.com/?tab=model#/api-key) | [配置](a-li-yun-bai-lian.md) |
| MiniMax | Anthropic、OpenAI Chat | [获取凭证](https://platform.minimaxi.com/user-center/basic-information/interface-key) | [配置](minimax.md) |
| ModelScope | Anthropic、OpenAI Chat | [获取凭证](https://modelscope.cn/my/myaccesstoken) | [配置](modelscope.md) |
| LongCat | Anthropic、OpenAI Chat | [获取凭证](https://longcat.chat/platform/api_keys) | — |
| Xiaomi MiMo | Anthropic、OpenAI Chat | [获取凭证](https://platform.xiaomimimo.com/#/console/usage) | — |
| zai | Anthropic、OpenAI Chat | [获取凭证](https://z.ai/manage-apikey/apikey-list) | — |
| minimax-global | Anthropic、OpenAI Chat | [获取凭证](https://platform.minimax.io/user-center/basic-information/interface-key) | — |

## 单接口模板

| Provider | 预设接口 | 凭证入口 | 专题 |
|---|---|---|---|
| OpenVINO Model Server | OpenAI Chat | [官网](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html) | — |
| ocoolAI | OpenAI Chat | [获取凭证](https://one.ocoolai.com/token) | — |
| AlayaNew | OpenAI Chat | [官网](https://www.alayanew.com/) | — |
| AIOnly | OpenAI Chat | [获取凭证](https://maas.aiionly.com/keyApi) | — |
| BurnCloud | OpenAI Chat | [获取凭证](https://ai.burncloud.com/token) | — |
| Cephalon | OpenAI Chat | [获取凭证](https://cephalon.cloud/api) | — |
| LANYUN | OpenAI Chat | [获取凭证](https://maas.lanyun.net/#/system/apiKey) | — |
| PH8 | OpenAI Chat | [获取凭证](https://ph8.co/apiKey) | — |
| SophNet | OpenAI Chat | [获取凭证](https://sophnet.com/#/project/key) | — |
| PPIO | OpenAI Chat | [获取凭证](https://ppio.com/settings/key-management) | [配置](ppio.md) |
| Anthropic | Anthropic | [获取凭证](https://console.anthropic.com/settings/keys) | [配置](anthropic.md) |
| OpenAI | OpenAI Responses | [获取凭证](https://platform.openai.com/api-keys) | [配置](openai.md) |
| Gemini | Gemini | [获取凭证](https://aistudio.google.com/app/apikey) | [配置](google-gemini.md) |
| Github Models | OpenAI Chat | [获取凭证](https://github.com/settings/tokens) | — |
| Github Copilot | OpenAI Chat | [官网](https://github.com/features/copilot) | [配置](github-copilot.md) |
| Yi | OpenAI Chat | [获取凭证](https://platform.lingyiwanwu.com/apikeys) | — |
| BAICHUAN AI | OpenAI Chat | [获取凭证](https://platform.baichuan-ai.com/console/apikey) | — |
| StepFun | OpenAI Chat | [获取凭证](https://platform.stepfun.com/interface-key) | — |
| doubao | OpenAI Chat | [控制台](https://www.volcengine.com/experience/ark) | [配置](doubao.md) |
| Infini | OpenAI Chat | [获取凭证](https://cloud.infini-ai.com/iam/secret/key) | — |
| Groq | OpenAI Chat | [获取凭证](https://console.groq.com/keys) | [配置](groq.md) |
| Together | OpenAI Chat | [获取凭证](https://api.together.ai/settings/api-keys) | — |
| Fireworks | OpenAI Chat | [获取凭证](https://fireworks.ai/account/api-keys) | — |
| nvidia | OpenAI Chat | [控制台](https://build.nvidia.com/explore/discover) | — |
| Grok | OpenAI Chat | [官网](https://x.ai/) | [配置](grok.md) |
| Hyperbolic | OpenAI Chat | [获取凭证](https://app.hyperbolic.xyz/settings) | — |
| Mistral | OpenAI Chat | [获取凭证](https://console.mistral.ai/api-keys/) | — |
| Jina | OpenAI Chat | [官网](https://jina.ai) | — |
| Perplexity | OpenAI Chat | [获取凭证](https://www.perplexity.ai/settings/api) | — |
| Xirang | OpenAI Chat | [控制台](https://huiju.ctyun.cn/service/serviceGroup) | — |
| hunyuan | OpenAI Chat | [获取凭证](https://console.cloud.tencent.com/hunyuan/api-key) | — |
| Tencent Cloud TI | OpenAI Chat | [获取凭证](https://console.cloud.tencent.com/lkeap/api) | — |
| Baidu Cloud | OpenAI Chat | [获取凭证](https://console.bce.baidu.com/iam/#/iam/apikey/list) | — |
| VoyageAI | OpenAI Chat | [获取凭证](https://dashboard.voyageai.com/organization/api-keys) | — |
| Poe | OpenAI Chat | [获取凭证](https://poe.com/api/keys) | — |
| Hugging Face | OpenAI Responses | [获取凭证](https://huggingface.co/settings/tokens) | — |
| Vercel AI Gateway | OpenAI Chat | [官网](https://vercel.com/) | — |
| Cerebras AI | OpenAI Chat | [控制台](https://cloud.cerebras.ai) | — |

## 专用接入模板

这几项不是普通的 API Key + Base URL 组合。请按页面字段准备对应云平台信息。

| Provider | 鉴权或连接方式 | 凭证入口 | 专题 |
|---|---|---|---|
| Azure OpenAI | Azure 凭证、API Version、部署信息 | [Azure Portal](https://portal.azure.com/) | [配置](azure-openai.md) |
| VertexAI | Google Cloud 项目、区域与凭证 | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) | [配置](vertex-ai.md) |
| GPUStack | GPUStack 服务地址与凭证 | [官网](https://gpustack.ai/) | — |
| AWS Bedrock | AWS 区域与 IAM 或 Bedrock API Key | [IAM 文档](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html) | — |

{% hint style="warning" %}
服务商可能调整注册地址、模型权限、地区限制和计费规则。创建凭证前请阅读该平台最新说明；Cherry Studio 只负责连接，不代替服务商提供账户或额度。
{% endhint %}

## 列表中没有目标服务

- 自建 New API：使用 [New API](newapi.md) 模板；
- 自建 One API 或其他兼容网关：参考 [OneAPI](oneapi.md) 或[自定义服务商](zi-ding-yi-fu-wu-shang.md)；
- 仅有 OpenAI、Anthropic、Gemini 或 OpenAI Responses 兼容地址：直接创建[自定义服务商](zi-ding-yi-fu-wu-shang.md)并填写对应端点。

如果模板名称存在，但你的部署地址与默认值不同，可以复制该服务商，再修改副本的地址和鉴权配置。

遇到问题时，请先按[模型服务](README.md#常见问题)检查服务商开关、模型开关、API Key、Base URL 和接口类型。
