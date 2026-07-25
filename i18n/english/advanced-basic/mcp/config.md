# Configure and Use MCP

Using MCP in Cherry Studio involves two steps:

1. Add an MCP Server under **Settings → MCP Servers**, then configure its connection and permissions;
2. Add each enabled server to the assistant or Agent that needs to use it.

If you are not familiar with MCP yet, read the [MCP Tutorial](README.md) first. If NPX, Bun, or UV is missing from your system, complete [MCP Environment Installation](install.md) before continuing.

## Choose how to add a server

Open **Settings → MCP Servers**, click **Add Server**, and choose:

| Method | When to use it |
| --- | --- |
| New | Enter a STDIO, SSE, or Streamable HTTP configuration manually |
| Import from JSON | The developer provided `mcpServers` JSON |
| Import from DXT | You have a `.dxt` extension package |
| Built-in Servers | Use a common tool already adapted for Cherry Studio |

For common requirements, check the [Built-in MCP Servers](in-memory.md) first. A built-in version does not require you to find the command manually and makes permissions easier to control.

## Connection types

### STDIO

Cherry Studio starts a STDIO server locally. You usually need to enter:

| Field | Description |
| --- | --- |
| Name | Identifies the server and can be customized |
| Type | `STDIO` |
| Command | An executable such as `npx`, `uvx`, or `node` |
| Arguments | One argument per line, in the same order as the developer documentation |
| Environment Variables | One `KEY=value` pair per line |

When a command contains NPX, Bun, UV, or UVX, the page displays optional package registry settings. You do not need to change them unless the default registry is unavailable.

The following minimal configuration uses the official Time Server:

| Field | Value |
| --- | --- |
| Name | `time` |
| Type | `STDIO` |
| Command | `uvx` |
| Arguments | Enter `mcp-server-time` on the first line and `--local-timezone=Asia/Shanghai` on the second |

You can also omit the time-zone argument and let the model pass a time zone explicitly when it calls the tool.

### SSE

Use this type to connect to a remote MCP Server that uses Server-Sent Events. After selecting `SSE`, enter the server URL. For example:

```text
https://example.com/sse
```

If the service requires authentication, enter one `KEY=value` pair per line under **Headers**:

```text
Authorization=Bearer your-token
```

### Streamable HTTP

Use this type to connect to a newer Streamable HTTP MCP Server. Its configuration is similar to SSE, but the URL often ends in `/mcp`:

```text
https://example.com/mcp
```

The protocol type must match the server. Do not assume that a URL supports both SSE and Streamable HTTP simply because it opens in a browser.

{% hint style="warning" %}
A remote server's headers may contain account tokens. Enter keys only in the server settings, not in prompts, screenshots, or shared configurations.
{% endhint %}

## Import from JSON

Cherry Studio imports one server at a time. A common format is:

```json
{
  "mcpServers": {
    "example-server": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"],
      "env": {
        "EXAMPLE_API_KEY": "Replace after importing"
      }
    }
  }
}
```

A remote server can use `type`, `url`, and `headers`:

```json
{
  "mcpServers": {
    "remote-example": {
      "type": "streamableHttp",
      "url": "https://example.com/mcp",
      "headers": {
        "Authorization": "Bearer your-token"
      }
    }
  }
}
```

Imported servers are disabled by default. Before connecting, open the server details and inspect the command, arguments, URL, headers, and environment variables.

## Import from DXT

DXT is an extension package containing a server manifest and resources. After you select a `.dxt` file, Cherry Studio reads its startup configuration and creates the server.

DXT is still an executable extension. Install files only from sources you trust, then inspect the provider, command, arguments, and required permissions after importing.

## Inspect the server details

Click an installed server to open its details. After saving the configuration and enabling the server, you can inspect:

- **Settings**: Connection type, command, arguments, environment variables, headers, timeout, and advanced information;
- **Tools**: Tools provided by the server, parameter schemas, enabled status, and automatic approval;
- **Prompts**: MCP Prompts provided by the server;
- **Resources**: MCP Resources provided by the server;
- **Logs**: The connection process and STDIO error output.

Not every server provides prompts or resources. These tabs appear only after the server is enabled.

### Timeout and long-running tasks

The default timeout for a regular tool call is 60 seconds. Enable **Long Running Mode** or increase the timeout only when the server genuinely needs more time. Timeout settings cannot fix an incorrect command, invalid key, or inaccessible URL.

### Tool permissions

On the **Tools** page, you can disable individual tools and control automatic approval. Recommended settings:

- Enable query and read-only tools as needed;
- Keep manual confirmation for operations such as writing files, deleting data, sending messages, or creating orders;
- Disable tools you do not use to reduce the scope for accidental model calls.

## Use MCP with a regular assistant

Open the **MCP** page in Assistant Settings, or use the MCP shortcut panel in the input box. You can choose among three modes:

| Mode | Behavior |
| --- | --- |
| Disabled | The current assistant does not use MCP |
| Auto | Discover and call tools from all enabled MCP Servers through the built-in Hub |
| Manual | Use only the enabled servers selected for the current assistant |

Use **Manual** mode for permission-sensitive work. Auto mode is useful when you have many tools and want the model to discover capabilities, but you should still restrict high-risk operations on the **Tools** page of each server.

After selecting a mode, use a model that supports tool calls and give it a specific task. For example:

```text
Use the time tool to find the current time in Tokyo and give the time difference from Shanghai.
```

Whether the model calls a tool depends on the model's capabilities, the question, and the prompt. When retrieval is required, explicitly describe the purpose of the server or tool.

## Use MCP with an Agent

1. Open the edit or settings page for the target Agent.
2. Go to **Tools → MCP**.
3. Add the required servers.
4. Save the Agent.

Only enabled MCP Servers can be selected. After a server is disabled, it does not provide tools even if it remains in the Agent configuration.

## Verify the connection

Check the following in order:

1. The server shows as enabled in the server list;
2. The **Tools** page in the server details lists its tools;
3. The target assistant or Agent has the server added;
4. The selected model supports tool calls;
5. Send a narrowly scoped test question with an easily verified result;
6. Expand the tool-call record in the response and confirm that the arguments and result are correct.

If a server does not start, connects without showing tools, or times out during a call, see [MCP Server Troubleshooting](chang-jian-wen-ti.md).

## Related documentation

- [MCP Tutorial](README.md)
- [MCP Environment Installation](install.md)
- [Built-in MCP Servers](in-memory.md)
- [Automatically Install MCP Servers](auto-install.md)
- [Feedback and Suggestions](../../question-contact/suggestions.md)
