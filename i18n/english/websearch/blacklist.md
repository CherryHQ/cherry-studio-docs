---
icon: ban
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Network Search Blacklist Configuration

Cherry Studio supports two methods for configuring blacklists: manual setup and adding subscription sources. Configuration rules reference [ublacklist](https://github.com/iorate/ublacklist)

## Manual Configuration

You can add rules to search results or click the toolbar icon to block specified websites. Rules can be specified using: [match patterns](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (example: `*://*.example.com/*`) or [regular expressions](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (example: `/example\.(net|org)/`).

## Subscription Sources Configuration

You can also subscribe to public rule sets. This website lists some subscriptions:\
https://iorate.github.io/ublacklist/subscriptions

Here are some recommended subscription source links:

| Name                                                                                                    | Link                                                                                                   | Type       |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Chinese    |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | AI Generated |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Subscription Source Configuration</p></figcaption></figure>