
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

---
icon: cherries
---

# GitHub Copilot

GitHub Copilot을 사용하려면 먼저 GitHub 계정이 필요하며 GitHub Copilot 서비스에 구독해야 합니다. 무료 버전도 사용 가능하지만, 무료 버전은 최신 Claude 3.7 모델을 지원하지 않습니다. 자세한 내용은 [GitHub Copilot 공식 사이트](https://github.com/features/copilot)를 참고하세요.

## Device Code 획득

「GitHub 로그인」을 클릭하여 Device Code를 생성하고 복사합니다.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Device Code 획득 예시 이미지"><figcaption><p>Device Code 획득</p></figcaption></figure>

## 브라우저에서 Device Code 입력 및 승인

Device Code를 성공적으로 획득한 후 링크를 클릭해 브라우저를 열고, GitHub 계정으로 로그인한 다음 Device Code를 입력하여 승인합니다.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="GitHub 승인 예시 이미지"><figcaption><p>GitHub 승인</p></figcaption></figure>

승인이 완료되면 Cherry Studio로 돌아와「GitHub 연결」을 클릭합니다. 성공 시 GitHub 사용자명과 프로필 사진이 표시됩니다.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="GitHub 연결 성공 예시 이미지"><figcaption><p>GitHub 연결 성공</p></figcaption></figure>

## 「관리」 클릭으로 모델 목록 확인

하단의「관리」버튼을 클릭하면 자동으로 현재 지원되는 모델 목록을 인터넷에서 불러옵니다.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="관리 버튼으로 모델 목록 확인 예시 이미지"><figcaption><p>모델 목록 확인</p></figcaption></figure>

## 자주 묻는 질문

### Device Code 획득 실패 시 재시도

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Device Code 획득 실패 예시 이미지"><figcaption><p>Device Code 획득 실패</p></figcaption></figure>

현재 Axios를 사용해 요청을 구성하고 있으며, Axios는 socks 프록시를 지원하지 않습니다. 시스템 프록시 또는 HTTP 프록시를 사용하거나, CherryStudio 내 프록시 설정 없이 **글로벌 프록시**를 사용해 주세요. Device Code 획득 실패를 방지하려면 먼저 네트워크 연결 상태를 확인하시기 바랍니다.