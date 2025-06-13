---
icon: ban
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configuração de Lista Negra de Pesquisa na Web

O Cherry Studio suporta dois métodos para configurar listas negras: manualmente e através de fontes de assinatura. As regras de configuração são baseadas no [ublacklist](https://github.com/iorate/ublacklist)

## Configuração Manual

Você pode adicionar regras aos resultados de pesquisa ou clicar no ícone da barra de ferramentas para bloquear sites específicos. As regras podem ser especificadas usando: [Padrões de correspondência](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (exemplo: `*://*.example.com/*`) ou [Expressões regulares](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (exemplo: `/example\.(net|org)/`).

## Configuração de Feed de Assinaturas

Você também pode assinar conjuntos de regras públicas. Este site lista algumas assinaturas:\
https://iorate.github.io/ublacklist/subscriptions

Aqui estão alguns feeds de assinatura recomendados:

| Nome                                                                                                                              | Link                                                                                                                                 | Tipo           |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation)                             | https://git.io/ublacklist                                                                                                            | Chinês         |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)                                     | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt                                 | Gerado por IA  |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configuração de Feed de Assinaturas</p></figcaption></figure>