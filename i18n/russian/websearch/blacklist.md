---
icon: ban
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Настройка черного списка для веб-поиска

Cherry Studio поддерживает два способа настройки черного списка: ручной и добавление источников подписок. Правила конфигурации основаны на [ublacklist](https://github.com/iorate/ublacklist)

## Ручная настройка

Вы можете добавлять правила для результатов поиска или щелкнуть значок на панели инструментов для блокировки определенных сайтов. Правила можно указывать с помощью [шаблонов соответствия](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (например: `*://*.example.com/*`) или [регулярных выражений](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (например: `/example\.(net|org)/`).

## Настройка источников подписок

Вы также можете подписаться на публичные наборы правил. На этом сайте представлен список подписок:\
https://iorate.github.io/ublacklist/subscriptions

Ниже приведены некоторые рекомендуемые источники подписок:

| Название                                                                                                    | Ссылка                                                                                                   | Тип       |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation)     | https://git.io/ublacklist                                                                              | Китайский |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)             | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | Сгенерировано ИИ |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Настройка источников подписок</p></figcaption></figure>