---
icon: ban
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Конфигурация чёрного списка для веб-поиска

Cherry Studio поддерживает настройку чёрного списка двумя способами: вручную и через добавление источников подписок. Правила настройки можно найти в [ublacklist](https://github.com/iorate/ublacklist).

## Ручная настройка

Вы можете добавлять правила для результатов поиска или щёлкать по иконке на панели инструментов, чтобы блокировать определённые сайты. Правила можно указывать с помощью [шаблонов соответствия](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (например: `*://*.example.com/*`) или с использованием [регулярных выражений](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (например: `/example\\.(net|org)/`).

## Настройка через источники подписок

Вы также можете подписываться на публичные наборы правил. Некоторые подписки перечислены на сайте:\
https://iorate.github.io/ublacklist/subscriptions

Ниже приведены некоторые рекомендуемые источники подписок:

| Название                                                                                                    | Ссылка                                                                                                   | Тип        |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation)       | https://git.io/ublacklist                                                                                | Китайский  |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)               | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt     | Генерируемый ИИ |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Настройка источников подписок</p></figcaption></figure>