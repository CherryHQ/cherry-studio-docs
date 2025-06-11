# 自动安装 MCP

> 自动安装 MCP 需要将 Cherry Studio 升级至 v1.1.18 或更高版本。

## 功能简介

除了手动安装外，Cherry Studio 还内置了 `@mcpmarket/mcp-auto-install` 工具，这是一个更便捷的 MCP 服务器安装方式。你只需要在支持 MCP 服务的大模型对话中输入相应的指令即可。

{% hint style="warning" %}
**测试阶段提醒：**

* `@mcpmarket/mcp-auto-install` 目前仍处于测试阶段
* 效果依赖大模型的"智商"，有些会自动添加，有些还是**需要在 MCP 设置中再手动更改某些参数**
* 目前搜索源是从 @modelcontextprotocol 中进行搜索，可以自行配置(下方说明)
{% endhint %}

## 使用说明

例如，你可以输入：

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>输入指令安装 MCP 服务器</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP 服务器配置界面</p></figcaption></figure>

系统会自动识别你的需求，并通过 `@mcpmarket/mcp-auto-install` 完成安装。这个工具支持多种类型的 MCP 服务器，包括但不限于：

* filesystem（文件系统）
* fetch（网络请求）
* sqlite（数据库）
* 等等...

> MCP\_PACKAGE\_SCOPES 变量可以自定义 MCP 服务搜索源，默认值为：`@modelcontextprotocol`，可以自定义配置。

## `@mcpmarket/mcp-auto-install` 库的介绍

{% hint style="info" %}
**默认配置参考：**

```json
// `axun-uUpaWEdMEMU8C61K` 为服务id,自定义即可
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

`@mcpmarket/mcp-auto-install` 是一个开源的 npm 包，你可以在 [npm 官方仓库](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) 查看其详细信息和使用文档。`@mcpmarket` 为 Cherry Studi 官方 MCP 服务集合。
{% endhint %}
