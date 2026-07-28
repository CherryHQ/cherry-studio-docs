---
icon: cloud-plus
---

# 模型服务配置

Cherry Studio 内置 60+ 家 Provider（模型服务商）的连接模板，覆盖国内外大部分主流模型与本地推理框架。本节为每家 Provider 提供独立配置指南。

{% hint style="info" %}
**Provider（模型服务商）** 提供真正生成回答的模型。Cherry Studio 负责连接和使用这些模型，但不是模型本身。
{% endhint %}

## 第一次使用该选哪个？

| 你的情况 | 推荐选择 |
|---|---|
| 只想尽快完成第一次对话 | [CherryIN](cherryai/README.md)，按客户端当前提示登录或授权 |
| 已经有服务商 API Key | 选择 DeepSeek、OpenAI、Gemini、Anthropic 等对应 Provider |
| 使用第三方中转或自建网关 | [自定义服务商](zi-ding-yi-fu-wu-shang.md)，按网关协议选择 OpenAI / Anthropic / Gemini 兼容类型 |
| 希望模型在本机运行 | [Ollama](ollama.md) 或 [LM Studio](lm-studio.md) |

API Key 属于敏感凭据，不要放进截图、公开文档、群聊或 Git 仓库。怀疑泄露时立即到服务商后台撤销。

### Provider 类型

Cherry Studio 把 Provider 按协议分为以下几类，行为略有差异：

| 类型 | 兼容协议 | 典型代表 |
|---|---|---|
| **OpenAI 兼容** | `/v1/chat/completions` | OpenAI、DeepSeek、硅基流动、OpenRouter、绝大多数三方网关 |
| **Anthropic 兼容** | `/v1/messages` | Anthropic、CherryIN、部分网关 |
| **Gemini** | Google AI Studio / Vertex | Google Gemini、Vertex AI |
| **Bedrock** | AWS Bedrock SDK | AWS Bedrock |
| **Azure OpenAI** | Azure OpenAI Service | Azure OpenAI |
| **本地推理** | 本地 HTTP 服务 | Ollama、LM Studio、GPUStack、OpenVINO Model Server |
| **特殊网关** | 厂商私有协议 | NewAPI、OneAPI、AiHubMix、DMXAPI 等 |

### 添加一个 Provider 的通用步骤

1. 打开 `设置 → 模型服务`
2. 在内置 Provider 列表中找到目标 Provider，点击进入详情页
3. 填写 **API 密钥**（必填），按需修改 **API 地址**（默认是 Provider 官方地址）
4. 点击 **获取模型列表**，按需添加你常用的对话/嵌入/视觉模型
5. （可选）点击 **检测**，用任一对话模型验证连接是否成功

### 成功标志

* 页面能获取到模型列表；
* 至少一个对话模型处于启用状态；
* 点击 **检测** 后返回成功结果；
* 回到对话页选择该模型，可以收到正常回复。

如果检测失败，请优先检查 API Key、API 地址、账户余额和当前网络。不要通过反复修改高级参数来排查最基本的连接问题。

### Provider 配置详解

#### 通用/网关类
* [CherryIN](cherryai/)
* [NewAPI](newapi.md) / [OneAPI](oneapi.md) — 自建/三方网关

#### 海外厂商
* [OpenAI](openai.md)
* [Google Gemini](google-gemini.md)
* [Vertex AI](vertex-ai.md)
* [GitHub Copilot](github-copilot.md)
* [MiniMax Coding Plan](minimax-coding-plan.md)

#### 国内厂商
* [阿里云百炼](a-li-yun-bai-lian.md)
* [硅基流动](siliconcloud.md)
* [火山引擎（豆包）](doubao.md)
* [华为云](huawei.md)
* [无问芯穹](wu-wen-xin-qiong.md)
* [PPIO 派欧云](ppio.md)
* [ModelScope（魔搭）](modelscope.md)

#### 本地推理
* [Ollama](ollama.md)

#### 自定义服务商
* [自定义服务商](zi-ding-yi-fu-wu-shang.md) — 任意 OpenAI / Anthropic / Gemini 兼容端点

{% hint style="info" %}
**没找到你用的 Provider 怎么办？**

Cherry Studio 内置的 Provider 模板多于本节已经收录的专题页。

* 先在 **设置 → 模型服务** 中搜索 Provider 名称；
* 找到后直接填写密钥并获取模型列表；
* 没有内置模板时，使用 [自定义服务商](zi-ding-yi-fu-wu-shang.md) 连接兼容端点。

Anthropic、Azure OpenAI、DeepSeek、Grok、Groq、LM Studio、OpenRouter、Mistral、Perplexity 和 Together 等均可按上述方式配置。
{% endhint %}

### API 密钥与 API 地址

详见 [模型服务设置](../settings/providers.md)（含 多 Key 轮询、`#` 结尾固定路径等高级用法）。

## 下一步

完成模型检测后，返回[快速开始](../../getting-started/quick-start.md)发送第一条测试消息。只有需要知识库时才配置嵌入模型；只有需要绘画时才配置图像生成模型。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
