
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 화웨이 클라우드(Huawei Cloud)

1. [화웨이 클라우드](https://auth.huaweicloud.com/authui/login)에서 계정 생성 및 로그인

2. [이 링크](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) 클릭하여 MaaS 콘솔 접속

3. 권한 부여

<details>

<summary>권한 부여 단계 (이미 부여한 경우 건너뜀)</summary>

1. 위 링크 페이지 접속 후 안내에 따라 권한 부여 페이지 이동(IAM 서브 사용자 → 신규 위임 → 일반 사용자)

![](<../../.gitbook/assets/image (49).png>)

2. 생성 후 (2)의 링크 페이지로 재접속
3. 접근 권한 부족 안내 → "여기를 클릭하세요" 선택
4. 기존 권한 추가 및 확인

![](<../../.gitbook/assets/image (50).png>)

&#x20;주의: 초보자를 위한 방법으로, 복잡한 내용 없이 안내만 따라 클릭하면 됩니다. 직접 성공적으로 권한 부여할 수 있다면 본인 방식으로 진행 가능합니다.

</details>

4. 사이드바에서 '인증 관리' 선택 → API Key(비밀키) 생성 및 복사

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

CherryStudio에서 새 서비스 제공자 생성

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

생성 후 비밀키 입력

5. 사이드바에서 '모델 배포' 선택 → 모두 받기

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6. 호출(call) 클릭

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

① 위치의 주소 복사 → CherryStudio 서비스 제공자 주소 필드에 붙여넣기 → 끝에 "#" 추가

끝에 "#" 추가

끝에 "#" 추가

끝에 "#" 추가

끝에 "#" 추가

"#" 추가 이유는 [여기 참조](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> 해당 설명을 보지 않고 바로 따라해도 되며,
>
> v1/chat/completions 부분을 삭제하는 방식으로 입력해도 무방합니다. 방법을 알고 있다면 자유롭게 진행하되, 모를 경우 반드시 안내대로 진행하세요.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

② 위치 모델 이름 복사 → CherryStudio에서 "+추가" 버튼 클릭 → 새 모델 생성

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

모델 이름 입력 (예시와 정확히 동일하게, 인용부호 없이)

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

모델 추가 버튼 클릭으로 완료

{% hint style="info" %}
화웨이 클라우드는 모델별로 주소가 다르므로, 각 모델마다 새 서비스 제공자를 생성해야 합니다. 위 단계를 모델마다 반복 적용하세요.
{% endhint %}