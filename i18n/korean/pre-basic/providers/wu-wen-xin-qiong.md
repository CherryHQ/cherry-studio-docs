
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 무문심궁

이런 상황을 겪고 계신가요?  
WeChat에 26개의 유용한 글을 저장해 놓고 다시 열어보지 못하고, 컴퓨터에는 "학습 자료" 폴더에 흩어진 10개 이상의 파일이 있으며, 반년 전 읽었던 특정 이론을 찾으려는데 희미한 키워드만 기억나는 상황.  
매일 처리 가능한 정보량을 초과할 때, 소중한 지식의 90%가 72시간 이내에 사라집니다.  
무문심궁 대형모델 서비스 플랫폼 API + Cherry Studio를 활용해 개인 지식베이스를 구축하면, 먼지 쌓인 WeChat 글과 파편화된 강의 콘텐츠를 구조화된 지식으로 전환해 정확하게 활용할 수 있습니다.

### 1. 개인 지식베이스 구축

#### 1. 무문심궁 API 서비스: 지식베이스의 "사고 중추", 안정적이고 편리함

지식베이스의 "사고 중추" 역할을 하는 무문심궁 대형모델 서비스 플랫폼은 DeepSeek R1 최적화 버전 등 모델을 제공하며 안정적인 API 서비스를 지원합니다.  
**현재 가입 후 무료로 사용 가능합니다.**  
주요 임베딩 모델인 bge, jina 모델을 통해 지식베이스를 구축할 수 있으며, **플랫폼은 지속적으로 최신/최강 오픈소스 모델 서비스를 업데이트**합니다.  
이미지, 비디오, 음성 등 다양한 모달리티를 지원합니다.

<figure><img src="../../.gitbook/assets/1280X1280 (1) (1).PNG" alt=""><figcaption></figcaption></figure>

#### 2. Cherry Studio: 코드 없이 지식베이스 구축

Cherry Studio는 사용하기 쉬운 AI 도구로, RAG 지식베이스 개발에 1-2개월이 소요되는 반면 이 도구는 **코드 작성 없이** Markdown/PDF/웹페이지 등 다양한 형식을 한 번에 가져올 수 있습니다.  
40MB 파일을 1분 내로 분석할 수 있으며, PC 로컬 폴더, WeChat 저장소 글 URL, 강의 노트도 추가할 수 있습니다.

### 2. 3단계로 나만의 지식 관리자 만들기

#### Step 1: 기본 준비

1. Cherry Studio 공식 사이트에서 호환 버전 다운로드 (https://cherry-ai.com/)
2. 계정 등록: 무문심궁 대형모델 서비스 플랫폼 로그인 (https://cloud.infini-ai.com/genstudio/model?cherrystudio)

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

* API 키 획득: 「모델 광장」에서 deepseek-r1 선택 → 생성 후 APIKEY 획득, 모델 이름 복사

<figure><img src="../../.gitbook/assets/output (1).png" alt=""><figcaption></figcaption></figure>

#### Step 2: CherryStudio 설정에서 모델 서비스 선택 → 무문심궁 선택 → API 키 입력 후 서비스 활성화

<figure><img src="../../.gitbook/assets/1280X1280 (2) (1).png" alt=""><figcaption></figcaption></figure>

이후 대화 시 필요한 대형모델을 선택하면 CherryStudio에서 무문심궁 API 서비스를 사용할 수 있습니다.  
편의를 위해 「기본 모델」로 설정할 수도 있습니다.

<figure><img src="../../.gitbook/assets/01445ab7-b863-4155-b517-2b6c3c581f47.png" alt=""><figcaption></figcaption></figure>

#### Step 3: 지식베이스 추가

무문심궁 대형모델 서비스 플랫폼의 임베딩 모델(bge 시리즈 또는 jina 시리즈) 중 원하는 버전 선택

<figure><img src="../../.gitbook/assets/1 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/2 (2).png" alt=""><figcaption></figcaption></figure>

### 3. 실제 사용자 시나리오 테스트

* 학습 자료 가져온 후 "머신러닝 3장 핵심 공식 유도 과정 정리" 입력

<figure><img src="../../.gitbook/assets/6bbdbd0d-5db4-4440-b840-3bb3f422b831.gif" alt="《머신러닝》 3장 핵심 공식 유도 정리"><figcaption></figcaption></figure>

**※ 생성 결과 첨부**

<figure><img src="../../.gitbook/assets/3.gif" alt="생성 결과"><figcaption></figcaption></figure>