---
description: Use assistants, topics, models, and input tools for multi-model chats
icon: message
---

# Chat interface

Chat is the most frequently used workspace in Cherry Studio. You can create assistants for different purposes, manage multiple independent topics under each assistant, and add files, knowledge bases, web search, MCP tools, or multiple models as needed.

{% hint style="info" %}
Before your first chat, add a provider, enable a model, and pass the connection check under [Model Services](../../pre-basic/providers/).
{% endhint %}

## Understand assistants and topics

The Chat page uses a two-level “assistant → topic” structure:

* **Assistant**: Stores the role prompt, current model, model parameters, knowledge bases, MCP, web search, and other settings.
* **Topic**: Stores an independent chat history.

An assistant can have multiple topics. They share the assistant's settings, but their message histories remain separate. For example, you can create “Project A” and “Project B” topics under the same “Code Review Assistant.”

For tasks that must autonomously access a workspace, read or write files, or run commands, use [Agents](../../advanced-basic/agent.md). Do not treat chat assistants and agents as the same feature. See [Concepts 101](../../advanced-basic/concepts-101.md) for more details.

## Page layout

The Chat page has four main areas:

1. **Assistant and topic list**: Switch assistants, create topics, and search or manage history.
2. **Top bar**: Shows the current assistant and model, with controls for chat settings, search, and the sidebar.
3. **Message area**: Shows user messages, model responses, thinking processes, tool calls, and citations.
4. **Input area**: Enter messages and use attachments, web search, knowledge bases, MCP, multiple models, and other tools.

Depending on your display settings, the topic list can appear on the left or right, and the sidebar can be collapsed. Its position does not change the relationship between assistants and topics.

## Start your first chat

1. Open **Chat** from the sidebar.
2. Select an assistant, or add one from the [Assistant Library](agents.md).
3. Click **New Topic**.
4. Select a model from the top bar.
5. Enter your question and press the configured send shortcut.

If the model does not respond, check that the model service is enabled, the API Key and endpoint are correct, and the current model is available.

## Select a model

### Current assistant model

The model selector in the top bar determines the assistant's base model. After you switch models, subsequent messages use the new model. You can change the assistant's default model and whether new topics reset the model under Assistant Settings.

Select only models intended for chat. Embedding and reranking models process knowledge bases and do not appear in the standard chat model list.

### Get parallel responses from multiple models

Click the model mention button in the input area, or type `@`, to select one or more models. The selected models appear above the input box:

* When one model is selected, it responds instead of the assistant's base model.
* When multiple models are selected, Cherry Studio generates their responses in parallel so you can compare the results.
* Removing the model tags above the input box restores the assistant's base model.

When uploading an image, every mentioned model must support visual input. Otherwise, you may be unable to select the model or send the message.

## Input tools

You can drag input tools to reorder them or use the context menu to show and hide them. Some buttons are collapsed when the window is narrow or many tools are enabled.

| Tool | Purpose | Notes |
| --- | --- | --- |
| New Topic | Create an independent topic under the current assistant | Does not delete the original topic |
| Attachment | Add an image, document, or text | Available types depend on model capabilities |
| Web Search | Add search results as supporting context | Requires native model search or a configured search service |
| Knowledge Base | Select one or more knowledge bases for the assistant | The selection remains in the assistant settings until removed |
| MCP | View or call MCP tools assigned to the assistant | Requires a configured MCP server |
| Mention Models | Select one or more response models for the input | You can also type `@` to open it |
| Quick Phrases | Insert frequently used prompt templates | Managed centrally in Settings |
| Thinking | Adjust the thinking mode or effort for reasoning models | Appears only when supported by the model |
| Web Context | Allow supported models to read a URL | Appears only for compatible model and provider combinations |
| Generate Image | Ask a supported image generation model to return an image | For dedicated image creation, you can also use [Painting](drawing.md) |
| Clear Messages | Delete messages in the current topic | Cannot be undone |
| New Context | Keep the visible history, but stop sending earlier messages to the model from this point | Useful when the topic continues but the model should not use earlier content |
| Expand Input | Expand or restore the input area | Useful for long prompts |

Tool availability depends on the current page, model capabilities, assistant settings, and your toolbar configuration. If a button is missing, right-click the input toolbar to see whether it is hidden, then confirm that the model or assistant meets the requirements.

### `@` and `/` quick panels

When input quick panels are enabled:

* Type `@` to open the model selection panel.
* Type `/` to open a quick panel of available actions and resources.

The current chat context and enabled tools determine what appears in a quick panel. You can turn off character triggers under Input Settings and continue to use the same features through their tool buttons.

## Use attachments

1. Click **Attachment**, or drag a file into the input area.
2. Confirm that a file preview appears above the input box.
3. State clearly in your question how the model should process the file.
4. Send the message.

Available file types depend on model capabilities:

* Images require a vision model or a model that supports image generation or editing.
* Documents and text are processed as attachments before being added to the message context.
* When multiple models are mentioned, an attachment must match the capabilities shared by all selected models.

Long text can also be converted to a file automatically according to your input settings, keeping it from filling the input box. Before sending private or confidential information, check the current model provider and its data policy.

## Use a knowledge base

1. First, create a knowledge base and finish processing its content under [Knowledge Base](knowledge-base.md).
2. Return to the Chat page and click **Knowledge Base**.
3. Select one or more knowledge bases.
4. In your question, specify the subject, scope, or time range to retrieve.

Knowledge base tags appear above the input box. In the current version, attachments and knowledge base selections can conflict in some combinations. If the button is unavailable, remove the current attachment before selecting a knowledge base.

Retrieved knowledge base content is reference material for the model's answer and does not guarantee accuracy. Verify citations and original sources for important conclusions.

## Use web search and MCP

### Web search

Web search has two types of sources:

* Native search capabilities provided by the model provider.
* External search services configured in Cherry Studio.

See [Web Search Mode](../../websearch/) for configuration details. After enabling search, verify that each cited link actually supports the model's conclusion.

### MCP tools

MCP lets chat assistants call external tools or data. Before using it:

1. Install and enable a server under MCP Settings.
2. Assign the required MCP server to the current assistant.
3. Select a model that supports tool calls.
4. Review the enabled tools and permissions before sending your message.

See [MCP](../../advanced-basic/mcp/) for complete instructions.

## Work with messages

Move the pointer near a message to reveal its action bar. Available buttons vary with the message role and your settings.

| Action | Purpose |
| --- | --- |
| Copy | Copy the message body |
| Edit and Resend | Edit a user message and regenerate from that point |
| Regenerate | Ask the model to answer again |
| Respond with Another Model | Select another model to generate a response from this point |
| Translate | Translate the model response into the selected language |
| Save to Notes | Save the response to Cherry Studio Notes |
| Delete | Delete one message |
| New Branch | Create a new chat branch from the current message |
| Multi-select | Select multiple messages for another action |
| Save or Export | Save as a file, add to a knowledge base, or export content |

Regenerating, editing a message in the history, or deleting a message can change the subsequent conversation chain. Create a new branch first if you need to keep the original result.

## Manage long chats

| Action | Are messages kept? | Is earlier context sent with later messages? | Best for |
| --- | --- | --- | --- |
| New Topic | Kept in the original topic | No | Starting a new task or project |
| New Context | Kept in the current topic | Restarts from the marker | Moving to a new stage of the same task, or resetting confused context |
| Clear Messages | Deleted | No | Removing a topic you no longer need |
| New Branch | Original chat is kept | Continues from the selected message | Comparing different prompts or model approaches |

{% hint style="warning" %}
Clear Messages deletes the current topic's content. New Context only stops earlier history from being sent to the model. These actions are not the same.
{% endhint %}

The Token count shown in the input area is an estimate that helps you judge whether the context is near the model's limit. Tokenization and billing rules vary by model and provider, so refer to your provider for the final usage.

## Assistant and global settings

### Assistant settings

Assistant settings affect every topic under that assistant. They include:

* Name, avatar, and system prompt.
* Default model and model parameters.
* Knowledge bases, web search, and MCP.
* Context length, maximum output length, streaming, and provider-specific parameters.

Not every model supports the same parameters. Use the defaults unless you have a specific requirement. Custom parameters can override built-in settings.

### Chat and input settings

Chat Settings also include global display and input preferences, such as:

* Message style, fonts, code blocks, mathematical formulas, and the display of thinking content.
* Token estimates, pasting long text, input translation, and the send method.
* Assistant list, topic position, and toolbar display.

Related pages:

* [Default Models](settings/default-models.md)
* [Display Settings](settings/display.md)
* [Keyboard Shortcuts](settings/key-shortcut.md)
* [Prompts and Quick Insert](../../pre-basic/settings/quick-phrase.md)

## Troubleshooting

### The Send button is unavailable

Check whether the input is empty, generation is still in progress, the current model supports the attachment type, and the model service is enabled.

### A knowledge base or MCP is missing

Confirm that the feature has been created or enabled and that the current assistant supports tool calls. If the Knowledge Base button is unavailable, remove attachments from the input area first.

### Multiple model responses do not appear

Confirm that the mentioned models still appear above the input box and that each model is available. A disabled model, insufficient balance, or incompatible API can cause an individual response to fail.

### The chat becomes slow or drifts off topic

Check the Token estimate and context length first. Use **New Context** to restart within the current topic, or create a new topic to separate tasks.

If the problem persists, submit your Cherry Studio version, model name, provider, reproduction steps, and error details through [Feedback and suggestions](../../question-contact/suggestions.md).
