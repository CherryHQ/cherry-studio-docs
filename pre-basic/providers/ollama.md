---
icon: server
---

# Ollama

Ollama 可以在 macOS、Windows 和 Linux 上运行本地模型，也可以通过 Ollama Cloud 调用云端模型。Cherry Studio V2 使用 Ollama 原生 Chat API，并从 `/api/tags` 同步当前实例可见的模型。

本地运行时，模型推理和对话请求默认在你的设备上完成；如果选择 Cloud 模型、Ollama 云端 API 或联网能力，请求仍会离开本机。

{% hint style="info" %}
在 Cherry Studio 中点击**添加**或同步模型，只会读取 Ollama 已有模型列表，不会下载模型权重。请先在 Ollama 中拉取模型，再回到 Cherry Studio 同步。
{% endhint %}

## 选择使用方式

| 方式 | Base URL | API Key |
| --- | --- | --- |
| 同一台电脑上的 Ollama | `http://localhost:11434` | 留空 |
| 局域网或远程自建 Ollama | 服务器实际地址 | 取决于反向代理 |
| Ollama Cloud 直连 | `https://ollama.com` | Ollama API Key |
| 本地 Ollama 代理 Cloud 模型 | `http://localhost:11434` | 本地登录后通常留空 |

本地 API 默认不需要身份验证。Cherry Studio 在 API Key 非空时会发送 `Authorization: Bearer ...`，可用于 Ollama Cloud 或配置了 Bearer 鉴权的反向代理。

## 安装 Ollama

前往 [Ollama 官网](https://ollama.com/)下载对应系统版本并完成安装。

Linux 也可以使用官方安装脚本：

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

安装后确认服务正在运行：

```bash
ollama list
```

如果命令能够返回模型列表，说明 Ollama CLI 与本地服务基本可用。

## 拉取模型

从 [Ollama 模型库](https://ollama.com/library)选择模型和标签，然后运行：

```bash
ollama pull <model>:<tag>
```

例如：

```bash
ollama pull gemma3
```

常用管理命令：

```bash
ollama list
ollama ps
ollama stop <model>
ollama rm <model>:<tag>
```

- `ollama list`：查看已经拉取的模型；
- `ollama ps`：查看当前已加载模型及 CPU/GPU 占用；
- `ollama stop`：从内存或显存卸载模型；
- `ollama rm`：删除本地模型文件。

模型标签会影响参数规模、量化方式、上下文和磁盘占用。不要只看模型系列名称，应根据内存、显存和任务选择具体标签。

## 在 Cherry Studio 配置

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **Ollama**；
4. 本机使用时保留 Base URL `http://localhost:11434`；
5. 本地服务的 API Key 留空；
6. 打开页面顶部的服务商开关；
7. 点击**添加**读取 Ollama 模型列表；
8. 检查同步预览并应用变更；
9. 只启用准备使用的模型。

Cherry Studio 会把 `http://localhost:11434`、带 `/v1` 的地址或带 `/api` 的地址规范化为 Ollama 原生 `/api` 路径。为减少混淆，建议填写不带具体接口的主机地址。

如果刚拉取的模型没有出现，先确认 `ollama list` 能看到完全相同的标签，再重新点击**添加**。

## API Key 与 Cloud 模型

### 通过本地 Ollama 使用 Cloud 模型

先在 Ollama 中登录：

```bash
ollama signin
```

然后按官方说明拉取或运行带 `:cloud` 的模型。Cherry Studio 仍连接 `http://localhost:11434`，本地 Ollama 负责云端鉴权。

### 直接连接 Ollama Cloud

1. 在 Ollama 账户中创建 API Key；
2. 将 Base URL 改为 `https://ollama.com`；
3. 在 API Key 中填入该密钥；
4. 同步云端可用模型；
5. 运行连接和模型健康检查。

{% hint style="warning" %}
API Key 不应写入聊天消息、文档、代码仓库或问题截图。Cloud Key 泄露后应立即在 Ollama 账户中撤销并重新创建。
{% endhint %}

本地模型不会自动变成云端模型。确认模型标签和当前连接的 Ollama 主机，避免误判数据实际处理位置。

## 选择对话、视觉与工具模型

Ollama 模型能力由模型本身和标签决定，Cherry Studio 会根据模型 ID 识别常见能力。

### 普通对话

任何支持 Ollama Chat API 的生成模型都可以用于基本对话。首次请求需要加载权重，响应可能明显慢于后续请求。

### 视觉理解

选择 Ollama 模型库中明确标记支持 Vision 的模型。同步后检查 Cherry Studio 是否显示图片能力，再上传一张小图片测试。

- 模型名称相似不代表都支持图片；
- 不同标签可能具有不同能力；
- 图片会增加上下文和内存占用；
- 模型 ID 未被自动识别时，不要仅修改显示名称伪装能力。

### 工具调用与 MCP

模型必须原生支持 Tool Calling，Cherry Studio 才能稳定使用 MCP。

1. 选择模型库中明确支持工具调用的模型；
2. 先完成普通对话；
3. 只启用一个简单 MCP 工具；
4. 明确要求模型调用工具；
5. 确认模型实际发起调用；
6. 再增加更多工具。

部分小模型会输出“打算调用工具”的文字，却不会生成结构化调用。遇到这种情况应更换工具能力更强的模型，而不是反复增加提示词。

## 设置思考模式

Ollama Chat API 使用 `think` 参数控制思考：

- 对支持 GPT-OSS 分级推理的模型，Cherry Studio 可发送低、中、高；
- 其他支持思考的模型通常只接受开启或关闭；
- 选择**关闭**时发送 `think: false`；
- 使用默认或开启时，实际行为仍取决于模型。

如果模型不支持 `think` 却返回参数错误，关闭思考或改用正确的模型标签。不要把一个模型的思考选项直接套用到所有本地模型。

## 上下文与硬件占用

Ollama 的实际上下文由模型、服务器设置和可用内存决定。更长上下文会显著增加 RAM 或 VRAM 占用。

可在启动 Ollama 时设置默认上下文：

```bash
OLLAMA_CONTEXT_LENGTH=8192 ollama serve
```

查看模型是否在 GPU 上运行：

```bash
ollama ps
```

`PROCESSOR` 列会显示 CPU、GPU 或混合加载比例。

当 Cherry Studio 中填写的模型上下文大于 Ollama 实际配置时，服务器仍可能截断输入或返回超限。应以 Ollama 运行时配置和日志为准。

## 模型加载与并发

Ollama 默认会在空闲后卸载模型以释放资源。需要调整时，可使用 Ollama 的 `OLLAMA_KEEP_ALIVE`、`OLLAMA_MAX_LOADED_MODELS`、`OLLAMA_NUM_PARALLEL` 和 `OLLAMA_MAX_QUEUE`。

- 保持模型常驻可减少首条回复等待，但持续占用内存或显存；
- 并行数越高，每个模型需要的上下文内存越多；
- 多个大模型同时加载可能触发排队或卸载；
- 队列满时服务器可能返回 503。

不要只提高并发参数。先用 `ollama ps` 和系统监控确认硬件余量。

## 知识库与嵌入模型

Ollama 可以提供本地嵌入模型，用于知识库和[全局记忆](../../advanced-basic/memory.md)。

1. 从模型库拉取专用嵌入模型；
2. 回到 Cherry Studio 同步模型；
3. 确认模型被识别为嵌入模型；
4. 在知识库中选择它；
5. 检测维度并运行健康检查；
6. 再导入文档。

Ollama 在 Cherry Studio 中不支持重排序模型。需要 Rerank 时选择其他服务商。

嵌入模型一旦用于现有知识库，不应随意更换模型或维度；否则通常需要重新构建向量索引。

## PDF 与附件

当前 V2 不把 PDF 直接发送给 Ollama。Cherry Studio 会先在本地提取 PDF 文本，再交给模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用模型上下文；
- PDF 中的图片需要单独发送给视觉模型。

## 连接远程 Ollama

Ollama 默认只监听 `127.0.0.1:11434`。要让其他设备上的 Cherry Studio 连接，需在 Ollama 主机设置监听地址，例如：

```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

不同系统设置环境变量和重启服务的方式不同，请参考 [Ollama FAQ](https://docs.ollama.com/faq)。

{% hint style="danger" %}
不要把未鉴权的 Ollama 端口直接暴露到公网。局域网也应配合防火墙；公网访问应使用 VPN 或带 HTTPS 与鉴权的反向代理。
{% endhint %}

连接 Docker、虚拟机或 WSL 中的 Ollama 时，`localhost` 指向 Cherry Studio 所在系统，不一定是容器或虚拟机。改用宿主机可达地址，并检查端口映射。

## 检查连接

1. 在 Ollama 主机运行 `ollama list`；
2. 确认目标模型已拉取；
3. 在 Cherry Studio 运行服务商连接检查；
4. 点击**添加**同步模型；
5. 运行模型健康检查；
6. 回到对话界面发送简单消息；
7. 再测试思考、图片、MCP 或知识库。

本机命令也失败时，先修复 Ollama；只有 Cherry Studio 失败时，重点检查 Base URL、网络与模型标签。

## 常见问题

### 无法连接 `localhost:11434`

Ollama 未启动、端口被修改或被防火墙拦截。先运行 `ollama list`，并检查 Ollama 日志。

### 模型列表为空

当前 Ollama 主机没有已拉取模型，或 Cherry Studio 连接到了错误主机。`ollama list` 与 Cherry Studio 必须指向同一实例。

### 找不到刚下载的模型

重新点击**添加**同步列表，并使用 `ollama list` 显示的完整名称和标签。Cherry Studio 同步不会替你执行下载。

### 首次回复很慢

Ollama 正在把模型加载到内存或显存。用 `ollama ps` 检查加载位置；后续请求通常更快。

### 返回内存不足、崩溃或一直排队

选择更小参数量或更高量化的模型，缩短上下文，降低并发，并停止其他已加载模型。

### 返回 503

服务器负载过高或队列已满。降低并发、等待当前请求完成，或调整 Ollama 队列配置。

### 图片或 MCP 不可用

确认具体模型标签支持相应能力，并检查 Cherry Studio 是否正确识别。普通对话可用不代表模型支持视觉或工具。

### 远程连接被拒绝

确认 Ollama 已监听非本地地址、端口已开放、反向代理路径正确。不要通过关闭所有安全措施解决公网连接问题。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。Ollama API 见[官方文档](https://docs.ollama.com/api/introduction)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
