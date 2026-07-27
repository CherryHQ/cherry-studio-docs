---
icon: cloud-plus
---

# Model Services

Model Services connects Cherry Studio to cloud model platforms, local inference services, and self-hosted gateways. After configuring a provider, you must also enable models in its model list before you can select them in Assistants, Translate, Knowledge Base, and other features.

{% hint style="info" %}
If you already know which provider you want to use, go directly to the [provider configuration guides](#provider-configuration-guides). For a quick comparison of supported options, see the [All Providers quick reference](quick-reference.md).
{% endhint %}

## Before you begin

Prepare the following information for your provider type:

- **Cloud model platform or aggregation gateway**: an API Key and the models enabled for your account;
- **Self-hosted gateway**: an API Key, Base URL, and the API protocols supported by the gateway;
- **Local inference service**: the address of a running service and the models already downloaded or loaded;
- **Cloud-specific connection**: you may also need a region, project, deployment name, or cloud account credentials.

Authentication and URL structures vary between providers. Prefer Cherry Studio's built-in provider templates. Create a custom provider only when the target provider is not listed or when you need to connect to a self-hosted compatible API.

## Configure a provider

### 1. Find or add a provider

Open `Settings → Model Services`.

The list on the left displays enabled providers by default. You can:

- Search by provider or model name;
- Filter for **Enabled**, **Disabled**, **All Providers**, or providers that support the Agent API;
- Drag providers to change their order;
- Select `+` to the right of the search box to create a custom provider;
- Use a provider's context menu to edit, duplicate, or delete manageable entries.

{% hint style="warning" %}
The “Agent Supported” filter only indicates that the provider has a compatible endpoint required by the current Agent features. It does not mean every model from that provider supports tool calling. Actual capabilities still depend on the selected model and provider.
{% endhint %}

### 2. Enter authentication and endpoint details

After selecting a provider, complete its authentication settings on the right:

1. Enter an API Key, or follow the on-screen instructions for OAuth, AWS, Azure, Google Cloud, or other provider-specific authentication;
2. Check the Base URL. When you use a built-in template, the default URL is usually correct;
3. If the provider offers multiple protocols, you can configure separate OpenAI Chat Completions, Anthropic Messages, Google Generate Content, or OpenAI Responses endpoints under API settings;
4. Turn on the provider switch at the top of the page.

Custom providers use **OpenAI Chat Completions** as the primary API by default. You can also expand “More Endpoints” to add other compatible APIs. For detailed rules, see [Custom Provider](zi-ding-yi-fu-wu-shang.md).

{% hint style="danger" %}
An API Key is a sensitive credential. Never include a real key in documentation, chat content, or issue screenshots. When troubleshooting, show only a few masked characters at the beginning and end.
{% endhint %}

### 3. Sync and enable models

Under **Models**:

1. Select **Add** to synchronize the models currently available from the provider;
2. Review added, updated, and removed entries in the sync preview, then apply the changes;
3. If the API cannot return a model list, select **Custom** and enter the model ID manually;
4. Turn on the models you plan to use.

You can search the model list by name or filter it by capabilities such as vision, reasoning, and tool calling. Capability labels primarily come from provider information and Cherry Studio's model rules. If automatic detection is inaccurate, edit the model and adjust its capabilities manually.

### 4. Check the connection

After configuration, run these two checks:

- In the authentication area, start a connection check and select a configured model and API Key to verify the request;
- Run Health Check in the model list to confirm in batches that enabled models are accessible.

After the checks pass, create or open an Assistant, select a newly enabled model in the model selector, and send a test message.

## Choose a connection method

| Use case | Recommended method | Notes |
|---|---|---|
| Use official APIs from OpenAI, Anthropic, DeepSeek, and similar providers | Select the matching built-in template | The default URL and API type are predefined |
| Use models from multiple companies with one key | Select an aggregation provider or gateway template | The platform determines model availability, pricing, and supported regions |
| Connect to a self-hosted gateway such as NewAPI or OneAPI | Prefer the matching template | If the deployment path differs, change the Base URL |
| Use a local service such as Ollama or LM Studio | Select a local service template | First confirm that the local service is running and its port is accessible |
| Connect to a compatible API that is not listed | Create a custom provider | Confirm the protocol, Base URL, and model ID |

{% hint style="info" %}
You can configure multiple API Keys for one provider and apply more granular request URL and parameter settings. See [Model Services settings](../../cherrystudio/preview/settings/providers.md).
{% endhint %}

## Troubleshooting

### Models cannot be synchronized

First confirm that the API Key, Base URL, and API protocol match. Some providers do not offer a model-list endpoint; in this case, add the model ID shown in the provider console manually.

### A model does not appear in the model selector

Make sure both the provider switch at the top of the page and the target model switch are on. A synchronized model does not appear as an option while it is disabled.

### The provider returns 401 or 403

This usually means the API Key is invalid, the account lacks permission, the target model has not been enabled for the account, or the provider restricts the request source. Check the credential status and model permissions in the provider console.

### The provider returns 404 or a protocol error

Check the Base URL for duplicated or missing path segments, then confirm which API protocol the provider actually supports. When using a gateway, also confirm that it supports the selected model's endpoint.

### A local model connection times out

Make sure the local inference service is running and that its listening address and port match the Cherry Studio settings. If the service runs in a container, virtual machine, or another device, also confirm that network and firewall rules allow access.

## Provider configuration guides

### Common official providers

- [OpenAI](openai.md)
- [Anthropic](anthropic.md)
- [Azure OpenAI](azure-openai.md)
- [Google Gemini](google-gemini.md)
- [Vertex AI](vertex-ai.md)
- [DeepSeek](deepseek.md)
- [Grok](grok.md)
- [Groq](groq.md)
- [Moonshot AI (Kimi)](moonshot.md)
- [MiniMax](minimax.md)

### Aggregation services and gateways

- [CherryAI (Free)](cherryai/)
- [CherryIN](cherryin-1.md)
- [OpenRouter](openrouter.md)
- [NewAPI](newapi.md)
- [OneAPI](oneapi.md)

### Local and custom connections

- [Ollama](ollama.md)
- [LM Studio](lm-studio.md)
- [Custom Provider](zi-ding-yi-fu-wu-shang.md)

For more listed providers, use the navigation on the left or see the [All Providers quick reference](quick-reference.md).

If the configuration still does not work, record the Cherry Studio version, operating system, provider name, model ID, and sanitized error details before submitting feedback. See [Feedback and Suggestions](../../question-contact/suggestions.md) for contact options.
