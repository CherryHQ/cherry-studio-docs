---
icon: cloud
---

# Vertex AI

Cherry Studio V2 的 Vertex AI 内置模板通过 Google Cloud **Service Account** 连接 Vertex AI。它需要项目 ID、地区、Service Account 客户端邮箱和私钥，不使用 Gemini API Key。

V2 既能调用 Vertex AI 上的 Gemini 模型，也能为可用的 Claude 模型选择 Vertex Anthropic 路由；最终可用范围取决于项目、地区、权限和 Model Garden 的实际开放情况。

{% hint style="info" %}
Google AI Studio 的 Gemini API Key 不能直接用于本页配置。若只有 Gemini API Key，请使用 [Google Gemini](google-gemini.md) 服务商。
{% endhint %}

## 开始前准备

在 Google Cloud 中完成以下准备：

- 选择或创建一个 Google Cloud 项目；
- 为项目启用结算；
- 启用 Vertex AI API；
- 创建专用于 Cherry Studio 的 Service Account；
- 为该账号授予调用目标模型所需的最小权限；
- 创建并安全下载 Service Account JSON 密钥；
- 确认目标模型可用的 Location。

Google 官方快速入门通常要求调用者具有 **Vertex AI User**（`roles/aiplatform.user`）权限。企业项目可能使用自定义 IAM 角色，请按组织策略由管理员授权。

相关入口：

- [Vertex AI 快速入门](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)
- [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)

## 从 JSON 密钥中读取字段

Cherry Studio 当前需要手动填写以下内容：

| Cherry Studio 字段 | Service Account JSON 或 Google Cloud 中的值 |
| --- | --- |
| 客户端邮箱 | `client_email` |
| 私钥 | `private_key`，包含完整的 BEGIN/END 行 |
| 项目 ID | `project_id` |
| 地区 | 目标模型实际可用的 Location，例如 `us-central1` |

复制私钥时应保留原有换行和 `-----BEGIN PRIVATE KEY-----`、`-----END PRIVATE KEY-----`。

{% hint style="danger" %}
Service Account 私钥属于高敏感凭据。不要把完整 JSON、`private_key` 或客户端配置页写入聊天消息、文档、代码仓库和问题截图。泄露后应立即在 Google Cloud 中删除该密钥并创建新密钥。
{% endhint %}

## 配置 Vertex AI

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **VertexAI**；
3. 在 **客户端邮箱**填写 JSON 的 `client_email`；
4. 在 **私钥**填写完整的 `private_key`；
5. 在 **项目 ID**填写 `project_id`；
6. 在 **地区**填写目标模型可用的 Location；
7. 保持 API 地址为空；
8. 打开页面顶部的服务商开关；
9. 添加并启用准备使用的模型。

{% hint style="warning" %}
Vertex AI 的 API 地址通常由项目和地区自动生成，不建议手动填写。只有在明确使用反向代理并了解其完整路径时才修改。
{% endhint %}

## 添加并选择模型

在模型列表点击**添加**，检查同步预览并应用变更。若远端没有返回目标模型，可以点击**自定义**并填写 Model Garden 或 Google 官方文档中的模型 ID。

- Gemini 模型使用 Google Generate Content 能力；
- Claude 模型会使用 Vertex Anthropic 路由；
- 模型必须在当前项目和 Location 中可用；
- 第三方模型可能需要额外启用、授权或接受条款；
- 模型名称、地区和版本需要同时对应，不能只复制其他项目中的模型 ID。

旧版文档中“暂时不支持 Claude”的说明已经不适用于 V2，但代码支持路由不等于你的 Google Cloud 项目已经获得该模型权限。

## 检查连接

1. 确认四个必填字段均来自同一个 Service Account 和项目；
2. 确认 Vertex AI API 已启用；
3. 确认 Service Account 具有所需 IAM 权限；
4. 选择一个已添加并启用的模型；
5. 运行连接检查；
6. 再运行模型健康检查；
7. 回到对话界面发送一条简单消息。

如果 Gemini 可用而 Claude 不可用，优先检查 Claude 是否在当前项目、地区和 Model Garden 中开放，而不是修改 Gemini 配置。

## 管理多个项目或地区

不同项目或地区使用不同凭据时，可以复制 VertexAI 服务商并分别配置：

- 名称中标记项目或地区；
- 每个副本只保留该环境可用的模型；
- 不要混用项目 A 的 Service Account 与项目 B 的项目 ID；
- 轮换密钥时逐个副本验证；
- 生产与测试环境使用不同 Service Account。

这样可以降低权限范围，也更容易区分配额、地区和模型可用性问题。

## 常见问题

### 提示 VertexAI 未配置

项目 ID、Location、客户端邮箱或私钥至少有一项为空。检查私钥是否完整，并在字段失焦后等待设置保存。

### 返回 401 或认证失败

Service Account 密钥无效、已删除、私钥格式损坏，或客户端邮箱与私钥不匹配。重新从同一份 JSON 核对字段。

### 返回 403

Vertex AI API 未启用，Service Account 缺少 IAM 权限，或目标模型尚未对项目开放。请在 Google Cloud 中检查项目、API 和角色。

### 返回 404 或模型不存在

模型 ID、项目或 Location 不匹配。到 Model Garden 核对目标模型支持的地区，再更新 Cherry Studio。

### 返回 429

当前项目、地区或模型达到配额限制。请在 Google Cloud Console 中检查配额和用量。

### Gemini 可以使用，Claude 不能使用

确认 Claude 模型已在当前项目和地区开放，并使用完整、正确的模型 ID。Vertex AI 的 Gemini 权限不会自动授予第三方模型权限。

更多通用设置见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
