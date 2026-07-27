---
icon: bolt
---

# Groq

Groq is a model service platform known for low-latency inference, offering several open-weight models and the Groq Compound systems. Cherry Studio V2's built-in Groq template uses Groq's official OpenAI-compatible endpoint and can sync the models currently available to your account.

{% hint style="warning" %}
**Groq** and xAI's **Grok** are separate providers. Groq provides a model inference platform, while Grok is xAI's model family. Confirm that you selected the correct entry before configuring it.
{% endhint %}

## Before you begin

- An account that can sign in to the [GroqCloud Console](https://console.groq.com/);
- An API Key created under [Groq API Keys](https://console.groq.com/keys);
- Available credit and rate limits for the account;
- Confirmation that the models you plan to use are still available.

Groq's model catalog and life cycles change. Do not add a discontinued model solely because it appeared in older documentation.

## Configure Groq

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **Groq**;
3. Enter the Groq API Key;
4. Keep the default Base URL `https://api.groq.com/openai`;
5. Turn on the provider switch at the top of the page;
6. Click **Add** in the model list, review the sync preview, and apply the changes;
7. Enable the models you plan to use.

{% hint style="danger" %}
Do not include the API Key in chat messages, documents, code repositories, or issue screenshots. If exposed, revoke it immediately in the GroqCloud Console and create a new one.
{% endhint %}

## Sync and select models

After you click **Add**, Cherry Studio calls Groq's model list endpoint and displays the models accessible to the current key. Models change quickly, so refer to [Groq Supported Models](https://console.groq.com/docs/models) and the sync results.

Common types include:

| Type | Example model ID | Recommended use |
| --- | --- | --- |
| Lightweight text model | `llama-3.1-8b-instant` | Low-latency Q&A, classification, and simple extraction |
| Large general-purpose model | `openai/gpt-oss-120b` | Complex text, coding, and reasoning |
| Other hosted model | `qwen/qwen3.6-27b` | Multilingual work, structured output, and tool tasks |
| Compound system | `groq/compound`, `groq/compound-mini` | Groq server-side search and code execution |

- Enable only the models you actually need;
- Verify the complete model ID, including slashes and capitalization;
- Sync again after a model is discontinued instead of changing only its display name;
- The same model may have different rate limits under different plans;
- Audio, speech, or specialized models are not necessarily suitable for standard chat.

## Configure the Service Tier

In the Groq settings for a chat, you can select a **Service Tier**:

| Option | Meaning |
| --- | --- |
| Ignore | Do not send `service_tier`; Groq uses its default behavior |
| auto | Use an appropriate tier currently available to the account |
| on demand | Use standard on-demand processing |
| flex | Prioritize high throughput, but fail quickly if capacity is unavailable |

Whether a service tier takes effect depends on the current model, account plan, and Cherry Studio's capability detection. Keep **Ignore** or **auto** if you are unfamiliar with the differences.

{% hint style="info" %}
Flex processing may return `498 capacity_exceeded` when capacity is unavailable. It is suitable for retryable batch tasks, not interactive requests that must succeed on the first attempt.
{% endhint %}

## Use MCP and tool calls

Standard Groq-hosted models can use Cherry Studio's MCP or other tools according to their capabilities:

1. Select a model that supports tool calls;
2. Enable one simple MCP tool;
3. Send a request that clearly requires the tool;
4. Confirm that the model actually calls the tool;
5. Then add parallel tools or complex parameters.

Groq Compound is a different mechanism:

- `groq/compound` can use multiple Groq server-side tools in one request;
- `groq/compound-mini` uses only one server-side tool per request and has lower latency;
- Groq servers perform search, web access, and code execution;
- Compound is not the same as Cherry Studio MCP and does not support passing user-defined tools directly to Compound.

If you need your own MCP tools, select a standard hosted model that supports local tool calls instead of treating Compound as an MCP executor.

## Check the connection

1. Run the connection check in the API Key section;
2. Select a synced and enabled text model;
3. Confirm that the check succeeds;
4. Run the health check in the model list;
5. Return to the chat interface and send a simple message;
6. If you use tools or Compound, test each corresponding capability separately.

A successful connection check confirms only that a basic request works. It does not mean every model has the same context, tool, or rate limits.

## Connect to a Groq-compatible gateway

If you are not using the official Groq API:

1. Create a [custom provider](zi-ding-yi-fu-wu-shang.md);
2. Set OpenAI Chat Completions as the primary endpoint;
3. Enter the Base URL and API Key supplied by the gateway;
4. Sync or manually add the models actually provided by the gateway;
5. Verify that tool calls and service tiers are supported.

Do not overwrite the official Groq template. A third-party gateway also does not automatically gain access to Groq Compound's server-side tools.

## Troubleshooting

### Response code 401

The API Key is invalid, revoked, or incomplete. Create a new key and ensure that it has no extra spaces.

### Response code 404 or model not found

The model has been discontinued, the model ID is incorrect, or the current account does not have access. Click **Add** again to sync the list.

### Response code 429

The request has reached the model or account rate limit. Reduce concurrency, try again later, and check limits in the GroqCloud Console.

### Response code 498

The flex tier currently has no available capacity. Switch to auto, on demand, or Ignore, or add backoff and retries to the task.

### The response is fast but truncated

Check the model's context and maximum output limits, then shorten the input or adjust the maximum output tokens. Inference speed does not change the model's own limits.

### Compound did not call my MCP tool

Compound uses Groq server-side tools and does not accept Cherry Studio's custom MCP tools. Use a hosted model that supports standard tool calls instead.

### The Service Tier does not change

The current model or account may not support the selected tier. Keep Ignore or auto, and rely on the actual request records in the GroqCloud Console.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
