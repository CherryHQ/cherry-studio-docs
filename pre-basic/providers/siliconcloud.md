# 硅基流动

硅基流动（SiliconFlow）提供对话、视觉、Embedding、Rerank 和图片生成 API。Cherry Studio V2 内置硅基流动服务商，并为对话、Embedding 和图片生成实现了专用适配。

V2 预设 API Host：

```text
https://api.siliconflow.cn
```

实际 OpenAI 兼容请求使用 `/v1` 路径，例如 `https://api.siliconflow.cn/v1/chat/completions`。

{% hint style="info" %}
首次配置应保留 V2 预设地址。不要把控制台页面、模型广场 URL 或文档地址填入 API Host。
{% endhint %}

## 使用前准备

1. 注册并登录 SiliconFlow；
2. 完成平台要求的账户验证；
3. 创建 API Key；
4. 充值或确认账户仍有可用余额；
5. 查看准备使用的模型是否仍在线；
6. 确认模型的价格和速率限制。

SiliconFlow 会调整模型、能力、价格和上下线状态。本文不固定列出赠金、免费模型或价格，请以[模型广场](https://cloud.siliconflow.cn/models)和控制台为准。

## 获取 API Key

1. 登录 [SiliconFlow 控制台](https://cloud.siliconflow.cn/)；
2. 打开 [API 密钥](https://cloud.siliconflow.cn/account/ak)；
3. 点击**新建密钥**；
4. 填写便于识别的名称；
5. 复制生成的 Key；
6. 保存到安全的密码管理工具。

{% hint style="danger" %}
API Key 相当于账户凭据。不要写入聊天、文档、代码仓库或问题截图；泄露后应立即删除并重新创建。
{% endhint %}

## 在 Cherry Studio 配置

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **Silicon / 硅基流动**；
4. 在 API Key 中粘贴 SiliconFlow 密钥；
5. 保留 API Host `https://api.siliconflow.cn`；
6. 打开页面顶部的服务商开关；
7. 点击**添加**或同步模型；
8. 检查同步预览并应用变更；
9. 只启用准备使用的模型；
10. 运行模型健康检查。

连接检查只说明密钥和基础请求可用，不代表账户可以调用列表中的每个模型。最终权限、余额和速率由 SiliconFlow 判断。

## 同步与添加模型

Cherry Studio 会从 SiliconFlow 的模型列表接口读取当前模型。SiliconFlow 的 `/v1/models` 还支持按以下类型筛选：

- `chat`
- `embedding`
- `reranker`
- `text-to-image`
- `image-to-image`
- 其他音频与视频类型

同步后建议：

1. 查看新增、更新和移除项；
2. 确认每个模型的类型；
3. 应用同步结果；
4. 删除自己手动保留的旧模型；
5. 分别运行健康检查。

V2 内置模型只是候选项，平台实时返回结果优先。如果模型未被自动识别为 Embedding、Rerank、视觉或图片生成，可以在模型管理中核对能力，但不要只修改显示名称来绕过接口差异。

{% hint style="warning" %}
Model ID 必须与 SiliconFlow 当前列表完全一致，包括 `Pro/` 前缀、组织名、大小写、斜杠和版本后缀。
{% endhint %}

## 选择对话模型

SiliconFlow 对话使用 OpenAI 兼容 Chat Completions。

建议按以下顺序测试：

1. 发送一条简短的纯文本消息；
2. 检查流式输出；
3. 增加系统提示词；
4. 测试较长上下文；
5. 再测试图片、思考和工具调用。

`Pro/` 版本与普通版本可能具有不同的价格、吞吐量或可用性。应把它们视为不同 Model ID，并分别运行健康检查。

## 视觉模型

只有 SiliconFlow 明确标记为视觉语言模型的 Model ID 才能接收图片。

在 Cherry Studio 中：

1. 同步最新模型；
2. 选择显示图片能力的模型；
3. 先上传一张小图片；
4. 检查模型是否真正理解图片；
5. 再尝试多图或高分辨率图片。

同一模型系列的文本版与视觉版可能是不同 ID。图片还会增加请求体大小、上下文消耗和费用。

## 思考模式

SiliconFlow 的部分 DeepSeek、GLM、Qwen 和混元模型使用 `enable_thinking` 与 `thinking_budget`。

Cherry Studio V2 对受支持的 SiliconFlow 思考模型会：

- 使用 `enable_thinking` 开关；
- 在设置思考预算时，把非零预算至少提升到 32,768；
- 关闭思考时发送 `enable_thinking: false`。

这意味着 V2 当前不适合在 SiliconFlow 上精确设置较小的思考预算。需要减少消耗时，优先关闭思考、缩短上下文或改用非思考模型。

如果开启思考后报错：

1. 将思考设置恢复为**默认**；
2. 清除模型自定义参数；
3. 确认 Model ID 仍在线；
4. 对照 SiliconFlow 当前模型说明；
5. 重新运行健康检查。

## MCP 与工具调用

SiliconFlow Chat Completions 支持 `tools`，但最终能否正确调用仍取决于具体模型。

1. 先确认普通对话正常；
2. 只启用一个简单 MCP 工具；
3. 明确要求调用；
4. 检查是否产生结构化调用；
5. 确认工具结果能回传给模型；
6. 再增加工具。

模型只用文字描述“将要调用工具”不等于真实调用。出现这种情况时，应检查模型能力、提示词和工具定义。

## Embedding、Rerank 与知识库

SiliconFlow 提供：

```text
POST /v1/embeddings
POST /v1/rerank
```

当前可见的示例模型可能包括 `BAAI/bge-m3`、Qwen Embedding、Qwen Reranker 和 BGE Reranker，但实际清单应从模型广场或同步结果获取。

创建知识库时：

1. 同步模型；
2. 选择明确识别为 Embedding 的模型；
3. 检测向量维度；
4. 运行健康检查；
5. 再选择当前可用的 Rerank 模型；
6. 导入少量文档试运行；
7. 确认检索与重排结果后再批量导入。

部分 Qwen Embedding 模型允许选择输出维度。维度一旦用于现有知识库，不应直接修改；否则通常需要重建向量索引。

Rerank 与 Embedding 使用不同端点和模型。Embedding 可用不代表 Rerank 一定可用，应分别检查。

## 图片生成与编辑

Cherry Studio V2 为 SiliconFlow 实现了专用图片模型，请求发送到：

```text
POST /v1/images/generations
```

当前 V2 模型注册信息重点覆盖 Qwen Image 的生成与编辑。官网出现的其他图片模型不一定已经被当前版本正确识别，应以 Cherry Studio 绘画页面可选项为准。

根据模型能力，V2 可以传递：

- `image_size`
- `batch_size`
- `seed`
- `negative_prompt`
- `num_inference_steps`
- `guidance_scale`
- `cfg`
- `prompt_enhancement`
- 最多三张编辑输入图

SiliconFlow 使用明确的 `image_size`，V2 不会把单独的宽高比参数自动转换为有效请求。遮罩输入在当前专用适配中也不受支持。

{% hint style="warning" %}
图片模型可能按输出张数计费。首次测试把批量数量设为 1，并使用模型支持的常见尺寸。
{% endhint %}

如果返回的是图片 URL，应及时保存结果。临时链接的有效期由 SiliconFlow 决定。

## PDF 与附件

当前 V2 会先在本地提取 PDF 文本，再发送给 SiliconFlow 对话模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用模型上下文和费用；
- PDF 中的图片需要单独发送给视觉模型。

SiliconFlow 是云端服务。上传文档、图片或知识库内容前，应确认符合隐私、版权和组织安全要求。

## 速率、余额与排障信息

SiliconFlow 的限流可能按模型分别计算，并同时受 RPM、TPM、RPD、TPD、IPM 或 IPD 等指标影响。

建议：

1. 在控制台查看余额与模型价格；
2. 为自动任务设置并发和重试上限；
3. 遇到 429 时降低频率并等待；
4. 定期同步模型；
5. 保存错误响应中的 `x-siliconcloud-trace-id`，便于提交工单。

不要通过创建多个 Key 规避账户级限流；平台限制通常不是按单个 Key 独立计算。

## 常见问题

### 返回 401

API Key 错误、已删除、复制时带入空格，或请求未正确使用 Bearer 鉴权。重新复制或创建 Key。

### 返回 403

账户、模型或内容没有权限。检查实名认证、余额、模型资格和平台策略。

### 返回 404

API Host、Model ID 或接口类型错误。恢复 V2 预设地址，并重新同步模型。

### 返回 429

达到模型的 RPM、TPM、RPD、TPD、IPM 或 IPD 限制。降低并发、缩短上下文并等待恢复。

### 返回 503 或 504

模型繁忙或上游超时。降低并发后重试；持续失败时换用其他在线模型并记录 Trace ID。

### 模型列表为空

检查 API Key、API Host 和网络代理。也可以从模型广场复制完整 Model ID 后手动添加。

### 预设模型无法使用

V2 预设可能早于模型下线、改名或权限变化。以实时同步结果为准，移除失效模型。

### 思考预算与设置不一致

V2 当前会把受支持 SiliconFlow 模型的非零思考预算至少提升到 32,768。这是客户端适配行为；需要减少消耗时应关闭思考或换用非思考模型。

### Embedding 可用，但 Rerank 不可用

两者使用不同模型和接口。确认 Rerank Model ID、余额和能力标签，并单独运行健康检查。

### 图片模型在官网存在，但绘画页面没有

当前 V2 还没有为该模型登记图片生成模式。不要把它当作对话模型使用；等待适配或选择绘画页面已有模型。

### 图片编辑只处理了第一张图

确认模型是否支持多图编辑。V2 最多发送三张输入图，但具体模型可能只接受一张。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。SiliconFlow 当前接口与模型请参阅[模型列表](https://docs.siliconflow.cn/cn/api-reference/models/get-model-list)、[Chat Completions](https://docs.siliconflow.cn/cn/api-reference/chat-completions/chat-completions)、[Embedding](https://docs.siliconflow.cn/cn/api-reference/embeddings/create-embeddings)、[Rerank](https://docs.siliconflow.cn/cn/api-reference/rerank/create-rerank)和[图片生成](https://docs.siliconflow.cn/cn/userguide/capabilities/images)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
