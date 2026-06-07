---
icon: spider
---

# OpenClaw

**OpenClaw 是一款独立的开源 AI 智能体工具**，提供高可定制性的 Agent 运行与交互服务，由独立开源团队开发。

对于想要体验 OpenClaw 强大能力的普通用户，Cherry Studio 提供了 **一键式集成接口**。你无需自己折腾复杂的底层命令、运行依赖和代理，直接在 Cherry Studio 内即可复用已配置好的模型服务（Provider）一键开启 OpenClaw 托管服务。

{% hint style="info" %}
**我是否需要 OpenClaw？**

* **普通用户**：如果你仅在 Cherry Studio 客户端的图形界面里日常使用智能体，直接参考 **[智能体](agent.md)** 即可，**不需要** 启用 OpenClaw。
* **尝试体验/深度用户**：如果你希望在终端或独立工作流中体验 OpenClaw 项目，可以使用本模块来快速启动 Gateway 服务。
{% endhint %}

### 安装 OpenClaw

在顶部 Tab 栏点击 `+` ➡️ **启动台** ➡️ 点击 **OpenClaw** 图标。首次进入会看到：

<figure><img src="../.gitbook/assets/cherry-openclaw.png" alt=""><figcaption><p>OpenClaw 未安装状态</p></figcaption></figure>

* 点击 **安装 OpenClaw** ➡️ Cherry Studio 会自动从官方源下载并安装 OpenClaw 的最新运行二进制包。
* 安装完成后，页面会转为“运行中 / 已停止”状态，你可在这里一键 **启动** 或 **停止** 本地 OpenClaw Gateway。

### 配置 Provider 与模型

在 OpenClaw 配置面板中：

1. 选择要分配给 OpenClaw 使用的 **Provider 服务商**（必须是已在 `设置 → 模型服务` 中配置完毕的平台）。
2. 选择具体的 **模型**。
3. 点击 **启动** 按钮，OpenClaw Gateway 就会在本地监听端口并开始服务。

### 在 OpenClaw CLI 中使用

一键启动后，在你的终端里直接运行 `openclaw` 即可调用你在 Cherry Studio 托管启动的算力和模型。

* 详细 CLI 使用手册请阅读官方文档：[https://docs.openclaw.ai/](https://docs.openclaw.ai/)
* 亦可直接点击 OpenClaw 配置页面右上角的 **查看文档** 直达。

### 与 [智能体](agent.md) 的根本定位区别

两者并不简单是“命令行与图形界面”的划分，它们在 Cherry Studio 里的定位截然不同：

| 维度 | Cherry Agent (内置智能体) | OpenClaw |
|---|---|---|
| **运行位置** | 客户端（Cherry Studio）原生内部运行 | 独立的外部进程 Gateway |
| **产品定位** | 与客户端 UI 原生深度绑定的工具和流程型智能体 | 为想要尝鲜的用户 **极大地降低 OpenClaw 项目的底层依赖、代理及环境配置成本** |
| **交互界面** | Cherry Studio 图形对话窗口 | 终端 CLI 交互或其他支持 OpenClaw 接口的客户端 |
| **运行依赖** | 必须依赖客户端内的 **[API 服务器](api-server.md)** | 独立 Gateway，由 Cherry Studio 提供一键环境托管 |

### 提示与技巧

* OpenClaw 与内置的 Cherry Agent 可在系统中并行不悖地使用，互不冲突。
* 一台机器上 OpenClaw Gateway 启动后会占用其特定的本地端口（具体见 OpenClaw 文档说明），与 Cherry Studio 内置 **[API 服务器](api-server.md)** 默认监听的 `23333` 端口完全独立、互不干扰。
* 当关闭 Cherry Studio 软件时，被托管启动的 OpenClaw Gateway 服务会自动停止；若需要在后台长期常驻运行，建议使用 OpenClaw 官方自带的守护进程（Daemon）模式。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../question-contact/suggestions.md) 中提供的官方渠道，或前往 [OpenClaw 官方仓库](https://github.com/openclaw) 参与开源讨论。
