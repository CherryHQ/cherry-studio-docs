---
icon: gauge
---

# Zhipu GLM-4.5-Air

Cherry Studio recognizes GLM-4.5-Air and its common variants from multiple providers. It identifies the standard model as a text reasoning and tool-calling model. Whether these capabilities are available still depends on the provider API and actual tests.

{% hint style="warning" %}
This page no longer promises that GLM-4.5-Air will always be a free trial model from CherryAI or CherryIN. Refer to the model selector, provider console, and actual request results to determine whether the model is free and still available.
{% endhint %}

## Check whether it is already available

1. Open the model selector on the Chats page;
2. Search for `GLM-4.5-Air`;
3. Confirm the model's provider and capability tags;
4. Select the model and send a simple test message.

If multiple entries have the same name, use the provider name and complete model ID to distinguish them.

## Connect through a provider

If GLM-4.5-Air does not appear in the model selector:

1. Open `Settings → Model Services`;
2. Select ZhiPu or an aggregation provider that offers the model for your account;
3. Enter the API Key and check the Base URL;
4. Select **Add** and apply the model changes;
5. Search for and enable GLM-4.5-Air;
6. Run a connection check or Model Health Check.

Cherry Studio's model registry contains GLM-4.5-Air identifiers used by multiple providers. These mappings identify models but do not mean your account has permission or free quota.

## Choose the correct variant

A provider may offer standard, AirX, FP8, or `free`-suffixed entries.

- Standard, AirX, and FP8 versions are different models or deployments;
- `free` only means that the provider marked the model ID as free; it does not mean the model will remain free permanently;
- Context, speed, tool calling, and reasoning controls for models with the same name may differ between endpoints;
- Do not copy a model ID directly from one provider to another.

{% hint style="danger" %}
Copy the model ID from the current provider's console or API documentation. Manually entering an ID that looks correct but is not supported results in 404 or “model not found.”
{% endhint %}

## Reasoning and tool calling

If the model selector shows Reasoning capability, you can use the thinking settings provided by Cherry Studio in a chat. Providers may control reasoning through parameters, model variants, or prompts. Cherry Studio selects the corresponding method based on the provider configuration.

To use MCP or another tool:

1. Confirm that the model has the Tool capability tag;
2. Enable a simple, verifiable tool first;
3. Send an explicit instruction and watch whether the model actually initiates a call;
4. If the model only outputs a call plan without executing it, check the provider endpoint and model capabilities.

## Troubleshooting

### The thinking switch is unavailable

The current provider or model variant may not support controllable reasoning. Sync the model again and check its capability tags. Do not judge by the model name alone.

### Tool-call formatting is invalid

Try a different provider endpoint or model variant. Aggregation gateways can differ in their compatibility with tool-calling parameters.

### The provider returns 401, 403, or insufficient balance

Check the API Key, model permissions, account balance, and regional restrictions. When trial quota is exhausted, configure your own credentials or switch models.

### The model ID does not exist

Delete the incorrect manually added entry and sync the list again, or use the complete model ID from the provider documentation.

For general free-trial rules, see [CherryAI (Free Trial)](README.md). For the provider setup process, see [Model Services](../README.md).
