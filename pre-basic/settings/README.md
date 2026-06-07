---
icon: gear
---

# 设置

Cherry Studio 的设置面板覆盖**模型配置、界面行为、数据备份、个性化**等所有偏好选项。本节按主题分篇详解，下面是地图：

### 模型与默认值

| 文档 | 内容 |
|---|---|
| [模型服务设置](providers.md) | Provider 添加、密钥、API 地址、多 Key 轮询 |
| [默认模型设置](default-models.md) | 全局默认对话/嵌入/助手模型 |

### 应用行为

| 文档 | 内容 |
|---|---|
| [常规设置](general.md) | 语言、代理、通知、启动、托盘等基础项 |
| [显示设置](display.md) | 侧边栏位置、字体、消息样式 |
| [快捷键设置](key-shortcut.md) | 全部快捷键的修改与启停 |
| [语音功能](yu-yin-gong-neng.md) | 语音输入与朗读 |

### 数据与备份

| 文档 | 内容 |
|---|---|
| [数据设置](../data-settings/) | WebDAV / S3 / 笔记类备份与第三方集成 |
| [个性化设置](../personalization-settings/) | CSS、字体、存储位置 |

### 进阶能力（在主菜单里也属于"设置"）

| 功能 | 文档 |
|---|---|
| [API 服务器](../../advanced-basic/api-server.md) | 暴露本地 OpenAI 兼容 API |
| [全局记忆](../../advanced-basic/memory.md) | 跨会话记忆系统 |
| [技能](skills.md) | 为助手或智能体加装专项能力 |
| [快捷短语](quick-phrase.md) | 管理可复用提示词模板 |
| [频道](../../advanced-basic/agent-channels.md) | Agent 接入飞书/Telegram 等 |
| [定时任务](../../advanced-basic/scheduled-tasks.md) | Agent 按 Cron 定时运行 |
| [MCP 服务器](../../advanced-basic/mcp/) | Model Context Protocol 工具接入 |

{% hint style="info" %}
设置改动会**实时生效**，无需重启。涉及 Provider / Model / 默认模型这类核心项时，建议先在 `设置 → 数据设置 → 备份` 中做一次备份。
{% endhint %}

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
