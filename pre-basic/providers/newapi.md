---
icon: arrows-rotate
---

# NewAPI

NewAPI 是一个统一大模型网关。它在服务端连接 OpenAI、Anthropic、Google 等上游渠道，再向 Cherry Studio 提供统一的模型列表、鉴权、路由和计费接口。

Cherry Studio V2 已内置专用的 **New API** 服务商类型，不需要再把它伪装成普通 OpenAI 服务商。专用类型可以按模型选择 OpenAI Chat Completions、OpenAI Responses、Anthropic Messages、Google Generate Content、图像生成或重排序端点。

{% hint style="warning" %}
请求会经过 NewAPI 实例及其配置的上游渠道。只使用自己部署或明确可信、具有合法上游授权与合规责任的服务。不要把敏感数据和 API Key 交给来源不明的公共实例。
{% endhint %}

## 先确认你的角色

普通用户与 NewAPI 管理员的准备工作不同：

| 角色 | 在 NewAPI 中需要完成的工作 |
| --- | --- |
| 普通用户 | 创建令牌，确认额度、分组、模型权限和 IP 限制 |
| 管理员 | 先配置并测试上游渠道、模型映射、分组和计费，再向用户发放令牌 |

如果你只是使用别人维护的实例，不需要在 Cherry Studio 中填写上游厂商的 Key，只填写该 NewAPI 实例发放的用户令牌。

## 在 NewAPI 创建令牌

1. 登录可信的 NewAPI 实例；
2. 打开**令牌**页面；
3. 创建一个专供 Cherry Studio 使用的令牌；
4. 按需设置额度、有效期、模型限制、分组和 IP 白名单；
5. 复制令牌并妥善保存；
6. 在 NewAPI 自带的 Playground 中先测试一个模型。

建议为不同设备或用途创建独立令牌。发生泄露时可以只撤销受影响的令牌，也更容易核对用量。

{% hint style="danger" %}
不要把 NewAPI 令牌写入聊天消息、文档、代码仓库或问题截图。泄露后应立即在 NewAPI 控制台删除并重新创建。
{% endhint %}

## 获取正确的 API 地址

优先复制 NewAPI 首页展示的 API Base URL，或向实例管理员确认。常见形式如下：

| 部署方式 | 示例 |
| --- | --- |
| HTTPS 域名 | `https://newapi.example.com` |
| 已包含版本路径 | `https://newapi.example.com/v1` |
| 本机部署 | `http://localhost:3000` |
| 局域网 IP | `http://192.168.1.20:3000` |

Cherry Studio 会为普通 NewAPI 地址补齐 `/v1`，已经包含 `/v1` 时不会重复追加。因此填写站点根地址或规范的 `/v1` Base URL 都可以。

- `http` 与 `https` 必须和服务器实际配置一致；
- 公网实例应使用有效的 HTTPS 证书；
- 浏览器后台页面中的 `/console/...` 不是 API Base URL；
- 不要把令牌页面、登录页面或具体 `/chat/completions` 路径填入 Base URL。

## 配置 New API

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择内置的 **New API**；
4. 输入 NewAPI 发放的令牌；
5. 将 Base URL 改为实例的 API 地址；
6. 打开页面顶部的服务商开关；
7. 点击**添加**同步模型列表；
8. 检查模型与端点类型后应用变更；
9. 只启用准备使用的模型。

内置模板默认地址为 `http://localhost:3000`，仅适用于本机默认部署。连接远程实例时必须替换为实际地址。

如果 NewAPI 管理员配置了 Cherry Studio 一键导入链接，可以用链接预填地址与令牌；导入前仍应核对目标域名，避免恶意链接把密钥发送到错误服务器。

## 理解端点类型

NewAPI 的同一个模型名称可能支持一种或多种协议。Cherry Studio 会根据模型的端点类型选择不同的请求实现：

| Cherry Studio 端点类型 | 典型用途 |
| --- | --- |
| OpenAI Chat Completions | 大多数 OpenAI 兼容对话模型 |
| OpenAI Responses | 原生支持 Responses API 的 OpenAI 模型 |
| Anthropic Messages | Claude 或其他原生 Messages 兼容模型 |
| Google Generate Content | Gemini 原生协议 |
| OpenAI Image Generation | 绘画页面中的生成与编辑模型 |
| Jina Rerank | 知识库重排序模型 |

较新的 NewAPI 实例会在 `/models` 响应中返回 `supported_endpoint_types`，Cherry Studio 同步时会读取这些信息。

如果服务器没有返回端点元数据：

- 批量添加时选择该批模型共同使用的端点类型；
- 不同协议的模型分批添加；
- 手动添加模型时至少选择一种端点类型；
- 只选择 NewAPI 实例真正支持的协议；
- 不要仅根据模型名称猜测。

错误的端点类型可能造成 404、参数不兼容、工具调用丢失或图片请求失败。能在列表中看到模型，不代表所有协议都可用。

## 管理员：先检查渠道与模型映射

如果你负责维护 NewAPI 实例，在让用户连接 Cherry Studio 前完成以下检查：

1. 每个上游渠道都通过 NewAPI 的渠道测试；
2. 渠道勾选的模型与实际权限一致；
3. 模型映射使用客户端将要请求的模型 ID；
4. 用户令牌所在分组能访问对应渠道；
5. 计费倍率、额度和自动禁用策略已核对；
6. `/v1/models` 返回的模型与用户权限一致；
7. Chat、Responses、Messages、Gemini 和图片端点分别测试。

模型映射会把 Cherry Studio 请求的名称转换为上游名称。若健康检查返回模型不存在，应同时检查 Cherry Studio 的模型 ID、NewAPI 模型映射和上游渠道中的实际 ID。

## 对话、思考与工具调用

NewAPI 只是路由层，最终能力取决于上游模型、渠道类型、协议转换和实例版本。

- 思考选项要与目标模型及端点类型匹配；
- Claude 原生能力优先使用 Anthropic Messages；
- OpenAI 原生 Responses 功能优先使用 OpenAI Responses；
- Gemini 原生能力优先使用 Google Generate Content；
- MCP 需要模型、上游和转换层都保留工具字段；
- 多轮工具调用失败时，先用单一工具排查。

模型在普通对话中可用，不代表思考内容、工具调用、联网或结构化输出一定完整。为关键工作流分别做健康检查，不要只测试一句“你好”。

## 绘画、嵌入与重排序

Cherry Studio 的 NewAPI 适配还可使用：

- OpenAI 兼容图像生成与图片编辑；
- OpenAI 兼容嵌入模型；
- Jina 兼容重排序模型。

使用前需要 NewAPI 实例实际开放相应端点，并给模型选择正确的端点类型。

### 绘画模型

1. 同步或手动添加图像模型；
2. 将端点类型设为 **OpenAI Image Generation**；
3. 启用模型；
4. 在绘画页面选择该 NewAPI 服务商；
5. 分别测试生成和编辑。

图片生成成功不代表图片编辑也受支持。两者可能使用不同的上游端点、参数和计费方式。

### 嵌入与重排序

- 嵌入模型使用 Embeddings 接口，可供知识库与[全局记忆](../../advanced-basic/memory.md)使用；
- 重排序模型需要选择 **Jina Rerank**；
- 对话、嵌入和重排序模型可以来自不同上游；
- 分别运行健康检查并核对倍率。

## PDF 与附件

NewAPI 属于聚合网关。Cherry Studio 不会因为模型名称含有 Claude、Gemini 或 OpenAI 就假设网关完整支持原生 PDF。

当前 V2 会先在本地提取 PDF 文本，再把文本发送到 NewAPI：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会计入输入 Token；
- 若需要原生多模态附件，应使用已验证的端点与模型。

## 检查连接

建议按从服务器到客户端的顺序排查：

1. 在 NewAPI Playground 用同一令牌测试目标模型；
2. 在 Cherry Studio 运行服务商连接检查；
3. 点击**添加**并确认模型能够同步；
4. 检查模型端点类型；
5. 运行模型健康检查；
6. 回到对话界面发送普通消息；
7. 再测试思考、MCP、绘画或知识库。

如果 Playground 也失败，问题通常在 NewAPI 令牌、渠道、余额或上游；如果 Playground 成功但 Cherry Studio 失败，重点检查 Base URL、端点类型和客户端版本。

## 常见问题

### 返回 401

令牌无效、已删除、过期或复制不完整。确认填写的是 NewAPI 用户令牌，不是上游厂商 Key。

### 返回 403

令牌的模型权限、分组或 IP 白名单不允许当前请求。让实例管理员检查令牌、渠道与分组的交集。

### 返回 404

Base URL 填入了控制台路径、端点类型错误，或服务器未开放对应路由。恢复为站点根地址或规范 `/v1` 地址后重试。

### 模型列表为空

令牌没有可用模型、渠道未启用、分组不匹配，或旧版 NewAPI 的 `/models` 响应不兼容。先在 NewAPI Playground 和 `/v1/models` 检查。

### 模型存在但调用时报“不支持”

检查模型映射、上游渠道和 Cherry Studio 端点类型。模型出现在 `/models` 中只说明可见，不保证当前协议与参数组合可用。

### 返回额度或倍率相关错误

检查用户余额、令牌额度、分组倍率、模型倍率和上游账户余额。NewAPI 额度充足时，上游渠道仍可能欠费。

### MCP 只输出调用计划

确认模型支持工具调用，NewAPI 版本与渠道能保留 `tools`、`tool_calls` 和工具结果。先使用一个简单工具，并尝试模型原生协议。

### 绘画模型出现在对话列表

编辑模型，将端点类型改为 **OpenAI Image Generation**，并在绘画页面使用。图像生成模型不是普通聊天模型。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。NewAPI 使用与管理说明见[官方文档](https://docs.newapi.pro/)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
