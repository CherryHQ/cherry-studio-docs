# 无问芯穹 GenStudio

无问芯穹 GenStudio 提供大语言模型、视觉模型、Embedding、Rerank 等 API。Cherry Studio V2 已内置**无问芯穹（Infini）**服务商，通过 OpenAI 兼容接口接入。

V2 预设 API Host：

```text
https://cloud.infini-ai.com/maas
```

Cherry Studio 会在请求时补齐 `/v1`，实际对话接口为：

```text
https://cloud.infini-ai.com/maas/v1/chat/completions
```

{% hint style="info" %}
使用内置服务商时，优先保留预设 API Host。不要把模型广场、控制台或文档页面的 URL 填入 API Host。
{% endhint %}

## 使用前准备

1. 注册并登录无问芯穹智算云平台；
2. 确认当前账号所属租户；
3. 创建 GenStudio API Key；
4. 在服务列表或模型广场确认目标模型的 Model ID；
5. 查看模型价格、服务等级和速率限制；
6. 确认账户余额或已购包并发服务仍可用。

模型、价格和限额会调整。本文不固定列出“免费模型”或赠送额度，请以[服务列表](https://cloud.infini-ai.com/genstudio/usage/limit)和[预置模型列表](https://docs.infini-ai.com/gen-studio/models/supported-models.html)为准。

## 获取 API Key

1. 登录[智算云平台](https://cloud.infini-ai.com/)；
2. 打开 [API 密钥管理](https://cloud.infini-ai.com/iam/secret/key)；
3. 创建新的 GenStudio API Key；
4. 复制完整密钥；
5. 保存到安全的密码管理工具。

GenStudio 当前使用以 `sk-` 开头的 API Key，并通过 Bearer 鉴权发送请求。

{% hint style="danger" %}
API Key 相当于账户凭据。不要写入聊天、文档、代码仓库、截图或工单；泄露后应立即删除并重新创建。
{% endhint %}

## 在 Cherry Studio 配置

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择**无问芯穹 / Infini**；
4. 在 API Key 中粘贴 GenStudio 密钥；
5. 保留 API Host `https://cloud.infini-ai.com/maas`；
6. 打开页面顶部的服务商开关；
7. 点击**添加**或同步模型；
8. 查看同步预览并应用变更；
9. 只启用准备使用的模型；
10. 运行模型健康检查。

健康检查通过只说明当前 Key、地址和测试模型可以完成基础请求，不代表账号拥有列表中所有模型的权限。

## 同步与添加模型

Cherry Studio 会使用 OpenAI 兼容模型列表接口：

```text
GET /maas/v1/models
```

同步后建议：

1. 检查新增、更新和移除项；
2. 确认 Model ID 与服务列表完全一致；
3. 应用同步结果；
4. 删除已下线的旧模型；
5. 分别测试对话、Embedding 和 Rerank 模型。

如果同步失败，可以从服务列表或模型广场复制 Model ID 后手动添加。Model ID 的大小写、连字符、版本后缀和 `pro-` 前缀都属于标识的一部分。

{% hint style="warning" %}
包并发服务通常使用以 `pro-` 开头的专属 Model ID。不要把普通按量模型和包并发模型视为同一个 ID。
{% endhint %}

V2 内置的候选模型可能早于平台当前列表。实际使用时，应优先相信实时同步结果和服务列表。

## 选择对话模型

GenStudio 对话模型使用 OpenAI 兼容 Chat Completions。

首次测试建议：

1. 选择当前账户明确可用的模型；
2. 发送一条简短的纯文本消息；
3. 检查流式输出；
4. 增加系统提示词；
5. 再测试长上下文、思考、图片和工具调用。

模型系列和版本会更新。不要依赖旧教程中的固定示例，直接从服务列表复制当前 Model ID。

## 视觉模型

只有 GenStudio 明确标记为视觉语言模型的 Model ID 才能理解图片。

在 Cherry Studio 中：

1. 同步最新模型；
2. 确认模型详情包含图片输入能力；
3. 先上传一张尺寸较小的图片；
4. 询问图片中可直接验证的内容；
5. 确认成功后再尝试多图或高分辨率图片。

同一系列的文本模型与视觉模型可能使用不同 Model ID。模型名称相近不代表输入模态相同。

## 思考模式

GenStudio 提供多种推理模型，不同系列可能使用不同的思考参数和返回格式。Cherry Studio 会按识别到的模型系列应用通用适配，但无问芯穹服务商当前没有单独的思考参数面板。

首次使用推理模型时：

1. 保持思考设置为**默认**；
2. 不添加自定义请求参数；
3. 确认基础对话正常；
4. 再尝试开启或关闭思考；
5. 对照模型详情检查支持的参数。

如果开启思考后返回 400，应先恢复默认设置，而不是反复修改 Model ID。

## MCP 与工具调用

GenStudio 的部分模型支持 Function Calling。Cherry Studio 可以通过 Chat Completions 把 MCP 工具定义发送给模型，但最终能否稳定调用取决于具体模型。

建议按以下顺序验证：

1. 确认普通对话正常；
2. 只启用一个参数简单的 MCP 工具；
3. 明确要求模型调用该工具；
4. 检查是否产生结构化工具调用；
5. 确认工具结果能回传；
6. 再逐步增加工具。

模型只用文字描述“将要调用工具”不等于真实调用。出现这种情况时，应检查模型详情、工具定义和提示词。

## Embedding 与知识库

GenStudio 提供 OpenAI 兼容 Embedding 接口：

```text
POST /maas/v1/embeddings
```

当前服务可能提供 `bge-m3` 等向量模型，实际 Model ID 以服务列表为准。Cherry Studio 会根据模型 ID 和手动类型标记识别 Embedding 模型。

创建知识库前：

1. 同步或手动添加 Embedding 模型；
2. 确认模型被识别为**嵌入**类型；
3. 运行健康检查；
4. 检测向量维度；
5. 用少量文档创建测试知识库；
6. 验证召回结果后再批量导入。

向量维度是知识库索引的一部分。知识库创建后更换 Embedding 模型或维度，通常需要重新构建索引。

## Rerank

GenStudio 提供 Rerank 接口：

```text
POST /maas/v1/rerank
```

官方当前示例模型为 `bge-reranker-v2-m3`，但可用状态仍应以服务列表为准。

在 Cherry Studio 中：

1. 同步或手动添加 Rerank 模型；
2. 确认模型被识别为**重排序**类型；
3. 在知识库设置中选择该模型；
4. 用少量查询比较启用前后的结果；
5. 再决定是否用于正式知识库。

Embedding 和 Rerank 使用不同模型与端点。Embedding 可用不代表 Rerank 一定可用，应分别验证。

## 图片与视频生成

GenStudio 平台还提供图片和视频生成能力，但 Cherry Studio V2 当前内置的无问芯穹服务商主要按 OpenAI 兼容对话、Embedding 和 Rerank 接口工作，没有注册无问芯穹专用的图片或视频生成传输层。

因此：

- 不要把图片或视频生成模型当作对话模型添加；
- 以 Cherry Studio 绘画页面实际可选的服务商和模型为准；
- 官网存在某个生成模型，不代表当前 V2 已完成对应适配。

## PDF 与附件

Cherry Studio V2 会先在本地提取 PDF 文本，再把提取结果发送给对话模型：

- 文本型 PDF 通常可以直接处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用模型上下文和 Token；
- PDF 中的图片需要单独发送给视觉模型。

无问芯穹是云端服务。上传文档、图片或知识库内容前，应确认符合隐私、版权和组织安全要求。

## 计费与限流

GenStudio 的 API 调用会受账户服务等级、模型价格和频率限制影响。平台可能同时限制：

- RPM：每分钟请求数；
- RPD：每天请求数；
- TPM：每分钟 Token 数；
- 包并发服务的并发槽位。

当前计费与限制可能随时间调整。自动任务上线前应：

1. 查看最新计费规则；
2. 确认账户余额；
3. 设置并发和重试上限；
4. 监控 Token 用量；
5. 遇到 429 时退避重试；
6. 保留响应 `id` 和 `traceresponse` 便于排查。

不要通过创建多个 Key 规避租户级限制；同一租户下的 Key 可能共享配额。

## 常见问题

### 返回 401

API Key 错误、已删除、复制时带入空格，或请求没有正确使用 Bearer 鉴权。重新复制或创建 Key。

### 返回 403

账号、租户或目标模型没有权限。检查模型是否需要申请、账户状态和当前租户。

### 返回 404

API Host、接口路径或 Model ID 错误。恢复内置预设地址，并从服务列表复制完整 Model ID。

### 返回 429

达到 RPM、RPD、TPM 或包并发限制。降低并发、缩短上下文并等待恢复。

### 返回 400

模型不支持当前参数、图片格式或思考设置。清除自定义参数，恢复默认思考设置后重新测试。

### 模型列表为空

检查 API Key、API Host、网络代理和租户权限。也可以从服务列表复制 Model ID 后手动添加。

### 预设模型无法调用

V2 内置候选项可能已经下线、改名或不在当前账号权限内。同步最新列表并删除失效模型。

### 包并发模型调用失败

确认购买状态仍有效，并使用平台分配的完整专属 Model ID；不要去掉 `pro-` 前缀。

### Embedding 模型出现在对话列表

检查模型类型标记。Model ID 应包含平台给出的完整名称，并在模型管理中设为 Embedding，而不是普通对话模型。

### Rerank 健康检查没有执行

当前 V2 的通用模型连接检查会跳过 Rerank。应在知识库检索流程中实际验证重排请求。

### 上传文件后返回不支持

先确认文件已成功提取文本，再检查当前对话模型是否支持对应输入。扫描 PDF 需要 OCR，图片需要视觉模型。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。无问芯穹当前能力与配置请参阅[GenStudio API 快速集成](https://docs.infini-ai.com/gen-studio/api/get-started/)、[Cherry Studio 集成教程](https://docs.infini-ai.com/gen-studio/integrations/use-cherrystudio.html)、[预置模型列表](https://docs.infini-ai.com/gen-studio/models/supported-models.html)、[Rerank 教程](https://docs.infini-ai.com/gen-studio/api/retrieval/tutorial-rerank.html)、[计费规则](https://docs.infini-ai.com/gen-studio/api/usage-and-billing/billing.html)和[调用限制](https://docs.infini-ai.com/gen-studio/api/usage-and-billing/rate-limit.html)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
