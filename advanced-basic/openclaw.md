---
icon: spider
---

# OpenClaw

OpenClaw 是一个独立的外部 Agent CLI 工具，Cherry Studio v1.9.x 提供原生集成入口，把你在 Cherry Studio 中已配置的 Provider / 模型暴露给 OpenClaw 使用。

{% hint style="info" %}
OpenClaw 本身不是 Cherry Studio 的一部分。如果你只想在 Cherry Studio 内使用 Agent，请直接看 [Cherry Agent](agent.md)；OpenClaw 是给愿意用命令行 + 更深度自定义场景的用户准备的。
{% endhint %}

### 安装 OpenClaw

顶部 Tab `+` → **启动台** → 点击 **OpenClaw**。首次进入会看到：

<figure><img src="../.gitbook/assets/cherry-openclaw.png" alt=""><figcaption><p>OpenClaw 未安装态</p></figcaption></figure>

* 点击 **安装 OpenClaw** → Cherry Studio 会从官方源下载并安装 OpenClaw 二进制
* 安装完成后页面会变为"运行中 / 已停止"状态，可在此**启动**或**停止**本地 OpenClaw gateway

### 配置 Provider 与模型

在 OpenClaw 页面中：

1. 选择要给 OpenClaw 使用的 **Provider**（必须是已在 `设置 → 模型服务` 中配置好的）
2. 选择具体的 **模型**
3. 点击 **启动**，OpenClaw 即开始在本地监听

### 在 OpenClaw CLI 中使用

启动后，在终端运行 `openclaw` 命令即可使用 Cherry Studio 中的模型。

* 详细 CLI 用法请见官方文档：[https://docs.openclaw.ai/](https://docs.openclaw.ai/)
* 点击 OpenClaw 页面右上角 **查看文档** 直达

### 与 [Cherry Agent](agent.md) 的区别

| 维度 | Cherry Agent | OpenClaw |
|---|---|---|
| 运行位置 | Cherry Studio 内 | 独立 CLI |
| UI | Cherry Studio 图形界面 | 终端 |
| 适合场景 | 日常对话型 Agent、IM 接入 | CLI 工作流、脚本自动化、CI 集成 |
| 是否依赖 [API 服务器](api-server.md) | 是 | 否（OpenClaw 走独立 gateway） |

### 提示与技巧

* OpenClaw 与 Cherry Agent 可同时使用，互不冲突
* 一台机器上 OpenClaw gateway 启动后会占用本地端口（默认见 OpenClaw 文档），与 [API 服务器](api-server.md) 默认 23333 不冲突
* 关闭 Cherry Studio 时 OpenClaw gateway 会自动停止；如需后台常驻请用 OpenClaw 自带的 daemon 模式

如遇问题，请在 [反馈与建议](../question-contact/suggestions.md) 中提交反馈，或前往 [OpenClaw 官方仓库](https://github.com/openclaw)。
