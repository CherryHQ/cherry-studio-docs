---
icon: rocket-launch
---

# 5 分钟快速开始

本页带你从零完成第一次 AI 对话。成功标准是：**在 Cherry Studio 中选择一个模型，发送消息，并收到正常回答。**

## 开始前需要什么？

* Windows、macOS 或 Linux 电脑；
* 可访问模型服务的网络，或者已经在本机运行 Ollama / LM Studio；
* 一个可用的模型来源。

模型来源有三种，选择一种即可：

| 我是哪类用户？ | 推荐方式 | 需要准备 |
|---|---|---|
| 第一次使用，不想研究 API | **CherryIN** | 按客户端提示登录或填写授权信息，以界面实际要求为准 |
| 已有 DeepSeek、OpenAI、Gemini 等账号 | **对应模型服务商** | 服务商创建的 API Key |
| 希望本地运行或尽量不把内容发到云端 | **Ollama / LM Studio** | 已安装并启动本地推理服务 |

{% hint style="warning" %}
Cherry Studio 不是模型本身。使用云端模型时，模型费用、额度、内容处理和隐私政策由对应服务商决定。
{% endhint %}

## 第 1 步：下载并安装

1. 打开[客户端下载](../cherrystudio/download.md)；
2. 根据操作系统和芯片架构选择安装包；
3. 完成安装并启动 Cherry Studio。

看到 Cherry Studio 主界面即表示安装成功。无法启动时，请查看 [Windows](../cherry-studio/installation/windows.md)、[macOS](../cherry-studio/installation/macos.md) 或 [Linux](../cherry-studio/installation/linux.md) 安装说明。

## 第 2 步：添加模型服务

1. 打开 `设置 → 模型服务`；
2. 选择 CherryIN、DeepSeek、OpenAI、Gemini、Ollama 或你正在使用的服务商；
3. 按页面要求填写 API Key、API 地址或本地服务地址；
4. 点击 **获取模型列表**；
5. 添加并启用至少一个**对话模型**。

{% hint style="info" %}
嵌入模型用于知识库，重排模型用于优化检索，图像模型用于绘画。第一次对话需要选择“对话模型”。
{% endhint %}

**成功标志**：模型列表中出现至少一个已启用的对话模型，并且“检测”能够正常返回结果。

如果获取不到模型：

* 检查 API Key 是否复制完整，前后不要带空格；
* 检查 API 地址是否被手动修改；
* 检查服务商账户是否有额度；
* 使用本地模型时，确认 Ollama / LM Studio 服务正在运行；
* 查看[模型服务配置](../pre-basic/providers/README.md)中的对应服务商教程。

## 第 3 步：发送第一条消息

1. 点击顶部的 **对话**；
2. 选择系统默认助手；
3. 在输入框附近的模型选择器中，选择刚才启用的对话模型；
4. 输入下面的测试消息：

> 请用三句话介绍 Cherry Studio，并说明你当前可以帮助我完成什么。

5. 点击发送。

**成功标志**：页面开始显示模型回复，且不是空白消息或连接错误。

如果发送失败，先展开错误详情，再依次检查模型是否启用、API Key、账户额度和网络连接。使用本地模型时还要确认本地服务没有退出。

## 第 4 步：选择下一条学习路线

| 接下来想做什么？ | 下一步 |
|---|---|
| 学会上传文件、切换模型和管理话题 | [对话界面](../cherrystudio/preview/chat.md) |
| 保存一个固定角色和提示词 | [助手与助手库](../cherrystudio/preview/assistants.md) |
| 用自己的 PDF、Word、网页或笔记问答 | [知识库教程](../knowledge-base/knowledge-base.md) |
| 让 AI 读取文件、调用工具并执行多步骤任务 | [Cherry Agent](../advanced-basic/agent.md) |
| 还分不清助手、Agent、Skill 和 MCP | [核心概念](../advanced-basic/concepts-101.md) |

{% hint style="success" %}
完成第一次对话就已经具备日常使用条件。API 网关、MCP、频道和定时任务都属于按需启用的进阶能力，不需要一次配置完成。
{% endhint %}
