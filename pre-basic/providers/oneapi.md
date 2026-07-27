---
icon: shuffle
---

# OneAPI

OneAPI 是一个把多个上游大模型渠道转换为 OpenAI 兼容接口的网关。管理员在 OneAPI 中配置上游 Key、模型和路由，普通用户使用 OneAPI 发放的令牌连接 Cherry Studio。

Cherry Studio V2 没有单独的 OneAPI 内置服务商；OneAPI 与 NewAPI 共用 **New API** 兼容适配。对于标准 OneAPI 实例，模型端点类型通常选择 **OpenAI Chat Completions**。

{% hint style="warning" %}
请求会经过 OneAPI 实例及其上游渠道。只使用自己部署或明确可信、具有合法上游授权与合规责任的服务。来源不明的公共实例可能记录请求、泄露附件或错误计费。
{% endhint %}

## OneAPI 与 NewAPI 的区别

OneAPI 是较早的统一网关项目，NewAPI 在类似架构上继续扩展了更多原生协议、端点类型和模型元数据。

| 项目 | 在 Cherry Studio 中的建议 |
| --- | --- |
| OneAPI | 使用 New API 兼容服务商，默认按 OpenAI Chat Completions 处理 |
| NewAPI | 使用专用 New API 类型，并按模型选择 Chat、Responses、Anthropic、Gemini、图片或 Rerank |

如果实例经过二次开发或主题定制，不能只凭页面外观判断它属于哪个项目。向管理员确认服务器版本和支持的 API 协议。

## 先确认你的角色

普通用户只需要实例地址和用户令牌。管理员还需要维护上游渠道：

| 角色 | 准备工作 |
| --- | --- |
| 普通用户 | 创建专用令牌，确认额度、分组和模型权限 |
| 管理员 | 配置上游渠道、模型映射、倍率、分组与故障切换 |

不要把 OpenAI、Anthropic 等上游厂商 Key 直接填到 Cherry Studio 的 OneAPI 连接中。客户端应使用 OneAPI 发放的令牌。

## 在 OneAPI 创建令牌

1. 登录可信的 OneAPI 实例；
2. 打开**令牌**页面；
3. 新建一个专供 Cherry Studio 使用的令牌；
4. 按需设置名称、额度、有效期和可用模型；
5. 复制令牌并妥善保存；
6. 使用 OneAPI 自带的测试功能验证一个模型。

不建议长期共用默认令牌。独立令牌更容易审计用量、设置上限和单独撤销。

{% hint style="danger" %}
不要把 OneAPI 令牌写入聊天消息、文档、代码仓库或问题截图。泄露后应立即在 OneAPI 控制台删除并重新创建。
{% endhint %}

## 获取 API Base URL

OneAPI 官方 OpenAI 兼容格式通常使用：

```text
https://your-oneapi.example.com/v1
```

Cherry Studio 的 New API 兼容适配会为站点根地址补齐 `/v1`，所以以下两种写法都可以：

- `https://your-oneapi.example.com`
- `https://your-oneapi.example.com/v1`

本地或局域网部署也可以使用：

- `http://localhost:3000`
- `http://192.168.1.20:3000`

注意：

- `http` 与 `https` 必须和服务器实际配置一致；
- 公网服务应使用有效 HTTPS 证书；
- `/console/...`、登录页和令牌页不是 API Base URL；
- 不要填写具体的 `/chat/completions` 路径。

## 在 Cherry Studio 配置

如果没有使用其他 NewAPI 网关，可以直接配置内置 **New API**；如果已有其他实例，先复制或新增一个 New API 兼容服务商，避免覆盖原配置。

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **New API**，或新增一个以 New API 为模板的服务商；
4. 将名称改为易识别的 OneAPI 实例名称；
5. 输入 OneAPI 用户令牌；
6. 填写 OneAPI Base URL；
7. 打开页面顶部的服务商开关；
8. 点击**添加**同步模型列表；
9. 将标准 OneAPI 模型的端点类型设为 **OpenAI Chat Completions**；
10. 只启用准备使用的模型。

OneAPI 的 `/models` 响应通常不会提供 NewAPI 新版本中的 `supported_endpoint_types`。Cherry Studio 因此可能要求你在批量添加时选择端点类型，这是正常现象。

## 添加模型

优先从服务器同步模型，不要照抄其他实例的模型名称。

如果同步失败，可以手动添加：

1. 在 OneAPI 控制台确认令牌可见的完整模型 ID；
2. 在 Cherry Studio 点击**添加模型**；
3. 输入完全相同的模型 ID；
4. 端点类型选择 **OpenAI Chat Completions**；
5. 保存并运行健康检查。

模型显示名称可以自定义，但实际模型 ID 必须和 OneAPI 的可用模型或映射名称一致。

{% hint style="info" %}
OneAPI 会把客户端请求的模型 ID 映射到上游模型。模型不存在时，应同时检查 Cherry Studio 中的 ID、OneAPI 渠道模型和管理员配置的模型映射。
{% endhint %}

## 能力边界

OneAPI 主要把不同上游统一成 OpenAI 兼容格式。基础对话通常最稳定，较新的原生能力不一定完整保留。

- Claude 的原生 thinking block 可能被转换或丢失；
- Gemini 的原生多模态结构可能受实例版本限制；
- OpenAI Responses 专属能力不等同于 Chat Completions；
- 工具调用需要 OneAPI 与上游都正确转换 `tools` 和 `tool_calls`；
- 联网、缓存、服务层级等厂商专属参数可能不生效；
- 模型列表可见不代表所有参数组合都可用。

若工作流依赖某个厂商的最新原生能力，优先使用模型原厂服务商或支持对应原生端点的新版本 NewAPI。

## 工具调用与 MCP

可以使用支持 Function Calling 的 OneAPI 模型连接 MCP，但应先做最小测试：

1. 选择明确支持工具调用的模型；
2. 完成一轮普通对话；
3. 只启用一个简单 MCP 工具；
4. 明确要求模型调用该工具；
5. 确认 OneAPI 日志中出现工具请求；
6. 再增加更多工具。

如果模型只输出调用计划，可能是上游模型不支持工具、OneAPI 转换不完整，或渠道把工具字段删除。先在 OneAPI 中直接测试同一模型。

## 知识库与嵌入模型

当 OneAPI 实例开放兼容的 Embeddings 接口时，可把嵌入模型用于知识库或[全局记忆](../../advanced-basic/memory.md)。

- 只添加实例实际提供的嵌入模型；
- 不要把对话模型当作嵌入模型；
- 对话和嵌入可以使用不同服务商；
- 分别运行健康检查；
- 核对 OneAPI 与上游的计费倍率。

旧实例或特定渠道可能没有嵌入接口。模型名称存在不代表 `/v1/embeddings` 可用。

## PDF 与附件

OneAPI 属于聚合网关，Cherry Studio 不会仅根据模型名称假设它支持原生 PDF。

当前 V2 会先在本地提取 PDF 文本，再发送到 OneAPI：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用输入 Token；
- 图片等多模态附件仍取决于实例和上游能力。

## 管理员检查清单

向用户发放令牌前，建议管理员确认：

1. 上游渠道测试成功；
2. 渠道启用的模型与实际权限一致；
3. 模型映射没有拼写错误；
4. 用户分组能访问目标渠道；
5. 模型倍率和分组倍率正确；
6. 令牌限制与用户用途匹配；
7. `/v1/models` 和 `/v1/chat/completions` 均可用；
8. 关键模型完成工具调用测试。

多渠道负载均衡时，同一个模型可能路由到不同上游。需要稳定行为时，减少不一致的渠道，或由管理员按 OneAPI 支持的方式固定渠道。

## 检查连接

1. 在 OneAPI 自带测试或兼容请求中验证同一令牌；
2. 在 Cherry Studio 运行服务商连接检查；
3. 点击**添加**确认模型列表可同步；
4. 检查端点类型是 OpenAI Chat Completions；
5. 运行模型健康检查；
6. 回到对话界面发送一条简单消息；
7. 再测试工具调用、附件或知识库。

服务器端也失败时，优先检查 OneAPI 渠道、令牌和上游；仅 Cherry Studio 失败时，重点检查 Base URL、模型 ID 与端点类型。

## 常见问题

### 返回 401

令牌无效、已删除、过期或复制不完整。确认填写的是 OneAPI 用户令牌，不是上游厂商 Key。

### 返回 403

令牌没有目标模型权限、额度已耗尽，或分组无法访问可用渠道。联系实例管理员检查。

### 返回 404

Base URL 填入了后台页面或具体接口路径，或者实例未开放标准 OpenAI 兼容路由。恢复为站点根地址或 `/v1`。

### 模型列表为空

令牌没有可见模型、渠道未启用、分组不匹配，或实例版本的 `/models` 响应不兼容。先在 OneAPI 中测试并确认 `/v1/models`。

### 模型存在但调用失败

检查 OneAPI 模型映射与上游渠道。列表中的模型名只是入口，实际路由仍可能找不到或无权限。

### 思考内容、联网或工具能力缺失

OneAPI 的 OpenAI 格式转换可能未保留厂商原生字段。用简单 Chat Completions 功能对比；需要完整原生能力时改用原厂服务商或 NewAPI 的对应端点。

### 请求结果时好时坏

多个渠道的模型版本、参数支持或余额不一致。请管理员检查渠道测试、优先级、权重和自动禁用状态。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。若实例实际为 NewAPI，请改看 [NewAPI](newapi.md)；OneAPI 项目说明见[官方仓库](https://github.com/songquanpeng/one-api)。意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
