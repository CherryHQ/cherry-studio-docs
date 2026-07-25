---
icon: route
---

# Call Chain (Trace)

Call Chain (Trace) shows the steps that a conversation goes through inside Cherry Studio. Based on OpenTelemetry traces and spans, it organizes model requests, tool calls, knowledge base retrieval, and other operations into a tree and displays each node's duration, status, inputs, outputs, and token usage.

When a response is unexpected, a tool call fails, or processing slows down, Call Chain can help you identify where the issue occurred:

* Whether the model received the correct context;
* What web search or knowledge base retrieval returned;
* Which parameters an MCP tool used;
* Which step took the longest or returned an error;
* How many tokens each response used in a multi-model conversation.

{% hint style="warning" %}
Call Chain is a developer diagnostic feature. It may store prompts, model outputs, tool parameters, and retrieved content. Do not leave it enabled for long periods in production conversations that contain sensitive information, and do not share a complete trace without reviewing it first.
{% endhint %}

## Enable Call Chain

1. Open `Settings → General Settings`.
2. Find **Developer Mode**.
3. Turn on **Enable Developer Mode**.
4. Completely quit and reopen Cherry Studio.
5. Start a new conversation and send a message.

{% hint style="info" %}
You must restart the app. The Trace window and cache services are activated at Cherry Studio startup based on the Developer Mode setting. If you only toggle the setting without restarting, the entry point may not appear or Trace data may be unavailable.
{% endhint %}

Messages generated before Call Chain was enabled will not receive traces retroactively. The entry point appears only for messages created after the restart and successfully assigned a Trace ID.

## Open a Call Chain

In a regular conversation, find the message you want to inspect, hover over its action bar, and click the **Call Chain** icon.

The entry point is currently available only for regular conversation messages. The message action bar in Agent Session does not show the Call Chain button.

The button appears only when all of the following conditions are met:

* Developer Mode is enabled;
* The current message has a Trace ID;
* The Trace service was activated when the app started.

Cherry Studio opens a separate Call Chain window. If you click the Call Chain button on another message, the existing window switches to that message's trace.

If the same question produced responses from multiple models, click Call Chain on each model's corresponding response. The window filters Trace data by the model associated with that message.

## Understand the Trace Tree

A complete request corresponds to one trace, and each processing step within it corresponds to a span. A child node indicates that the step occurred in the context of its parent node.

After you select a node, the details pane may show:

| Information | Purpose |
|---|---|
| Start and end times | Determine the order in which steps occurred |
| Duration | Identify time-consuming operations |
| Error highlighting | If the node name turns red, inspect that step's error output |
| Input / Attributes | Inspect inputs, parameters, and context |
| Outputs | View returned content; error details also appear here |
| Token Usage | Compare Prompt Tokens and Completion Tokens |

Not every request produces the same nodes. The actual structure depends on the model, whether web access is used, whether a knowledge base is linked, and whether the model calls an MCP tool.

### Model Calls

Use a model node to inspect:

* The model that was actually called;
* The input sent to the model;
* The text or streamed result returned by the model;
* Prompt Tokens and Completion Tokens;
* Request duration and error status.

If a response clearly omits information, first confirm that the model input contains the relevant context.

### Web Search

When web search is used, the trace may include nodes for the search request, result processing, and model calls. Check:

* Whether the search query is accurate;
* Whether the search returned successfully;
* Whether the results were filtered before being sent to the model;
* Whether search duration is the main bottleneck.

### Knowledge Base Retrieval

After linking a [knowledge base](../knowledge-base/knowledge-base.md), use Call Chain to confirm whether retrieval found the expected content. Inspect the retrieval query, returned chunks, similarity information, and the final context sent to the model.

If the knowledge base node has no results, check the embedding model, document processing status, retrieval threshold, and wording of the user's question.

### MCP Tool Calls

When using [MCP](mcp/README.md), Trace can help you verify the tool name, call parameters, return value, duration, and errors.

When a tool fails, distinguish among these cases:

* The model selected the wrong tool;
* Tool parameters were incomplete or incorrectly formatted;
* The MCP Server was not running or the connection failed;
* The tool ran, but the model did not use its returned content correctly.

{% hint style="info" %}
Trace displays diagnostic data. It does not automatically retry or repair failed steps. After identifying the cause, return to the relevant conversation, model, knowledge base, or MCP settings to update the configuration.
{% endhint %}

## Data Storage and Cleanup

Trace data is stored in the current user's home directory:

```
~/.cherrystudio/trace
```

Data below this directory is organized by topic ID and Trace ID. On Windows, `~` represents the current user directory, such as `C:\Users\<username>`.

When you delete a message or topic, Cherry Studio removes the corresponding Trace data. To clear all local Trace data:

1. Open `Settings → Data Settings`.
2. Find the cache information.
3. Click **Clear Cache** and confirm.

Clearing the cache also deletes other app caches. Before continuing, make sure you do not need to retain any diagnostic data.

{% hint style="danger" %}
Do not edit Trace files manually while Cherry Studio is running. When sharing diagnostic information, capture only the necessary nodes and redact API keys, personal data, file paths, and business content first.
{% endhint %}

## Troubleshooting

### Developer Mode Is Enabled, but There Is No Call Chain Button

Check the following in order:

1. Make sure you completely restarted Cherry Studio after enabling the setting.
2. Make sure the current message was generated after the restart.
3. Make sure you are viewing a regular conversation message. Historical messages without a Trace ID do not show the entry point.
4. Create a new topic and send a simple test message.

### The Call Chain Window Is Empty

* Wait for the current model output and tool calls to finish, then reopen Call Chain.
* Make sure the corresponding message was not deleted and the Trace cache was not cleared.
* If you just enabled Developer Mode, restart the app, create a new conversation, and try again.
* For multi-model responses, open Call Chain separately from each model's corresponding response message.

### Knowledge Base, Search, or MCP Nodes Are Missing

The relevant spans appear only if the current request actually used those capabilities. Check the conversation result and model tool-call records first to confirm that the step occurred.

### There Is Too Much Trace Data

After troubleshooting, turn off Developer Mode and restart Cherry Studio. To free local storage immediately, clear the cache in Data Settings.

***

### 💡 Get Help and Submit Feedback

If Call Chain data is abnormal, include the necessary Trace screenshots, Cherry Studio version, model used, and whether the knowledge base, web search, or MCP was enabled when you submit feedback. See [Feedback and Suggestions](../question-contact/suggestions.md) for official support channels.
