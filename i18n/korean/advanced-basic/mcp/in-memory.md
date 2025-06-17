
{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 내장형 MCP 구성

### @cherry/mcp-auto-install

MCP 서비스 자동 설치 (베타 버전)

### @cherry/memory

로컬 지식 그래프 기반 영구 메모리 기본 구현체. 이 기능을 통해 모델은 대화 간에 사용자 관련 정보를 기억할 수 있습니다.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

구조화된 사고 프로세스를 통해 동적이고 반성적인 문제 해결을 지원하는 MCP 서버 구현체.

### @cherry/brave-search

Brave 검색 API를 통합한 MCP 서버 구현체로, 웹 및 로컬 검색의 이중 기능을 제공합니다.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

URL 웹 페이지 콘텐츠를 가져오기 위한 MCP 서버.

### @cherry/filesystem

파일 시스템 조작을 위한 모델 컨텍스트 프로토콜(MCP) Node.js 서버 구현체.