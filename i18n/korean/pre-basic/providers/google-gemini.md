
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# Google Gemini

## APIKey 발급받기

* Gemini의 API key를 발급받기 전에 Google Cloud 프로젝트가 필요합니다(이미 보유 중인 경우 이 과정은 건너뛸 수 있습니다).
* [Google Cloud](https://console.cloud.google.com/projectcreate)에 접속해 프로젝트를 생성하고, 프로젝트 이름을 입력한 뒤 '프로젝트 만들기'를 클릭하세요.

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

* 공식 [API Key 페이지](https://aistudio.google.com/app/apikey?hl=zh-cn)에서 `키 만들기` 버튼을 클릭하세요.

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

* 생성된 키를 복사하고, CherryStudio의 [서비스 공급자 설정](broken-reference)을 엽니다.
* 서비스 공급자 목록에서 Gemini를 찾아 방금 획득한 키를 입력합니다.

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

* 하단의 '관리' 또는 '추가' 버튼을 클릭해 지원되는 모델을 추가하고, 우측 상단의 서비스 공급자 스위치를 활성화하면 사용할 수 있습니다.

{% hint style="info" %}
- 중국(타이완 제외) 지역에서는 Google Gemini 서비스를 직접 이용할 수 없으며, 프록시 문제를 별도로 해결해야 합니다.
{% endhint %}