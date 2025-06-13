---
icon: ban
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Konfiguration der Netzsuch-Blacklist

Cherry Studio unterstützt die manuelle Konfiguration der Blacklist sowie das Hinzufügen über Abonnementquellen. Die Konfigurationsregeln basieren auf [ublacklist](https://github.com/iorate/ublacklist)

## Manuelle Konfiguration

Sie können Regeln für Suchergebnisse hinzufügen oder über das Symbol in der Symbolleiste bestimmte Websites blockieren. Regeln können mittels folgender Methoden definiert werden: [Match Patterns](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (Beispiel: `*://*.example.com/*`) oder über [reguläre Ausdrücke](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (Beispiel: `/example\.(net|org)/`).

## Abonnementquellen konfigurieren

Sie können auch öffentliche Regelsätze abonnieren. Auf dieser Website finden Sie einige Abonnements:\
https://iorate.github.io/ublacklist/subscriptions

Hier einige empfohlene Abonnementlinks:

| Name                                                                                                    | Link                                                                                                   | Typ       |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Chinesisch |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | KI-generiert |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Aboquelle konfigurieren</p></figcaption></figure>