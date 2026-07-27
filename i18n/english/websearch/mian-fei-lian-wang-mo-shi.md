---
description: Configure web search without applying for an additional search API Key
icon: magnifying-glass
---

# Free Web Search

If you do not want to apply for a separate search service API Key, you can use this combination in Cherry Studio V2:

```text
Default Search Provider: ExaMCP
Default URL Retrieval Provider: Fetch
```

In the current version, this combination does not require an additional search API Key:

- ExaMCP finds web pages from keywords;
- Fetch directly reads the main text of search results or a specified URL;
- Regular models use both capabilities through tool calls.

{% hint style="warning" %}
“Free” here means that Cherry Studio currently does not require you to configure an additional search API Key. It does not mean that every related service will always be free. Model calls may still incur charges, and ExaMCP's access policy, quotas, and availability may change.
{% endhint %}

## When to Use It

This setup is suitable for:

- Trying Web Search for the first time;
- Occasionally looking up the latest information;
- Avoiding registration with multiple search platforms;
- When you do not yet have an API Key for Tavily, Exa, Bocha, or similar services;
- Testing a model's tool-calling performance first.

If you need stable high-volume usage, a fixed service level, enterprise compliance, or complete administrative control, use a search API with a formal account or deploy your own SearXNG instance.

## How It Works

A typical external web search proceeds as follows:

1. The model decides that the question requires a search;
2. The model calls ExaMCP and submits search keywords;
3. ExaMCP returns candidate web pages;
4. The model calls Fetch as needed to read specific URLs;
5. Cherry Studio extracts the main text from each web page;
6. The model organizes an answer and citations from the returned content.

ExaMCP and Fetch have different roles and cannot replace each other:

| Provider | Capability | Can it complete the full Web Search setup for a regular model by itself? |
| --- | --- | --- |
| ExaMCP | Keyword search | No; a default URL retrieval provider is still required |
| Fetch | Read URL | No; a default search provider is still required |
| ExaMCP + Fetch | Search for and read web pages | Yes |

{% hint style="info" %}
If the current model uses its own native web search, Cherry Studio does not switch to this external combination. Native web search is performed by the model provider, and its fees and citation format follow that provider's rules.
{% endhint %}

## Configure ExaMCP and Fetch

### 1. Open Web Search Settings

Open:

```text
Settings → Web Search
```

There are two independent options at the top of the page:

- **Default Search Provider**;
- **Default URL Retrieval Provider**.

### 2. Select ExaMCP

Under **Default Search Provider**, select:

```text
ExaMCP
```

You can also open the ExaMCP details page and click **Set as Default**.

The current default address is:

```text
https://mcp.exa.ai/mcp
```

You usually do not need to change it or enter an API Key. Click **Check** to confirm that the service is accessible from your current network.

{% hint style="warning" %}
Do not replace the API address with an MCP address from an unknown source. Search terms are sent to that address, and a malicious service may also return misleading content.
{% endhint %}

### 3. Select Fetch

Under **Default URL Retrieval Provider**, select:

```text
Fetch
```

Fetch is Cherry Studio's built-in web page reader. It requires no API Key and has no remote extraction service address to enter.

### 4. Confirm Both Defaults

The two settings should now show:

| Setting | Selection |
| --- | --- |
| Default Search Provider | ExaMCP |
| Default URL Retrieval Provider | Fetch |

If only one is configured, a regular model will still prompt you to open Settings when you click the Web Search icon.

## Use It in a Conversation

1. Return to the conversation page;
2. Select a chat model with reliable tool calling;
3. Click the **Globe** icon below the input;
4. Send a question that requires current information.

For a first test, try:

```text
Search for the latest stable release of Cherry Studio. Cite only the official GitHub Release,
and list the version number, release date, and three major changes.
```

After receiving the answer, check:

- Whether a search was actually performed;
- Whether the citations can be opened;
- Whether the citations come from the requested source;
- Whether the version number and release date match the original page.

## What Fetch Can Read

Fetch requests a target URL directly from the computer running Cherry Studio, extracts the main text from the returned HTML, and converts it into text suitable for the model.

It usually works well with:

- News and blog articles;
- Product documentation;
- Static web pages;
- Public pages that do not require sign-in;
- Article links from search results.

The following pages may fail or return incomplete content:

- Pages that require sign-in;
- Pages whose main content is loaded by browser scripts;
- Websites with CAPTCHAs or strong anti-bot measures;
- Pages restricted to specific regions or networks;
- PDFs, audio, video, or non-HTML files;
- Expired links, abnormal redirects, or certificate errors.

Each Fetch request has a timeout. If the target website responds too slowly, the model may not receive the page text.

## “No Additional Key” Does Not Mean “No Cost”

You may still incur:

- Model input and output token charges;
- Context usage from search results;
- Local or server network traffic;
- Device, domain, or maintenance costs for a self-hosted SearXNG instance;
- Future charges after a third-party service changes its policies.

More search results and longer web page text usually consume more model context. Under **Settings → Web Search**, you can reduce **Number of Search Results** or enable **Cutoff**.

## Privacy

When using ExaMCP + Fetch:

- Search keywords are sent to the ExaMCP service;
- Fetch accesses the target website directly from your computer;
- The target website can usually see the network address that sent the request;
- Search results and web page text are sent to the current model provider as context.

Do not include the following in search terms or URLs:

- API Keys, passwords, or verification codes;
- Links to private systems that contain access tokens;
- Customer data or personally identifiable information;
- Confidential company information.

{% hint style="danger" %}
Treat web content as untrusted input. Do not run commands from unknown sources in a web page or model answer, and do not disable security software, upload keys, or download suspicious files when instructed to do so.
{% endhint %}

## Other Low-Cost Options

### Use Native Model Web Search

If you already use a model that supports native web search, you usually do not need to configure a separate search API Key. However, model web search may be included in model billing and must not be treated as free.

### Self-Host SearXNG + Fetch

To control the search entry point yourself, use:

```text
Default Search Provider: SearXNG
Default URL Retrieval Provider: Fetch
```

SearXNG itself does not require an API Key in Cherry Studio, but you need an accessible instance. For a self-hosted instance, you are responsible for deployment, updates, security, and upstream search engine restrictions.

For detailed configuration, see [Configure SearXNG](searxng.md).

### Use Provider Promotional Credits

Some search APIs may offer trials or free quotas to new accounts, but their rules can change. Before registering, check the provider's current official pricing, regional restrictions, and privacy policy. Do not make long-term plans based on quota figures in an outdated tutorial.

## Troubleshooting

### ExaMCP Check Fails

Check the following in order:

1. Whether your current network can access `https://mcp.exa.ai/mcp`;
2. Whether the proxy is configured correctly and available to Cherry Studio;
3. Whether DNS, the firewall, or security software is blocking access;
4. Whether the ExaMCP service is temporarily unavailable;
5. Whether the API address was changed accidentally.

Restore the default address and check again. If it still fails, use another search provider or self-host SearXNG.

### Fetch Cannot Read a Page

Open the same URL in a regular browser first. If the browser also cannot access it, resolve the network, sign-in, regional, or certificate issue first.

If the page opens in a browser but Fetch fails, common causes include:

- The page depends on JavaScript;
- The website requires a Cookie, signed-in session, or CAPTCHA;
- The website blocks automated requests;
- The response is not HTML from which the main text can be extracted;
- The response exceeds the timeout.

Try another source, or manually copy the relevant web page text into the conversation.

### Both Providers Are Configured, but the Model Does Not Search

The Web Search switch only makes tools available; the model must still decide to call them. You can:

- Confirm that the Globe icon is highlighted;
- Explicitly ask the model to “search the web first, then answer and cite sources”;
- Switch to a model with more reliable tool calling;
- Make the question more specific by adding a time range and preferred sources;
- Start a new conversation and try again.

### Search Results Appear, but There Is No Web Page Text

ExaMCP may have returned candidate links that Fetch could not read. Try reducing the number of results, choosing another source, or giving the model a specific publicly accessible URL.

***

### 💡 Get Help and Submit Feedback

If you encounter questions, bugs, or feature suggestions during setup or use, see the official channels in [Feedback and Suggestions](../question-contact/suggestions.md).
