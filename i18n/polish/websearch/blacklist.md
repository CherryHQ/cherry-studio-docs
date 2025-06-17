---
icon: ban
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Konfiguracja czarnej listy wyszukiwania internetowego

Cherry Studio obsługuje ręczną konfigurację czarnej listy oraz dodawanie źródeł subskrypcji. Konfiguracja opiera się na regułach [ublacklist](https://github.com/iorate/ublacklist).

## Konfiguracja ręczna

Możesz dodać reguły do wyników wyszukiwania lub użyć ikony na pasku narzędzi, aby zablokować określone witryny. Reguły można określić za pomocą:  
- [wzorców dopasowania](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (np. `*://*.example.com/*`)  
- [wyrażeń regularnych](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (np. `/example\.(net|org)/`).

## Konfiguracja subskrypcji

Możesz subskrybować publiczne zestawy reguł. Lista dostępnych subskrypcji:  
https://iorate.github.io/ublacklist/subscriptions

Polecane źródła subskrypcji:

| Nazwa                                                                                                    | Link                                                                                                   | Typ       |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Chiński   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | Generowane przez AI |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Konfiguracja subskrypcji</p></figcaption></figure>