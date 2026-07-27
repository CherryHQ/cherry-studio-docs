---
icon: whale
---

# DeepSeek

Cherry Studio V2 的 DeepSeek 内置模板用于连接 DeepSeek 官方 API。当前模板默认使用 **OpenAI Chat Completions**，同时包含 DeepSeek 官方 Anthropic 兼容端点，并针对 DeepSeek V4 的思考开关与推理强度做了适配。

{% hint style="info" %}
如果只想先体验模型，可以使用 Cherry Studio 内置的 [CherryAI 免费试用](cherryai/README.md)。本页适用于已拥有 DeepSeek 官方 API Key 的用户。
{% endhint %}

## 开始前准备

- 可登录 [DeepSeek 开放平台](https://platform.deepseek.com/)的账户；
- 在 [API Keys](https://platform.deepseek.com/api_keys) 创建的 API Key；
- 账户具有可用余额或配额；
- 已确认当前可用模型和官方 API 变更。

DeepSeek 网页端或 App 的登录状态不会自动写入 Cherry Studio。调用官方 API 需要单独创建 API Key。

## 配置 DeepSeek

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **deepseek**；
3. 输入 DeepSeek API Key；
4. 保留默认 Base URL `https://api.deepseek.com`；
5. 打开页面顶部的服务商开关；
6. 在模型列表点击**添加**，检查同步预览并应用变更；
7. 启用准备使用的模型。

{% hint style="danger" %}
不要把 API Key 写入聊天消息、文档、代码仓库或问题截图。泄露后应立即在 DeepSeek 开放平台删除并重新创建。
{% endhint %}

## 选择当前模型

DeepSeek 官方当前提供以下主要模型 ID：

| 模型 ID | 适合场景 |
| --- | --- |
| `deepseek-v4-flash` | 日常对话、快速任务、对延迟敏感的工作 |
| `deepseek-v4-pro` | 复杂推理、代码、长上下文和 Agent 任务 |

旧模型别名 `deepseek-chat` 和 `deepseek-reasoner` 已在 2026 年 7 月停止提供。若旧配置返回模型不存在，请重新点击**添加**同步列表，改用当前 V4 模型 ID。

{% hint style="warning" %}
模型列表和生命周期可能继续变化。请以 [DeepSeek API 文档](https://api-docs.deepseek.com/)和实际同步结果为准，不要依赖旧截图中的固定模型名。
{% endhint %}

## 设置思考模式

DeepSeek V4 同时支持思考与非思考模式，并默认启用思考。Cherry Studio 会在输入框的思考按钮中显示适用选项：

- **默认**：使用服务商默认行为；
- **关闭**：发送禁用思考参数；
- **高**：使用 DeepSeek 的 `high` 推理强度；
- **穷究**：映射为 DeepSeek 的 `max` 推理强度。

`穷究` 通常会消耗更多推理时间和 Token。日常问答可先使用默认或关闭；复杂代码、规划和 Agent 任务再提高强度。

思考模式下，部分采样参数可能不生效。遇到结果差异时，先保持默认参数，只调整思考开关和强度。

## 工具调用与 Agent

DeepSeek V4 支持思考模式下的工具调用，Cherry Studio 也会保留工具调用过程所需的思考内容。使用前仍应完成实际测试：

1. 启用一个简单 MCP 工具；
2. 选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`；
3. 先使用默认思考强度；
4. 发出明确需要工具的请求；
5. 确认模型实际调用工具，而不是只输出调用计划。

若连续工具调用返回 400，先更新 Cherry Studio 与模型列表，再检查网关是否真的是 DeepSeek 官方端点。

## 检查连接

1. 在 API Key 区域运行连接检查；
2. 选择一个已同步并启用的 V4 模型；
3. 确认检查成功；
4. 在模型列表运行健康检查；
5. 回到对话界面发送一条简单消息；
6. 再分别测试思考模式和工具调用。

连接检查成功不代表账户有无限配额，也不代表所有模型都已开放。

## 知识库与嵌入模型

DeepSeek 内置模板当前只配置对话端点，不提供嵌入模型。使用[全局记忆](../../advanced-basic/memory.md)或知识库时：

- 对话模型可以继续选择 DeepSeek；
- 嵌入模型需要从其他服务商选择；
- 嵌入模型和对话模型不必来自同一家服务商；
- 配置完成后分别运行模型健康检查。

## 连接 DeepSeek 兼容网关

如果使用的不是 DeepSeek 官方 API：

1. 新建[自定义服务商](zi-ding-yi-fu-wu-shang.md)；
2. 按网关文档选择 OpenAI Chat Completions 或 Anthropic Messages；
3. 填写网关提供的 Base URL 和 API Key；
4. 同步或手动添加网关实际提供的模型 ID；
5. 验证思考参数和工具调用是否被网关完整支持。

不要直接覆盖 DeepSeek 官方模板。独立服务商更容易区分官方账户、第三方模型名和协议差异。

## 常见问题

### 返回 401

API Key 无效、已删除或复制不完整。重新创建 Key，并确认没有多余空格。

### 返回余额或配额错误

到 DeepSeek 开放平台检查余额、用量和账户状态。切换模型不会绕过账户级限制。

### 返回 404 或模型不存在

重新点击**添加**同步模型，并确认使用 `deepseek-v4-flash` 或 `deepseek-v4-pro`。旧别名已经停止提供。

### 返回 429 或服务器繁忙

当前请求达到速率限制或服务暂时拥塞。稍后重试，减少并发，或检查账户限制。

### 思考按钮没有显示完整选项

确认模型 ID 是当前 V4 ID，并重新同步模型。手动添加时不要修改模型 ID；显示名称可以自定义。

### 工具调用只输出文字

确认模型支持工具调用、MCP 已启用，并使用 DeepSeek 官方端点或明确支持完整工具协议的网关。先用单个简单工具排查。

更多通用设置见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
