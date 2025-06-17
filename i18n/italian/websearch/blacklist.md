---
icon: ban
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Configurazione della Blacklist per la Ricerca Web

Cherry Studio supporta la configurazione della blacklist tramite aggiunta manuale o sottoscrizione di feed. Per le regole di configurazione, fare riferimento a [ublacklist](https://github.com/iorate/ublacklist)

## Configurazione Manuale

Puoi aggiungere regole ai risultati di ricerca o fare clic sull'icona della barra degli strumenti per bloccare siti web specifici. Le regole possono essere specificate utilizzando: 
- [Schemi di corrispondenza](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (esempio: `*://*.example.com/*`) 
- [Espressioni regolari](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (esempio: `/example\.(net|org)/`).

## Configurazione tramite Sottoscrizione

Puoi inoltre sottoscrivere elenchi di regole pubbliche. Alcuni feed disponibili sono elencati su:\
https://iorate.github.io/ublacklist/subscriptions

Ecco alcuni feed consigliati:

| Nome                                                                                                    | Collegamento                                                                                                   | Tipo     |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | -------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                                     | Cinese   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | Generato da AI |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configurazione dei feed sottoscritti</p></figcaption></figure>