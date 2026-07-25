---
description: Manage model providers, API Keys, request addresses, endpoints, and model lists in Cherry Studio V2.
icon: cloud-check
---

# Model Provider Settings

Model Providers is where Cherry Studio connects to large language, vision, embedding, and rerank models. It manages provider credentials, request addresses, protocol endpoints, and model lists. For registration and key instructions for each provider, see [Model Providers](../../../pre-basic/providers/).

{% hint style="info" %}
Different platforms may call a credential an API Key, key, token, or Token. Its exact format and permissions are determined by the provider; keys from different platforms are not interchangeable.
{% endhint %}

## Open Model Providers

Open:

> **Settings → Model Providers**

The provider list is on the left, and connection and model settings for the current provider are on the right.

The provider list supports:

- Searching by provider name, model name, or model ID;
- Viewing enabled, disabled, all, or agent-compatible providers;
- Dragging providers to change their display order;
- Expanding multiple instances created from the same preset;
- Copying, editing, or deleting manageable providers from the context menu;
- Clicking **+** beside the search box to add a custom provider.

If every provider is disabled, the list automatically shows all providers so that you can complete the first configuration.

## Configure a Built-In Provider

### 1. Select and Enable the Provider

Select a provider on the left and turn on the switch in the upper-right corner.

The provider switch only determines whether the provider is available in the application. It does not mean that the API Key, address, and models are configured correctly.

### 2. Enter the API Key

Paste the API Key created in the provider console into **API Key**.

The right side of the input usually provides options to:

- Show or hide the key;
- Copy the key;
- Open multi-key management;
- Open the connection check.

Some providers use OAuth, cloud-account identity, or device authorization and may not display a regular API Key input. Follow the provider-specific page to sign in or enter cloud-account parameters.

{% hint style="danger" %}
Do not put a real API Key in screenshots, public repositories, chat records, or feedback attachments. Hide the key before taking a screenshot. If you suspect exposure, revoke the old key in the provider console immediately.
{% endhint %}

### 3. Check the Request Address

Built-in providers usually include a default API address. Keep it unless you use a proxy, compatible gateway, or private deployment.

Example Base URL:

```text
https://api.example.com/v1
```

Do not append `/chat/completions`, `/responses`, or `/messages` to the Base URL simply because the provider documentation shows a complete request example. Cherry Studio generates the request path according to the model's endpoint type.

If the address was changed, the interface may provide **Restore Default Address**. Request Configuration also manages endpoint addresses for different protocols and custom request headers.

### 4. Check the Connection

Click **Connection Check** to the right of the API Key input.

The current V2 opens a check panel where you select:

- One enabled API Key;
- One added model that can be used for the check.

The check sends an actual request to the selected model. A successful connection means at least that this key, address, endpoint, and model can complete a basic call. It does not guarantee that every model, image, tool call, or long-context request will work.

## Manage Multiple API Keys

Click **Key List** beside the key input to:

- Add multiple keys;
- Give each key a recognizable label;
- Enable or disable a key individually;
- Edit, copy, or delete a key;
- View the number of enabled keys.

At runtime, Cherry Studio rotates through enabled keys in order. Disabled keys do not participate. If no key is enabled, a regular API Key provider cannot complete requests.

{% hint style="warning" %}
Older versions commonly stored multiple keys in one input separated by English commas. V2 is better suited to managing them individually in Key List, where each can be named, disabled, and checked separately. This also avoids accidentally using Chinese commas or treating a label as a key.
{% endhint %}

Key rotation cannot bypass provider account quotas, organization-level limits, or terms of use. Multiple keys under the same account may share billing and limits.

## API Addresses and Endpoints

### Base URL

In most cases, enter the service root address or version root path, for example:

```text
https://api.example.com/v1
```

Whether `/v1` is required depends on the provider documentation and the corresponding Cherry Studio preset. The address must be a valid `http://` or `https://` URL.

### Complete Endpoints and `#`

If a compatible service provides only a complete endpoint, retain `#` at the end of the address so Cherry Studio recognizes it and stops appending another endpoint. For example:

```text
https://api.example.com/custom/chat/completions#
```

Use this format only when the provider explicitly supplies an unusual complete path. Common recognized endpoints include:

- `chat/completions`
- `responses`
- `messages`
- `generateContent`
- `streamGenerateContent`
- Image generation or editing endpoints

Do not add `#` to a regular Base URL.

### Multiple Protocol Endpoints

Custom providers and some built-in providers can configure these endpoints separately:

| Protocol endpoint | Common use |
| --- | --- |
| OpenAI Chat Completions | Most OpenAI-compatible chat models |
| OpenAI Responses | Models using the Responses API |
| Anthropic Messages | Native Claude or compatible Messages APIs |
| Google Generate Content | Native Gemini or compatible APIs |

A gateway displaying multiple protocols does not mean that every model supports every endpoint. The model endpoint type must match the protocol actually implemented by the server.

### Custom Request Headers

Under **Request Configuration**, you can define additional request headers as a list or JSON.

Add them only when the gateway documentation explicitly requires them, such as a tenant ID or project identifier. Do not duplicate authentication headers already managed by Cherry Studio or put an API Key in multiple places.

### Provider API Options

The lightning button beside the provider name may offer:

- Array content format;
- The `developer` role;
- Stream Options;
- Service Tier;
- Reasoning switches or verbosity;
- Anthropic Prompt Cache settings.

These options change only the request format; they do not add capabilities that the server does not support. If you encounter `400`, unknown parameters, or response-format errors, restore the default options first.

## Synchronize the Model List

Click **Pull** in the model list below the provider. Cherry Studio retrieves available models from the provider and shows a synchronization preview first.

The preview usually distinguishes:

- Models newly available on the server that can be added locally;
- Models already stored locally and still present on the server;
- Local models that are no longer present in the server list;
- Items the user can choose to enable, disable, or retain.

Review the selections before applying them. Do not assume that pulling automatically enables every model on the server.

If the provider does not expose a model list endpoint, or a proxy does not implement it, use **Add** to create a model manually.

## Add and Edit Models Manually

At minimum, manual creation requires the correct **Model ID**. This is the value sent to the server in requests and must match the provider documentation exactly.

You can also configure:

- Display name;
- Group name;
- Endpoint type;
- Context window;
- Maximum input and output tokens;
- Model capabilities.

Common capability labels include:

- Vision;
- Native web search;
- Reasoning;
- Tool calling;
- Embedding;
- Rerank.

{% hint style="warning" %}
Capability labels tell Cherry Studio how to use a model; they do not change server capabilities. Incorrectly marking a regular model as supporting vision, native web search, or tool calling may cause requests to fail or prevent external tools from being injected correctly.
{% endhint %}

Embedding and rerank models are for retrieval workflows such as knowledge bases and should not be used as regular chat models.

## Model Visibility and Health Checks

The provider switch and model switch are two independent controls:

1. The provider must be enabled;
2. The specific model must also be enabled.

The model list toolbar can:

- Search models;
- Filter by capability;
- Enable or disable visible models in batches;
- Run model health checks;
- Pull server models;
- Add a model manually.

A health check is useful for testing multiple models at once. A connection check validates a specified key and model. Both may send real API requests and incur small charges.

## Add a Custom Provider

Click **+** beside the provider search box to create a custom provider.

Basic process:

1. Enter the provider name;
2. Select or upload an icon;
3. Enter the primary Base URL;
4. Optionally enter the first API Key;
5. If needed, expand **More Endpoints** and enter other protocol addresses;
6. After creation, open the details page to add more keys and models;
7. Enable the provider and run a connection check.

A new custom provider uses OpenAI Chat Completions as its primary endpoint by default. If the target service supports only Anthropic, Google, or Responses API, explicitly choose the correct protocol in endpoint and model settings.

You can also **Copy Provider** from a built-in preset to create independent configuration instances. For example, if one gateway has test and production addresses, give them separate names, keys, and enabled states.

## Recommended Configuration Order

To reduce the troubleshooting scope:

1. Enable the provider;
2. Enter one key that you have confirmed is valid;
3. Keep or verify the default API address;
4. Pull or manually add one chat model;
5. Confirm that the model is enabled;
6. Run the connection check with that key and model;
7. Return to chat and send a short message;
8. After basic calls work, add multiple keys, custom headers, and advanced endpoints.

Do not change the key, address, endpoint, request headers, and advanced options all at once at the start. If the request fails, it will be difficult to identify the cause.

## Troubleshooting

### The Provider Is Configured, but No Model Appears in the Selector

Check:

- The provider switch in the upper-right corner is enabled;
- The target model was added to the model list;
- The target model itself is enabled;
- A capability filter is not hiding the model on the current page;
- The model ID was saved successfully.

### Connection Check Reports No Model Available

Pull or manually add at least one non-rerank model and enable it. Rerank models cannot be used for a regular connection check.

### Response Is 401 or 403

This is usually related to authentication or permissions:

- The key is complete and has not been revoked;
- The key belongs to the correct project, region, or organization;
- The selected model is authorized;
- A custom request header did not override the correct authentication header;
- The cloud service does not require another region, project, or API version.

### Response Is 404

Check:

- Whether the Base URL includes or omits a required version path;
- Whether a complete `/chat/completions` URL was mistakenly entered as a regular Base URL;
- Whether the model endpoint type matches the server protocol;
- Whether the custom gateway implements model-list and chat paths;
- Whether Azure or a similar service requires a deployment name or API Version.

### Response Is 400 or “Unknown Parameter”

Restore provider API options and model capabilities to their defaults, remove unnecessary custom request headers, and test the simplest text conversation again.

### Pulling Models Fails

Some providers do not expose a model list endpoint, or a gateway may proxy only chat. In that case, add the official model ID manually.

A successful pull does not mean that every model is available to the current account. Verify with a health check or actual conversation.

### Connection Check Succeeds, but Chat Still Fails

A check usually covers only one key, one model, and one basic request. Continue checking:

- Whether chat actually selected the same model;
- Whether multi-key rotation includes an invalid key;
- Whether long context, images, Web Search, or tool calls exceed model capabilities;
- Whether the assistant defines incompatible custom parameters;
- Whether the provider is enforcing quota, concurrency, or content-policy limits.

### Key Rotation Selects an Invalid Credential

Open Key List, disable or delete the failing key, then check each remaining key. An invalid key continues participating in rotation for as long as it remains enabled.

## Security and Backups

- Do not use real keys in documentation screenshots;
- Do not paste complete request headers into feedback reports;
- Do not mix production and test keys in a list where they cannot be identified;
- Create a backup before deleting a provider or clearing data;
- After backup or synchronization, verify local paths, proxy, and cloud-account permissions again on the target device;
- When sharing configuration, prefer provider names, address structures, and model IDs that contain no credentials.

***

### Get Help and Submit Feedback

If configuration fails, submit feedback through the official channels listed in [Feedback and Suggestions](../../../question-contact/suggestions.md). Include the Cherry Studio version, provider, model ID, endpoint type, sanitized API address, and complete error text, but do not attach a real API Key.
