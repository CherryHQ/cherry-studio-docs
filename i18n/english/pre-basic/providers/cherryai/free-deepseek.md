---
icon: brain
---

# DeepSeek V3.2

Cherry Studio recognizes DeepSeek V3.2 and its common variants from multiple providers. Whether a model is free, remains available, and which model ID it uses depends on your provider.

{% hint style="warning" %}
This page no longer promises that DeepSeek V3.2 will always be a free trial model from CherryAI or CherryIN. Refer to the **Free** indicator in the model selector, the provider console, and actual request results.
{% endhint %}

## Check whether it is already available

1. Open the model selector on the Chats page;
2. Search for `DeepSeek V3.2`;
3. If you find the model, confirm which provider supplies it;
4. Select the model and send a simple test message.

Multiple providers may offer the same model, and its display name and API model ID may differ. Before selecting it, check your account quota, regional availability, and the provider's pricing rules.

## Connect through a provider

If DeepSeek V3.2 does not appear in the model selector:

1. Open `Settings → Model Services`;
2. Select the official [DeepSeek](../deepseek.md) service or an aggregation provider that offers the model for your account;
3. Enter the API Key and check the Base URL;
4. Select **Add** and apply the model changes in the sync preview;
5. Search for DeepSeek V3.2 and turn on the target model;
6. Run a connection check or Model Health Check.

Cherry Studio's model registry contains DeepSeek V3.2 identifiers used by multiple providers. These identifiers are only used to recognize model capabilities and do not mean every provider account can call the model.

## Add the model manually when it cannot be synchronized

Some gateways do not provide a model-list API. In this case, select **Custom** and enter the model ID from the provider console exactly as shown.

Common names may include:

- `deepseek-v3.2`
- `deepseek/deepseek-v3.2`
- Variants with a date, `thinking`, `exp`, or `speciale` suffix

{% hint style="danger" %}
Do not guess a model ID from this page. IDs, capabilities, and routes differ between providers. You must copy the actual value from the provider console or API documentation.
{% endhint %}

## Use it in a chat

The DeepSeek V3.2 family is suitable for tasks such as code, long-text analysis, and multi-step reasoning. Recommendations:

- Enable the model's reasoning capability for complex tasks; avoid unnecessary reasoning overhead for simple questions;
- Before calling MCP or other tools, confirm that the model has the tool-calling capability tag and complete a test;
- If a long conversation reaches context or output limits, create a new topic or attach fewer files;
- Review important results yourself instead of using model output directly as a final decision.

Capabilities vary between model variants. For example, a reasoning variant with a special suffix may not support tool calling. Refer to the capabilities displayed in Cherry Studio and to actual tests.

## Troubleshooting

### The model appears in search but cannot be selected

Make sure both the provider and model are enabled. If the model comes from an old configuration, fetch the list again and recheck it.

### The provider returns 401, 403, or insufficient balance

Check the API Key, account permissions, balance, and regional restrictions. After trial quota is exhausted, switch providers or configure your own API Key.

### The provider returns “model not found”

The model ID usually does not match the provider. Delete the incorrect entry and fetch the list again, or copy the full ID from the provider documentation and add it manually.

### Tools are unavailable

A provider offering a model with the same name does not guarantee that its endpoint supports tool calling. Check the model's capability tags and, if necessary, switch to a variant or provider that supports tool calling.

For general free-trial rules, see [CherryAI (Free Trial)](../cherryin/README.md). For the provider setup process, see [Model Services](../README.md).
