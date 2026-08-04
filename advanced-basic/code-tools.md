---
description: 安装、配置和启动 AI 编程 CLI 工具
icon: code
---

# 编码搭档

编码搭档用于在 Cherry Studio 中安装、配置和启动 AI 编程 CLI 工具。不同工具可以使用 Cherry Studio 中已有的模型服务，也可以通过工具自己的账号登录。

## 打开编码搭档

点击顶部标签栏右侧的 **+** 打开启动台，然后选择 **编码搭档**。如果已经将它固定到侧边栏，也可以直接点击侧边栏入口。

当前支持以下工具：

- Claude Code
- OpenAI Codex
- Gemini CLI
- OpenCode
- Qwen Code
- Kimi Code
- Qoder CLI
- GitHub Copilot CLI
- OpenClaw

## 安装或更新 CLI

1. 从左侧选择一个 CLI 工具。
2. 查看页面顶部的版本状态。
3. 如果显示 **未安装**，点击 **安装**。
4. 如果检测到新版本，可以点击 **升级**。

Cherry Studio 也能识别部分已经安装在系统中的 CLI。安装或升级失败时，页面会保留错误信息，可展开查看详情后重试。

## 配置服务商和模型

CLI 安装完成后，页面会显示与该工具兼容的服务商。

1. 找到要使用的服务商，点击 **配置**。
2. 选择模型，并按需调整该工具的参数。
3. 保存后点击 **启用**。

服务商列表会根据 CLI 支持的接口类型自动筛选。如果没有看到某个服务商，请先前往 **设置 → 模型服务**，确认服务商已经启用并配置了兼容端点。

> **提示：** **Qoder CLI** 和 **GitHub Copilot CLI** 使用各自的登录流程，不需要在 Cherry Studio 中选择服务商或模型。首次使用前，请先按对应 CLI 的提示完成登录。

页面中的 **统一网关** 可以让外部 CLI 使用 Cherry Studio 已配置的模型。启用后需要保持 Cherry Studio 运行，否则 CLI 无法连接本地网关。

## 启动 CLI

完成安装和配置后：

1. 点击页面顶部的 **启动**。
2. 点击 **选择文件夹**，指定 CLI 的工作目录。
3. 如果页面列出了多个终端，选择要使用的终端应用。
4. 再次点击 **启动**。

CLI 会以所选文件夹作为工作目录，并按照自身权限访问其中的文件。启动前请确认目录中不包含不希望 CLI 读取或修改的敏感文件。

## 各工具的配置差异

| 工具 | 配置要点 |
| --- | --- |
| Claude Code | 使用支持 Anthropic Messages 接口的服务商 |
| OpenAI Codex | 使用支持 OpenAI Responses 接口的服务商 |
| Gemini CLI | 使用 Gemini 服务或兼容的 Gemini 接口 |
| OpenCode | 可使用 Anthropic、OpenAI 兼容或 Gemini 接口 |
| Qwen Code、Kimi Code | 使用 OpenAI 兼容接口 |
| Qoder CLI、GitHub Copilot CLI | 通过 CLI 自带的账号登录流程认证 |
| OpenClaw | 在编码搭档中配置模型、启动或停止网关，并打开 Dashboard |

第三方 API 网关即使提供同名模型，也不一定兼容对应 CLI 的认证方式和接口协议。配置失败时，应优先检查服务商的端点类型，而不是只检查模型名称。

## 后续管理

回到对应工具页面，可以升级或移除由 Cherry Studio 管理的 CLI。工具运行后，页面还会显示停止操作；OpenClaw 运行时可以从这里打开 Dashboard。

> **注意：** AI 编程 CLI 可能读取、修改或执行工作目录中的内容，并消耗较多模型额度。请在启动前确认工作目录、权限设置和服务商计费规则。

***

### 获取帮助与提交反馈

如果在配置或使用过程中遇到问题，或有功能改进建议，请通过[反馈与建议](../question-contact/suggestions.md)页面提供的官方渠道联系我们。
