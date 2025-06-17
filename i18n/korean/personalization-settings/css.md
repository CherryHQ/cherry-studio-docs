---
icon: file-code
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 사용자 정의 CSS

사용자 정의 CSS를 통해 소프트웨어의 외관을 자신의 취향에 맞게 수정할 수 있습니다. 예를 들어 다음과 같습니다:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>사용자 정의 CSS</p></figcaption></figure>

```css
:root {
  --color-background: #1a462788;
  --color-background-soft: #1a4627aa;
  --color-background-mute: #1a462766;
  --navbar-background: #1a4627;
  --chat-background: #1a4627;
  --chat-background-user: #28b561;
  --chat-background-assistant: #1a462722;
}

#content-container {
  background-color: #2e5d3a !important;
}
```

### 내장 변수

```css
:root {
  font-family: "汉仪唐美人" !important; /* 글꼴 */
}

/* 심층 사고 확장 글자 색상 */
.ant-collapse-content-box .markdown {
  color: red;
}

/* 테마 변수 */
:root {
  --color-black-soft: #2a2b2a; /* 다크 배경색 */
  --color-white-soft: #f8f7f2; /* 라이트 배경색 */
}

/* 다크 테마 */
body[theme-mode="dark"] {
  /* 색상 */
  --color-background: #2b2b2b; /* 다크 배경색 */
  --color-background-soft: #303030; /* 중간톤 배경색 */
  --color-background-mute: #282c34; /* 중성 배경색 */
  --navbar-background: var(-–color-black-soft); /* 내비게이션 바 배경색 */
  --chat-background: var(–-color-black-soft); /* 채팅 배경색 */
  --chat-background-user: #323332; /* 사용자 채팅 배경색 */
  --chat-background-assistant: #2d2e2d; /* 어시스턴트 채팅 배경색 */
}

/* 다크 테마 특정 스타일 */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* 콘텐츠 컨테이너 배경색 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* 메시지 배경색 */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* 입력창 배경색 */
    border: 1px solid #5e5d5940; /* 입력창 테두리 색상 */
    border-radius: 8px; /* 입력창 테두리 둥근 모서리 */
  }

  /* 코드 스타일 */
  code {
    background-color: #e5e5e20d; /* 코드 배경색 */
    color: #ea928a; /* 코드 텍스트 색상 */
  }

  pre code {
    color: #abb2bf; /* 미리 서식된 코드 텍스트 색상 */
  }
}

/* 라이트 테마 */
body[theme-mode="light"] {
  /* 색상 */
  --color-white: #ffffff; /* 흰색 */
  --color-background: #ebe8e2; /* 라이트 배경색 */
  --color-background-soft: #cbc7be; /* 중간톤 배경색 */
  --color-background-mute: #e4e1d7; /* 중성 배경색  */
  --navbar-background: var(-–color-white-soft); /* 내비게이션 바 배경색 */
  --chat-background: var(-–color-white-soft); /* 채팅 배경색 */
  --chat-background-user: #f8f7f2; /* 사용자 채팅 배경색 */
  --chat-background-assistant: #f6f4ec; /* 어시스턴트 채팅 배경색 */
}

/* 라이트 테마 특정 스타일 */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* 콘텐츠 컨테이너 배경색 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* 메시지 배경색 */
  }

  .inputbar-container {
    background-color: #ffffff; /* 입력창 배경색 */
    border: 1px solid #87867f40; /* 입력창 테두리 색상 */
    border-radius: 8px; /* 입력창 테두리 둥근 모서리 */
  }

  /* 코드 스타일 */
  code {
    background-color: #3d39290d; /* 코드 배경색 */
    color: #7c1b13; /* 코드 텍스트 색상 */
  }

  pre code {
    color: #000000; /* 미리 서식된 코드 텍스트 색상 */
  }
}
```

더 많은 테마 변수는 소스 코드를 참조하세요: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### 관련 추천

Cherry Studio 테마 라이브러리: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

중국 풍 Cherry Studio 테마 스킨 공유: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)