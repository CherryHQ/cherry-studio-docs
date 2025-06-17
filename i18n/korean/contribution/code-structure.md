---
hidden: True
icon: code
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 코드 구조

```yaml
...
├─ docs/ # 문서 디렉토리
├─ resources/ # 리소스 파일 디렉토리
├─ scripts/ # 스크립트 파일 디렉토리
└─ src/ # 주요 소스 코드 디렉토리
    ├─main/ # 메인 프로세스 코드
    ├─preload/ # 프리로드 스크립트 디렉토리
    └─renderer/ # 렌더링 프로세스 코드
        ├─src/ # 렌더링 프로세스의 소스 코드
            ├─assets/ # 리소스 파일
                ├─fonts/ # 폰트 파일
                ├─images/ # 아바타 등의 이미지 파일
                └─styles/ # 스타일 파일
            ├─components/ # 컴포넌트
            ├─config/ # 설정 파일
            ├─context/ # 컨텍스트
            ├─databases/ # 데이터베이스 관련 파일
            ├─hooks/ # 커스텀 훅
            ├─i18n/ # 국제화 파일
            ├─pages/ # 페이지 파일
            ├─providers/ # 서비스 제공자 관련 설정
            ├─services/ # 서비스 파일
            ├─store/ # 상태 관리 파일
            ├─types/ # TypeScript 타입 정의 파일
            ├─utils/ # 유틸리티 함수
            ...
        ...
    ...
...
```