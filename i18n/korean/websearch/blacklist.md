---
icon: ban
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 웹 검색 블랙리스트 설정

Cherry Studio는 수동과 구독소스 추가 두 가지 방법으로 블랙리스트를 설정할 수 있습니다. 설정 규칙은 [ublacklist](https://github.com/iorate/ublacklist)를 참조하세요.

## 수동 설정

검색 결과에 규칙을 추가하거나 툴바 아이콘을 클릭해 특정 사이트를 차단할 수 있습니다. 규칙은 다음 방식으로 지정할 수 있습니다: [매치 패턴](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (예: `*://*.example.com/*`) 또는 [정규 표현식](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (예: `/example\.(net|org)/`).

## 구독소스 설정

공개 규칙 집합을 구독할 수도 있습니다. 이 웹사이트에서 일부 구독을 확인할 수 있습니다:\  
https://iorate.github.io/ublacklist/subscriptions

추천하는 구독소스 링크 목록입니다:

| 이름                                                                                                    | 링크                                                                                                   | 유형     |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | 중국어    |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | AI 생성 |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>구독소스 설정</p></figcaption></figure>