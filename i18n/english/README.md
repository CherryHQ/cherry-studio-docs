---
icon: cherries
---

# Cherry Studio Community Edition

Cherry Studio is an open-source desktop AI client for using cloud or local large language models from one application on Windows, macOS, and Linux. Beyond multi-model conversations, it brings Assistants, Agents, knowledge bases, Skills, MCP, translation, image generation, files, notes, and other capabilities into a single workspace.

Community Edition is designed for individual users and developers who want to choose their own model services, manage work data locally, and extend AI workflows as needed.

## What you can do

| Need | Capability in Cherry Studio |
| :--- | :--- |
| Use models from different providers or local deployments | Configure model services in one place, then switch models or compare multiple models in a conversation |
| Save a consistent role and conversation settings | Create an Assistant with a prompt, model parameters, knowledge bases, and MCP |
| Let AI read a workspace and perform tasks | Create an Agent and control accessible directories, tools, and approval modes |
| Have AI follow a specialized workflow | Install Skills and enable them for individual Agents |
| Connect search, databases, or third-party services | Add a local or remote MCP Server |
| Build a personal retrieval library | Import documents and configure an Embedding model |
| Work with images, translations, notes, and files | Use the separate Image Generation, Translation, Notes, and Files workspaces |
| Run an Agent from a chat platform or at a scheduled time | Configure Channels and Scheduled Tasks |

## Main workspaces

The Cherry Studio V2 sidebar can display these applications as needed:

* **Chat**: Communicate with Assistants and models, and manage sessions and messages.
* **Agents**: Perform tasks that require files, commands, or multi-step tool calls.
* **Library**: Manage Assistants, Agents, Skills, and prompts in one place.
* **Image Generation**: Create and manage images with image-generation models.
* **Translation**: Translate between two languages and read the texts side by side.
* **Mini Apps**: Open added web tools inside the application.
* **Knowledge Base**: Import sources, process chunks, and retrieve information.
* **Files**: View and manage file resources from the application.
* **Code Tools**: Manage developer-oriented coding tools.
* **Notes**: Edit and organize Markdown notes.
* **OpenClaw**: Use a separate autonomous Agent workspace.

The sidebar shows only the entry points that you enable. Hiding an item does not delete its data.

## Quick start

### 1. Download and install

Open [Client Downloads](cherrystudio/download.md) and select the version for your system. For your first installation or when the operating system displays a security warning, see the [Installation Guide](pre-basic/installation/).

Cherry Studio supports Windows, macOS, and Linux. Installation packages differ by operating system and chip architecture, so follow the instructions on the download page.

### 2. Configure model services

Open **Settings → Model Services**:

1. Select an existing provider or add a compatible provider.
2. Enter the API URL and API key.
3. Fetch the model list and enable the models you want to use.
4. Return to Chat, select a model, and send your first message.

If you use a local service such as Ollama or LM Studio, make sure the service is already running on the computer. See [Model Services](pre-basic/providers/) for detailed instructions.

### 3. Start with one use case

* For everyday Q&A, writing, or translation, start with [Chat](cherrystudio/preview/chat.md).
* For a consistent prompt and parameters, create an Assistant in the [Library](cherrystudio/preview/library.md).
* To work with local files or run tools, create an [Agent](advanced-basic/agent.md).
* To answer from personal sources, create a [Knowledge Base](knowledge-base/knowledge-base.md).

You do not need to configure every feature at once. Complete one small, verifiable task before adding Skills, MCP, or automation; this makes troubleshooting easier.

## Assistants, Agents, and extensions

### Assistant

An Assistant stores a reusable conversation configuration, including its prompt, model parameters, knowledge bases, and MCP. It is designed for stable, conversation-centered use cases.

### Agent

An Agent can access specified directories and call built-in tools, MCP, and Skills. You can choose Normal, Plan, Auto-edit, or Full Auto permission modes. See [Agents](advanced-basic/agent.md).

### Skills and MCP

* [Skills](pre-basic/settings/skills.md) tell an Agent how to complete a type of work using a specific workflow.
* [MCP](advanced-basic/mcp/) connects external tools, prompts, and resources to an Assistant or Agent.

If you are not sure which one to choose, read [Concepts 101](advanced-basic/concepts-101.md).

## Data and security

Cherry Studio stores its application configuration and work data primarily on the local computer, but “using a desktop application” does not mean that “all processing stays local”:

* When you use a cloud model, messages, attachments, or retrieved context are sent to the selected model provider as required by the request.
* When you use a remote MCP Server, Channel, or another third-party service, relevant data may be sent to that service.
* Agents and local MCP Servers may read files or run commands according to the permissions you grant.
* Local models can reduce cloud data transfer, but you must still review connected model services, plugins, and network tools.

{% hint style="warning" %}
Do not put API keys, access tokens, passwords, or private keys in prompts, knowledge bases, documentation, or screenshots. Restrict directories accessible to Agents, use least privilege for MCP and Channels, and complete a controlled test before enabling Full Auto Mode.
{% endhint %}

Back up important data regularly. Cherry Studio supports local export and backups to WebDAV, S3-compatible storage, and other destinations. See [Data Settings](data-settings/) for available options.

## Open source and licensing

The Cherry Studio Community Edition source code is hosted on [GitHub](https://github.com/CherryHQ/cherry-studio) and licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). Before using, modifying, or distributing it, read the [Open Source License Agreement](contact-us/questions/cherrystudio-xu-ke-xie-yi.md).

You are welcome to participate:

* [Contribute code](contribution/code.md)
* [Contribute documentation](contribution/docs.md)
* [Report an issue](https://github.com/CherryHQ/cherry-studio/issues)
* [Join a discussion](https://github.com/CherryHQ/cherry-studio/discussions)

## Get help

When you encounter a problem, start with [Frequently Asked Questions](question-contact/questions.md) and [How to Ask Effective Questions](question-contact/ask.md). When submitting feedback, include the Cherry Studio version, operating system, reproduction steps, and necessary logs, and remove sensitive information such as API keys or file contents first.

Community links:

* [Telegram](https://t.me/CherryStudioAI)
* [Discord](https://discord.gg/wez8HtpxqQ)
* [QQ Group](https://qm.qq.com/q/lo0D4qVZKi)
* [Feedback and Suggestions](question-contact/suggestions.md)
