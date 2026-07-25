---
icon: graduation-cap
---

# Concepts 101: Assistants, Agents, Skills, MCP, and Channels

Cherry Studio V2 separates “chatting with a model” from “having a model perform tasks” into different layers. Understanding the following concepts will help you decide where to begin configuring a workflow.

## The short version

| Concept | Primary purpose | Typical use |
| :--- | :--- | :--- |
| Model service | Provide model and API access | Connect DeepSeek, Claude, GPT, and other models |
| Assistant | Save a reusable conversation configuration | Translation, writing, Q&A, and knowledge base retrieval |
| Agent | Call tools with controlled permissions and complete multi-step tasks | Work with files, run commands, and execute workflows |
| Skill | Give an Agent instructions, workflows, and resources for a specific task | Create presentations, review code, and write documentation to team standards |
| MCP | Connect external tools and data through a standard protocol | Search the web, read databases, and call third-party services |
| Channel | Connect an Agent to an instant messaging platform | Use an Agent from Feishu, Telegram, Slack, and other platforms |
| Scheduled task | Run an Agent once, at intervals, or on a Cron schedule | Daily briefings, periodic checks, and scheduled summaries |

The most common choices are:

* If you only need a consistent persona, model parameters, or knowledge base Q&A, use an **Assistant**.
* If AI needs to read directories, modify files, run commands, or call tools in sequence, use an **Agent**.
* If an Agent lacks a particular work method, install and enable a **Skill**.
* If an Assistant or Agent needs a tool outside Cherry Studio, configure **MCP**.
* If team members should use an Agent from messaging software, configure a **Channel**.
* If an Agent should run unattended on a schedule, create a **Scheduled Task**.

## Model services provide capabilities

Model services store API URLs, keys, and model lists. Assistants and Agents both require a model, but their model requirements differ:

* Assistants are designed for everyday conversations. Depending on the use case, you can choose a model that supports text, vision, reasoning, or tool calls.
* The Agent model selector shows only models that support Anthropic Messages endpoints and are suitable for conversational execution. Embedding, Rerank, and image-generation models do not appear there.

Configure a model under **Settings → Model Services** before creating an Assistant or Agent. See [Model Services](../pre-basic/providers/) for detailed steps.

## Assistant: a reusable conversation configuration

An Assistant saves conversation behavior that you want to reuse over time. In addition to a name and prompt, you can configure the model, sampling parameters, context length, knowledge bases, and MCP mode.

For example, you can create:

* A translation Assistant with fixed terminology and output formatting.
* A customer-support Assistant connected to a product documentation knowledge base.
* A research Assistant that can call a search MCP Server.

Assistants are suited to conversation-centered tasks. They can retrieve from knowledge bases or call configured MCP tools, but they do not receive a local working directory, file-editing permissions, or command-execution permissions like Agents do.

Create and maintain Assistants in the [Library](../cherrystudio/preview/library.md), then use them on the main conversation page. Continue with [Assistant Library](../cherrystudio/preview/agents.md) and [Chat](../cherrystudio/preview/chat.md).

## Agent: an executable task configuration

In addition to a prompt and model, an Agent can be configured with:

* Local directories it may access.
* A tool permission mode.
* Built-in tools, MCP Servers, and Skills.
* Primary, planning, and small models.
* Runtime settings such as maximum turns, environment variables, and heartbeat.

These settings allow an Agent to keep performing multiple steps toward a goal instead of only suggesting actions. For example, it can read workspace files, modify documents, call MCP services, and save the results locally.

{% hint style="warning" %}
An Agent's permission scope determines which directories it can read and write and whether it can run tools directly. When getting started, limit the accessible directories and prefer a permission mode that requires confirmation. Use a mode that skips confirmation only when you understand the risks.
{% endhint %}

The Agent page depends on Cherry Studio's local **API Server**. V2 automatically attempts to start it when you create an Agent, so you usually do not need to configure it manually in Settings first. If the service is disabled or not running, the Agent page prompts you to start it. The API Server can also let other applications call Cherry Studio through a local HTTP interface. See [Agents](agent.md) and [API Server](api-server.md).

## Skill: tell an Agent how to perform a type of work

A Skill is an installable set of task instructions and supporting resources. It works like a playbook that describes its trigger conditions, execution steps, quality requirements, and any scripts or templates it may use.

Skills are bound to an Agent by Agent ID. When creating an Agent, save it first; you can then enable Skills under **Capability Extensions → Skills** for that Agent.

Use a Skill when:

* A type of task should follow the same workflow every time.
* You need to reuse team standards, templates, or checklists.
* You want several Agents to use an established method.

See [Skills](../pre-basic/settings/skills.md) for installation, search, and management instructions.

## MCP: connect AI to external capabilities

MCP (Model Context Protocol) connects AI applications to external tools, prompts, and resources. Cherry Studio can add a local STDIO Server or connect to an SSE or Streamable HTTP Server.

An MCP Server can provide three types of capabilities to a model:

| Capability | Purpose |
| :--- | :--- |
| Tools | Perform searches, queries, writes, API calls, and other operations |
| Prompts | Provide reusable prompt templates |
| Resources | Provide readable data or context |

Assistants support Disabled, Auto, and Manual MCP modes. An Agent can select services to bind from enabled MCP Servers.

{% hint style="warning" %}
An MCP Server may run a program locally or send content to a remote service. Before adding one, verify its source, command, environment variables, accessible directories, and remote address. Grant only the permissions required for the task.
{% endhint %}

See the [MCP Tutorial](mcp/) for configuration instructions.

## Skill compared with MCP

Skills and MCP often work together, but they solve different problems:

| Comparison | Skill | MCP |
| :--- | :--- | :--- |
| Core question | Tell an Agent “how to do it” | Give a model “something it can call” |
| Main content | Instructions, workflows, templates, scripts, and resources | Tool, prompt, and resource interfaces |
| Primary use | Agents | Assistants and Agents |
| External service required | Not necessarily | Depends on the Server |

For example, “write a weekly report using the team template” can be a Skill, while “read this week's tasks from the project management system” can be provided through MCP. Combined, the Agent knows the writing process and can obtain the required data.

## Channel: connect an Agent to a chat platform

A Channel binds an Agent to an instant messaging platform. Cherry Studio V2 currently supports Channel configurations for Feishu / Lark, Telegram, QQ, WeChat, Discord, and Slack.

The Channel receives platform messages, sends them to the bound Agent for processing, and returns the results to the original platform. It does not replace the Agent: the model, prompt, tools, directories, and permissions remain configured on the Agent.

Channels often run unattended. Before enabling one, check:

* Whether the correct Agent and model are bound.
* Whether the conversations or Channel IDs allowed to receive responses are restricted.
* Whether the Agent has the tool permissions required for the task.
* Whether platform tokens and keys are stored only in the corresponding configuration.

See [Channels](agent-channels.md).

## Scheduled task: run an Agent on a schedule

A Scheduled Task also uses an Agent as its executor. You can create:

* A task that runs only once.
* A task that repeats at a fixed interval.
* A task scheduled with a Cron expression.

Scheduled Tasks are suitable for work that does not require human input. Before creating one, make sure the corresponding Agent can complete the same task successfully in a regular conversation, then configure appropriate permissions, timeout, and schedule. See [Scheduled Tasks](scheduled-tasks.md).

## Combine the capabilities

Consider a workflow that summarizes team project progress every day and sends it to a Feishu group:

1. Configure a model for the Agent under **Model Services**.
2. Create an **Agent** and specify the summary rules and output format.
3. Install and enable a team weekly-report **Skill** to standardize the writing process.
4. Connect the project management system through **MCP** to read task data.
5. Create a **Scheduled Task** that runs the Agent every day.
6. Create a Feishu **Channel** so team members can continue asking questions from the group chat.

Not every use case requires every capability. Start with an Assistant or Agent, then add Skills, MCP, Channels, or Scheduled Tasks only when a clear need appears. This keeps the configuration easier to maintain.

## Recommended learning path

1. Configure [Model Services](../pre-basic/providers/) and complete a regular conversation.
2. Create an Assistant from the [Library](../cherrystudio/preview/library.md) and become familiar with prompts, models, and knowledge bases.
3. Create an [Agent](agent.md), starting with a restricted directory and permissions that require confirmation.
4. Add [Skills](../pre-basic/settings/skills.md) or [MCP](mcp/) as the task requires.
5. After the Agent runs reliably, configure [Scheduled Tasks](scheduled-tasks.md) and [Channels](agent-channels.md).
