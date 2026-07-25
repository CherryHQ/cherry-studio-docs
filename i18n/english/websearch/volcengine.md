---
description: Let Volcengine Ark models use Cherry Studio Web Search tools
icon: globe-pointer
---

# Web Search for Volcengine Models

Cherry Studio V2 can give Volcengine Ark chat models access to external web search. The recommended combination is:

```text
Volcengine Ark model
    + Cherry Studio Default Search Provider
    + Cherry Studio Default URL Retrieval Provider
```

The current V2 does not register Volcengine Ark Web Search as an independent web search provider, and it does not automatically inject Ark's cloud Web Search tool into the built-in `doubao` provider.

{% hint style="warning" %}
The path in older tutorials—“create a zero-code app → enable the Web Search plugin → connect the app as an OpenAI model”—is not recommended for the current V2. The interface, plugins, and APIs have changed; do not keep copying old screenshots or old API Host formats.
{% endhint %}

## Understand the Two Web Search Capabilities

| Method | Who performs the search | Current status in Cherry Studio V2 | Recommended use |
| --- | --- | --- | --- |
| Cherry Studio external web search | Search providers such as ExaMCP, Tavily, SearXNG, and Bocha | Supported | Regular chat and centralized search service management |
| Volcengine Ark cloud Web Search | Volcengine Ark Responses API or app plugin | No dedicated adaptation | You already develop an app on Ark and are willing to verify the API yourself |

This page covers the first method. It does not require creating “My App” in Volcengine Ark or depend on the legacy Web Search plugin.

### Cherry Studio External Web Search

When the current model is not recognized as a native web search model, Cherry Studio gives it:

- A keyword search tool;
- A URL reading tool.

The model uses Function Calling to decide when to search and read web pages. Search results are returned to the model, which then generates an answer with citations.

### Volcengine Ark Cloud Web Search

The Volcengine Ark website provides cloud tools such as Responses API, Web Search, Knowledge Search, and Remote MCP. These are Ark API capabilities and are not the same as Cherry Studio's Web Search settings.

The built-in `doubao` provider currently uses the following by default:

```text
OpenAI Chat Completions
```

Default API Host:

```text
https://ark.cn-beijing.volces.com/api/v3/
```

Support for a Responses API tool on the official website does not mean that Cherry Studio automatically supports its request fields, event stream, or citation results.

## Before You Begin

Prepare:

1. A Volcengine account;
2. A Volcengine Ark API Key;
3. A currently available Model ID or Endpoint ID;
4. A chat model that supports Function Calling;
5. A keyword search provider;
6. A URL retrieval provider.

For basic Volcengine Ark configuration, see [Volcengine (Ark / Doubao)](../pre-basic/providers/doubao.md).

{% hint style="danger" %}
Do not put a Volcengine Ark API Key, search service API Key, or private URL containing a token in chats, screenshots, or public documentation.
{% endhint %}

## Configure a Volcengine Ark Model

### 1. Enable a Model and Copy Its Identifier

In the Volcengine Ark console:

1. Create an API Key;
2. Enable the model you plan to use;
3. Copy its current Model ID;
4. If you use a dedicated inference endpoint, copy the Endpoint ID in `ep-...` format;
5. Confirm the project, region, balance, and rate limits.

Do not copy:

- The model's display name;
- The console page URL;
- A Bot ID from a legacy app;
- An Endpoint ID from another project.

### 2. Enable the Provider in Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter to **All Providers**;
3. Select **Doubao / Volcengine**;
4. Enter the Ark API Key;
5. Keep the default API Host;
6. Turn on the provider;
7. Manually add the current Model ID or Endpoint ID;
8. Run a model health check.

Send a regular text message first to confirm that chat works, then configure Web Search.

## Choose a Model Suitable for Web Search

Cherry Studio external web search works best with models that support structured Function Calling.

The current V2 recognizes many newer Doubao Seed models, including models whose names match these series:

```text
doubao-seed-1.6...
doubao-seed-1.8...
doubao-seed-2.0...
doubao-seed-code...
```

Specific Model IDs change over time. Copy the current ID from the Volcengine Ark model page; do not use the series names above as complete IDs.

{% hint style="warning" %}
DeepSeek R1, used in older tutorials, is excluded from structured Function Calling models in the current V2 and is not recommended as the first choice for Cherry Studio external web search. It may work for regular chat but still fail to call search tools.
{% endhint %}

You can view or adjust capability labels in model management, but these labels affect only client-side decisions. They cannot give a model Function Calling support that the server does not provide.

## Configure Web Search

Open:

```text
Settings → Web Search
```

Configure both:

| Setting | Purpose | Examples |
| --- | --- | --- |
| Default Search Provider | Finds web pages from keywords | ExaMCP, Tavily, SearXNG, Bocha |
| Default URL Retrieval Provider | Reads the main text of a specific web page | Fetch, Jina |

Both are required.

If you do not want to apply for an additional search API Key, start with:

```text
Default Search Provider: ExaMCP
Default URL Retrieval Provider: Fetch
```

For details, see:

- [Web Search](README.md)
- [Free Web Search](mian-fei-lian-wang-mo-shi.md)
- [Configure SearXNG](searxng.md)

## Enable It in a Conversation

1. Return to the conversation page;
2. Select a Volcengine Ark model that passed its health check;
3. Click the **Globe** icon below the input;
4. Confirm that the icon is highlighted;
5. Send a question that requires current information.

Test question:

```text
Search the web for the latest stable release of Cherry Studio.
Cite only the official GitHub Release, and list the version number, release date, and major changes.
```

Check whether the answer:

- Actually called the search tool;
- Includes citations that can be opened;
- Cites the requested website;
- Matches the original page's date and version number;
- Does not present old knowledge as current results.

## What Happens During Web Search

For a Volcengine Ark model without native web search adaptation in the current V2, the typical flow is:

1. The user enables Web Search and sends a question;
2. Cherry Studio gives external search tools to the model;
3. The model generates a structured tool call;
4. Cherry Studio calls the default search provider;
5. The model calls the default URL retrieval provider as needed;
6. Search results and web page text are returned to the model;
7. The model generates the final answer and citations.

The search service API Key is not sent to the Volcengine Ark model, but search result text is sent to Ark as conversation context.

## Differences from Older Tutorials

| Older method | Current V2 recommendation |
| --- | --- |
| Create a zero-code “My App” | Use an Ark Model ID or Endpoint ID directly |
| Purchase or enable a legacy Web Search plugin in an Ark app | Configure an external search provider in Cherry Studio |
| Add a custom OpenAI provider | Prefer the built-in Doubao provider |
| Put the complete `/chat/completions` path in the URL | Enter the Base URL and let V2 append the request path |
| Add `#` to the end of API Host | Not required |
| Use the small app ID as the model name | Use the current Model ID or Endpoint ID |
| Use the legacy DeepSeek R1 Web Search example | Choose a current model that supports Function Calling |

When migrating from an old configuration, create a clean Doubao provider instance or restore the built-in provider defaults. Do not keep layering compatibility parameters onto the old address.

## Do Not Manually Mark “Native Web Search”

The Web Search capability label in model details affects whether Cherry Studio selects native or external web search.

Do not mark a regular Volcengine Ark model as a native web search model just to display the Globe icon. The current V2 has no corresponding adaptation for the Ark Web Search plugin. An incorrect label may cause:

- Cherry Studio to stop injecting external search tools;
- Ark to receive no correctly configured cloud Web Search tool;
- The Web Search switch to be highlighted even though no search occurs.

If you changed the label accidentally, restore automatic model detection and use the external Web Search configuration on this page.

## If You Must Use Ark Cloud Web Search

Volcengine Ark cloud Web Search is configured mainly through Responses API or an Ark app. The built-in `doubao` connection in the current Cherry Studio V2 has no dedicated settings page for these tools.

Do not connect an Ark cloud app as a regular model until you have confirmed all of the following:

1. Web Search is enabled according to the current official Volcengine Ark documentation;
2. You have confirmed whether the call uses Chat API, Responses API, or the app Bot API;
3. You have the corresponding Model ID, Endpoint ID, or Bot ID;
4. You have confirmed the request address and authentication method;
5. You have confirmed that the returned events can be parsed by Cherry Studio's current endpoint;
6. You have confirmed the citation, streaming output, and tool-result formats;
7. You understand the fees for both the model and search plugin.

{% hint style="info" %}
This is an advanced compatibility scenario and is not part of the current V2 built-in Web Search flow. Historical app URLs and parameters may stop working after Ark API upgrades.
{% endhint %}

For current Volcengine Ark tool information, see the [Volcengine Ark Product Documentation](https://www.volcengine.com/docs/82379/) and [Tool Calling](https://www.volcengine.com/docs/82379/1958524).

## Privacy and Costs

When using Cherry Studio external web search, data may be sent separately to:

- Volcengine Ark: the user's question, search results, and retrieved web page text;
- The search provider: search keywords;
- The target website: the web request;
- The URL retrieval provider: the target URL, depending on the selected service.

Costs may include:

- Volcengine Ark model input and output tokens;
- Search service calls;
- Ark inference endpoints or model units;
- Additional network traffic;
- Related plugin fees if you separately use Ark Web Search.

Do not budget based on free request counts or prices shown in old screenshots. Refer to each service's current console.

## Troubleshooting

### Clicking the Globe Icon Opens Web Search Settings

The current model has no native web search adaptation, and either the **Default Search Provider** or **Default URL Retrieval Provider** is missing. Configure both and try again.

### Regular Chat Works, but the Search Tool Is Not Called

Check the following in order:

1. Whether the Globe icon is highlighted;
2. Whether the current model supports Function Calling;
3. Whether the Model ID was incorrectly marked as not supporting tools;
4. Whether you are using the legacy DeepSeek R1;
5. Whether the question explicitly requires a search and citations;
6. Whether the search provider passed its check.

Switch to a current Doubao Seed tool model and try again in a new conversation.

### The Model Says “I Will Search” but Returns No Results

This is not a successful tool call. Check the message details for a structured tool process. If there is none, switch to a model with more reliable tool calling.

### Search Results Appear, but Citations Do Not Open

The page may be unavailable, require sign-in, use anti-bot protections, have regional restrictions, or fail to load through Fetch. Ask the model to use another source and manually verify important conclusions.

### The Model Still Uses Old Knowledge After Web Search Is Enabled

Explicitly prompt:

```text
You must search the web first. If the search fails, explain the failure instead of answering only from existing knowledge.
```

If it still does not work, start a new conversation, switch models, or check the search provider.

### Use Volcengine Ark's Own Web Search

Cherry Studio currently has no corresponding built-in configuration. Do not treat a model capability switch as an adapter. Verify the current Ark Responses API or app API yourself, or use Cherry Studio external web search for now.

### Response Is 401, 403, 404, or 429

These are usually Volcengine Ark model connection problems rather than Web Search settings:

- `401`: Invalid API Key;
- `403`: The project, model, or Endpoint lacks permission;
- `404`: The API Host, Model ID, or Endpoint ID is incorrect;
- `429`: A rate, concurrency, or quota limit was reached.

Disable Web Search and confirm that regular chat works again, then troubleshoot the model and search service separately.

***

### 💡 Get Help and Submit Feedback

If you encounter questions, bugs, or feature suggestions during setup or use, see the official channels in [Feedback and Suggestions](../question-contact/suggestions.md).
