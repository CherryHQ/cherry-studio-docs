---
icon: ban
---
# Configuration de liste noire pour les recherches web


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio permet de configurer les listes noires manuellement ou via des sources d'abonnement. Les règles de configuration suivent les références [ublacklist](https://github.com/iorate/ublacklist).

## Configuration manuelle

Vous pouvez ajouter des règles aux résultats de recherche ou cliquer sur l'icône de la barre d'outils pour bloquer des sites spécifiques. Les règles peuvent être définies via :
- [Modèles de correspondance](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (ex: `*://*.example.com/*`)
- [Expressions régulières](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (ex: `/example\.(net|org)/`)

## Configuration par abonnement

Vous pouvez également souscrire à des ensembles de règles publics. Ce site liste certains abonnements :\
https://iorate.github.io/ublacklist/subscriptions

Voici quelques sources d'abonnement recommandées :

| Nom                                                                                                    | Lien                                                                                                   | Type         |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------|
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                              | Chinois      |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt    | Généré par IA |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configuration de source d'abonnement</p></figcaption></figure>