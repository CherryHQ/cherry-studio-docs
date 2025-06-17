---
icon: ban
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Web Arama Karaliste Yapılandırması

Cherry Studio, karalisteyi manuel ekleme ve abonelik beslemeleri ekleme olmak üzere iki yöntemle yapılandırmayı destekler. Yapılandırma kuralları için [ublacklist](https://github.com/iorate/ublacklist)'e bakın.

## Manuel Yapılandırma

Arama sonuçlarınıza kural ekleyebilir veya araç çubuğu simgesine tıklayarak belirli web sitelerini engelleyebilirsiniz. Kurallar şu yollarla belirtilebilir: [eşleşme deseni](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (örnek: `*://*.example.com/*`) veya [düzenli ifade](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) kullanarak (örnek: `/example\.(net|org)/`).

## Abonelik Beslemesi Yapılandırması

Ayrıca genel kural setlerine abone olabilirsiniz. Bazı abonelikler şu sitede listelenmiştir:\
https://iorate.github.io/ublacklist/subscriptions

Önerilen bazı abonelik beslemeleri:

| Ad                                                                                                    | Bağlantı                                                                                                   | Tür   |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Çince |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | AI Üretimi |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Abonelik Beslemesi Yapılandırması</p></figcaption></figure>