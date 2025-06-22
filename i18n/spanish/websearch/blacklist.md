---
icon: ban
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuración de lista negra de búsqueda web

Cherry Studio admite dos métodos para configurar listas negras: manualmente y mediante fuentes de suscripción. Las reglas de configuración hacen referencia a [ublacklist](https://github.com/iorate/ublacklist)

## Configuración manual

Puede agregar reglas a los resultados de búsqueda o hacer clic en el icono de la barra de herramientas para bloquear sitios web específicos. Las reglas se pueden especificar mediante [patrones de coincidencia](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (ejemplo: `*://*.example.com/*`) o utilizando [expresiones regulares](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (ejemplo: `/example\.(net|org)/`).

## Configuración de fuente de suscripción

También puede suscribirse a conjuntos de reglas públicos. Este sitio web lista algunas suscripciones:\
https://iorate.github.io/ublacklist/subscriptions

Aquí hay algunas fuentes de suscripción recomendadas:

| Nombre                                                                                                    | Enlace                                                                                                   | Tipo             |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation)      | https://git.io/ublacklist                                                                                | Chino            |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)              | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | Generado por IA  |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configuración de fuente de suscripción</p></figcaption></figure>