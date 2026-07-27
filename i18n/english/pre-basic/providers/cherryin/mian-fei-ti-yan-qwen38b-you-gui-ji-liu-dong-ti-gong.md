---
icon: feather
---

# Qwen3-8B

Cherry Studio recognizes Qwen3-8B models from multiple providers. Some versions use `Qwen/Qwen3-8B` as an in-app trial model and direct its service entry point to CherryIN. Other providers may use the same or a different model ID.

{% hint style="warning" %}
A model appearing in the trial list does not mean it will remain free. Refer to the **Free** indicator in the model selector, the provider console, and actual request results.
{% endhint %}

## Check whether it is already available

1. Open the model selector on the Chats page;
2. Search for `Qwen3-8B`, or enable the **Free** tag;
3. Confirm which provider supplies the model;
4. Select the model and send a simple test message.

If CherryIN appears beside the trial indicator, select the indicator to open the corresponding provider settings. CherryAI itself does not appear in the regular Model Services list.

## Connect through a provider

If Qwen3-8B does not appear in the model selector:

1. Open `Settings → Model Services`;
2. Select ModelScope, OpenRouter, or another provider that offers the model for your account;
3. Enter the API Key and check the Base URL;
4. Select **Add** and apply the model changes;
5. Search for and enable Qwen3-8B;
6. Run a connection check or Model Health Check.

Some providers use `Qwen/Qwen3-8B`, while others use `qwen/qwen3-8b`. Letter case, namespaces, and suffixes can all affect routing.

## Add the model manually when it cannot be synced

If the provider does not offer a model-list API, select **Custom** and copy the complete model ID from the provider console or API documentation.

{% hint style="danger" %}
Do not copy a model ID directly from another platform. Even when names match, providers may use different namespaces, capability settings, or API paths.
{% endhint %}

## Reasoning and tool calling

The Qwen3 family may support controllable reasoning. Depending on provider capabilities, Cherry Studio uses the `enable_thinking` parameter or a compatible method for controlling thinking mode on APIs that do not support the parameter.

Recommendations:

- Rely on thinking settings only when the model selector shows Reasoning capability;
- Before using MCP or other tools, confirm the Tool capability tag and complete a simple test;
- Do not hard-code `/think` or `/no_think` into every prompt. Prefer Cherry Studio's thinking settings;
- When multiple providers offer a model with the same name, test reasoning and tool calling separately for each.

## Troubleshooting

### Qwen3-8B does not appear under the Free filter

The trial model may not be available in your current version or region. You can still configure a provider that supports it and use your own API Key.

### Selecting the trial indicator opens CherryIN

This is expected. V2 maps the service entry point for specific Qwen trial models to CherryIN so users can configure the service after their trial quota is exhausted.

### Thinking mode does not change

Check whether the provider supports `enable_thinking` and whether the current model is a variant with switchable reasoning. Some endpoints ignore unsupported parameters.

### The provider returns “model not found”

Check the letter case and complete model ID, then sync the list again. If you added the entry manually, replace it with the ID supplied by the current provider.

For general free-trial rules, see [CherryAI (Free Trial)](README.md). For the provider setup process, see [Model Services](../README.md).
