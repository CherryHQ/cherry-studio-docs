---
description: 让火山方舟模型使用 Cherry Studio 联网工具
icon: globe-pointer
---

# 火山引擎模型联网

Cherry Studio V2 可以让火山方舟的对话模型使用外部网络搜索。推荐组合是：

```text
火山方舟模型
    + Cherry Studio 默认搜索服务商
    + Cherry Studio 默认 URL 获取服务商
```

当前 V2 没有把火山方舟 Web Search 注册为独立的网络搜索服务商，也不会在内置 `doubao` 服务商中自动注入方舟的云端 Web Search 工具。

{% hint style="warning" %}
旧教程中的“创建零代码应用 → 开通联网插件 → 把应用当作 OpenAI 模型接入”不是当前 V2 的推荐路径。界面、插件和接口已经变化，旧截图与旧 API Host 写法不应继续照搬。
{% endhint %}

## 先区分两套联网能力

| 方式 | 搜索由谁执行 | Cherry Studio V2 当前状态 | 推荐场景 |
| --- | --- | --- | --- |
| Cherry Studio 外部联网 | ExaMCP、Tavily、SearXNG、博查等搜索服务商 | 已支持 | 普通对话、希望统一管理搜索服务 |
| 火山方舟云端 Web Search | 火山方舟 Responses API 或应用插件 | 没有专用适配 | 已在方舟侧开发应用，并愿意自行验证接口 |

本文介绍第一种方式。它不要求在火山方舟创建“我的应用”，也不依赖旧版联网插件。

### Cherry Studio 外部联网

当前模型没有被识别为原生联网模型时，Cherry Studio 会向模型提供：

- 搜索关键词工具；
- 读取 URL 工具。

模型通过 Function Calling 决定何时搜索和读取网页。搜索结果会返回给模型，再由模型生成带引用的回答。

### 火山方舟云端 Web Search

火山方舟官网提供 Responses API、Web Search、Knowledge Search、Remote MCP 等云端工具。这些能力属于方舟接口，不等同于 Cherry Studio 的网络搜索设置。

当前内置 `doubao` 服务商默认使用：

```text
OpenAI Chat Completions
```

默认 API Host：

```text
https://ark.cn-beijing.volces.com/api/v3/
```

官网支持某项 Responses API 工具，不代表 Cherry Studio 已经自动适配它的请求字段、事件流和引用结果。

## 使用前准备

需要准备：

1. 火山引擎账号；
2. 火山方舟 API Key；
3. 当前可用的 Model ID 或 Endpoint ID；
4. 支持 Function Calling 的对话模型；
5. 一个关键词搜索服务商；
6. 一个 URL 获取服务商。

火山方舟基础配置参见[火山引擎（方舟 / 豆包）](../providers/doubao.md)。

{% hint style="danger" %}
不要把火山方舟 API Key、搜索服务 API Key 或带令牌的私有 URL 写入聊天、截图和公开文档。
{% endhint %}

## 配置火山方舟模型

### 1. 开通并复制模型标识

在火山方舟控制台：

1. 创建 API Key；
2. 开通准备使用的模型；
3. 复制当前 Model ID；
4. 如果使用专用推理接入点，复制 `ep-...` 格式的 Endpoint ID；
5. 确认项目、地域、余额和限流。

不要复制：

- 模型显示名称；
- 控制台页面 URL；
- 旧应用的 Bot ID；
- 其他项目中的 Endpoint ID。

### 2. 在 Cherry Studio 启用服务商

1. 打开 `设置 → 模型服务`；
2. 将筛选切换为**全部服务商**；
3. 选择 **Doubao / 豆包 / 火山引擎**；
4. 填写方舟 API Key；
5. 保留默认 API Host；
6. 打开服务商开关；
7. 手动添加当前 Model ID 或 Endpoint ID；
8. 运行模型健康检查。

先发送一条普通文本消息，确认对话可用，再配置联网。

## 选择适合联网的模型

Cherry Studio 外部联网优先使用支持结构化 Function Calling 的模型。

当前 V2 会识别多种较新的 Doubao Seed 模型，例如符合以下系列命名的模型：

```text
doubao-seed-1.6...
doubao-seed-1.8...
doubao-seed-2.0...
doubao-seed-code...
```

具体 Model ID 会更新，应从火山方舟当前模型页复制，不要照抄上面的系列名称作为完整 ID。

{% hint style="warning" %}
旧教程使用的 DeepSeek R1 在当前 V2 中被排除在结构化 Function Calling 模型之外，不适合作为 Cherry Studio 外部联网的首选。即使普通对话可用，也可能不调用搜索工具。
{% endhint %}

在模型管理中可以查看或调整能力标记，但能力标记只影响客户端判断，不会让模型获得服务端原本不支持的 Function Calling。

## 配置网络搜索

打开：

```text
设置 → 网络搜索
```

同时设置：

| 设置 | 作用 | 可选示例 |
| --- | --- | --- |
| 默认搜索服务商 | 根据关键词查找网页 | ExaMCP、Tavily、SearXNG、博查 |
| 默认 URL 获取服务商 | 读取具体网页正文 | Fetch、Jina |

这两项缺一不可。

不想额外申请搜索 API Key 时，可先使用：

```text
默认搜索服务商：ExaMCP
默认 URL 获取服务商：Fetch
```

详细说明：

- [联网模式](README.md)
- [免费联网模式](free-search.md)
- [SearXNG 配置](searxng.md)

## 在对话中启用

1. 返回对话页面；
2. 选择已通过健康检查的火山方舟模型；
3. 点击输入框下方的**地球**图标；
4. 确认图标高亮；
5. 发送需要实时资料的问题。

测试问题：

```text
先联网搜索 Cherry Studio 最近一个正式版本，
只引用官方 GitHub Release，列出版本号、发布日期和主要变化。
```

检查回答中是否：

- 实际调用了搜索工具；
- 出现可打开的引用；
- 引用来自要求的网站；
- 日期和版本号与原文一致；
- 没有把旧知识当作实时结果。

## 联网时发生了什么

对于当前 V2 中没有原生联网适配的火山方舟模型，流程通常是：

1. 用户开启联网并发送问题；
2. Cherry Studio 将外部搜索工具提供给模型；
3. 模型生成结构化工具调用；
4. Cherry Studio 调用默认搜索服务商；
5. 模型按需调用默认 URL 获取服务商；
6. 搜索结果和网页正文回传给模型；
7. 模型生成最终回答与引用。

搜索服务的 API Key 不会发送给火山方舟模型，但搜索结果正文会作为对话上下文发送给火山方舟。

## 与旧版教程的差异

| 旧版做法 | 当前 V2 建议 |
| --- | --- |
| 创建零代码“我的应用” | 直接使用方舟 Model ID 或 Endpoint ID |
| 在方舟应用中购买或启用旧联网插件 | 在 Cherry Studio 配置外部搜索服务商 |
| 添加自定义 OpenAI 服务商 | 优先使用内置 Doubao 服务商 |
| 把完整 `/chat/completions` 写入 URL | 填写 Base URL，由 V2 拼接请求路径 |
| 在 API Host 末尾添加 `#` | 不需要 |
| 把应用小字 ID 当作模型名 | 使用当前 Model ID 或 Endpoint ID |
| 使用旧 DeepSeek R1 联网示例 | 选择支持 Function Calling 的当前模型 |

从旧配置迁移时，建议新建一个干净的 Doubao 服务商实例或恢复内置服务商默认值，不要在旧地址上继续叠加兼容参数。

## 不要手动标记“原生联网”

模型详情中的联网能力标记会影响 Cherry Studio 选择原生联网还是外部联网。

不要为了显示地球图标，直接把普通火山方舟模型标记为原生联网模型。当前 V2 没有对应的方舟 Web Search 插件适配，错误标记可能导致：

- Cherry Studio 不再注入外部搜索工具；
- 方舟端又没有收到正确的云端 Web Search 工具；
- 联网开关高亮，但实际没有搜索。

如果误改，恢复模型自动识别，再使用本页的外部联网配置。

## 如果必须使用方舟云端 Web Search

火山方舟云端 Web Search 主要通过 Responses API 或方舟应用配置。当前 Cherry Studio V2 内置 `doubao` 连接不提供专用设置页来配置这些工具。

在以下条件都确认前，不建议把方舟云端应用当作普通模型接入：

1. 已根据火山方舟当前官方文档开通 Web Search；
2. 已确认调用的是 Chat API、Responses API 还是应用 Bot API；
3. 已获得对应的 Model ID、Endpoint ID 或 Bot ID；
4. 已确认请求地址和认证方式；
5. 已确认返回事件能被 Cherry Studio 当前端点解析；
6. 已确认引用、流式输出和工具结果格式；
7. 已了解模型与搜索插件的费用。

{% hint style="info" %}
这是高级兼容场景，不属于当前 V2 的内置联网流程。方舟接口升级后，历史应用 URL 和参数可能失效。
{% endhint %}

火山方舟当前工具说明可参考[火山方舟产品文档](https://www.volcengine.com/docs/82379/)和[工具调用](https://www.volcengine.com/docs/82379/1958524)。

## 隐私与费用

使用 Cherry Studio 外部联网时，数据可能分别发送给：

- 火山方舟：用户问题、搜索结果和读取到的网页正文；
- 搜索服务商：搜索关键词；
- 目标网站：网页请求；
- URL 获取服务商：目标 URL，取决于所选服务。

费用可能包括：

- 方舟模型输入与输出 Token；
- 搜索服务调用；
- 方舟推理接入点或模型单元；
- 额外网络流量；
- 如果另行使用方舟 Web Search，相关插件费用。

不要依据旧截图中的免费次数或价格做预算，应以各服务当前控制台为准。

## 常见问题

### 点击地球图标后跳转到网络搜索设置

当前模型没有原生联网适配，并且缺少**默认搜索服务商**或**默认 URL 获取服务商**。同时配置两项后重试。

### 普通对话可用，但没有调用搜索工具

依次检查：

1. 地球图标是否高亮；
2. 当前模型是否支持 Function Calling；
3. Model ID 是否被错误标记为不支持工具；
4. 是否使用了旧 DeepSeek R1；
5. 问题是否明确要求先搜索并引用；
6. 搜索服务商是否检测成功。

可以改用当前 Doubao Seed 工具模型，并在新对话中重试。

### 模型只说“我会搜索”，但没有结果

这不是成功的工具调用。检查消息详情中是否出现结构化工具过程；没有时，更换工具调用能力更稳定的模型。

### 有搜索结果，但引用打不开

可能是网页失效、登录限制、反爬、地区限制或 Fetch 读取失败。要求模型改用其他来源，并手动核对关键结论。

### 开启后仍使用模型旧知识

明确提示：

```text
必须先联网搜索；如果搜索失败，请说明失败，不要仅凭已有知识回答。
```

仍无效时，新建对话、更换模型或检查搜索服务商。

### 想使用火山方舟自己的 Web Search

Cherry Studio 当前没有对应的内置配置。不要把模型能力开关当作适配器；应按方舟当前 Responses API 或应用 API 文档自行验证，或暂时使用 Cherry Studio 外部联网。

### 返回 401、403、404 或 429

这些通常是方舟模型连接问题，而不是网络搜索设置本身：

- `401`：API Key 无效；
- `403`：项目、模型或 Endpoint 没有权限；
- `404`：API Host、Model ID 或 Endpoint ID 错误；
- `429`：达到速率、并发或额度限制。

先关闭联网，确认普通对话恢复，再分别排查模型和搜索服务。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到疑问、Bug 或功能建议，请参考[反馈与建议](../../question-contact/suggestions.md)中的官方渠道。
