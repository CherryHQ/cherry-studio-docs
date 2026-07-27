---
icon: list
---

# All Providers quick reference

This page lists the model service templates currently built into Cherry Studio V2 so you can confirm provider names, preset APIs, and credential entry points. The list changes as the app is updated. If this page differs from the client, use the providers displayed under `Settings → Model Services → All Providers`.

{% hint style="info" %}
“API” on this page refers to the connection method that Cherry Studio presets for a template. It does not mean every model from that provider supports the same capabilities. Check the provider's model documentation and test the model to confirm support for vision, reasoning, and tool calling.
{% endhint %}

## How to use this table

1. Find a provider for which you already have an account or plan to connect;
2. Open the **Credentials** link and create an API Key or cloud account credentials as required by the provider;
3. Return to `Settings → Model Services`, switch the filter on the left to **All Providers**, and select the provider with the same name;
4. Follow the steps under [Model Services](README.md) to complete authentication, fetch models, enable models, and check the connection.

If a provider is not listed but offers a compatible API, use [Custom Provider](zi-ding-yi-fu-wu-shang.md).

## API names

| Short name | Corresponding API |
|---|---|
| OpenAI Chat | OpenAI Chat Completions |
| OpenAI Responses | OpenAI Responses |
| Anthropic | Anthropic Messages |
| Gemini | Google Generate Content |
| Ollama | Ollama Chat |
| Dedicated integration | Cherry Studio uses authentication and routing specific to the cloud platform or service |

The **Agent Supported** filter in the list on the left displays providers with an Anthropic-compatible endpoint. It only filters by connection method and does not guarantee that every model can call tools.

## Multi-API templates

These templates preset two APIs. You can choose the appropriate connection method for different models under the same provider.

| Provider | Preset APIs | Credentials | Guide |
|---|---|---|---|
| CherryIN | Anthropic, OpenAI Chat | [Get credentials](https://open.cherryin.ai/console/token) | [Setup](cherryin-1.md) |
| Silicon | Anthropic, OpenAI Chat | [Get credentials](https://cloud.siliconflow.cn/) | [Setup](siliconcloud.md) |
| AiHubMix | Anthropic, OpenAI Chat | [Get credentials](https://aihubmix.com) | — |
| ZhiPu | Anthropic, OpenAI Chat | [Get credentials](https://open.bigmodel.cn/usercenter/apikeys) | — |
| deepseek | Anthropic, OpenAI Chat | [Get credentials](https://platform.deepseek.com/api_keys) | [Setup](deepseek.md) |
| DMXAPI | Anthropic, OpenAI Chat | [Get credentials](https://www.dmxapi.cn/) | — |
| TokenFlux | Anthropic, OpenAI Chat | [Get credentials](https://api.tokenflux.ai/dashboard/api-keys) | — |
| 302.AI | Anthropic, OpenAI Chat | [Get credentials](https://dash.302.ai/apis/list) | — |
| Qiniu | Anthropic, OpenAI Chat | [Get credentials](https://portal.qiniu.com/ai-inference/api-key) | — |
| OpenRouter | Anthropic, OpenAI Chat | [Get credentials](https://openrouter.ai/settings/keys) | [Setup](openrouter.md) |
| Ollama | Anthropic, Ollama | [Website](https://ollama.com/) | [Setup](ollama.md) |
| New API | Anthropic, OpenAI Chat | [Docs](https://docs.newapi.pro/) | [Setup](newapi.md) |
| LM Studio | Anthropic, OpenAI Chat | [Website](https://lmstudio.ai/) | [Setup](lm-studio.md) |
| Moonshot AI | Anthropic, OpenAI Chat | [Get credentials](https://platform.moonshot.cn/console/api-keys) | [Setup](moonshot.md) |
| Bailian | Anthropic, OpenAI Chat | [Get credentials](https://bailian.console.aliyun.com/?tab=model#/api-key) | [Setup](a-li-yun-bai-lian.md) |
| MiniMax | Anthropic, OpenAI Chat | [Get credentials](https://platform.minimaxi.com/user-center/basic-information/interface-key) | [Setup](minimax.md) |
| ModelScope | Anthropic, OpenAI Chat | [Get credentials](https://modelscope.cn/my/myaccesstoken) | [Setup](modelscope.md) |
| LongCat | Anthropic, OpenAI Chat | [Get credentials](https://longcat.chat/platform/api_keys) | — |
| Xiaomi MiMo | Anthropic, OpenAI Chat | [Get credentials](https://platform.xiaomimimo.com/#/console/usage) | — |
| zai | Anthropic, OpenAI Chat | [Get credentials](https://z.ai/manage-apikey/apikey-list) | — |
| minimax-global | Anthropic, OpenAI Chat | [Get credentials](https://platform.minimax.io/user-center/basic-information/interface-key) | — |

## Single-API templates

| Provider | Preset API | Credentials | Guide |
|---|---|---|---|
| OpenVINO Model Server | OpenAI Chat | [Website](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html) | — |
| ocoolAI | OpenAI Chat | [Get credentials](https://one.ocoolai.com/token) | — |
| AlayaNew | OpenAI Chat | [Website](https://www.alayanew.com/) | — |
| AIOnly | OpenAI Chat | [Get credentials](https://maas.aiionly.com/keyApi) | — |
| BurnCloud | OpenAI Chat | [Get credentials](https://ai.burncloud.com/token) | — |
| Cephalon | OpenAI Chat | [Get credentials](https://cephalon.cloud/api) | — |
| LANYUN | OpenAI Chat | [Get credentials](https://maas.lanyun.net/#/system/apiKey) | — |
| PH8 | OpenAI Chat | [Get credentials](https://ph8.co/apiKey) | — |
| SophNet | OpenAI Chat | [Get credentials](https://sophnet.com/#/project/key) | — |
| PPIO | OpenAI Chat | [Get credentials](https://ppio.com/settings/key-management) | [Setup](ppio.md) |
| Anthropic | Anthropic | [Get credentials](https://console.anthropic.com/settings/keys) | [Setup](anthropic.md) |
| OpenAI | OpenAI Responses | [Get credentials](https://platform.openai.com/api-keys) | [Setup](openai.md) |
| Gemini | Gemini | [Get credentials](https://aistudio.google.com/app/apikey) | [Setup](google-gemini.md) |
| Github Models | OpenAI Chat | [Get credentials](https://github.com/settings/tokens) | — |
| Github Copilot | OpenAI Chat | [Website](https://github.com/features/copilot) | [Setup](github-copilot.md) |
| Yi | OpenAI Chat | [Get credentials](https://platform.lingyiwanwu.com/apikeys) | — |
| BAICHUAN AI | OpenAI Chat | [Get credentials](https://platform.baichuan-ai.com/console/apikey) | — |
| StepFun | OpenAI Chat | [Get credentials](https://platform.stepfun.com/interface-key) | — |
| doubao | OpenAI Chat | [Console](https://www.volcengine.com/experience/ark) | [Setup](doubao.md) |
| Infini | OpenAI Chat | [Get credentials](https://cloud.infini-ai.com/iam/secret/key) | — |
| Groq | OpenAI Chat | [Get credentials](https://console.groq.com/keys) | [Setup](groq.md) |
| Together | OpenAI Chat | [Get credentials](https://api.together.ai/settings/api-keys) | — |
| Fireworks | OpenAI Chat | [Get credentials](https://fireworks.ai/account/api-keys) | — |
| nvidia | OpenAI Chat | [Console](https://build.nvidia.com/explore/discover) | — |
| Grok | OpenAI Chat | [Website](https://x.ai/) | [Setup](grok.md) |
| Hyperbolic | OpenAI Chat | [Get credentials](https://app.hyperbolic.xyz/settings) | — |
| Mistral | OpenAI Chat | [Get credentials](https://console.mistral.ai/api-keys/) | — |
| Jina | OpenAI Chat | [Website](https://jina.ai) | — |
| Perplexity | OpenAI Chat | [Get credentials](https://www.perplexity.ai/settings/api) | — |
| Xirang | OpenAI Chat | [Console](https://huiju.ctyun.cn/service/serviceGroup) | — |
| hunyuan | OpenAI Chat | [Get credentials](https://console.cloud.tencent.com/hunyuan/api-key) | — |
| Tencent Cloud TI | OpenAI Chat | [Get credentials](https://console.cloud.tencent.com/lkeap/api) | — |
| Baidu Cloud | OpenAI Chat | [Get credentials](https://console.bce.baidu.com/iam/#/iam/apikey/list) | — |
| VoyageAI | OpenAI Chat | [Get credentials](https://dashboard.voyageai.com/organization/api-keys) | — |
| Poe | OpenAI Chat | [Get credentials](https://poe.com/api/keys) | — |
| Hugging Face | OpenAI Responses | [Get credentials](https://huggingface.co/settings/tokens) | — |
| Vercel AI Gateway | OpenAI Chat | [Website](https://vercel.com/) | — |
| Cerebras AI | OpenAI Chat | [Console](https://cloud.cerebras.ai) | — |

## Dedicated integration templates

These entries are not ordinary API Key + Base URL combinations. Prepare the corresponding cloud platform information shown in the fields on the page.

| Provider | Authentication or connection | Credentials | Guide |
|---|---|---|---|
| Azure OpenAI | Azure credentials, API Version, and deployment information | [Azure Portal](https://portal.azure.com/) | [Setup](azure-openai.md) |
| VertexAI | Google Cloud project, region, and credentials | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) | [Setup](vertex-ai.md) |
| GPUStack | GPUStack service URL and credentials | [Website](https://gpustack.ai/) | — |
| AWS Bedrock | AWS region and IAM or a Bedrock API Key | [IAM docs](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html) | — |

{% hint style="warning" %}
Providers may change registration URLs, model permissions, regional restrictions, and pricing rules. Read the platform's latest documentation before creating credentials. Cherry Studio only provides the connection and does not provide accounts or quota on a provider's behalf.
{% endhint %}

## The target service is not listed

- For a self-hosted New API instance, use the [New API](newapi.md) template;
- For a self-hosted One API instance or another compatible gateway, see [OneAPI](oneapi.md) or [Custom Provider](zi-ding-yi-fu-wu-shang.md);
- If you only have an OpenAI-, Anthropic-, Gemini-, or OpenAI Responses-compatible URL, create a [Custom Provider](zi-ding-yi-fu-wu-shang.md) directly and enter the corresponding endpoint.

If a matching template exists but your deployment URL differs from its default, duplicate the provider and edit the URL and authentication settings in the copy.

If you encounter a problem, first follow [Model Services](README.md#troubleshooting) to check the provider switch, model switch, API Key, Base URL, and API type.
