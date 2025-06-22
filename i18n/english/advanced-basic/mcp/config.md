
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Configuring and Using MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Open Cherry Studio settings.
2. Find the `MCP Server` option.
3. Click `Add Server`.
4. Fill in the parameters for the MCP Server ([reference link](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). This may include:
   * Name: Custom name, e.g., `fetch-server`
   * Type: Select `STDIO`
   * Command: Enter `uvx`
   * Arguments: Enter `mcp-server-fetch`
   * (Additional parameters may be required depending on the specific Server)
5. Click `Save`.

{% hint style="success" %}
After completing the above configuration, Cherry Studio will automatically download the required MCP Server - `fetch server`. Once downloaded, we can start using it! Note: If mcp-server-fetch configuration fails, try restarting your computer.
{% endhint %}

### Enabling MCP Service in the Chatbox

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* After successfully adding the MCP server in `MCP Server` settings

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demonstration of Usage Effects**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

As shown above, after integrating MCP's `fetch` functionality, Cherry Studio can better understand user query intentions. It retrieves relevant information from the web to provide more accurate and comprehensive responses.