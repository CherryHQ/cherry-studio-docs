---
icon: key
---

# OpenAI

Cherry Studio V2's built-in OpenAI template connects to the official OpenAI API and uses the **OpenAI Responses** API by default. After preparing an OpenAI API Key, you can sync the models available to your account and use them in chats.

{% hint style="warning" %}
The OpenAI template is no longer used for third-party OpenAI-compatible gateways. If your Base URL is not an official OpenAI URL, create a [Custom Provider](zi-ding-yi-fu-wu-shang.md) and select OpenAI Chat Completions or OpenAI Responses as required by the gateway.
{% endhint %}

## Before you begin

- An account that can access the OpenAI API;
- An API Key created under [OpenAI API Keys](https://platform.openai.com/api-keys);
- Models enabled for the API account and available quota;
- A network environment that meets OpenAI's latest regional and account requirements.

Your login state in the ChatGPT website or client is not automatically imported into Cherry Studio. Cherry Studio requires an API Key to call the OpenAI API.

## Configure OpenAI

1. Open `Settings → Model Services`;
2. Switch the filter on the left to **All Providers** and select **OpenAI**;
3. Enter the API Key;
4. Keep the default Base URL, `https://api.openai.com`;
5. Turn on the provider switch at the top of the page;
6. Select **Add** in the model list, review the sync preview, and apply the changes;
7. Enable the models you plan to use.

{% hint style="danger" %}
An API Key is displayed in full only when it is created. Do not include it in chat messages, documentation, code repositories, or issue screenshots. If a Key is exposed, revoke it immediately in the OpenAI console and create a new one.
{% endhint %}

## Why Responses is the default

V2 presets the `openai-responses` endpoint for the OpenAI template. This template targets OpenAI's current official API, and the app handles text, reasoning, tool-calling, and other requests based on model capabilities.

If a third-party gateway supports only `/v1/chat/completions`:

1. Do not modify the built-in OpenAI template to connect to it;
2. Select `+` beside the provider-list search box;
3. Create a custom provider;
4. Set OpenAI Chat Completions as the primary endpoint;
5. Enter the Base URL, API Key, and model ID supplied by the gateway.

This preserves the official OpenAI template and prevents protocol mismatches between Responses and Chat Completions.

## Sync and enable models

After you select **Add**, Cherry Studio syncs the model list from the provider and displays added, updated, and removed entries before applying them.

- Enable only the models you actually need to keep the model selector concise;
- When multiple versions share a name, verify the complete model ID;
- If the API does not return a model, select **Custom** and manually enter the official model ID;
- Do not add model IDs from another gateway directly to the official OpenAI template.

Model availability depends on OpenAI account permissions. Cherry Studio recognizing a model does not mean your account has access to it.

## Check the connection

1. Select the connection check in the API Key area;
2. Choose a synced and enabled model;
3. Confirm that the check succeeds;
4. Then run Model Health Check;
5. Return to the Chats page and send a simple message.

If you use a reasoning or tool-calling model, test the thinking settings and tool calling separately. Do not judge capabilities by the model name alone.

## Optional settings

The OpenAI template supports request options such as Service Tier. **Service Tier** may appear in the model settings at the top of a chat; leave it set to **Auto** by default.

Select a different tier only when you understand how OpenAI supports and bills it for the corresponding model. Do not change capability switches in provider request settings without a clear reason; incorrectly declaring support can cause requests to fail.

## Troubleshooting

### The page says that old calling methods are no longer supported

This is a V2 notice for the built-in OpenAI template. Use the current template for the official OpenAI API. Create a custom provider for third-party compatible APIs.

### The provider returns 401

The API Key is invalid, revoked, or incomplete. Create a new Key and make sure it contains no extra spaces.

### The provider returns 403

The account, region, organization, or model permissions may not meet the requirements. Check the account status and model access in the OpenAI console.

### The provider reports a balance or quota error

Check the API account's quota, billing status, and usage limits. Switching models does not bypass account-level limits.

### The provider returns 404 or model not found

Select **Add** again to sync the list and verify the model ID. If you are connecting to a third-party gateway, use a custom provider and choose the correct endpoint.

### The model can chat but cannot call tools

Check the model capability tags and OpenAI's tool support for that model. Test with one simple tool first, then add MCP or other tools gradually.

For general settings, see [Model Services](README.md) and [Model Services settings](../../cherrystudio/preview/settings/providers.md). See [Feedback and Suggestions](../../question-contact/suggestions.md) for contact options.
