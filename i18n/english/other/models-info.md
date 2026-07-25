---
icon: database
---

# Model Data

Cherry Studio V2 no longer relies on a large, static model table in the documentation. Model versions, context, pricing, and provider capabilities change quickly, and long-term manual maintenance can make outdated information appear definitive.

This page instead explains where the model data in the app comes from, what each field means, and how to determine whether a model is actually available from your current provider.

{% hint style="info" %}
Model information displayed in the app is used for configuration and routing. The model provider’s official documentation, console permissions, and actual API responses are the final authorities on availability, limits, and billing.
{% endhint %}

## Where model data comes from

V2 merges several kinds of data into the model displayed to you:

1. **Model catalog**: general names, capabilities, input and output types, context, parameters, pricing, and other basic information.
2. **Provider overrides**: endpoints, special restrictions, aliases, or substitute models for a specific provider.
3. **Provider model list**: some providers can return the Model IDs visible to the current account through an API.
4. **User configuration**: custom information for manually added models, names, capability tags, endpoints, limits, and similar fields.

User configuration has the highest merge priority, followed by provider overrides and then the general model catalog.

When a provider API returns only a Model ID, Cherry Studio attempts to fill in information from the catalog. An ID that is not in the catalog can still be added as a custom model, but some fields may be incomplete.

## Where to view it

Open **Settings → Model Providers** and select a provider. In the model list, you can:

* Search for a model name or ID.
* Filter by capability.
* Enable or disable one model.
* Enable all models in the current filtered result.
* Open the model editor to view or change selected fields.
* Add a model that the provider did not list automatically.

Only enabled models appear in most model pickers. Disabling a model does not delete its configuration.

See [Model providers](../pre-basic/providers/) for the complete provider-configuration workflow.

## Common fields

### Display name and Model ID

| Field | Purpose |
| :--- | :--- |
| Display name | The name shown in the Cherry Studio interface; it may differ from the API ID |
| Model ID | The actual model identifier used when requesting the provider API |
| Provider | The configuration responsible for authentication, endpoint, and request routing |
| Group | Organizes the model list only; it does not change API behavior |

The same Model ID may exist under several providers. Internally, the app combines the provider and Model ID into a unique identifier. When adding a model manually, however, enter the API Model ID from the provider documentation and do not add an internal app prefix yourself.

### Endpoint type

The endpoint type determines the request format. V2 supports these model endpoints:

* OpenAI Chat Completions
* OpenAI Responses
* Anthropic Messages
* Google Generate Content
* OpenAI Image Generation
* Jina Rerank

The same model name does not mean that every provider supports the same endpoint. A mismatched endpoint commonly produces `400`, `404`, invalid tool parameters, or an unparseable response structure.

### Context and output limits

| Field | Meaning |
| :--- | :--- |
| Context window | Overall Token capacity processed in one request |
| Maximum input | Provider’s input Token limit |
| Maximum output | Output Token limit for one generation |

These values do not follow a simple addition rule. A provider may impose separate limits for images, tool definitions, caching, reasoning Tokens, or a particular plan.

Do not treat `k` or `M` abbreviations in documentation as exact usable values. When setting a value, use the integer in the provider’s current API documentation and validate it with a minimal request.

### Input and output types

A model can declare its supported input and output types separately:

* Text
* Image
* Audio
* Video

Understanding an image and generating an image are different capabilities. Audio input support also does not imply speech generation.

### Capability tags

The model list may display these capabilities:

| Capability | Description |
| :--- | :--- |
| Vision understanding | Accept images and produce text |
| Image generation | Generate or edit images |
| Audio understanding | Accept or recognize audio |
| Audio generation | Generate audio or speech |
| Video understanding | Accept and understand video |
| Video generation | Generate video |
| Reasoning | Support reasoning effort or thinking-related configuration |
| Tool calling | Produce structured function or tool calls |
| Native web access | Search through the model or provider endpoint |
| Embedding | Generate vectors for Knowledge Base indexing and retrieval |
| Rerank | Reorder candidate text |

Capability tags affect model filters, interface controls, and request routing. Selecting a tag manually tells Cherry Studio how to use the model; it **does not add a real capability to the provider model**.

### Parameter support

Different models may support different parameters, such as:

* Temperature
* Top P
* Top K
* Frequency Penalty
* Presence Penalty
* Max Tokens
* Stop Sequences
* System Message

A reasoning model may ignore or reject some traditional sampling parameters. If you encounter `unsupported parameter`, restore the defaults first, then enable parameters one at a time according to the model’s current official documentation.

### Reasoning configuration

A reasoning model may also define:

* Reasoning type.
* Available reasoning efforts.
* Minimum, maximum, and default thinking Tokens.
* Whether interleaved thinking is supported.

Actual values depend on the model, endpoint, and provider implementation together. The same model may use different parameter formats through an OpenAI-compatible endpoint and an Anthropic Messages endpoint.

### Pricing

The catalog may store prices for input, output, caching, images, audio, or video, but this information is suitable only for estimates:

* A provider may change pricing at any time.
* Regions, plans, and channels may differ.
* Reasoning, caching, batch processing, and tool calls may be billed separately.
* A third-party relay may use its own pricing model.

Use the provider’s bill for payment and cost reconciliation.

## Why identical model names show different information

Common causes include:

* The provider maps them to different snapshots or aliases.
* Their endpoint types differ.
* The current account has access to only some capabilities.
* The provider limits context or output length.
* An aggregator uses its own Model ID and pricing.
* A local model has different quantization, templates, or runtime parameters.
* A user manually changed capabilities or limit fields.

When comparing models, record the **provider, Model ID, endpoint, and date** together. Do not compare only their display names.

## Limits of automatic model-list retrieval

“Model list retrieved successfully” means only that the provider returned a set of model IDs. It does not mean that:

* The current API Key has permission to call each model.
* A model supports images, tools, reasoning, or web access.
* Context and pricing information is complete.
* A model is valid for every endpoint.
* The provider will not remove or rename it later.

After retrieving the list, enable the models you need and perform a real request.

## How to validate a model

### 1. Basic connection

Check the API Host and credentials in the provider settings, then run the connection check. After it passes, complete a real chat with a short text message.

### 2. Test only the capabilities you need

| Target capability | Minimal test |
| :--- | :--- |
| Vision understanding | Upload a non-sensitive image and ask the model to describe one clear element |
| Tool calling | Connect a side-effect-free tool and ask it to read fixed information |
| Reasoning | Use a multi-step question you can verify manually and observe whether its parameters are accepted |
| Native web access | Ask about recently updated, verifiable information and inspect the actual search record and citations |
| Embedding | Retrieve the dimension and run one retrieval test with a small sample document |
| Rerank | Sort a fixed set of candidate texts and check whether the result fits the question |
| Image generation | Generate a test image from a simple prompt and inspect the response format and dimensions |

### 3. Record the test environment

Record at least:

* Cherry Studio version.
* Provider.
* Model ID.
* Endpoint type.
* Test date.
* Successful capabilities and parameters.

This lets you distinguish a change in model behavior from a change in local configuration after the provider upgrades a model.

## Edit model data manually

You can edit a model when catalog information is missing or the provider uses a custom ID.

Before editing:

1. Save the current Model ID, endpoint, and capabilities.
2. Change only one field.
3. Run the corresponding minimal test immediately.
4. Restore the original value if it fails.

{% hint style="warning" %}
Do not select capabilities blindly merely to make a model appear in a filter. Incorrect Embedding, Rerank, image-generation, or tool-calling tags may send a request to an incompatible API.
{% endhint %}

## Frequently asked questions

### A model exists in the provider console but not in Cherry Studio

Try retrieving the model list first. If it still does not appear, add it manually with the exact Model ID supplied by the provider. Check whether the model requires a dedicated endpoint, region, or API version.

### A model appears in the list, but the request returns 404

The API Host, Model ID, region, or endpoint commonly does not match. Do not change capitalization or remove a version suffix based only on the list’s display name.

### Model tags do not match actual capabilities

Use the provider’s official documentation and a real request as the source of truth, then edit the capability tags. If the public catalog is wrong, follow [Feedback and suggestions](../question-contact/suggestions.md) and provide the provider, Model ID, official documentation link, and test result.

### Context does not reach the advertised limit

Check the maximum output, images, files, tool definitions, and message-history usage. An aggregator may also apply a lower limit than the model vendor.

### Pricing differs from the bill

Catalog pricing may be outdated or inapplicable to the current channel. Stop using it for financial settlement and consult the current provider’s pricing page and billing details.

## Related documentation

* [Model providers](../pre-basic/providers/)
* [Default model settings](../cherrystudio/preview/settings/default-models.md)
* [Embedding models](../knowledge-base/emb-models-info.md)
* [Knowledge Base guide](../knowledge-base/knowledge-base.md)
* [Model leaderboard](model_rank/lmarena.md)
