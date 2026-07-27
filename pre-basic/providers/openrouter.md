---
icon: route
---

# OpenRouter

OpenRouter 是多模型统一网关。Cherry Studio V2 的 OpenRouter 内置模板使用一组 API Key 同步 OpenRouter 的对话和嵌入模型，并针对推理内容、联网插件和模型能力做了适配。

{% hint style="warning" %}
OpenRouter 不是模型原厂。请求会经过 OpenRouter，并可能由多个上游推理服务商路由。使用敏感数据前，应在 OpenRouter 控制台检查隐私、日志和供应商路由策略。
{% endhint %}

## 开始前准备

- 可登录 [OpenRouter](https://openrouter.ai/)的账户；
- 在 [OpenRouter Keys](https://openrouter.ai/settings/keys) 创建的 API Key；
- 账户具有可用余额或免费模型配额；
- 已确认模型价格、上下文、工具与数据策略。

建议为 Cherry Studio 单独创建 Key，并在 OpenRouter 中设置合适的额度上限。这样更容易区分用量，也能降低密钥泄露后的风险。

## 配置 OpenRouter

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **OpenRouter**；
3. 输入 OpenRouter API Key；
4. 保留默认 Base URL `https://openrouter.ai/api/v1/`；
5. 打开页面顶部的服务商开关；
6. 在模型列表点击**添加**，检查同步预览并应用变更；
7. 只启用准备使用的模型。

{% hint style="danger" %}
不要把 API Key 写入聊天消息、文档、代码仓库或问题截图。泄露后应立即在 OpenRouter 中撤销并重新创建。
{% endhint %}

## 理解模型 ID

OpenRouter 模型 ID 通常使用 `<组织>/<模型>` 格式，例如：

| 类型 | 示例 |
| --- | --- |
| 固定模型 | `openai/gpt-oss-120b` |
| 厂商最新别名 | `~anthropic/claude-sonnet-latest` |
| 自动路由 | `openrouter/auto` |
| 免费路由 | `openrouter/free` |
| 免费变体 | 在具体模型 ID 后使用 `:free` |

- 完整模型 ID 决定上游模型和路由行为；
- `latest`、自动路由和免费路由的实际模型可能变化；
- 需要可重复结果时，选择固定版本而不是动态别名；
- 免费变体可能有速率、可用性或数据策略限制；
- 不要只根据显示名称判断价格与能力。

点击**添加**会同步当前模型，不必把几百个模型全部启用。优先保留团队实际使用的少量模型，模型选择器会更清晰。

## 对话与嵌入模型

Cherry Studio 会分别请求 OpenRouter 的对话模型和嵌入模型接口，并合并到同步结果。

- 对话模型可用于助手、翻译和普通聊天；
- 支持工具调用的模型可用于 MCP 或 Agent 场景；
- 嵌入模型可用于知识库和[全局记忆](../../advanced-basic/memory.md)；
- 同一个 Key 对不同模型的权限、价格和限制可能不同；
- 模型出现于列表，不代表每个上游供应商都可用。

为知识库选择模型时，确认它确实是嵌入模型，不要仅凭厂商名称判断。

## 设置思考模式

OpenRouter 会把不同模型的推理参数统一为 `reasoning` 配置。Cherry Studio 根据模型能力发送关闭、强度或预算设置，并保留跨轮工具调用需要的推理内容。

- 选择**默认**时，尽量使用 OpenRouter 或上游默认行为；
- 选择**关闭**时，向支持的模型发送禁用推理；
- 低、中、高等选项只会对支持相应强度的模型生效；
- 推理 Token 通常计入输出用量；
- 部分模型不会返回可见思考内容。

如果切换模型后思考按钮选项变化，这是正常现象。不要把一个模型的推理配置直接套用到所有模型。

## 使用联网

在对话输入框打开**联网**后，Cherry Studio V2 当前会为 OpenRouter 请求添加 Web Search 插件，并传入联网设置中的最大结果数。

使用步骤：

1. 选择一个 OpenRouter 模型；
2. 打开输入框中的**联网**；
3. 提出需要当前网页信息的问题；
4. 等待搜索和模型回答；
5. 展开并核对引用。

{% hint style="info" %}
OpenRouter 联网会产生额外搜索费用，即使底层模型是免费变体也可能收费。OpenRouter 正在从旧 Web 插件迁移到服务器端搜索工具；若联网突然不再可用，请先更新 Cherry Studio 并查看 OpenRouter 最新文档。
{% endhint %}

Perplexity Sonar 或 OpenAI Search 等自带搜索的模型可能具有不同的联网行为。模型本身是否强制联网，也由 OpenRouter 和上游能力决定。

## 工具调用与 Agent

OpenRouter 内置模板包含 OpenAI Chat Completions 与 Anthropic Messages 端点，但实际工具能力仍取决于模型和上游路由。

使用前：

1. 选择明确支持工具调用的模型；
2. 运行普通对话健康检查；
3. 启用一个简单 MCP 工具；
4. 确认模型实际发起调用；
5. 再增加多个工具或长链路 Agent。

若 Agent 稳定性不理想，可以对比模型原厂、Anthropic 或 CherryIN 的直连结果。OpenRouter 的统一入口很方便，但上游路由增加了一层变量。

## 隐私与上游路由

OpenRouter 默认会在可用上游之间路由以提高可用性。Cherry Studio 当前不会替你设置 OpenRouter 的全部供应商路由和隐私字段。

在 OpenRouter 控制台中检查：

- 是否启用输入输出日志；
- 是否允许 OpenRouter 使用输入输出；
- 是否限制可能保存数据的上游；
- 是否要求 Zero Data Retention；
- 是否允许 fallback；
- 组织或 Key 的模型与额度限制。

这些设置属于 OpenRouter 账户策略，不会因为 Cherry Studio 使用本地客户端而自动改变。

## 检查连接

1. 在 API Key 区域运行连接检查；
2. 选择一个已同步并启用的模型；
3. 确认检查成功；
4. 在模型列表运行健康检查；
5. 回到对话界面发送一条简单消息；
6. 再分别测试推理、联网和工具调用。

连接检查成功只说明基本凭据可用。具体模型仍可能因为余额、上游故障、隐私策略或参数不兼容而失败。

## 常见问题

### 返回 401

API Key 无效、已撤销或复制不完整。重新创建 Key，并确认没有多余空格。

### 返回余额或额度错误

检查 OpenRouter 余额、Key 限额和组织策略。免费模型也可能受到单独速率限制。

### 返回 404 或模型不存在

模型 ID 已变更、模型被移除，或动态别名当前不可用。重新点击**添加**同步列表，并在 [OpenRouter Models](https://openrouter.ai/models)核对。

### 返回 429

当前模型、上游供应商或 Key 达到速率限制。降低并发、稍后重试，或选择其他可用路由。

### 同一个模型结果或价格变化

动态别名、自动路由或上游 fallback 可能选择不同版本或供应商。需要稳定行为时使用固定模型 ID，并在 OpenRouter 控制台限制路由。

### 联网没有引用

确认输入框联网已打开，并检查 OpenRouter 搜索功能是否仍兼容当前 Cherry Studio 版本。搜索插件与模型自带搜索不是同一种机制。

### 工具调用不稳定

确认模型页面标记支持工具，并检查上游是否支持请求中的所有参数。可以换用固定供应商路由，或改用模型原厂连接对比。

更多通用设置见[模型服务](README.md)、[联网模式](../websearch/)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
