# Huawei Cloud ModelArts Studio (MaaS)

Huawei Cloud ModelArts Studio (MaaS) provides inference APIs for built-in and custom-deployed models. Cherry Studio V2 currently has no built-in Huawei Cloud provider, so you must create an **OpenAI-compatible custom provider**.

{% hint style="info" %}
Older tutorials instruct you to enter the complete `/chat/completions` address in API Host and append `#`. V2 does not need this legacy compatibility format. Remove `/chat/completions` from the complete invocation address and keep only the Base URL.
{% endhint %}

## Choose an Integration Method First

Huawei Cloud MaaS commonly provides two invocation methods:

| Method | Address pattern | Cherry Studio configuration |
| --- | --- | --- |
| MaaS Standard API | Several built-in models share a `/v1` or `/v2` Base URL | One custom provider is usually sufficient |
| Custom real-time inference service | Each service may have an independent URL, Endpoint, or path | Create separate providers for different Base URLs |

This page applies only to OpenAI-compatible MaaS services that use a Bearer API Key. IAM Tokens, AppKey/AppSecret, AppCode, or signature authentication from older ModelArts versions cannot be entered directly in Cherry Studio's standard API Key field.

## Regions and Versions

Available MaaS regions, API Keys, and model lists are linked and cannot be mixed across regions.

The current MaaS Standard API V2 example in Huawei Cloud's international documentation is:

```text
https://api-ap-southeast-1.modelarts-maas.com/v2/chat/completions
```

In Cherry Studio, enter:

```text
https://api-ap-southeast-1.modelarts-maas.com/v2
```

MaaS Standard API V1 is no longer actively evolving. For a new configuration, prefer the V2 address provided by the console. For an existing V1 service, follow the console's Invocation Instructions.

{% hint style="warning" %}
Do not copy the example address from this page directly. Check the Invocation Instructions in your own Huawei Cloud region and service page first. If the console provides a different domain or version, use the console address.
{% endhint %}

## Activate MaaS

1. Register and sign in to [Huawei Cloud](https://auth.huaweicloud.com/authui/login);
2. Switch to a region currently supported by MaaS;
3. Open ModelArts Studio (MaaS);
4. Complete IAM authorization as instructed by the console;
5. Select a model in the model hub;
6. Activate a built-in service or deploy it as a real-time inference service;
7. Wait until the service status indicates that it can be called.

A custom deployment uses compute and storage resources and incurs charges. Do not select "Deploy All" without understanding the billing method.

## Create an API Key

### Built-In MaaS Service

1. Open MaaS API Key management;
2. Click **Create API Key**;
3. Set a label;
4. Configure an IP, model, or custom Endpoint allowlist as needed;
5. Copy and save the Key immediately after creating it.

### Custom Real-Time Inference Service

1. Open `Model Inference → Real-Time Inference → My Services`;
2. Find the running service;
3. Select `More → View Invocation Instructions`;
4. Click **Create API Key**;
5. Configure permissions and copy the Key;
6. Copy the complete API URL and model parameters as well.

A MaaS Key may take several minutes to become active after creation.

{% hint style="danger" %}
An API Key is shown only once during creation. Do not put it in chats, documents, code repositories, or troubleshooting screenshots. Delete and replace it if it is lost or exposed.
{% endhint %}

## Extract the Base URL from a Complete URL

Suppose the console provides this complete address:

```text
https://example.com/v2/chat/completions
```

Enter the following in Cherry Studio:

```text
https://example.com/v2
```

Rules:

1. Remove the trailing `/chat/completions`;
2. Keep `/v1` or `/v2`;
3. Do not append `#`;
4. Do not add the model name to the URL;
5. Do not use a console-page URL as an API URL.

If the Invocation Instructions for a custom service use a different path, first confirm that it supports OpenAI Chat Completions. A non-compatible API cannot be connected merely by removing a path.

## Create a Custom Provider in Cherry Studio

1. Open `Settings → Model Providers`;
2. Click **Add Provider**;
3. Enter a name, such as `Huawei Cloud MaaS`;
4. Select the **OpenAI-Compatible** type;
5. Paste the MaaS API Key;
6. Enter the extracted Base URL;
7. Turn on the provider switch;
8. Synchronize models or add the Model ID manually;
9. Enable only the models you plan to use;
10. Run a model health check.

If all models share the same MaaS Standard API Base URL, you can keep them in one provider. Create another provider only when the Base URL, authentication, or proxy path differs.

## Get and Synchronize Models

The MaaS Standard API provides model-list endpoints:

```text
GET /v1/models
GET /v2/models
```

The specific version depends on the Base URL provided by the console.

After synchronization:

1. Check the returned Model IDs;
2. Apply the synchronization results;
3. Confirm model types;
4. Run a health check for each model.

If a custom service does not provide a model-list endpoint:

1. Copy the `model` parameter from the Invocation Instructions;
2. Add it manually in Cherry Studio;
3. Preserve capitalization and punctuation exactly;
4. Run a health check.

{% hint style="warning" %}
An API Key can have model and custom Endpoint allowlists. If a model exists but returns a 401, check the Key permissions instead of only copying the Key again.
{% endhint %}

## Chat Models

The MaaS Standard API uses OpenAI-compatible Chat Completions.

Test in this order:

1. Send a short plain-text message;
2. Check streaming output;
3. Add a system prompt;
4. Test a longer context;
5. Then test reasoning, images, and tool calls.

Allowed `role` values, context lengths, and output parameters vary by model. If a 400 occurs, compare the request with the MaaS API invocation specification for that model.

## Reasoning Mode

Different models on Huawei Cloud MaaS may use:

- `reasoning_content`
- `thinking`
- `chat_template_kwargs`
- Model-specific switches

Cherry Studio currently has no Huawei Cloud-specific parameter integration. The reasoning parameters generated by V2 for a generic OpenAI-compatible provider may not exactly match a particular MaaS model.

If enabling reasoning causes an error:

1. Restore the reasoning setting to **Default**;
2. Clear custom model parameters;
3. Confirm that standard chat works first;
4. Review the request example for the model in MaaS;
5. Add only parameters explicitly required by the official documentation.

Do not copy one model's `chat_template_kwargs` to another model.

## Vision and Multimodal Models

Only a model explicitly marked by MaaS as vision or multimodal can receive images.

When testing:

1. Add the exact Model ID;
2. Confirm that Cherry Studio shows image support;
3. Upload one small image first;
4. Check whether the model actually understands the content;
5. Then try multiple images or large files.

Even if a custom real-time service deploys a vision model, it must use an OpenAI-compatible image-message format to connect directly from Cherry Studio.

## MCP and Tool Calling

Some MaaS Standard API V2 models support Tool Calling, but the final capability depends on the model.

1. Complete a standard chat first;
2. Enable only one simple MCP tool;
3. Explicitly request a tool call;
4. Check whether it produces a structured call;
5. Confirm that the tool result can be returned to the model;
6. Add more tools afterward.

A model saying that it will call a tool is not an actual call. Check the model, API version, and tool format.

## Embedding, Rerank, and Image Generation

Cherry Studio currently has no Huawei Cloud-specific Embedding, Rerank, or image-generation integration.

Attempt one only when all of the following conditions are met:

1. The MaaS service provides the corresponding OpenAI-compatible API;
2. Cherry Studio can select the correct Endpoint Type for the model;
3. The request and response formats are compatible with V2;
4. A health check or small real-world test succeeds.

Do not assume that a Cherry Studio knowledge base or image-generation page has integrated a model only because the MaaS console supports it.

For knowledge bases, the safest option is to use Embedding and Rerank providers explicitly supported by V2. For image generation, use providers and models actually listed on the image-generation page.

## PDFs and Attachments

V2 currently extracts PDF text locally before sending it to a MaaS chat model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes model context and incurs cost;
- Images in a PDF must be sent separately to a vision model.

This is not the same as Huawei Cloud's native file-upload or document-understanding APIs.

Before uploading documents, images, or knowledge-base content, confirm compliance with data-region, privacy, and organization security requirements.

## Custom Real-Time Services

For a custom real-time service, also check:

- Whether the service is running;
- Whether the resource pool and OBS are in the same region as MaaS;
- Whether the Endpoint is in the Key allowlist;
- Whether content moderation is enabled;
- QPS and timeouts;
- Compute and storage costs;
- Service upgrade or stopped status.

If each custom service has a different Base URL, create a separate provider for each URL. When several models share one standard Base URL, you do not need to create duplicate providers.

## Troubleshooting

### A 401 Error Is Returned

The API Key is incorrect, not yet active, or in the wrong region, or the IP, model, or Endpoint is not in the Key allowlist. Check Key permissions and retry.

### A 403 Error Is Returned

IAM authorization, model permissions, content moderation, or account status is restricted. Check the specific error code in the MaaS console.

### A 404 Error Is Returned

The Base URL, API version, path, or Model ID is incorrect. Copy the complete URL again from View Invocation Instructions and remove `/chat/completions` according to the rules.

### A 429 Error Is Returned

The QPS or concurrency limit of MaaS, the model, or the custom real-time service has been reached. Reduce concurrency and wait for recovery.

### A 400 Error Is Returned

The model does not accept the current message role, attachment, or reasoning parameter. Clear custom parameters and test a minimal plain-text request first.

### The Model List Is Empty

A custom service may not provide `/models`. Copy the `model` parameter from the Invocation Instructions and add it manually.

### A Newly Created Key Is Reported as Invalid

A MaaS Key may take several minutes to become active. Confirm the Key, region, and Base URL, then wait and retry.

### Does Every Model Need a Separate Provider?

Not necessarily. Models that share the same MaaS Standard API Base URL and Key can stay in one provider. Split them only when the invocation address or authentication differs.

### Why Do Older Tutorials Append `#`?

That is a legacy compatibility method used when older Cherry Studio versions accepted a complete API address. V2 should use the Base URL after removing `/chat/completions` and should not append `#`.

### A Custom Service Works on the Website but Not in Cherry Studio

The service may use a non-OpenAI format, older AppCode or signature authentication, a custom path, or a Key allowlist that does not include the Endpoint. A generic custom provider cannot automatically adapt these differences.

### Enabling Reasoning Causes a Parameter Error

Restore the default reasoning setting. The current V2 has no Huawei Cloud MaaS-specific reasoning parameter integration.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For current Huawei Cloud MaaS invocation methods, see the [API Invocation Specification](https://support.huaweicloud.com/intl/zh-cn/model-call-maas/model-call-017.html), [MaaS Standard API V2](https://support.huaweicloud.com/intl/zh-cn/model-call-maas/model-call-019.html), [Invoke Model Services](https://support.huaweicloud.com/intl/zh-cn/inference-maas/maas-modelarts-0011.html), and [API URL Format](https://support.huaweicloud.com/intl/zh-cn/maas_faq/maas_faq_0005.html). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
