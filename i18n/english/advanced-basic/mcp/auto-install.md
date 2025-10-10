# Automatic MCP Installation


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="warning" %}
Automatic MCP installation requires Cherry Studio to be upgraded to v1.1.18 or higher.
{% endhint %}

## Feature Overview

In addition to manual installation, Cherry Studio also comes with the built-in `@mcpmarket/mcp-auto-install` tool, which provides a more convenient way to install MCP servers. You simply need to enter the corresponding commands in a large model conversation that supports MCP services.

{% hint style="warning" %}
**Testing Phase Reminder:**

*   `@mcpmarket/mcp-auto-install` is currently still in the testing phase.
*   The effectiveness depends on the "intelligence" of the large model; some parameters will be added automatically, while others still **need to be manually changed in the MCP settings**.
*   Currently, the search source is from @modelcontextprotocol, which can be configured by yourself (explained below).
{% endhint %}

## Usage Instructions

For example, you can enter:

```
Install a filesystem mcp server for me
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Enter command to install MCP server</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP Server Configuration Interface</p></figcaption></figure>

The system will automatically recognize your needs and complete the installation using `@mcpmarket/mcp-auto-install`. This tool supports various types of MCP servers, including but not limited to:

*   filesystem
*   fetch
*   sqlite
*   etc.

> The MCP_PACKAGE_SCOPES variable allows you to customize the MCP service search source. The default value is `@modelcontextprotocol`, which can be configured as needed.

## Introduction to the `@mcpmarket/mcp-auto-install` Library

{% hint style="info" %}
**Default Configuration Reference:**

```json
// `axun-uUpaWEdMEMU8C61K` is the service ID, which can be customized.
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
    "MCP_REGISTRY_PATH": "See https://www.npmjs.com/package/@mcpmarket/mcp-auto-install for details"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` is an open-source npm package. You can view its detailed information and usage documentation on the [official npm repository](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` is the official MCP service collection for Cherry Studio.
{% endhint %}