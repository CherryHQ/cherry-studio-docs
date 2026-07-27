# PPIO

PPIO provides large language models, vision models, Embedding, Rerank, and image-generation APIs. Cherry Studio V2 includes a built-in PPIO provider that can synchronize models currently available on the platform without creating a custom provider.

The built-in Base URL for chat and Embedding in V2 is:

```text
https://api.ppinfra.com/v3/openai/
```

{% hint style="info" %}
Some examples in the official PPIO API manual use `api.ppio.com/openai/v1`, but the built-in Cherry Studio V2 provider currently uses the compatible address above. Keep the application preset during initial configuration. Change it only when PPIO or Cherry Studio explicitly requires a migration.
{% endhint %}

## Before You Begin

Using the PPIO model API for the first time usually requires you to:

1. Register and sign in to PPIO;
2. Complete individual or business identity verification;
3. Add funds to the account or confirm that a usable balance is available;
4. Create an API Key;
5. Confirm that the model you plan to use is still in service.

PPIO may adjust its models, prices, and availability. This page does not list fixed prices or promotional allowances. Use the console and [model service page](https://ppio.com/model-api/product/llm-api) as the source of truth.

## Get an API Key

1. Sign in to the [PPIO console](https://ppio.com/);
2. Open [API Key Management](https://ppio.com/settings/key-management);
3. Click **Create**;
4. Enter a recognizable Key name;
5. Copy the Key immediately after creating it and store it securely.

PPIO authenticates an API Key as a Bearer token. Each account can currently create up to ten Keys, and a Key cannot be viewed again after creation.

{% hint style="danger" %}
An API Key is an account credential. Do not put it in chats, documents, code repositories, or troubleshooting screenshots. If it is lost or exposed, delete it in PPIO and create a replacement immediately.
{% endhint %}

## Configure Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **PPIO**;
4. Paste the PPIO Key into API Key;
5. Keep the preset Base URL as `https://api.ppinfra.com/v3/openai/`;
6. Turn on the provider switch at the top of the page;
7. Click **Add** or synchronize models;
8. Review the synchronization preview and apply the changes;
9. Enable only the models you plan to use;
10. Run a model health check.

A successful connection check only confirms that the credential and a basic request work. It does not mean that the account can call every model in the list. PPIO still determines model permissions, balances, regional restrictions, and availability.

## Synchronize Models

Cherry Studio V2 reads three model lists in parallel:

```text
/models
/models?model_type=embedding
/models?model_type=reranker
```

The results are merged and deduplicated by Model ID, so one synchronization can discover chat, Embedding, and Rerank models together.

After synchronization:

1. Review added, updated, and removed items;
2. Confirm the type of each model;
3. Apply the synchronization results;
4. Delete obsolete models that you retained manually;
5. Run separate health checks.

{% hint style="warning" %}
The built-in V2 presets are for initial display and may predate a PPIO model retirement or rename. The model list returned by the platform in real time and official announcements take priority. Do not continue using an older Model ID only because it remains visible locally.
{% endhint %}

## Choose a Chat Model

PPIO chat models connect through OpenAI-compatible Chat Completions. Support for long contexts, vision, tool calling, and reasoning parameters varies by model.

Test in this order:

1. Send a short plain-text message;
2. Check streaming output;
3. Add a system prompt;
4. Test a longer context;
5. Test images, reasoning, and tool calls last.

The Model ID must exactly match the current PPIO list, including the organization prefix, capitalization, slashes, and version suffix. Do not use a model display name or product-page URL as the Model ID.

## Vision Models

Only a Model ID explicitly marked by PPIO as a vision-language model can receive images.

In Cherry Studio:

1. Synchronize the latest models;
2. Select a model that shows image support;
3. Upload one small image first;
4. Check whether the model actually understands the image;
5. Then try multiple or high-resolution images.

Text and vision variants in the same model family may use different IDs. Images also increase request size, context usage, and cost.

## Reasoning Mode

Cherry Studio generates the corresponding reasoning parameters by model family. For DeepSeek hybrid-reasoning models on PPIO, V2 uses the platform-compatible `thinking` control.

If enabling reasoning causes a parameter error:

1. Restore the reasoning option to **Default**;
2. Clear custom model parameters;
3. Confirm that the Model ID does not point to an older version;
4. Synchronize models again;
5. Test against PPIO's current model description.

Do not copy a reasoning parameter accepted by one model to another family. PPIO only forwards parameters supported by the platform; the specific model still determines the final behavior.

## MCP and Tool Calling

Cherry Studio MCP requires a model that supports structured Tool Calling.

1. Confirm that standard chat works first;
2. Enable only one simple MCP tool;
3. Explicitly ask the model to call that tool;
4. Check whether it produces a structured call;
5. Confirm that the tool result can be returned to the model;
6. Add more tools gradually.

If a model only says that it will call a tool without making an actual call, the cause is usually model capability, model detection, or parameter compatibility. It does not mean that the MCP server itself is running successfully.

## Embedding, Rerank, and Knowledge Bases

PPIO provides OpenAI-compatible Embedding and Rerank APIs. V2 queries these two model types separately during synchronization.

Examples currently listed in the official API manual include:

- Embedding: `baai/bge-m3`;
- Rerank: `baai/bge-reranker-v2-m3`.

These names may still change as the platform is updated. Use the synchronization results and PPIO model page as the source of truth.

When creating a knowledge base:

1. Synchronize PPIO models first;
2. Select a model explicitly recognized as an Embedding model;
3. Detect its vector dimensions;
4. Run a health check;
5. Select a currently available Rerank model;
6. Import a small number of documents as a test;
7. Confirm retrieval and reranking results before importing in bulk.

Do not directly change an Embedding model or vector dimension after using it in an existing knowledge base. Doing so usually requires rebuilding the vector index.

## Image Generation and Editing

Cherry Studio V2 implements a dedicated image transport path for PPIO. It uses a different host from the chat API:

| Purpose | Address used by V2 |
| --- | --- |
| Chat and Embedding | `https://api.ppinfra.com/v3/openai/` |
| Image generation and task queries | `https://api.ppio.com` |

The image page selects a synchronous or asynchronous API based on model registration information and displays only the modes and parameters declared by that model, such as:

- Text-to-image;
- Image editing;
- Image dimensions;
- Seed;
- Watermark;
- LoRA or reference images for certain models.

Not every image model on the PPIO website has been integrated with the current V2. Start by testing a PPIO model available on the Cherry Studio image-generation page.

On January 31, 2026, PPIO retired a set of older Image APIs, including legacy `txt2img`, `img2img`, background removal, background replacement, inpainting, text erasure, object erasure, and face-fusion APIs. Do not continue following tutorials or screenshots that use these retired APIs.

{% hint style="warning" %}
Image generation may incur significant charges. Test with a small size and one output first. Do not repeatedly submit requests while waiting for an asynchronous task, as this may create multiple billable tasks.
{% endhint %}

## PDFs and Attachments

V2 currently extracts PDF text locally before sending it to a PPIO chat model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes model context and incurs cost;
- Images in a PDF must be sent separately to a vision model.

PPIO is a cloud service. Before uploading documents, images, or knowledge-base content, confirm that they comply with privacy, copyright, and organization security requirements.

## Balance, Rate Limits, and Model Retirement

PPIO charges by model and usage. Specific prices, rates, and concurrency limits may change.

Recommendations:

1. Set a budget or balance alert in the console;
2. Validate a new model with a short request first;
3. Avoid allowing several automated tasks that share one Key to retry indefinitely;
4. Reduce concurrency and wait after a 429 response;
5. Follow the [official announcements](https://ppio.com/docs/announcement/announcement) for model and API retirements;
6. Synchronize models regularly and remove older IDs.

The community documentation does not hard-code limited-time prices, invitation codes, promotional credits, or "free forever" claims that could mislead users after a promotion ends.

## Troubleshooting

### A 401 Error Is Returned

The API Key is incorrect, deleted, copied with an extra space, or the request did not use Bearer authentication correctly. Create and copy a Key again from the Key management page.

### A 402 Error or Insufficient Balance Is Returned

The account balance is insufficient, or the current model is not included in the available entitlement. Check PPIO billing, balance, and model pricing.

### A 403 Error Is Returned

The account may not have completed identity verification, may lack model permissions, or the request content may trigger a platform policy. Check the account status in the PPIO console first.

### A 404 Error Is Returned

The Base URL, Model ID, or image API may be obsolete. Restore the V2 preset address first, then synchronize models and review official retirement announcements.

### A 429 Error Is Returned

A model rate, concurrency, or account limit has been reached. Reduce concurrency, shorten requests, and wait for recovery. Do not retry immediately in a loop.

### The Model List Is Empty

Check the API Key, Base URL, and network proxy. Restore the preset Base URL and synchronize again. If necessary, copy a complete Model ID from the current PPIO model page and add it manually.

### A Preset Model Does Not Work

The preset may predate a platform retirement, rename, or permission change. Use real-time synchronization results as the source of truth, remove the invalid model, and choose a currently available version.

### Embedding Works, but Rerank Does Not

They use different models and APIs. Synchronize and run health checks separately, confirm that the Rerank model has not been retired, and verify that the knowledge base selected a reranking model rather than an Embedding model.

### An Image Task Keeps Waiting

The task may still be queued, the platform may be busy, network polling may have failed, or the balance may be insufficient. Wait and review the error information first. Do not repeatedly submit the same task.

### An Image Model from an Older Tutorial Cannot Be Found

PPIO has retired certain older Image APIs, and V2 only shows image models that are currently integrated. Synchronize the latest models and use the actual options on the image-generation page.

### Chat and Image Generation Both Fail After Changing the Base URL

PPIO's chat and image paths use different hosts. Do not overwrite V2's internal image address to match an API example from an article. Restore the built-in provider defaults and retry.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For current PPIO account requirements, Keys, and APIs, see [Quick Start](https://ppio.com/docs/model/get-start), [Manage API Keys](https://ppio.com/docs/support/api-key), [Embedding](https://ppio.com/docs/models/reference-llm-create-embeddings), and [Rerank](https://ppio.com/docs/models/reference-llm-create-rerank). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
