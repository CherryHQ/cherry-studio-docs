---
description: Tools
icon: code
---

# Code Switch 使用教程

Code Switch 可以在 Cherry Studio 内直接启动和管理多种 AI 编程 CLI 工具，例如 Claude Code、OpenAI Codex、OpenCode、Gemini CLI、Qwen Code、Kimi Code、Qoder CLI、GitHub Copilot CLI 和 OpenClaw。本教程按当前界面说明完整配置流程。

***

### 操作步骤

#### 1. 确认 Cherry Studio 版本

请先确认 Cherry Studio 已升级到当前正式版。你可以前往 [客户端下载](../cherrystudio/download.md)、[GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 或 [官方网站](https://cherryai.com.cn/download) 下载安装包。

#### 2. 进入 Code Switch 界面

点击顶部 Tab 栏的 `+` 打开启动台，然后选择 **Code Switch**。如果已经把 Code Switch 固定到左侧导航，也可以直接点击左侧图标。

<figure><img src="../.gitbook/assets/cherry-launchpad.png" alt="启动台中的 Code Switch 入口"><figcaption><p>启动台中的 Code Switch 入口</p></figcaption></figure>

#### 3. 选择 CLI 工具

根据你的需求和所持有的 API Key，选择一个要使用的 Code Agent 工具。目前支持以下几种：

* **Claude Code**
* **Qwen Code**
* **Gemini CLI**
* **OpenAI Codex**
* **GitHub Copilot CLI**
* **Kimi Code**
* **OpenCode**
* **Qoder CLI**
* **OpenClaw**

<figure><img src="../.gitbook/assets/cherry-code-tools-cli-select.png" alt=""><figcaption><p>选择 Code Agent 工具</p></figcaption></figure>

#### 4. 安装或更新 CLI

选中工具后，页面顶部会显示它的版本状态：

* 显示 **未安装** 时，点击 **安装**
* 已检测到系统或托管版本时，可直接继续配置
* 存在新版本时，可在同一状态卡片中升级

这些 CLI 并非全部随 Cherry Studio 安装包内置。页面安装失败时，可展开错误详情检查网络、代理和运行环境。

#### 5. 配置并启用服务商

除 Qoder CLI 和 GitHub Copilot CLI 外，页面会列出当前工具兼容的服务商卡片。常见入口包括：

* **统一网关**：通过 Cherry Studio 本地 API 网关使用已配置模型；启用后需要保持 Cherry Studio 运行
* **CLI 官方登录 / 官方服务**：仅在对应工具支持时显示
* **CherryIN 或其他兼容 Provider**：只有 Endpoint 协议满足该 CLI 要求时才会出现

点击卡片上的 **配置**，选择模型并调整该 CLI 的专属参数；完成后点击 **启用**，Cherry Studio 会把受管配置写入对应 CLI。Qoder CLI 与 GitHub Copilot CLI 使用各自账号认证，因此不会显示 Provider 或模型选择。

{% hint style="info" %}
服务商列表只展示兼容当前 CLI 的 Endpoint。没有看到某个 Provider 时，请先到 `设置 → 模型服务` 检查它是否配置了该 CLI 所需的 Endpoint。
{% endhint %}

#### 6. 选择工作目录并启动

CLI 已安装且配置可用后，点击状态卡片中的 **启动**。启动弹窗中：

1. 点击 **选择文件夹** 指定工作目录
2. 在 Windows 或 macOS 上，从系统检测到的终端列表中选择终端
3. 点击 **启动**

工作目录会作为 CLI 的启动目录，CLI 可按自身权限访问其中的文件和子目录。启动弹窗不提供任意环境变量编辑区，也不支持手动填写任意终端可执行文件路径；需要额外环境变量时，请在系统或目标终端中配置。

{% hint style="warning" %}
当前终端自动检测支持 Windows 和 macOS；Linux 上不会列出可启动的终端。
{% endhint %}

#### 7. 后续管理

回到同一工具页面，可以升级或移除受管 CLI。工具处于运行状态时，状态卡片还会提供停止操作；OpenClaw 则可在这里启停网关并打开 Dashboard。

***

### 重要注意事项

1. **模型兼容性说明**：
   * **Claude Code**：需要选择支持 Anthropic API Endpoint 格式的模型。优先使用 Claude 系列模型；部分官方平台也会提供 Claude Code 兼容模型，具体以模型下拉列表和服务商说明为准。
   * **Qwen Code**：支持 OpenAI Chat Completions 或 OpenAI Responses API 格式的模型，推荐使用 Qwen Coder 系列模型以获得更好的代码生成效果。
   * **Gemini CLI**：需要选择 Google Gemini 系列模型。
   * **OpenAI Codex**：需要选择支持 OpenAI Responses API Endpoint 的 Provider 与模型；仅支持 Chat Completions 的兼容服务不能用于 Codex。
   * **Kimi Code** / **OpenCode**：需选择与其平台协议相互兼容的 API 模型，通常由对应服务商官方渠道或 API 聚合网关提供。
   * **Qoder CLI** / **GitHub Copilot CLI**：使用各自账号登录，不需要在 Cherry Studio 中选择 Provider 或模型。
   * **OpenClaw**：原独立设置页已并入 Code Switch。选择 OpenClaw 后，可在这里完成 Provider / 模型选择、网关启停并打开 Dashboard。
   * **注意**：第三方网关（如 One API、New API 等）即使能转发同名模型，也不一定兼容对应 CLI 的认证方式、Endpoint 格式或工具调用协议。若启动失败，请优先使用该 CLI 官方支持的模型服务。
2. **依赖与环境冲突**：
   * Cherry Studio 会管理多种 Code Agent 的安装与配置，也会识别系统中已有的 CLI。
   * 通过页面安装 Qoder CLI 时，Cherry Studio 使用托管的 Node.js 22 运行环境，无需把 Node.js 20 作为系统 PATH 的硬性前置条件。
   * 若使用系统中已有的 CLI，请按该 CLI 的官方要求准备运行环境；发生版本冲突时，可改用页面内的托管安装，或检查 PATH 中实际命中的 CLI 版本。
3. **API Token 消耗警告**：
   * **Code Agent 对 API Token 的消耗量非常大**。在处理复杂任务时，Agent 为了思考、规划和生成代码，可能会产生大量请求，导致 Token 快速消耗。
   * 请务必根据自己的 API 额度和预算，**量力而为**，密切关注 Token 使用情况，以防止预算超支。

希望本教程能帮助你快速上手 Cherry Studio 强大的 Code Agent 功能！

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../question-contact/suggestions.md) 中提供的官方渠道。
