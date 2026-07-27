# 华为云 ModelArts Studio（MaaS）

华为云 ModelArts Studio（MaaS）提供内置模型和自定义部署模型的推理 API。Cherry Studio V2 当前没有内置“华为云”服务商，需要创建一个 **OpenAI 兼容自定义服务商**。

{% hint style="info" %}
旧教程要求把完整 `/chat/completions` 地址填入 API Host 并追加 `#`。V2 不需要这种历史兼容写法，应从完整调用地址中移除 `/chat/completions`，只保留 Base URL。
{% endhint %}

## 先选择接入方式

华为云 MaaS 常见两类调用方式：

| 方式 | 地址特征 | Cherry Studio 配置 |
| --- | --- | --- |
| MaaS 标准 API | 多个内置模型共用 `/v1` 或 `/v2` Base URL | 通常一个自定义服务商即可 |
| 自定义实时推理服务 | 每个服务可能有独立 URL、Endpoint 或路径 | 不同 Base URL 需要分别建服务商 |

本文只适用于使用 Bearer API Key 的 OpenAI 兼容 MaaS 服务。旧版 ModelArts 的 IAM Token、AppKey/AppSecret、AppCode 或签名鉴权不能直接填入 Cherry Studio 的普通 API Key 输入框。

## 地域与版本

MaaS 的可用地域、API Key 和模型列表相互关联，不能跨地域混用。

华为云当前国际站文档中的 MaaS Standard API V2 示例为：

```text
https://api-ap-southeast-1.modelarts-maas.com/v2/chat/completions
```

在 Cherry Studio 中应填写：

```text
https://api-ap-southeast-1.modelarts-maas.com/v2
```

MaaS Standard API V1 已不再继续演进。新配置优先使用控制台提供的 V2 地址；已有 V1 服务仍应以控制台“调用说明”为准。

{% hint style="warning" %}
不要直接照抄本文示例地址。先在自己的华为云地域和服务页面查看调用说明；如果控制台给出的域名或版本不同，应使用控制台地址。
{% endhint %}

## 开通 MaaS

1. 注册并登录[华为云](https://auth.huaweicloud.com/authui/login)；
2. 切换到 MaaS 当前支持的地域；
3. 打开 ModelArts Studio（MaaS）；
4. 按控制台提示完成 IAM 授权；
5. 在模型广场选择模型；
6. 开通内置服务，或部署为实时推理服务；
7. 等待服务状态变为可调用。

自定义部署会使用计算和存储资源并产生费用。不要在不理解计费方式的情况下选择“全部部署”。

## 创建 API Key

### 内置 MaaS 服务

1. 打开 MaaS 的 API Key 管理；
2. 点击**创建 API Key**；
3. 设置标签；
4. 按需配置 IP、模型或自定义 Endpoint 白名单；
5. 创建后立即复制并保存。

### 自定义实时推理服务

1. 打开 `模型推理 → 实时推理 → 我的服务`；
2. 找到正在运行的服务；
3. 选择`更多 → 查看调用说明`；
4. 点击**创建 API Key**；
5. 设置权限并复制 Key；
6. 同时复制完整 API URL 和模型参数。

MaaS Key 创建后可能需要几分钟才生效。

{% hint style="danger" %}
API Key 只在创建时显示一次。不要写入聊天、文档、代码仓库或问题截图；遗失或泄露后应删除并重新创建。
{% endhint %}

## 从完整 URL 提取 Base URL

假设控制台给出的完整地址是：

```text
https://example.com/v2/chat/completions
```

Cherry Studio 应填写：

```text
https://example.com/v2
```

处理规则：

1. 删除末尾 `/chat/completions`；
2. 保留 `/v1` 或 `/v2`；
3. 不追加 `#`；
4. 不把模型名称拼进 URL；
5. 不把控制台网页 URL 当作 API URL。

如果自定义服务的调用说明使用不同路径，应先确认它兼容 OpenAI Chat Completions。非兼容接口不能仅靠删除路径接入。

## 在 Cherry Studio 创建自定义服务商

1. 打开 `设置 → 模型服务`；
2. 点击**添加服务商**；
3. 输入名称，例如 `Huawei Cloud MaaS`；
4. 选择 **OpenAI 兼容**类型；
5. 粘贴 MaaS API Key；
6. 填写提取后的 Base URL；
7. 打开服务商开关；
8. 同步模型或手动添加 Model ID；
9. 只启用准备使用的模型；
10. 运行模型健康检查。

如果所有模型共用同一个 MaaS Standard API Base URL，可以放在一个服务商中。只有 Base URL、鉴权或代理路径不同，才需要再建服务商。

## 获取与同步模型

MaaS 标准 API 提供模型列表接口：

```text
GET /v1/models
GET /v2/models
```

具体使用哪个版本取决于控制台给出的 Base URL。

同步后：

1. 检查返回的 Model ID；
2. 应用同步结果；
3. 确认模型类型；
4. 逐个运行健康检查。

如果自定义服务不提供模型列表接口：

1. 在“调用说明”中复制 `model` 参数；
2. 在 Cherry Studio 手动添加；
3. 保持大小写与标点完全一致；
4. 运行健康检查。

{% hint style="warning" %}
API Key 可以设置模型和自定义 Endpoint 白名单。模型存在但返回 401 时，应同时检查 Key 权限，而不是只重新复制 Key。
{% endhint %}

## 对话模型

MaaS 标准 API 使用 OpenAI 兼容 Chat Completions。

建议按以下顺序测试：

1. 发送一条简短的纯文本消息；
2. 检查流式输出；
3. 增加系统提示词；
4. 测试较长上下文；
5. 再测试思考、图片和工具调用。

不同模型允许的 `role`、上下文长度和输出参数不同。出现 400 时，应对照该模型的 MaaS API 调用规范。

## 思考模式

华为云 MaaS 上的不同模型可能使用：

- `reasoning_content`
- `thinking`
- `chat_template_kwargs`
- 模型专属开关

Cherry Studio 当前没有华为云专用参数适配。V2 对通用 OpenAI 兼容服务商生成的思考参数，未必与某个 MaaS 模型完全一致。

如果开启思考后报错：

1. 将思考设置恢复为**默认**；
2. 清除模型自定义参数；
3. 先确认普通对话可用；
4. 查看 MaaS 中该模型的请求示例；
5. 只添加官方明确要求的参数。

不要把一个模型的 `chat_template_kwargs` 复制给其他模型。

## 视觉与多模态

只有 MaaS 明确标记为视觉或多模态的模型才能接收图片。

测试时：

1. 添加准确 Model ID；
2. 确认 Cherry Studio 显示图片能力；
3. 先上传一张小图片；
4. 检查模型是否真正理解内容；
5. 再尝试多图或大文件。

自定义实时服务即使部署了视觉模型，也必须使用 OpenAI 兼容的图片消息格式，才能直接从 Cherry Studio 接入。

## MCP 与工具调用

MaaS Standard API V2 的部分模型支持 Tool Calling，但最终能力取决于模型。

1. 先完成普通对话；
2. 只启用一个简单 MCP 工具；
3. 明确要求调用；
4. 检查是否产生结构化调用；
5. 确认工具结果能回传给模型；
6. 再增加工具。

模型只用文字描述“将要调用工具”不等于真实调用。应检查模型、API 版本和工具格式。

## Embedding、Rerank 与图片生成

Cherry Studio 当前没有华为云专用 Embedding、Rerank 或图片生成适配。

只有满足以下条件时才应尝试：

1. MaaS 服务提供对应的 OpenAI 兼容接口；
2. Cherry Studio 能为模型选择正确的 Endpoint Type；
3. 请求和响应格式与 V2 兼容；
4. 健康检查或实际小样本测试通过。

不要因为 MaaS 控制台支持某种模型，就假定 Cherry Studio 知识库或绘画页面已经接入。

对于知识库，最稳妥的做法是使用已由 V2 明确支持的 Embedding 与 Rerank 服务商；对于图片生成，使用绘画页面实际列出的服务商和模型。

## PDF 与附件

当前 V2 会先在本地提取 PDF 文本，再发送给 MaaS 对话模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用模型上下文和费用；
- PDF 中的图片需要单独发送给视觉模型。

这不等同于华为云原生文件上传或文档理解 API。

上传文档、图片或知识库内容前，应确认符合数据地域、隐私和组织安全要求。

## 自定义实时服务

自定义实时服务还需要关注：

- 服务是否正在运行；
- 资源池和 OBS 是否与 MaaS 在同一地域；
- Endpoint 是否在 Key 白名单中；
- 内容审核是否开启；
- QPS 和超时；
- 计算与存储费用；
- 服务升级或停止状态。

如果每个自定义服务的 Base URL 不同，应为每个 URL 单独创建服务商。多个模型共用同一标准 Base URL 时，不需要重复创建。

## 常见问题

### 返回 401

API Key 错误、尚未生效、区域不匹配，或 IP、模型、Endpoint 不在 Key 白名单。检查 Key 权限后重试。

### 返回 403

IAM 授权、模型权限、内容审核或账户状态受限。到 MaaS 控制台查看具体错误码。

### 返回 404

Base URL、API 版本、路径或 Model ID 错误。重新从“查看调用说明”复制完整 URL，并按规则删除 `/chat/completions`。

### 返回 429

达到 MaaS、模型或自定义实时服务的 QPS / 并发限制。降低并发并等待恢复。

### 返回 400

模型不接受当前消息角色、附件或思考参数。先清除自定义参数并测试最小纯文本请求。

### 模型列表为空

自定义服务可能不提供 `/models`。从调用说明复制 `model` 参数后手动添加。

### Key 刚创建就提示无效

MaaS Key 可能需要几分钟生效。确认 Key、地域和 Base URL 后稍等再试。

### 每个模型都要建服务商吗

不一定。共用同一个 MaaS Standard API Base URL 和 Key 的模型可以放在同一服务商；只有调用地址或鉴权不同才需要拆分。

### 旧教程为什么要求追加 `#`

那是旧版 Cherry Studio 用完整接口地址时的历史兼容方式。V2 应填写去掉 `/chat/completions` 后的 Base URL，不再追加 `#`。

### 自定义服务在网页中可调用，Cherry Studio 不可用

该服务可能使用非 OpenAI 格式、旧版 AppCode/签名鉴权、自定义路径，或 Key 白名单未包含 Endpoint。普通自定义服务商无法自动适配这些差异。

### 思考开启后参数错误

恢复默认思考设置。当前 V2 没有华为云 MaaS 专用思考参数适配。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。华为云 MaaS 当前调用方式请参阅[API 调用规范](https://support.huaweicloud.com/intl/zh-cn/model-call-maas/model-call-017.html)、[MaaS Standard API V2](https://support.huaweicloud.com/intl/zh-cn/model-call-maas/model-call-019.html)、[调用模型服务](https://support.huaweicloud.com/intl/zh-cn/inference-maas/maas-modelarts-0011.html)和[API URL 格式说明](https://support.huaweicloud.com/intl/zh-cn/maas_faq/maas_faq_0005.html)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
