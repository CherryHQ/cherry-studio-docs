---
icon: database
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 데이터 설정

이 인터페이스에서는 클라이언트 데이터의 클라우드 및 로컬 백업, 로컬 데이터 디렉토리 조회, 캐시 지우기 등의 작업을 수행할 수 있습니다.

### 데이터 백업

현재 데이터 백업은 WebDAV 방식만 지원합니다. WebDAV를 지원하는 서비스를 선택하여 클라우드 백업을 할 수 있습니다.

또한 `A 컴퓨터` $$\xrightarrow{\text{백업}}$$ `WebDAV` $$\xrightarrow{\text{복구}}$$ `B 컴퓨터` 방식으로 멀티 디바이스 간 데이터 동기화를 구현할 수 있습니다.

#### 坚果云을 예시로

1. 坚果云에 로그인하고 오른쪽 상단 사용자 이름을 클릭하여 "계정 정보" 선택:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "보안 설정" 선택 후 "앱 추가" 클릭:

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. 응용 프로그램 이름 입력 후 임시 비밀번호 생성:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. 비밀번호 복사하여 저장:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. 서버 주소, 계정 및 비밀번호 획득:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio 설정 > 데이터 설정에서 WebDAV 정보 입력:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. 데이터 백업 또는 복구 선택, 자동 백업 주기 설정 가능:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV 서비스 접근성이 높은 클라우드 스토리지:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (멤버십 필요)
* [阿里云盘](https://www.alipan.com/) (구매 필요)
* [Box](https://www.box.com/) (무료 공간 10GB, 파일당 최대 250MB 제한)
* [Dropbox](https://www.dropbox.com/) (무료 2GB, 초대 시 최대 16GB 확장)
* [TeraCloud](https://teracloud.jp/en/) (무료 10GB, 초대 시 5GB 추가 확장)
* [Yandex Disk](https://disk.yandex.com/) (무료 사용자 10GB 제공)

자체 배포 필요 서비스:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}