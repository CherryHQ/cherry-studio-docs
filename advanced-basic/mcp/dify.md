# 配置 Dify 知识库

[Dify](https://dify.ai/) 是一个 AI 应用开发平台，也提供知识库功能。通过 Cherry Studio 内置的 `@cherry/dify-knowledge` MCP 服务器，你可以在对话或工作中查询已有的 Dify 知识库，无需重复导入资料。

<figure><img src="../../.gitbook/assets/cherry-dify-mcp-flow.svg" alt="Dify 知识库接入 Cherry Studio 的流程"><figcaption><p>Dify 提供知识库与 API，MCP 服务器完成连接，再由 Cherry Studio 的对话或工作调用</p></figcaption></figure>

## 使用前准备

你需要：

* 一个可正常访问的 Dify 实例；
* 至少一个已经完成索引的 Dify 知识库；
* 该知识库的 API Key；
* 一个支持工具调用的对话模型。

{% hint style="warning" %}
Dify API Key 属于敏感凭据。不要把它放进截图、公开文档、群聊或 Git 仓库；怀疑泄露时请立即在 Dify 中撤销并重新生成。
{% endhint %}

## 添加 Dify MCP 服务器

1. 打开 **设置 → MCP**。
2. 在内置服务器中找到 `@cherry/dify-knowledge`，点击添加或启用。
3. 打开服务器配置，填写 Dify 地址和 `DIFY_KEY`。
4. 保存后确认服务器状态正常，并已加载知识库查询工具。

## 获取知识库 API Key

在 Dify 中打开目标知识库，进入 API 访问或 API 扩展页面，创建并复制知识库 API Key。不同 Dify 版本的入口名称可能略有差异，以当前界面为准。

## 在对话或工作中使用

1. **对话**：在当前助手中启用 Dify MCP 服务器，新建话题，并明确要求模型从 Dify 知识库检索后回答。
2. **工作**：在目标工作区或 Agent 中启用相同服务器，让多步骤任务在需要时调用知识库。
3. 检查工具调用记录和引用内容，确认结果来自目标知识库。

## 排查连接失败

* **401 / 403**：检查 API Key 是否属于目标知识库，以及是否已被撤销。
* **无法连接**：检查 Dify 地址、反向代理、证书和当前网络。
* **查不到内容**：确认知识库文档已经完成索引，并尝试使用更明确的关键词。
* **对话里没有工具**：确认服务器和当前助手均已启用 MCP。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
