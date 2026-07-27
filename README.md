---
icon: cherries
---

# Cherry Studio 社区版

Cherry Studio 是一款开源的桌面 AI 客户端，可在 Windows、macOS 和 Linux 上统一使用云端或本地大模型。它不仅提供多模型对话，还把助手、智能体、知识库、技能、MCP、翻译、绘画、文件和笔记等能力整合在同一个工作空间中。

社区版适合希望自主选择模型服务、在本地管理工作资料，并按需扩展 AI 工作流的个人用户和开发者。

## 你可以用它做什么

| 需求 | Cherry Studio 中的能力 |
| :--- | :--- |
| 使用不同厂商或本地部署的模型 | 统一配置模型服务，在对话中切换或同时比较多个模型 |
| 保存固定角色和对话设置 | 创建助手，配置提示词、模型参数、知识库和 MCP |
| 让 AI 读取工作区并执行任务 | 创建智能体，控制可访问目录、工具和审批模式 |
| 让 AI 遵循专门的工作流程 | 安装技能，并按智能体启用 |
| 连接搜索、数据库或第三方服务 | 添加本地或远程 MCP Server |
| 建立自己的资料检索库 | 导入文档并配置 Embedding 模型 |
| 处理图片、翻译、笔记和文件 | 使用绘画、翻译、笔记和文件等独立工作区 |
| 在聊天平台或固定时间运行智能体 | 配置频道和定时任务 |

## 主要工作区

Cherry Studio V2 的侧栏可以按需显示这些应用：

* **对话**：与助手和模型交流，管理会话和消息。
* **智能体**：执行需要文件、命令或多步工具调用的任务。
* **资源库**：集中管理助手、智能体、技能和提示词。
* **绘画**：使用图像生成模型创建和管理图片。
* **翻译**：进行双语翻译和对照阅读。
* **小程序**：在应用内打开已添加的 Web 工具。
* **知识库**：导入资料、处理分段并进行检索。
* **文件**：集中查看和管理应用中的文件资源。
* **Code Tools**：管理面向开发者的代码工具。
* **笔记**：编辑和整理 Markdown 笔记。
* **OpenClaw**：使用独立的自主智能体工作区。

侧栏只显示你启用的入口；隐藏某项不会删除对应数据。

## 快速开始

### 1. 下载并安装

前往[客户端下载](cherrystudio/download.md)选择适合系统的版本。首次安装或遇到系统安全提示时，参考[安装教程](cherry-studio/installation/)。

Cherry Studio 支持 Windows、macOS 和 Linux。不同系统和芯片架构使用的安装包不同，请根据下载页说明选择。

### 2. 配置模型服务

打开 **设置 → 模型服务**：

1. 选择已有服务商，或添加兼容服务商。
2. 填写 API 地址和 API Key。
3. 获取模型列表，启用需要使用的模型。
4. 返回对话页面，选择模型并发送第一条消息。

如果使用 Ollama、LM Studio 等本地服务，请先确保对应服务已经在本机运行。详细步骤见[模型服务](pre-basic/providers/)。

### 3. 从一个场景开始

* 日常问答、写作或翻译：从[对话界面](cherrystudio/preview/chat.md)开始。
* 需要固定提示词和参数：在[资源库](cherrystudio/preview/library.md)创建助手。
* 需要操作本地文件或运行工具：创建[智能体](advanced-basic/agent.md)。
* 需要基于个人资料回答：创建[知识库](knowledge-base/knowledge-base.md)。

不需要一次配置全部功能。先完成一个可验证的小任务，再增加技能、MCP 或自动化，排错会更容易。

## 助手、智能体与扩展能力

### 助手

助手保存可重复使用的对话配置，包括提示词、模型参数、知识库和 MCP。它适合以对话为主的稳定场景。

### 智能体

智能体可以访问指定目录并调用内置工具、MCP 和技能。你可以选择普通、计划、自动编辑或全自动权限模式。详见[智能体](advanced-basic/agent.md)。

### 技能与 MCP

* [技能](pre-basic/settings/skills.md)告诉智能体如何按特定流程完成一类工作。
* [MCP](advanced-basic/mcp/)为助手或智能体连接外部工具、提示词和资源。

如果还不确定该选什么，先阅读[概念入门](advanced-basic/concepts-101.md)。

## 数据与安全

Cherry Studio 的应用配置和工作资料主要保存在本地，但“使用桌面应用”不等于“所有处理都在本地完成”：

* 使用云端模型时，消息、附件或检索到的上下文会按请求需要发送给所选模型服务商。
* 使用远程 MCP Server、频道或其他第三方服务时，相关数据可能发送给对应服务。
* 智能体和本地 MCP Server 可能按已授予的权限读取文件或运行命令。
* 使用本地模型可以减少云端传输，但仍要检查所连接的模型服务、插件和网络工具。

{% hint style="warning" %}
不要把 API Key、访问令牌、密码或私钥写进提示词、知识库、文档和截图。为智能体限制可访问目录，为 MCP 和频道使用最小权限，并在启用全自动模式前先完成受控测试。
{% endhint %}

重要数据应定期备份。Cherry Studio 支持本地导出以及 WebDAV、S3 兼容存储等备份方式，具体选项见[数据设置](pre-basic/data-settings/)。

## 开源与许可

Cherry Studio 社区版代码托管在 [GitHub](https://github.com/CherryHQ/cherry-studio)，社区版采用 GNU Affero General Public License v3.0（AGPL-3.0）。使用、修改或分发前，请阅读[开源许可协议](contact-us/questions/license.md)。

欢迎参与：

* [贡献代码](contribution/code.md)
* [贡献文档](contribution/docs.md)
* [提交问题](https://github.com/CherryHQ/cherry-studio/issues)
* [参与讨论](https://github.com/CherryHQ/cherry-studio/discussions)

## 获取帮助

遇到问题时，先查看[常见问题](question-contact/questions.md)和[如何高效提问](question-contact/ask.md)。提交反馈时，请提供 Cherry Studio 版本、操作系统、复现步骤和必要日志，并先移除 API Key、文件内容等敏感信息。

社区入口：

* [Telegram](https://t.me/CherryStudioAI)
* [Discord](https://discord.gg/wez8HtpxqQ)
* [QQ 群](https://qm.qq.com/q/lo0D4qVZKi)
* [反馈与建议](question-contact/suggestions.md)
