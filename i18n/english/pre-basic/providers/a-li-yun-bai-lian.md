# Alibaba Cloud Bailian

Alibaba Cloud Bailian (Alibaba Cloud Model Studio) provides Qwen and models from several third-party providers. Cherry Studio V2 includes a built-in Bailian provider that supports OpenAI-compatible chat, Anthropic-compatible calls, Embedding, Rerank, and dedicated image-generation and editing paths.

The default V2 addresses for China (Beijing) are:

| Protocol | Default Base URL |
| --- | --- |
| OpenAI-compatible | `https://dashscope.aliyuncs.com/compatible-mode/v1/` |
| Anthropic-compatible | `https://dashscope.aliyuncs.com/apps/anthropic` |

{% hint style="info" %}
Bailian API Keys, Base URLs, and model lists are isolated by region and cannot be mixed across regions. Using a Beijing Key with a Singapore address, or a Singapore Key with a Beijing address, usually returns a 401.
{% endhint %}

## Before You Begin

Using the Bailian API for the first time usually requires you to:

1. Register and sign in to an Alibaba Cloud account;
2. Complete identity verification for the account;
3. Activate Alibaba Cloud Bailian;
4. Choose the region you plan to use;
5. Create an API Key;
6. Confirm the account balance, free allowance, or subscription entitlement;
7. Record the corresponding Workspace ID.

Models, prices, free allowances, and regional availability may change. This page does not list fixed costs. Use the [Bailian model list](https://help.aliyun.com/zh/model-studio/models) and console billing as the source of truth.

## Choose a Region and Base URL

Bailian is promoting workspace-specific domains. They are usually more stable than the older public DashScope domain and require replacing `{WorkspaceId}` with the actual Workspace ID.

Common OpenAI-compatible addresses:

| Region | Base URL |
| --- | --- |
| China (Beijing) default | `https://dashscope.aliyuncs.com/compatible-mode/v1/` |
| China (Beijing) workspace domain | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/` |
| Singapore | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/` |
| Japan (Tokyo) | `https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1/` |
| Germany (Frankfurt) | `https://{WorkspaceId}.eu-central-1.maas.aliyuncs.com/compatible-mode/v1/` |
| US (Virginia) | `https://dashscope-us.aliyuncs.com/compatible-mode/v1/` |

The corresponding Anthropic-compatible address usually replaces the final path with `/apps/anthropic`. Supported regions and protocols vary by model. Copy the address from the model details page instead of inferring it from the model name.

{% hint style="warning" %}
Do not enter `{WorkspaceId}` literally in Cherry Studio. You can find the Workspace ID on Bailian's workspace management page; it usually resembles `llm-...`.
{% endhint %}

## Get an API Key

1. Open [Bailian API Key Management](https://bailian.console.aliyun.com/?tab=model#/api-key);
2. Confirm the target region in the upper-right corner of the page;
3. Click **Create API Key**;
4. Choose the owning workspace;
5. Select all permissions, or configure an IP allowlist and model scope according to your organization's requirements;
6. Enter a recognizable description;
7. Copy the Key immediately after creating it and store it securely.

A newly created pay-as-you-go Key may begin with `sk-ws` and is shown only once during creation. Older `sk-` Keys may continue to work.

{% hint style="danger" %}
An API Key is an account credential. Do not put it in chats, documents, code repositories, or troubleshooting screenshots. Reset or delete it in the Bailian console immediately if it is exposed.
{% endhint %}

## Configure Cherry Studio

### Use the Default Beijing Address

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **Bailian / Alibaba Cloud Bailian**;
4. Paste an API Key from the Beijing region;
5. Keep the OpenAI Base URL as `https://dashscope.aliyuncs.com/compatible-mode/v1/`;
6. Turn on the provider switch at the top of the page;
7. Click **Add** or synchronize models;
8. Review the synchronization preview and apply the changes;
9. Enable only the models you plan to use;
10. Run a model health check.

### Use Another Region or a Workspace Domain

1. Copy the API Host for the target workspace from the Bailian console;
2. In Cherry Studio, change the OpenAI Base URL to the corresponding `/compatible-mode/v1/` address;
3. If you plan to use an Anthropic-compatible workflow, update the Anthropic Base URL as well;
4. Use an API Key created under the **same region and billing plan**;
5. Synchronize models again;
6. Run a health check for each model.

V2 derives the image API host from the user-configured OpenAI Base URL. After switching to a workspace domain, image requests also follow that domain instead of being forced back to the public Beijing domain.

## Synchronize and Add Models

Bailian's model catalog changes frequently. The built-in V2 list is only for initial display. Use the current results returned by Bailian during synchronization.

Recommendations:

1. Confirm that the region and Key match;
2. Synchronize models;
3. Review added, updated, and removed items;
4. Apply the synchronization results;
5. Check model capability labels;
6. Delete obsolete models that you retained manually;
7. Run a health check for each model.

If synchronization results are incomplete, copy the complete Model ID from the Bailian model page and add it manually. Capitalization, slashes, and version suffixes are all part of the ID; for example, a third-party model may have an organization prefix.

{% hint style="warning" %}
A model appearing in a V2 preset or another region does not mean that the current API Key has permission to call it. Final access depends on the Bailian server, workspace permissions, and the regional model list.
{% endhint %}

## Chat Models

Standard chat uses OpenAI-compatible Chat Completions.

Test in this order:

1. Send a short plain-text message;
2. Check streaming output;
3. Add a system prompt;
4. Test a longer context;
5. Then test images, reasoning, and tool calls.

Bailian provides both Qwen and third-party models. Even when calling a model from the same vendor through Bailian, use the Model ID and parameters from the Bailian model page instead of copying IDs from another platform.

## Anthropic Compatibility and Code Tools

Bailian provides an Anthropic-compatible Messages API for coding tools or Agent workflows that support a custom Anthropic address.

In Cherry Studio:

1. Confirm that the target model supports the Anthropic-compatible protocol;
2. Enter the Anthropic Base URL for the region;
3. Keep the API Key in the same region;
4. Run a standard chat first;
5. Then test Code Tools or Agent scenarios.

The OpenAI- and Anthropic-compatible addresses are different paths. Changing only the OpenAI Base URL does not guarantee that the Anthropic workflow points to the same region.

## Reasoning Mode

Qwen, DeepSeek, GLM, Kimi, and other models on Bailian may use different reasoning parameters. Cherry Studio V2 adapts parameters such as `enable_thinking` and reasoning budgets by model family.

If enabling reasoning causes an error:

1. Restore the reasoning setting to **Default**;
2. Clear custom model parameters;
3. Confirm that you are using the current Model ID;
4. Check the official example for that model in the current region;
5. Run the health check again.

Some models support only turning reasoning on or off and do not accept effort levels such as `low`, `medium`, or `high`. Do not copy reasoning parameters from another platform directly to Bailian.

## Vision and Multimodal Models

Only models that explicitly support image, audio, or video input can receive the corresponding attachments.

When testing a vision model:

1. Synchronize the latest Model ID;
2. Confirm that the model shows image support;
3. Upload one small image first;
4. Check whether the model actually understands the content;
5. Then try multiple images, video, or high-resolution files.

Text, vision, and Omni variants in the same family may be different models. Attachments increase context usage, network time, and cost.

## MCP and Tool Calling

Cherry Studio MCP requires a model that supports structured Tool Calling.

1. Confirm that standard chat works first;
2. Enable only one simple MCP tool;
3. Explicitly request a tool call;
4. Check whether it produces a structured call;
5. Confirm that the tool result can be returned to the model;
6. Add more tools afterward.

A model describing that it will call a tool is not an actual call. If this occurs, check model capabilities, protocol, prompt, and tool definitions.

## Embedding, Rerank, and Knowledge Bases

Bailian provides text and multimodal Embedding as well as text and multimodal Rerank. Current recommendations on the model page may include:

- Text Embedding: `text-embedding-v4`;
- Text Rerank: `qwen3-rerank`;
- Multimodal Embedding: `qwen3-vl-embedding`;
- Multimodal Rerank: `qwen3-vl-rerank`.

These are platform examples, not a permanent list. `gte-rerank` was retired on May 30, 2026, and should no longer be configured according to older tutorials.

When creating a knowledge base:

1. Add a currently available Embedding model;
2. Confirm that Cherry Studio recognizes it as an embedding model;
3. Detect its vector dimensions;
4. Run a health check;
5. Add and test a Rerank model;
6. Import a small number of documents as a test;
7. Confirm retrieval and reranking results before importing in bulk.

Do not directly change an Embedding model or vector dimension after using it in an existing knowledge base. Doing so usually requires rebuilding the vector index.

Rerank endpoints and capabilities may differ among Bailian regions. If a model can be added but a reranking request fails, turn off Rerank first to keep basic retrieval available, then verify the current V2 version, regional API, and model permissions.

## Image Generation and Editing

Cherry Studio V2 implements a dedicated image transport path for Bailian:

1. Select the native DashScope image API based on the model;
2. Enable `X-DashScope-Async` in requests for asynchronous models;
3. Obtain the `task_id`;
4. Poll the task status;
5. Read the image URL after success.

V2 displays the corresponding modes and parameters only for integrated models, such as:

- Text-to-image;
- Image editing;
- Image translation;
- Dimensions;
- Seed;
- Negative prompts;
- Watermark;
- Reference images or function types for certain models.

Not every image model on the Bailian website has been integrated with the current V2. Start by testing a Bailian model available on the Cherry Studio image-generation page.

{% hint style="warning" %}
Image tasks may be billed by the number of successful outputs. Set the output count to 1 for the first test and avoid submitting the request again while waiting for an asynchronous result.
{% endhint %}

Cancelling the wait in Cherry Studio only stops local polling. DashScope does not provide a general task-cancellation API that the current V2 can call, so a submitted task may continue running and incur charges.

## PDFs and Attachments

V2 currently extracts PDF text locally before sending it to a Bailian chat model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes model context and incurs cost;
- Images in a PDF must be sent separately to a vision model.

Bailian is a cloud service. Before uploading documents, images, or knowledge-base content, confirm compliance with privacy, cross-border data, and organization security requirements. Pay particular attention to the data-processing scope of the selected region.

## Allowances, Permissions, and Rate Limits

Bailian may simultaneously be restricted by:

- Account balance and free allowance;
- Workspace budget;
- The Key's IP allowlist;
- The Key's model permissions;
- RPM / TPM;
- Number of concurrent tasks;
- Image task queue;
- Regional resource availability.

Set budget and usage alerts in the console, and do not allow multiple automated tasks sharing the same Key to retry indefinitely.

## Troubleshooting

### A 401 Error Is Returned

The API Key is incorrect or reset, or its region does not match the Base URL. Confirm the region first, then copy the corresponding Key again.

### A 403 Error Is Returned

The Key lacks model permission, the IP is not on the allowlist, the workspace is not authorized, or the account status is restricted. Check Key permissions and workspace policies.

### A 404 Error Is Returned

The Base URL, Workspace ID, protocol path, or Model ID is incorrect. Do not use a console-page URL as an API address.

### A 429 Error Is Returned

An RPM, TPM, concurrency, or task-queue limit has been reached. Reduce concurrency, shorten the context, and wait for recovery. Do not retry immediately in a loop.

### Insufficient Balance or Exhausted Quota

Check the account balance, free allowance, workspace budget, and model billing method. Different models may use separate allowance pools.

### The Model List Is Empty

Check the region, API Key, Base URL, and network proxy. You can also copy a complete Model ID from the model page for the current region and add it manually.

### A Preset Model Does Not Work

The V2 preset may predate a Bailian model retirement or regional change. Synchronize again and use the current regional model list as the source of truth.

### Standard Chat Works, but Agent or Code Tools Do Not

Check whether the Anthropic Base URL still points to the default Beijing address and whether the target model supports the Anthropic-compatible protocol and tool calling.

### Image Generation Returns the Wrong Address

Check that the OpenAI Base URL contains the correct workspace domain and `/compatible-mode/v1/` suffix. V2 derives the native image API host from it.

### An Image Task Keeps Waiting

The task may still be queued, network polling may have failed, the allowance may be insufficient, or the model may be busy. Review the error and Bailian task status first instead of submitting the task again.

### A Rerank Model Can Be Selected but Has No Effect

Confirm that the model has not been retired, the regional API is compatible, and the knowledge base actually enabled Rerank. If necessary, turn reranking off temporarily and verify Embedding retrieval first.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For current Bailian regions, Keys, and models, see [Regions and endpoints](https://help.aliyun.com/zh/model-studio/regions/), [Get an API Key](https://help.aliyun.com/zh/model-studio/get-api-key/), [Choose a model](https://help.aliyun.com/zh/model-studio/models), [Embeddings and reranking](https://help.aliyun.com/zh/model-studio/embedding-rerank-model/), and [Image generation and editing](https://help.aliyun.com/zh/model-studio/image-model). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
