---
icon: route
---

# OpenRouter

OpenRouter is a unified gateway for multiple models. Cherry Studio V2's built-in OpenRouter template uses one set of API Keys to sync OpenRouter chat and embedding models, with adaptations for reasoning content, the Web Search plugin, and model capabilities.

{% hint style="warning" %}
OpenRouter is not the original model provider. Requests pass through OpenRouter and may be routed among multiple upstream inference providers. Before using sensitive data, check the privacy, logging, and provider routing policies in the OpenRouter console.
{% endhint %}

## Before you begin

- An account that can sign in to [OpenRouter](https://openrouter.ai/);
- An API Key created under [OpenRouter Keys](https://openrouter.ai/settings/keys);
- Available balance or free-model quota on the account;
- Confirmation of the model's price, context, tools, and data policy.

We recommend creating a separate key for Cherry Studio and setting an appropriate spending limit in OpenRouter. This makes usage easier to distinguish and reduces the risk if the key is exposed.

## Configure OpenRouter

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **OpenRouter**;
3. Enter the OpenRouter API Key;
4. Keep the default Base URL `https://openrouter.ai/api/v1/`;
5. Turn on the provider switch at the top of the page;
6. Click **Add** in the model list, review the sync preview, and apply the changes;
7. Enable only the models you plan to use.

{% hint style="danger" %}
Do not include the API Key in chat messages, documents, code repositories, or issue screenshots. If exposed, revoke it immediately in OpenRouter and create a new one.
{% endhint %}

## Understand model IDs

OpenRouter model IDs usually use the `<organization>/<model>` format. For example:

| Type | Example |
| --- | --- |
| Fixed model | `openai/gpt-oss-120b` |
| Provider's latest alias | `~anthropic/claude-sonnet-latest` |
| Automatic routing | `openrouter/auto` |
| Free routing | `openrouter/free` |
| Free variant | Append `:free` to a specific model ID |

- The complete model ID determines the upstream model and routing behavior;
- The actual model behind `latest`, automatic routing, and free routing may change;
- For reproducible results, select a fixed version instead of a dynamic alias;
- Free variants may have rate, availability, or data policy restrictions;
- Do not judge price and capabilities from the display name alone.

Clicking **Add** syncs the current models; you do not need to enable hundreds of them. Keep only the small set your team actually uses to make the model selector easier to navigate.

## Chat and embedding models

Cherry Studio requests OpenRouter's chat and embedding model endpoints separately and merges them into the synced results.

- Chat models can be used for assistants, translation, and standard chat;
- Models that support tool calls can be used for MCP or Agent scenarios;
- Embedding models can be used for knowledge bases and [Global Memory](../../advanced-basic/memory.md);
- The same key may have different permissions, prices, and restrictions for different models;
- A model appearing in the list does not guarantee that every upstream provider is available.

When selecting a model for a knowledge base, confirm that it is actually an embedding model instead of judging only from the provider name.

## Configure thinking mode

OpenRouter normalizes the reasoning parameters of different models into a `reasoning` configuration. Cherry Studio sends disabled, effort, or budget settings according to model capabilities and preserves the reasoning content needed for tool calls across turns.

- Selecting **Default** attempts to use the OpenRouter or upstream default behavior;
- Selecting **Off** sends disabled reasoning to supported models;
- Low, Medium, High, and similar options take effect only on models that support the corresponding effort;
- Reasoning tokens usually count toward output usage;
- Some models do not return visible thinking content.

It is normal for the thinking button options to change after switching models. Do not apply one model's reasoning configuration directly to every model.

## Use Web Search

After you enable **Web Search** in the chat input box, Cherry Studio V2 currently adds the Web Search plugin to OpenRouter requests and passes the maximum result count from the Web Search settings.

To use it:

1. Select an OpenRouter model;
2. Enable **Web Search** in the input box;
3. Ask a question that requires current information from the web;
4. Wait for the search and model response;
5. Expand and verify the citations.

{% hint style="info" %}
OpenRouter Web Search incurs additional search charges, even when the underlying model is a free variant. OpenRouter is migrating from its legacy Web plugin to server-side search tools. If Web Search suddenly stops working, update Cherry Studio first and review the latest OpenRouter documentation.
{% endhint %}

Models with built-in search, such as Perplexity Sonar or OpenAI Search, may behave differently. Whether the model always searches is also determined by OpenRouter and upstream capabilities.

## Tool calls and Agent

The built-in OpenRouter template includes OpenAI Chat Completions and Anthropic Messages endpoints, but actual tool capabilities still depend on the model and upstream route.

Before use:

1. Select a model explicitly marked as supporting tool calls;
2. Run a standard chat health check;
3. Enable one simple MCP tool;
4. Confirm that the model actually makes a call;
5. Then add multiple tools or a long-running Agent workflow.

If Agent stability is unsatisfactory, compare direct connections to the original model provider, Anthropic, or CherryIN. OpenRouter's unified entry point is convenient, but upstream routing adds another variable.

## Privacy and upstream routing

OpenRouter routes among available upstream providers by default to improve availability. Cherry Studio does not currently configure every OpenRouter provider routing and privacy field for you.

Check the following in the OpenRouter console:

- Whether input and output logging is enabled;
- Whether OpenRouter is allowed to use inputs and outputs;
- Whether upstream providers that may retain data are restricted;
- Whether Zero Data Retention is required;
- Whether fallback is allowed;
- Model and spending limits for the organization or key.

These settings are part of your OpenRouter account policy and do not change automatically because Cherry Studio is a local client.

## Check the connection

1. Run the connection check in the API Key section;
2. Select a synced and enabled model;
3. Confirm that the check succeeds;
4. Run the health check in the model list;
5. Return to the chat interface and send a simple message;
6. Test reasoning, Web Search, and tool calls separately.

A successful connection check confirms only that the basic credentials work. A specific model may still fail because of balance, an upstream outage, privacy policy, or incompatible parameters.

## Troubleshooting

### Response code 401

The API Key is invalid, revoked, or incomplete. Create a new key and ensure that it has no extra spaces.

### Balance or spending limit error

Check the OpenRouter balance, key limit, and organization policy. Free models may also have separate rate limits.

### Response code 404 or model not found

The model ID has changed, the model was removed, or a dynamic alias is currently unavailable. Click **Add** again to sync the list, then verify it under [OpenRouter Models](https://openrouter.ai/models).

### Response code 429

The current model, upstream provider, or key has reached a rate limit. Reduce concurrency, try again later, or select another available route.

### Results or pricing change for the same model

A dynamic alias, automatic route, or upstream fallback may select a different version or provider. Use a fixed model ID for stable behavior, and restrict routing in the OpenRouter console.

### Web Search has no citations

Confirm that Web Search is enabled in the input box and that OpenRouter search remains compatible with the current Cherry Studio version. The search plugin and a model's built-in search are different mechanisms.

### Tool calls are unstable

Confirm that the model page indicates tool support and that the upstream supports every parameter in the request. You can use a fixed provider route or compare it with a direct connection to the original model provider.

For general configuration, see [Model Providers](README.md), [Web Search Mode](../../websearch/README.md), and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
