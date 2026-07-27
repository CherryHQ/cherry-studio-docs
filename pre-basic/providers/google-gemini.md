---
icon: gem
---

# Google Gemini

Cherry Studio V2 的 Gemini 内置模板用于连接 Google 官方 Gemini API，默认使用原生 **Google Generate Content** 端点。完成 API Key 配置后，可以同步当前账户可用的 Gemini 模型。

{% hint style="info" %}
Gemini API 与 Google Cloud Vertex AI 是两种不同的接入方式。本页使用 Google AI Studio 创建的 API Key；若使用 Google Cloud 项目、区域和服务账号，请参阅 Vertex AI 文档。
{% endhint %}

## 开始前准备

- 可访问 Google AI Studio 和 Gemini API 的 Google 账户；
- 所在地区符合 Google 当前的[可用地区要求](https://ai.google.dev/gemini-api/docs/available-regions)；
- 已阅读并接受 Gemini API 的相关条款；
- 已准备可用的 API Key 和模型配额。

Google AI Studio 可能会为新用户自动创建默认 Google Cloud 项目和 API Key。已有项目的用户也可以在 AI Studio 中导入或选择项目，不必为了 Cherry Studio 重复创建项目。

## 创建 API Key

1. 打开 [Google AI Studio API Keys](https://aistudio.google.com/app/apikey)；
2. 登录并选择准备使用的 Google Cloud 项目；
3. 创建新的 Gemini API Key；
4. 复制 Key，并立即保存到安全的位置；
5. 回到 Cherry Studio 完成配置。

{% hint style="danger" %}
不要把 API Key 写入聊天消息、文档、代码仓库或问题截图。Google 可能阻止被公开泄露或不符合限制要求的 Key；泄露后应在 AI Studio 中删除并重新创建。
{% endhint %}

## 配置 Gemini

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **Gemini**；
3. 输入从 Google AI Studio 创建的 API Key；
4. 保留默认 Base URL `https://generativelanguage.googleapis.com`；
5. 打开页面顶部的服务商开关；
6. 在模型列表点击**添加**，检查同步预览并应用变更；
7. 启用准备使用的模型。

Gemini 内置模板使用 Google 原生端点。不要为官方 Gemini API 改成 OpenAI Chat Completions 或 OpenAI Responses。

## 同步并选择模型

点击**添加**后，Cherry Studio 会调用 Gemini 的模型列表接口，并把远端结果与内置模型信息合并后显示。

- 只启用实际需要的模型；
- 核对完整模型 ID，不要只看显示名称；
- Stable、Preview、Latest 和 Experimental 版本的稳定性与生命周期不同；
- 接口没有返回目标模型时，可以点击**自定义**并填写 Google 官方文档中的模型 ID；
- 模型出现在列表中，不代表当前 Key 一定具有调用权限或剩余额度。

Google 会持续调整模型版本。请以 [Gemini 模型文档](https://ai.google.dev/gemini-api/docs/models/gemini)和实际同步结果为准，不要依赖旧截图中的固定清单。

## 检查连接

1. 在 API Key 区域运行连接检查；
2. 选择一个已同步并启用的文本模型；
3. 确认检查成功；
4. 在模型列表运行健康检查；
5. 回到对话界面发送一条简单消息。

如果准备使用图片理解、图片生成、推理或工具调用，再分别测试对应功能。模型名称相近，不代表能力和请求参数完全相同。

## 推理与工具调用

Cherry Studio 会根据模型注册信息显示推理和工具能力，并为支持的 Gemini 模型转换思考参数。使用时仍需满足：

- 当前模型版本支持相应能力；
- API Key 对该模型具有权限和配额；
- 模型能力标签与实际端点一致；
- MCP 或其他工具已经启用；
- 请求参数没有超过模型限制。

若升级模型后推理或工具调用异常，先重新同步模型，再用简单对话和单个工具分别排查。

## 连接 Gemini 兼容网关

如果使用的不是 Google 官方 Gemini API：

1. 新建[自定义服务商](zi-ding-yi-fu-wu-shang.md)；
2. 将 Google Generate Content 设为主要端点；
3. 填写网关提供的 Base URL 和 API Key；
4. 同步或手动添加该网关实际提供的模型；
5. 运行连接检查和模型健康检查。

使用独立自定义服务商可以保留官方 Gemini 模板，也避免把网关路径或模型 ID 混入官方配置。

## 常见问题

### 返回 400

模型不支持当前参数，或请求超过输入限制。先用纯文本短消息测试，再逐步启用图片、推理和工具。

### 返回 401 或 API Key 无效

Key 复制不完整、已删除或已被阻止。到 Google AI Studio 检查状态；若 Key 曾公开泄露，请重新创建。

### 返回 403

账户、项目、地区或模型权限不满足要求。检查当前 Key 所属项目、[可用地区](https://ai.google.dev/gemini-api/docs/available-regions)和 Google 账户状态。

### 返回 404 或模型不存在

重新点击**添加**同步模型，核对完整模型 ID。Preview、Latest 或 Experimental 模型可能已经更名或停止提供。

### 返回 429

当前项目或模型达到速率或配额限制。检查 Google AI Studio 中的用量和计费状态，稍后重试或更换有可用配额的模型。

### 同步不到模型

确认使用 Google AI Studio 创建的 Gemini API Key，并保留官方 Base URL。也可以参考官方[模型列表接口](https://ai.google.dev/api/models)核对 Key 是否能列出模型。

更多通用设置见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
