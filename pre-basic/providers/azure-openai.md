---
icon: cloud
---

# Azure OpenAI

Cherry Studio V2 的 Azure OpenAI 内置模板用于连接部署在 Microsoft Azure 上的模型。它会根据 **API Version** 选择 Azure Responses 或部署式调用方式，因此 Base URL、API Version 和模型 ID 必须与 Azure 资源中的配置对应。

{% hint style="info" %}
Azure OpenAI 与 OpenAI 官方 API 是两个独立服务。Azure 资源的 Endpoint、API Key、API Version 和部署名称不能直接填入 OpenAI 模板。
{% endhint %}

## 开始前准备

在 [Azure Portal](https://portal.azure.com/) 准备以下信息：

- Azure AI Foundry 或 Azure OpenAI 资源的 Endpoint；
- 该资源对应的 API Key；
- 当前资源支持的 API Version；
- 至少一个可调用的模型部署。

若使用日期格式的 API Version，还需要记住每个模型的**部署名称**。部署名称由你在 Azure 中设置，可能与底层模型名称不同。

## 配置 Azure OpenAI

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **Azure OpenAI**；
3. 输入 Azure 资源的 API Key；
4. 在 Base URL 中填写资源 Endpoint，例如 `https://<resource>.openai.azure.com`；
5. 填写 Azure 资源当前支持的 API Version；
6. 打开页面顶部的服务商开关；
7. 添加并启用准备使用的模型；
8. 运行连接检查和模型健康检查。

{% hint style="warning" %}
Base URL 只填写资源 Endpoint。不要追加 `/openai`、`/v1`、`/chat/completions` 或部署路径；Cherry Studio 会根据当前配置补充请求路径。
{% endhint %}

{% hint style="danger" %}
不要把 Azure API Key 写入聊天消息、文档、代码仓库或问题截图。Key 泄露后，应立即在 Azure Portal 中重新生成。
{% endhint %}

## 选择 API Version

Cherry Studio 会根据 API Version 选择调用方式：

| API Version | Cherry Studio 的处理方式 | 模型配置要点 |
| --- | --- | --- |
| `v1` 或 `preview` | 使用 Azure Responses 方式 | 按当前 Azure 资源提供的模型路由配置 |
| 日期格式版本，例如 `2024-xx-xx-preview` | 使用 Azure 部署式 URL | 模型 ID 应与 Azure 中的部署名称一致 |

API Version 必须是 Azure 资源实际支持的值。界面中的示例只说明格式，不代表该版本一定适用于你的资源。

如果现有连接升级后突然返回 404，先到 Azure Portal 或 [Azure OpenAI 文档](https://learn.microsoft.com/azure/ai-services/openai/)核对当前 Endpoint、API Version 和部署名称，再修改 Cherry Studio。

## 添加并启用模型

在模型列表点击**添加**，检查同步预览并应用变更。若 Azure 未返回可用列表，可以点击**自定义**手动填写模型。

使用日期格式 API Version 时：

- **模型 ID**填写 Azure 中的部署名称；
- 不要只填写底层模型家族名称，除非它刚好也是部署名称；
- 多个部署需要分别添加；
- 删除或重命名 Azure 部署后，也要同步修改 Cherry Studio 中的模型。

例如，Azure 中把某个模型部署为 `support-prod`，则 Cherry Studio 中的模型 ID 应填写 `support-prod`，而不是根据底层模型名称猜测。

## 检查连接

1. 确认 Base URL 没有附加 API 路径；
2. 确认 API Key 来自同一个 Azure 资源；
3. 确认 API Version 受该资源支持；
4. 选择一个已添加并启用的模型；
5. 运行连接检查；
6. 再运行模型健康检查；
7. 回到对话界面发送一条简单消息。

连接检查成功只说明凭据和基本请求可用。若准备使用图片、推理或工具调用，还应分别验证对应模型与部署是否支持这些能力。

## 管理多个资源或部署

如果不同 Azure 资源使用不同 Endpoint、Key 或 API Version，可以复制 Azure OpenAI 服务商并分别配置：

- 为每个副本设置容易识别的名称；
- 每个副本只保留该资源真实存在的部署；
- 不要在一个副本中混用其他资源的 Key 或部署名称；
- 升级 API Version 时先测试一个副本，再更新其他连接。

这样能把生产、测试或不同区域的资源隔离开，也更容易定位配额与权限问题。

## 常见问题

### 返回 401

API Key 无效、复制不完整，或 Key 与 Base URL 不属于同一个 Azure 资源。重新从资源的 Keys and Endpoint 页面核对。

### 返回 404

依次检查 Base URL、API Version 和模型部署名称。最常见的原因是附加了多余路径、日期版本不受支持，或把底层模型名当成了部署名称。

### 返回 429

当前资源、区域或部署达到速率或配额限制。请在 Azure Portal 检查配额和使用量；切换 Cherry Studio 中的模型名称不会绕过资源限制。

### 同步不到模型

部分 Azure 配置不会返回适合直接使用的模型列表。点击**自定义**，按 Azure 中的实际部署添加模型，再运行健康检查。

### `v1`、`preview` 与日期版本应该选哪个

以 Azure 资源和官方文档当前支持的方式为准。`v1` 或 `preview` 会走 Responses 方式；日期版本会走部署式 URL。不要仅凭模型名称切换 API Version。

更多通用设置见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
