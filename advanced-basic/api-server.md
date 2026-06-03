---
icon: server
---

# API 服务器

API 服务器是 Cherry Studio 在本地启动的一个 **OpenAI 兼容 HTTP 服务**，用于把 Cherry Studio 已配置的所有模型与能力暴露给本机其他程序使用。它同时是 [Cherry Agent](agent.md) 与 [频道（Cherry Claw）](agent-channels.md) 的运行底座 —— 想使用 Agent 必须先启用 API 服务器。

### 启用 API 服务器

1. 打开 `设置 → API 服务器`
2. 默认监听端口为 **23333**，如端口被占用可改为其他空闲端口（建议 1024 以上）
3. 点击右上角绿色 **▶ 启动** 按钮

<figure><img src="../.gitbook/assets/cherry-api-server-stopped.png" alt=""><figcaption><p>未启用时显示"已停止"，并提示"请启用 API 服务器以使用智能体功能"</p></figcaption></figure>

启动成功后，状态变为绿色 **运行中**，并显示监听地址 `http://127.0.0.1:<port>`：

<figure><img src="../.gitbook/assets/cherry-api-server-running.png" alt=""><figcaption><p>运行中状态，包含"重启"与"停止"按钮</p></figcaption></figure>

### API 密钥与授权头

每次启动会生成一个 **API 密钥**（形如 `cs-sk-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`），用于客户端访问的安全认证令牌。

调用 API 时需在请求头加入：

```
Authorization: Bearer cs-sk-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

如怀疑密钥泄露，点击 **重新生成** 即可换新密钥（旧密钥立即失效）。

{% hint style="warning" %}
API 密钥拥有访问你 Cherry Studio 内全部 Provider 的权限，**请勿在公网或团队共享渠道暴露**。
{% endhint %}

### 查看 API 文档

页面右上角点击 **API 文档** 按钮可打开内置的 OpenAPI 接口文档（Swagger 风格），包含完整的端点与请求示例。

### 端口冲突排查

启动失败并提示 `EADDRINUSE: address already in use 127.0.0.1:<port>` 时：

1. 大概率是已有另一个 Cherry Studio 实例占用了同一端口
2. 在端口输入框改为其他空闲端口后再次启动
3. 或在终端使用 `lsof -i :<port>` 查出占用进程并处理

### 重启与停止

* **重启**：点击 ↻ 图标，常用于切换端口或刷新密钥后生效
* **停止**：点击红色 ⏹ 图标，会立即关闭服务，Agent 与频道一并暂停

{% hint style="info" %}
API 服务器仅监听 `127.0.0.1`，**不会**暴露到局域网或公网。若需要跨机访问，请配合 SSH 反向隧道或类似方案。
{% endhint %}

### 下一步

* 启用后即可继续配置 [Cherry Agent](agent.md)
* 想把 Agent 接入飞书 / Telegram / Discord 等 IM 平台，请阅读 [频道（Cherry Claw）](agent-channels.md)
