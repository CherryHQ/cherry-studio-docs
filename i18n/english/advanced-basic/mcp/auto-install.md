
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Automatic Installation of MCP

> Automatic installation of MCP requires upgrading Cherry Studio to v1.1.18 or higher.

## Feature Introduction

In addition to manual installation, Cherry Studio has a built-in `@mcpmarket/mcp-auto-install` tool that provides a more convenient way to install MCP servers. You simply need to enter specific commands in conversations with large models that support MCP services.

{% hint style="warning" %}
**Beta Phase Reminder:**
* `@mcpmarket/mcp-auto-install` is currently in beta phase
* Effectiveness depends on the "intelligence" of the large model - some configurations are automatically added, while others **still require manual parameter adjustments in MCP settings**
* Current search sources are from @modelcontextprotocol, but this can be customized (explained below)
{% endhint %}

## Usage Instructions

For example, you can input:

```
Help me install a filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Installing MCP server via command input</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP server configuration interface</p></figcaption></figure>

The system will automatically recognize your requirements and complete the installation via `@mcpmarket/mcp-auto-install`. This tool supports various types of MCP servers, including but not limited to:

* filesystem (file system)
* fetch (network requests)
* sqlite (database)
* etc.

> The MCP_PACKAGE_SCOPES variable allows customization of MCP service search sources. Default value: `@modelcontextprotocol`.

## Introduction to the `@mcpmarket/mcp-auto-install` Library

{% hint style="info" %}
**Default Configuration Reference:**

```json
// `axun-uUpaWEdMEMU8C61K` is the service ID - customizable
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
    "MCP_REGISTRY_PATH": "Details at https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` is an open-source npm package. You can view its details and documentation in the [npm registry](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` is the official MCP service collection for Cherry Studio.
{% endhint %}