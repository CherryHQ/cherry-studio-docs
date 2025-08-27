---
description: Tools
icon: code
---

# Code Tools 使用教程

Cherry Studio v1.5.7 版本引入了操作简单，强大的 Code Agent 功能，可以直接启动和管理多种 AI 编程agent 。本教程将引导您完成设置和启动的完整流程。

***

### 操作步骤

#### 1. 升级 Cherry Studio

首先，请确保您的 Cherry Studio 已升级到 **v1.5.7** 或更高版本。您可以前往 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 或官方网站下载最新版本。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 2. 调整导航栏位置

为了方便使用顶部标签页功能，我们建议将导航栏调整至顶部。

* 操作路径：`设置` -> `显示设置` -> `导航栏设置`
* 将“导航栏位置”选项设置为 **`顶部`**。

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. 新建标签页

点击界面顶部的“+”号图标，新建一个空白标签页。

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. 打开 Code Agent 功能

在新建的标签页中，点击 `Code`（或 `</>`）图标，进入 Code Agent 配置界面。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. 选择 CLI 工具

根据您的需求和所持有的 API Key，选择一个要使用的 Code Agent 工具。 目前支持以下几种：

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. 选择 Agent 调用的模型

在模型下拉列表中，选择与您所选 CLI 工具兼容的模型。 _（详细的模型兼容性说明，请参考下方的“重要注意事项”）_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. 指定工作目录

点击“选择目录”按钮，为 Agent 指定一个工作目录。Agent 将拥有访问此目录下所有文件和子目录的权限，以便于它理解项目上下文、读取文件和执行代码。

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. 设置环境变量

* **自动配置**：您在第 6 步（模型）和第 7 步（工作目录）中的选择，会自动生成相应的环境变量。
* **自定义添加**：如果您的 Agent 或项目需要其他特定的环境变量（例如 `PROXY_URL` 等），可以在此区域自定义添加。

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. 更新选项

* **内置可执行文件**：Cherry Studio 已为您集成了上述所有 Code Agent 的可执行文件，在大多数情况下，您无需联网即可直接使用。
* **自动更新**：如果您希望 Agent 始终保持最新版本，可以勾选 **`检查更新并安装最新版本`** 的选项。勾选后，每次启动时程序都会联网检查并更新 Agent 工具。

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. 启动 Agent

所有配置完成后，点击 **`启动`** 按钮。 Cherry Studio 会自动调用您系统自带的 Terminal（终端）工具，并在其中加载好所有环境变量，然后运行您选择的 Code Agent。现在您可以在弹出的终端窗口中与 AI Agent 进行交互了。

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### 重要注意事项

1. **模型兼容性说明**：
   * **Claude Code**: 需要选择支持 Anthropic API Endpoint 格式的模型。目前官方支持的模型包括：
     * Claude 系列模型
     * DeepSeek V3.1 (官方 API 平台)
     * Kimi K2 (官方 API 平台)
     * 智谱 GLM 4.5 (官方 API 平台)
     * **注意**：当前许多第三方服务商（如 One API, New API 等）针对 DeepSeek, Kimi, GLM 的 API 接口大多只支持 OpenAI Chat Completions 格式，可能无法与 Claude Code 直接兼容，需要等待服务商逐步适配。
   * **Gemini CLI**: 需要选择 Google 的 Gemini 系列模型。
   * **Qwen Code**: 支持 OpenAI Chat Completions API 格式的模型，强烈推荐使用 **`Qwen3 Coder`** 系列模型以获得最佳代码生成效果。
   * **OpenAI Codex**: 支持 GPT 系列模型（如 `gpt-4o`, `gpt-5` 等）。
2. **依赖与环境冲突**：
   * Cherry Studio 内部集成了独立的 Node.js 运行环境、Code Agent 可执行文件及环境变量配置，旨在提供一个开箱即用的纯净环境。
   * 如果您在启动 Agent 时遇到依赖冲突或奇怪的错误，可以考虑暂时**卸载或禁用系统内已安装的相关依赖**（如全局安装的 Node.js 或特定工具链），以排除冲突。
3. **API Token 消耗警告**：
   * **Code Agent 对 API Token 的消耗量非常大**。在处理复杂任务时，Agent 为了思考、规划和生成代码，可能会产生大量请求，导致 Token 快速消耗。
   * 请务必根据自己的 API 额度和预算，**量力而为**，密切关注 Token 使用情况，以防止预算超支。

希望本教程能帮助您快速上手 Cherry Studio 强大的 Code Agent 功能！
