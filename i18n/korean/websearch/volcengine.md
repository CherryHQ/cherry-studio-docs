---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# Volc Engine 인터넷 접속 연동

### 1. 「Volc Engine」 계정 로그인/등록 <a href="#rclz7" id="rclz7"></a>

공식 웹사이트 접속: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Volc Engine 공식 웹사이트</p></figcaption></figure>

### 2. 「인터넷 연결 가능한」 「나의 애플리케이션」 생성 <a href="#gvzaa" id="gvzaa"></a>

2.1. Volc Engine에 로그인 후 「Volc Ark」 페이지 이동: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. <mark style="color:red;">**차례로 클릭: 「나의 애플리케이션」 → 「애플리케이션 생성」 → 「노코드」 → 「1:1 채팅」**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. 정보 입력 후 애플리케이션 배포 <a href="#zzdfe" id="zzdfe"></a>

**애플리케이션 이름**: 요구사항에 따라 자유롭게 지정 (항목 앞에 <mark style="color:red;">**\* 필수**</mark> 표시된 항목만 입력, 나머지는 생략 가능)

<mark style="color:red;">**중요: 인터넷 연결 플러그인 활성화 필요 (사전 개방 필요)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. 인터넷 플러그인 기능 개방 (요금 및 무료 사용 횟수 확인) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>"즉시 구매" 클릭 후 단계별 진행하여 아래 화면이 나타나면 개방 성공</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>상태 확인, 개방 완료</p></figcaption></figure>

이후 이전의 「애플리케이션 정보 입력」 화면으로 돌아가 계속 진행합니다.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. 인터넷 검색 「고급 설정」 설명 <a href="#sp6uz" id="sp6uz"></a>

실제 상황에 따라 선택 개인 권장 사항:

* 입출력 정밀 제어 필요 시 「**사용자 정의 호출**」 사용;
* 번거로움을 피하려면 변경 없이 「**자동 호출**」- 기본값 유지;
* 비용 부담 없고 정보 신속성 요구 시 「**강제 활성화**」.

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. 애플리케이션 배포 <a href="#fe1gf" id="fe1gf"></a>

우측 상단 「배포」 버튼 클릭하여 애플리케이션 생성 완료.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. API Key 획득 <a href="#jtqlu" id="jtqlu"></a>

순차적으로 클릭: **「API 호출 가이드」→「API Key 선택 후 복사」→「확인 및 선택」**

API Key를 먼저 복사한 후 cherry studio에 붙여넣습니다. (상세 절차는 아래 화면 참조)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

참고: API Key 없을 경우 팝업창 우측 상단 - 「**API Key 생성**」 후 복사.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Cherry Studio에서 API Key 사용하여 DeepSeek-R1 인터넷 접속 구현 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Cherry Studio 열기 → 「설정」→ 「임의 이름 작성」→「유형: openAI」 선택 <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. URL 및 Key 설정 <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">주의: 주소 확인 불가 또는 베이징 노드 아닐 경우 아래 위치에서 정확한 주소 확인, "/" 빠짐 주의:</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. 모델 이름 추가 <a href="#qmh3i" id="qmh3i"></a>

주의: 아래 작은 글자를 모델 이름으로 복사해야 함, 그렇지 않으면 오류 발생.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. 실행 효과 미리보기 <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>