
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Automatic MCP Installation

> Automatic MCP installation requires upgrading Cherry Studio to v1.1.18 or a higher version.

## Feature Introduction

In addition to manual installation, Cherry Studio has a built-in tool, `@mcpmarket/mcp-auto-install`, which provides a more convenient way to install MCP servers. You just need to input the corresponding command in a large model conversation that supports MCP services.

{% hint style="warning" %}
**Beta Phase Reminder:**

*   `@mcpmarket/mcp-auto-install` is still in its beta phase.
*   The effectiveness depends on the "intelligence" of the large model. Some configurations will be added automatically, while others may still **require manual changes to certain parameters in the MCP settings**.
*   Currently, the search source is `@modelcontextprotocol`, which you can configure yourself (explained below).
{% endhint %}

## Usage Instructions

For example, you can enter:

```
Install a filesystem mcp server for me
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Enter the command to install the MCP server</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP server configuration interface</p></figcaption></figure>

The system will automatically recognize your request and complete the installation via `@mcpmarket/mcp-auto-install`. This tool supports various types of MCP servers, including but not limited to:

*   filesystem
*   fetch
*   sqlite
*   and more...

> The `MCP_PACKAGE_SCOPES` variable allows you to customize the MCP service search source. The default value is: `@modelcontextprotocol`, which can be configured.

## Introduction to the `@mcpmarket/mcp-auto-install` Library

{% hint style="info" %}
**Default Configuration Reference:**

```json
// `axun-uUpaWEdMEMU8C61K` is the service ID, which can be customized
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
    "MCP_REGISTRY_PATH": "For details, see https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` is an open-source npm package. You can view its detailed information and documentation on the [official npm repository](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` is the official collection of MCP services for Cherry Studio.
{% endhint %}