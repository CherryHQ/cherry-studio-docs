---
icon: hexagon-exclamation
---

# MCP 常见问题

本页用于排查 MCP Server 无法启动、连接后没有工具、调用超时或参数错误等问题。第一次配置 MCP 时，建议先阅读 [配置和使用 MCP](config.md)；如果系统缺少运行环境，请先完成 [MCP 环境安装](install.md)。

## 先确定连接类型

打开 `设置 → MCP 服务器`，进入出现问题的 Server，先确认类型和必填项匹配：

| 类型 | 必填配置 | 常见问题 |
|---|---|---|
| `stdio` | Command、Arguments，按需填写环境变量 | 命令不存在、参数拆分错误、依赖未安装 |
| `SSE` | Server URL，按需填写 Headers | URL 路径错误、服务未运行、认证失败 |
| `Streamable HTTP` | Server URL，按需填写 Headers | 把 SSE 地址误填为 `/mcp`，或反之 |
| 内置 | 按页面说明配置 | 缺少授权、目录或搜索密钥 |

`stdio` 会由 Cherry Studio 启动本地子进程；SSE 和 Streamable HTTP 则连接已经运行的远程或本地服务。排错方法不同，不要只替换 URL 或 Command 后反复重试。

## 查看实时日志

进入 Server 详情，点击标题旁的 **查看日志**。日志会显示：

* `stdout` / `stderr`：本地命令的输出；
* `info` / `warn` / `error`：连接、初始化和调用状态；
* 最近的启动参数、连接错误或工具返回信息。

建议先关闭 Server，再打开日志并重新启用，这样更容易找到第一条错误。日志最多保留页面当前会话中的最近记录，复现后及时复制必要部分。

{% hint style="warning" %}
日志可能包含命令参数、文件路径、请求地址或工具返回内容。提交反馈前先遮盖 Token、API Key、Cookie、个人目录和业务数据。
{% endhint %}

## Server 无法启用

### `npx`、`uvx` 或其他命令不存在

Cherry Studio 会读取登录 Shell 的环境变量来查找命令。对于 `npx`，应用还会尝试使用内置 Bun；对于 `uv` / `uvx`，会尝试使用已安装的内置版本。

如果仍提示 `not found`：

1. 打开 `设置 → MCP 服务器 → 环境安装`。
2. 安装 Server 所需的 Node.js 或 `uv` 运行环境。
3. 完全退出并重新打开 Cherry Studio，让新的 PATH 生效。
4. 回到 Server 详情，重新启用。

也可以在终端验证：

```bash
node --version
npx --version
uvx --version
```

只需要验证该 Server 实际使用的命令，不必安装所有环境。

### Command 和 Arguments 填写错误

在 Cherry Studio 中：

* **Command** 只填写可执行命令，例如 `npx`、`uvx` 或可执行文件绝对路径；
* **Arguments** 每行填写一个独立参数；
* 不要把完整命令复制到 Command 一栏；
* 带空格的文件路径作为一个完整参数填写，不要自行加入 Shell 引号，除非 Server 文档明确要求。

例如，下面的 JSON：

```json
{
  "command": "npx",
  "args": ["-y", "@example/mcp-server", "--mode", "read-only"]
}
```

在表单中应填写：

```text
Command
npx

Arguments
-y
@example/mcp-server
--mode
read-only
```

### JSON 导入失败

从 JSON 添加时，最外层应包含 `mcpServers`，且一次只导入一个 Server：

```json
{
  "mcpServers": {
    "example": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"]
    }
  }
}
```

常见原因包括：

* 使用了中文引号或多余逗号；
* `args` 不是字符串数组；
* 同一个 JSON 中包含多个 Server；
* 把 `url`、`command` 和类型混合为不兼容配置；
* 复制内容中包含 Markdown 代码围栏。

## 远程 Server 无法连接

### URL 或协议不匹配

确认 Server 官方文档提供的是 SSE 还是 Streamable HTTP：

* SSE 常见地址类似 `http://localhost:3000/sse`；
* Streamable HTTP 常见地址类似 `http://localhost:3000/mcp`。

路径由 Server 自己决定，`/sse` 和 `/mcp` 只是常见形式。先在终端或浏览器确认服务确实监听该地址，再选择相应类型。

如果 Server 运行在 Docker、虚拟机或另一台设备中，`127.0.0.1` 指向的是 Cherry Studio 所在系统，不一定是 Server 所在主机。

### 返回 401 或 403

在 **Headers** 中按每行 `名称=值` 的格式填写认证信息，例如：

```text
Authorization=Bearer YOUR_TOKEN
```

不要把真实 Token 写进可公开分享的配置。修改 Headers 后保存；已启用的 Server 会尝试按新配置重新连接，失败时会自动回到停用状态。

## 已连接，但看不到工具

依次检查：

1. Server 在 `设置 → MCP 服务器` 中已启用。
2. Server 详情的 **工具** 标签是否列出工具。
3. 对应工具没有在列表中被单独关闭。
4. 当前助手或 Agent 已启用该 MCP Server。
5. 开始一个新对话，让新的工具配置进入上下文。

“Server 已连接”只表示协议初始化成功，不代表每个助手都会自动获得它的工具。

如果工具列表为空，但 Server 文档声称提供工具，查看日志中是否出现 `listTools`、协议版本或初始化错误。

## 工具调用超时

Cherry Studio 的默认工具调用超时是 60 秒。Server 详情中的 **Timeout** 可以按秒提高；开启长任务支持后，Server 发送进度事件时可延长等待，但总时间仍有限制。

连接初始化使用更宽松的等待时间，首次下载依赖或启动远程 Server 可能需要数分钟。请区分：

* **启用时超时**：通常是安装、网络、URL 或初始化问题；
* **工具执行时超时**：通常是 Server 任务本身太慢，或没有发送进度。

不要无限提高 Timeout。先在日志中确认请求确实在推进，并检查 Server 是否支持 MCP Progress。

## 环境变量没有生效

Server 的环境变量应按每行 `KEY=VALUE` 填写。Cherry Studio 会把它们与登录 Shell 环境合并后传给 `stdio` 子进程。

检查：

* 键名是否与 Server 文档完全一致；
* 值中是否意外包含引号或首尾空格；
* 修改后是否保存并重新连接；
* Token 是否已经过期；
* Server 是否实际从环境变量读取，而不是要求 Header 或配置文件。

对于远程 SSE / Streamable HTTP Server，认证通常应放在 Headers，而不是本地进程环境变量。

## `mcp-server-time` 时区错误

官方 Time Server 是 Python Server，通常通过 `uvx` 启动。若需要指定本地时区，可按独立参数填写：

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": [
        "mcp-server-time",
        "--local-timezone=Asia/Shanghai"
      ]
    }
  }
}
```

时区应使用 IANA 名称，例如 `Asia/Shanghai`、`Europe/Berlin` 或 `America/New_York`，不要填写 `UTC+8` 这类偏移缩写。

如果提示 `uvx not found`，先安装 MCP 的 Python 环境并重启 Cherry Studio。Time Server 的安装方式或参数可能随版本变化，最终以 [官方 MCP Servers 仓库](https://github.com/modelcontextprotocol/servers/tree/main/src/time) 为准。

## 最小化复现问题

如果仍无法解决：

1. 新建一个只包含必要字段的 Server 配置。
2. 暂时移除代理、自定义镜像和非必要环境变量。
3. 在空白助手中只启用这个 MCP Server。
4. 调用一个最简单、无副作用的工具。
5. 保存错误弹窗和 **查看日志** 中对应时间段的信息。

提交反馈时附上 Cherry Studio 版本、操作系统、Server 类型、脱敏配置和脱敏日志。不要附真实凭据。官方渠道见 [反馈与建议](../../question-contact/suggestions.md)。
