---
icon: ban
---
# Configuração da Lista Negra de Pesquisa na Web


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Cherry Studio suporta a configuração de lista negra de duas maneiras: manual e por adição de fontes de subscrição. As regras de configuração referem-se ao [ublacklist](https://github.com/iorate/ublacklist)

## Configuração Manual

Você pode adicionar regras aos resultados de pesquisa ou clicar no ícone da barra de ferramentas para bloquear sites específicos. As regras podem ser especificadas através de: [padrões de correspondência](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (exemplo: `*://*.example.com/*`) ou usando [expressões regulares](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (exemplo: `/example\.(net|org)/`).

## Configuração de Fontes de Subscrição

Você também pode subscrever conjuntos de regras públicas. Este site lista algumas subscrições:\  
https://iorate.github.io/ublacklist/subscriptions

Aqui estão alguns links de subscrição recomendados:

| Nome                                                                                                    | Link                                                                                                   | Tipo       |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------- |
| [Compilação de subscrições uBlacklist](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                              | Chinês     |
| [Lista de Bloqueio Huge AI para uBlockOrigin](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist) | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | Gerada por IA |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Configuração de Fontes de Subscrição</p></figcaption></figure>