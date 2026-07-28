---
icon: cherries
---

# Cherry Studio 是什么？

<figure><img src=".gitbook/assets/docs-readme-banner1.png" alt="Cherry Studio"><figcaption></figcaption></figure>

Cherry Studio 是一个**开源的桌面 AI 工作台**。它把 CherryIN、DeepSeek、OpenAI、Claude、Gemini 以及 Ollama 等本地模型连接到同一个客户端，并提供对话、知识库、Agent、翻译和绘画等能力。

## 你可以用它做什么？

* **问答、写作或编程**：使用[对话与助手](cherrystudio/preview/chat.md)总结文章、修改邮件或解释代码。
* **统一管理不同模型**：通过[模型服务](pre-basic/providers/README.md)使用 DeepSeek、Gemini 或本地模型。
* **根据自己的资料回答**：用[知识库](cherrystudio/preview/knowledge-base.md)查询产品手册、课程资料、合同和笔记。
* **完成多步骤任务**：让[Agent](advanced-basic/agent.md)读取工作区、整理文件、修改代码或生成报告。
* **连接外部服务**：通过[MCP](advanced-basic/mcp/README.md)查询数据库，或调用 GitHub、Notion 等服务。
* **自动运行或进入群聊**：结合[定时任务](advanced-basic/scheduled-tasks.md)和[频道](advanced-basic/agent-channels.md)生成简报并发送到飞书。
* **处理图片、翻译和笔记**：使用[绘画](cherrystudio/preview/drawing.md)、[翻译](cherrystudio/preview/translation.md)和[笔记](cherrystudio/preview/notes.md)完成内容工作。

## 第一次使用，从这里开始

{% content-ref url="getting-started/quick-start.md" %}
[quick-start.md](getting-started/quick-start.md)
{% endcontent-ref %}

按[快速开始](getting-started/quick-start.md)完成模型配置和第一次对话后，再根据需要查阅知识库、Agent 或其他功能。

## 模型、费用与数据分别由谁负责？

```text
云端模型服务商 / 本地模型
            ↓
      Cherry Studio
            ↓
对话 · 知识库 · Agent · 翻译 · 绘画
```

* **模型来源**：可以使用 CherryIN 中当前可用的模型、自己的服务商 API Key，或本机运行的 Ollama / LM Studio。
* **软件费用**：Cherry Studio 客户端开源；模型是否收费、如何计费以及可用额度由模型服务商决定。
* **数据位置**：对话、设置和知识库索引主要保存在本机；使用云端模型时，完成请求所需的内容会发送给对应服务商。
* **完全本地使用**：需要使用本地模型，并避免启用云端模型、联网搜索和其他外部服务。

不要把 API Key 发布到截图、文档、群聊或公开仓库中。怀疑密钥泄露时，请立即到服务商后台撤销并重新生成。

## 助手、Agent、知识库

| 能力 | 最适合的任务 | 是否会主动执行操作 |
|---|---|---|
| **助手** | 固定角色和回复风格的日常对话 | 否，以对话为主 |
| **Agent** | 读取工作区、调用工具并完成多步骤任务 | 是，按权限执行 |
| **知识库** | 从你导入的资料中检索相关内容 | 否，为对话或 Agent 提供资料 |

第一次看到 Skill、MCP、频道等术语时，请阅读[核心概念](advanced-basic/concepts-101.md)。

## 获取帮助

* 遇到错误：先查看[常见问题](question-contact/questions.md)
* 需要提交 Bug 或建议：查看[反馈与建议](question-contact/suggestions.md)
* 关注动态：[X](https://x.com/CherryStudioHQ) · [哔哩哔哩](https://space.bilibili.com/3546657515898892) · [微博](https://weibo.com/u/7975656228)
* 加入社区：[QQ群](https://qm.qq.com/q/lo0D4qVZKi) · [Telegram](https://t.me/CherryStudioAI) · [Discord](https://discord.gg/wez8HtpxqQ)
