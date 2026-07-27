---
icon: graduation-cap
---

# 核心概念

Cherry Studio 将模型、资料和工具组织为助手、Agent、知识库、技能和 MCP 等能力。本页说明它们分别解决什么问题，以及如何组合；具体配置步骤见对应教程。

## 能力对照

* **模型服务（Provider）** — 提供生成回答所需的模型，并决定可用模型、费用与数据政策。
* **助手（Assistant）** — 保存对话规则和回复风格，适合固定角色的日常问答、写作、翻译或编程。
* **Agent** — 读取工作区、调用工具并执行多步骤任务，例如整理文件、分析项目、修改代码或生成报告。
* **知识库** — 检索导入的文档，为基于产品手册、课程资料、合同或笔记的回答提供内容。
* **技能（Skill）** — 为 Agent 提供可复用的流程、模板和资料，适合固定流程的专项任务。
* **MCP** — 让助手或 Agent 使用外部工具和数据源，例如数据库、Notion 或 GitHub。
* **频道** — 将 Agent 接入飞书、Telegram、QQ、微信、Discord 或 Slack 等 IM 平台。
* **定时任务** — 按计划触发 Agent，适合日报、周报和数据同步等周期性任务。

## 助手与 Agent

助手以对话为主。它保存角色设定和回复方式，也可以结合知识库或 MCP。

Agent 面向需要连续执行的任务。它可以读取工作区、调用已授权的工具，并根据目标完成多个步骤。

相关文档：[对话与助手](../cherrystudio/preview/assistants.md) · [Agent](agent.md)

## 知识库

知识库从导入的资料中检索相关内容，再交给模型生成回答。它既可以用于普通对话，也可以作为 Agent 的资料来源。

知识库适合处理相对稳定且需要反复查询的资料；临时文件可以直接作为对话附件使用。

相关文档：[知识库](../knowledge-base/knowledge-base.md)

## 技能与 MCP

技能定义任务的处理方法，通常包含操作说明、模板和配套资源。MCP 提供可调用的外部工具或数据。

例如，制作周报的技能可以规定分析和排版流程；连接项目管理系统的 MCP 工具可以读取实际任务数据。两者可以配合使用。

Cherry Studio 已内置文件上传和知识库能力。读取本地资料不要求配置 MCP。

相关文档：[技能](../pre-basic/settings/skills.md) · [MCP](mcp/)

## 频道与定时任务

频道让 Agent 在支持的 IM 平台中接收消息并返回结果。定时任务按设定的时间自动触发 Agent。

这两项能力负责触发和传递任务，不改变 Agent 本身的模型、工具或权限设置。

相关文档：[频道](agent-channels.md) · [定时任务](scheduled-tasks.md)

## 组合关系

* Provider 提供模型。
* 知识库提供资料。
* 技能提供处理方法。
* MCP 提供外部工具与数据。
* 助手和 Agent 负责对话或任务执行。
* 频道和定时任务提供消息入口或自动触发。

## 按需求查阅

* 配置模型并开始对话：[快速开始](../getting-started/quick-start.md)
* 固定对话角色：[助手与助手库](../cherrystudio/preview/assistants.md)
* 使用自己的资料：[知识库](../knowledge-base/knowledge-base.md)
* 执行多步骤任务：[Agent](agent.md)
* 连接外部服务：[MCP](mcp/)
* 接入群聊或周期运行：[频道](agent-channels.md) · [定时任务](scheduled-tasks.md)
