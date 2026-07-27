---
icon: key
---

# Anthropic

Cherry Studio V2's built-in Anthropic template connects to the official Anthropic API and uses the **Anthropic Messages** endpoint by default. After configuring an API Key, you can sync Claude models and use them for chat, reasoning, and tool calling.

{% hint style="info" %}
A provider having an Anthropic endpoint does not mean every model from that provider supports tool calling or Agent. Review the model capability tags and complete an actual tool test before use.
{% endhint %}

## Before you begin

- An account that can use the Anthropic API;
- An API Key created under [Anthropic API Keys](https://console.anthropic.com/settings/keys);
- Models enabled for the account and available quota;
- A network environment that meets Anthropic's latest account and regional requirements.

An Anthropic API Key and your login state on the website are separate configurations. Cherry Studio requires a Key that can be used for API requests.

## Configure Anthropic

1. Open `Settings → Model Services`;
2. Switch the filter on the left to **All Providers** and select **Anthropic**;
3. Enter the API Key;
4. Keep the default Base URL, `https://api.anthropic.com`;
5. Turn on the provider switch at the top of the page;
6. Select **Add** in the model list, review the sync preview, and apply the changes;
7. Enable the Claude models you plan to use.

{% hint style="danger" %}
Do not include an API Key in chat messages, documentation, code repositories, or issue screenshots. If a Key is exposed, revoke it immediately in the Anthropic Console and create a new one.
{% endhint %}

## Sync and select models

Anthropic model names and versions change, so this page does not specify a fixed list. Select **Add** to sync the models currently available to your account and verify the complete model IDs.

- Enable only the models you actually need;
- Different versions in the same family may have different context, reasoning, and tool capabilities;
- If the API does not return a model, select **Custom** and enter a model ID from the official Anthropic documentation;
- Do not add a model ID from a third-party gateway directly to the official Anthropic template.

A model appearing in the Cherry Studio registry does not mean your Anthropic account has access to it.

## Check the connection

1. Start a connection check in the API Key area;
2. Choose a synced and enabled model;
3. Confirm that the check succeeds;
4. Run Health Check in the model list;
5. Return to the Chats page and send a simple message.

If you plan to use MCP or Agent, also enable one simple tool and verify that the model actually initiates a call.

## Agent and tool calling

The Anthropic template appears under the **Agent Supported** filter in Model Services because it has an Anthropic-compatible endpoint. You must still meet all of the following conditions:

- The target model has tool-calling capability;
- The current API endpoint enables tool calling;
- MCP or other tools are enabled correctly;
- The Assistant has not disabled tools;
- Provider permissions or security policies do not block the request.

If the model outputs only a tool-call plan without executing it, troubleshoot with one simple tool first, then check the model capabilities and endpoint.

## Prompt Cache

You can configure Prompt Cache for the Anthropic endpoint under **API Settings** in Cherry Studio:

- **Cache Token Threshold**: Enables caching only when messages exceed this amount; set it to `0` to disable caching;
- **Cache System Message**: Determines whether to cache the system prompt;
- **Cache Last N Messages**: Controls how many recent conversation messages are cached.

{% hint style="warning" %}
The provider determines whether caching takes effect, how it is billed, and which models support it. Keep the defaults when you do not understand the provider's rules; incorrect configuration does not necessarily reduce costs.
{% endhint %}

## Connect to an Anthropic-compatible gateway

If you are not using the official Anthropic API:

1. Right-click Anthropic in the provider list on the left;
2. Choose to duplicate it or add another provider of the same type;
3. Enter the Base URL and API Key supplied by the gateway for the copy;
4. Keep Anthropic Messages as the primary endpoint;
5. Sync or manually add the models actually provided by the gateway.

Using a separate copy avoids overwriting the official Anthropic template and makes it easier to troubleshoot endpoints and permissions separately.

## Troubleshooting

### The provider returns 401

The API Key is invalid, revoked, or incomplete. Create a new Key and make sure it contains no extra spaces.

### The provider returns 403

The account, region, workspace, or model permissions may not meet the requirements. Check the account status in the Anthropic Console.

### The provider returns 404 or model not found

Select **Add** again to sync the list and verify the complete model ID. When using a third-party gateway, confirm that the Base URL and Anthropic Messages path match the gateway documentation.

### The model does not appear under the Agent filter

The Agent filter checks whether the provider has an Anthropic endpoint. A custom gateway must have its Anthropic Messages endpoint configured correctly, and the model itself must also support tool calling.

### Prompt Cache has no effect

Confirm that the cache threshold is greater than `0` and that the provider and model support caching. Short conversations may not reach the configured threshold.

For general settings, see [Model Services](README.md) and [Model Services settings](../../cherrystudio/preview/settings/providers.md). See [Feedback and Suggestions](../../question-contact/suggestions.md) for contact options.
