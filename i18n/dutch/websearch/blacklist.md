---
icon: ban
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Configuratie van zwarte lijst voor webzoeken

Cherry Studio ondersteunt twee manieren om een zwarte lijst te configureren: handmatig en door abonnementsbronnen toe te voegen. Zie [ublacklist](https://github.com/iorate/ublacklist) voor configuratieregels.

## Handmatige configuratie

U kunt regels toevoegen aan zoekresultaten of op het werkbalkpictogram klikken om specifieke websites te blokkeren. Regels kunnen worden gespecificeerd met: [patroonovereenkomst](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (voorbeeld: `*://*.example.com/*`) of door [reguliere expressies](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) te gebruiken (voorbeeld: `/example\.(net|org)/`).

## Configuratie van abonnementsbronnen

U kunt zich ook abonneren op openbare regelcollecties. Deze website somt enkele abonnementen op:\
https://iorate.github.io/ublacklist/subscriptions

Hier zijn enkele aanbevolen abonnementsbronkoppelingen:

| Naam                                                                                              | Koppeling                                                                                                   | Type            |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Chinees         |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | AI-gegenereerd  |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configuratie van abonnementsbronnen</p></figcaption></figure>