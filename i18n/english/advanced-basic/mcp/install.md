# MCP Environment Setup


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="warning" %}
This document is translated from Chinese by AI and has not yet been reviewed. I will try to check the document one by one to ensure the translation is reasonable.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**MCP (Model Context Protocol)** is an open-source protocol designed to provide context information to Large Language Models (LLMs) in a standardized way. For more information about MCP, please refer to [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Using MCP in Cherry Studio

Below, taking the `fetch` function as an example, we demonstrate how to use MCP in Cherry Studio. Details can be found in the [documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparation: Install uv, bun**

{% hint style="warning" %}
Cherry Studio currently only uses the built-in [uv](https://github.com/astral-sh/uv) and [bun](https://github.com/oven-sh/bun), and **will not reuse** uv and bun already installed in the system.
{% endhint %}

In `Settings - MCP Server`, click the `Install` button to automatically download and install. Since it's downloaded directly from GitHub, the speed might be slow, and there's a high chance of failure. Whether the installation is successful depends on whether there are files in the folder mentioned below.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Executable Installation Directory:**

Windows: `C:\Users\Username\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin directory</p></figcaption></figure>

**If installation fails:**

You can soft link the corresponding commands in the system here. If the corresponding directory does not exist, you need to create it manually. Alternatively, you can manually download the executable files and place them in this directory:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)