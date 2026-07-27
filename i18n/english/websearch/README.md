---
description: How to use Web Search in Cherry Studio
icon: globe
---

# Web Search

Web Search lets a model search the web or read a specified link before answering. It is useful for news, version updates, prices, policies, and other information that may change over time.

It is not a switch that automatically guarantees the latest answer. Cherry Studio gives search results or web page text to the model, but the final answer still depends on the sources, the model's tool-calling ability, and the quality of its response.

{% hint style="info" %}
Even when using Web Search, open the cited sources and verify their publication dates, original context, and key figures. For high-risk medical, legal, or financial information, do not make decisions based only on a model-generated summary.
{% endhint %}

## Two Ways to Search the Web

Cherry Studio automatically selects a web search method based on the current model.

| Method | When it is used | Who performs the search | Is a web search provider required? |
| --- | --- | --- | --- |
| Native model web search | The current model and provider support built-in web search | The model provider | Usually not |
| Cherry Studio external web search | The current model has no available native web search capability | Cherry Studio calls configured search and web page retrieval services | Both a default search provider and a default URL retrieval provider are required |

Both methods use the same Web Search switch in the chat input, but billing, search coverage, citation format, and available parameters may differ.

### Native Model Web Search

Cherry Studio passes web search parameters to the current model provider, which performs the search and organizes the results. Availability depends on:

- Whether the current model is recognized as supporting web search;
- Whether the current provider implements the relevant API;
- Account, region, and model permissions;
- The provider's current API rules.

Some models always use their own web search capabilities. For example, some Sonar or OpenRouter web search models may perform searches even if no external search provider has been configured separately.

### Cherry Studio External Web Search

When the current model does not use native web search, Cherry Studio gives the model two tools:

- **Search the Web**: finds candidate web pages from keywords;
- **Read URL**: opens a search result or a link provided in the conversation and extracts its main text.

The model decides when to call the tools, which keywords to use, and whether to continue reading pages. Search results are organized as numbered references that the model can cite in its answer.

{% hint style="warning" %}
External web search depends on the model's tool-calling performance. Even when the switch is enabled, the model may not search, may search inadequately, or may fail to cite sources correctly.
{% endhint %}

## Configure Before Use

If you use only models that support native web search, you can skip to [Enable Web Search in a Conversation](#enable-web-search-in-a-conversation).

To let a regular model use external web search, open:

```text
Settings → Web Search
```

Complete at least these two settings:

1. Select a **Default Search Provider**;
2. Select a **Default URL Retrieval Provider**.

These roles are independent:

- The search provider finds web pages from keywords;
- The URL retrieval provider reads the main text of a specific web page.

If either one is missing, Cherry Studio prompts you to open Settings when you enable Web Search for a regular model.

## Choose Providers

The current version includes these web search providers:

| Provider | Keyword search | Read URL | Configuration |
| --- | :---: | :---: | --- |
| Zhipu | ✓ |  | Uses the API Key from the Zhipu model provider |
| Tavily | ✓ |  | Requires a Tavily API Key |
| SearXNG | ✓ |  | Connects to a self-hosted or accessible SearXNG instance |
| Exa | ✓ |  | Requires an Exa API Key |
| ExaMCP | ✓ |  | Performs searches through the Exa MCP service |
| Bocha | ✓ |  | Requires a Bocha API Key |
| Querit | ✓ |  | Requires a Querit API Key |
| Fetch |  | ✓ | Cherry Studio's built-in URL retrieval service |
| Jina | ✓ | ✓ | Can be used for both search and web page retrieval |

Provider plans, quotas, and regional availability may change. Refer to each provider's official website for current information. For a quick start, continue with [Free Web Search](mian-fei-lian-wang-mo-shi.md).

### Configure an API Provider

1. Open the target provider under **Settings → Web Search**;
2. Enter the API Key;
3. If you use a proxy, private deployment, or compatible gateway, change the API address as needed;
4. Click **Check**;
5. After verification succeeds, set it as the default provider for the relevant role.

Some providers support multiple API Keys. They can be rotated at runtime, but each key must come from an account you are authorized to use. Do not put keys in prompts, screenshots, or public documentation.

### Configure SearXNG

SearXNG requires an instance address accessible from the computer running Cherry Studio. The default address is:

```text
http://localhost:8080
```

If SearXNG runs on another computer, a NAS, a Docker container, or a public server, enter the address that is actually accessible. If the instance uses Basic Auth, also enter the username and password.

For detailed steps, see [Configure SearXNG](searxng.md).

### Zhipu API Key

Zhipu Web Search uses the API Key saved in the Zhipu model provider. Configure Zhipu under **Settings → Model Providers** first, then return to **Settings → Web Search**, select Zhipu, and run the check.

## Configure Search Results

### Number of Search Results

**Number of Search Results** can be set from `1–100`; the default is `5`.

More results usually provide broader coverage, but they also:

- Increase response time;
- Use more context;
- Consume more tokens;
- Introduce more duplicate or low-relevance sources.

Start with the default for everyday questions. Increase it gradually only when you need to compare multiple sources.

### Search Result Compression

You can choose:

| Compression method | Behavior | Best for |
| --- | --- | --- |
| None | Keeps the text returned by the provider | Fewer results or when more original context is required |
| Cutoff | Shortens each result's text to the configured limit | More results or when you need to control context usage |

After enabling **Cutoff**, enter a cutoff length. A value that is too small may remove important context, while one that is too large will not control token use effectively. Start with the default and adjust it if answers omit information.

### Blacklist

The blacklist excludes matching domains before external search results are sent to the model. Use it to block content farms, mirror sites, or websites you do not want to use.

For rule formats and subscription settings, see [Web Search Blacklist](blacklist.md).

{% hint style="info" %}
Native model web search is performed by the model provider. Whether the blacklist applies and how many exclusion rules are supported depend on that provider's implementation; do not assume it behaves exactly like external web search.
{% endhint %}

## Enable Web Search in a Conversation

1. Open a conversation;
2. Select the model you want to use;
3. Click the **Globe** icon below the input;
4. Send your question after the icon becomes highlighted.

The Web Search state is stored in the current assistant. After you switch models, Cherry Studio reevaluates whether to use native or external web search for the new model.

Examples of questions that benefit from web search:

```text
Find the release notes for the latest stable version of Cherry Studio and cite the official release page.
```

```text
Compare the current official pricing of these three products, using only their official websites as sources.
```

```text
Read this link, summarize its main conclusions, and identify the article's publication date and author.
```

For more reliable results, specify:

- The time range;
- Which sources to prioritize;
- Whether to exclude forums or aggregator sites;
- Whether each claim needs a citation;
- Which fields to verify, such as version number, price, or publication date.

## Review and Verify Citations

External web search organizes results as numbered references and instructs the model to cite them in formats such as `[1]` and `[2]`. Citation formatting for native model web search is determined by the corresponding provider.

After receiving an answer, check at least:

1. Whether each citation opens;
2. Whether the page title matches the topic of the answer;
3. Whether the original text actually supports the claim;
4. Whether the publication date falls within the requested time range;
5. Whether different sources conflict.

An empty search result does not mean the information is absent from the web. It may also be caused by the keywords, service quota, network, blacklist, or a website's anti-bot protections.

## Known Compatibility Limitations

### Earlier Gemini Models and MCP

In function-tool mode, earlier Gemini models cannot use built-in model web search and an enabled MCP at the same time. When they conflict, Cherry Studio disables Web Search and displays a notice.

You can try:

- Temporarily disabling MCP;
- Switching to a newer model that supports the combination;
- Using another model that supports web search.

### GPT-5 Series with minimal Reasoning Effort

GPT-5 series reasoning models cannot enable OpenAI Web Search when using `minimal` reasoning effort. Cherry Studio disables Web Search and displays a notice.

Increase the reasoning effort and try again, or choose another web search method.

## Privacy and Costs

After Web Search is enabled, search keywords, URLs to be read, and necessary conversation context may be sent to the model provider, search provider, or web server.

Before use, confirm that:

- Search terms do not contain passwords, API Keys, personal identity information, or internal secrets;
- The target service meets your organization's data-compliance requirements;
- You understand the cost rules for search, model calls, and network traffic;
- Web content may contain incorrect information or malicious instructions targeting the model.

{% hint style="danger" %}
Treat web content as untrusted input. Do not paste keys, run unknown commands, download suspicious files, or change security settings just because a web page or model response asks you to.
{% endhint %}

## Troubleshooting

### Clicking the Web Search Icon Opens Settings

The current model is not using native web search, and either the **Default Search Provider** or **Default URL Retrieval Provider** has not been selected. Complete both settings and try again.

### Provider Check Fails

Check the following in order:

1. The API Key is complete, valid, and has available quota;
2. The API address is an API endpoint, not a web console;
3. The proxy, firewall, and DNS allow access;
4. The self-hosted service is running and listening on the correct address;
5. The system clock is accurate;
6. The provider's status page does not report an outage.

### Web Search Is Enabled, but the Answer Has No Citations

Possible reasons include:

- The model did not call the search tool;
- Native model web search did not return displayable citations;
- The search returned no results or results with low relevance;
- The model did not follow the citation instructions;
- The current question did not require web search, so the model answered directly.

You can explicitly require the model to “search and cite every source,” or switch to a model with more reliable tool calling.

### Search Results Are Too Long or Responses Are Slow

Reduce **Number of Search Results**, or enable **Cutoff** and gradually decrease the cutoff length. Do not set both the result count and cutoff length very high at the same time.

***

### 💡 Get Help and Submit Feedback

If you encounter questions, bugs, or feature suggestions during setup or use, see the official channels in [Feedback and Suggestions](../question-contact/suggestions.md).
