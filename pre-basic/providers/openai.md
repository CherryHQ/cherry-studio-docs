---
icon: key
---

# OpenAI

Cherry Studio V2 的 OpenAI 内置模板用于连接 OpenAI 官方 API，默认使用 **OpenAI Responses** 接口。准备好 OpenAI API Key 后，可以同步账户可用模型并在对话中使用。

{% hint style="warning" %}
OpenAI 模板不再用于第三方 OpenAI 兼容网关。若你的 Base URL 不是 OpenAI 官方地址，请新建[自定义服务商](zi-ding-yi-fu-wu-shang.md)，并按网关要求选择 OpenAI Chat Completions 或 OpenAI Responses。
{% endhint %}

## 开始前准备

- 可访问 OpenAI API 的账户；
- 在 [OpenAI API Keys](https://platform.openai.com/api-keys) 创建的 API Key；
- 已为 API 账户开通的模型与可用额度；
- 符合 OpenAI 最新地区与账户要求的网络环境。

ChatGPT 网页或客户端的登录状态不会自动写入 Cherry Studio。Cherry Studio 需要 API Key 才能调用 OpenAI API。

## 配置 OpenAI

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部**，选择 **OpenAI**；
3. 输入 API Key；
4. 保留默认 Base URL `https://api.openai.com`；
5. 打开页面顶部的服务商开关；
6. 在模型列表点击**添加**，检查同步预览并应用变更；
7. 启用准备使用的模型。

{% hint style="danger" %}
API Key 只会在创建时完整显示。不要把它写入聊天消息、文档、代码仓库或问题截图；泄露后应立即在 OpenAI 控制台撤销并重新创建。
{% endhint %}

## 为什么默认使用 Responses

V2 的 OpenAI 模板预设 `openai-responses` 端点。该模板面向 OpenAI 官方当前接口，应用会根据模型能力处理文本、推理、工具调用等请求。

如果第三方网关只支持 `/v1/chat/completions`：

1. 不要修改 OpenAI 内置模板来连接它；
2. 点击服务商列表搜索框旁的 `+`；
3. 创建自定义服务商；
4. 将 OpenAI Chat Completions 设为主要端点；
5. 填写网关提供的 Base URL、API Key 和模型 ID。

这样可以保留官方 OpenAI 模板，也避免 Responses 与 Chat Completions 协议不匹配。

## 同步并启用模型

点击**添加**后，Cherry Studio 会从服务商同步模型列表，并在应用前显示新增、更新与移除项。

- 只启用实际需要的模型，模型选择器会更简洁；
- 同名模型存在多个版本时，核对完整模型 ID；
- 接口未返回模型时，可以点击**自定义**并手动填写官方模型 ID；
- 不要把其他网关的模型 ID 直接添加到 OpenAI 官方模板。

模型可用性由 OpenAI 账户权限决定。Cherry Studio 能识别模型，不代表你的账户已经获得访问权限。

## 检查连接

1. 在 API Key 区域点击连接检查；
2. 选择一个已同步并启用的模型；
3. 确认检查成功；
4. 再运行模型健康检查；
5. 回到对话界面发送一条简单消息。

如果使用推理或工具调用模型，再分别测试一次思考设置与工具调用，不要只依赖模型名称判断能力。

## 可选设置

OpenAI 模板支持服务层级等请求选项。对话顶部的模型设置中可能显示**服务层级**，默认使用**自动**即可。

只有在你明确了解 OpenAI 对相应模型的支持和计费方式时，才选择其他层级。服务商请求配置中的能力开关也不应随意更改；错误声明支持项可能导致请求失败。

## 常见问题

### 页面提示“不再支持旧的调用方式”

这是 V2 对 OpenAI 内置模板的提示。官方 OpenAI API 使用当前模板；第三方兼容 API 请创建自定义服务商。

### 返回 401

API Key 无效、已撤销或复制不完整。重新创建 Key，并确认没有多余空格。

### 返回 403

账户、地区、组织或模型权限可能不满足要求。请在 OpenAI 控制台检查账户状态和模型访问权限。

### 返回余额或配额错误

检查 API 账户的额度、计费状态和使用限制。切换模型不会绕过账户级限制。

### 返回 404 或模型不存在

重新点击**添加**同步列表，并核对模型 ID。若正在连接第三方网关，请改用自定义服务商并选择正确端点。

### 模型可以对话，但不能调用工具

检查模型能力标签和 OpenAI 对该模型的工具支持。先使用一个简单工具测试，再逐步增加 MCP 或其他工具。

更多通用设置见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
