---
icon: hexagon-exclamation
---

# MCP FAQ

This page helps you troubleshoot MCP Servers that fail to start, connect without showing tools, time out during calls, or report invalid parameters. If this is your first MCP configuration, read [Configure and Use MCP](config.md) first. If the required runtimes are missing, complete [Install the MCP Environment](install.md) before continuing.

## Identify the connection type first

Open `Settings → MCP Servers`, select the affected server, and make sure its type matches the required configuration:

| Type | Required configuration | Common problems |
|---|---|---|
| `stdio` | Command and Arguments; Environment Variables as needed | Command not found, arguments split incorrectly, dependencies not installed |
| `SSE` | Server URL; Headers as needed | Incorrect URL path, service not running, authentication failed |
| `Streamable HTTP` | Server URL; Headers as needed | An SSE address entered as `/mcp`, or the reverse |
| Built-in | Configure as described on the server's page | Missing authorization, directory, or search key |

Cherry Studio starts a local child process for `stdio`. SSE and Streamable HTTP connect to an already running local or remote service. The troubleshooting methods differ, so do not repeatedly retry after changing only the URL or Command.

## View real-time logs

Open the server details and click **View Logs** beside the title. The logs show:

* `stdout` / `stderr`: Output from local commands;
* `info` / `warn` / `error`: Connection, initialization, and call status;
* Recent startup arguments, connection errors, or tool responses.

For easier diagnosis, disable the server first, open the logs, and then enable it again. The page retains only the most recent entries from the current session, so copy the necessary information promptly after reproducing the issue.

{% hint style="warning" %}
Logs may contain command arguments, file paths, request URLs, or tool responses. Before submitting feedback, redact tokens, API keys, cookies, personal directories, and business data.
{% endhint %}

## The server cannot be enabled

### `npx`, `uvx`, or another command is not found

Cherry Studio reads environment variables from the login shell to locate commands. For `npx`, the app also tries its built-in Bun runtime. For `uv` / `uvx`, it tries an installed built-in version.

If you still see `not found`:

1. Open `Settings → MCP Servers → Environment Installation`.
2. Install the Node.js or `uv` runtime required by the server.
3. Completely quit and reopen Cherry Studio so that the new PATH takes effect.
4. Return to the server details and enable it again.

You can also verify the commands in a terminal:

```bash
node --version
npx --version
uvx --version
```

You only need to verify the command used by that server; you do not need to install every runtime.

### Command and Arguments are configured incorrectly

In Cherry Studio:

* Enter only the executable command in **Command**, such as `npx`, `uvx`, or the absolute path to an executable;
* Enter one independent argument per line in **Arguments**;
* Do not paste the entire command into the Command field;
* Enter a file path containing spaces as one complete argument. Do not add shell quotes unless the server documentation explicitly requires them.

For example, for this JSON:

```json
{
  "command": "npx",
  "args": ["-y", "@example/mcp-server", "--mode", "read-only"]
}
```

Enter the following in the form:

```text
Command
npx

Arguments
-y
@example/mcp-server
--mode
read-only
```

### JSON import fails

When adding a server from JSON, the top level must contain `mcpServers`, and you can import only one server at a time:

```json
{
  "mcpServers": {
    "example": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"]
    }
  }
}
```

Common causes include:

* Curly quotation marks or trailing commas;
* An `args` value that is not an array of strings;
* Multiple servers in the same JSON;
* Combining `url`, `command`, and a type into an incompatible configuration;
* Markdown code fences included in the copied content.

## A remote server cannot connect

### The URL and protocol do not match

Check the server's official documentation to confirm whether it uses SSE or Streamable HTTP:

* A common SSE address looks like `http://localhost:3000/sse`;
* A common Streamable HTTP address looks like `http://localhost:3000/mcp`.

The server determines its own path; `/sse` and `/mcp` are only common patterns. First confirm in a terminal or browser that the service is actually listening at that address, then select the matching type.

If the server runs in Docker, a virtual machine, or another device, `127.0.0.1` refers to the system running Cherry Studio and may not be the server's host.

### A request returns 401 or 403

In **Headers**, enter authentication details with one `Name=Value` pair per line. For example:

```text
Authorization=Bearer YOUR_TOKEN
```

Do not put a real token in a configuration that may be shared publicly. Save after changing Headers. If the server is enabled, it attempts to reconnect with the new configuration and automatically returns to the disabled state if the connection fails.

## The server is connected, but no tools appear

Check the following in order:

1. The server is enabled in `Settings → MCP Servers`.
2. The **Tools** tab in the server details lists the expected tools.
3. The relevant tools have not been disabled individually.
4. The current assistant or Agent has this MCP Server enabled.
5. Start a new conversation so the updated tool configuration enters the context.

“Server connected” means only that protocol initialization succeeded. It does not automatically give every assistant access to the server's tools.

If the tool list is empty even though the server's documentation says it provides tools, check the logs for `listTools`, protocol-version, or initialization errors.

## Tool calls time out

The default tool-call timeout in Cherry Studio is 60 seconds. You can increase the number of seconds with **Timeout** in the server details. When long-running task support is enabled, progress events from the server can extend the wait, but the total time is still limited.

Connection initialization uses a more generous timeout. Downloading dependencies for the first time or starting a remote server can take several minutes. Distinguish between:

* **Timeout while enabling**: Usually an installation, network, URL, or initialization problem;
* **Timeout during tool execution**: Usually the server task itself is too slow or does not send progress.

Do not increase Timeout without limit. First confirm in the logs that the request is progressing, and check whether the server supports MCP Progress.

## Environment variables do not take effect

Enter server environment variables with one `KEY=VALUE` pair per line. Cherry Studio merges them with the login shell environment and passes them to the `stdio` child process.

Check:

* The key exactly matches the server documentation;
* The value does not contain unintended quotation marks or leading or trailing spaces;
* You saved the change and reconnected;
* The token has not expired;
* The server actually reads an environment variable instead of expecting a Header or configuration file.

For remote SSE / Streamable HTTP servers, authentication usually belongs in Headers rather than local process environment variables.

## The `mcp-server-time` time zone is incorrect

The official Time Server is a Python server and usually starts through `uvx`. To specify the local time zone, enter it as a separate argument:

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": [
        "mcp-server-time",
        "--local-timezone=Asia/Shanghai"
      ]
    }
  }
}
```

Use an IANA time zone name such as `Asia/Shanghai`, `Europe/Berlin`, or `America/New_York`, rather than an offset abbreviation such as `UTC+8`.

If you see `uvx not found`, install the Python environment for MCP and restart Cherry Studio. The Time Server's installation method or arguments may change between versions; refer to the [official MCP Servers repository](https://github.com/modelcontextprotocol/servers/tree/main/src/time) for the latest information.

## Create a minimal reproduction

If the issue persists:

1. Create a server configuration containing only the required fields.
2. Temporarily remove proxies, custom registries, and nonessential environment variables.
3. Enable only this MCP Server in a blank assistant.
4. Call the simplest tool available that has no side effects.
5. Save the error dialog and the relevant time range from **View Logs**.

When submitting feedback, include your Cherry Studio version, operating system, server type, redacted configuration, and redacted logs. Do not include real credentials. See [Feedback and Suggestions](../../question-contact/suggestions.md) for official support channels.
