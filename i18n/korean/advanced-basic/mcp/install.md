
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# MCP 환경 설치

**MCP(Model Context Protocol)**는 대규모 언어 모델(LLM)에 표준화된 방식으로 컨텍스트 정보를 제공하기 위한 오픈소스 프로토콜입니다. MCP에 대한 자세한 내용은 [#MCP란 무엇인가](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")에서 확인하세요.

## Cherry Studio에서 MCP 사용하기

`fetch` 기능을 예로 들어 Cherry Studio에서 MCP를 사용하는 방법을 보여드립니다. 자세한 내용은 [문서](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)에서 확인할 수 있습니다.

### **사전 준비: uv, bun 설치**

{% hint style="warning" %}
Cherry Studio는 현재 내장된 [uv](https://github.com/astral-sh/uv)와 [bun](https://github.com/oven-sh/bun)만 사용하며, 시스템에 이미 설치된 uv 및 bun을 **재사용하지 않습니다**.
{% endhint %}

`설정 > MCP 서버`에서 `설치` 버튼을 클릭하면 자동으로 다운로드 및 설치가 진행됩니다. GitHub에서 직접 다운로드하므로 속도가 느리거나 실패할 가능성이 높습니다. 설치 성공 여부는 아래에서 언급된 폴더에 파일이 존재하는지로 확인합니다.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**실행 파일 설치 경로:**

Windows: `C:\Users\사용자명\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_폴더.png" alt=""><figcaption><p>bin 디렉토리</p></figcaption></figure>

**정상 설치가 불가능한 경우:**

시스템에 해당 명령어를 심볼릭 링크로 연결하거나, 해당 디렉토리가 없으면 수동으로 생성할 수 있습니다. 또는 실행 파일을 수동으로 다운로드하여 이 디렉토리에 배치하세요:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)