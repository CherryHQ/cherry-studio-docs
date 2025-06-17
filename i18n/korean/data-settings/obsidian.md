---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# Obsidian 구성 튜토리얼

Cherry Studio는 Obsidian과 연동되어 전체 대화 또는 개별 메시지를 Obsidian 저장소로 내보낼 수 있습니다.

{% hint style="warning" %}
별도의 Obsidian 플러그인 설치가 필요하지 않습니다. 다만 Cherry Studio에서 Obsidian으로 가져오는 방식이 Obsidian Web Clipper와 유사하기 때문에, **[긴 대화 시 가져오기 실패를 방지하기 위해](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0)** Obsidian을 최신 버전(**1.7.2 이상**)으로 업그레이드할 것을 권장합니다.
{% endhint %}

## 신규 튜토리얼

{% hint style="info" %}
이전 버전과 달리, 신규 Obsidian 내보내기 기능은 저장소 경로를 자동으로 선택하며 수동으로 저장소명/폴더명을 입력할 필요가 없습니다.
{% endhint %}

### 1단계: Cherry Studio 설정

Cherry Studio에서 _설정_ → _데이터 설정_ → _Obsidian 설정_ 메뉴로 이동합니다. 열려있는 Obsidian 저장소명이 드롭다운에 자동 표시됩니다. 대상 Obsidian 저장소를 선택하세요:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### 2단계: 대화 내보내기

#### 전체 대화 내보내기

Cherry Studio 대화 인터페이스에서 대화를 우클릭한 후 _내보내기_ → _Obsidian으로 내보내기_를 선택합니다:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

다음 옵션을 설정할 수 있는 팝업 창이 나타납니다:
* **저장소**: 다른 Obsidian 저장소 선택 가능
* **경로**: 내보낼 노트의 저장 폴더 선택
* **Obsidian 노트 속성(Properties)**:
  * 태그(tags)
  * 생성 시간(created)
  * 출처(source)
* **처리 방식** 옵션:
  * **새로 만들기(기존 파일 덮어쓰기)**: 지정된 폴더에 새 노트 생성, 동일한 이름의 노트가 있을 경우 덮어씁니다
  * **앞에 추가**: 기존 노트가 있을 경우 선택한 내용을 노트 시작 부분에 추가
  * **뒤에 추가**: 기존 노트가 있을 경우 선택한 내용을 노트 끝 부분에 추가

{% hint style="info" %}
속성(Properties)은 첫 번째 방식에서만 추가되며, 나머지 두 방식에는 포함되지 않습니다.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>노트 속성 설정</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>경로 선택</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>처리 방식 선택</p></figcaption></figure>

모든 옵션 설정 후 확인을 클릭하면 전체 대화가 해당 Obsidian 저장소의 지정된 폴더로 내보내집니다.

#### 개별 메시지 내보내기

개별 메시지를 내보내려면 메시지 하단의 _세 줄 메뉴_를 클릭한 후 _내보내기_ → _Obsidian으로 내보내기_를 선택합니다:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>개별 메시지 내보내기</p></figcaption></figure>

이후 전체 대화 내보내기와 동일한 설정 창이 나타나며, [상단 튜토리얼](obsidian.md#dao-chu-wan-zheng-dui-hua)과 동일하게 진행하면 됩니다.

### 내보내기 성공

🎉 Cherry Studio와 Obsidian 연동 설정을 완료하고 내보내기 프로세스를 성공적으로 실행했습니다. 즐겨보세요!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidian으로 내보내기</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>내보내기 결과 확인</p></figcaption></figure>

***

## 이전 튜토리얼 (Cherry Studio<v1.1.13용)

### 1단계: Obsidian 준비

Obsidian 저장소를 열고 내보낼 대화를 저장할 `폴더`를 생성합니다(예: Cherry Studio 폴더):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

왼쪽 하단에 표시된 `저장소명`을 기억해 두세요.

### 2단계: Cherry Studio 설정

Cherry Studio에서 _설정_ → _데이터 설정_ → _Obsidian 설정_ 메뉴로 이동합니다. [1단계](obsidian.md#di-yi-bu)에서 확인한 `저장소명`과 `폴더명`을 입력합니다:

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

`전역 태그`는 선택 사항이며, 모든 내보낸 대화에 적용할 Obsidian 태그를 지정할 수 있습니다.

### 3단계: 대화 내보내기

#### 전체 대화 내보내기

Cherry Studio 대화 인터페이스에서 대화를 우클릭한 후 _내보내기_ → _Obsidian으로 내보내기_를 선택합니다.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>전체 대화 내보내기</p></figcaption></figure>

다음 옵션을 설정할 수 있는 팝업 창이 나타납니다:
* **노트 속성(Properties)**
* **처리 방식** 옵션:
  * **새로 만들기(기존 파일 덮어쓰기)**: [2단계](obsidian.md#di-er-bu)에서 지정한 폴더에 새 노트 생성
  * **앞에 추가**: 기존 노트의 시작 부분에 내용 추가
  * **뒤에 추가**: 기존 노트의 끝 부분에 내용 추가

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>노트 속성 설정</p></figcaption></figure>

{% hint style="info" %}
속성(Properties)은 첫 번째 방식에서만 추가됩니다.
{% endhint %}

#### 개별 메시지 내보내기

메시지 하단의 _세 줄 메뉴_를 클릭한 후 _내보내기_ → _Obsidian으로 내보내기_를 선택합니다.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>개별 메시지 내보내기</p></figcaption></figure>

이후 [상단 튜토리얼](obsidian.md#dao-chu-wan-zheng-dui-hua)과 동일하게 진행하면 됩니다.

### 내보내기 성공

🎉 Cherry Studio와 Obsidian 연동 설정을 완료하고 내보내기 프로세스를 성공적으로 실행했습니다. 즐겨보세요!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidian으로 내보내기</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>내보내기 결과 확인</p></figcaption></figure>