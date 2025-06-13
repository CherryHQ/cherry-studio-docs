---
icon: database
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 데이터 설정

이 인터페이스에서는 클라이언트 데이터의 클라우드 및 로컬 백업, 로컬 데이터 디렉토리 조회, 캐시 삭제 등의 작업을 수행할 수 있습니다.

### 데이터 백업

현재 데이터 백업은 WebDAV 방식을 통해서만 지원됩니다. WebDAV를 지원하는 서비스를 선택하여 클라우드 백업을 진행할 수 있습니다.

또는 `A 컴퓨터` $$\xrightarrow{\text{백업}}$$ `WebDAV` $$\xrightarrow{\text{복구}}$$ `B 컴퓨터` 방식으로 여러 기기 간 데이터 동기화를 구현할 수 있습니다.

#### 넛스토어 클라우드(坚果云) 예시

1. 넛스토어 클라우드에 로그인한 후 우측 상단 사용자 이름을 클릭하고 "계정 정보"를 선택합니다:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "보안 설정"을 선택하고 "애플리케이션 추가"를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. 애플리케이션 이름을 입력하고 랜덤 비밀번호를 생성합니다:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. 비밀번호를 복사하여 저장합니다:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. 서버 주소, 계정 및 비밀번호를 획득합니다:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio 설정 → 데이터 설정에서 WebDAV 정보를 입력합니다:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. 데이터 백업 또는 복구를 선택하고 자동 백업 주기를 설정할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
이용이 쉽고 무료 용량이 제공되는 주요 WebDAV 서비스:

* [넛스토어 클라우드(坚果云)](https://www.jianguoyun.com/)
* [123판(123盘)](https://www.123pan.com/) (회원 필요)
* [알리 클라우드 디스크(阿里云盘)](https://www.alipan.com/) (구매 필요)
* [Box](https://www.box.com/) (무료 10GB, 파일 당 250MB 제한)
* [Dropbox](https://www.dropbox.com/) (무료 2GB, 초대 시 최대 16GB 확장 가능)
* [TeraCloud](https://teracloud.jp/en/) (무료 10GB, 초대 시 5GB 추가)
* [Yandex Disk](https://disk.yandex.com/) (무료 10GB 제공)

자가 호스팅 가능한 솔루션:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}