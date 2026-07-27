---
icon: bolt
---

# Groq

Groq 是以低延迟推理为特点的模型服务平台，提供多种开放权重模型和 Groq Compound 系统。Cherry Studio V2 的 Groq 内置模板使用 Groq 官方 OpenAI 兼容端点，并可同步账户当前可用的模型。

{% hint style="warning" %}
**Groq** 与 xAI 的 **Grok** 是两个独立服务商。Groq 提供模型推理平台；Grok 是 xAI 的模型系列。配置前请确认选中了正确条目。
{% endhint %}

## 开始前准备

- 可登录 [GroqCloud Console](https://console.groq.com/)的账户；
- 在 [Groq API Keys](https://console.groq.com/keys) 创建的 API Key；
- 账户具有可用额度和速率限制；
- 已确认准备使用的模型仍处于可用状态。

Groq 的模型清单和生命周期会调整。不要根据旧文档固定添加已经下线的模型。

## 配置 Groq

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **Groq**；
3. 输入 Groq API Key；
4. 保留默认 Base URL `https://api.groq.com/openai`；
5. 打开页面顶部的服务商开关；
6. 在模型列表点击**添加**，检查同步预览并应用变更；
7. 启用准备使用的模型。

{% hint style="danger" %}
不要把 API Key 写入聊天消息、文档、代码仓库或问题截图。泄露后应立即在 GroqCloud Console 撤销并重新创建。
{% endhint %}

## 同步并选择模型

点击**添加**后，Cherry Studio 会调用 Groq 的模型列表接口，并显示当前 Key 可访问的模型。模型变化较快，请以 [Groq Supported Models](https://console.groq.com/docs/models)和同步结果为准。

常见类型包括：

| 类型 | 示例模型 ID | 适合场景 |
| --- | --- | --- |
| 轻量文本模型 | `llama-3.1-8b-instant` | 低延迟问答、分类和简单抽取 |
| 大型通用模型 | `openai/gpt-oss-120b` | 复杂文本、代码和推理 |
| 其他托管模型 | `qwen/qwen3.6-27b` | 多语言、结构化输出和工具任务 |
| Compound 系统 | `groq/compound`、`groq/compound-mini` | Groq 服务器端搜索与代码执行 |

- 只启用实际需要的模型；
- 核对完整模型 ID，包括斜杠和大小写；
- 模型下线后应重新同步，不要只修改显示名称；
- 同一模型在不同计划下可能具有不同速率限制；
- 音频、语音或专用模型不一定适用于普通聊天。

## 设置服务层级

在对话的 Groq 设置中，可以选择**服务层级**：

| 选项 | 含义 |
| --- | --- |
| 忽略 | 不发送 `service_tier`，由 Groq 使用默认行为 |
| 自动 | 使用账户当前可用的合适层级 |
| 按需 | 使用常规按需处理 |
| 弹性 | 优先高吞吐，但容量不足时可能快速失败 |

服务层级是否生效取决于当前模型、账户计划和 Cherry Studio 的能力识别。不了解差异时保持**忽略**或**自动**。

{% hint style="info" %}
弹性处理可能在容量不足时返回 `498 capacity_exceeded`。它适合可重试的批量任务，不适合必须一次成功的交互请求。
{% endhint %}

## 使用 MCP 与工具调用

普通 Groq 托管模型可以按其能力使用 Cherry Studio 的 MCP 或其他工具：

1. 选择支持工具调用的模型；
2. 启用一个简单 MCP 工具；
3. 发出明确需要工具的请求；
4. 确认模型实际调用工具；
5. 再增加并行工具或复杂参数。

Groq Compound 是另一种机制：

- `groq/compound` 可在单次请求中使用多个 Groq 服务器端工具；
- `groq/compound-mini` 每次请求只使用一个服务器端工具，延迟更低；
- 搜索、访问网页和代码执行由 Groq 服务器完成；
- Compound 不等同于 Cherry Studio MCP，也不支持把用户自定义工具直接传给 Compound。

如果需要自建 MCP 工具，应选择支持本地工具调用的普通托管模型，而不是把 Compound 当成 MCP 执行器。

## 检查连接

1. 在 API Key 区域运行连接检查；
2. 选择一个已同步并启用的文本模型；
3. 确认检查成功；
4. 在模型列表运行健康检查；
5. 回到对话界面发送一条简单消息；
6. 若使用工具或 Compound，再分别测试相应能力。

连接检查成功只说明基本请求可用，不代表每个模型都具有相同上下文、工具和速率限制。

## 连接 Groq 兼容网关

如果使用的不是 Groq 官方 API：

1. 新建[自定义服务商](zi-ding-yi-fu-wu-shang.md)；
2. 将 OpenAI Chat Completions 设为主要端点；
3. 填写网关提供的 Base URL 和 API Key；
4. 同步或手动添加网关实际提供的模型；
5. 验证工具调用和服务层级是否受支持。

不要覆盖 Groq 官方模板。第三方网关也不会自动获得 Groq Compound 的服务器端工具。

## 常见问题

### 返回 401

API Key 无效、已撤销或复制不完整。重新创建 Key，并确认没有多余空格。

### 返回 404 或模型不存在

模型已经下线、模型 ID 输入错误，或当前账户没有访问权限。重新点击**添加**同步列表。

### 返回 429

请求达到模型或账户的速率限制。降低并发、稍后重试，并在 GroqCloud Console 检查限制。

### 返回 498

弹性层级当前没有可用容量。切换为自动、按需或忽略，或者为任务增加退避重试。

### 响应很快但内容被截断

检查模型的上下文和最大输出限制，并减少输入长度或调整最大输出 Token。推理速度不会改变模型自身限制。

### Compound 没有调用我的 MCP

Compound 使用 Groq 服务器端工具，不接受 Cherry Studio 的自定义 MCP 工具。请改用支持普通工具调用的托管模型。

### 服务层级没有变化

当前模型或账户可能不支持所选层级。保持忽略或自动，并以 GroqCloud Console 的实际请求记录为准。

更多通用设置见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
