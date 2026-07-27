---
icon: shuffle
---

# OneAPI

OneAPI is a gateway that converts multiple upstream large-model channels into an OpenAI-compatible interface. Administrators configure upstream keys, models, and routing in OneAPI, while standard users connect Cherry Studio with tokens issued by OneAPI.

Cherry Studio V2 does not include a separate built-in OneAPI provider. OneAPI and NewAPI share the **New API** compatibility integration. For a standard OneAPI instance, the model endpoint type is usually **OpenAI Chat Completions**.

{% hint style="warning" %}
Requests pass through the OneAPI instance and its upstream channels. Use only services you deploy yourself or explicitly trust, with legitimate upstream authorization and compliance responsibility. Unknown public instances may log requests, expose attachments, or bill incorrectly.
{% endhint %}

## Differences between OneAPI and NewAPI

OneAPI is an earlier unified gateway project. NewAPI continues to expand a similar architecture with more native protocols, endpoint types, and model metadata.

| Project | Recommendation in Cherry Studio |
| --- | --- |
| OneAPI | Use a New API-compatible provider and handle models as OpenAI Chat Completions by default |
| NewAPI | Use the dedicated New API type and select Chat, Responses, Anthropic, Gemini, Image, or Rerank for each model |

If the instance has secondary development or a customized theme, you cannot identify the project from its appearance alone. Ask the administrator to confirm the server version and supported API protocols.

## Confirm your role first

Standard users need only the instance address and a user token. Administrators must also maintain upstream channels:

| Role | Preparation |
| --- | --- |
| Standard user | Create a dedicated token and confirm quota, group, and model permissions |
| Administrator | Configure upstream channels, model mappings, multipliers, groups, and failover |

Do not enter keys from upstream providers such as OpenAI or Anthropic directly in the Cherry Studio OneAPI connection. The client should use the token issued by OneAPI.

## Create a token in OneAPI

1. Sign in to a trusted OneAPI instance;
2. Open the **Tokens** page;
3. Create a token dedicated to Cherry Studio;
4. Set its name, quota, expiration, and available models as needed;
5. Copy the token and store it securely;
6. Use OneAPI's built-in test function to verify one model.

Sharing the default token long-term is not recommended. A dedicated token makes usage easier to audit, limit, and revoke separately.

{% hint style="danger" %}
Do not include the OneAPI token in chat messages, documents, code repositories, or issue screenshots. If exposed, delete it immediately in the OneAPI console and create a new one.
{% endhint %}

## Get the API Base URL

OneAPI's official OpenAI-compatible format usually uses:

```text
https://your-oneapi.example.com/v1
```

Cherry Studio's New API compatibility integration appends `/v1` to the site root, so both of these formats work:

- `https://your-oneapi.example.com`
- `https://your-oneapi.example.com/v1`

A local or LAN deployment can also use:

- `http://localhost:3000`
- `http://192.168.1.20:3000`

Notes:

- `http` and `https` must match the actual server configuration;
- A public internet service should use a valid HTTPS certificate;
- `/console/...`, login pages, and token pages are not the API Base URL;
- Do not enter a specific `/chat/completions` path.

## Configure in Cherry Studio

If you do not use another NewAPI gateway, you can configure the built-in **New API** provider directly. If another instance is already configured, first duplicate or add a New API-compatible provider to avoid overwriting the existing configuration.

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**;
3. Select **New API**, or add a provider based on the New API template;
4. Rename it to an easily recognizable OneAPI instance name;
5. Enter the OneAPI user token;
6. Enter the OneAPI Base URL;
7. Turn on the provider switch at the top of the page;
8. Click **Add** to sync the model list;
9. Set the endpoint type for standard OneAPI models to **OpenAI Chat Completions**;
10. Enable only the models you plan to use.

OneAPI's `/models` response usually does not include `supported_endpoint_types` from newer NewAPI versions. Cherry Studio may therefore ask you to select an endpoint type during bulk addition, which is normal.

## Add models

Prefer syncing models from the server instead of copying model names from another instance.

If synchronization fails, add a model manually:

1. Confirm the complete model ID visible to the token in the OneAPI console;
2. Click **Add Model** in Cherry Studio;
3. Enter the exact same model ID;
4. Select **OpenAI Chat Completions** as the endpoint type;
5. Save and run a health check.

You can customize the display name, but the actual model ID must match an available model or mapping name in OneAPI.

{% hint style="info" %}
OneAPI maps the model ID requested by the client to an upstream model. If the model does not exist, check the ID in Cherry Studio, the OneAPI channel model, and the model mapping configured by the administrator together.
{% endhint %}

## Capability boundaries

OneAPI primarily normalizes different upstream providers into an OpenAI-compatible format. Basic chat is generally the most reliable, while newer native capabilities may not be fully preserved.

- Native Claude thinking blocks may be converted or lost;
- Native Gemini multimodal structures may be restricted by the instance version;
- OpenAI Responses-only capabilities are not equivalent to Chat Completions;
- Tool calls require OneAPI and the upstream provider to convert `tools` and `tool_calls` correctly;
- Provider-specific parameters such as Web Search, caching, or Service Tier may not take effect;
- A visible model list does not mean every parameter combination works.

If a workflow depends on the latest native capabilities of a provider, prefer the original model provider or a newer NewAPI version that supports the corresponding native endpoint.

## Tool calls and MCP

You can connect MCP with a OneAPI model that supports Function Calling, but run a minimal test first:

1. Select a model explicitly marked as supporting tool calls;
2. Complete a standard chat;
3. Enable only one simple MCP tool;
4. Explicitly ask the model to call that tool;
5. Confirm that the tool request appears in the OneAPI logs;
6. Then add more tools.

If the model outputs only a call plan, the upstream model may not support tools, the OneAPI conversion may be incomplete, or the channel may have removed the tool fields. Test the same model directly in OneAPI first.

## Knowledge bases and embedding models

When a OneAPI instance exposes a compatible Embeddings endpoint, you can use its embedding models for knowledge bases or [Global Memory](../../advanced-basic/memory.md).

- Add only embedding models actually provided by the instance;
- Do not use a chat model as an embedding model;
- Chat and embeddings can use different providers;
- Run health checks separately;
- Verify the OneAPI and upstream billing multipliers.

Older instances or certain channels may not have an embedding endpoint. A model name existing does not mean `/v1/embeddings` is available.

## PDFs and attachments

OneAPI is an aggregation gateway, so Cherry Studio does not assume native PDF support based only on the model name.

The current V2 version extracts PDF text locally first and then sends it to OneAPI:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes input tokens;
- Multimodal attachments such as images still depend on the instance and upstream capabilities.

## Administrator checklist

Before issuing tokens to users, administrators should confirm:

1. Upstream channel tests succeed;
2. Models enabled on each channel match the actual permissions;
3. Model mappings contain no spelling errors;
4. The user group can access the target channel;
5. Model and group multipliers are correct;
6. Token restrictions match the user's purpose;
7. `/v1/models` and `/v1/chat/completions` are both available;
8. Critical models pass a tool-call test.

With load balancing across multiple channels, the same model may be routed to different upstream providers. For stable behavior, reduce inconsistent channels or ask the administrator to pin a channel using a method supported by OneAPI.

## Check the connection

1. Verify the same token using OneAPI's built-in test or a compatible request;
2. Run the provider connection check in Cherry Studio;
3. Click **Add** and confirm that the model list can be synced;
4. Check that the endpoint type is OpenAI Chat Completions;
5. Run the model health check;
6. Return to the chat interface and send a simple message;
7. Then test tool calls, attachments, or the knowledge base.

If the server-side test also fails, check the OneAPI channel, token, and upstream provider first. If only Cherry Studio fails, focus on the Base URL, model ID, and endpoint type.

## Troubleshooting

### Response code 401

The token is invalid, deleted, expired, or incomplete. Confirm that you entered a OneAPI user token, not an upstream provider key.

### Response code 403

The token cannot access the target model, its quota is exhausted, or its group cannot access an available channel. Contact the instance administrator.

### Response code 404

The Base URL contains an administration page or specific endpoint path, or the instance does not expose the standard OpenAI-compatible route. Restore it to the site root or `/v1`.

### The model list is empty

The token has no visible models, the channel is disabled, the group does not match, or the instance version returns an incompatible `/models` response. Test in OneAPI first and confirm `/v1/models`.

### The model exists but calls fail

Check the OneAPI model mapping and upstream channel. The model name in the list is only an entry point; the actual route may still be unavailable or unauthorized.

### Thinking content, Web Search, or tool capabilities are missing

OneAPI's OpenAI format conversion may not preserve native provider fields. Compare with a simple Chat Completions request. For complete native capabilities, use the original provider or the corresponding NewAPI endpoint.

### Request results are inconsistent

Multiple channels may have inconsistent model versions, parameter support, or balances. Ask the administrator to check channel tests, priorities, weights, and automatic disable status.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). If the instance is actually NewAPI, see [NewAPI](newapi.md). For the OneAPI project, see the [official repository](https://github.com/songquanpeng/one-api); for feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
