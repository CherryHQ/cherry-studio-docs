---
description: Exclude websites you do not want in Web Search results
icon: ban
---

# Web Search Blacklist

The Web Search blacklist excludes web pages you do not want to enter the model's context, such as content farms, mirror sites, low-quality aggregators, or websites unrelated to your work.

Blacklist rules are saved under:

```text
Settings → Web Search → Blacklist
```

{% hint style="info" %}
The blacklist is primarily for reducing unwanted sources; it is not a fact checker or security filter. Websites that are not blocked may still contain incorrect, outdated, or malicious content.
{% endhint %}

## How the Blacklist Works

For Cherry Studio external web search, the app filters URLs against the blacklist after the provider returns results. Matching results are not sent to the model.

For native model web search, blacklist support depends on the model provider:

- Anthropic native search receives converted blocked domains;
- xAI native search receives at most the first `5` converted domains;
- Other native web search services may not support or use the blacklist.

Do not assume that the same rules will behave identically across all models and providers.

## Add Rules

1. Open **Settings → Web Search**;
2. Find **Blacklist**;
3. Enter one rule per line;
4. Click **Save**;
5. Confirm that no “invalid entry” notice appears;
6. Start or continue a Web Search conversation to verify the rules.

The number beside the input indicates how many rules are currently saved.

{% hint style="warning" %}
If even one rule is invalid, the blacklist will not be saved. Correct every invalid entry, then click Save again.
{% endhint %}

## Two Supported Formats

### Match Patterns

Match patterns are useful for blocking websites by protocol, domain, subdomain, and path.

Common examples:

```text
*://*.example.com/*
```

Blocks HTTP and HTTPS pages on `example.com` and all of its subdomains.

```text
https://example.com/private/*
```

Blocks only pages under `https://example.com/private/`.

```text
*://news.example.com/archive/*
```

Blocks only the `archive` path on the specified subdomain.

The structure of a match pattern is:

```text
protocol://host/path
```

| Part | Examples | Description |
| --- | --- | --- |
| Protocol | `https`, `http`, `*` | Here, `*` matches HTTP and HTTPS |
| Host | `example.com`, `*.example.com`, `*` | `*.example.com` matches both the root domain and its subdomains |
| Path | `/*`, `/news/*` | Must begin with `/`; `*` is supported |

For complete rule details, see [MDN Match Patterns](https://developer.mozilla.org/zh-CN/docs/Mozilla/Add-ons/WebExtensions/Match_patterns).

{% hint style="warning" %}
Do not enter only `example.com`. A plain domain is not a valid match pattern; use `*://*.example.com/*`.
{% endhint %}

### Regular Expressions

For more precise URL matching, you can use a regular expression. The rule must begin with `/` and end with `/`:

```text
/example\.(com|org)/
```

```text
/example\.com\/(ads|sponsored)\//
```

Cherry Studio ignores case and tests the rule against the complete “protocol + domain + path + query parameters.”

Regular expressions are useful for:

- Matching multiple top-level domains;
- Blocking pages that contain specific path segments;
- Excluding results based on URL query parameters;
- Rules that are difficult to express with regular match patterns.

For syntax, see the [MDN Regular Expressions Guide](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_expressions).

{% hint style="danger" %}
An overly broad regular expression may accidentally block many results. Do not copy a complex expression from an unknown source if you cannot understand it.
{% endhint %}

## Copyable Examples

Modify these rules as needed:

```text
*://*.example.com/*
*://mirror.example.org/*
https://news.example.net/archive/*
/example\.io\/sponsored/
```

Enter one rule per line. Blank lines are ignored.

### Block a Domain and All Its Subdomains

```text
*://*.example.com/*
```

Matches:

```text
https://example.com/article
https://www.example.com/article
http://docs.example.com/guide
```

### Block Only a Specific Path

```text
https://example.com/ads/*
```

Blocks:

```text
https://example.com/ads/page-1
```

Does not block:

```text
https://example.com/blog/page-1
```

### Block Several Similar Domains

```text
/example\.(com|net|org)/
```

If you need to block only three fixed websites, three separate match patterns are usually easier to maintain.

## Unsupported Legacy Features

The current V2 blacklist page supports only manually entered rules. It does not provide:

- Blocking a website directly from a browser toolbar;
- Downloading rules automatically from a subscription URL;
- Automatically updating uBlacklist subscriptions;
- Importing the complete configuration of a browser extension.

Subscription tables and subscription screenshots in older documentation do not apply to the current interface.

If you need to use a public rule set, inspect its contents first, then manually convert it into match patterns or regular expressions supported by Cherry Studio. Do not paste thousands of rules directly; too many rules are harder to maintain and more likely to block legitimate sources accidentally.

## Verify Rules

After saving, test with a question whose results are easy to observe:

```text
Search example.com for content about Cherry Studio and list the cited sources.
```

If `example.com` is blocked, results from that domain should no longer appear in an external web search answer.

When verifying:

1. Confirm whether the current model is using external or native model web search;
2. Check the final URL of each citation, not only its title;
3. Remember that a web page may redirect to another domain;
4. New rules do not remove old citations already stored in conversation history;
5. Different native web search providers may ignore some rules.

## Troubleshooting

### “Invalid Entry” Appears

Common mistakes:

| Incorrect | Problem | Recommended |
| --- | --- | --- |
| `example.com` | Protocol and path are missing | `*://*.example.com/*` |
| `https://example.com` | Path is missing | `https://example.com/*` |
| `*.example.com` | Not a complete match pattern | `*://*.example.com/*` |
| `/[example/` | Invalid regular expression syntax | Correct the bracket or character class |
| `# example` | Comment lines are not supported | Delete the line |

Correct every invalid entry and save again.

### Blocked Websites Still Appear After Saving

Possible reasons include:

- The current model uses native web search and the provider did not apply the blacklist;
- The rule matches only the root domain, not the actual subdomain;
- The rule matches only HTTPS, but the result uses HTTP;
- The path is too narrow;
- The citation comes from an answer created before the rule was saved;
- The page redirects;
- The model mentioned the website from existing knowledge without searching.

Test with a complete rule such as `*://*.example.com/*` first, then gradually narrow its scope.

### All Search Results Disappear

Check whether you used:

```text
<all_urls>
```

This pattern matches every HTTP and HTTPS URL. Delete it and save again.

Also check whether a regular expression is too broad, for example:

```text
/.*/
```

### Restore the Default State

Clear the blacklist input and click **Save**. When the count changes to `0`, external web search no longer excludes results using custom rules.

## Recommendations

- Block by domain first; use a regular expression only for complex cases;
- Start with a small number of explicit rules;
- Regularly remove expired or duplicate rules;
- Before blocking a website, check whether only some of its pages are low quality;
- Require multiple independent sources for important conclusions;
- Do not use the blacklist as a substitute for manually verifying citations.

***

### 💡 Get Help and Submit Feedback

If you encounter questions, bugs, or feature suggestions during setup or use, see the official channels in [Feedback and Suggestions](../question-contact/suggestions.md).
