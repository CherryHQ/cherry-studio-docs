---
icon: cloud-plus
---

# 模型服务配置

Cherry Studio v1.9.x 内置 60+ 家 Provider（模型服务商）的连接模板，覆盖国内外大部分主流模型与本地推理框架。本节为每家 Provider 提供独立配置指南。

### Provider 类型

Cherry Studio 把 Provider 按协议分为以下几类，行为略有差异：

| 类型 | 兼容协议 | 典型代表 |
|---|---|---|
| **OpenAI 兼容** | `/v1/chat/completions` | OpenAI、DeepSeek、硅基流动、OpenRouter、绝大多数三方网关 |
| **Anthropic 兼容** | `/v1/messages` | Anthropic、CherryIN、部分网关。**Cherry Agent 需要此类型** |
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

### Provider 配置详解

#### 通用/网关类
* [CherryAI (免费)](cherryai/)
* [CherryIN](cherryin-1.md) — 双端点（OpenAI + Anthropic），Cherry Agent 推荐
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

Cherry Studio 内置 60+ Provider 模板，但**远多于本节文档已收录**的数量。如果你用的是 Anthropic（Claude）、Azure OpenAI、DeepSeek 官方、Grok、Groq、LM Studio、OpenRouter、Mistral、Perplexity、Together 等，**它们都在 Provider 列表里**，直接添加密钥即可。本节文档将分批补齐这些 Provider 的专题页。
{% endhint %}

### API 密钥与 API 地址

详见 [模型服务设置](../settings/providers.md)（含 多 Key 轮询、`#` 结尾固定路径等高级用法）。
