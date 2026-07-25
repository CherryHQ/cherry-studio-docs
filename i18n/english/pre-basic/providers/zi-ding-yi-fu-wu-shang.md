# Custom Providers

Custom providers let you connect Cherry Studio to cloud platforms that are not yet built in, OpenAI-compatible proxies, LAN gateways, or self-hosted model services.

Cherry Studio V2 provides two ways to create one:

| Method | Best for | Main characteristic |
| --- | --- | --- |
| Add a custom provider | New platforms, OpenAI-compatible services, and local inference services | Uses OpenAI Chat Completions as the primary chat protocol by default |
| Add an instance from a preset provider | A second account, region, gateway, or private address for the same vendor | Retains the original provider's authentication method, default protocol, and dedicated adaptations |

{% hint style="info" %}
If the target platform already has a preset provider, add another instance of that provider first. A fully custom provider is intended for standard compatible APIs and does not automatically gain vendor-specific authentication, image tasks, or parameter adaptations.
{% endhint %}

## Before You Begin

Before creating a provider, confirm the following in the target service's official documentation:

1. Which API protocol it uses;
2. The Base URL, rather than the web console address;
3. The API Key or other authentication method;
4. Whether the model list endpoint is available;
5. The complete Model ID you plan to call;
6. Whether the model supports vision, reasoning, tools, Embedding, or Rerank;
7. Whether extra request headers are required;
8. Whether there are IP allowlist, proxy, or certificate requirements.

API compatibility alone is not enough. Response fields, streaming format, tool calls, reasoning content, and error structures must also be compatible with the selected protocol.

## Choose a Creation Method

### Add a Fully Custom Provider

This method is suitable for:

- OpenAI-compatible cloud services;
- Unified gateways such as OneAPI and NewAPI;
- Self-hosted services such as vLLM and LocalAI;
- Compatible internal enterprise proxies;
- Platforms that are not yet included in the preset list.

The default primary endpoint for a fully custom provider in V2 is:

```text
OpenAI Chat Completions
```

When creating one, the legacy “OpenAI / Gemini / Anthropic / Azure OpenAI” provider-type dropdown is no longer used.

### Add an Instance from a Preset Provider

This method is suitable when:

- You use multiple independent accounts for the same provider;
- Different regions use different Base URLs;
- A company proxy and the official endpoint are both needed;
- You need to retain dedicated authentication for Azure, Vertex AI, Bedrock, or similar services;
- You need to retain provider-specific image, reasoning, or model synchronization adaptations.

In the preset provider's group, click **Add Instance**, or open the provider menu and choose the same action. After the new instance is created, enter its own authentication information and address.

{% hint style="warning" %}
Copying a preset provider copies only the configuration structure, not sensitive credentials from the original instance. Enter the authentication information again on the new instance's details page.
{% endhint %}

## Add a Fully Custom Provider

1. Open `Settings → Model Providers`;
2. If necessary, switch the filter to **All Providers**;
3. Click `+` to the right of the provider search box;
4. Enter a provider name that is easy to recognize;
5. Optionally choose a built-in icon or upload your own;
6. Enter the primary Base URL;
7. Optionally enter the first API Key;
8. If the platform also provides other compatible protocols, expand **More Endpoints**;
9. Click **Add**;
10. Open the new provider's details page to continue configuring models.

The name affects only how the provider is displayed; it does not change the request protocol. Consider including the platform, region, or purpose in the name, such as “Internal Gateway-Shanghai.”

## Enter a Base URL

The Base URL is the API root address, not a complete request URL.

For OpenAI Chat Completions, for example:

```text
Correct: https://api.example.com/v1
Incorrect: https://api.example.com/v1/chat/completions
Incorrect: https://console.example.com/models
```

V2 appends the specific request path according to the endpoint type. Whether `/v1`, `/v1beta`, or a custom path is required depends on the target service's official documentation.

{% hint style="warning" %}
Do not copy a “proxy address” from another client unless you have confirmed that it expects a Base URL. The same platform may require a root address in one tool and a complete request URL in another.
{% endhint %}

### Localhost and LAN Addresses

A common address for a local service is:

```text
http://127.0.0.1:8000/v1
```

If the service runs in Docker, a virtual machine, or another computer, `localhost` may refer to a different device. Use an address that is accessible from the computer running Cherry Studio, and verify the firewall and listening network interface.

For an HTTPS service using a self-signed certificate, system certificate validation may also block the connection. Do not disable security validation for the entire computer just to resolve a certificate issue.

## Configure More Endpoints

The fully custom provider creation page can also accept:

- Anthropic Messages;
- Google Gemini;
- OpenAI Responses.

After creation, you can also open **Request Configuration** to the right of API Host to add or modify endpoints.

These addresses describe different protocol entry points offered by the same provider. They do not automatically turn a model that supports only OpenAI into an Anthropic or Gemini model.

For a regular manually added custom model, the primary protocol still follows the provider's default endpoint. If a vendor-specific protocol or dedicated authentication is required, add an instance from the corresponding preset provider first.

## API Keys and Multiple Keys

You can enter the first API Key during creation, or leave it blank and configure it later.

On the provider details page, you can:

- Add multiple keys;
- Add a recognizable label to each key;
- Pause a key;
- Delete an expired or exposed key.

Only enabled keys can be used for requests. Whether multiple keys have access to the same models, balance, and organization permissions is still determined by the server.

{% hint style="danger" %}
Do not put a real API Key in documentation, chats, public repositories, screenshots, or custom request-header examples. Revoke it on the server immediately if it is exposed.
{% endhint %}

A local service that does not require authentication can leave the key blank. Do not enter production credentials arbitrarily just to satisfy a form.

## Custom Request Headers

Click the request-configuration button to the right of API Host to enter additional request headers as a list or JSON.

Common uses include:

- Organization or project identifiers;
- Tenant headers required by enterprise gateways;
- Version headers required by proxies;
- Custom authentication headers explicitly required by the server.

Before entering headers:

1. Add only fields explicitly required by the official documentation;
2. Do not redundantly override `Content-Type`;
3. Do not configure a conflicting `Authorization` value in both the API Key and custom headers;
4. JSON mode must contain an object;
5. Object values are sent as strings;
6. Run the connection check again after making changes.

Request headers are sent to the target address with the relevant requests. Do not send sensitive headers through an untrusted proxy.

## Enable the Provider

After creation:

1. Select the new provider;
2. Check the API Key and API Host;
3. Turn on the provider;
4. Synchronize or manually add models;
5. Enable only the models you actually need;
6. Run a health check.

If the provider is disabled, its models will not appear correctly in the relevant model selectors even if they have already been added.

## Synchronize Models

For an OpenAI-compatible service, V2 attempts to read the following endpoint by default:

```text
GET {Base URL}/models
```

If the target service implements the model list endpoint correctly, Cherry Studio displays a synchronization preview. Before applying it, check:

- Newly added models;
- Updated models;
- Models removed from the server;
- Model IDs and display names;
- Whether model capabilities were identified correctly.

A synchronization failure does not necessarily mean that the chat endpoint also fails. Some services implement Chat Completions but not `/models`; in that case, add models manually.

## Add Models Manually

1. Click **Add Model** in the model list;
2. Enter the complete Model ID required by the server;
3. Optionally enter a more readable display name and group;
4. Enter the context and maximum output limits according to the official specifications;
5. Select only the capabilities the model actually supports;
6. Save and enable the model;
7. Run a health check.

Capabilities you can mark manually include:

- Image understanding;
- Web search;
- Reasoning;
- Tool calling;
- Embedding;
- Rerank.

Capability labels are used for interface filtering and request routing; they do not change what the server can do. Incorrect labels may cause requests to fail or make Embedding and Rerank models appear incorrectly in the chat model list.

{% hint style="warning" %}
The Model ID must exactly match the value on the server. You can customize the display name, but it cannot replace the Model ID sent in requests.
{% endhint %}

## Connection Checks and Model Health Checks

Use checks in stages:

1. Check the provider connection first;
2. Then check an individual chat model;
3. Test streaming output separately;
4. Test vision, reasoning, and tool calling separately;
5. Test Embedding and Rerank in an actual knowledge-base workflow.

The generic health check in the current V2 skips Rerank models, so Rerank must be verified in the knowledge-base retrieval workflow.

A successful connection check does not mean that:

- Every model is authorized;
- The account has sufficient balance;
- Vision or tool calling is available;
- Long-context requests will always succeed;
- All server-side extension parameters are compatible.

## OpenAI-Compatible Capability Boundaries

A fully custom provider can reuse standard OpenAI-compatible capabilities:

- Chat Completions;
- Streaming output;
- Vision input;
- Function Calling;
- Embeddings;
- Standard model lists.

Availability depends on the server and the specific model. The following capabilities usually cannot be obtained automatically by declaring OpenAI compatibility:

- Vendor-native asynchronous image tasks;
- Dedicated file uploads;
- Cloud knowledge bases;
- Special reasoning parameters;
- Nonstandard Rerank;
- OAuth, IAM, or cloud-account signing;
- Vendor-specific model synchronization categories.

If the provider requires these capabilities, use a preset adaptation or dedicated documentation.

## Create a Local Provider with vLLM

vLLM provides an OpenAI-compatible server. Review the [official vLLM documentation](https://docs.vllm.ai/en/stable/serving/openai_compatible_server/) first for installation instructions and hardware requirements.

Start the service with a model that supports a chat template:

```sh
vllm serve NousResearch/Meta-Llama-3-8B-Instruct \
  --dtype auto \
  --api-key local-test-token
```

The default listening port is `8000`. Add a fully custom provider in Cherry Studio:

```text
Provider Name: vLLM Local
Base URL: http://127.0.0.1:8000/v1
API Key: local-test-token
```

Then synchronize `/v1/models`, or manually add the Model ID returned by vLLM.

{% hint style="info" %}
The key above is only for a local example. A LAN or public deployment must use strong credentials, access control, TLS, and a firewall. Do not directly expose an unauthenticated inference port.
{% endhint %}

If the response says that a chat template is missing, use a model that includes one or configure `--chat-template` according to the vLLM documentation.

## PDFs, Attachments, and Privacy

For general chat models, Cherry Studio extracts PDF text locally before sending it to the server:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes context;
- Images in a PDF require a vision model.

The custom provider's Base URL determines where the data is ultimately sent. Before connecting a proxy or enterprise gateway, confirm:

- The operator's identity;
- Data-retention policies;
- Logging and training policies;
- Cross-border data transfers;
- TLS and certificates;
- Organizational compliance requirements.

## Troubleshooting

### Response Is 401

The API Key is incorrect, the authentication-header format is incompatible, or a custom request header has overridden the correct `Authorization` value. Recheck the server's authentication instructions.

### Response Is 403

The key does not have model or project permissions, the IP address is not on the allowlist, or an organization policy rejected the request.

### Response Is 404

The Base URL may have been entered as a complete request URL, the version path may be missing, or the server may not provide the endpoint. Check `/models` and `/chat/completions` separately.

### Response Is 400

The model does not support the current parameters, message format, images, reasoning, or tool calls. Test with plain text and default parameters first.

### Response Is 429

The server's request, token, or concurrency limit has been reached. Reduce concurrency and use retry backoff.

### Model Synchronization Returns No Models

The target service may not implement `/models`, or the endpoint may require different permissions. After verifying the address, add the Model ID manually.

### Chat Works, but Images Fail

A regular text model may not support vision. Check the model capabilities and the server's image-message format.

### The Model Describes a Tool but Does Not Call It

The model may not support Function Calling, or its response format may be incompatible. Verify structured tool calling with a simple tool first.

### An Embedding Model Appears in the Chat List

The model type is labeled incorrectly. Edit the model, enable the Embedding capability, and disable any unsupported chat capability.

### Rerank Cannot Pass the Health Check

The generic health check skips Rerank. Configure the model in a knowledge base and perform an actual retrieval.

### A Local Service Opens in the Browser, but Cherry Studio Still Cannot Connect

Opening the root page in a browser does not mean the API is available. Check `/v1/models`, the firewall, listening address, proxy, self-signed certificate, and chat template.

### Anthropic or Gemini Addresses Were Added, but the Model Still Uses OpenAI

The primary endpoint of a fully custom provider is OpenAI Chat Completions by default. Entering secondary endpoints alone does not guarantee that a regular manually added model will switch protocols automatically. When a vendor-specific protocol is required, add an instance from the corresponding preset provider first.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For the vLLM API, see [OpenAI-Compatible Server](https://docs.vllm.ai/en/stable/serving/openai_compatible_server/). For feedback channels, see [Feedback and Suggestions](../../question-contact/suggestions.md).
