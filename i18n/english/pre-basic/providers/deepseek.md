---
icon: whale
---

# DeepSeek

Cherry Studio V2's built-in DeepSeek template connects to the official DeepSeek API. The template currently uses **OpenAI Chat Completions** by default, also includes DeepSeek's official Anthropic-compatible endpoint, and adapts the thinking switch and reasoning effort for DeepSeek V4.

{% hint style="info" %}
If you only want to try the models first, use the built-in [CherryAI free trial](cherryin/README.md). This page is for users who already have an official DeepSeek API Key.
{% endhint %}

## Before you begin

- An account that can sign in to the [DeepSeek Platform](https://platform.deepseek.com/);
- An API Key created under [API Keys](https://platform.deepseek.com/api_keys);
- Available balance or quota on the account;
- Confirmation of the currently available models and official API changes.

Signing in to the DeepSeek website or app does not automatically sign you in through Cherry Studio. Calling the official API requires a separate API Key.

## Configure DeepSeek

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **deepseek**;
3. Enter the DeepSeek API Key;
4. Keep the default Base URL `https://api.deepseek.com`;
5. Turn on the provider switch at the top of the page;
6. Click **Add** in the model list, review the sync preview, and apply the changes;
7. Enable the models you plan to use.

{% hint style="danger" %}
Do not include the API Key in chat messages, documents, code repositories, or issue screenshots. If exposed, delete the key immediately on the DeepSeek Platform and create a new one.
{% endhint %}

## Choose a current model

DeepSeek currently provides the following primary model IDs:

| Model ID | Recommended use |
| --- | --- |
| `deepseek-v4-flash` | Everyday chat, quick tasks, and latency-sensitive work |
| `deepseek-v4-pro` | Complex reasoning, coding, long context, and Agent tasks |

The legacy model aliases `deepseek-chat` and `deepseek-reasoner` were discontinued in July 2026. If an old configuration returns model not found, click **Add** again to sync the list and use a current V4 model ID.

{% hint style="warning" %}
The model list and life cycles may continue to change. Refer to the [DeepSeek API documentation](https://api-docs.deepseek.com/) and actual sync results instead of relying on fixed model names in old screenshots.
{% endhint %}

## Configure thinking mode

DeepSeek V4 supports both thinking and non-thinking modes, with thinking enabled by default. Cherry Studio displays the applicable options under the thinking button in the input box:

- **Default**: Use the provider's default behavior;
- **Off**: Send the parameter that disables thinking;
- **High**: Use DeepSeek's `high` reasoning effort;
- **Extra High**: Map to DeepSeek's `max` reasoning effort.

`Extra High` generally uses more reasoning time and tokens. Start with Default or Off for everyday questions, and increase the effort for complex code, planning, and Agent tasks.

Some sampling parameters may not take effect in thinking mode. If results differ, keep the default parameters and adjust only the thinking switch and effort.

## Tool calls and Agent

DeepSeek V4 supports tool calls in thinking mode, and Cherry Studio preserves the thinking content required during the tool-call process. You should still test the behavior:

1. Enable one simple MCP tool;
2. Select `deepseek-v4-pro` or `deepseek-v4-flash`;
3. Start with the default thinking effort;
4. Send a request that clearly requires a tool;
5. Confirm that the model actually calls the tool instead of only describing a call plan.

If consecutive tool calls return 400, update Cherry Studio and the model list first, then verify that the gateway is actually an official DeepSeek endpoint.

## Check the connection

1. Run the connection check in the API Key section;
2. Select a synced and enabled V4 model;
3. Confirm that the check succeeds;
4. Run the health check in the model list;
5. Return to the chat interface and send a simple message;
6. Test thinking mode and tool calls separately.

A successful connection check does not mean the account has unlimited quota or that every model is available.

## Knowledge bases and embedding models

The built-in DeepSeek template currently configures only a chat endpoint and does not provide embedding models. When using [Global Memory](../../advanced-basic/memory.md) or a knowledge base:

- You can continue to use DeepSeek as the chat model;
- Select the embedding model from another provider;
- The embedding and chat models do not need to come from the same provider;
- Run a model health check for each after configuration.

## Connect to a DeepSeek-compatible gateway

If you are not using the official DeepSeek API:

1. Create a [custom provider](zi-ding-yi-fu-wu-shang.md);
2. Select OpenAI Chat Completions or Anthropic Messages according to the gateway documentation;
3. Enter the Base URL and API Key supplied by the gateway;
4. Sync or manually add the model IDs actually provided by the gateway;
5. Verify that the gateway fully supports the thinking parameters and tool calls.

Do not overwrite the official DeepSeek template directly. A separate provider makes it easier to distinguish official accounts, third-party model names, and protocol differences.

## Troubleshooting

### Response code 401

The API Key is invalid, deleted, or incomplete. Create a new key and ensure that it has no extra spaces.

### Balance or quota error

Check the balance, usage, and account status on the DeepSeek Platform. Switching models does not bypass account-level limits.

### Response code 404 or model not found

Click **Add** again to sync models, and confirm that you are using `deepseek-v4-flash` or `deepseek-v4-pro`. The legacy aliases are no longer available.

### Response code 429 or server busy

The current request has reached a rate limit, or the service is temporarily congested. Try again later, reduce concurrency, or check account limits.

### The thinking button does not show all options

Confirm that the model ID is a current V4 ID, then sync models again. Do not change the model ID when adding it manually; you can customize the display name.

### Tool calls produce only text

Confirm that the model supports tool calls, MCP is enabled, and you are using the official DeepSeek endpoint or a gateway that explicitly supports the complete tool protocol. Troubleshoot with one simple tool first.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
