# SiliconFlow

SiliconFlow provides chat, vision, Embedding, Rerank, and image-generation APIs. Cherry Studio V2 includes a built-in SiliconFlow provider with dedicated integrations for chat, Embedding, and image generation.

Preset API Host in V2:

```text
https://api.siliconflow.cn
```

Actual OpenAI-compatible requests use the `/v1` path, such as `https://api.siliconflow.cn/v1/chat/completions`.

{% hint style="info" %}
Keep the V2 preset address during initial configuration. Do not enter a console page, model-hub URL, or documentation address as the API Host.
{% endhint %}

## Before You Begin

1. Register and sign in to SiliconFlow;
2. Complete the account verification required by the platform;
3. Create an API Key;
4. Add funds or confirm that the account still has an available balance;
5. Check whether the model you plan to use is still online;
6. Confirm the model's price and rate limits.

SiliconFlow may adjust models, capabilities, prices, and availability. This page does not list fixed promotional credits, free models, or prices. Use the [model hub](https://cloud.siliconflow.cn/models) and console as the source of truth.

## Get an API Key

1. Sign in to the [SiliconFlow console](https://cloud.siliconflow.cn/);
2. Open [API Keys](https://cloud.siliconflow.cn/account/ak);
3. Click **Create Key**;
4. Enter a recognizable name;
5. Copy the generated Key;
6. Save it in a secure password manager.

{% hint style="danger" %}
An API Key is an account credential. Do not put it in chats, documents, code repositories, or troubleshooting screenshots. Delete and replace it immediately if it is exposed.
{% endhint %}

## Configure Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **Silicon / SiliconFlow**;
4. Paste the SiliconFlow Key into API Key;
5. Keep the API Host as `https://api.siliconflow.cn`;
6. Turn on the provider switch at the top of the page;
7. Click **Add** or synchronize models;
8. Review the synchronization preview and apply the changes;
9. Enable only the models you plan to use;
10. Run a model health check.

A successful connection check only confirms that the Key and a basic request work. It does not mean that the account can call every model in the list. SiliconFlow determines final access, balances, and rates.

## Synchronize and Add Models

Cherry Studio reads current models from SiliconFlow's model-list API. SiliconFlow's `/v1/models` endpoint can also filter by the following types:

- `chat`
- `embedding`
- `reranker`
- `text-to-image`
- `image-to-image`
- Other audio and video types

After synchronization:

1. Review added, updated, and removed items;
2. Confirm the type of each model;
3. Apply the synchronization results;
4. Delete older models that you retained manually;
5. Run separate health checks.

The built-in V2 models are only candidates; real-time platform results take priority. If a model is not automatically recognized as Embedding, Rerank, vision, or image generation, review its capabilities in model management. Do not change only its display name to bypass API differences.

{% hint style="warning" %}
The Model ID must exactly match the current SiliconFlow list, including the `Pro/` prefix, organization name, capitalization, slashes, and version suffix.
{% endhint %}

## Choose a Chat Model

SiliconFlow chat uses OpenAI-compatible Chat Completions.

Test in this order:

1. Send a short plain-text message;
2. Check streaming output;
3. Add a system prompt;
4. Test a longer context;
5. Then test images, reasoning, and tool calls.

A `Pro/` version and standard version may have different prices, throughput, or availability. Treat them as separate Model IDs and run a health check for each.

## Vision Models

Only a Model ID explicitly marked by SiliconFlow as a vision-language model can receive images.

In Cherry Studio:

1. Synchronize the latest models;
2. Select a model that shows image support;
3. Upload one small image first;
4. Check whether the model actually understands the image;
5. Then try multiple or high-resolution images.

Text and vision variants in the same model family may have different IDs. Images also increase request size, context usage, and cost.

## Reasoning Mode

Certain DeepSeek, GLM, Qwen, and Hunyuan models on SiliconFlow use `enable_thinking` and `thinking_budget`.

For supported SiliconFlow reasoning models, Cherry Studio V2:

- Uses the `enable_thinking` switch;
- Raises any nonzero reasoning budget to at least 32,768;
- Sends `enable_thinking: false` when reasoning is disabled.

This means that V2 is not currently suitable for setting a precise, smaller reasoning budget on SiliconFlow. To reduce usage, turn reasoning off, shorten the context, or choose a non-reasoning model.

If enabling reasoning causes an error:

1. Restore the reasoning setting to **Default**;
2. Clear custom model parameters;
3. Confirm that the Model ID is still online;
4. Compare your configuration with SiliconFlow's current model description;
5. Run the health check again.

## MCP and Tool Calling

SiliconFlow Chat Completions supports `tools`, but successful calls still depend on the specific model.

1. Confirm that standard chat works first;
2. Enable only one simple MCP tool;
3. Explicitly request a tool call;
4. Check whether it produces a structured call;
5. Confirm that the tool result can be returned to the model;
6. Add more tools afterward.

A model saying that it will call a tool is not an actual call. If this happens, check model capabilities, prompts, and tool definitions.

## Embedding, Rerank, and Knowledge Bases

SiliconFlow provides:

```text
POST /v1/embeddings
POST /v1/rerank
```

Currently visible example models may include `BAAI/bge-m3`, Qwen Embedding, Qwen Reranker, and BGE Reranker, but retrieve the actual list from the model hub or synchronization results.

When creating a knowledge base:

1. Synchronize models;
2. Select a model explicitly recognized as an Embedding model;
3. Detect its vector dimensions;
4. Run a health check;
5. Select a currently available Rerank model;
6. Import a small number of documents as a test;
7. Confirm retrieval and reranking results before importing in bulk.

Some Qwen Embedding models allow selecting an output dimension. Do not directly change a dimension after using it in an existing knowledge base. Doing so usually requires rebuilding the vector index.

Rerank and Embedding use different endpoints and models. A working Embedding model does not guarantee that Rerank works; check them separately.

## Image Generation and Editing

Cherry Studio V2 implements dedicated SiliconFlow image models. Requests are sent to:

```text
POST /v1/images/generations
```

The current V2 model registration focuses on Qwen Image generation and editing. Other image models on the website may not be correctly recognized by the current version. Use the options available on the Cherry Studio image-generation page as the source of truth.

Depending on the model's capabilities, V2 can pass:

- `image_size`
- `batch_size`
- `seed`
- `negative_prompt`
- `num_inference_steps`
- `guidance_scale`
- `cfg`
- `prompt_enhancement`
- Up to three editing input images

SiliconFlow uses an explicit `image_size`. V2 does not automatically convert a separate aspect-ratio parameter into a valid request. Mask input is also unsupported by the current dedicated integration.

{% hint style="warning" %}
Image models may be billed by the number of outputs. Set the batch count to 1 for the first test and use a common size supported by the model.
{% endhint %}

If the response contains an image URL, save the result promptly. SiliconFlow determines how long temporary links remain valid.

## PDFs and Attachments

V2 currently extracts PDF text locally before sending it to a SiliconFlow chat model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes model context and incurs cost;
- Images in a PDF must be sent separately to a vision model.

SiliconFlow is a cloud service. Before uploading documents, images, or knowledge-base content, confirm compliance with privacy, copyright, and organization security requirements.

## Rates, Balance, and Troubleshooting Information

SiliconFlow may calculate rate limits separately by model, with simultaneous RPM, TPM, RPD, TPD, IPM, or IPD metrics.

Recommendations:

1. Check the balance and model prices in the console;
2. Set concurrency and retry limits for automated tasks;
3. Reduce the request rate and wait after a 429 response;
4. Synchronize models regularly;
5. Save the `x-siliconcloud-trace-id` from an error response for a support ticket.

Do not create multiple Keys to evade account-level rate limits. Platform limits are usually not calculated independently per Key.

## Troubleshooting

### A 401 Error Is Returned

The API Key is incorrect, deleted, copied with an extra space, or the request did not use Bearer authentication correctly. Copy the Key again or create a replacement.

### A 403 Error Is Returned

The account, model, or content lacks permission. Check identity verification, balance, model eligibility, and platform policies.

### A 404 Error Is Returned

The API Host, Model ID, or API type is incorrect. Restore the V2 preset address and synchronize models again.

### A 429 Error Is Returned

The model's RPM, TPM, RPD, TPD, IPM, or IPD limit has been reached. Reduce concurrency, shorten the context, and wait for recovery.

### A 503 or 504 Error Is Returned

The model is busy or an upstream request timed out. Reduce concurrency and retry. If failures continue, choose another online model and record the Trace ID.

### The Model List Is Empty

Check the API Key, API Host, and network proxy. You can also copy the complete Model ID from the model hub and add it manually.

### A Preset Model Does Not Work

The V2 preset may predate a model retirement, rename, or permission change. Use real-time synchronization results as the source of truth and remove the invalid model.

### The Reasoning Budget Does Not Match the Setting

V2 currently raises any nonzero reasoning budget to at least 32,768 for supported SiliconFlow models. This is client-integration behavior. To reduce usage, turn reasoning off or choose a non-reasoning model.

### Embedding Works, but Rerank Does Not

They use different models and APIs. Confirm the Rerank Model ID, balance, and capability label, and run a separate health check.

### An Image Model Exists on the Website but Not on the Image-Generation Page

The current V2 has not registered an image-generation mode for that model. Do not use it as a chat model. Wait for integration support or select a model already available on the image-generation page.

### Image Editing Processes Only the First Image

Confirm whether the model supports multi-image editing. V2 sends up to three input images, but the specific model may accept only one.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For current SiliconFlow APIs and models, see [Model List](https://docs.siliconflow.cn/cn/api-reference/models/get-model-list), [Chat Completions](https://docs.siliconflow.cn/cn/api-reference/chat-completions/chat-completions), [Embedding](https://docs.siliconflow.cn/cn/api-reference/embeddings/create-embeddings), [Rerank](https://docs.siliconflow.cn/cn/api-reference/rerank/create-rerank), and [Image Generation](https://docs.siliconflow.cn/cn/userguide/capabilities/images). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
