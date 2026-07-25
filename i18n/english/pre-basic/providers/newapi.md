---
icon: arrows-rotate
---

# NewAPI

NewAPI is a unified large-model gateway. It connects to upstream OpenAI, Anthropic, Google, and other channels on the server, then provides Cherry Studio with unified model listing, authentication, routing, and billing endpoints.

Cherry Studio V2 includes a dedicated **New API** provider type, so you no longer need to disguise it as a standard OpenAI provider. The dedicated type can select OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, Google Generate Content, image generation, or reranking endpoints for each model.

{% hint style="warning" %}
Requests pass through the NewAPI instance and its configured upstream channels. Use only services you deploy yourself or explicitly trust, with legitimate upstream authorization and compliance responsibility. Do not provide sensitive data or API Keys to unknown public instances.
{% endhint %}

## Confirm your role first

Standard users and NewAPI administrators have different preparation tasks:

| Role | Required work in NewAPI |
| --- | --- |
| Standard user | Create a token and confirm quota, group, model permissions, and IP restrictions |
| Administrator | Configure and test upstream channels, model mappings, groups, and billing before issuing tokens to users |

If you use an instance maintained by someone else, do not enter the upstream provider's key in Cherry Studio. Enter only the user token issued by that NewAPI instance.

## Create a token in NewAPI

1. Sign in to a trusted NewAPI instance;
2. Open the **Tokens** page;
3. Create a token dedicated to Cherry Studio;
4. Set quota, expiration, model restrictions, group, and IP allowlist as needed;
5. Copy the token and store it securely;
6. Test one model in NewAPI's built-in Playground first.

We recommend creating separate tokens for different devices or purposes. If one is exposed, you can revoke only the affected token and review its usage more easily.

{% hint style="danger" %}
Do not include the NewAPI token in chat messages, documents, code repositories, or issue screenshots. If exposed, delete it immediately in the NewAPI console and create a new one.
{% endhint %}

## Get the correct API address

Prefer the API Base URL shown on the NewAPI home page, or confirm it with the instance administrator. Common formats include:

| Deployment | Example |
| --- | --- |
| HTTPS domain | `https://newapi.example.com` |
| Version path already included | `https://newapi.example.com/v1` |
| Local deployment | `http://localhost:3000` |
| LAN IP | `http://192.168.1.20:3000` |

Cherry Studio appends `/v1` to a standard NewAPI address and does not append it again when `/v1` is already present. You can therefore enter either the site root or a standard `/v1` Base URL.

- `http` and `https` must match the actual server configuration;
- A public internet instance should use a valid HTTPS certificate;
- `/console/...` from a browser administration page is not the API Base URL;
- Do not enter the token page, login page, or a specific `/chat/completions` path as the Base URL.

## Configure New API

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**;
3. Select the built-in **New API** provider;
4. Enter the token issued by NewAPI;
5. Change the Base URL to the instance's API address;
6. Turn on the provider switch at the top of the page;
7. Click **Add** to sync the model list;
8. Review the models and endpoint types, then apply the changes;
9. Enable only the models you plan to use.

The built-in template defaults to `http://localhost:3000`, which applies only to a default local deployment. Replace it with the actual address when connecting to a remote instance.

If the NewAPI administrator configured a Cherry Studio one-click import link, you can use it to prefill the address and token. Still verify the target domain before importing to prevent a malicious link from sending the key to the wrong server.

## Understand endpoint types

The same model name in NewAPI may support one or more protocols. Cherry Studio selects a different request implementation according to the model's endpoint type:

| Cherry Studio endpoint type | Typical use |
| --- | --- |
| OpenAI Chat Completions | Most OpenAI-compatible chat models |
| OpenAI Responses | OpenAI models with native Responses API support |
| Anthropic Messages | Claude or other native Messages-compatible models |
| Google Generate Content | Native Gemini protocol |
| OpenAI Image Generation | Generation and editing models on the painting page |
| Jina Rerank | Knowledge-base reranking models |

In the `/models` response, newer NewAPI instances return `supported_endpoint_types`, and Cherry Studio reads this information during synchronization.

If the server does not return endpoint metadata:

- When adding in bulk, select the endpoint type shared by that batch of models;
- Add models that use different protocols in separate batches;
- Select at least one endpoint type when adding a model manually;
- Select only protocols the NewAPI instance actually supports;
- Do not guess based only on the model name.

An incorrect endpoint type can cause 404 errors, incompatible parameters, lost tool calls, or failed image requests. Seeing a model in the list does not mean every protocol is available.

## Administrators: check channels and model mappings first

If you maintain the NewAPI instance, complete these checks before allowing users to connect Cherry Studio:

1. Every upstream channel passes the NewAPI channel test;
2. Models selected for the channel match the actual permissions;
3. Model mappings use the model ID that the client will request;
4. The group containing the user token can access the corresponding channel;
5. Billing multipliers, quotas, and automatic disable policies have been reviewed;
6. The models returned by `/v1/models` match the user's permissions;
7. Test Chat, Responses, Messages, Gemini, and image endpoints separately.

A model mapping converts the name requested by Cherry Studio into an upstream name. If a health check returns model not found, check the Cherry Studio model ID, NewAPI model mapping, and actual upstream channel ID together.

## Chat, thinking, and tool calls

NewAPI is only the routing layer. Final capabilities depend on the upstream model, channel type, protocol conversion, and instance version.

- Thinking options must match the target model and endpoint type;
- Prefer Anthropic Messages for native Claude capabilities;
- Prefer OpenAI Responses for native OpenAI Responses features;
- Prefer Google Generate Content for native Gemini capabilities;
- MCP requires the model, upstream, and conversion layer to preserve tool fields;
- If multi-turn tool calls fail, troubleshoot with one tool first.

A model working in standard chat does not guarantee complete thinking content, tool calls, Web Search, or structured output. Run separate health checks for important workflows instead of testing only one “Hello.”

## Painting, embeddings, and reranking

Cherry Studio's NewAPI integration can also use:

- OpenAI-compatible image generation and image editing;
- OpenAI-compatible embedding models;
- Jina-compatible reranking models.

The NewAPI instance must expose the corresponding endpoint, and the model must use the correct endpoint type.

### Painting models

1. Sync or manually add an image model;
2. Set the endpoint type to **OpenAI Image Generation**;
3. Enable the model;
4. Select the NewAPI provider on the painting page;
5. Test generation and editing separately.

Successful image generation does not mean image editing is also supported. They may use different upstream endpoints, parameters, and billing methods.

### Embeddings and reranking

- Embedding models use the Embeddings endpoint for knowledge bases and [Global Memory](../../advanced-basic/memory.md);
- Reranking models require **Jina Rerank**;
- Chat, embedding, and reranking models can come from different upstream providers;
- Run health checks separately and verify the multipliers.

## PDFs and attachments

NewAPI is an aggregation gateway. Cherry Studio does not assume that the gateway fully supports native PDFs merely because a model name contains Claude, Gemini, or OpenAI.

The current V2 version extracts PDF text locally first and then sends the text to NewAPI:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text counts toward input tokens;
- For native multimodal attachments, use a verified endpoint and model.

## Check the connection

We recommend troubleshooting from the server to the client:

1. Test the target model in the NewAPI Playground with the same token;
2. Run the provider connection check in Cherry Studio;
3. Click **Add** and confirm that models can be synced;
4. Check the model endpoint type;
5. Run the model health check;
6. Return to the chat interface and send a standard message;
7. Then test thinking, MCP, painting, or the knowledge base.

If the Playground also fails, the problem is usually the NewAPI token, channel, balance, or upstream provider. If the Playground works but Cherry Studio fails, focus on the Base URL, endpoint type, and client version.

## Troubleshooting

### Response code 401

The token is invalid, deleted, expired, or incomplete. Confirm that you entered a NewAPI user token, not an upstream provider key.

### Response code 403

The token's model permissions, group, or IP allowlist do not permit the current request. Ask the instance administrator to check the intersection of the token, channel, and group.

### Response code 404

The Base URL contains a console path, the endpoint type is incorrect, or the server does not expose the route. Restore the site root or a standard `/v1` address and try again.

### The model list is empty

The token has no available models, the channel is disabled, the group does not match, or an older NewAPI `/models` response is incompatible. Check the NewAPI Playground and `/v1/models` first.

### The model exists but returns “not supported”

Check the model mapping, upstream channel, and Cherry Studio endpoint type. A model appearing in `/models` means only that it is visible, not that the current combination of protocol and parameters works.

### Quota or multiplier error

Check the user balance, token quota, group multiplier, model multiplier, and upstream account balance. The upstream channel may still be out of credit even when NewAPI quota is available.

### MCP only outputs a call plan

Confirm that the model supports tool calls and that the NewAPI version and channel preserve `tools`, `tool_calls`, and tool results. Start with one simple tool and try the model's native protocol.

### A painting model appears in the chat list

Edit the model, change its endpoint type to **OpenAI Image Generation**, and use it on the painting page. An image generation model is not a standard chat model.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For NewAPI usage and administration, see the [official documentation](https://docs.newapi.pro/); for feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
