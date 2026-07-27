# LM Studio

LM Studio 可以在 macOS、Windows 和 Linux 上下载并运行本地模型，并通过 OpenAI 兼容 API 向 Cherry Studio 提供对话、视觉、工具调用和嵌入能力。

Cherry Studio V2 内置了 LM Studio 服务商，默认连接 `http://localhost:1234`。普通对话使用 OpenAI 兼容接口，模型列表来自 `/v1/models`。

{% hint style="info" %}
Cherry Studio 中的模型同步只读取 LM Studio 当前可见的模型，不会替你下载模型。请先在 LM Studio 的 **Discover** 页面下载模型，再启动本地 API Server。
{% endhint %}

## 准备 LM Studio

1. 从 [LM Studio 官网](https://lmstudio.ai/)下载并安装最新版本；
2. 打开 **Discover**，搜索并下载模型；
3. 根据设备内存或显存选择参数规模和量化版本；
4. 打开 **Developer** 页面；
5. 点击 **Start server** 启动 API Server。

默认监听地址为：

```text
http://localhost:1234
```

也可以在终端启动：

```bash
lms server start
```

首次使用建议先在 LM Studio 内完成一次加载和对话，确认模型本身可以运行，再连接 Cherry Studio。

## 选择模型与量化

模型文件、量化方式和上下文长度都会影响内存占用与速度。

- 参数规模越大，通常能力越强，但需要更多 RAM 或 VRAM；
- GGUF 模型可以使用 CPU 与 GPU 混合推理；
- Apple Silicon 可使用兼容的 MLX 模型；
- 较低比特量化占用更小，但可能降低输出质量；
- 上下文越长，KV Cache 占用越高；
- 视觉模型还需要处理图片编码，占用通常高于同规模纯文本模型。

不确定时，先选择设备能够稳定加载的中小模型和常见量化版本，再逐步增加参数规模或上下文。

LM Studio CLI 也可以估算资源占用：

```bash
lms load --estimate-only <model-key>
```

## 在 Cherry Studio 配置

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **LM Studio**；
4. 保留 Base URL `http://localhost:1234`；
5. LM Studio 未启用鉴权时，将 API Key 留空；
6. 打开页面顶部的服务商开关；
7. 点击**添加**或同步模型；
8. 检查同步预览并应用变更；
9. 只启用准备使用的模型；
10. 运行模型健康检查，再进入对话测试。

建议在 Base URL 中填写主机和端口，不必手动附加 `/v1`。Cherry Studio 会按 OpenAI 兼容接口访问模型列表和对话接口。

## 模型列表为什么会变化

LM Studio 的 `/v1/models` 返回服务器当前可见的模型：

| LM Studio 设置 | 模型列表行为 |
| --- | --- |
| 开启 Just-In-Time Model Loading | 可以返回所有已下载模型，并在首次请求时自动加载 |
| 关闭 Just-In-Time Model Loading | 通常只返回已经加载到内存的模型 |

因此，旧版教程中“必须先手动 Load 才能同步”的说法不再适用于所有版本。

如果 Cherry Studio 中模型列表为空：

1. 确认 API Server 已启动；
2. 在浏览器或终端访问 `http://localhost:1234/v1/models`；
3. 检查 LM Studio 是否开启 JIT Loading；
4. 关闭 JIT 时，先在 LM Studio 加载模型；
5. 回到 Cherry Studio 重新同步。

{% hint style="warning" %}
模型同步成功不代表设备一定能加载该模型。开启 JIT 后，未加载的模型也可能出现在列表中；首次对话才会触发加载并暴露内存不足、上下文过大等问题。
{% endhint %}

## API Token 与鉴权

LM Studio 默认不要求 API Token。本机使用时，Cherry Studio 的 API Key 可以留空。

LM Studio 0.4.0 及以上版本可以在 `Developer → Server Settings` 开启 **Require Authentication**：

1. 打开 **Manage Tokens**；
2. 创建 Token 并设置权限；
3. 复制新 Token；
4. 在 Cherry Studio 的 LM Studio 服务商中填入该 Token；
5. 重新同步模型并运行健康检查。

Cherry Studio 会把非空 API Key 作为 Bearer Token 发送。LM Studio 也支持 OpenAI 与 Anthropic 兼容接口常见的鉴权头。

{% hint style="danger" %}
API Token 只在创建时完整显示。不要把 Token 写入聊天、文档、代码仓库或问题截图；泄露后应立即删除并重新创建。
{% endhint %}

## 对话、视觉与 MCP

### 普通对话

选择支持 Chat Completions 的指令模型。基础对话正常后，再测试思考、图片或工具调用。

本地模型的回答质量取决于模型、量化、提示模板和上下文设置。能成功返回内容，只说明接口可用，并不代表模型适合所有任务。

### 视觉理解

LM Studio 的 OpenAI 兼容 Chat Completions 支持文本和图片，但具体模型必须具备视觉能力。

1. 下载明确标记为视觉模型的版本；
2. 在 LM Studio 中加载或允许 JIT 加载；
3. 同步到 Cherry Studio；
4. 确认模型显示图片能力；
5. 先发送一张尺寸较小的图片测试。

模型名称相近不代表每个量化或变体都支持图片。若 Cherry Studio 没有识别到视觉能力，应先确认模型 ID 和运行时支持，不要只修改显示名称。

### 工具调用与 MCP

Cherry Studio 的 MCP 依赖模型输出结构化 Tool Calling。LM Studio 会根据模型模板提供原生或兼容模式，但实际稳定性仍由模型决定。

建议按以下顺序测试：

1. 先完成普通对话；
2. 只启用一个简单 MCP 工具；
3. 明确要求模型调用该工具；
4. 检查是否产生结构化调用；
5. 确认工具结果能够回传给模型；
6. 再逐步增加工具数量。

小模型可能只输出“准备调用工具”的文字，而没有真正发起调用。遇到这种情况，优先换用带原生 Tool Use 标记、参数规模更大或工具训练更充分的模型。

Cherry Studio MCP 与 LM Studio 服务器自身的 MCP 集成是两条不同链路。只使用 Cherry Studio MCP 时，不需要在 LM Studio 中重复配置同一个工具。

## 思考模型与结构化输出

LM Studio 能否处理思考参数或结构化输出，取决于模型模板和 OpenAI 兼容实现。

- 优先使用 LM Studio 已明确支持的模型与模板；
- 不同模型的思考开关和强度参数并不通用；
- 如果启用思考后返回参数错误，先恢复默认或关闭思考；
- JSON 或结构化输出失败时，先在 LM Studio 中用同一模型验证；
- 不要通过修改模型显示名称伪装成另一种能力。

## 模型加载、JIT 与显存

开启 JIT Loading 后，Cherry Studio 首次调用某个模型时，LM Studio 可以自动把它加载到内存或显存。首次回复会明显慢于后续请求。

LM Studio 0.4+ 还提供：

- **Idle TTL**：模型空闲多久后自动卸载；
- **Auto-Evict**：加载新模型前自动卸载先前由 JIT 加载的模型；
- **Only Keep Last JIT Loaded Model**：只保留最近使用的 JIT 模型。

Cherry Studio 的 LM Studio 服务商页面也会显示**保持活跃时间**。实际是否卸载以及何时释放内存，还会受到 LM Studio 的 JIT、TTL、Auto-Evict 和手动加载状态影响；排查时以 LM Studio 的已加载模型列表和服务器设置为准。

如果需要手动控制，可以使用：

```bash
lms load <model-key> --context-length 8192 --gpu max
lms unload <model-key>
lms unload --all
```

不要同时加载多个接近设备上限的大模型。频繁切换模型时，开启 Auto-Evict 通常比持续堆叠模型更稳定。

## 上下文长度

模型支持的最大上下文与实际加载上下文不是同一个概念。LM Studio 在加载模型时配置的 Context Length 才决定当前实例可用范围。

上下文过长可能导致：

- RAM 或 VRAM 不足；
- 首次加载时间增加；
- 提示处理变慢；
- 请求被截断或返回超限；
- 视觉和长文档任务更容易失败。

当 Cherry Studio 的模型信息大于 LM Studio 实际加载值时，应以 LM Studio 运行时配置为准。先使用较短上下文验证稳定性，再按需要增加。

## 知识库与嵌入模型

LM Studio 提供 OpenAI 兼容的 `/v1/embeddings` 接口，可以运行专用嵌入模型。

1. 下载嵌入模型；
2. 在 LM Studio 中加载或允许 JIT 加载；
3. 在 Cherry Studio 同步模型；
4. 确认该模型被识别为嵌入模型；
5. 在知识库中选择它并检测维度；
6. 运行健康检查后再导入文档。

LM Studio 在 Cherry Studio 中不支持重排序模型。需要 Rerank 时，应选择其他服务商。

嵌入模型或维度一旦用于现有知识库，不应随意更换；否则通常需要重新构建向量索引。

## PDF 与附件

当前 V2 不把 PDF 原文件直接发送给 LM Studio。Cherry Studio 会先在本地提取 PDF 文本，再交给模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会占用上下文；
- PDF 中的图片需要单独发送给视觉模型。

## Code Tools 与 Anthropic 兼容接口

Cherry Studio 的 LM Studio 预设同时保留了 Anthropic 兼容地址，默认仍为 `http://localhost:1234`，供部分 Code Tools 使用。

LM Studio 提供 `/v1/messages`。如果 Code Tool 要求 Anthropic 兼容服务：

1. 确认使用较新的 LM Studio；
2. 启动 API Server；
3. 确认目标模型支持所需工具能力；
4. 开启鉴权时填入同一个 Token；
5. 使用 LM Studio 中实际的模型标识；
6. 先用简单任务验证，再开放文件或命令权限。

支持 Messages 接口不代表任意本地模型都能可靠完成代码代理任务。模型能力、上下文、工具调用质量和设备性能都会影响结果。

## 连接局域网或远程 LM Studio

如果 Cherry Studio 与 LM Studio 不在同一台设备：

1. 在 LM Studio 的 Server Settings 开启 **Serve on Local Network**；
2. 开启 **Require Authentication** 并创建 Token；
3. 确认系统防火墙允许服务器端口；
4. 在 Cherry Studio 中填写 LM Studio 主机的局域网地址；
5. 填入 Token；
6. 先访问 `/v1/models`，再运行健康检查。

CLI 也可以监听所有网卡：

```bash
lms server start --bind 0.0.0.0
```

不要把未鉴权的 LM Studio 端口直接暴露到公网。公网使用应通过 VPN，或配置 HTTPS、鉴权和访问控制完善的反向代理。

在 Docker、虚拟机、WSL 或远程桌面场景中，`localhost` 指向 Cherry Studio 所在系统，不一定是运行 LM Studio 的主机。应改用实际可达地址。

## 常见问题

### 无法连接 `localhost:1234`

LM Studio API Server 未启动、端口已修改或被防火墙拦截。先确认 Developer 页面显示服务器正在运行。

### 模型列表为空

检查 `/v1/models` 是否有返回。关闭 JIT 时，需要先加载模型；开启 JIT 时，确认模型已经下载并对服务器可见。

### 能同步模型，但对话时报错

模型可能尚未成功加载、资源不足、上下文过大或接口模板不兼容。查看 LM Studio 服务器日志和加载状态。

### 首次回复很慢

JIT 正在加载模型。后续请求通常更快；也可以预先加载模型，但会持续占用内存或显存。

### 返回内存或显存不足

换用更小模型或更高压缩量化，缩短上下文，提高 GPU Offload 的设置应以设备余量为前提，并卸载其他模型。

### 图片或 MCP 不可用

普通对话可用不代表模型具备视觉或工具能力。检查模型版本、模板、Cherry Studio 的能力识别与 LM Studio 日志。

### API Token 无效

确认 LM Studio 已开启 Require Authentication、Token 未被删除、权限正确，并且 Cherry Studio 中没有多余空格。

### 远程连接被拒绝

确认已开启 Serve on Local Network、端口可达、防火墙和反向代理路径正确。不要通过关闭所有安全措施解决公网连接问题。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。LM Studio 的服务器、兼容接口和模型管理请参阅[官方文档](https://lmstudio.ai/docs)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
