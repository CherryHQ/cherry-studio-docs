# 火山引擎（方舟 / 豆包）

火山方舟是火山引擎的大模型服务平台，提供豆包及多家第三方模型。Cherry Studio V2 内置的服务商 ID 为 `doubao`，界面中可能显示为 **Doubao**、**豆包**或**火山引擎**。

V2 默认 API Host：

```text
https://ark.cn-beijing.volces.com/api/v3/
```

{% hint style="info" %}
当前 V2 内置服务商默认使用 OpenAI 兼容 Chat Completions。火山方舟官网同时提供 Responses API、Files API 和云端内置工具，但官网支持不代表这些能力已自动接入 Cherry Studio。
{% endhint %}

## 使用前准备

1. 注册并登录火山引擎；
2. 进入火山方舟控制台；
3. 确认项目与地域；
4. 开通准备使用的模型或计费方式；
5. 创建 API Key；
6. 从当前模型列表复制 Model ID；
7. 确认余额、额度和速率限制。

火山方舟的模型、版本、价格和上下线状态会调整。本文不固定列出价格或赠送额度，请以[模型列表](https://www.volcengine.com/docs/82379/1554711)和控制台为准。

## 获取 API Key

1. 打开[火山方舟控制台](https://console.volcengine.com/ark/)；
2. 确认当前项目和华北 2（北京）地域；
3. 打开 [API Key 管理](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey)；
4. 点击**创建 API Key**；
5. 填写便于识别的名称；
6. 复制并安全保存。

{% hint style="danger" %}
API Key 相当于账户凭据。不要写入聊天、文档、代码仓库或问题截图；泄露后应立即在方舟控制台删除或轮换。
{% endhint %}

## 获取 Model ID

火山方舟目前可以使用标准模型的 Model ID，也可以在部分场景使用自定义推理接入点 ID。

| 标识 | 常见格式 | 适用场景 |
| --- | --- | --- |
| Model ID | `doubao-seed-...` | 平台预置、按量调用的模型 |
| Endpoint ID | `ep-...` | 自定义模型、专用资源或已创建的推理接入点 |

获取当前 Model ID：

1. 打开[模型列表](https://www.volcengine.com/docs/82379/1554711)；
2. 选择目标模型和版本；
3. 确认它支持 Chat API；
4. 复制完整 Model ID；
5. 不要复制模型显示名或控制台页面 URL。

如果组织使用自定义模型、模型单元或专用推理接入点，应从[推理接入点](https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint)复制 `ep-...` ID。

## 在 Cherry Studio 配置

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **Doubao / 火山引擎**；
4. 在 API Key 中粘贴方舟密钥；
5. 保留 API Host `https://ark.cn-beijing.volces.com/api/v3/`；
6. 打开页面顶部的服务商开关；
7. 点击**添加模型**；
8. 粘贴当前 Model ID 或 Endpoint ID；
9. 只启用准备使用的模型；
10. 运行模型健康检查。

V2 预设列表中包含一些旧豆包、DeepSeek 和 Embedding 模型。预设只是候选项，不代表模型仍在线。

## 同步与手动添加

火山方舟的模型目录与自定义推理接入点并不总能通过标准 OpenAI 模型列表完整返回，因此同步结果可能为空或不完整。

最稳定的方式是：

1. 从方舟当前模型页复制 Model ID；
2. 在 Cherry Studio 手动添加；
3. 检查模型能力标签；
4. 运行健康检查；
5. 删除无法调用的旧预设。

{% hint style="warning" %}
不要因为某个旧 Model ID 仍显示在 V2 预设中就继续使用。方舟模型版本通常带日期后缀，旧版本可能已经下线。
{% endhint %}

## API Host

保持默认：

```text
https://ark.cn-beijing.volces.com/api/v3/
```

Cherry Studio 会按模型类型追加请求路径。旧教程中把完整的 `/chat/completions` 写入 API Host 并以 `#` 结尾，是历史兼容方法；V2 不需要这样配置。

如果使用非北京地域、代理或企业专用域名，应完整替换 API Host，并确认：

- API Key 属于同一项目与地域；
- 域名支持 `/api/v3`；
- 代理能转发流式响应；
- Model ID 或 Endpoint ID 在目标环境有效。

## 对话模型

当前内置服务商主要通过 OpenAI 兼容 Chat Completions 对话。

建议按以下顺序测试：

1. 发送一条简短的纯文本消息；
2. 检查流式输出；
3. 增加系统提示词；
4. 测试较长上下文；
5. 再测试图片、思考和工具调用。

火山方舟官网的新示例可能优先展示 Responses API。不要因为 Responses 示例可用，就假定 V2 当前对话已经切换到同一接口或支持所有 Responses 专属字段。

## 思考模式

不同豆包版本使用的思考参数不同。Cherry Studio V2 会按 Model ID 适配：

- 较新的 Doubao Seed 模型使用 `reasoningEffort`；
- 部分旧思考模型使用 `thinking: enabled`；
- 支持自动思考的旧模型可以使用 `thinking: auto`；
- 其他组合可能不发送思考字段。

如果修改思考强度后报错：

1. 将思考设置恢复为**默认**；
2. 清除模型自定义参数；
3. 确认 Model ID 与官方当前版本一致；
4. 查看该模型的 Chat API 示例；
5. 重新运行健康检查。

不要把 Responses API 的 `thinking` 示例原样复制到 Chat Completions 模型。

## 视觉与多模态

只有方舟明确标记为视觉或多模态的模型才能接收图片或视频。

在 Cherry Studio 中：

1. 添加当前视觉 Model ID；
2. 确认模型显示图片能力；
3. 先上传一张小图片；
4. 检查模型是否真正理解内容；
5. 再尝试多图或较大附件。

方舟官网提供原生文件和视频输入能力，但当前 V2 是否能直接使用取决于客户端的附件格式适配。官网支持某种输入，不等于 Cherry Studio 已经使用 Files API 上传它。

## MCP 与工具调用

Cherry Studio MCP 使用模型的结构化 Function Calling。

1. 先完成普通对话；
2. 只启用一个简单 MCP 工具；
3. 明确要求调用；
4. 检查是否产生结构化调用；
5. 确认工具结果能回传给模型；
6. 再增加工具。

火山方舟的 Web Search、Image Process、Knowledge Search 和 Remote MCP 属于方舟云端工具，主要通过 Responses API 配置。它们与 Cherry Studio 自己添加的 MCP 服务器不是同一套配置。

模型只用文字描述“将要调用工具”不等于真实调用，应检查 Model ID、接口和工具定义。

## Embedding 与知识库

火山方舟提供文本和多模态向量化 API。V2 预设中可能保留旧 Embedding Model ID，但应优先使用方舟当前文档列出的版本。

创建知识库时：

1. 从方舟当前向量化模型页复制 Model ID；
2. 在 Cherry Studio 手动添加；
3. 确认模型被识别为 Embedding；
4. 检测向量维度；
5. 运行健康检查；
6. 导入少量文档试运行；
7. 再批量导入。

多模态向量化模型接受的输入格式可能与 Cherry Studio 知识库当前的文本切片不同。用于文档知识库时，应先验证纯文本 Embedding。

Embedding 模型或向量维度一旦用于现有知识库，不应直接更换；否则通常需要重建向量索引。

当前 V2 没有为 `doubao` 内置登记专用 Rerank 模型。需要重排时，应选择已由 V2 支持并通过健康检查的其他服务商。

## 图片生成

火山方舟官网提供图片生成 API，支持 Model ID 或图片推理接入点 ID。

但是，当前 V2 `main` 分支没有为内置 `doubao` 服务商登记专用图片生成模型和传输链路。因此：

- 官网支持 Seedream 不代表 Cherry Studio 绘画页面会自动出现；
- 不要把图片 Model ID 当作普通对话模型；
- 不要根据旧截图手动猜测 Endpoint Type；
- 以当前绘画页面实际可选服务商和模型为准。

如果后续 V2 版本加入方舟图片适配，应重新同步或添加当前 Model ID，并先用单张、常见尺寸测试。

{% hint style="warning" %}
图片生成可能按成功输出张数计费。不要为了验证兼容性连续重复提交任务。
{% endhint %}

## PDF 与附件

当前 V2 会先在本地提取 PDF 文本，再发送给方舟对话模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用模型上下文和费用；
- PDF 中的图片需要单独发送给视觉模型。

这与方舟原生 Files API 或文档理解 API 不同。Cherry Studio 不会因为方舟支持文件上传，就自动把 PDF 作为方舟文件对象处理。

上传文档、图片或知识库内容前，应确认符合隐私、数据安全和组织合规要求。

## 计费、限流与用量

方舟可能同时受以下因素限制：

- 账户余额；
- 项目预算；
- 按量、模型单元或套餐权益；
- RPM / TPM；
- 推理接入点限流；
- 模型并发；
- 内容安全策略。

建议在控制台查看用量统计并设置预算告警。自定义 Endpoint 还应检查其状态、资源规格和限流配置。

## 常见问题

### 返回 401

API Key 错误、已删除、复制时带入空格，或 Key 与 API Host 不匹配。重新复制方舟 API Key。

### 返回 403

项目、模型、Endpoint 或内容没有权限。检查模型开通状态、项目、IAM 和内容安全策略。

### 返回 404

API Host、Model ID 或 Endpoint ID 错误，或模型已下线。恢复默认地址，并从当前模型页重新复制 ID。

### 返回 429

达到模型、项目或推理接入点的 RPM、TPM 或并发限制。降低并发并等待恢复。

### 模型列表为空

方舟不一定通过标准模型列表返回所有模型与自定义 Endpoint。直接从官方模型页或推理接入点页复制 ID 后手动添加。

### 预设模型无法使用

V2 预设中可能包含已下线的旧日期版本。删除失效模型，添加当前 Model ID。

### Model ID 可用，Endpoint ID 不可用

Endpoint 可能未启动、没有绑定正确模型、属于其他项目，或资源已释放。到方舟控制台检查 Endpoint 状态。

### 思考参数错误

恢复为默认思考设置。新旧豆包模型的 `reasoningEffort` 与 `thinking` 参数不能混用。

### 普通对话可用，MCP 不调用

确认模型支持 Function Calling。方舟云端 Remote MCP 与 Cherry Studio MCP 是不同功能，不能只在方舟控制台启用。

### Embedding 模型无法添加

确认使用的是向量化 Model ID，并在模型管理中标记为 Embedding。不要把展示名称或 Endpoint 页面 URL 当作模型 ID。

### Seedream 在官网可用，但绘画页面没有

当前 V2 内置 `doubao` 服务商尚未登记专用图片生成链路。等待客户端适配或使用绘画页面已有服务商。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。火山方舟当前能力请参阅[产品文档](https://www.volcengine.com/docs/82379/)、[模型列表](https://www.volcengine.com/docs/82379/1554711)、[API 参考](https://www.volcengine.com/docs/82379/1523520)、[管理推理接入点](https://www.volcengine.com/docs/82379/1182403)和[图片生成 API](https://www.volcengine.com/docs/82379/1824137)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
