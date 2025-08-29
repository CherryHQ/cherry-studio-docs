---
icon: ban
---
# Network Search Blacklist Configuration


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="warning" %}
Cherry Studio supports two ways to configure blacklists: manually and by adding subscription sources. For configuration rules, refer to [ublacklist](https://github.com/iorate/ublacklist)
{% endhint %}

## Manual Configuration

You can add rules for search results or click the toolbar icon to block specific websites. Rules can be specified using [match patterns](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (e.g., `*://*.example.com/*`) or [regular expressions](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (e.g., `/example\.(net|org)/`).

## Subscription Source Configuration

You can also subscribe to public rule sets. This website lists some subscriptions:
https://iorate.github.io/ublacklist/subscriptions

Here are some recommended subscription source links:

| Name                                                                                                    | Link                                                                                                   | Type         |
| :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :----------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Chinese      |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | AI Generated |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Subscription Source Configuration</p></figcaption></figure>