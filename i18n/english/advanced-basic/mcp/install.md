
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# MCP Environment Installation

**MCP (Model Context Protocol)** is an open-source protocol designed to provide context information to large language models (LLMs) in a standardized manner. For more details about MCP, see [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Using MCP in Cherry Studio

The following demonstrates how to use MCP in Cherry Studio using the `fetch` feature as an example. Detailed information can be found in the [documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Prerequisites: Installing uv and bun**

{% hint style="warning" %}
Cherry Studio currently only uses built-in [uv](https://github.com/astral-sh/uv) and [bun](https://github.com/oven-sh/bun), and **will not reuse** uv or bun already installed on your system.
{% endhint %}

In `Settings > MCP Server`, click the `Install` button to automatically download and install them. Downloads are sourced directly from GitHub and may be slow with a high probability of failure. Installation success should be verified by checking for files in the directories mentioned below.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Executable Installation Directories:**

Windows: `C:\Users\username\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin directory</p></figcaption></figure>

**If unable to install normally:**

You can create symlinks from the system's corresponding commands to these locations. If the directory doesn't exist, create it manually. Alternatively, manually download executables and place them in this directory:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)