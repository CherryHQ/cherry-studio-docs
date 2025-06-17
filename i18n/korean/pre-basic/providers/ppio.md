
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# PPIO 파이오 클라우드

## Cherry Studio PPIO LLM API 연동 가이드

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)튜토리얼 개요 <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio는 멀티모델 데스크톱 클라이언트로 현재 Windows, Linux, MacOS 시스템을 지원합니다. 주요 LLM 모델을 통합하여 다양한 시나리오에서 사용자를 지원하며, 지능형 대화 관리, 오픈소스 커스터마이징, 다중 테마 인터페이스를 통해 작업 효율성을 높입니다.

Cherry Studio는 이제 **PPIO 고성능 API 채널**과 완벽하게 호환됩니다. 엔터프라이즈급 컴퓨팅 파워로 **DeepSeek-R1/V3 초고속 응답** 및 **99.9% 서비스 가용성**을 보장하여 원활한 경험을 제공합니다.

아래 가이드에 포함된 전체 연동 솔루션(API 키 설정 포함)을 따라 3분 만에 "Cherry Studio 지능형 스케줄링 + PPIO 고성능 API"의 고급 모드를 시작하세요.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. CherryStudio에서 "PPIO" 모델 공급자 추가 <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

공식 웹사이트에서 Cherry Studio 다운로드: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (접속 어려울 경우 아래 Quark 웹디스크 링크에서 버전 선택): [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share)

(1) 좌측 하단 설정 클릭 → 공급자 이름을 `PPIO`로 지정 → "확인" 클릭

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) [파이오 컴퓨팅 클라우드 API 키 관리](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio) 접속 → 【사용자 아바타】-【API 키 관리】선택

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

【+ 생성】버튼 클릭 후 새 API 키 이름 지정. **생성된 키는 발급 시점에만 표시되므로 반드시 복사 후 문서에 저장해주세요(향후 사용에 영향)**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) CherryStudio에서 키 입력 → 【PPIO 파이오 클라우드】선택 → 공식 웹사이트에서 생성한 API 키 입력 → 【확인】클릭

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) 모델 선택: deepseek/deepseek-r1/community 예시. 다른 모델로 변경 필요 시 직접 교체 가능

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1/V3 커뮤니티 버전은 체험용으로 전체 파라미터 풀버전 모델이며 안정성과 성능은 동일합니다. 대량 호출 필요 시 **충전 후 non-community 버전으로 전환**해야 합니다.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. 모델 사용 설정 <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) 【확인】클릭 후 연결 성공 표시 시 정상 사용 가능

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) 【@】클릭 → PPIO 공급자 하위에 추가된 DeepSeek R1 모델 선택 → 채팅 시작!

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【일부 자료 출처: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. PPIO×Cherry Studio 동영상 사용 가이드 <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

시각적 학습을 선호하시는 경우 Bilibili에 준비한 동영상 튜토리얼을 참고하세요. 단계별 안내로 "PPIO API+Cherry Studio" 설정 방법을 빠르게 익히고 원활한 개발 경험을 시작해보세요 → [《[DeepSeek 로딩 속도에 답답하신가요?] 파이오 클라우드+DeepSeek 풀버전=?
더 이상의 지체 없이 즉시 시작하세요》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【영상 출처: sola】