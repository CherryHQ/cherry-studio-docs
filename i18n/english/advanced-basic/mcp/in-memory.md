# Built-in MCP Servers

Cherry Studio provides a collection of built-in MCP servers that you can install directly. They run inside the app or use preset connections, so you do not need to write JSON configurations manually. Use them to quickly add web access, file operations, code execution, memory, third-party services, and other capabilities to assistants and Agents.

{% hint style="info" %}
“Built-in” does not mean that every server is automatically enabled. You must first install a server from the built-in list. Servers marked **Requires Configuration** also require arguments or environment variables.
{% endhint %}

## Install and use a server

1. Open **Settings → MCP Servers**.
2. Find the server you need under **Builtin Servers**, or switch to the **Installable** filter.
3. Click **Install**.
4. If the server shows **Requires Configuration**, return to the installed server list, select the server, and enter the arguments described on this page.
5. Save and enable the server.
6. Add the MCP server in the tool settings of the target assistant or Agent.

You must also use a model that supports tool calls. If you install a server without adding it to the current assistant or Agent, the model cannot use its tools.

## Currently available built-in servers

| Server | Primary use | Additional preparation |
| --- | --- | --- |
| `@cherry/fetch` | Read a URL as HTML, Markdown, plain text, or JSON | None |
| `@cherry/browser` | Open and interact with dynamic web pages, manage tabs, and take screenshots | None |
| `@cherry/filesystem` | Find, read, edit, and delete files within an allowed directory | Configure the directory that the server may access |
| `@cherry/python` | Run Python code in a Pyodide environment | None |
| `@cherry/brave-search` | Brave web search and local place search | `BRAVE_API_KEY` |
| `@cherry/memory` | Store memory across conversations in a local knowledge graph | `MEMORY_FILE_PATH` |
| `@cherry/sequentialthinking` | Provide step-by-step, revision, and branching tools for complex tasks | None |
| `@cherry/dify-knowledge` | Query Dify knowledge bases | API URL and `DIFY_KEY` |
| `@cherry/flomo` | Write notes and ideas to flomo | flomo account authorization |
| `@cherry/didi-mcp` | Search for places, estimate prices, and manage ride-hailing orders | `DIDI_API_KEY`; supported only in mainland China |
| `@cherry/nowledge-mem` | Connect to Nowledge Mem running locally | Install and run Nowledge Mem |
| `@cherry/mcp-auto-install` | Let the model search for and install other MCP servers | Experimental; requires NPX or the built-in Bun runtime |

## Web and code tools

### `@cherry/fetch`

Use this server to read web pages or endpoints that do not require complex interactions. It can return HTML, Markdown, plain text, or JSON and supports custom headers in requests.

If a page requires a signed-in session, JavaScript rendering, or click interactions, use `@cherry/browser` instead.

### `@cherry/browser`

Operates web pages through an Electron browser window managed by Cherry Studio. It can:

- Open URLs and run page scripts;
- Capture a page snapshot or screenshot;
- List, switch, and close tabs;
- Reset the browsing session.

The browser can access page content and any signed-in session that may be present. Before use, check the sites that the model intends to access, and do not let untrusted prompts perform sensitive account operations.

### `@cherry/python`

Provides the `python_execute` tool for running Python 3.12 code in a Pyodide environment. It is suitable for data calculations, text processing, and format conversion, and it can declare dependencies through PEP 723 metadata.

Each call has a default timeout of 60 seconds. This is not a complete local Python environment, so code that depends on native binaries, system commands, or specific hardware may not run.

### `@cherry/sequentialthinking`

Provides the model with step-by-step thinking tools that support revisions and branches. It is suitable for complex planning and analysis, but it does not automatically improve every response; simple questions usually do not need it.

## Local files and memory

### `@cherry/filesystem`

Provides the `glob`, `ls`, `grep`, `read`, `edit`, `write`, and `delete` tools. The server should access only the working directory that you explicitly authorize.

After installation, configure the directory in the server details by using either method:

- **Arguments**: Enter the absolute path to the working directory on the first line;
- **Environment Variables**: Enter `WORKSPACE_ROOT=absolute path`.

If both are present, `WORKSPACE_ROOT` takes precedence. `~` can expand to the user directory, but entering the complete absolute path reduces ambiguity.

{% hint style="warning" %}
By default, `write`, `edit`, and `delete` are not automatically approved. Do not broaden the authorized directory or approve unfamiliar write or delete operations merely to avoid confirmation prompts.
{% endhint %}

### `@cherry/memory`

Stores entities, relationships, and observations in a local JSON file so that the model can read and update them across conversations. Configure the following after installation:

```text
MEMORY_FILE_PATH=/absolute/path/memory.json
```

This is the MCP server's own knowledge-graph memory and is separate from Cherry Studio's [Global Memory](../memory.md). Most users can start with Global Memory and enable this server only when they need direct control over entities and relationships.

### `@cherry/nowledge-mem`

Connects to `http://127.0.0.1:14242/mcp` on the local computer. Install and run [Nowledge Mem](https://mem.nowledge.co/) before use; you do not need to enter a remote URL in Cherry Studio.

## Search, knowledge bases, and third-party services

### `@cherry/brave-search`

Provides web search and local place search. First obtain a key from the [Brave Search API](https://brave.com/search/api/), then enter the following in the server details:

```text
BRAVE_API_KEY=YOUR_API_KEY
```

### `@cherry/dify-knowledge`

Lists and retrieves Dify knowledge bases. Enter the knowledge-base API base URL in **Arguments** and `DIFY_KEY` in **Environment Variables**. See [Connect a Dify Knowledge Base](dify.md) for complete instructions.

### `@cherry/flomo`

Connects an account through flomo's remote MCP URL. After installation and activation, follow the authorization page to authorize your flomo account if it appears. Do not paste your flomo password into Cherry Studio's arguments or environment variables.

### `@cherry/didi-mcp`

Provides tools for place search, price estimation, creating or canceling ride-hailing orders, checking orders, and viewing driver locations. Enter the following after installation:

```text
DIDI_API_KEY=YOUR_API_KEY
```

The service is supported only in mainland China. Creating or canceling an order performs a real external action, so disable automatic approval for these tools on the **Tools** page.

### `@cherry/mcp-auto-install`

Allows the model to search for and install other MCP servers in a conversation. This feature is currently experimental. The preset starts through NPX. If startup fails, check and install the runtime dependencies in MCP settings first. See [Automatically Install MCP Servers](auto-install.md) for details.

## Permission recommendations

Built-in servers use the same MCP permission settings. After installation:

- Enable only the servers and tools required for the current task;
- Give file, browser, memory, and third-party account tools only the access they need;
- Keep manual confirmation for operations such as writing or deleting files and creating or canceling orders;
- Disable or uninstall servers that you no longer use;
- Store API keys only in the server configuration, not in prompts, screenshots, or shared records.

## Troubleshooting

### The server is installed, but its tools do not appear in a conversation

Make sure the server is enabled and added to the current assistant or Agent. Then check whether the selected model supports tool calls.

### The server shows “Requires Configuration”

After installation, select the server in the installed server list. On the **Settings** page, enter the arguments or environment variables and save. Enter one item per line in both fields.

### The server cannot be enabled

Open the logs in the server details and check for missing arguments, an invalid API key, directory permissions, or local dependencies. See [MCP Server Troubleshooting](chang-jian-wen-ti.md) for more guidance.

## Related documentation

- [Configure and Use MCP](config.md)
- [Automatically Install MCP Servers](auto-install.md)
- [MCP Server Troubleshooting](chang-jian-wen-ti.md)
- [Feedback and Suggestions](../../question-contact/suggestions.md)
