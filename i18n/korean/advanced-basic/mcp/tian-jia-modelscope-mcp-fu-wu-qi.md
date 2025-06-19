
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 모델스코프 MCP 서버 추가하기

> 모델스코프 MCP 서버 추가는 Cherry Studio를 v1.2.9 이상으로 업그레이드해야 합니다.

v1.2.9 버전에서 Cherry Studio는 모델스코프 모다와 공식 협업하여 MCP 서버 추가 절차를 획기적으로 간소화했습니다. 구성 오류를 방함은 물론 모델스코프 커뮤니티에서 방대한 MCP 서버를 발견할 수 있습니다. 다음 단계를 따라 Cherry Studio에서 모델스코프의 MCP 서버를 동기화하는 방법을 살펴보겠습니다.

## 작업 절차

### 동기화 진입점:
설정의 MCP 서버 설정에서 `서버 동기화` 선택

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### MCP 서비스 발견:
ModelScope 선택 후 MCP 서비스 탐색

<figure><img src="../../.gitbook/assets/image (1) (4).png" alt=""><figcaption></figcaption></figure>

### MCP 서버 상세 정보 확인
모델스코프에 로그인 후 MCP 서비스 상세 정보 확인

<figure><img src="../../.gitbook/assets/image (2) (6).png" alt=""><figcaption></figcaption></figure>

### 서버 연결
MCP 서비스 상세 정보에서 "서비스 연결" 선택

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### API 토큰 신청 및 복사/붙여넣기
Cherry Studio에서 "API 가져오기" 클릭 → 모델스코프 공식 사이트 이동 → API 토큰 복사 → Cherry Studio에 붙여넣기

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### 동기화 성공
Cherry Studio MCP 서버 목록에서 연결된 모델스코프 MCP 서비스 확인 및 대화에서 호출 가능

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### 증분 업데이트
향후 모델스코프 웹에서 새로 연결된 MCP 서버는 `서버 동기화` 클릭만으로 추가 가능

<figure><img src="../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

이상의 단계를 통해 Cherry Studio에서 모델스코프의 MCP 서버를 간편하게 동기화하는 방법을 완벽히 마스터하셨습니다. 수동 구성의 번거로움과 잠재적 오류를 효과적으로 방지하는 동시에, 모델스코프 커뮤니티가 제공하는 방대한 MCP 서버 리소스에 손쉽게 접근할 수 있습니다.

이 강력한 MCP 서비스들을 탐색하고 활용하여 Cherry Studio 사용 경험에 더 많은 편의와 가능성을 선사하세요!