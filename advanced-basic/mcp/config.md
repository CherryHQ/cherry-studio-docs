# 配置和使用 MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. 打开 Cherry Studio 设置。
2. 找到 `MCP 服务器` 选项。
3. 点击 `添加服务器`。
4. 将 MCP Server 的相关参数填入（[参考链接](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。可能需要填写的内容包括：
   * 名称：自定义一个名称，例如 `fetch-server`
   * 类型：选择 `STDIO`
   * 命令：填写 `uvx`
   * 参数：填写 `mcp-server-fetch`
   * （可能还有其他参数，视具体 Server 而定）
5. 点击 `保存`。

{% hint style="success" %}
完成上述配置后，Cherry Studio 会自动下载所需的 MCP Server - `fetch server`。下载完成后，我们就可以开始使用了！注意：当 mcp-server-fetch 配置不成功的时候，可以尝试重启一下电脑。
{% endhint %}

### 在聊天框中启用 MCP 服务

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* 在 `MCP 服务器` 设置成功添加了 MCP 服务器

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **使用效果展示**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

从上图可以看出，结合了 MCP 的 `fetch` 功能后，Cherry Studio 能够更好地理解用户的查询意图，并从网络上获取相关信息，给出更准确、更全面的回答。
