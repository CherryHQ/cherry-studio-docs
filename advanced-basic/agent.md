---
icon: robot
---

# Cherry Agent

想让 AI 不只是聊天，而是**真的帮你把事情做完**？这就是 Cherry Agent。

打个比方：

* 普通对话里的 AI 像是"**会说话的同事**" —— 你问它怎么做，它告诉你方法
* Cherry Agent 像是"**有手脚的同事**" —— 你给它目标，它自己读文件、查资料、调工具，一步步完成

举几个真实场景：

* "把 `~/Downloads` 里所有 PDF 整理成 Excel 清单"
* "查一下今天主流科技媒体的头条，做一份 5 条要点的简报"
* "review 我刚写的这个 Python 文件，给出改进建议并直接修改"
* "每天早上 9 点自动做一遍上面这些事"（搭配[定时任务](scheduled-tasks.md)）

> 还没搞清楚「助手 / 智能体 / 技能 / MCP / 频道」之间的关系？先看 [5 分钟搞懂](concepts-101.md)。

### 开始前需要准备两样东西

#### 1. 一家"支持 Claude 模型对话方式"的 AI 服务商

为什么？因为 Cherry Agent 需要 AI 用"工具调用"的方式回话，而目前这种对话方式最成熟的是 Claude 系列模型。所以你需要找一家提供 Claude 或同类对话方式的 AI 服务商，常见选择：

* **[CherryIN](../pre-basic/providers/cherryin-1.md)**（最方便）：一个账号同时支持普通对话和 Cherry Agent
* **[Anthropic 官方](../pre-basic/providers/anthropic.md)**：直接用 Claude 账号
* 其他主流 AI 网关（如 [OpenRouter](../pre-basic/providers/openrouter.md)）也可以

#### 2. 打开"API 服务器"开关

Cherry Studio 需要在你电脑上开一个"内部小服务"来运行 Agent。听起来很技术，实际就是 `设置 → API 服务器` 里点一下绿色启动按钮，详情见 [API 服务器](api-server.md)。

{% hint style="warning" %}
**注意：Agent 会比普通聊天烧更多 token。** 因为它要多轮对话、调用各种工具，每一步都要消耗模型额度。建议在 AI 服务商后台设个月度上限避免意外超支。
{% endhint %}

### 第 1 步：配置 Anthropic 类型的 Provider

打开 `设置 → 模型服务`，找到（或新建）一个支持 Anthropic 端点的 Provider：

* 填写 **API 密钥**
* 确认 **API 地址** 指向正确的 Anthropic 端点（CherryIN 默认 `https://open.cherryin.cc`）
* 点击 **获取模型列表**，添加至少一个对话模型（如 `claude-sonnet-4` / `agent/deepseek-v4-flash` 等）

{% hint style="info" %}
订阅了 Claude Code 的用户可直接把 Anthropic key 与 endpoint 填入对应字段获取模型。
{% endhint %}

### 第 2 步：启用 API 服务器

打开 `设置 → API 服务器`，将端口与密钥确认后点击 ▶ 启动。详细说明见 [API 服务器](api-server.md)。

<figure><img src="../.gitbook/assets/cherry-api-server-running.png" alt=""><figcaption><p>API 服务器已运行，Agent 才能工作</p></figcaption></figure>

### 第 3 步：创建一个 Agent

顶部 Tab 进入 **智能体**：

* 点击 **+ 新建智能体**
* 在弹窗中填写 **名称**、**头像**、**模型**（选刚才配的 Anthropic Provider 下任一模型）
* 编辑 **系统提示词**，描述这个 Agent 是干什么的、风格、可用工具的边界

### 第 4 步：配置 Agent 权限与工具

Agent 列表中 **右键** 任一 Agent → 进入编辑界面，可配置：

* **权限模式**：
  * **正常模式**：所有敏感操作（写文件、执行命令）需要人工确认
  * **灵魂模式 / 无权限模式**：跳过确认，自主决策。**定时任务必须使用此类模式**，详见 [定时任务](scheduled-tasks.md)
* **可用工具**：内置工具开关 + 引入 [MCP 服务器](mcp/) 提供的额外工具
* **知识库挂载**：让该 Agent 访问指定的 [知识库](../knowledge-base/knowledge-base.md)

### 第 5 步：与 Agent 对话

返回智能体页面，点击你刚创建的 Agent 进入会话：

* 直接输入任务，例如"帮我把 `~/Downloads/report.md` 转成 PPT 大纲"
* Agent 会自动决定调用哪些工具、是否需要多轮 reasoning
* 工具调用与决策过程会以可折叠卡片形式展示

### 常见问题

#### 智能体页面提示"请启用 API 服务器以使用智能体功能"

回 `设置 → API 服务器`，点击绿色 ▶ 启动按钮。详情见 [API 服务器](api-server.md)。

#### 创建 Agent 时下拉里没有模型

* 确认所选 Provider 至少添加了一个对话模型
* 确认该 Provider 类型为 **Anthropic** 或 **CherryIN**（OpenAI-only 的 Provider 不会出现在 Agent 模型选择里）

#### Agent 输出突然停止

可能命中工具调用上限或单次会话长度上限。提高 Agent 设置中的最大轮数与单次输出 token 上限即可。

### 下一步

* 把 Agent 接到 IM 平台（飞书 / Telegram / QQ / 微信 / Discord / Slack）→ [频道（Cherry Claw）](agent-channels.md)
* 让 Agent 定时自动执行任务 → [定时任务](scheduled-tasks.md)
* 拓展工具能力 → [MCP 使用教程](mcp/)
