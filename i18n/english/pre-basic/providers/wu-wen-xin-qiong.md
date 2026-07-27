# Infini-AI GenStudio

Infini-AI GenStudio provides large language model, vision model, Embedding, Rerank, and other APIs. Cherry Studio V2 includes a built-in **Infini-AI (Infini)** provider that connects through an OpenAI-compatible API.

Preset API Host in V2:

```text
https://cloud.infini-ai.com/maas
```

Cherry Studio completes the `/v1` path when sending a request. The actual chat endpoint is:

```text
https://cloud.infini-ai.com/maas/v1/chat/completions
```

{% hint style="info" %}
When using the built-in provider, keep the preset API Host whenever possible. Do not enter a model-hub, console, or documentation-page URL as the API Host.
{% endhint %}

## Before You Begin

1. Register and sign in to the Infini-AI computing cloud platform;
2. Confirm the tenant for the current account;
3. Create a GenStudio API Key;
4. Confirm the target model's Model ID in the service list or model hub;
5. Review the model price, service tier, and rate limits;
6. Confirm that the account balance or purchased concurrency package remains available.

Models, prices, and limits may change. This page does not list fixed "free models" or promotional allowances. Use the [service list](https://cloud.infini-ai.com/genstudio/usage/limit) and [preset model list](https://docs.infini-ai.com/gen-studio/models/supported-models.html) as the source of truth.

## Get an API Key

1. Sign in to the [computing cloud platform](https://cloud.infini-ai.com/);
2. Open [API Key Management](https://cloud.infini-ai.com/iam/secret/key);
3. Create a new GenStudio API Key;
4. Copy the complete Key;
5. Save it in a secure password manager.

GenStudio currently uses API Keys that begin with `sk-` and sends requests through Bearer authentication.

{% hint style="danger" %}
An API Key is an account credential. Do not put it in chats, documents, code repositories, screenshots, or support tickets. Delete and replace it immediately if it is exposed.
{% endhint %}

## Configure Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **Infini-AI / Infini**;
4. Paste the GenStudio Key into API Key;
5. Keep the API Host as `https://cloud.infini-ai.com/maas`;
6. Turn on the provider switch at the top of the page;
7. Click **Add** or synchronize models;
8. Review the synchronization preview and apply the changes;
9. Enable only the models you plan to use;
10. Run a model health check.

A successful health check only confirms that the current Key, address, and test model can complete a basic request. It does not mean that the account has access to every model in the list.

## Synchronize and Add Models

Cherry Studio uses the OpenAI-compatible model-list endpoint:

```text
GET /maas/v1/models
```

After synchronization:

1. Check added, updated, and removed items;
2. Confirm that each Model ID exactly matches the service list;
3. Apply the synchronization results;
4. Delete older models that have been retired;
5. Test chat, Embedding, and Rerank models separately.

If synchronization fails, copy a Model ID from the service list or model hub and add it manually. Capitalization, hyphens, version suffixes, and the `pro-` prefix are all part of the Model ID.

{% hint style="warning" %}
Concurrency-package services usually use dedicated Model IDs beginning with `pro-`. Do not treat a standard pay-as-you-go model and a concurrency-package model as the same ID.
{% endhint %}

The built-in V2 candidate models may predate the current platform list. Prefer real-time synchronization results and the service list.

## Choose a Chat Model

GenStudio chat models use OpenAI-compatible Chat Completions.

For the first test:

1. Select a model explicitly available to the current account;
2. Send a short plain-text message;
3. Check streaming output;
4. Add a system prompt;
5. Then test a long context, reasoning, images, and tool calls.

Model families and versions are updated. Do not rely on fixed examples from older tutorials; copy the current Model ID directly from the service list.

## Vision Models

Only a Model ID explicitly marked by GenStudio as a vision-language model can understand images.

In Cherry Studio:

1. Synchronize the latest models;
2. Confirm that the model details include image-input support;
3. Upload one small image first;
4. Ask about content that can be verified directly in the image;
5. After success, try multiple or high-resolution images.

Text and vision models in the same family may use different Model IDs. Similar names do not mean that the input modalities are the same.

## Reasoning Mode

GenStudio provides several reasoning models. Different families may use different reasoning parameters and response formats. Cherry Studio applies generic integrations based on the recognized model family, but the Infini-AI provider currently has no separate reasoning-parameter panel.

When using a reasoning model for the first time:

1. Keep the reasoning setting at **Default**;
2. Do not add custom request parameters;
3. Confirm that basic chat works;
4. Then try turning reasoning on or off;
5. Check the supported parameters in the model details.

If enabling reasoning returns a 400, restore the default setting before repeatedly changing the Model ID.

## MCP and Tool Calling

Certain GenStudio models support Function Calling. Cherry Studio can send MCP tool definitions to a model through Chat Completions, but stable calls still depend on the specific model.

Validate in this order:

1. Confirm that standard chat works;
2. Enable only one MCP tool with simple parameters;
3. Explicitly ask the model to call that tool;
4. Check whether it produces a structured tool call;
5. Confirm that the tool result can be returned;
6. Add more tools gradually.

A model saying that it will call a tool is not an actual call. If this happens, check the model details, tool definition, and prompt.

## Embedding and Knowledge Bases

GenStudio provides an OpenAI-compatible Embedding endpoint:

```text
POST /maas/v1/embeddings
```

The current service may provide vector models such as `bge-m3`; use the service list for the actual Model ID. Cherry Studio identifies an Embedding model from its Model ID and manually assigned type.

Before creating a knowledge base:

1. Synchronize or manually add an Embedding model;
2. Confirm that the model is recognized as the **Embedding** type;
3. Run a health check;
4. Detect the vector dimensions;
5. Create a test knowledge base with a small number of documents;
6. Verify retrieval results before importing in bulk.

Vector dimensions are part of a knowledge-base index. Changing an Embedding model or dimension after creating a knowledge base usually requires rebuilding the index.

## Rerank

GenStudio provides a Rerank endpoint:

```text
POST /maas/v1/rerank
```

The current official example model is `bge-reranker-v2-m3`, but use the service list for its availability.

In Cherry Studio:

1. Synchronize or manually add a Rerank model;
2. Confirm that the model is recognized as the **Rerank** type;
3. Select it in the knowledge-base settings;
4. Compare results before and after enabling it with a small number of queries;
5. Then decide whether to use it for a production knowledge base.

Embedding and Rerank use different models and endpoints. A working Embedding model does not guarantee that Rerank works; validate them separately.

## Image and Video Generation

The GenStudio platform also provides image- and video-generation capabilities, but the built-in Infini-AI provider in Cherry Studio V2 currently works primarily through OpenAI-compatible chat, Embedding, and Rerank endpoints. It has no dedicated Infini-AI image- or video-generation transport registered.

Therefore:

- Do not add an image- or video-generation model as a chat model;
- Use the providers and models actually available on the Cherry Studio image-generation page;
- A generative model existing on the website does not mean that the current V2 has integrated it.

## PDFs and Attachments

Cherry Studio V2 extracts PDF text locally before sending the extracted result to a chat model:

- Text-based PDFs can usually be processed directly;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes model context and Tokens;
- Images in a PDF must be sent separately to a vision model.

Infini-AI is a cloud service. Before uploading documents, images, or knowledge-base content, confirm compliance with privacy, copyright, and organization security requirements.

## Billing and Rate Limits

GenStudio API calls are affected by the account service tier, model pricing, and rate limits. The platform may simultaneously limit:

- RPM: requests per minute;
- RPD: requests per day;
- TPM: Tokens per minute;
- Concurrency slots for concurrency-package services.

Current billing and limits may change over time. Before enabling an automated task:

1. Review the latest billing rules;
2. Confirm the account balance;
3. Set concurrency and retry limits;
4. Monitor Token usage;
5. Back off and retry after a 429;
6. Retain the response `id` and `traceresponse` for troubleshooting.

Do not create multiple Keys to evade tenant-level limits. Keys in the same tenant may share quotas.

## Troubleshooting

### A 401 Error Is Returned

The API Key is incorrect, deleted, copied with an extra space, or the request did not use Bearer authentication correctly. Copy the Key again or create a replacement.

### A 403 Error Is Returned

The account, tenant, or target model lacks permission. Check whether the model requires an application, the account status, and the current tenant.

### A 404 Error Is Returned

The API Host, endpoint path, or Model ID is incorrect. Restore the built-in preset address and copy the complete Model ID from the service list.

### A 429 Error Is Returned

An RPM, RPD, TPM, or concurrency-package limit has been reached. Reduce concurrency, shorten the context, and wait for recovery.

### A 400 Error Is Returned

The model does not support the current parameter, image format, or reasoning setting. Clear custom parameters, restore the default reasoning setting, and test again.

### The Model List Is Empty

Check the API Key, API Host, network proxy, and tenant permissions. You can also copy a Model ID from the service list and add it manually.

### A Preset Model Cannot Be Called

A built-in V2 candidate may have been retired, renamed, or excluded from the current account's permissions. Synchronize the latest list and delete invalid models.

### A Concurrency-Package Model Call Fails

Confirm that the purchase remains valid and use the complete dedicated Model ID assigned by the platform. Do not remove the `pro-` prefix.

### An Embedding Model Appears in the Chat List

Check the model type label. The Model ID should contain the complete name provided by the platform and be set to Embedding in model management rather than a standard chat model.

### The Rerank Health Check Did Not Run

The current V2 generic model connection check skips Rerank. Validate an actual reranking request in the knowledge-base retrieval flow.

### An Uploaded File Returns an Unsupported Error

First confirm that text was extracted successfully from the file, then check whether the current chat model supports the corresponding input. Scanned PDFs require OCR, and images require a vision model.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For current Infini-AI capabilities and configuration, see [GenStudio API Quick Integration](https://docs.infini-ai.com/gen-studio/api/get-started/), [Cherry Studio Integration Guide](https://docs.infini-ai.com/gen-studio/integrations/use-cherrystudio.html), [Preset Model List](https://docs.infini-ai.com/gen-studio/models/supported-models.html), [Rerank Guide](https://docs.infini-ai.com/gen-studio/api/retrieval/tutorial-rerank.html), [Billing Rules](https://docs.infini-ai.com/gen-studio/api/usage-and-billing/billing.html), and [Rate Limits](https://docs.infini-ai.com/gen-studio/api/usage-and-billing/rate-limit.html). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
