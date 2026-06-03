# OpenRouter

OpenRouter 是一个**统一网关**，用一把 key 接入 200+ 家厂商的对话模型（GPT、Claude、Gemini、Llama、DeepSeek 等），按 token 转计费，适合多模型对比 / 没法一一注册各家账号的用户。

## 获取 API Key

* 前往 [OpenRouter](https://openrouter.ai/) 注册账号
* `Settings → Keys` → `Create Key`，复制 `sk-or-...` 密钥
* 充值任意金额（最低 $1）

## 在 Cherry Studio 配置

* 打开 `设置 → 模型服务`，找到 **OpenRouter** Provider 进入详情页
* **API 密钥** 填入 `sk-or-...`
* **API 地址** 默认 `https://openrouter.ai/api`，无需修改
* 点击 **获取模型列表**，OpenRouter 会返回数百个可用模型

## 推荐用法

OpenRouter 的模型 ID 形如 `<vendor>/<model>`：

| 模型 ID 示例 | 实际是谁 |
|---|---|
| `openai/gpt-4o` | OpenAI GPT-4o |
| `anthropic/claude-sonnet-4` | Anthropic Claude Sonnet 4 |
| `google/gemini-2.0-flash` | Google Gemini Flash |
| `meta-llama/llama-3.3-70b-instruct` | Meta Llama 3.3 70B |
| `deepseek/deepseek-chat` | DeepSeek V3 |
| `x-ai/grok-4` | xAI Grok |

## 适用场景

* **多模型 A/B 对比**：在同一 Cherry Studio Provider 下随意切模型，无需切 Provider
* **避免一一注册**：一个 key 一个发票就能用 200+ 模型
* **冷门模型**：很多小厂商只在 OpenRouter 上提供（如 Cohere、Reka 等）

## 与 Anthropic 协议的关系

OpenRouter 默认走 OpenAI 协议格式封装所有上游模型。这意味着：

* ✅ 普通对话、知识库、快捷助手都可用
* ⚠️ [Cherry Agent](../../advanced-basic/agent.md) **建议直接用** Anthropic / CherryIN，不要走 OpenRouter（Agent 需要 Anthropic 原生协议）

{% hint style="info" %}
* OpenRouter 在原厂价格基础上有少量加价（通常 5-10%），换来"一个账号通用"
* 部分模型可走 "free" 版本（免费有限速），筛选时注意带 `(free)` 后缀的条目
* 详细价格表见 [OpenRouter Models](https://openrouter.ai/models)
{% endhint %}
