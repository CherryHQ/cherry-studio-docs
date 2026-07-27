---
icon: monero
---

# MCP Tutorial

MCP (Model Context Protocol) is a standard protocol that lets models use external tools and data. After connecting an MCP Server, an assistant or Agent in Cherry Studio can read web pages, query databases, work with files, call business APIs, or use prompts and resources provided by the server while preparing a response.

## How MCP works

A typical call involves these roles:

| Role | Responsibility |
| --- | --- |
| Model | Determines whether a tool is needed and generates its arguments |
| Cherry Studio | Connects to the MCP Server, checks permissions, and displays the call process |
| MCP Server | Provides tools, prompts, or resources and performs the actual operation |

The general flow is:

1. You give an assistant or Agent a task;
2. The model selects a tool from the tools it is authorized to use;
3. Cherry Studio determines whether you must confirm the call based on server and tool permissions;
4. The MCP Server performs the operation and returns a result;
5. The model uses the result to continue its response.

The model does not directly “sign in to your computer or account.” It works through interfaces provided by the MCP Server. However, an MCP Server may be a local executable or a remote service, so you must still review its source and permissions.

## Common uses

- Reading and searching local files;
- Fetching web pages, controlling a browser, or calling network endpoints;
- Querying knowledge bases, databases, and team documentation;
- Running Python or other code;
- Connecting online services for notes, messages, project management, and more;
- Performing write, delete, or business operations after explicit authorization.

Actual capabilities depend on the tools provided by the server. MCP Servers of the same type may also differ in permissions, data handling, and quality.

## What an MCP Server can provide

MCP is not limited to tools:

- **Tools**: Operations that the model can call, such as search, read, and write;
- **Prompts**: Reusable prompt templates provided by the server;
- **Resources**: Files, documents, or other context resources provided by the server.

After enabling a server, open its details to see which capabilities it actually provides. If it does not provide a capability type, the corresponding tab may be empty or hidden.

## MCP compared with Skills

| Comparison | Skills | MCP |
| --- | --- | --- |
| Core purpose | Tell an Agent how to complete a type of task | Let a model call external tools or data |
| Main content | Instructions, workflows, and optional resources | Tools, prompts, resources, and connection protocols |
| External operations | Depends on the tools called by the Skill | Usually connects to a local program or remote service |
| Where it is used in V2 | Primarily with Agents | With regular assistants and Agents |

A Skill can tell an Agent when and how to use MCP; MCP performs the actual tool calls. The two can work together. See [Skills](../../pre-basic/settings/skills.md) for details.

## Use MCP in Cherry Studio

The complete workflow is:

1. Install or add a server under **Settings → MCP Servers**;
2. Enter its command, URL, arguments, headers, or environment variables;
3. Enable the server and inspect its tools and logs;
4. Add the server to a regular assistant or Agent;
5. Start a task with a model that supports tool calls.

{% hint style="info" %}
Only STDIO servers started with local commands such as `uv`, `uvx`, `npx`, or `bun` may require an additional runtime. Remote servers and most built-in servers do not require UV or Bun to be installed first.
{% endhint %}

See [Configure and Use MCP](config.md) for detailed steps.

## Where to find servers

MCP settings in Cherry Studio provide several entry points:

- **Built-in Servers**: Common servers already adapted for Cherry Studio;
- **MCP Marketplaces**: Browse servers from integrated marketplaces;
- **Providers**: Connect to supported MCP service providers;
- **Import from JSON or DXT**: Use a configuration or extension package supplied by a developer;
- **Create Manually**: Enter a STDIO, SSE, or Streamable HTTP configuration from the official documentation.

For your first server, start with the [Built-in MCP Servers](in-memory.md). Their configuration paths are clearer and their permissions are easier to verify.

## Security boundaries

{% hint style="danger" %}
MCP tool declarations are not a security sandbox. A STDIO Server runs with the current user's permissions, so a malicious or compromised server may access any data available to its process. A remote Server also receives the content that you send to its tools.
{% endhint %}

Before installing or enabling a server:

- Verify the developer, package, download location, and update history;
- Authorize only the directories, accounts, and API scopes required for the task;
- Do not put real keys in prompts or shared JSON;
- Disable unnecessary tools on the **Tools** page;
- Keep manual confirmation for actions such as writing files, deleting data, sending messages, or creating orders;
- Disable or uninstall the server when you no longer use it.

Automatic approval reduces only the number of confirmation steps; it does not reduce the tool's permissions. Do not enable automatic approval in bulk for an unfamiliar server.

## Choose the next step

| Your situation | Recommended reading |
| --- | --- |
| You are not sure whether a local runtime is required | [Install the MCP Environment](install.md) |
| You are ready to add your first server | [Configure and Use MCP](config.md) |
| You want to use tools already adapted for Cherry Studio | [Built-in MCP Servers](in-memory.md) |
| You want the model to help find a server and generate its configuration | [Automatically Install MCP Servers](auto-install.md) |
| You need to connect a Dify knowledge base | [Connect a Dify Knowledge Base](dify.md) |
| You encounter a startup, connection, or call error | [MCP Server Troubleshooting](chang-jian-wen-ti.md) |

## Get help

If logs do not identify the problem, use [Feedback and Suggestions](../../question-contact/suggestions.md) to submit the Cherry Studio version, operating system, server type, and redacted error details.
