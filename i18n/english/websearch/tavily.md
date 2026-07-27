---
description: Configure Tavily in Cherry Studio V2 for reliable keyword web search.
icon: magnifying-glass
---

# Tavily Web Search

Tavily is a web search service for AI applications. In Cherry Studio V2, it finds web pages from keywords and gives their titles, summaries, and links to the model for generating an answer.

{% hint style="info" %}
In the current version, Tavily is a **Keyword Search Provider** and cannot replace a web page retrieval service. To let the model continue reading the full content of a result page, also configure a default URL retrieval provider such as Fetch or Jina.
{% endhint %}

## Before You Begin

To configure Tavily, you need:

- A working Tavily account;
- A Tavily API Key;
- At least one model available for chat in Cherry Studio;
- A URL retrieval provider if you need to read specific web pages.

Tavily measures usage in API Credits. Free quotas, paid plans, and request limits may change. Refer to [Tavily Pricing](https://www.tavily.com/pricing) and live information in the console.

## Get an API Key

1. Open [Tavily Platform](https://app.tavily.com/home).
2. Register or sign in by following the current page prompts.
3. Create or find an available key in the API Keys area of the console.
4. Copy the key so that you can paste it into Cherry Studio.

Tavily's registration and verification flow may change over time, so this page does not prescribe a fixed CAPTCHA, two-factor authentication, or third-party sign-in interface. If the page differs, follow Tavily's current prompts.

{% hint style="danger" %}
An API Key is an account credential. Do not put a real key in screenshots, chat records, public documentation, or code repositories. If you suspect exposure, revoke the old key in the Tavily console immediately and create a new one.
{% endhint %}

## Configure Tavily in Cherry Studio

### 1. Open Web Search Settings

Open:

> **Settings → Web Search**

Find **Tavily** in the provider list.

### 2. Enter the API Key

Paste the key from the Tavily console into the **API Key** input.

If you have saved multiple keys, you can switch or manage them in the key list. Multiple keys are useful for rotating credentials, but they do not increase the total quota of one Tavily account.

### 3. Check the API Host

The default API Host is:

```text
https://api.tavily.com
```

Keep the default in most cases. Change it only when using a compatible proxy or gateway; a custom address must support Tavily's `/search` endpoint and Bearer authentication.

{% hint style="warning" %}
An incorrect API Host, appending `/search` twice, or a proxy that does not forward the `Authorization` request header will cause the connection check or actual searches to fail.
{% endhint %}

### 4. Check the Configuration

Click **Check** on the Tavily card.

- Check succeeds: the current API Host and key can complete a basic request;
- Check fails: verify the key, host, network proxy, and Tavily account status, then see Troubleshooting below.

### 5. Set It as the Default Keyword Search Provider

Set Tavily as the **Default Search Provider**. Cherry Studio uses it when external keyword search is required.

To let the model open web pages from the search results, also select a default **URL Retrieval Provider**. A common combination is:

| Purpose | Recommended provider |
| --- | --- |
| Keyword search | Tavily |
| URL retrieval | Fetch or Jina |

The search provider and URL retrieval provider are independent settings. Configuring only Tavily does not mean that the app can read the full text of any web page.

## Adjust General Search Settings

Cherry Studio applies its general Web Search settings to Tavily and other external providers.

### Maximum Number of Results

You can set the maximum number of results returned by each search. More results usually give the model more information, but may also increase search time, context length, and API usage.

Start with the default and increase it gradually only when an answer lacks sources.

### Search Result Compression

Depending on the task, you can keep search results uncompressed or cut them off. Compression reduces context use, but excessive cutoff may remove important details.

### Web Search Blacklist

After Tavily returns results, Cherry Studio uses the blacklist to filter URLs you do not want. See [Web Search Blacklist](blacklist.md) for configuration.

{% hint style="info" %}
The current Tavily adapter in Cherry Studio sends only the query and maximum result count to Tavily. Advanced parameters in the official Tavily API, such as `search_depth`, `topic`, `include_domains`, `exclude_domains`, and `include_answer`, are not currently exposed as separate settings in the V2 interface.
{% endhint %}

## Use Tavily in a Conversation

1. Open an assistant or start a new conversation.
2. Select the model you want to use.
3. Click the **Globe icon** near the input to enable Web Search.
4. Enter a question that requires current information or external sources and send it.
5. Check the source numbers and links in the answer.

For example:

```text
Search for the release notes of the latest stable version of Cherry Studio.
Summarize them by feature category and cite a source after each conclusion.
```

If the model supports native web search, Cherry Studio handles the request using that model's capabilities first. For a model without native web search that supports tool calling, Tavily can be used as the external keyword search provider.

For the difference between these two methods, see [Web Search](README.md).

## Current Integration Capabilities

| Capability | Current V2 support |
| --- | --- |
| Keyword search | Supported |
| Return web page title, summary, and URL | Supported |
| Set the maximum number of results | Supported through general Web Search settings |
| Multiple API Keys | Supported |
| Custom API Host | Supported |
| Read the main text of a specified URL | Not supported; configure Fetch or Jina |
| Advanced Tavily Search parameters | Not currently exposed in the interface |
| Tavily Extract, Crawl, Map, and Research | Not integrated by the current Tavily adapter |

Cherry Studio currently sends requests to Tavily's `/search` endpoint and authenticates with a Bearer API Key. For endpoint capabilities, see the [Tavily Search API](https://docs.tavily.com/documentation/api-reference/endpoint/search).

## Troubleshooting

### Check Reports an Authentication Failure

This is usually related to the API Key:

1. Copy the key again from the Tavily console and avoid extra spaces;
2. Confirm that the key has not been revoked;
3. Confirm that the current account or team still allows the key to be used;
4. If you suspect exposure, revoke the old key and create a new one.

### Insufficient Credits or Requests Are Too Frequent

Check Credits, billing, and rate limits in the Tavily console. Wait for credits to become available, reduce search frequency, or adjust the plan according to your actual needs.

Do not continuously retry to bypass limits; this only creates more failed requests.

### Check Succeeds, but the Conversation Does Not Search the Web

Confirm the following in order:

- Tavily is set as the default keyword search provider;
- The Globe icon is enabled for the current conversation;
- The current model supports tool calling or native web search;
- The question actually requires an external search;
- Tools are not disabled by assistant or model settings.

### Search Results Appear, but the Model Cannot Read Page Details

In the current version, Tavily performs keyword search only. Set Fetch or Jina as the default URL retrieval provider and try again.

### Search Returns No Results or Irrelevant Results

You can:

- Rewrite the question as explicit search keywords;
- Add a time, region, product name, or version number;
- Increase the maximum number of results moderately;
- Check whether the blacklist accidentally filters the target website;
- Verify an important conclusion again with a different search query.

### A Custom API Host Fails

Restore the default address:

```text
https://api.tavily.com
```

If you must use a proxy or gateway, confirm that it:

- Supports `POST /search`;
- Forwards Bearer authentication;
- Returns JSON compatible with the Tavily Search API;
- Does not append or remove paths.

## Security, Privacy, and Accuracy

- Search terms are sent to Tavily. Do not include passwords, API Keys, personal data, or non-public business information in a query.
- Web results may be outdated, incorrect, or contradictory. For high-risk medical, legal, or financial conclusions, open the original sources and verify them manually.
- Tavily manages its own quotas and billing. Before high-volume use, check the current plan and usage rules in the console.
- Regularly rotate keys you no longer need. For exposure response, see [Tavily API Key Management](https://docs.tavily.com/documentation/best-practices/api-key-management).

## Related Documentation

- [Web Search](README.md)
- [Free Web Search](mian-fei-lian-wang-mo-shi.md)
- [Web Search Blacklist](blacklist.md)
- [Tavily Quickstart](https://docs.tavily.com/documentation/quickstart)

***

### Get Help and Submit Feedback

If you encounter a problem during setup or use, submit feedback through the official channels listed in [Feedback and Suggestions](../question-contact/suggestions.md). Include the Cherry Studio version, model name, error message, and whether a proxy is in use, but do not attach a real API Key.
