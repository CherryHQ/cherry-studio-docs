---
icon: cloud-check
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 서비스 제공자 설정

현재 페이지는 인터페이스 기능 소개만을 목적으로 합니다. 구성 튜토리얼은 기초 튜토리얼의 [서비스 제공자 설정](../../../pre-basic/providers/)을 참조하세요.

{% hint style="info" %}
* 내장 서비스 제공자를 사용할 때는 해당 비밀키만 입력하면 됩니다.
* 서비스 제공자마다 비밀키에 대한 명칭이 다를 수 있으며, 비밀키, Key, API Key, 토큰 등은 모두 동일한 개념을 지칭합니다.
{% endhint %}

### API 비밀키

Cherry Studio에서는 단일 서비스 제공자가 여러 키를 순차적으로 사용할 수 있도록 지원하며, 순환 방식은 앞에서 뒤로 목록을 순회하는 방식입니다.

* 여러 키는 영문 쉼표로 구분하여 추가합니다. 예시:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
반드시 **영문** 쉼표를 사용해야 합니다.
{% endhint %}

### API 주소

내장 서비스 제공자를 사용할 때는 일반적으로 API 주소를 입력할 필요가 없습니다. 수정이 필요한 경우 공식 문서의 주소를 정확히 따라 입력하세요.

> 서비스 제공자가 <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> 형식의 주소를 제공하는 경우 루트 주소(<mark style="background-color:red;">https://xxx.xxx.com</mark>)만 입력하면 됩니다.
>
> Cherry Studio가 나머지 경로(<mark style="background-color:green;">/v1/chat/completions</mark>)를 자동으로 연결합니다. 지시사항을 따르지 않으면 정상 작동하지 않을 수 있습니다.

{% hint style="info" %}
참고: 대부분 서비스 제공자의 대규모 언어 모델 경로는 통일되어 있어 특별 조정이 필요 없습니다.  
API 경로가 v2, v3/chat/completions 등 다른 버전일 때는 주소 끝에 버전과 '`/`'를 명시하고,  
비정상적인 경로(<mark style="background-color:green;">/v1/chat/completions</mark> 외)의 경우 제공된 전체 주소 끝에 '`#`'를 추가하세요.

즉:
* API 주소가 '`/`'로 끝나면 "<mark style="background-color:green;">chat/completions</mark>"만 자동 연결
* API 주소가 '`#`'로 끝나면 입력 주소를 그대로 사용 (자동 연결 없음)

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### 모델 추가

일반적으로 서비스 제공자 설정 페이지 좌측 하단 `관리` 버튼을 클릭하면 호출 가능한 모든 모델 목록을 자동으로 불러옵니다. 목록에서 원하는 모델 오른쪽의 `+`를 클릭해 추가하세요.

{% hint style="info" %}
`관리` 버튼으로 불러온 모델은 자동 추가되지 않습니다. 반드시 모델별 `+`를 클릭해 서비스 제공자 모델 목록에 등록해야 실제 모델 선택창에 표시됩니다.
{% endhint %}

### 연결성 검사

API 비밀키 입력란 옆의 검사 버튼을 클릭해 정상 설정 여부를 확인합니다.

{% hint style="info" %}
검사 시 모델 목록의 마지막 대화 모델을 기본값으로 사용합니다. 실패 시 모델 목록에 잘못되었거나 미지원 모델이 있는지 확인하세요.
{% endhint %}

{% hint style="danger" %}
구성 완료 후 반드시 우상단 스위치를 활성화해야 합니다. 그렇지 않으면 서비스 제공자가 비활성 상태이며, 모델 목록에서 해당 모델을 찾을 수 없습니다.
{% endhint %}