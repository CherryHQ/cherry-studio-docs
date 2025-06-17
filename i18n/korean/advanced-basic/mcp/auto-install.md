
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 자동 설치 MCP

> MCP 자동 설치를 위해서는 Cherry Studio를 v1.1.18 이상 버전으로 업그레이드해야 합니다.

## 기능 소개

수동 설치 외에도 Cherry Studio는 `@mcpmarket/mcp-auto-install` 도구를 내장하고 있어 더 편리한 MCP 서버 설치 방식을 제공합니다. MCP 서비스를 지원하는 대규모 모델 대화창에서 해당 명령어를 입력하기만 하면 됩니다.

{% hint style="warning" %}
**테스트 단계 안내:**

* `@mcpmarket/mcp-auto-install`은 현재 테스트 단계에 있음
* 효과는 대형 모델의 "지능"에 따라 달라짐 (일부는 자동 적용, 일부는 **MCP 설정에서 매개변수 수동 조정 필요**)
* 현재 검색 소스는 @modelcontextprotocol에서 진행되며 사용자 정의 설정 가능 (아래 설명 참조)
{% endhint %}

## 사용 방법

예를 들어 다음과 같이 입력할 수 있습니다:

```
파일시스템 MCP 서버를 설치해 줘
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCP 서버 설치 명령 입력</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP 서버 설정 화면</p></figcaption></figure>

시스템이 자동으로 요구사항을 인식하고 `@mcpmarket/mcp-auto-install`을 통해 설치를 완료합니다. 이 도구는 다음과 같은 다양한 유형의 MCP 서버를 지원합니다:

* filesystem (파일 시스템)
* fetch (네트워크 요청)
* sqlite (데이터베이스)
* 기타...

> MCP_PACKAGE_SCOPES 변수로 MCP 서비스 검색 소스를 사용자 정의할 수 있으며, 기본값은 `@modelcontextprotocol`입니다.

## `@mcpmarket/mcp-auto-install` 라이브러리 소개

{% hint style="info" %}
**기본 구성 참조:**

```json
// `axun-uUpaWEdMEMU8C61K`는 서비스 ID로 사용자 정의 가능
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "MCP 서비스 자동 설치 (베타 버전)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "자세한 내용은 https://www.npmjs.com/package/@mcpmarket/mcp-auto-install 참조"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install`은 오픈소스 npm 패키지이며, [npm 공식 저장소](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install)에서 상세 정보와 사용 문서를 확인할 수 있습니다. `@mcpmarket`는 Cherry Studio 공식 MCP 서비스 컬렉션입니다.
{% endhint %}