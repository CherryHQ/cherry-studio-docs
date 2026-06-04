---
icon: robot
---

# Cherry Agent

Cherry Agent 让 AI 不仅能对话，更能**自主完成任务**。

类比：

* 普通对话中的 AI 类似"**仅能给建议的同事**" —— 你询问方法，它告诉你步骤
* Cherry Agent 类似"**具备执行能力的同事**" —— 你给定目标，它自主读取文件、查询资料、调用工具，逐步完成

适用场景示例：

* "将 `~/Downloads` 中所有 PDF 整理为 Excel 清单"
* "查询今日主流科技媒体头条，生成一份 5 条要点的简报"
* "审阅指定的 Python 文件，给出改进建议并直接修改"
* "每日早上 9 点自动执行以上任务"（结合 [定时任务](scheduled-tasks.md)）

> 推荐先阅读 [概念入门](concepts-101.md) 理清助手 / 智能体 / 技能 / MCP / 频道之间的关系。

### 开始前的两项准备

#### 1. 一家支持 Anthropic 协议的 Provider

Cherry Agent 依赖"工具调用"格式的对话方式，目前最成熟的实现是 Anthropic Claude 系列模型。因此需要一家提供该协议的模型服务商，推荐选项：

* **[CherryIN](../pre-basic/providers/cherryin-1.md)**（最便捷）：单一账号即可同时支持普通对话与 Cherry Agent
* **[Anthropic 官方](../pre-basic/providers/anthropic.md)**：直接使用 Claude 账号
* 其他主流 AI 网关（如 [OpenRouter](../pre-basic/providers/openrouter.md)）

#### 2. 启用 API 服务器

Cherry Studio 需要在本地运行一个内部服务以承载 Agent。操作上仅需在 `设置 → API 服务器` 中点击启动按钮即可，详见 [API 服务器](api-server.md)。

{% hint style="warning" %}
**Token 消耗提示**：Agent 模式涉及多轮对话与工具调用，单次任务的 token 消耗显著高于普通对话。建议在 Provider 后台设置月度上限以避免超支。
{% endhint %}

### 第 1 步：配置 Anthropic 类型的 Provider

打开 `设置 → 模型服务`，找到（或新建）一个支持 Anthropic 端点的 Provider：

* 填写 **API 密钥**
* 确认 **API 地址** 指向正确的 Anthropic 端点（CherryIN 默认 `https://open.cherryin.cc`）
* 点击 **获取模型列表**，添加至少一个对话模型（如 `claude-sonnet-4` / `agent/deepseek-v4-pro` 等）

<figure><img src="../.gitbook/assets/cherry-agent-step1-provider.png" alt=""><figcaption><p>已配置 CherryIN 并添加 agent 模型</p></figcaption></figure>

{% hint style="info" %}
订阅了 Claude Code 的用户可直接将 Anthropic key 与 endpoint 填入对应字段获取模型。
{% endhint %}

### 第 2 步：启用 API 服务器

打开 `设置 → API 服务器`，确认端口与密钥后点击 ▶ 启动。详细说明见 [API 服务器](api-server.md)。

<figure><img src="../.gitbook/assets/cherry-api-server-running.png" alt=""><figcaption><p>API 服务器运行中，Agent 方可工作</p></figcaption></figure>

### 第 3 步：进入智能体页面

顶部 Tab 点击 **智能体**。Cherry Studio 默认内置 **Cherry Assistant** 和 **Cherry Claw** 两个智能体，可直接使用，也可基于自己的需求新建一个。

<figure><img src="../.gitbook/assets/cherry-agent-step3-list.png" alt=""><figcaption><p>智能体页面：左侧列表 + 右侧对话区</p></figcaption></figure>

### 第 4 步：新建一个智能体

点击左侧栏顶部 **+ 智能体** 按钮，弹出 **添加 Agent** 表单：

<figure><img src="../.gitbook/assets/cherry-agent-step3-create-form.png" alt=""><figcaption><p>添加 Agent 表单</p></figcaption></figure>

各字段说明：

| 字段 | 说明 |
|---|---|
| **名称** | Agent 在列表中的显示名 |
| **模型** | 选择上一步在 Anthropic 类型 Provider 下添加的对话模型 |
| **自主模式** | 是否允许 Agent 在无人值守时自主推进任务。**定时任务必须开启此项** |
| **权限模式** | `普通模式`（敏感操作需人工确认）/ `无权限模式`（跳过确认） |
| **工作目录** | Agent 可读写的本地目录。留空则自动创建默认目录 |

填写完点击 **添加** 即完成创建。

### 第 5 步：调整智能体的提示词、工具与技能

点击智能体卡片右侧的 ⋮ 菜单 → **编辑**，进入完整编辑面板。左侧分类对应不同设置：

<figure><img src="../.gitbook/assets/cherry-agent-step4-edit-panel.png" alt=""><figcaption><p>智能体编辑面板（基础设置 Tab）</p></figcaption></figure>

* **基础设置**：头像、名称、模型、工作目录、自主模式、启用心跳、间隔、描述
* **提示词设置**：编辑系统提示词，决定 Agent 的角色与回话风格
* **权限模式**：与新建表单一致，可在此处调整
* **工具**：勾选 Agent 可使用的内置工具，及挂载来自 [MCP 服务器](mcp/) 的外部工具
* **技能**：挂载预先安装的 [技能](../pre-basic/settings/skills.md)
* **高级设置**：上下文长度、温度、最大轮数等参数

### 第 6 步：与智能体对话

返回智能体页面，点击智能体卡片进入会话：

* 在底部输入框输入任务，例如"请帮我把 `~/Downloads/report.md` 转成 PPT 大纲"
* Agent 会自动判断调用哪些工具、是否需要多轮推理
* 工具调用与决策过程以可折叠卡片形式逐步展示

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
