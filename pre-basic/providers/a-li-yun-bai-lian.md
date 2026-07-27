# 阿里云百炼

阿里云百炼（Alibaba Cloud Model Studio）提供千问和多家第三方模型。Cherry Studio V2 内置百炼服务商，支持 OpenAI 兼容对话、Anthropic 兼容调用、Embedding、Rerank，以及专用的图片生成和编辑链路。

V2 的华北 2（北京）默认地址为：

| 协议 | 默认 Base URL |
| --- | --- |
| OpenAI 兼容 | `https://dashscope.aliyuncs.com/compatible-mode/v1/` |
| Anthropic 兼容 | `https://dashscope.aliyuncs.com/apps/anthropic` |

{% hint style="info" %}
百炼的 API Key、Base URL 和模型列表按地域隔离，不能跨地域混用。北京 Key 配新加坡地址、或新加坡 Key 配北京地址，通常会返回 401。
{% endhint %}

## 使用前准备

首次使用百炼 API，通常需要：

1. 注册并登录阿里云账号；
2. 完成账号实名认证；
3. 开通阿里云百炼；
4. 选择准备使用的地域；
5. 创建 API Key；
6. 确认账户余额、免费额度或订阅权益；
7. 记录对应的业务空间 ID。

模型、价格、免费额度和地域可用性会调整。本文不固定列出费用，请以[百炼模型列表](https://help.aliyun.com/zh/model-studio/models)和控制台账单为准。

## 选择地域与 Base URL

百炼正在推广业务空间专属域名。它通常比旧 DashScope 公共域名更稳定，并且需要把 `{WorkspaceId}` 替换为真实业务空间 ID。

常见 OpenAI 兼容地址：

| 地域 | Base URL |
| --- | --- |
| 华北 2（北京）默认 | `https://dashscope.aliyuncs.com/compatible-mode/v1/` |
| 华北 2（北京）专属域名 | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/` |
| 新加坡 | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/` |
| 日本（东京） | `https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1/` |
| 德国（法兰克福） | `https://{WorkspaceId}.eu-central-1.maas.aliyuncs.com/compatible-mode/v1/` |
| 美国（弗吉尼亚） | `https://dashscope-us.aliyuncs.com/compatible-mode/v1/` |

对应的 Anthropic 兼容地址通常把末尾路径换为 `/apps/anthropic`。不同模型支持的地域和协议可能不同，应从模型详情页复制地址，不要凭模型名称推测。

{% hint style="warning" %}
不要把 `{WorkspaceId}` 原样填入 Cherry Studio。业务空间 ID 可在百炼的业务空间管理页面查看，通常类似 `llm-...`。
{% endhint %}

## 获取 API Key

1. 打开 [百炼 API Key 管理](https://bailian.console.aliyun.com/?tab=model#/api-key)；
2. 在页面右上角确认目标地域；
3. 点击**创建 API Key**；
4. 选择归属业务空间；
5. 选择全部权限，或按组织要求配置 IP 白名单和模型范围；
6. 填写便于识别的描述；
7. 创建后立即复制并安全保存。

新创建的按量付费 Key 可能以 `sk-ws` 开头，并且只在创建时显示一次；旧版 `sk-` Key 仍可能继续可用。

{% hint style="danger" %}
API Key 相当于账户凭据。不要写入聊天、文档、代码仓库或问题截图；泄露后应立即在百炼控制台重置或删除。
{% endhint %}

## 在 Cherry Studio 配置

### 使用北京默认地址

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **Bailian / 阿里云百炼**；
4. 粘贴北京地域的 API Key；
5. 保留 OpenAI Base URL `https://dashscope.aliyuncs.com/compatible-mode/v1/`；
6. 打开页面顶部的服务商开关；
7. 点击**添加**或同步模型；
8. 检查同步预览并应用变更；
9. 只启用准备使用的模型；
10. 运行模型健康检查。

### 使用其他地域或专属域名

1. 在百炼控制台复制目标业务空间的 API Host；
2. 在 Cherry Studio 把 OpenAI Base URL 改为对应的 `/compatible-mode/v1/` 地址；
3. 如果要使用 Anthropic 兼容工作流，同时更新 Anthropic Base URL；
4. 使用**同一地域、同一计费计划**下创建的 API Key；
5. 重新同步模型；
6. 对每个模型运行健康检查。

V2 会从用户配置的 OpenAI Base URL 推导图片接口主机。因此，改用专属域名后，图片请求也会跟随该域名，而不是强制返回北京公共域名。

## 同步与添加模型

百炼的模型范围会频繁更新，V2 内置列表只用于首次展示。同步时以百炼当前返回结果为准。

建议：

1. 先确认地域与 Key 匹配；
2. 同步模型；
3. 查看新增、更新和移除项；
4. 应用同步结果；
5. 检查模型能力标签；
6. 删除自己手动保留的过期模型；
7. 逐个运行健康检查。

如果同步结果不完整，可以从百炼模型页复制完整 Model ID 后手动添加。大小写、斜杠和版本后缀都属于 ID，例如第三方模型可能带组织前缀。

{% hint style="warning" %}
模型出现在 V2 预设或另一个地域，不代表当前 API Key 有权调用。最终权限由百炼服务端、业务空间权限和地域模型列表共同决定。
{% endhint %}

## 对话模型

普通聊天使用 OpenAI 兼容 Chat Completions。

建议按以下顺序测试：

1. 发送一条简短的纯文本消息；
2. 检查流式输出；
3. 增加系统提示词；
4. 测试较长上下文；
5. 再测试图片、思考和工具调用。

百炼同时提供千问和第三方模型。相同厂商的模型经百炼调用时，也应使用百炼模型页给出的 Model ID 和参数，不要照搬其他平台的 ID。

## Anthropic 兼容与 Code Tools

百炼提供 Anthropic 兼容 Messages API，可用于支持自定义 Anthropic 地址的编程工具或 Agent 工作流。

在 Cherry Studio 中：

1. 确认目标模型支持 Anthropic 兼容协议；
2. 填写与地域对应的 Anthropic Base URL；
3. 保持 API Key 与地域一致；
4. 先运行普通对话；
5. 再在 Code Tools 或 Agent 场景测试。

OpenAI 与 Anthropic 兼容地址不是同一条路径。只修改 OpenAI Base URL，不会自动保证 Anthropic 工作流指向同一地域。

## 思考模式

百炼上的千问、DeepSeek、GLM、Kimi 等模型可能使用不同思考参数。Cherry Studio V2 会按模型系列适配 `enable_thinking`、思考预算等参数。

如果开启思考后报错：

1. 将思考设置恢复为**默认**；
2. 清除模型自定义参数；
3. 确认使用的是当前 Model ID；
4. 查看该模型在当前地域的官方示例；
5. 重新运行健康检查。

有些模型只能开关思考，不能选择 `low`、`medium`、`high` 等强度。不要把其他平台的推理参数直接复制到百炼。

## 视觉与多模态

只有明确支持图片、音频或视频输入的模型才能接收对应附件。

测试视觉模型时：

1. 同步最新 Model ID；
2. 确认模型显示图片能力；
3. 先上传一张小图片；
4. 检查模型是否真正理解内容；
5. 再尝试多图、视频或高分辨率文件。

同一系列的文本版、视觉版和 Omni 版可能是不同模型。附件会增加上下文、网络耗时和费用。

## MCP 与工具调用

Cherry Studio MCP 要求模型支持结构化 Tool Calling。

1. 先确认普通对话正常；
2. 只启用一个简单 MCP 工具；
3. 明确要求调用；
4. 检查是否产生结构化调用；
5. 确认工具结果能回传给模型；
6. 再增加工具。

模型用文字描述“将要调用工具”不等于真实调用。出现这种情况时，应检查模型能力、协议、提示词和工具定义。

## Embedding、Rerank 与知识库

百炼提供文本与多模态 Embedding，以及文本和多模态 Rerank。当前模型页推荐项可能包括：

- 文本 Embedding：`text-embedding-v4`；
- 文本 Rerank：`qwen3-rerank`；
- 多模态 Embedding：`qwen3-vl-embedding`；
- 多模态 Rerank：`qwen3-vl-rerank`。

这些是平台示例，不是永久清单。`gte-rerank` 已于 2026 年 5 月 30 日下线，不应继续按旧教程配置。

创建知识库时：

1. 添加当前可用的 Embedding 模型；
2. 确认 Cherry Studio 将其识别为嵌入模型；
3. 检测向量维度；
4. 运行健康检查；
5. 再添加并测试 Rerank 模型；
6. 导入少量文档试运行；
7. 确认检索与重排结果后再批量导入。

Embedding 模型或向量维度一旦用于现有知识库，不应直接更换；否则通常需要重建向量索引。

百炼不同地域的 Rerank 端点和能力可能不同。若模型能添加但重排请求失败，应先关闭 Rerank 保证基本检索可用，再核对当前 V2 版本、地域接口与模型权限。

## 图片生成与编辑

Cherry Studio V2 为百炼实现了专用图片传输链路：

1. 根据模型选择原生 DashScope 图片接口；
2. 异步模型在请求中启用 `X-DashScope-Async`；
3. 获取 `task_id`；
4. 轮询任务状态；
5. 成功后读取图片 URL。

V2 只会为已经适配的模型显示对应模式和参数，例如：

- 文生图；
- 图片编辑；
- 图片翻译；
- 尺寸；
- Seed；
- 负面提示词；
- 水印；
- 部分模型的参考图或功能类型。

并非百炼官网出现的每个图片模型都已经被当前 V2 适配。应优先从 Cherry Studio 绘画页面可选的百炼模型开始测试。

{% hint style="warning" %}
图片任务可能按成功输出张数计费。首次测试把输出数量设为 1，并避免在等待异步结果时重复提交。
{% endhint %}

取消 Cherry Studio 中的等待只会停止本地轮询；DashScope 没有供当前 V2 调用的通用任务取消接口，已提交任务仍可能继续执行并产生费用。

## PDF 与附件

当前 V2 会先在本地提取 PDF 文本，再发送给百炼对话模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用模型上下文和费用；
- PDF 中的图片需要单独发送给视觉模型。

百炼是云端服务。上传文档、图片或知识库内容前，应确认符合隐私、数据跨境和组织安全要求；尤其要注意所选地域的数据处理范围。

## 额度、权限与限流

百炼可能同时受以下因素限制：

- 账户余额与免费额度；
- 业务空间预算；
- Key 的 IP 白名单；
- Key 的模型权限；
- RPM / TPM；
- 并发任务数；
- 图片任务队列；
- 地域资源可用性。

建议在控制台设置预算和用量告警，避免多个自动任务共用同一 Key 无限重试。

## 常见问题

### 返回 401

API Key 错误、已重置，或 Key 与 Base URL 地域不匹配。先确认地域，再重新复制对应 Key。

### 返回 403

Key 没有模型权限、IP 不在白名单、业务空间未授权，或账号状态受限。检查 Key 权限与业务空间策略。

### 返回 404

Base URL、Workspace ID、协议路径或 Model ID 错误。不要把控制台页面 URL 当作 API 地址。

### 返回 429

达到 RPM、TPM、并发或任务队列限制。降低并发、缩短上下文并等待恢复；不要立即循环重试。

### 提示余额不足或配额耗尽

检查账户余额、免费额度、业务空间预算和模型计费方式。不同模型可能使用不同额度池。

### 模型列表为空

检查地域、API Key、Base URL 和网络代理。也可以从当前地域的模型页复制完整 Model ID 后手动添加。

### 预设模型无法使用

V2 预设可能早于百炼模型下线或地域变化。重新同步，并以当前地域的模型列表为准。

### 普通聊天可用，Agent 或 Code Tools 不可用

检查 Anthropic Base URL 是否仍指向北京默认地址，以及目标模型是否支持 Anthropic 兼容协议和工具调用。

### 图片生成返回地址错误

检查 OpenAI Base URL 是否包含正确的业务空间域名和 `/compatible-mode/v1/` 后缀。V2 会从它推导原生图片接口主机。

### 图片任务一直等待

任务可能仍在队列、轮询网络失败、额度不足或模型繁忙。先查看错误信息和百炼任务状态，不要重复提交。

### Rerank 模型能选但没有生效

先确认模型没有下线、地域接口兼容，并检查知识库是否真的启用了 Rerank。必要时暂时关闭重排，先验证 Embedding 检索。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。百炼当前地域、Key 与模型请参阅[地域与接入域名](https://help.aliyun.com/zh/model-studio/regions/)、[获取 API Key](https://help.aliyun.com/zh/model-studio/get-api-key/)、[选择模型](https://help.aliyun.com/zh/model-studio/models)、[向量与重排序](https://help.aliyun.com/zh/model-studio/embedding-rerank-model/)和[图片生成与编辑](https://help.aliyun.com/zh/model-studio/image-model)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
