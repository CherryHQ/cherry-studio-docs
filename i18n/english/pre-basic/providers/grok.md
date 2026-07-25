---
icon: x
---

# Grok

Cherry Studio V2's built-in Grok template connects to the official xAI API. V2 uses an xAI Responses adapter for this provider, supporting chat, reasoning, tool calls, and xAI's official Web Search and X Search.

{% hint style="warning" %}
Grok does not receive real-time information automatically. Only after you enable Web Search in a chat does Cherry Studio request Web Search and X Search from xAI. Server-side search tools may incur additional charges.
{% endhint %}

## Before you begin

- An account that can sign in to the [xAI Console](https://console.x.ai/);
- An API Key created in the xAI Console;
- Available credit for the team or account;
- Confirmation of the currently available models and service regions.

Signing in to x.com or the Grok website does not automatically sign you in through Cherry Studio. Using the xAI API requires a separate API Key.

## Configure Grok

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **Grok**;
3. Enter the xAI API Key;
4. Keep the default Base URL `https://api.x.ai`;
5. Turn on the provider switch at the top of the page;
6. Click **Add** in the model list, review the sync preview, and apply the changes;
7. Enable the models you plan to use.

{% hint style="danger" %}
Do not include the API Key in chat messages, documents, code repositories, or issue screenshots. If exposed, revoke it immediately in the xAI Console and create a new one.
{% endhint %}

## Select a model

xAI continuously updates models and aliases. Click **Add** to sync the list currently visible to your account, and refer to the [xAI model documentation](https://docs.x.ai/developers/models).

Common current choices include:

| Model ID | Recommended use |
| --- | --- |
| `grok-4.5` | Complex knowledge work, coding, and Agent tasks |
| `grok-4.3` | General chat, image understanding, and adjustable reasoning |
| `grok-build-0.1` | Agent-oriented coding tasks |

- Enable only the models you actually need;
- Verify the complete model ID instead of relying only on the display name;
- A `-latest` alias may migrate automatically to a new version;
- Date-stamped model IDs are better for workflows that require fixed behavior;
- A model appearing in the synced list does not mean the account has unlimited credit.

## Use Web Search

After you enable **Web Search** in the chat input box, Cherry Studio configures the following for Grok:

- xAI Web Search;
- xAI X Search;
- Understanding images in search pages and X posts;
- Returning search sources and citations.

If you configure excluded domains in the Web Search settings, Grok's official search receives at most the first five valid domain rules.

To use it:

1. Select an enabled Grok text model;
2. Enable **Web Search** in the input box;
3. Ask a question that clearly requires current information from the web or X;
4. Wait for the model to complete its server-side search;
5. Expand the citations and verify the sources.

{% hint style="info" %}
“Newer model knowledge” and “Web Search” are not the same. When Web Search is disabled, Grok answers only from the model's existing knowledge. For current information, explicitly enable Web Search and check the citations.
{% endhint %}

## Reasoning and tool calls

Cherry Studio displays reasoning options according to the model ID:

- `grok-4.3` supports Off, Low, Medium, High, and other reasoning efforts;
- The reasoning and non-reasoning variants of Grok 4 Fast are different models and cannot be exchanged using only a switch;
- Options for other new models depend on the current Cherry Studio version and registered model information.

Before using MCP or other tools:

1. Complete a standard chat health check;
2. Enable one simple tool;
3. Send a request that clearly requires the tool;
4. Confirm that the model actually calls the tool;
5. Then add Web Search or multiple tools.

Web Search is an xAI server-side tool, while MCP tools run locally or remotely through Cherry Studio. They can be used together, but test them separately when troubleshooting.

## Check the connection

1. Run the connection check in the API Key section;
2. Select a synced and enabled model;
3. Confirm that the check succeeds;
4. Run the health check in the model list;
5. Return to the chat interface and send a simple message;
6. Then enable Web Search and test a query that returns citations.

A successful connection check does not guarantee that search tools are available. Search also depends on the model's capabilities, account permissions, and tool billing status.

## Connect to a Grok-compatible gateway

If you are not using the official xAI API:

1. Create a [custom provider](zi-ding-yi-fu-wu-shang.md);
2. Select OpenAI Chat Completions or OpenAI Responses according to the gateway documentation;
3. Enter the Base URL and API Key supplied by the gateway;
4. Sync or manually add the models actually provided by the gateway;
5. Verify reasoning, tool calls, and Web Search separately.

A third-party gateway offering Grok models does not necessarily support xAI's official Web Search or X Search. Do not overwrite the official Grok template.

## Troubleshooting

### Response code 401

The API Key is invalid, revoked, or incomplete. Create a new key and ensure that it has no extra spaces.

### Response code 403

The team, region, model, or tool permissions do not meet the requirements. Check account and model access in the xAI Console.

### Response code 404 or model not found

Click **Add** again to sync the list, then verify the complete model ID. An older model may have been migrated, redirected, or discontinued.

### Response code 429

The current team or model has reached a rate limit. Reduce concurrency, try again later, and check limits and usage in the xAI Console.

### No citations after enabling Web Search

Confirm that Web Search is enabled in the input box and ask a question that clearly requires current information. If you use a third-party gateway, it may not support xAI's server-side search tools.

### Web Search costs more than expected

xAI may charge for both model tokens and server-side tool calls. Reduce unnecessary Web Search requests and verify actual usage in the xAI Console.

### Reasoning options do not match the documentation

Sync the models again and confirm that Cherry Studio is up to date. New xAI models may be released before their capability rules are added to the app; in that case, rely on the current interface and actual health checks.

For general configuration, see [Model Providers](README.md), [Web Search Mode](../../websearch/README.md), and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
