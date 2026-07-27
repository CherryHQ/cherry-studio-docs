---
icon: key
---

# Anthropic

Cherry Studio V2 的 Anthropic 内置模板用于连接 Anthropic 官方 API，默认使用 **Anthropic Messages** 端点。完成 API Key 配置后，可以同步 Claude 模型并用于对话、推理和工具调用。

{% hint style="info" %}
服务商具有 Anthropic 端点，不等于其中每个模型都支持工具调用或 Agent。请查看模型能力标签，并在使用前完成一次实际工具测试。
{% endhint %}

## 开始前准备

- 可使用 Anthropic API 的账户；
- 在 [Anthropic API Keys](https://console.anthropic.com/settings/keys) 创建的 API Key；
- 账户已开通的模型与可用额度；
- 符合 Anthropic 最新账户与地区要求的网络环境。

Anthropic API Key 与网页端登录状态是不同的配置。Cherry Studio 需要可用于 API 请求的 Key。

## 配置 Anthropic

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **Anthropic**；
3. 输入 API Key；
4. 保留默认 Base URL `https://api.anthropic.com`；
5. 打开页面顶部的服务商开关；
6. 在模型列表点击**添加**，检查同步预览并应用变更；
7. 启用准备使用的 Claude 模型。

{% hint style="danger" %}
不要把 API Key 写入聊天消息、文档、代码仓库或问题截图。泄露后应立即在 Anthropic Console 撤销并重新创建。
{% endhint %}

## 同步并选择模型

Anthropic 的模型名称和版本会调整，本文不写死具体清单。点击**添加**同步账户当前可用模型，并核对完整模型 ID。

- 只启用实际需要的模型；
- 同系列不同版本可能具有不同上下文、推理和工具能力；
- 接口没有返回模型时，可以点击**自定义**并填写 Anthropic 官方文档中的模型 ID；
- 不要把第三方网关的模型 ID 直接添加到官方 Anthropic 模板。

模型出现在 Cherry Studio 注册表中，不代表你的 Anthropic 账户已经获得访问权限。

## 检查连接

1. 在 API Key 区域发起连接检查；
2. 选择一个已同步并启用的模型；
3. 确认检查成功；
4. 在模型列表运行健康检查；
5. 回到对话界面发送一条简单消息。

如果准备使用 MCP 或 Agent，再启用一个简单工具并验证模型是否真正发起调用。

## Agent 与工具调用

Anthropic 模板会出现在模型服务列表的 **Agent** 筛选中，因为它具有 Anthropic 兼容端点。使用时仍需同时满足：

- 目标模型带有工具调用能力；
- 当前 API 端点开放工具调用；
- MCP 或其他工具已正确启用；
- 助手没有关闭工具；
- 请求没有被服务商权限或安全策略阻止。

若模型只输出工具调用计划，却没有实际执行，请先用单个简单工具排查，再检查模型能力和端点。

## Prompt Cache

Anthropic 端点可以在 Cherry Studio 的 **API 设置**中配置 Prompt Cache：

- **缓存 Token 阈值**：消息超过该数量后才启用缓存；设为 `0` 表示关闭；
- **缓存系统消息**：决定是否缓存系统提示词；
- **缓存最后 N 条消息**：控制最近对话消息的缓存数量。

{% hint style="warning" %}
缓存是否生效、如何计费以及支持哪些模型，由服务商决定。不了解服务商规则时保持默认值；错误配置不一定降低成本。
{% endhint %}

## 连接 Anthropic 兼容网关

如果使用的不是 Anthropic 官方 API：

1. 在左侧服务商列表中右键 Anthropic；
2. 选择复制或新增同类服务商；
3. 为副本填写网关提供的 Base URL 和 API Key；
4. 保留 Anthropic Messages 作为主要端点；
5. 同步或手动添加该网关实际提供的模型。

使用独立副本可以避免覆盖官方 Anthropic 模板，也方便分别排查端点和权限。

## 常见问题

### 返回 401

API Key 无效、已撤销或复制不完整。重新创建 Key，并确认没有多余空格。

### 返回 403

账户、地区、工作区或模型权限可能不满足要求。请在 Anthropic Console 检查账户状态。

### 返回 404 或模型不存在

重新点击**添加**同步列表，核对完整模型 ID。使用第三方网关时，确认 Base URL 和 Anthropic Messages 路径符合网关文档。

### 模型没有出现在 Agent 筛选中

Agent 筛选按服务商是否具有 Anthropic 端点判断。自定义网关需要正确配置 Anthropic Messages 端点；模型本身还需要工具调用能力。

### Prompt Cache 没有效果

确认缓存阈值大于 `0`，并检查服务商与模型是否支持缓存。短对话可能达不到设置的阈值。

更多通用设置见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
