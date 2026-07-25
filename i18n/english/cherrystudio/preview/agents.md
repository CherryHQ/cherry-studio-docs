---
description: Find, create, import, and manage chat assistant presets
icon: head-side-gear
---

# Assistant Library

The Assistant Library is Cherry Studio's marketplace for chat assistant presets. A preset primarily stores a name, icon, prompt, and some default settings. When you add a preset to Chat, it becomes an independently editable assistant.

{% hint style="warning" %}
An “assistant” in the Assistant Library is intended for role-based chat and is not the same as a [Cherry Agent](../../advanced-basic/agent.md). Use an agent when you need to access a workspace, read or write files, run commands, or call tools across multiple steps.
{% endhint %}

## Assistant Library, chat assistants, and Resource Library

| Name | Purpose |
| --- | --- |
| Assistant Library | Browse built-in presets, maintain your own presets, and import or subscribe to preset sources |
| Chat assistant | An available assistant already added to the [Chat page](chat.md), with its own topics and settings |
| [Resource Library](library.md) | Create and edit models, assistants, agents, and other resources in one place; best for complete configuration |

When you add a preset from the Assistant Library, Cherry Studio creates a separate copy as a chat assistant. Editing or deleting the original preset later does not automatically change the assistant you created.

## Open the Assistant Library

You can open it from:

* **Launchpad → Assistant Library**.
* The add button in the assistant list on the Chat page.

If you only want to add an assistant quickly, search for a preset from the Chat page. Open the full Assistant Library when you need to browse categories, import, subscribe, or manage presets in bulk.

## Browse and search presets

The left side of the Assistant Library organizes presets under “My” and purpose-based categories. The main area shows cards in the current category.

* **Categories**: View categories supplied by built-in or subscribed sources.
* **Search**: Search across categories by name and description.
* **Card preview**: View the name, description, and a prompt summary.
* **My**: View presets you created or imported.

Categories and counts can change with the app version, current language, or subscription source, so this guide does not provide a fixed list.

## Create a chat assistant from a preset

1. Find the preset you need.
2. Click its card to review the prompt and description.
3. Select **Add to Assistants**.
4. Return to the [Chat page](chat.md).
5. Select the assistant you just added, then choose a model from the top bar.

The new assistant has its own ID and default topic. You can edit its prompt, model, knowledge bases, MCP, and model parameters without changing the original preset in the Assistant Library.

## Create your own assistant

There are two methods for different levels of configuration.

### Create a lightweight preset in the Assistant Library

Click **Create Assistant**, then enter:

* **Name**: Used for search and identification.
* **Emoji**: The assistant icon. If you do not select one, Cherry Studio attempts to extract one from the name.
* **Prompt**: Defines the role, goals, boundaries, and output style.
* **Knowledge Base**: Optional; links an existing knowledge base.

Name and prompt are required. The prompt editor can use the default assistant model to improve the prompt, and you can undo that AI rewrite.

After you save it, the preset appears under My. To use it in Chat, click the preset and select **Add to Assistants**.

### Create a fully configured assistant in the Resource Library

To set the model, tags, and advanced parameters at the same time, create the assistant in the [Resource Library](library.md). The full editor includes:

* Name, Emoji, description, tags, and model.
* System prompt.
* Temperature, Top P, maximum output, context length, and streaming.
* Tool call mode, maximum tool calls, and custom parameters.
* Knowledge bases.
* MCP mode and servers.

The full editor still requires a name and prompt. Keep model parameters at their defaults unless you have a specific requirement.

## How the model is selected

When you create or import a lightweight preset in the Assistant Library, Cherry Studio uses the current [Default Assistant Model](settings/default-models.md) as the preset's default model. After adding it to Chat, you can switch models from the top bar.

When you create a fully configured assistant in the Resource Library, you can select the model before saving.

Do not put model settings in the system prompt. Use the model selector when you need to change models so you can verify the provider and actual model ID.

## Import assistant presets

Click **Import**, then choose one of these methods:

### Import from a URL

1. Select **URL**.
2. Paste an address that returns JSON directly.
3. Click Import.

### Import from a file

1. Select **File**.
2. Choose a `.json` file.
3. Click Import.

The imported content can be one object or an array of objects. Each preset requires at least `name` and `prompt`:

```json
[
  {
    "name": "Documentation Review Assistant",
    "emoji": "📝",
    "description": "Checks structure, terminology, and usability",
    "prompt": "Review product documentation and provide specific revision suggestions."
  }
]
```

During import, Cherry Studio assigns each preset a new local ID and uses the current default assistant model. Old topics and messages in the source file are not imported as chat history.

{% hint style="warning" %}
Import presets only from trusted sources. Preset prompts may contain hidden goals, external links, or behavior requirements that are not appropriate for you. Review each prompt before adding it to Chat.
{% endhint %}

## Subscribe to an assistant source

A subscription is useful when a team or community maintains a remote collection of presets:

1. Click **Import**.
2. In the subscription section, enter an HTTP(S) address that returns a JSON array directly.
3. Click **Subscribe**.
4. After Cherry Studio reloads, it reads system presets from that address.

While the subscription source is available, Cherry Studio uses it as the system preset source. If the remote source cannot be read, Cherry Studio falls back to its built-in presets. Canceling the subscription also restores the built-in presets.

Subscription vs. one-time import:

| | One-time import | Subscription |
| --- | --- | --- |
| Data location | Imported as local presets under My | Read from the remote source at startup or reload |
| Future updates | Does not change automatically | Can update from the remote source after a reload |
| Suitable for local editing | Yes | Best maintained centrally at the subscription source |

For the detailed format and maintenance workflow, see [Assistant Subscriptions](../../data-settings/assistants-subscribe.md).

## Manage presets under My

Under My, use a card menu or **Manage Assistants** to:

* Edit a preset.
* Add it as a chat assistant.
* Export one preset as JSON.
* Delete a preset.
* Drag presets to reorder them.
* Select, export, or delete multiple presets.

You can import a batch-exported JSON file on another device. Before deleting a preset, confirm that you will not need it to create another assistant. Assistants already added to Chat are not deleted with the preset.

## Edit an assistant already added to Chat

After adding a preset to Chat, edit it under chat assistant settings or in the Resource Library. Common settings include:

* System prompt.
* Current and default models.
* Knowledge bases and web search.
* MCP tools.
* Context and output parameters.

See [Chat Interface](chat.md) for complete chat instructions.

## Assistant or agent

| Requirement | Recommended option |
| --- | --- |
| Questions, writing, translation, or analysis with a fixed role | Chat assistant |
| Reuse and share prompt templates | Assistant Library preset |
| Edit the model, parameters, knowledge bases, and MCP in one place | Assistant editor in the Resource Library |
| Access a workspace, read or write files, or run commands | [Agent](../../advanced-basic/agent.md) |
| Run on a schedule and send results to an external channel | Agent + [Scheduled Tasks](../../advanced-basic/scheduled-tasks.md) + [Channels](../../advanced-basic/agent-channels.md) |

If an import fails, a subscription source cannot be read, or a preset behaves unexpectedly, submit a JSON example, the address response status, and error details through [Feedback and suggestions](../../question-contact/suggestions.md). Remove private data and keys before submitting.
