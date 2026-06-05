# 内置 MCP 配置

Cherry Studio **预装了若干常用 MCP**，无需手动安装即可在 `设置 → MCP 服务器` 中启用。下面是当前内置清单，**新版本可能调整**，请以应用内实际显示为准。

> 想自己装其他 MCP？看 [配置和使用 MCP](config.md)。

### 通用工具

#### `@cherry/fetch`

用于获取 URL 网页内容的 MCP 服务器。日常给 AI"看一下某个网页"的首选。

#### `@cherry/browser`

通过 Chrome DevTools 协议控制隐藏的 Electron 窗口，支持打开 URL、执行单行 JS、重置会话。适合需要让 AI 操作真实浏览器、读取动态网页的场景。

#### `@cherry/filesystem`

实现文件系统操作的 Node.js MCP 服务器，让 AI 能读取、创建、修改本地文件。**必须配置允许访问的目录**，否则无法启动：

```text
WORKSPACE_ROOT=/Users/yourname/your-project-dir
```

如果不配置环境变量，需要在对话中手动指定路径。

#### `@cherry/python`

在 Pyodide 沙盒中执行 Python 代码，支持多数标准库与科学计算包。让 AI"自己跑一段 Python"做数据分析、画图、转换格式都很合适。

#### `@cherry/brave_search`

集成 [Brave Search API](https://brave.com/search/api/) 的搜索工具，提供网页与本地搜索双重功能。需要先到 Brave 申请 API Key 并配置环境变量：

```text
BRAVE_API_KEY=你的_brave_api_key
```

### 记忆类

#### `@cherry/memory`

基于本地知识图谱的持久性记忆基础实现，让模型在不同对话间记住用户的相关信息。需要配置 `MEMORY_FILE_PATH` 环境变量：

```text
MEMORY_FILE_PATH=/path/to/memory.json
```

> 注：这是 MCP 形式的记忆。**Cherry Studio 的 [全局记忆](../memory.md)** 是更上层的功能，二者可叠加，但通常用其中之一即可。

#### `@cherry/nowledge_mem`

接入 [Nowledge Mem](https://mem.nowledge.co/) 应用，把对话、工具、笔记、智能体和文件都保存在本地的私有记忆系统中。需要先在本机安装 Nowledge Mem。

### 思维 / 框架

#### `@cherry/sequentialthinking`

提供"结构化思维过程"工具，让 AI 在解决复杂问题时一步步推理，并在推理过程中可以回溯、反思。适合复杂逻辑任务。

#### `@cherry/mcp-auto-install`

让 AI 在对话中自动搜索并安装其他 MCP（测试版）。详见 [自动安装 MCP](auto-install.md)。

### 国内服务集成

#### `@cherry/dify_knowledge`

通过 Dify 平台访问知识库。详见 [配置 Dify 知识库](dify.md)。

#### `@cherry/flomo`

连接 flomo 笔记，让 AI 帮你快速记录想法。需要 flomo 账号授权。

#### `@cherry/didi_mcp`

集成滴滴出行：地图搜索、价格预估、订单管理、司机跟踪等能力。**仅支持中国大陆地区**，需要配置 `DIDI_API_KEY` 环境变量。

### 总结

| 适用场景 | 推荐内置 MCP |
|---|---|
| 想让 AI 读网页 | `@cherry/fetch` 或 `@cherry/browser` |
| 想让 AI 搜网络（结构化结果）| `@cherry/brave_search` |
| 想让 AI 处理本地文件 | `@cherry/filesystem` |
| 想让 AI 跑 Python 代码 | `@cherry/python` |
| 想让 AI 接 Dify 知识库 | `@cherry/dify_knowledge` |
| 想让 AI 持久记忆 | 优先用上层的 [全局记忆](../memory.md)，需高级控制再用 `@cherry/memory` |
| 让 AI 帮你安装其他 MCP | `@cherry/mcp-auto-install` |

启用方法都一样：在 `设置 → MCP 服务器` 中找到对应条目，按提示填入环境变量，点击启用即可。
