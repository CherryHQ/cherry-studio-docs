---
icon: ban
---
# Configuración de lista negra para búsquedas web


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio admite dos métodos para configurar listas negras: manual y mediante suscripción a fuentes. Las reglas de configuración consultan [ublacklist](https://github.com/iorate/ublacklist)

## Configuración manual

Puedes agregar reglas para los resultados de búsqueda o hacer clic en el icono de la barra de herramientas para bloquear sitios web específicos. Las reglas pueden especificarse mediante: [patrones de coincidencia](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (ejemplo: `*://*.example.com/*`) o usando [expresiones regulares](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (ejemplo: `/example\.(net|org)/`).

## Configuración de fuentes

También puedes suscribirte a conjuntos de reglas públicos. Este sitio web muestra algunas suscripciones:\
https://iorate.github.io/ublacklist/subscriptions

Estos son algunos de los enlaces de fuentes más recomendados:

| Nombre                                                                                                    | Enlace                                                                                                   | Tipo        |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation)     | https://git.io/ublacklist                                                                                | Chino       |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)             | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt      | Generado por IA |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configuración de fuente</p></figcaption></figure>