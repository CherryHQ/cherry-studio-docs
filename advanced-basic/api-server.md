---
icon: server
---

# API 服务器

API 服务器的核心作用：**将 Cherry Studio 中已配置的 AI 能力，通过本地接口对外开放**（同时也是智能体功能的底层依赖），供其他程序调用。

使用场景：你已在 Cherry Studio 中配置了 OpenAI、Anthropic、DeepSeek 等服务商。若你的其他工具（例如某个编程插件或自定义脚本）希望调用相同的 AI 能力，**API 服务器**会在本机开放一个标准接口，使这些工具可直接复用 Cherry Studio 已有配置，无需重复注册各家账号。

**何时需要启用？**

* 使用 [智能体](agent.md) → **必须启用**
* 让 Agent 接入 IM 平台（[频道](agent-channels.md)）→ **必须启用**
* 仅使用 Cherry Studio 普通对话、绘画、翻译等功能 → **无需启用**

> 推荐先阅读 [概念入门](concepts-101.md) 了解 Agent、频道等相关概念。

### 启用 API 服务器

1. 打开 `设置 → API 服务器`
2. 默认监听端口为 **23333**，可填入 **1000-65535** 之间的任意空闲端口
3. 点击右上角绿色 **▶ 启动** 按钮

<figure><img src="../.gitbook/assets/cherry-api-server-stopped.png" alt=""><figcaption><p>未启用时显示"已停止"，并提示"请启用 API 服务器以使用智能体功能"</p></figcaption></figure>

启动成功后，状态变为绿色 **运行中**，并显示监听地址 `http://127.0.0.1:<port>`：

<figure><img src="../.gitbook/assets/cherry-api-server-running.png" alt=""><figcaption><p>运行中状态，包含"重启"与"停止"按钮</p></figcaption></figure>

{% hint style="info" %}
**修改端口的方式**：端口输入框在服务器运行时是只读的。如需修改，请先点击 ⏹ **停止**，改完端口再启动。
{% endhint %}

### API 密钥与授权头

**API 密钥**形如 `cs-sk-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`，在首次启用 API 服务器时自动生成并**持续保留**，重启服务器不会刷新。

如需手动换新：**必须先点击 ⏹ 停止服务器**，密钥右侧才会出现 **重新生成** 按钮（运行中只显示复制按钮）。点击后旧密钥立即失效，再次启动会生成新密钥。

调用 API 时需在请求头加入：

```
Authorization: Bearer cs-sk-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

{% hint style="warning" %}
API 密钥拥有访问你 Cherry Studio 内全部 Provider 的权限，**请勿在公网或团队共享渠道暴露**。
{% endhint %}

### 查看 API 文档

页面右上角点击 **API 文档** 按钮可打开内置的 OpenAPI 接口文档（Swagger 风格），包含完整的端点与请求示例。

### 端口冲突排查

启动失败并提示 `EADDRINUSE: address already in use 127.0.0.1:<port>` 时：

1. 大概率是另一个 Cherry Studio 实例占用了同一端口
2. 点击 ⏹ 停止，把端口改成其他空闲值再启动
3. 或在终端执行 `lsof -i :<port>`（macOS / Linux）查出占用进程并处理

### 重启与停止

* **重启**：点击 ↻ 图标，常用于密钥重新生成后强制刷新所有连接
* **停止**：点击红色 ⏹ 图标，会立即关闭服务；正在使用 [智能体](agent.md) 与 [频道](agent-channels.md) 的连接会同步中断

{% hint style="info" %}
API 服务器仅监听 `127.0.0.1`，**不会**暴露到局域网或公网。若需要跨机访问，请配合 SSH 反向隧道或类似方案。
{% endhint %}

### 下一步

* 启用后即可继续配置 [智能体](agent.md)
* 想把 Agent 接入飞书 / Telegram / Discord 等 IM 平台，请阅读 [频道](agent-channels.md)

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../question-contact/suggestions.md) 中提供的官方渠道。
