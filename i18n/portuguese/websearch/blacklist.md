---
icon: ban
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configuração da Lista Negra de Pesquisa na Web

O Cherry Studio suporta duas formas de configurar a lista negra: manualmente e através da adição de fontes de assinatura. As regras de configuração seguem a referência do [ublacklist](https://github.com/iorate/ublacklist).

## Configuração Manual

Você pode adicionar regras aos resultados de pesquisa ou clicar no ícone da barra de ferramentas para bloquear sites específicos. As regras podem ser especificadas através de:
- [Padrões de correspondência](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (exemplo: `*://*.example.com/*`)
- [Expressões regulares](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (exemplo: `/example\.(net|org)/`).

## Configuração de Fontes de Assinatura

Você também pode assinar conjuntos de regras públicos. Este site lista algumas assinaturas:  
https://iorate.github.io/ublacklist/subscriptions

Abaixo estão algumas fontes de assinatura recomendadas:

| Nome                                                                                                    | Link                                                                                                   | Tipo        |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                              | Chinês      |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | Gerado por IA |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configuração de fontes de assinatura</p></figcaption></figure>