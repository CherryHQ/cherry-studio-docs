
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# MCP Environment Setup

**MCP (Model Context Protocol)** is an open-source protocol designed to provide context information to Large Language Models (LLMs) in a standardized way. For more information about MCP, please see [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Using MCP in Cherry Studio

The following uses the `fetch` feature as an example to demonstrate how to use MCP in Cherry Studio. You can find more details in the [documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparation: Install uv, bun**

{% hint style="warning" %}
Cherry Studio currently only uses the built-in [uv](https://github.com/astral-sh/uv) and [bun](https://github.com/oven-sh/bun), and **will not reuse** any existing installations of uv and bun on the system.
{% endhint %}

In `Settings - MCP Server`, click the `Install` button to automatically download and install them. Since the downloads are directly from GitHub, the speed might be slow, and there is a high chance of failure. The success of the installation depends on whether the files exist in the folder mentioned below.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Executable Installation Directory:**

Windows: `C:\Users\YourUsername\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin directory</p></figcaption></figure>

**If the installation fails:**

You can create a symbolic link (soft link) from the corresponding system command to this directory. If the directory does not exist, you need to create it manually. Alternatively, you can manually download the executable files and place them in this directory:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)