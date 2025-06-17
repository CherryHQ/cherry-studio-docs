
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 바이트댄스(도우빈)

*   [화산 엔진](https://console.volcengine.com/)에 로그인
*   직접 [여기 클릭](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)하여 바로 이동

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### API Key 획득

*   사이드바 하단의 [API Key 관리](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) 클릭
*   API Key 생성

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   생성 완료 후, 생성된 API Key 옆의 👁️ 아이콘을 클릭하여 확인 및 복사

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   복사한 API Key를 Cherry Studio에 입력한 후, 서비스 제공사 스위치를 활성화합니다.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### 모델 활성화 및 추가

*   방주 콘솔 사이드바 하단의 [활성화 관리](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false)에서 필요한 모델을 활성화하세요. (도우빈 시리즈 및 DeepSeek 등)

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   [모델 목록 문서](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)에서 필요한 모델의 **모델 ID**를 확인하세요.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="화산 엔진 모델 ID 예시"><figcaption></figcaption></figure>

*   Cherry Studio의 [모델 서비스](../../cherrystudio/preview/settings/providers.md) 설정에서 **화산 엔진** 선택
*   **추가** 버튼 클릭 후, 획득한 **모델 ID**를 입력란에 복사하세요

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   동일한 절차로 필요한 모델을 순차적으로 추가합니다

### API 주소

API 주소는 두 가지 형식으로 작성 가능합니다:
1.  클라이언트 기본값: `https://ark.cn-beijing.volces.com/api/v3/`
2.  대체 형식: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
두 형식 간 차이는 없으므로 기본값을 유지하면 됩니다.

`/`와 `#`로 끝나는 차이점은 서비스 제공사 설정의 [API 주소 부분](../../cherrystudio/preview/settings/providers.md#api-di-zhi)을 참조하세요.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>공식 문서 cURL 예시</p></figcaption></figure>