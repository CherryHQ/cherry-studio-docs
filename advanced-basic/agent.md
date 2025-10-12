---
icon: robot
---

# Cherry Agent 使用教程

Cherry Studio v1.7.0.alpha 版本引入了Agent，可以在 Cherry Studio 中使用 Cherry Agent 。本教程将引导您完成设置和启动的完整流程。

### 1. 创建 Anthropic 类型的供应商

&#x20;任意支持 Anthropic 端点的服务商都可以使用，以 CherryIn 为例，创建一个新的 Agent 服务商，填写好密钥和地址，添加任意模型即可。

{% hint style="warning" %}
Agent 模式消耗 token 量很大，请注意 token 使用
{% endhint %}

{% hint style="info" %}
订阅了 Claude Code 的用户也可以将 key 和 url 地址填入获取到模型
{% endhint %}

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.26.35@2x.png" alt=""><figcaption></figcaption></figure>

### 2. 开启 API 服务器

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 19.56.22@2x.png" alt=""><figcaption></figcaption></figure>

### 3. 创建一个 Agent

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.24.43@2x.png" alt=""><figcaption></figcaption></figure>

右键 Agent 可以进入编辑界面，编辑 Agent 的权限和可以使用的工具或 mcp 服务。

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.25.10@2x (1).png" alt=""><figcaption></figcaption></figure>

### 结果展示

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.30.26@2x (1).png" alt=""><figcaption></figcaption></figure>
