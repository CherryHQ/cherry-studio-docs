---
icon: moon
---

# Moonshot AI (Kimi)

Cherry Studio V2's built-in Moonshot AI template connects to the Kimi API Platform. The template uses OpenAI Chat Completions by default and also provides Moonshot's Anthropic-compatible endpoint.

Current Kimi models cover general chat, long-horizon coding, vision understanding, Agent scenarios, and more. Different model generations use different thinking parameters, so confirm the model ID before selecting a thinking option in Cherry Studio.

{% hint style="info" %}
The Kimi website, Kimi membership, Kimi Code, and the Kimi API Platform are separate products. Signing in to the website or a membership does not automatically sign you in through Cherry Studio. Calls through Cherry Studio require a separate API Key and are billed according to the API Platform rules.
{% endhint %}

## Before you begin

- An account that can sign in to the [Kimi API Platform](https://platform.kimi.com/);
- An API Key created under [API Keys](https://platform.moonshot.cn/console/api-keys);
- Sufficient balance and access permission for the target model;
- Review of the current [model list](https://platform.kimi.com/docs/models) and parameter limits.

We recommend creating a separate key for Cherry Studio to make usage and permission revocation easier to distinguish.

## Configure Moonshot AI

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **Moonshot**;
3. Enter the Kimi API Key;
4. Keep the default Base URL `https://api.moonshot.cn`;
5. Turn on the provider switch at the top of the page;
6. Click **Add** in the model list, review the sync preview, and apply the changes;
7. Enable only the models you plan to use.

{% hint style="danger" %}
Do not include the API Key in chat messages, documents, code repositories, or issue screenshots. If the key is exposed, delete it immediately on the API Platform and create a new one.
{% endhint %}

The official SDK documentation usually shows `https://api.moonshot.cn/v1`. The Cherry Studio template handles the endpoint path, so keep the default address shown on the page when using the built-in template. Do not append the request path again.

## Select a model

Use the actual synced list as the source of truth. The current primary models can be selected as follows:

| Model ID | Primary use | Cherry Studio guidance |
| --- | --- | --- |
| `kimi-k3` | Flagship general model with 1M context for long-horizon coding, knowledge work, and complex reasoning | In the current V2 version, keep thinking set to **Default** |
| `kimi-k2.7-code` | Coding and Agent model with 256K context | Always thinks; keep **Default** |
| `kimi-k2.7-code-highspeed` | Same family as K2.7 Code with faster output | Availability may fluctuate when resources are busy |
| `kimi-k2.6` | 256K context for general chat, vision, and Agent tasks | Use the default thinking behavior or disable it when needed |

Kimi K3, K2.7 Code, and K2.6 officially support text, image, and video input. The exact attachment controls also depend on whether the current Cherry Studio version recognizes the model's capabilities correctly.

Model names, access requirements, and life cycles change. Do not manually enter a model ID based only on an old screenshot. Click **Add** again to sync the list first, and refer to the official Kimi documentation.

## Configure thinking mode

Different Kimi model families use different reasoning parameters:

- Kimi K3 always thinks and uses top-level `reasoning_effort` with `low`, `high`, or `max`; the default is `max`;
- Kimi K2.7 Code always thinks and cannot be disabled;
- Kimi K2.6 uses `thinking` to enable or disable thinking.

{% hint style="warning" %}
The current Cherry Studio V2 version identifies Kimi K2.5 and newer models as Kimi thinking models and sends the `thinking` parameter for any non-default option. Kimi K3 uses `reasoning_effort`, while K2.7 Code does not allow thinking to be disabled. Therefore, keep **Default** when using K3 or K2.7 Code to avoid a 400 response caused by incompatible parameters.
{% endhint %}

The Low, High, and Maximum reasoning efforts for Kimi K3 may not yet appear completely in Cherry Studio's thinking menu. When kept at Default, K3 uses the provider's default `max`. If precise effort control is required, wait for the corresponding Cherry Studio adaptation.

When using K2.6:

- **Default**: Do not override the provider's default behavior;
- **Off**: Send the parameter that disables thinking;
- **Auto**: The current V2 version sends the parameter that enables thinking.

K2.5 and newer models have fixed or restricted sampling parameters. If a parameter error occurs, first restore Temperature, Top P, and penalty settings to their defaults.

## Use images, videos, and files

Confirm the official model capabilities and the client's current detection separately:

1. Sync the model list again;
2. Select the target model;
3. Check whether image or file controls appear in the input box;
4. Upload a standard image first for a health test;
5. Then test a video or large attachment.

The current V2 version can automatically recognize the vision capability of K2.6. K3 and K2.7 Code have newer official capabilities, so the current version may not show all vision indicators yet. If the attachment control does not appear, update Cherry Studio and the model list first. If it is still unavailable, use `kimi-k2.6` temporarily instead of forcing unsupported content to be sent as text.

For PDFs, the built-in Moonshot template does not currently use Kimi's native file upload endpoint directly. Cherry Studio extracts PDF text locally first and then sends the text to the model:

- Text-based PDFs can usually be processed directly;
- Scanned documents may require OCR first;
- Tables, complex layouts, and image information may be lost during extraction;
- The extracted text consumes model input tokens.

## Tool calls and MCP

Official Kimi models support tool calls, but whether Cherry Studio displays MCP capabilities also depends on model capability detection.

We recommend validating in this order:

1. Complete a standard chat first;
2. Enable one simple MCP tool;
3. Use a prompt that explicitly requires a tool call;
4. Confirm that the model actually makes the call;
5. Then add multiple tools or a long-running workflow.

The current V2 version includes tool detection rules for the Kimi K2 family, but automatic detection for K3 and K2.7 Code may lag behind the official model release. If the MCP control is missing, update Cherry Studio first. If the model is still not recognized, temporarily use a model recognized by the current version to complete the task.

When MCP returns an image, audio, or resource with a large amount of binary data, Cherry Studio converts the result into a text summary to prevent base64 content from exceeding the Kimi request size limit. The model can then read the text description of the tool result, but it cannot directly analyze the original media that was replaced.

## Knowledge bases and embedding models

The built-in Moonshot AI template currently configures chat endpoints and does not provide an embedding model. When using a knowledge base or [Global Memory](../../advanced-basic/memory.md):

- You can continue to use Kimi as the chat model;
- Select the embedding model from another provider;
- The chat and embedding models do not need to come from the same provider;
- Run a model health check for each after configuration.

## Check the connection

1. Run the connection check in the API Key section;
2. Select a synced and enabled model;
3. Confirm that the check succeeds;
4. Run the health check in the model list;
5. Return to the chat interface and send a simple message;
6. Test thinking, attachments, and MCP separately.

A successful connection check confirms only that the basic credentials work. It does not mean the account has access to every model or that the current client recognizes every model capability.

## Troubleshooting

### Response code 401

The API Key is invalid, deleted, or incomplete. Create a new key and ensure that it has no extra spaces.

### Balance or access requirement error

Check the API Platform balance, account tier, and access requirements for the target model. A Kimi website membership balance cannot replace API balance.

### Response code 404 or model not found

The model ID has changed, the model was discontinued, or the account does not yet have access. Click **Add** again to sync the list, then verify it in the [model list](https://platform.kimi.com/docs/models).

### Response code 400 or invalid `thinking` parameter

If you use Kimi K3 or K2.7 Code, change the thinking option to **Default** and restore Temperature, Top P, and other parameters to their defaults. K3 does not accept the `thinking` switch used by K2.6.

### Response code 429 or request busy

The account has reached a concurrency, RPM, TPM, or TPD limit, or resources for a high-speed model are temporarily busy. Reduce concurrency, shorten the context, or try again later.

### No image, video, or MCP controls for K3 or K2.7 Code

This means the official model capabilities and the current Cherry Studio automatic detection rules are not yet synchronized. Update Cherry Studio and sync the models again. If the controls are still missing, use K2.6 temporarily and wait for the client adaptation.

### Incomplete PDF content recognition

Confirm whether the PDF is scanned. Run OCR first, or convert key pages to images and use a Kimi model that Cherry Studio recognizes as a vision model.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). See the [model parameter reference](https://platform.kimi.com/docs/api/models-overview) for Kimi parameter differences; for feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
