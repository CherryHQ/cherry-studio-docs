---
icon: cherries
---

# 项目简介

<figure><img src=".gitbook/assets/docs-readme-banner1.png" alt="Cherry Studio"><figcaption></figcaption></figure>

关注我们的社交账号：[推特（X）](https://x.com/CherryStudioHQ) · [小红书](https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a) · [微博](https://weibo.com/u/7975656228) · [哔哩哔哩](https://space.bilibili.com/3546657515898892) · [抖音](https://www.douyin.com/user/MS4wLjABAAAAmw9A54m5J0hHVMQY5eGrVJ-EHDoOS0hgJ6M1F9MN2Tn2V163A0xrC4_KVzfmQSxC)

加入我们的社群：[QQ群](https://qm.qq.com/q/lo0D4qVZKi) · [Telegram](https://t.me/CherryStudioAI) · [Discord](https://discord.gg/wez8HtpxqQ) · [微信群](https://www.cherry-ai.com/#Community)

***

Cherry Studio 是一款集多模型对话、智能体、知识库管理、AI 绘画、翻译等功能于一体的全能 AI 助手平台。Cherry Studio 高度自定义的设计、强大的扩展能力和友好的用户体验，使其成为专业用户和 AI 爱好者的理想选择。无论是零基础用户还是开发者，都能在 Cherry Studio 中找到适合自己的 AI 功能，提升工作效率和创造力。

{% hint style="info" %}
**CherryIN 是模型服务商（Provider），不是模型。** Cherry Studio 也可以连接 DeepSeek、OpenAI、Claude、Gemini 等服务商，以及 Ollama、LM Studio 等本地模型服务。
{% endhint %}

## 你可以用它做什么？

* **问答、写作或编程**：使用[对话与助手](cherrystudio/preview/chat.md)总结文章、修改邮件或解释代码。
* **统一管理不同模型**：通过[模型服务](pre-basic/providers/README.md)使用 DeepSeek、Gemini 或本地模型。
* **根据自己的资料回答**：用[知识库](cherrystudio/preview/knowledge-base.md)查询产品手册、课程资料、合同和笔记。
* **完成多步骤任务**：进入[工作（Agent）](advanced-basic/agent.md)，让 AI 读取工作区、整理文件、修改代码或生成报告。
* **连接外部服务**：通过[MCP](advanced-basic/mcp/README.md)查询数据库，或调用 GitHub、Notion 等服务。
* **自动运行或进入群聊**：结合[定时任务](advanced-basic/scheduled-tasks.md)和[频道](advanced-basic/agent-channels.md)生成简报并发送到飞书。
* **处理图片、翻译和笔记**：使用[绘画](cherrystudio/preview/drawing.md)、[翻译](cherrystudio/preview/translation.md)和[笔记](cherrystudio/preview/notes.md)完成内容工作。

## 核心功能与特色

### 对话与助手

* **多模型对比**：同一个问题可以交给多个模型回答，便于比较结果。
* **助手与话题管理**：按助手组织不同角色和回复风格，并在助手下管理多个话题。
* **对话导出**：可将完整对话或单条消息导出为 Markdown、Word 等格式。
* **助手库**：可从助手库添加预设助手，也可以创建自己的助手。
* **内容渲染**：支持 Markdown、公式、代码块等内容显示。

### 工作与自动化

* **工作（Agent）**：读取工作区、调用工具并执行多步骤任务。
* **技能（Skill）**：为工作中的 Agent 提供可复用的流程、模板和资料。
* **MCP**：连接数据库、Notion、GitHub 等外部工具和数据源。
* **频道**：将 Agent 接入飞书、Telegram、QQ、微信、Discord 或 Slack 等平台。
* **定时任务**：按计划触发 Agent，适合日报、周报和数据同步等任务。

### 内置应用与工具

* **绘画、翻译与笔记**：在独立页面完成图片生成、文本翻译和 Markdown 笔记整理。
* **小程序**：在应用网格中集中打开内置或自定义的网页服务。
* **文件**：集中管理 Cherry Studio 中使用的图片、视频、音频、文本和文档。
* **全局搜索**：搜索对话、任务、助手、Agent 和知识库。
* **快捷助手与划词助手**：在其他应用中快速提问，或对选中的文本进行翻译、解释、润色和总结。

### 模型服务与个性化

* **统一管理服务商**：集中配置 CherryIN、OpenAI、Gemini、Anthropic、Azure OpenAI 等云端服务商，以及 Ollama、LM Studio 等本地模型服务。
* **获取模型列表**：从服务商获取当前账号可用的模型，实际可用性由服务商和账号配置决定。
* **多 API Key 轮询**：同一服务商可以配置多个已启用的 API Key，客户端按轮询方式选用。
* **自定义服务商**：可接入兼容 OpenAI、Gemini 或 Anthropic 接口规范的服务商。
* **界面个性化**：支持自定义 CSS、消息样式、头像，以及启动台和侧栏应用顺序。

### 知识库与数据保障

* **多种数据源**：可导入文件、文件夹、网址、站点地图或手动输入的内容。
* **索引与召回测试**：建立索引后，可通过召回测试检查检索结果和分段效果。
* **本地与云端备份**：支持本地备份，也可配置 WebDAV 或 S3 兼容存储。
* **本地模式有前提**：若希望数据处理尽量留在本机，需要使用本地模型，并避免启用联网搜索、云端模型及其他外部服务。

<figure><img src=".gitbook/assets/cherry-business-analysis-stable.png" alt="Cherry Studio 对季度营收数据生成柱状图"><figcaption><p>对话示例：把季度营收数据整理为可视化图表，并继续分析业务趋势</p></figcaption></figure>

## 项目优势

* **容易上手**：常用应用集中在启动台和侧栏，用户可按需要逐步完成配置。
* **持续迭代**：产品会根据功能演进和用户反馈继续更新。
* **开源与可扩展**：可通过开源代码、自定义服务商、MCP 和技能扩展使用场景。

## 适用场景

* **知识管理与查询**：构建和检索自己的资料库。
* **多模型对话与创作**：比较不同模型的回答，完成写作、翻译或编程任务。
* **自动化工作**：让 Agent 读取工作区、调用工具并执行多步骤任务。
* **图片与内容处理**：使用绘画、翻译、笔记、快捷助手和划词助手完成内容工作。

## 第一次使用，从这里开始

{% content-ref url="getting-started/quick-start.md" %}
[快速开始](getting-started/quick-start.md)
{% endcontent-ref %}

按快速开始完成模型配置和第一次对话后，再根据需要查阅知识库、Agent 或其他功能。

## 模型、费用与数据分别由谁负责？

<p align="center"><strong>云端模型服务商 / 本地模型</strong></p>

<p align="center">↓</p>

<p align="center"><strong>Cherry Studio</strong></p>

<p align="center">↓</p>

<p align="center"><strong>对话 · 知识库 · Agent · 翻译 · 绘画</strong></p>

* **模型来源**：可以使用 CherryIN 中当前可用的模型、自己的服务商 API Key，或本机运行的 Ollama / LM Studio。
* **软件费用**：Cherry Studio 客户端开源；模型是否收费、如何计费以及可用额度由模型服务商决定。
* **数据位置**：对话、设置和知识库索引主要保存在本机；使用云端模型时，完成请求所需的内容会发送给对应服务商。
* **完全本地使用**：需要使用本地模型，并避免启用云端模型、联网搜索和其他外部服务。

不要把 API Key 发布到截图、文档、群聊或公开仓库中。怀疑密钥泄露时，请立即到服务商后台撤销并重新生成。

## 对话、工作与知识库

| 能力 | 最适合的任务 | 是否会主动执行操作 |
|---|---|---|
| **助手** | 固定角色和回复风格的日常对话 | 否，以对话为主 |
| **工作（Agent）** | 读取工作区、调用工具并完成多步骤任务 | 是，按权限执行 |
| **知识库** | 从你导入的资料中检索相关内容 | 否，为对话或 Agent 提供资料 |

第一次看到 Skill、MCP、频道等术语时，请阅读[核心概念](advanced-basic/concepts-101.md)。

## 获取帮助

* 遇到错误：先查看[常见问题](question-contact/questions.md)
* 需要提交 Bug 或建议：查看[反馈与建议](question-contact/suggestions.md)

***

## 关注我们的社交账号

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a">小红书</a></td><td><a href=".gitbook/assets/1.png">1.png</a></td><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a">https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a</a></td></tr><tr><td><a href="https://space.bilibili.com/3546657515898892">哔哩哔哩</a></td><td><a href=".gitbook/assets/3.png">3.png</a></td><td><a href="https://space.bilibili.com/3546657515898892">https://space.bilibili.com/3546657515898892</a></td></tr><tr><td><a href="https://weibo.com/u/7975656228">微博</a></td><td><a href=".gitbook/assets/2.png">2.png</a></td><td><a href="https://weibo.com/u/7975656228">https://weibo.com/u/7975656228</a></td></tr><tr><td><a href="https://www.douyin.com/user/MS4wLjABAAAAmw9A54m5J0hHVMQY5eGrVJ-EHDoOS0hgJ6M1F9MN2Tn2V163A0xrC4_KVzfmQSxC">抖音</a></td><td><a href=".gitbook/assets/4.png">4.png</a></td><td><a href="https://www.douyin.com/user/MS4wLjABAAAAmw9A54m5J0hHVMQY5eGrVJ-EHDoOS0hgJ6M1F9MN2Tn2V163A0xrC4_KVzfmQSxC">https://www.douyin.com/user/MS4wLjABAAAAmw9A54m5J0hHVMQY5eGrVJ-EHDoOS0hgJ6M1F9MN2Tn2V163A0xrC4_KVzfmQSxC</a></td></tr><tr><td><a href="https://x.com/CherryStudioHQ">推特（X）</a></td><td><a href=".gitbook/assets/5.png">5.png</a></td><td><a href="https://x.com/CherryStudioHQ">https://x.com/CherryStudioHQ</a></td></tr></tbody></table>

加入我们的社群：[QQ群](https://qm.qq.com/q/lo0D4qVZKi) · [Telegram](https://t.me/CherryStudioAI) · [Discord](https://discord.gg/wez8HtpxqQ) · [微信群](https://www.cherry-ai.com/#Community)
