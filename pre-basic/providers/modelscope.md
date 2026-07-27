# ModelScope（魔搭）

ModelScope 通过 API-Inference 把部分开源模型提供为可直接调用的在线 API。Cherry Studio V2 内置 ModelScope 服务商，支持 OpenAI 兼容对话、视觉模型、嵌入模型和异步图片生成。

默认 Base URL：

```text
https://api-inference.modelscope.cn/v1/
```

{% hint style="info" %}
ModelScope 模型库中的模型不一定都支持 API-Inference。只有模型页面带有 API-Inference 标识并提供调用示例的模型，才能直接接入 Cherry Studio。
{% endhint %}

## 使用前确认

ModelScope 免费 API-Inference 目前要求：

1. 注册并登录 ModelScope；
2. 绑定阿里云账号；
3. 完成对应阿里云账号的实名认证；
4. 创建 ModelScope Access Token；
5. 使用当前仍支持 API-Inference 的模型。

API-Inference 是体验型免费服务，不提供生产 SLA。需要商业、高并发或稳定服务时，应使用商业 API 提供商或自行部署模型。

## 获取 Access Token

1. 登录 [ModelScope](https://modelscope.cn/)；
2. 打开[访问令牌](https://modelscope.cn/my/myaccesstoken)；
3. 新建令牌并填写便于识别的名称；
4. 复制生成的 Access Token；
5. 将 Token 保存在安全位置。

{% hint style="danger" %}
Access Token 相当于账户凭据。不要写入聊天、文档、代码仓库或问题截图；泄露后应立即在 ModelScope 删除并重新创建。
{% endhint %}

## 在 Cherry Studio 配置

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **ModelScope 魔搭**；
4. 在 API Key 中粘贴 Access Token；
5. 保留 Base URL `https://api-inference.modelscope.cn/v1/`；
6. 打开页面顶部的服务商开关；
7. 点击**添加**或同步模型；
8. 检查同步预览并应用变更；
9. 只启用准备使用的模型；
10. 运行模型健康检查。

如果同步列表中包含旧模型，不要直接假定它仍可调用。ModelScope 会随着新模型发布逐步调整或下线旧模型，应到模型详情页确认 API-Inference 状态。

## 查找可用模型

1. 打开 [ModelScope 模型库](https://modelscope.cn/models)；
2. 筛选支持 **API-Inference** 的模型；
3. 打开模型详情页；
4. 确认右侧有 API 调用入口与示例；
5. 复制完整 Model ID；
6. 在 Cherry Studio 同步或手动添加该 ID；
7. 运行健康检查。

Model ID 通常包含组织与模型名称，例如：

```text
Qwen/Qwen3.5-35B-A3B
```

大小写、斜杠和后缀都属于 ID。不要把页面显示名、仓库 URL 或本地文件名当作 API Model ID。

{% hint style="warning" %}
V2 内置模型清单只是候选项，平台实时支持状态优先。出现 404 或模型不可用时，先到 ModelScope 模型页核对，不要反复重试已下线模型。
{% endhint %}

## 对话模型

ModelScope 的 LLM API-Inference 使用 OpenAI 兼容 Chat Completions。选择模型时应确认它是对话或指令模型，而不是基础模型、Embedding 或图片生成模型。

建议按以下顺序测试：

1. 发送一条简短的纯文本消息；
2. 测试流式输出；
3. 再增加系统提示词；
4. 测试长上下文；
5. 最后测试思考、图片或工具调用。

不同开源模型的参数和提示模板可能不同。ModelScope 官方建议以模型详情页的 API 示例为准，尤其是思考模型。

## 视觉模型

支持视觉的模型可以通过 OpenAI 兼容消息接收图片 URL 或 Base64 图片。

在 Cherry Studio 中：

1. 选择明确支持视觉的 Model ID；
2. 确认模型显示图片能力；
3. 先上传一张小图片；
4. 检查模型是否真正理解图片；
5. 再尝试多图或高分辨率图片。

模型系列名称相同不代表所有变体都支持视觉。图片还会占用更多上下文和免费额度。

## 思考与工具调用

### 思考

思考模型可能使用模型专属参数或返回格式。若修改思考选项后报错：

1. 恢复为**默认**；
2. 清除自定义参数；
3. 对照模型页示例；
4. 重新运行健康检查。

### MCP 与工具调用

Cherry Studio MCP 要求模型能输出结构化 Tool Calling。

1. 先完成普通对话；
2. 只启用一个简单 MCP 工具；
3. 明确要求调用；
4. 检查是否真正产生结构化调用；
5. 确认结果能回传给模型；
6. 再增加工具。

ModelScope 平台的 MCP 广场与 ModelScope 模型服务是两项不同功能。模型 Access Token 可以用于相应平台能力，但在 Cherry Studio 中仍需分别配置“模型服务”和“MCP 服务器”。

## 图片生成与编辑

Cherry Studio V2 为 ModelScope 实现了专用异步图片生成链路：

1. 向 `/v1/images/generations` 提交任务；
2. 获取 `task_id`；
3. 轮询 `/v1/tasks/{task_id}`；
4. 任务成功后读取图片 URL。

选择 ModelScope 当前支持的 AIGC 模型后，可以在绘画页面使用：

- 图片尺寸；
- 负面提示词；
- 采样步数；
- Guidance；
- Seed；
- 支持模型的图片编辑输入；
- 支持模型的 LoRA。

不同模型支持的尺寸、步数、Guidance 和编辑能力不同。应以模型详情页给出的范围为准。

图片任务是异步执行的，等待时间可能明显长于对话。取消任务、网络中断、额度不足或平台高负载都可能导致轮询失败。

## 嵌入模型与知识库

Cherry Studio 的 ModelScope 服务商实现了 OpenAI 兼容 Embeddings 调用，但只有实际提供兼容 Embedding API 的 ModelScope 模型才能使用。

1. 在模型页确认任务类型与 API 示例；
2. 添加完整 Model ID；
3. 确认 Cherry Studio 将其识别为嵌入模型；
4. 在知识库中检测维度；
5. 运行健康检查；
6. 再导入文档。

模型或维度一旦用于现有知识库，不应随意更换；否则通常需要重建向量索引。

## PDF 与附件

当前 V2 会先在本地提取 PDF 文本，再发送给 ModelScope 对话模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用上下文与免费调用额度；
- PDF 中的图片需要单独发送给视觉模型。

ModelScope 是云端服务。上传前应确认文档符合隐私和组织安全要求。

## 额度与限流

ModelScope 当前的免费 API-Inference 规则包括：

- 每个注册用户每天总计最多 2,000 次调用；
- 单个模型通常每天最多 200 次调用；
- 部分大模型可能进一步限制为每天 100 次或更少；
- 并发会随平台负载动态调整；
- AIGC 模型可能有独立限制；
- 具体模型额度可随时动态变化。

服务返回的响应头可以包含：

| 响应头 | 含义 |
| --- | --- |
| `modelscope-ratelimit-requests-limit` | 用户每日总额度 |
| `modelscope-ratelimit-requests-remaining` | 用户每日剩余额度 |
| `modelscope-ratelimit-model-requests-limit` | 当前模型每日额度 |
| `modelscope-ratelimit-model-requests-remaining` | 当前模型剩余额度 |

Cherry Studio 当前不会把这些响应头当作完整账单页面展示。额度判断应结合错误信息、ModelScope 页面和平台最新规则。

不应通过创建或切换备用账号规避平台限制。免费额度用于体验和原型，批量调用应迁移到合适的商业服务。

## API-Inference 与 API-Provider

ModelScope 还提供 API-Provider，可绑定外部 API 提供商。它与免费 API-Inference 的额度和计费来源不同。

- API-Inference：由 ModelScope 提供体验型推理资源；
- API-Provider：调用绑定的外部提供商，不受免费 API-Inference 同一限额约束，但受外部服务商计费与限制。

本页的默认 `api-inference.modelscope.cn` 配置指向 API-Inference。不要在不理解计费来源的情况下混用外部提供商凭据。

## 常见问题

### 返回 401

Access Token 错误、已删除、包含空格或没有正确发送。重新复制 Token，并确认 Base URL 未被代理改写。

### 返回 403

账号可能未绑定阿里云、未完成实名认证，或模型权限受限。先在 ModelScope 网页完成账户要求。

### 返回 404

模型 ID 错误、模型已下线或 Base URL 不正确。检查完整 ID 和模型页 API-Inference 状态。

### 返回 429

可能达到用户总额度、单模型额度、AIGC 独立额度或动态并发限制。降低频率并等待额度恢复；生产需求应换用商业服务。

### 模型列表为空

检查 Token、Base URL 和网络。也可以从模型页复制当前支持的完整 Model ID 后手动添加。

### 预设模型无法使用

V2 预设可能早于平台下线或改名。以 ModelScope 当前模型页为准，重新同步或换用仍支持的模型。

### 图片生成一直等待

任务仍在队列、平台繁忙、轮询网络失败或额度不足。检查 ModelScope 任务状态并降低并发。

### 图片编辑参数错误

目标模型可能不支持编辑、输入尺寸不合规，或需要特定的 `image_url`。对照模型页示例和参数范围。

### MCP 无法使用

先确认模型支持工具调用。ModelScope MCP 广场的服务还需要在 Cherry Studio 的 MCP 设置中单独同步或添加。

### 需要稳定高并发

免费 API-Inference 不适合 SLA 或商业高并发。使用 ModelScope API-Provider、其他商业模型服务，或部署开源模型。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。ModelScope 的模型、接口与最新额度请参阅 [API-Inference 文档](https://modelscope.cn/docs/model-service/API-Inference/intro)和[使用限制](https://modelscope.cn/docs/model-service/API-Inference/limits)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
