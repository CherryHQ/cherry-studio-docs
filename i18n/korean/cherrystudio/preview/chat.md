---
icon: message
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 대화 인터페이스

## 어시스턴트와 토픽

### 어시스턴트

`어시스턴트`는 선택한 모델에 개인화된 설정을 적용하여 사용하는 것으로, 프롬프트 프리셋 및 매개변수 프리셋 등을 통해 선택한 모델이 예상한 작업에 더 잘 부합하도록 합니다.

`시스템 기본 어시스턴트`는 비교적 범용적인 매개변수(프롬프트 없음)로 사전 설정되어 있으며, 직접 사용하거나 [에이전트 페이지](agents.md)에서 필요한 프리셋을 찾아 사용할 수 있습니다.

### 토픽

`어시스턴트`는 `토픽`의 상위 집합입니다. 단일 어시스턴트 아래에서 여러 토픽(즉, 대화)을 생성할 수 있으며, 모든 `토픽`은 `어시스턴트`의 매개변수 설정 및 프리셋 프롬프트(prompt) 등의 모델 설정을 공유합니다.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 대화 창 내 버튼

<figure><img src="../../.gitbook/assets/대화 인터페이스/대화창.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/대화 인터페이스/새 토픽.png) `새 토픽` 현재 어시스턴트 내에서 새 토픽을 생성합니다.

![](../../.gitbook/assets/대화 인터페이스/이미지 또는 문서 업로드.png) `이미지 또는 문서 업로드` 이미지 업로드에는 모델 지원이 필요하며, 문서 업로드 시 자동으로 텍스트로 변환되어 모델에 컨텍스트로 제공됩니다.

![](../../.gitbook/assets/대화 인터페이스/웹 검색.png) `웹 검색` 설정에서 웹 검색 관련 정보를 구성해야 하며, 검색 결과는 대형 모델에 컨텍스트로 반환됩니다. 자세한 내용은 [온라인 모드](../../websearch/) 참조.

![](../../.gitbook/assets/대화 인터페이스/지식 베이스.png) `지식 베이스` 지식 베이스 활성화, 자세한 내용은 [지식 베이스 튜토리얼](../../knowledge-base/knowledge-base.md) 참조.

![](<../../.gitbook/assets/대화 인터페이스/MCP 서버.png>) `MCP 서버` MCP 서버 기능 활성화, 자세한 내용은 [MCP 사용 튜토리얼](../../advanced-basic/mcp/) 참조.

![](../../.gitbook/assets/대화 인터페이스/이미지 생성.png) `이미지 생성` 기본적으로 표시되지 않으며, 이미지 생성이 지원되는 모델(예: Gemini)의 경우 수동으로 켜야 이미지 생성이 가능합니다.

{% hint style="info" %}
기술적인 이유로 이미지 생성을 위해 수동으로 버튼을 켜야 합니다. 이 기능이 최적화되면 해당 버튼은 제거될 예정입니다.
{% endhint %}

![](../../.gitbook/assets/대화 인터페이스/모델 선택.png) `모델 선택` 이후 대화를 위해 지정된 모델로 전환하며 컨텍스트는 유지됩니다.

![](../../.gitbook/assets/대화 인터페이스/빠른 문구.png) `빠른 문구` 먼저 설정에서 자주 사용하는 문구를 사전 설정하고 여기서 호출하여 직접 입력하며 변수를 지원합니다.

![](../../.gitbook/assets/대화 인터페이스/메시지 지우기.png) `메시지 지우기` 해당 토픽의 모든 내용을 삭제합니다.

![](../../.gitbook/assets/대화 인터페이스/확장.png) `확장` 대화창을 더 크게 만들어 긴 텍스트 입력을 용이하게 합니다.

![](../../.gitbook/assets/대화 인터페이스/컨텍스트 지우기.png) `컨텍스트 지우기` 내용을 삭제하지 않고 모델이 접근할 수 있는 컨텍스트를 차단합니다. 즉, 모델은 이전 대화 내용을 "잊게" 됩니다.

![](<../../.gitbook/assets/대화 인터페이스/예상 토큰 수.png>) `예상 토큰 수` 예상 토큰 수를 표시하며, 네 개의 데이터는 각각 `현재 컨텍스트 수`, `최대 컨텍스트 수` (∞는 무제한 컨텍스트 의미), `현재 입력창 메시지 단어 수`, `예상 토큰 수` 입니다.

{% hint style="info" %}
이 기능은 토큰 수 예측만을 위한 것으로, 실제 토큰 수는 각 모델마다 다릅니다. 모델 공급자의 데이터를 기준으로 하세요.
{% endhint %}

![](../../.gitbook/assets/대화 인터페이스/번역.png) `번역` 현재 입력창 내용을 영어로 번역합니다.

## 대화 설정

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 모델 설정

모델 설정은 어시스턴트 설정의 `모델 설정` 매개변수와 동기화됩니다. 자세한 내용은 [어시스턴트 설정](chat.md#편집-어시스턴트) 참조.

{% hint style="info" %}
대화 설정에서 모델 설정만 현재 어시스턴트에 적용되며 나머지 설정은 전역에 적용됩니다. 예: 메시지 스타일을 말풍선으로 설정하면 모든 어시스턴트의 모든 토픽에서 말풍선 스타일이 적용됩니다.
{% endhint %}

### 메시지 설정

#### <mark style="color:blue;">**`메시지 구분선`**</mark>:

구분선을 사용해 메시지 본문과 작업 막대를 분리합니다.

{% tabs %}
{% tab title="활성 시" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="비활성 시" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`세리프 글꼴 사용`**</mark>：

글꼴 스타일 전환. [사용자 정의 CSS](../../personalization-settings/)를 통해 글꼴을 변경할 수도 있습니다.

#### <mark style="color:blue;">**`코드에 줄 번호 표시`**</mark>：

모델이 코드 조각을 출력할 때 코드 블록에 줄 번호를 표시합니다.

{% tabs %}
{% tab title="비활성 시" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="활성 시" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`코드 블록 접기 가능`**</mark>：

활성화 시 코드 조각의 코드가 길면 코드 블록이 자동으로 접힙니다.

#### <mark style="color:blue;">**`코드 블록 줄바꿈 가능`**</mark>：

활성화 시 코드 조각의 한 줄이 길면(창을 초과할 때) 자동으로 줄바꿈됩니다.

#### <mark style="color:blue;">**`사고 과정 자동 접기`**</mark>：

활성화 시 사고가 지원되는 모델은 사고 완료 후 사고 과정을 자동으로 접습니다.

#### <mark style="color:blue;">**`메시지 스타일`**</mark>：

대화 인터페이스를 말풍선 스타일 또는 목록 스타일로 전환할 수 있습니다.

#### <mark style="color:blue;">**`코드 스타일`**</mark>：

코드 조각의 표시 스타일을 전환할 수 있습니다.

#### <mark style="color:blue;">**`수학 공식 엔진`**</mark>：

* KaTeX은 성능 최적화를 위해 설계되어 렌더링 속도가 더 빠름
* MathJax는 렌더링 속도가 느리지만 기능이 더 포괄적이며 더 많은 수학 기호와 명령을 지원함

#### <mark style="color:blue;">**`메시지 글꼴 크기`**</mark>：

대화 인터페이스의 글꼴 크기를 조정합니다.

### 입력 설정

#### <mark style="color:blue;">**`예상 토큰 수 표시`**</mark>：

입력창에 입력 텍스트의 예상 토큰 소모량을 표시합니다(실제 컨텍스트 소모 토큰이 아니며 참고용).

#### <mark style="color:blue;">**`긴 텍스트를 파일로 붙여넣기`**</mark>：

다른 곳에서 긴 텍스트를 복사해 입력창에 붙여넣을 때 자동으로 파일 스타일로 표시되어 후속 입력 시 방해를 줄입니다.

#### <mark style="color:blue;">**`Markdown 렌더링 입력 메시지`**</mark>：

비활성화 시 모델 응답 메시지만 렌더링하고 전송된 메시지는 렌더링하지 않음.

{% tabs %}
{% tab title="비활성 시" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="활성 시" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`빠른 스페이스 3회 탭으로 번역`**</mark>：

대화 인터페이스 입력창에 메시지를 입력한 후 스페이스바를 세 번 연속 탭하면 입력 내용이 영어로 번역됨.

{% hint style="warning" %}
참고: 이 작업은 원본 텍스트를 덮어씁니다.
{% endhint %}

#### <mark style="color:blue;">**`대상 언어`**</mark>：

입력창 번역 버튼 및 빠른 스페이스 3회 탭 번역의 대상 언어를 설정합니다.

## 어시스턴트 설정

어시스턴트 인터페이스에서 설정할 <mark style="background-color:yellow;">어시스턴트 이름</mark> 선택→<mark style="background-color:yellow;">우클릭 메뉴</mark>에서 해당 설정 선택

### 어시스턴트 편집

{% hint style="info" %}
어시스턴트 설정은 해당 어시스턴트의 모든 토픽에 적용됩니다.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 프롬프트 설정

#### <mark style="color:blue;">**`이름`**</mark>：

식별하기 쉬운 어시스턴트 이름을 사용자 정의할 수 있음.

#### <mark style="color:blue;">**`프롬프트`**</mark>：

즉 prompt이며, 에이전트 페이지의 프롬프트 작성법을 참조하여 내용 편집 가능.

#### 모델 설정

#### <mark style="color:blue;">**`기본 모델`**</mark>：

해당 어시스턴트에 기본 모델을 고정할 수 있으며, 에이전트 페이지에서 추가 시 또는 어시스턴트 복사 시 초기 모델이 이 모델임. 이 항목을 설정하지 않으면 초기 모델은 전역 초기 모델(즉 [기본 어시스턴트 모델](settings/default-models.md#기본-어시스턴트-모델))임.

{% hint style="info" %}
어시스턴트의 기본 모델은 두 가지 유형이 있습니다. 하나는 [전역 기본 대화 모델](settings/default-models.md#기본-어시스턴트-모델)이고 다른 하나는 어시스턴트 기본 모델입니다. 어시스턴트 기본 모델은 전역 기본 대화 모델보다 우선순위가 높습니다. 어시스턴트 기본 모델을 설정하지 않으면 어시스턴트 기본 모델=전역 기본 대화 모델이 됩니다.
{% endhint %}

#### <mark style="color:blue;">**`자동 모델 재설정`**</mark>：

활성화 시 - 해당 토픽에서 사용 중 다른 모델로 전환 후 새 토픽을 생성하면 새 토픽의 모델이 어시스턴트 기본 모델로 재설정됨. 이 항목이 비활성화 시 새 토픽 모델은 이전 토픽이 사용한 모델을 따름.

> 예: 어시스턴트 기본 모델이 gpt-3.5-turbo이고, 해당 어시스턴트 아래에서 토픽1을 생성한 후, 토픽1의 대화 과정에서 gpt-4o로 전환했다면:
>
> 자동 재설정 활성 시: 새 토픽2 생성 시, 토픽2 기본 선택 모델은 gpt-3.5-turbo임
>
> 자동 재설정 비활성 시: 새 토픽2 생성 시, 토픽2 기본 선택 모델은 gpt-4o임

#### <mark style="color:blue;">**`온도 (Temperature)`**</mark> ：

온도 매개변수는 모델이 생성하는 텍스트의 무작위성과 창의성 정도를 제어합니다(기본값 0.7). 구체적 특징:

* 낮은 온도 값(0-0.3):
  * 출력이 더 결정적이고 집중적임
  * 코드 생성, 데이터 분석 등 정확성이 필요한 시나리오에 적합
  * 가장 가능성 높은 어휘 선택 경향
* 중간 온도 값(0.4-0.7):
  * 창의성과 일관성의 균형
  * 일상 대화, 일반 글쓰기에 적합
  * 챗봇 대화에 권장(0.5 기준)
* 높은 온도 값(0.8-1.0):
  * 더 창의적이고 다양한 출력 생성
  * 창의적 글쓰기, 브레인스토밍 등 시나리오에 적합
  * 텍스트 일관성 저하 가능성 있음

#### <mark style="color:blue;">**`Top P (핵 샘플링)`**</mark>：

기본값 1. 값이 작을수록 AI 생성 내용이 단조롭고 이해하기 쉬우며, 값이 클수록 AI 응답 어휘 범위가 넓어져 다양해짐.

핵 샘플링은 어휘 선택 확률 임계값 제어를 통해 출력에 영향을 줌:

* 작은 값(0.1-0.3):
  * 최고 확률 어휘만 고려
  * 출력이 더 보수적이고 제어 가능
  * 코드 주석, 기술 문서 등 시나리오 적합
* 중간 값(0.4-0.6):
  * 어휘 다양성과 정확성 균형
  * 일반 대화 및 글쓰기 작업에 적합
* 큰 값(0.7-1.0):
  * 광범위한 어휘 선택 고려
  * 풍부하고 다양한 콘텐츠 생성
  * 표현 다양성이 필요한 창의적 글쓰기 시나리오 적합

{% hint style="info" %}
- 이 두 매개변수는 독립적으로 또는 조합해 사용 가능
- 특정 작업 유형에 적합한 매개변수 값 선택
- 실험을 통해 특정 애플리케이션 시나리오에 가장 적합한 매개변수 조합 찾기 권장
- 위 내용은 개념 이해를 위한 참고용이며, 주어진 매개변수 범위가 모든 모델에 적합하지 않을 수 있음. 구체적인 내용은 모델 관련 문서 참조
{% endhint %}

#### <mark style="color:blue;">**`컨텍스트 창 크기 (Context Window)`**</mark>

컨텍스트에 보관할 메시지 수