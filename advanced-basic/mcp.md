---
icon: monero
---

# MCP 使用教程

**MCP(Model Context Protocol)** 是一种开源协议，旨在以标准化的方式向大语言模型（LLM）提供上下文信息。更多关于 MCP 的介绍请见 [#shen-me-shi-mcpmodel-context-protocol](../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## 在 Cherry Studio 中使用 MCP

下面以 `fetch` 功能为例，演示如何在 Cherry Studio 中使用 MCP，可以在[文档](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)中查找详情。

### **准备工作：安装 uv、bun**

{% hint style="warning" %}
Cherry Studio 目前只使用内置的 [uv](https://github.com/astral-sh/uv) 和 [bun](https://github.com/oven-sh/bun)，**不会复用**系统中已经安装的 uv 和 bun。
{% endhint %}

在 `设置 - MCP 服务器` 中，点击 `安装` 按钮，即可自动下载并安装。因为是直接从 GitHub 上下载，速度可能会比较慢，且有较大可能失败。安装成功与否，以下文提到的文件夹内是否有文件为准。

<figure><img src="../.gitbook/assets/MCP-安装UV-BUN.png" alt=""><figcaption><p>MCP 设置界面</p></figcaption></figure>

**可执行程序安装目录：**

Windows: `C:\Users\用户名\.cherrystudio\bin`

macOS，Linux: `~/.cherrystudio/bin`

<figure><img src="../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin 目录</p></figcaption></figure>

**无法正常安装的情况下：**

可以将系统中的相对应命令使用软链接的方式链接到这里，如果没有对应目录，需要手动建立。也可以手动下载可执行文件放到这个目录下面：

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)

### **配置 MCP 服务器**

<figure><img src="../.gitbook/assets/PixPin_2025-03-10_20-42-38.png" alt=""><figcaption></figcaption></figure>

1. 打开 Cherry Studio 设置。
2. 找到 "MCP 服务器" 选项。
3. 点击 "添加服务器"。
4. 将 MCP Server 的相关参数填入（[参考链接](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。可能需要填写的内容包括：
   * 名称：自定义一个名称，例如 `fetch-server`
   * 类型：选择 `STDIO`
   * 命令：填写 `uvx`
   * 参数：填写 `mcp-server-fetch`
   * （可能还有其他参数，视具体 Server 而定）
5. 点击“确定”保存。

{% hint style="success" %}
完成上述配置后，Cherry Studio 会自动下载所需的 MCP Server - `fetch server`。下载完成后，我们就可以开始使用了！注意：当mcp-server-fetch配置不成功的时候，可以尝试重启一下电脑。{% endhint %}

### 在聊天框中启用 MCP 服务

<figure><img src="../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

在聊天框看到启用 MCP 服务的按钮，需要满足以下条件：

* 需要使用支持函数调用（在模型名字后会出现扳手符号）的模型

<figure><img src="../.gitbook/assets/函数调用示例图.png" alt=""><figcaption></figcaption></figure>

* 在 `MCP 服务器` 设置成功添加了 MCP 服务器

<figure><img src="../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **使用效果展示**

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

从上图可以看出，结合了 MCP 的 `fetch` 功能后，Cherry Studio 能够更好地理解用户的查询意图，并从网络上获取相关信息，给出更准确、更全面的回答。

### **自动安装 MCP**
> cherry-studio@v1.1.18
#### 功能简介

除了手动安装外，Cherry Studio 还内置了 `@mcpmarket/mcp-auto-install` 工具，这是一个更便捷的 MCP 服务器安装方式。你只需要在支持 MCP 服务的大模型对话中输入相应的指令即可。

{% hint style="warning" %}
**测试阶段提醒：**
* `@mcpmarket/mcp-auto-install` 目前仍处于测试阶段
* 效果依赖大模型的"智商"，有些会自动添加，有些还是**需要在 MCP 设置中再手动更改某些参数**
* 目前搜索源是从 @modelcontextprotocol 中进行搜索，可以自行配置(下方说明)
* 
{% endhint %}

#### 使用说明

例如，你可以输入：
```
帮我安装一个 filesystem mcp server
```

<figure><img src="../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>输入指令安装 MCP 服务器</p></figcaption></figure>

<figure><img src="../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP 服务器配置界面</p></figcaption></figure>

系统会自动识别你的需求，并通过 `@mcpmarket/mcp-auto-install` 完成安装。这个工具支持多种类型的 MCP 服务器，包括但不限于：
- filesystem（文件系统）
- fetch（网络请求）
- sqlite（数据库）
- 等等...

> MCP_PACKAGE_SCOPES 变量可以自定义 mcp 服务搜索源，默认值为：@modelcontextprotocol，可以自定义配置

#### @mcpmarket/mcp-auto-install 库的介绍

{% hint style="info" %}
**默认配置参考：**
```json
// axun-uUpaWEdMEMU8C61K mcp服务id,自定义即可
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "详情见https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` 是一个开源的 npm 包，你可以在 [npm 官方仓库](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) 查看其详细信息和使用文档。`@mcpmarket`为Cherry Studio官方MCP服务集合
{% endhint %}

### **总结与展望**

随着各大 AI 客户端逐渐开始支持 MCP，相信 MCP 的应用范围会越来越广泛。Cherry Studio 作为一个积极拥抱前沿技术的开源项目，也在不断完善 MCP 相关功能。希望大家多多关注 Cherry Studio，一起见证 MCP 为 AI 带来的更多可能性！
