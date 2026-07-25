# PPIO 派欧云

PPIO 派欧云是 Cherry Studio 内置的模型服务商之一。配置 API Key 后，可以在客户端中获取并使用 PPIO 当前提供的模型。

## 使用前准备

1. 登录 [PPIO 控制台](https://ppinfra.com/)。
2. 创建 API Key，并在生成时妥善保存。
3. 确认账户具备目标模型的调用权限和可用额度。

{% hint style="warning" %}
API Key 属于敏感凭据。不要把它放进截图、公开文档、群聊或 Git 仓库；怀疑泄露时请立即在 PPIO 控制台撤销。
{% endhint %}

## 在 Cherry Studio 中配置

1. 打开 **设置 → 模型服务**。
2. 在内置 Provider 列表中选择 **PPIO 派欧云**。
3. 粘贴 API Key。
4. API 地址没有特殊需求时保留默认值：`https://api.ppinfra.com/v3/openai`。
5. 点击 **获取模型列表**，添加要使用的模型。
6. 选择一个对话模型并点击 **检测**。

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt="在 Cherry Studio 中配置 PPIO API Key"><figcaption><p>配置 PPIO 模型服务</p></figcaption></figure>

## 开始对话

检测成功后回到对话页，从模型选择器中选择刚添加的 PPIO 模型，再发送一条简短测试消息。

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt="在对话页选择 PPIO 模型"><figcaption><p>选择 PPIO 模型开始对话</p></figcaption></figure>

## 如何判断配置成功

* Provider 页面能获取到模型列表；
* 点击检测后返回成功；
* 对话页能选择该模型并收到正常回复。

## 常见问题

* **401 / 403**：检查 API Key 是否正确、是否已撤销，以及账户是否有模型权限。
* **模型不可用**：重新获取模型列表，并以 PPIO 控制台的当前状态为准。
* **连接超时**：检查网络和系统代理，确认 API 地址没有多余路径。
* **额度不足**：到服务商控制台查看余额、限额和计费状态。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
