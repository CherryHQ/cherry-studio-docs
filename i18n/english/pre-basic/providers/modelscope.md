# ModelScope

ModelScope makes certain open-source models available as directly callable online APIs through API-Inference. Cherry Studio V2 includes a built-in ModelScope provider that supports OpenAI-compatible chat, vision models, embedding models, and asynchronous image generation.

Default Base URL:

```text
https://api-inference.modelscope.cn/v1/
```

{% hint style="info" %}
Not every model in the ModelScope model hub supports API-Inference. A model can connect directly to Cherry Studio only when its page shows the API-Inference label and provides an invocation example.
{% endhint %}

## Before You Begin

The free ModelScope API-Inference service currently requires you to:

1. Register and sign in to ModelScope;
2. Link an Alibaba Cloud account;
3. Complete real-name verification for the linked Alibaba Cloud account;
4. Create a ModelScope Access Token;
5. Use a model that currently supports API-Inference.

API-Inference is a free trial service and does not provide a production SLA. For commercial, high-concurrency, or stable service, use a commercial API provider or deploy a model yourself.

## Get an Access Token

1. Sign in to [ModelScope](https://modelscope.cn/);
2. Open [Access Tokens](https://modelscope.cn/my/myaccesstoken);
3. Create a token and give it a recognizable name;
4. Copy the generated Access Token;
5. Store the Token securely.

{% hint style="danger" %}
An Access Token is an account credential. Do not put it in chats, documents, code repositories, or troubleshooting screenshots. Delete and replace it in ModelScope immediately if it is exposed.
{% endhint %}

## Configure Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **ModelScope**;
4. Paste the Access Token into API Key;
5. Keep the Base URL as `https://api-inference.modelscope.cn/v1/`;
6. Turn on the provider switch at the top of the page;
7. Click **Add** or synchronize models;
8. Review the synchronization preview and apply the changes;
9. Enable only the models you plan to use;
10. Run a model health check.

If the synchronized list contains an older model, do not assume that it can still be called. ModelScope gradually adjusts or retires older models as new ones are released. Check the API-Inference status on the model details page.

## Find Available Models

1. Open the [ModelScope model hub](https://modelscope.cn/models);
2. Filter for models that support **API-Inference**;
3. Open the model details page;
4. Confirm that the page provides an API entry point and example on the right;
5. Copy the complete Model ID;
6. Synchronize or manually add that ID in Cherry Studio;
7. Run a health check.

A Model ID usually includes the organization and model name, for example:

```text
Qwen/Qwen3.5-35B-A3B
```

Capitalization, slashes, and suffixes are all part of the ID. Do not use a display name, repository URL, or local filename as an API Model ID.

{% hint style="warning" %}
The built-in V2 model list contains only candidates; the platform's current support status takes priority. If you encounter a 404 or unavailable-model error, check the ModelScope model page instead of repeatedly retrying a retired model.
{% endhint %}

## Chat Models

ModelScope LLM API-Inference uses OpenAI-compatible Chat Completions. When choosing a model, confirm that it is a chat or instruction model rather than a base, Embedding, or image-generation model.

Test in this order:

1. Send a short plain-text message;
2. Test streaming output;
3. Add a system prompt;
4. Test a long context;
5. Test reasoning, images, or tool calls last.

Parameters and prompt templates may differ among open-source models. ModelScope recommends following the API example on the model details page, especially for reasoning models.

## Vision Models

A model with vision support can receive an image URL or Base64 image through OpenAI-compatible messages.

In Cherry Studio:

1. Select a Model ID that explicitly supports vision;
2. Confirm that the model shows image support;
3. Upload one small image first;
4. Check whether the model actually understands the image;
5. Then try multiple or high-resolution images.

Models in the same family do not necessarily all support vision. Images also consume more context and free allowance.

## Reasoning and Tool Calling

### Reasoning

A reasoning model may use model-specific parameters or response formats. If changing a reasoning option causes an error:

1. Restore it to **Default**;
2. Clear custom parameters;
3. Compare your configuration with the model page example;
4. Run the health check again.

### MCP and Tool Calling

Cherry Studio MCP requires a model that can produce structured Tool Calling output.

1. Complete a standard chat first;
2. Enable only one simple MCP tool;
3. Explicitly request a tool call;
4. Check whether the model produces an actual structured call;
5. Confirm that the result can be returned to the model;
6. Add more tools afterward.

The MCP marketplace on ModelScope and the ModelScope model service are separate features. A model Access Token may be used for the relevant platform capabilities, but "Model Providers" and "MCP Servers" must still be configured separately in Cherry Studio.

## Image Generation and Editing

Cherry Studio V2 implements a dedicated asynchronous image-generation path for ModelScope:

1. Submit a task to `/v1/images/generations`;
2. Obtain the `task_id`;
3. Poll `/v1/tasks/{task_id}`;
4. Read the image URL after the task succeeds.

After selecting an AIGC model currently supported by ModelScope, you can use the following on the image-generation page:

- Image dimensions;
- Negative prompts;
- Sampling steps;
- Guidance;
- Seed;
- Image-editing input for supported models;
- LoRA for supported models.

Supported dimensions, steps, Guidance, and editing capabilities vary by model. Follow the ranges given on the model details page.

Image tasks run asynchronously and may take considerably longer than a chat. Cancelling a task, a network interruption, insufficient allowance, or high platform load may cause polling to fail.

## Embedding Models and Knowledge Bases

The ModelScope provider in Cherry Studio implements OpenAI-compatible Embeddings calls, but only ModelScope models that actually provide a compatible Embedding API can be used.

1. Confirm the task type and API example on the model page;
2. Add the complete Model ID;
3. Confirm that Cherry Studio recognizes it as an embedding model;
4. Detect its dimensions in a knowledge base;
5. Run a health check;
6. Import documents afterward.

Do not casually change a model or its dimensions after using it in an existing knowledge base. Doing so usually requires rebuilding the vector index.

## PDFs and Attachments

V2 currently extracts PDF text locally before sending it to a ModelScope chat model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes context and free call allowance;
- Images in a PDF must be sent separately to a vision model.

ModelScope is a cloud service. Before uploading a document, confirm that it complies with privacy and organization security requirements.

## Allowances and Rate Limits

Current rules for the free ModelScope API-Inference service include:

- Up to 2,000 total calls per registered user per day;
- Usually up to 200 calls per model per day;
- Some large models may be further limited to 100 calls per day or fewer;
- Concurrency is adjusted dynamically based on platform load;
- AIGC models may have separate limits;
- A specific model's allowance may change dynamically at any time.

Service response headers may include:

| Response header | Meaning |
| --- | --- |
| `modelscope-ratelimit-requests-limit` | Total daily user allowance |
| `modelscope-ratelimit-requests-remaining` | Remaining daily user allowance |
| `modelscope-ratelimit-model-requests-limit` | Daily allowance for the current model |
| `modelscope-ratelimit-model-requests-remaining` | Remaining allowance for the current model |

Cherry Studio does not currently display these response headers as a complete billing page. Evaluate allowances using error information, ModelScope pages, and the platform's latest rules together.

Do not create or switch to backup accounts to evade platform limits. The free allowance is for evaluation and prototyping; move batch calls to an appropriate commercial service.

## API-Inference vs. API-Provider

ModelScope also provides API-Provider, which can connect to an external API provider. Its allowance and billing source differ from the free API-Inference service.

- API-Inference: evaluation inference resources provided by ModelScope;
- API-Provider: calls a connected external provider and does not share the same free API-Inference limit, but is subject to the external provider's billing and restrictions.

The default `api-inference.modelscope.cn` configuration on this page points to API-Inference. Do not mix external-provider credentials without understanding which service will bill the request.

## Troubleshooting

### A 401 Error Is Returned

The Access Token is incorrect, deleted, contains spaces, or was not sent correctly. Copy the Token again and confirm that a proxy has not rewritten the Base URL.

### A 403 Error Is Returned

The account may not be linked to Alibaba Cloud, real-name verification may be incomplete, or model access may be restricted. Complete the account requirements on the ModelScope website first.

### A 404 Error Is Returned

The model ID may be incorrect, the model may have been retired, or the Base URL may be wrong. Check the complete ID and the API-Inference status on the model page.

### A 429 Error Is Returned

You may have reached the total user allowance, per-model allowance, separate AIGC allowance, or dynamic concurrency limit. Reduce the request rate and wait for the allowance to recover. Use a commercial service for production needs.

### The Model List Is Empty

Check the Token, Base URL, and network. You can also copy the complete Model ID of a currently supported model from its model page and add it manually.

### A Preset Model Does Not Work

The V2 preset may predate a platform retirement or rename. Use the current ModelScope model page as the source of truth, synchronize again, or choose a model that is still supported.

### Image Generation Keeps Waiting

The task may still be queued, the platform may be busy, polling may have a network failure, or the allowance may be insufficient. Check the ModelScope task status and reduce concurrency.

### Image-Editing Parameters Return an Error

The target model may not support editing, the input dimensions may be invalid, or it may require a specific `image_url`. Follow the examples and parameter ranges on the model page.

### MCP Does Not Work

First confirm that the model supports tool calling. Services from the ModelScope MCP marketplace must also be synchronized or added separately in Cherry Studio's MCP settings.

### Stable High Concurrency Is Required

The free API-Inference service is not suitable for an SLA or commercial high concurrency. Use ModelScope API-Provider, another commercial model service, or deploy an open-source model.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For ModelScope models, APIs, and current allowances, see the [API-Inference documentation](https://modelscope.cn/docs/model-service/API-Inference/intro) and [usage limits](https://modelscope.cn/docs/model-service/API-Inference/limits). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
