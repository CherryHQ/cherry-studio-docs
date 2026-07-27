# Volcengine (Ark / Doubao)

Volcengine Ark is Volcengine's large-model service platform, providing Doubao and models from several third-party providers. The built-in provider ID in Cherry Studio V2 is `doubao`, and the interface may display it as **Doubao**, **豆包**, or **Volcengine**.

Default API Host in V2:

```text
https://ark.cn-beijing.volces.com/api/v3/
```

{% hint style="info" %}
The current built-in V2 provider uses OpenAI-compatible Chat Completions by default. The Volcengine Ark website also provides the Responses API, Files API, and built-in cloud tools, but website support does not mean that Cherry Studio has automatically integrated these capabilities.
{% endhint %}

## Before You Begin

1. Register and sign in to Volcengine;
2. Open the Volcengine Ark console;
3. Confirm the project and region;
4. Activate the model or billing method you plan to use;
5. Create an API Key;
6. Copy the Model ID from the current model list;
7. Confirm the balance, allowances, and rate limits.

Volcengine Ark may adjust models, versions, prices, and availability. This page does not list fixed prices or promotional allowances. Use the [model list](https://www.volcengine.com/docs/82379/1554711) and console as the source of truth.

## Get an API Key

1. Open the [Volcengine Ark console](https://console.volcengine.com/ark/);
2. Confirm the current project and China (Beijing) region;
3. Open [API Key Management](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey);
4. Click **Create API Key**;
5. Enter a recognizable name;
6. Copy and store it securely.

{% hint style="danger" %}
An API Key is an account credential. Do not put it in chats, documents, code repositories, or troubleshooting screenshots. Delete or rotate it in the Ark console immediately if it is exposed.
{% endhint %}

## Get a Model ID

Volcengine Ark currently supports standard Model IDs and, in certain scenarios, custom inference Endpoint IDs.

| Identifier | Common format | Intended use |
| --- | --- | --- |
| Model ID | `doubao-seed-...` | Platform models called on a pay-as-you-go basis |
| Endpoint ID | `ep-...` | Custom models, dedicated resources, or created inference endpoints |

To get a current Model ID:

1. Open the [model list](https://www.volcengine.com/docs/82379/1554711);
2. Select the target model and version;
3. Confirm that it supports the Chat API;
4. Copy the complete Model ID;
5. Do not copy the model display name or console-page URL.

If your organization uses a custom model, model unit, or dedicated inference endpoint, copy its `ep-...` ID from [Inference Endpoints](https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint).

## Configure Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **Doubao / Volcengine**;
4. Paste the Ark Key into API Key;
5. Keep the API Host as `https://ark.cn-beijing.volces.com/api/v3/`;
6. Turn on the provider switch at the top of the page;
7. Click **Add Model**;
8. Paste the current Model ID or Endpoint ID;
9. Enable only the models you plan to use;
10. Run a model health check.

The V2 preset list includes some older Doubao, DeepSeek, and Embedding models. Presets are only candidates and do not mean that a model remains online.

## Synchronize or Add Manually

The Volcengine Ark model catalog and custom inference endpoints are not always fully returned through a standard OpenAI model list, so synchronization results may be empty or incomplete.

The most reliable method is to:

1. Copy the Model ID from the current Ark model page;
2. Add it manually in Cherry Studio;
3. Check the model capability labels;
4. Run a health check;
5. Delete older presets that cannot be called.

{% hint style="warning" %}
Do not continue using an older Model ID only because it remains visible in the V2 presets. Ark model versions commonly have date suffixes, and older versions may have been retired.
{% endhint %}

## API Host

Keep the default:

```text
https://ark.cn-beijing.volces.com/api/v3/
```

Cherry Studio appends request paths based on the model type. Older tutorials that put the complete `/chat/completions` path in the API Host and end it with `#` describe a legacy compatibility method; V2 does not require this configuration.

If you use a region other than Beijing, a proxy, or an enterprise-specific domain, replace the complete API Host and confirm that:

- The API Key belongs to the same project and region;
- The domain supports `/api/v3`;
- The proxy can forward streaming responses;
- The Model ID or Endpoint ID is valid in the target environment.

## Chat Models

The current built-in provider primarily uses OpenAI-compatible Chat Completions for chats.

Test in this order:

1. Send a short plain-text message;
2. Check streaming output;
3. Add a system prompt;
4. Test a longer context;
5. Then test images, reasoning, and tool calls.

New examples on the Volcengine Ark website may prioritize the Responses API. Do not assume that V2 chat has switched to the same API or supports all Responses-specific fields only because a Responses example works.

## Reasoning Mode

Different Doubao versions use different reasoning parameters. Cherry Studio V2 adapts them by Model ID:

- Newer Doubao Seed models use `reasoningEffort`;
- Certain older reasoning models use `thinking: enabled`;
- Older models with automatic reasoning can use `thinking: auto`;
- Other combinations may not send a reasoning field.

If changing the reasoning effort causes an error:

1. Restore the reasoning setting to **Default**;
2. Clear custom model parameters;
3. Confirm that the Model ID matches the current official version;
4. Review the Chat API example for that model;
5. Run the health check again.

Do not copy the `thinking` example from the Responses API directly to a Chat Completions model.

## Vision and Multimodal Models

Only models explicitly marked by Ark as vision or multimodal can receive images or video.

In Cherry Studio:

1. Add the current vision Model ID;
2. Confirm that the model shows image support;
3. Upload one small image first;
4. Check whether the model actually understands the content;
5. Then try multiple images or larger attachments.

The Ark website provides native file and video input capabilities, but whether the current V2 can use them directly depends on the client's attachment-format integration. Website support for an input type does not mean that Cherry Studio already uploads it through the Files API.

## MCP and Tool Calling

Cherry Studio MCP uses the model's structured Function Calling.

1. Complete a standard chat first;
2. Enable only one simple MCP tool;
3. Explicitly request a tool call;
4. Check whether it produces a structured call;
5. Confirm that the tool result can be returned to the model;
6. Add more tools afterward.

Volcengine Ark Web Search, Image Process, Knowledge Search, and Remote MCP are Ark cloud tools configured primarily through the Responses API. They are not the same configuration as MCP servers added in Cherry Studio.

A model saying that it will call a tool is not an actual call. Check the Model ID, API, and tool definitions.

## Embedding and Knowledge Bases

Volcengine Ark provides text and multimodal vectorization APIs. The V2 presets may retain older Embedding Model IDs, but prefer the versions listed in the current Ark documentation.

When creating a knowledge base:

1. Copy a Model ID from the current Ark vectorization model page;
2. Add it manually in Cherry Studio;
3. Confirm that it is recognized as Embedding;
4. Detect its vector dimensions;
5. Run a health check;
6. Import a small number of documents as a test;
7. Import in bulk afterward.

The input format accepted by a multimodal vectorization model may differ from the text chunks currently used by Cherry Studio knowledge bases. Verify plain-text Embedding first when using one for a document knowledge base.

Do not directly change an Embedding model or vector dimension after using it in an existing knowledge base. Doing so usually requires rebuilding the vector index.

The current V2 has no dedicated Rerank model registered for the built-in `doubao` provider. If reranking is required, choose another provider that V2 supports and that passes its health check.

## Image Generation

The Volcengine Ark website provides image-generation APIs that support Model IDs or image inference Endpoint IDs.

However, the current V2 `main` branch has no dedicated image-generation models or transport path registered for the built-in `doubao` provider. Therefore:

- Seedream support on the website does not mean that it automatically appears on the Cherry Studio image-generation page;
- Do not use an image Model ID as a standard chat model;
- Do not infer an Endpoint Type manually from an older screenshot;
- Use the providers and models actually available on the current image-generation page.

If a future V2 version adds an Ark image integration, synchronize or add the current Model ID again and test one image at a common size first.

{% hint style="warning" %}
Image generation may be billed by the number of successful outputs. Do not repeatedly submit tasks merely to test compatibility.
{% endhint %}

## PDFs and Attachments

V2 currently extracts PDF text locally before sending it to an Ark chat model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes model context and incurs cost;
- Images in a PDF must be sent separately to a vision model.

This differs from Ark's native Files API or document-understanding API. Cherry Studio does not automatically process a PDF as an Ark file object only because Ark supports file uploads.

Before uploading documents, images, or knowledge-base content, confirm compliance with privacy, data security, and organization requirements.

## Billing, Rate Limits, and Usage

Ark may simultaneously be restricted by:

- Account balance;
- Project budget;
- Pay-as-you-go, model-unit, or plan entitlements;
- RPM / TPM;
- Inference endpoint rate limits;
- Model concurrency;
- Content safety policies.

Review usage statistics and set budget alerts in the console. For a custom Endpoint, also check its status, resource specifications, and rate-limit configuration.

## Troubleshooting

### A 401 Error Is Returned

The API Key is incorrect, deleted, copied with an extra space, or does not match the API Host. Copy the Ark API Key again.

### A 403 Error Is Returned

The project, model, Endpoint, or content lacks permission. Check model activation, project, IAM, and content safety policies.

### A 404 Error Is Returned

The API Host, Model ID, or Endpoint ID is incorrect, or the model has been retired. Restore the default address and copy the ID again from the current model page.

### A 429 Error Is Returned

A model, project, or inference endpoint RPM, TPM, or concurrency limit has been reached. Reduce concurrency and wait for recovery.

### The Model List Is Empty

Ark does not necessarily return every model and custom Endpoint through the standard model list. Copy an ID directly from the official model page or inference endpoint page and add it manually.

### A Preset Model Does Not Work

The V2 presets may contain older dated versions that have been retired. Delete the invalid model and add the current Model ID.

### The Model ID Works, but the Endpoint ID Does Not

The Endpoint may not be running, may not be connected to the correct model, may belong to another project, or its resources may have been released. Check the Endpoint status in the Ark console.

### Reasoning Parameter Error

Restore the default reasoning setting. The `reasoningEffort` and `thinking` parameters for newer and older Doubao models cannot be mixed.

### Standard Chat Works, but MCP Is Not Called

Confirm that the model supports Function Calling. Ark cloud Remote MCP and Cherry Studio MCP are different features; enabling only the Ark console setting is insufficient.

### An Embedding Model Cannot Be Added

Confirm that you are using a vectorization Model ID and mark it as Embedding in model management. Do not use a display name or Endpoint-page URL as the model ID.

### Seedream Works on the Website but Is Missing from the Image-Generation Page

The built-in `doubao` provider in the current V2 has no dedicated image-generation path registered. Wait for client integration or use a provider already available on the image-generation page.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For current Volcengine Ark capabilities, see the [product documentation](https://www.volcengine.com/docs/82379/), [model list](https://www.volcengine.com/docs/82379/1554711), [API reference](https://www.volcengine.com/docs/82379/1523520), [Manage Inference Endpoints](https://www.volcengine.com/docs/82379/1182403), and [Image Generation API](https://www.volcengine.com/docs/82379/1824137). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
