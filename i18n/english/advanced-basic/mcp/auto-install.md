# Automatically Install MCP Servers

Cherry Studio's built-in `@cherry/mcp-auto-install` helps a model discover MCP servers, read configuration instructions, and generate startup commands. Use it as an installation assistant when you are unsure of a package name or configuration format.

{% hint style="warning" %}
This feature is still experimental. V2 currently runs the installation assistant in JSON mode, and it does not guarantee that generated server configurations will be written directly to Cherry Studio. Treat it as a discovery and configuration-generation tool, and review the results before importing them.
{% endhint %}

## Workflow

A complete assisted installation usually has four steps:

1. The model uses the installation assistant to search for available servers and read their configuration instructions.
2. The installation assistant returns suggested commands, arguments, and environment variables.
3. You review the package source and configuration, then import the JSON into Cherry Studio.
4. You enable the new server in MCP settings and inspect its tools and logs.

The installation assistant itself starts with this preset:

```text
npx -y @mcpmarket/mcp-auto-install connect --json
```

Cherry Studio manages the local registry path used by the assistant, so you do not need to enter `MCP_REGISTRY_PATH` manually.

## Enable the installation assistant

1. Open **Settings → MCP Servers**.
2. Search for `@cherry/mcp-auto-install` in the built-in servers.
3. Click **Install**, then enable it in the installed server list.
4. Add `@cherry/mcp-auto-install` in the tool settings of the target assistant or Agent.
5. Select a model that supports tool calls.

The first startup needs to run an NPX package. Cherry Studio uses NPX from your system when available and otherwise tries the built-in Bun runtime. If there is a dependency problem, run the dependency installer in MCP settings and restart the app.

## Generate a server configuration

You are more likely to get a usable result if you tell the model the purpose, runtime platform, and output format instead of simply saying “install an MCP server.” For example:

```text
Use the MCP auto-install tool to find an MCP server that can access a local SQLite database in read-only mode.
My system is macOS.

First explain the package source and required permissions, then generate a JSON configuration that I can import into Cherry Studio.
Do not enable the server for me or enter any real keys.
```

The installation assistant can:

- List MCP servers available in the registry;
- Read a server's README and configuration recommendations;
- Generate commands, arguments, and environment variables for a server;
- Manage the installation assistant's own local server registration data.

After the model returns a configuration, check at least the following:

- Whether the npm package name, publisher, and documentation URL are trustworthy;
- Whether `command` and `args` match the project's official instructions;
- Whether it contains download scripts, shell commands, or unnecessary high-privilege arguments;
- Whether the environment variable names are correct and still contain placeholder values;
- Which local files, network services, or accounts the server will access.

## Import into Cherry Studio

Ask the model to format the result as shown below, keeping only one server in each configuration:

```json
{
  "mcpServers": {
    "example-server": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"],
      "env": {
        "EXAMPLE_API_KEY": "Replace in Cherry Studio"
      }
    }
  }
}
```

Then:

1. Open **Settings → MCP Servers**.
2. Click **Add Server → Import from JSON**.
3. Paste the configuration you reviewed.
4. After importing it, open the server details, replace placeholder values, and save.
5. Enable the server and inspect the tools it actually exposes on the **Tools** page.
6. After testing, add the server to each assistant or Agent that needs it.

{% hint style="danger" %}
NPX can download and execute third-party code. Do not run an unfamiliar package solely because a model recommended it, and do not send API keys directly to the model. Verify the package, version, source code, or official documentation first, then enter the key in the server settings in Cherry Studio.
{% endhint %}

## Customize the search scope

By default, the installation assistant discovers servers from the `@modelcontextprotocol` npm scope. To search another scope, add this environment variable in the server details for `@cherry/mcp-auto-install`:

```text
MCP_PACKAGE_SCOPES=@modelcontextprotocol,@your-scope
```

Separate multiple scopes with commas. Expanding the search scope also increases the number of third-party packages, so apply stricter source-review standards.

## Troubleshooting

### The installation assistant is not called in a conversation

Make sure `@cherry/mcp-auto-install` is enabled and added to the current assistant or Agent, and use a model that supports tool calls. You can explicitly ask it to “call the MCP auto-install tool first.”

### NPX is not found or startup fails

Run the dependency installer in MCP settings, then restart Cherry Studio. If it still fails, open the server logs and check NPX, the built-in Bun runtime, network proxy, and npm registry.

### The target server cannot be found

The default search scope is limited. First identify the package's npm scope, then add it through `MCP_PACKAGE_SCOPES`. You can also skip automatic installation and [configure MCP manually](config.md) from the project's official documentation.

### A configuration was generated, but no server was added

This is expected in the current JSON mode. Copy the `mcpServers` JSON prepared by the model, then complete the installation through **Add Server → Import from JSON**.

### An imported server cannot be enabled

The installation assistant produces a suggested configuration, which may still be missing a path, key, or platform-specific argument. Correct the configuration according to the target server's official documentation, and see [MCP Server Troubleshooting](chang-jian-wen-ti.md) for help with the logs.

## Related documentation

- [`@mcpmarket/mcp-auto-install` package documentation](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install)
- [Configure and Use MCP](config.md)
- [Built-in MCP Servers](in-memory.md)
- [MCP Server Troubleshooting](chang-jian-wen-ti.md)
- [Feedback and Suggestions](../../question-contact/suggestions.md)
