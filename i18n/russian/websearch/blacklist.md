---
icon: ban
---
# Конфигурация черного списка веб-поиска


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




Cherry Studio поддерживает ручную настройку черного списка и добавление подписок. Правила настройки основаны на [ublacklist](https://github.com/iorate/ublacklist)

## Ручная настройка

Вы можете добавлять правила для результатов поиска или использовать значок на панели инструментов, чтобы заблокировать определенные сайты. Правила могут быть заданы с помощью [шаблонов соответствия](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (пример: `*://*.example.com/*`) или [регулярных выражений](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (пример: `/example\.(net|org)/`).

## Настройка через подписки

Вы также можете подписаться на публичные наборы правил. На этом сайте перечислены некоторые подписки:\
https://iorate.github.io/ublacklist/subscriptions

Вот несколько рекомендуемых источников подписок:

| Название                                                                                               | Ссылка                                                                                                | Тип     |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------|
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                             | Китайский |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)          | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | AI-генерация |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Настройка подписок</p></figcaption></figure>