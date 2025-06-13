---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 온라인 모드

{% hint style="info" %}
인터넷 연결이 필요한 시나리오 예시:

* 시의성 있는 정보: 예) 오늘/이번 주/방금 전 금 선물 가격 등
* 실시간 데이터: 예) 날씨, 환율 등 동적 수치
* 새로운 지식: 예) 새로 등장한 사물, 개념, 기술 등...
{% endhint %}

### 1. 인터넷 연결 활성화 방법

Cherry Studio의 질문 창에서 [지구 아이콘]을 클릭하면 인터넷 연결이 활성화됩니다.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>지구 아이콘 클릭 - 인터넷 연결 활성화</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>인터넷 연결 기능이 활성화되었음을 표시</p></figcaption></figure>

### 2. 특별 주의사항: 두 가지 인터넷 연결 모드

#### 모드 1: 모델 제공업체의 대규모 언어 모델 자체 내장 인터넷 기능

이 경우, 인터넷 연결을 활성화하면 바로 인터넷 서비스를 사용할 수 있어 매우 간편합니다.

{% hint style="warning" %}
질의응답 화면 상단의 모델 이름 뒤에 작은 지구 아이콘이 표시되는지 확인하면 해당 모델의 인터넷 지원 여부를 빠르게 판단할 수 있습니다.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

모델 관리 페이지에서도 이 방법으로 인터넷을 지원하는 모델과 지원하지 않는 모델을 신속하게 구분할 수 있습니다.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio에서 현재 지원하는 인터넷 연결 모델 제공업체**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter(전체 모델 인터넷 지원)</mark>
> * <mark style="color:green;">텐센트 혼위안</mark>
> * <mark style="color:green;">지프AI</mark>
> * <mark style="color:green;">알리바바 클라우드 바이란 등</mark>

{% hint style="danger" %}
특별 주의사항:

모델에 작은 지구 아이콘이 표시되지 않더라도 인터넷 연결이 가능한 특수한 경우가 있습니다. 아래 가이드 문서에서 설명하는 상황이 그 예입니다.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### 모드 2: 모델에 인터넷 기능이 없는 경우 Tavily 서비스 활용

인터넷 기능이 없는 대규모 언어 모델(이름 뒤에 지구 아이콘 없음)을 사용하면서 실시간 정보 처리가 필요한 경우, Tavily 웹 검색 서비스를 활용해야 합니다.

**Tavily 서비스를 처음 사용할 때**는 설정 안내 팝업이 나타납니다. 지시에 따라 간단하게 설정하세요!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>팝업에서 "설정으로 이동" 클릭</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>API 키 발급 클릭</p></figcaption></figure>

API 키 발급을 클릭하면 **Tavily 공식 사이트** 로그인/회원가입 페이지로 자동 이동합니다. 등록 후 로그인하여 API 키를 생성하고, 해당 키를 Cherry Studio에 복사해 붙여넣기만 하면 됩니다.

{% hint style="danger" %}
등록 방법이 불편할 경우, 본 문서와 동일한 디렉터리에 있는 Tavily 등록 가이드를 참조하세요.
{% endhint %}

**Tavily 등록 참고 문서:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

아래 화면이 표시되면 등록이 완료된 것입니다.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>API 키 복사</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>키 붙여넣기, 설정 완료</p></figcaption></figure>

다시 한번 효과를 확인해 보세요. 결과에서 정상적으로 인터넷 검색이 수행되었으며, 기본값으로 설정된 검색 결과 수(5개)가 적용된 것을 볼 수 있습니다.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
주의: Tavily는 월간 무료 사용량 제한이 있으며, 이를 초과하면 요금이 부과됩니다.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: 오류를 발견하시면 언제든지 연락 주시기 바랍니다.