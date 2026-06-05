# 配置和使用 MCP

本页用一个最常见的例子 —— **让 AI 能上网取页面内容**（叫 `fetch`，由 MCP 官方提供）—— 带你走完一次完整的 MCP 配置。后续装其他 MCP，流程基本相同。

> 不知道 MCP 是什么？先看 [MCP 使用教程总览](README.md)。

## 添加一个 MCP（以 fetch 为例）

<figure><img src="../../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption><p>MCP 服务器添加界面</p></figcaption></figure>

1. 打开 `设置 → MCP 服务器`
2. 点击 `+ 添加服务器`
3. 在弹出的表单中填写以下信息：

| 字段 | 填什么 | 说明 |
|---|---|---|
| **名称** | `fetch-server` | 自己取一个好认的名字，影响不到功能 |
| **类型** | `STDIO` | 这是常见的"本地命令行"类型 |
| **命令** | `uvx` | Cherry Studio 内置的 Python 工具，会自动下载所需脚本 |
| **参数** | `mcp-server-fetch` | 告诉 uvx 要装哪个 MCP |

4. 点击 `保存`，Cherry Studio 会自动下载 `fetch` 这个 MCP（首次需要联网）

{% hint style="success" %}
**保存后无明显反馈？** 部分 MCP 首次下载耗时较长（需从 GitHub 获取代码）。可点击服务器条目查看状态：
* 🟢 绿色 = 已就绪
* 🟡 黄色 = 下载或启动中
* 🔴 红色 = 失败，可点击查看错误日志

若长时间显示红色，请参考 [常见问题](chang-jian-wen-ti.md) 或重启 Cherry Studio 后重试。
{% endhint %}

## 这些字段从哪儿找？

不同 MCP 要填的"命令"和"参数"不一样。看 MCP 自己的说明页：

* **官方 MCP**：去 [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 找对应仓库，README 顶部会给一段配置示例
* **第三方 MCP**：开发者的 GitHub README 里也会给

不会读？让 Cherry Studio 帮你：参考 [自动安装 MCP](auto-install.md)，直接对 AI 说"帮我装一个 fetch MCP"就行。

## 让 AI 用上 MCP

添加完只是"装好了"，还需要在**对话里告诉 AI 它可以用**：

1. 在 [对话界面](../../cherrystudio/preview/chat.md) 的输入框下方找到 **MCP 工具** 图标
2. 点开，勾选你刚才添加的服务器
3. 正常提问，比如：**帮我抓一下 `https://docs.cherry-ai.com` 这个页面的标题和大纲**
4. AI 会自动调用 fetch MCP 去拿网页，然后回答你

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例 (1).png" alt=""><figcaption><p>对话框里的 MCP 工具选择</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/MCP服务器示例 (1).png" alt=""><figcaption><p>选择已启用的 MCP 服务器</p></figcaption></figure>

### 效果展示

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

不用 MCP 时，AI 只能凭"训练时见过的资料"回答；接上 fetch 后，AI 可以"现去网上看"，回答就准确得多。

## 给 [Cherry Agent](../agent.md) 装 MCP

如果你在用 Cherry Agent，MCP 的接入位置不同：

1. 进入 Agent 编辑界面 → `工具` 选项卡
2. 在 "MCP" 分组下勾选你要让该 Agent 使用的服务器
3. Agent 会自主决定何时调用

## 想再装一个不一样的？

* 想让 AI 操作你的本地文件 → 装 **filesystem** MCP
* 想让 AI 操作浏览器 → 装 **playwright** MCP
* 想让 AI 查 Notion → 装 **notion** MCP

所有这些都在 [官方仓库](https://github.com/modelcontextprotocol/servers) 里有现成配置示例，复制粘贴即可。
