---
description: Explore the main features and workflows in Cherry Studio V2
icon: box-check
---

# Feature overview

Cherry Studio V2 brings multi-model chat, agents, content creation, knowledge management, and automation tools into one desktop workspace. This page helps you choose the right module for a task. Follow the links to each feature's guide for detailed instructions.

## Find a feature

Cherry Studio provides three common entry points:

* **Launchpad**: Opens application modules and pinned mini apps from one place.
* **Left sidebar**: Keeps frequently used modules within reach. You can choose which icons appear in Settings.
* **Top tab bar**: Creates a tab whenever you open a feature or item, making it easy to switch between tasks.

If you are unfamiliar with the interface, start with [Launchpad](launchpad.md).

## Choose a module by goal

| What you want to do | Module | Main capabilities |
| --- | --- | --- |
| Ask models everyday questions | [Chat](chat.md) | Assistants, topics, attachments, knowledge bases, tool calls, and multi-model responses |
| Reuse role or prompt configurations | [Assistant Library](agents.md) | Browse, add, and create chat assistants |
| Let AI read files and carry out ongoing tasks | [Agents](../../advanced-basic/agent.md) | Workspaces, permission modes, skills, tools, and multi-turn task execution |
| Manage models, assistants, agents, and other configurations | [Resource Library](library.md) | Browse by category, search, edit, and reuse resources |
| Generate or edit images | [Painting](drawing.md) | Select an image model, enter prompts, and manage generated results |
| Translate quickly between two languages | [Translate](translation.md) | Choose the source language, target language, and translation model |
| Use a provider's web application | [Mini Apps](app.md) | Open and pin web apps in Cherry Studio tabs |
| Answer questions with your own material | [Knowledge Base](knowledge-base.md) | Import, vectorize, retrieve, and reference material in chats |
| Find attachments previously used by the app | [Files](files.md) | Browse or clean up files by document, image, and text categories |
| Capture and organize Markdown content | [Notes](notes.md) | Folders, search, editing, reading, and export |
| Ask questions quickly from another application | [Quick Assistant](kuai-jie-zhu-shou.md) | Open a lightweight chat window with a global shortcut |
| Process selected text immediately | [Selection Assistant](selection-assistant.md) | Run predefined actions after selecting text in another application |
| Use coding tools such as Claude Code and Codex | [Code Tools](../../advanced-basic/code-tools-shi-yong-jiao-cheng.md) | Manage CLIs, providers, and project sessions |
| Run a personal AI assistant gateway | [OpenClaw](../../advanced-basic/openclaw.md) | Configure the gateway, models, and external channels |

## Chat assistants vs. agents

Both modules use models, but they are designed for different types of work:

| | Chat assistant | Agent |
| --- | --- | --- |
| Best for | Questions, writing, analysis, and conversations with a fixed role | Tasks that need to read or write files, call tools, or continue across multiple steps |
| Core configuration | Prompt, model, knowledge base, and MCP | Workspace, permissions, skills, tools, and maximum turns |
| Execution style | Primarily message exchanges | Plans and executes multiple steps toward a goal |
| Risk controls | Mainly controls what is sent to the model | Also controls file and command permissions |

Use a chat assistant when you only need to discuss or generate content. Use an agent when a task must access a local workspace or perform actions.

## Common workflows

### First-time setup

1. Add a provider and model under [Model Services](../../pre-basic/providers/).
2. Open [Chat](chat.md) and send a test message.
3. Add frequently used assistants from the [Assistant Library](agents.md).
4. Configure backups under [Data Settings](../../data-settings/).

### Ask questions about your own material

1. Create a knowledge base under [Knowledge Base](knowledge-base.md).
2. Import files, URLs, or another supported data source.
3. Wait for the material to finish processing.
4. Select the knowledge base in a chat, then ask your question.

### Carry out a project task

1. Create an agent in the [Resource Library](library.md).
2. Choose a model, permission mode, skills, and tools.
3. Open the agent and confirm its workspace.
4. Start with a clear goal, then review permission requests and file changes while it runs.

### Use AI at any time

* Use [Quick Assistant](kuai-jie-zhu-shou.md) to ask a question without switching away from the current app.
* Use [Selection Assistant](selection-assistant.md) to translate, summarize, or rewrite selected text.

## Automation and external access

When the core features do not cover your workflow, use:

* [MCP](../../advanced-basic/mcp/): Connect external tools and data to chat assistants.
* [API Server](../../advanced-basic/api-server.md): Call local Cherry Studio capabilities through a compatible API. It is also part of the V2 agent execution path.
* [Channels](../../advanced-basic/agent-channels.md): Connect agents to supported messaging channels.
* [Scheduled Tasks](../../advanced-basic/scheduled-tasks.md): Start agent sessions on a schedule.

{% hint style="info" %}
Set up model services and data backups before enabling agents, MCP, channels, or scheduled tasks. When a workflow writes files, runs commands, or sends data externally, use the minimum permissions required for that task.
{% endhint %}

## Next steps

If you have just installed Cherry Studio, read these guides in order:

1. [Launchpad](launchpad.md)
2. [Chat interface](chat.md)
3. [Assistant Library](agents.md)
4. [Agents](../../advanced-basic/agent.md)

If you encounter a problem, submit your Cherry Studio version, operating system, reproduction steps, and error details through [Feedback and suggestions](../../question-contact/suggestions.md).
