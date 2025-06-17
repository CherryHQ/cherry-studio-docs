
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# MCP 구성 및 사용

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Cherry Studio 설정을 엽니다.
2. `MCP 서버` 옵션을 찾습니다.
3. `서버 추가`를 클릭합니다.
4. MCP Server 관련 파라미터를 입력합니다([참고 링크](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). 입력해야 할 내용은 다음과 같습니다:
   * 이름: 예시 `fetch-server`처럼 사용자 정의
   * 유형: `STDIO` 선택
   * 명령어: `uvx` 입력
   * 파라미터: `mcp-server-fetch` 입력
   * (특정 서버에 따라 추가 파라미터가 있을 수 있음)
5. `저장`을 클릭합니다.

{% hint style="success" %}
위 설정을 완료하면 Cherry Studio가 필요한 MCP Server(`fetch server`)를 자동으로 다운로드합니다. 다운로드 완료 후 사용을 시작할 수 있습니다! 참고: mcp-server-fetch 구성에 실패할 경우 컴퓨터를 재시작해 보세요.
{% endhint %}

### 채팅창에서 MCP 서비스 활성화

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt="MCP 입력 상자 버튼 예시"><figcaption></figcaption></figure>

* `MCP 서버` 설정에서 MCP 서버를 성공적으로 추가한 경우

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt="MCP 서버 예시"><figcaption></figcaption></figure>

### **사용 효과 데모**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

위 이미지에서 확인할 수 있듯이, MCP의 `fetch` 기능을 결합한 Cherry Studio는 사용자 질의 의도를 더 잘 이해하고 웹에서 관련 정보를 수집하여 더 정확하고 포괄적인 답변을 제공할 수 있습니다.