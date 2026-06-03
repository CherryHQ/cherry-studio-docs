---
icon: sparkles
---

# 技能（Skills）

技能（Skills）是 Cherry Studio v1.9.x 引入的**可装卸能力包**，让你能给助手或 Agent 注入"写邮件"、"画流程图"、"生成 PPT"等专门技能，避免每次都手写完整提示词。

### 在哪里管理技能

打开 `设置 → 技能`：

<figure><img src="../../.gitbook/assets/cherry-skills.png" alt=""><figcaption><p>技能管理面板</p></figcaption></figure>

可看到：

* **已安装**：当前账号已添加的技能
* **内置**：Cherry Studio 自带的内置技能（无需安装即可使用）
* **搜索 / 筛选**：按名称或类别筛选

### 安装技能

1. 在技能管理面板点击 **添加更多技能**
2. 在技能市场中浏览或搜索
3. 点击安装即可，之后在助手或 Agent 设置中可勾选启用

### 在助手中启用技能

* 进入 `助手设置 → 技能`
* 勾选要启用的技能
* 对话时助手会按提示词自动调用所选技能

### 在 [Cherry Agent](../../advanced-basic/agent.md) 中启用

* 进入 Agent 编辑界面 → `工具` 选项卡
* 在"技能"分组下勾选启用
* Agent 会自主决定何时调用

### 技能 vs MCP 工具 vs Provider

| 类型 | 提供方 | 适合做什么 |
|---|---|---|
| **技能（Skills）** | 内置或第三方技能包 | 模板化任务（写邮件 / 画图 / 写 PPT） |
| **[MCP 工具](../../advanced-basic/mcp/)** | 任意 MCP Server | 需要调用外部 API / 系统命令的任务 |
| **Provider 模型** | 各 AI 厂商 | 底层对话能力 |

三者可叠加：一个 Agent 可以同时挂载多个技能 + 多个 MCP 工具 + 任一 Provider 的模型。

如遇问题，请在 [反馈与建议](../../question-contact/suggestions.md) 中提交反馈。
