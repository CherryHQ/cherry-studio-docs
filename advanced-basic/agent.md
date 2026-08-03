---
icon: robot
---

# 工作

**工作**是 Cherry Studio 中专门运行 Agent 的页面。它让 AI 不仅能对话，还能读取工作区、调用工具并**自主完成多步骤任务**。

类比：

* 普通对话中的 AI 类似 **仅能给建议的同事** —— 你询问方法，它告诉你步骤
* Agent 类似 **具备执行能力的同事** —— 你给定目标，它自主读取文件、查询资料、调用工具，逐步完成

适用场景示例：

* "将 `~/Downloads` 中所有 PDF 整理为 Excel 清单"
* "查询今日主流科技媒体头条，生成一份 5 条要点的简报"
* "审阅指定的 Python 文件，给出改进建议并直接修改"
* "每日早上 9 点自动执行以上任务"（结合 [定时任务](scheduled-tasks.md)）

> 推荐先阅读 [核心概念](concepts-101.md)，了解对话中的助手与工作页面中的 Agent 有什么不同。

### 开始前的准备

需要先启用一个可用于 Agent 的对话模型。

工作页面的模型选择器会显示可用于对话的模型，并过滤嵌入、重排、图像生成等非对话模型。可选来源包括：

* [**CherryIN**](../pre-basic/providers/cherryin-1.md)、[Anthropic](../pre-basic/providers/anthropic.md) 等支持 Anthropic 或兼容端点的 Provider
* **Google / Gemini** 官方或自定义 Google 网关中的对话模型
* 其他能由 Cherry Studio 本地 API 网关转换为 Agent 运行协议的对话模型

不同模型的工具调用稳定性和费用差异较大。首次使用建议选择明确支持工具调用的模型，再用一个小任务测试。

{% hint style="info" %}
部分模型会由 Cherry Studio 在内部通过本地 API 网关路由。Agent 运行时会自动启动所需服务，不需要手动配置或开启 API 网关。
{% endhint %}

{% hint style="warning" %}
**Token 消耗提示**：Agent 模式涉及多轮对话与工具调用，单次任务的 token 消耗显著高于普通对话。建议在 Provider 后台设置月度上限以避免超支。
{% endhint %}

{% hint style="danger" %}
**⚠️ 数据安全与权限红线（务必先读）**

Agent 拥有读写文件、执行命令、调用外部 API 的真实能力，一旦授权范围过大或权限模式过高，可能造成**不可逆的数据丢失**。我们已收到用户反馈，例如：AI 在执行清理 / 整理任务时误删了整个磁盘（包括 C 盘系统目录、用户主目录下的文档、照片、项目代码等），导致系统无法启动或重要资料永久丢失。

为避免此类惨剧，请务必在开始任何任务前做到：

* **严格限制工作目录**：只授权本次任务真正需要的文件夹，**切勿**将整个磁盘、系统盘（如 `C:\`）、用户主目录（如 `C:\Users\你的用户名`、`~`）、桌面、下载、文档库或任何包含重要资料、密钥、项目代码的上级目录设为工作目录。
* **从最低权限起步**：首次使用请选择 **普通模式** 或 **计划模式**，确认 Agent 行为符合预期后再逐步提升；**全自动模式**仅用于范围受控、明确需要无人确认的场景。
* **逐项确认高风险操作**：涉及写文件、删除、移动、执行命令时，保持人工授权，仔细核对路径后再放行。
* **先备份再动手**：在让 Agent 处理已有重要数据前，先完成备份。
* **警惕"清理 / 批量"类指令**：删除、清空、批量重命名、递归处理等操作风险最高，执行前请逐条复核目标路径，宁可手动确认也不要放任自动执行。

权限和工作目录一旦授予即视为你授权 Agent 在该范围内自主操作，Cherry Studio 无法对已被删除的数据进行恢复。
{% endhint %}

### 第 1 步：配置 Provider 与模型

打开 `设置 → 模型服务`，找到或新建一个 Provider：

* 填写 **API 密钥**
* 确认 API 地址和端点类型与服务商要求一致
* 点击 **获取模型列表**，添加至少一个支持对话和工具调用的模型

<figure><img src="../.gitbook/assets/cherry-agent-step1-provider.png" alt=""><figcaption><p>已配置 CherryIN 并添加 agent 模型</p></figcaption></figure>

{% hint style="info" %}
已启用的 Google / Gemini 对话模型也可用于 Agent。若模型未出现在选择器中，请先确认 Provider 和模型均已启用，且模型类型不是嵌入、重排或生图。
{% endhint %}

### 第 2 步：进入工作页面

顶部点击 **工作** 进入 Agent 工作区。可以使用内置的 **Cherry Assistant**，也可以根据自己的需求新建 Agent。

<figure><img src="../.gitbook/assets/cherry-agent-step3-list.png" alt="Cherry Studio 工作页面"><figcaption><p>工作页面：左侧管理 Agent，右侧下达和执行任务</p></figcaption></figure>

### 第 3 步：新建一个 Agent

点击 Agent 列表中的添加入口，打开分步创建向导：

<figure><img src="../.gitbook/assets/cherry-agent-step3-create-form.png" alt=""><figcaption><p>添加 Agent 表单</p></figcaption></figure>

创建向导包含三步：

| 步骤       | 说明                      |
| -------- | ----------------------- |
| **基础信息** | 头像、名称、模型与描述；名称和模型为必填    |
| **角色设定** | 编写系统提示词，定义 Agent 的身份和行为 |
| **能力**   | 选择创建后启用的技能；内置技能默认可用     |

完成向导后点击 **创建**。工作区在开始任务时从输入框下方的工作区选择器中设置，可选择已有工作区、添加本地文件夹，或选择不使用工作目录。

### 第 4 步：调整 Agent 的提示词、工具与技能

点击 Agent 卡片本身，进入完整编辑面板：

<figure><img src="../.gitbook/assets/cherry-agent-step4-edit-panel.png" alt=""><figcaption><p>Agent 编辑面板（基础设置 Tab）</p></figcaption></figure>

编辑对话框的分类如下：

* **基础设置**：头像、名称、主模型、规划模型、小模型、描述、权限模式与心跳
* **提示词**：编辑系统提示词，决定 Agent 的角色与回应方式
* **工具 → 内置工具**：查看并禁用不希望 Agent 使用的内置工具
* **工具 → MCP**：挂载来自 [MCP 服务器](mcp/README.md) 的外部工具
* **工具 → 技能**：为 Agent 启用预先安装的 [技能](../pre-basic/settings/skills.md)
* **高级设置**：环境变量等高级配置

{% hint style="info" %}
编辑对话框会自动保存修改，关闭对话框时也会提交尚未完成的自动保存。已打开的 Agent 会话会接收模型、权限与工具策略等配置更新，无需先关闭全部会话。
{% endhint %}

#### 权限模式的 4 种选择

| 模式           | 行为                        | 适用场景                          |
| ------------ | ------------------------- | ----------------------------- |
| **普通模式**（默认） | 可自由读取文件；编辑文件或执行命令前会请求人工授权 | 日常对话型 Agent                   |
| **计划模式**     | 只能读取文件并制定计划，不能编辑或执行命令     | 让 Agent 给你"出方案"但你来执行          |
| **自动编辑模式**   | 可自由读写文件；执行命令前仍会请求授权       | 让 Agent 接管代码 / 文档编辑，但保留对命令的控制 |
| **全自动模式**    | 所有工具均无需人工授权               | 仅用于范围受控、明确需要无人确认的场景           |

{% hint style="danger" %}
**全自动模式**会让 Agent 跳过所有人工确认，包括写文件、删除文件、执行命令、调用外部 API 等。这意味着 Agent 可以不经你过目就删除或改写 `工作目录` 内的任意文件，一旦范围设置过大将造成**不可恢复的数据丢失**。

启用前请逐条确认：

* `工作目录` 必须是**仅用于本次任务的独立文件夹**，且其中不包含你不愿意被删除或覆盖的内容。
* **切勿**将整个磁盘、系统盘（`C:\`）、用户主目录（`C:\Users\...`、`~`）、桌面、下载、文档库或任何上级目录设为工作目录——历史上已多次出现 AI 在清理任务中误删整盘资料的情况。
* 启用前先完成系统级备份，确保即便发生误删也能恢复。
* 涉及删除、批量改名、递归处理等高危操作时，仍建议临时切回普通模式逐条确认。
  {% endhint %}

{% hint style="info" %}
所有 Agent 都具备任务管理、记忆和工作区能力；**权限模式**决定工具调用是否需要确认。[频道](agent-channels.md) 和[定时任务](scheduled-tasks.md)可以使用任意 Agent。
{% endhint %}

### 第 5 步：与 Agent 对话

返回 Agent 页面，点击 Agent 卡片进入会话：

* 在底部输入框输入任务，例如"请帮我把 `~/Downloads/report.md` 转成 PPT 大纲"
* 在输入框下方选择本次任务使用的 **工作区**；工作区决定 Agent 主要读写的目录
* Agent 会自动判断调用哪些工具、是否需要多轮推理
* 工具调用与决策过程以可折叠卡片形式逐步展示

#### 在右侧面板预览和编辑文件

Agent 生成或修改工作区文件后，可在右侧文件面板中搜索并打开文件。对于不超过 2 MiB、使用 UTF-8 编码且换行符统一为 LF 或 CRLF 的文本文件，可以从 **预览** 切换到编辑模式直接修改。

编辑内容会自动保存，没有单独的保存按钮。若在尚未保存完成时离开当前文件，Cherry Studio 会询问是否 **放弃并继续**；选择取消可留在当前文件继续编辑。

{% hint style="warning" %}
如果文件同时被外部程序修改，界面会提示“磁盘上的文件已发生变化”。选择 **重新加载文件** 会放弃当前草稿并读取磁盘上的最新内容；选择 **保留草稿** 会暂时停止自动保存，直到你处理冲突。二进制文件、超过 2 MiB 的文件、非 UTF-8 文本或混合换行符文件仍只能预览。
{% endhint %}

#### 成功标志

Agent 会在会话中展示任务进度、工具调用和最终结果。涉及写文件或执行命令时，普通模式会先显示权限确认；完成后可在右侧文件面板检查生成或修改的文件。

### 常见问题

#### Agent 页面提示 API 网关不可用

Agent 通常会自动启动所需的本地 API 网关。若仍出现此提示，请先重启 Cherry Studio；问题持续时，到 `设置 → API 网关` 检查端口是否被占用，并尝试手动启动。详情见 [API 网关](api-server.md)。

#### 创建 Agent 时下拉里没有模型

* 确认 Provider 与模型均已启用
* 确认至少添加了一个对话模型；嵌入、重排和生图模型不会出现在 Agent 模型选择器中
* Google / Gemini 模型可用于 Agent；若未出现，请检查 Google Provider 是否启用

#### Agent 输出突然停止

Agent 运行失败时会在对话中显示错误。请先展开错误信息，检查模型额度、API 网关自动启动状态、权限请求、工作区访问或工具执行失败。

### 下一步

* 把 Agent 接到 IM 平台（飞书 / Telegram / QQ / 微信 / Discord / Slack）→ [频道](agent-channels.md)
* 让 Agent 定时自动执行任务 → [定时任务](scheduled-tasks.md)
* 拓展工具能力 → [MCP 使用教程](mcp/README.md)

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../question-contact/suggestions.md) 中提供的官方渠道。


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.cherryai.com.cnagent.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
