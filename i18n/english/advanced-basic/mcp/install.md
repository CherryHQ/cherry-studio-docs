# Install the MCP Environment

Cherry Studio can manage two commonly used MCP runtimes:

- **UV**: Runs Python MCP Servers started through `uv` or `uvx`;
- **Bun**: Runs JavaScript tools and serves as a fallback runtime for some NPX servers when NPX is not installed on the system.

{% hint style="info" %}
Not every MCP Server requires UV and Bun. Remote SSE / Streamable HTTP servers and most built-in Cherry Studio servers do not depend on these runtimes. Use the `command` in the server documentation to determine what you need to install.
{% endhint %}

## Use the in-app installer

1. Open **Settings → Environment Dependencies**.
2. Find **UV** or **Bun**.
3. Click **Install** for each item marked **Not Installed**.
4. Wait for the status to change to **Installed**.

The MCP Servers page also displays a warning entry point when an environment dependency is missing. Click it to open the same Environment Dependencies page.

The in-app installer downloads an executable for the current operating system and CPU architecture, then stores it in Cherry Studio's private directory:

{% tabs %}
{% tab title="Windows" %}
`C:\Users\<username>\.cherrystudio\bin`
{% endtab %}

{% tab title="macOS / Linux" %}
`~/.cherrystudio/bin`
{% endtab %}
{% endtabs %}

After installation, click the folder icon beside a dependency to open that directory.

## System commands and private runtimes

When running a STDIO server, Cherry Studio searches in this order:

### `uv` and `uvx`

1. It first looks for a system installation of `uv` or `uvx` in the login shell environment;
2. If none is found, it uses the UV installed by Cherry Studio in `~/.cherrystudio/bin`.

### `npx`

1. It first looks for a system installation of `npx` in the login shell environment;
2. If none is found, it tries to run the package with the Bun installed by Cherry Studio.

Therefore, UV, UVX, or NPX installed correctly in the system PATH can also be used. The **Installed** status on the **Environment Dependencies** page checks only Cherry Studio's private directory; it does not mean that a system command is unavailable.

{% hint style="warning" %}
If you just installed or changed Node.js, NPX, UV, or UVX on the system, completely quit and reopen Cherry Studio so the app can read the login shell environment again.
{% endhint %}

## Determine which runtime you need

Inspect the configuration provided by the MCP developer:

| Command in the configuration | Required environment |
| --- | --- |
| `uvx` or `uv` | UV |
| `npx` | NPX provided by Node.js, or Cherry Studio's Bun fallback |
| `bun` or `bunx` | Bun |
| `node` | System Node.js |
| Another command | Install the corresponding program according to the developer documentation |
| A remote URL only | Usually no local runtime |

The Environment Dependencies page in Cherry Studio does not install Node.js or arbitrary third-party system commands.

## Install manually as a fallback

If the in-app download fails, install the runtime on the system using its official documentation:

- [Official UV installation instructions](https://docs.astral.sh/uv/getting-started/installation/)
- [Official Bun installation instructions](https://bun.com/docs/installation)
- [Download Node.js](https://nodejs.org/en/download)

After installation, verify the commands in a system terminal:

```bash
uv --version
bun --version
npx --version
```

You only need to verify the command that the server actually uses. After verification succeeds, restart Cherry Studio and enable the MCP Server again.

Advanced users can also place an executable matching the current system and architecture in `~/.cherrystudio/bin`; on Windows, use the corresponding user directory. Do not download binaries from untrusted sources.

## Troubleshooting

### Installation fails after clicking Install

Check the following in order:

- Whether the current network can reach the runtime download source;
- Whether a proxy, firewall, or security application blocks Cherry Studio;
- Whether the user directory is writable;
- Whether an installation package exists for the operating system and CPU architecture;
- Whether enough disk space is available.

### A server still reports that the command is missing after installation

Make sure **Command** in the server details is spelled correctly. For example, do not enter a complete argument string in place of `uvx`. Enter each argument on a separate line in **Arguments**.

If you use a system-installed command, verify it in a terminal and restart Cherry Studio. If you use an in-app runtime, open the dependency directory and confirm that the corresponding executable exists.

### UV and Bun are installed, but the server still does not start

A runtime starts the program; it cannot fix invalid arguments, a missing API key, or a failure in the server itself. Open the logs in the MCP Server details and see [MCP Server Troubleshooting](chang-jian-wen-ti.md).

## Related documentation

- [MCP Tutorial](README.md)
- [Configure and Use MCP](config.md)
- [MCP Server Troubleshooting](chang-jian-wen-ti.md)
- [Feedback and Suggestions](../../question-contact/suggestions.md)
