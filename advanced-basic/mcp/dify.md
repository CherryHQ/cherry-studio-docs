# 配置 Dify 知识库

[Dify](https://dify.ai/) 是一个企业级 AI 应用平台，里面也内置了知识库功能。如果你已经在 Dify 上建好了知识库（公司用 Dify 维护内部资料、或个人用 Dify 试做 RAG 应用），本页教你**让 Cherry Studio 里的 AI 直接查询 Dify 知识库**。

简单说：**你不必把资料从 Dify 搬到 Cherry Studio，Cherry Studio 里的对话就能查到 Dify 那边的内容**。

要求：Cherry Studio v1.2.9 或更高版本；已在 Dify 中创建好至少一个知识库并拿到该知识库的 API Key。

### 添加 Dify 知识库 MCP 服务器

<figure><img src="../../.gitbook/assets/CleanShot 2025-04-27 at 10.36.29@2x.jpg" alt=""><figcaption></figcaption></figure>

1. 打开 `搜索MCP`。
2. 添加 `dify-knowledge` 服务器。

### 配置 Dify 知识库

<figure><img src="../../.gitbook/assets/CleanShot 2025-04-27 at 10.36.05@2x.jpg" alt=""><figcaption></figcaption></figure>

> 需要配置参数和环境变量

1. Dify知识库key可以通过以下方式获取

<figure><img src="../../.gitbook/assets/CleanShot 2025-04-27 at 10.46.16@2x.jpg" alt=""><figcaption></figcaption></figure>

### 使用Dify知识库mcp

<figure><img src="../../.gitbook/assets/CleanShot 2025-04-27 at 10.26.24@2x.jpg" alt=""><figcaption></figcaption></figure>
