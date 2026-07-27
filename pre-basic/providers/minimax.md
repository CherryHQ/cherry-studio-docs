---
icon: bolt
---

# MiniMax

Cherry Studio V2 内置 **MiniMax** 与 **MiniMax 海外版**两个服务商。二者都可连接 MiniMax 的语言模型接口，但使用不同的开放平台、Base URL 和 API Key。

本页介绍如何在 Cherry Studio 中使用 MiniMax M 系列进行对话、编程和 Agent 任务。MiniMax 的语音、图像、视频和音乐生成使用独立 API，不等同于这里的语言模型服务。

{% hint style="info" %}
中国大陆开放平台请选择 **MiniMax**；国际开放平台请选择 **MiniMax 海外版**。两个平台的账户、Key、余额和订阅可能相互独立，不要混用。
{% endhint %}

## 开始前准备

根据账户所在平台准备凭据：

| 平台 | Cherry Studio 服务商 | 默认 Base URL |
| --- | --- | --- |
| 中国大陆 | MiniMax | `https://api.minimaxi.com/v1/` |
| 国际 | MiniMax 海外版 | `https://api.minimax.io/v1/` |

- 中国大陆用户可在 [MiniMax 开放平台](https://platform.minimaxi.com/)创建 API Key；
- 国际用户可在 [MiniMax API Platform](https://platform.minimax.io/)创建 API Key；
- 确认 Key 对应按量付费余额或有效的 Token Plan；
- 查看当前可用的模型、上下文和速率限制。

按量付费 API Key 与 Token Plan Key 使用不同的余额或额度。连接成功但返回额度错误时，应回到创建该 Key 的对应计费页面检查，而不是只查看另一个账户余额。

## 配置 MiniMax

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 中国大陆账户选择 **MiniMax**，国际账户选择 **MiniMax 海外版**；
4. 输入对应平台创建的 API Key；
5. 保留内置的默认 Base URL；
6. 打开页面顶部的服务商开关；
7. 在模型列表点击**添加**，检查同步预览并应用变更；
8. 只启用准备使用的模型。

{% hint style="danger" %}
不要把 API Key 写入聊天消息、文档、代码仓库或问题截图。密钥泄露后应立即在对应 MiniMax 开放平台删除并重新创建。
{% endhint %}

如果把 `.com` 平台的 Key 填入 `.io` 服务商，或反向混用，通常会返回未授权。优先检查服务商条目是否选对，不要随意覆盖内置地址。

## 选择模型

Cherry Studio V2 当前为两个 MiniMax 服务商预置以下主要模型：

| 模型 ID | 主要用途 |
| --- | --- |
| `MiniMax-M3` | 旗舰多模态编程与 Agent 模型，官方提供 1M 上下文 |
| `MiniMax-M2.7` | 编程、工具调用、办公和复杂 Agent 工作流 |
| `MiniMax-M2.7-highspeed` | 与 M2.7 同系列，优先考虑更低输出延迟 |

同步列表中还可能出现 M2.5、M2.1 或其他模型。模型 ID 和生命周期以实际同步结果及 MiniMax 官方文档为准，不要依赖旧文档中的 `abab` 系列名称。

- 日常综合任务优先尝试 M3；
- 主要做代码和工具调用时，可比较 M3 与 M2.7；
- 对输出速度敏感时选择 `MiniMax-M2.7-highspeed`；
- 需要可复现结果时记录完整模型 ID，不要只记录显示名称。

## OpenAI 与 Anthropic 兼容端点

两个内置服务商都包含 OpenAI Chat Completions 与 Anthropic Messages 兼容地址：

| 平台 | OpenAI 兼容 | Anthropic 兼容 |
| --- | --- | --- |
| 中国大陆 | `https://api.minimaxi.com/v1/` | `https://api.minimaxi.com/anthropic` |
| 国际 | `https://api.minimax.io/v1/` | `https://api.minimax.io/anthropic` |

Cherry Studio 默认使用 OpenAI Chat Completions。普通对话和模型同步可以先保持默认。

MiniMax 官方更推荐 Anthropic 兼容端点处理思考块与交错思考。如果你在 Cherry Studio 中手动为模型切换端点类型，应同时确认：

- Base URL 与账户区域匹配；
- 模型使用 Anthropic Messages 协议；
- Key 来自同一平台；
- 普通对话、思考显示和工具调用都重新通过健康检查。

不要只修改 Base URL 而保留错误的协议类型。OpenAI 与 Anthropic 兼容接口的消息结构并不完全相同。

## 思考内容与多轮工具调用

MiniMax M 系列会返回推理内容。对于 M2 系列，Cherry Studio 能识别其为推理模型；M3 发布较新，当前 V2 可能尚未完整显示专用的思考控制项。

使用时建议：

- 将思考设置保持为**默认**；
- 不要为固定思考模型强行发送关闭或自定义预算；
- 使用流式输出处理长回复；
- 不随意修改温度、Top P 和惩罚项；
- 切换协议后重新测试思考内容是否正常显示。

{% hint style="warning" %}
MiniMax 的多轮工具调用依赖完整的 assistant 消息，包括思考内容和 `tool_calls`。Cherry Studio 会负责维护对话历史；不要在工具执行中途手动删除或重写上一轮消息，否则模型可能失去推理连续性。
{% endhint %}

如果使用 OpenAI 兼容端点时看到 `<think>` 标签，通常是服务商把思考内容放在 `content` 中。切换到 Anthropic 兼容端点前，先在单独的服务商副本中测试，避免影响已有对话。

## 工具调用与 MCP

Cherry Studio V2 已识别 MiniMax M2、M2.x 和 M3 系列的工具调用能力，可用于 MCP 与 Agent 场景。

建议按以下顺序验证：

1. 选择已同步并启用的 M3 或 M2.7；
2. 完成一轮普通对话；
3. 启用一个简单的 MCP 工具；
4. 使用明确要求调用工具的提示词；
5. 确认模型实际发起工具调用；
6. 再增加多个工具或长链路任务。

长链路任务中应保留完整上下文。若模型反复调用同一工具，可先减少工具数量、缩短系统提示词，并明确停止条件。

## 图片、视频与文件

MiniMax M3 官方支持文本、图片和视频输入，但当前 Cherry Studio V2 的自动视觉模型识别规则可能尚未包含 M3。因此：

- 如果输入框显示图片或视频入口，先用小文件做健康测试；
- 如果入口没有出现，先更新 Cherry Studio 并重新同步模型；
- 不要仅修改显示名称来伪装模型能力；
- 当前版本仍不可用时，等待客户端适配更新。

MiniMax OpenAI 与 Anthropic 兼容接口中的旧版 M2 模型通常只支持文本和工具调用，不要把 MiniMax 的独立图像、视频或语音生成模型作为聊天模型添加。

对于 PDF，Cherry Studio 当前会先在本地提取文本，再把文本发送给 MiniMax：

- 文本型 PDF 通常可以直接处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能在提取时丢失；
- 提取后的文本会占用上下文与输入用量。

## 多模态生成不是聊天模型

MiniMax 还提供语音、图像、视频和音乐生成 API，但这些接口有独立的请求格式和任务流程。模型出现在开放平台不代表可以直接通过 Cherry Studio 的聊天服务商调用。

例如，把视频生成模型手动添加到对话模型列表，通常只会得到参数或端点错误。需要相关能力时，应使用 Cherry Studio 已适配的专用入口；当前没有适配的接口不能通过修改模型名称代替。

## 知识库与嵌入模型

MiniMax 内置服务商当前配置的是语言模型端点，不提供嵌入模型。使用知识库或[全局记忆](../../advanced-basic/memory.md)时：

- 对话模型可以继续选择 MiniMax；
- 嵌入模型需要从其他服务商选择；
- 两类模型不必来自同一家服务商；
- 配置后分别运行模型健康检查。

## 检查连接

1. 确认选择了正确的中国大陆或国际服务商；
2. 在 API Key 区域运行连接检查；
3. 选择一个已同步并启用的模型；
4. 在模型列表运行健康检查；
5. 回到对话界面发送一条简单消息；
6. 再分别测试长回复、思考显示和 MCP。

连接检查成功只说明基本凭据可用，不代表 Key 具有所有模型权限，也不代表 Token Plan 仍有可用额度。

## 常见问题

### 返回未授权或错误码 1004

API Key 无效、已删除，或 Key 与 `.com` / `.io` 服务商不匹配。确认服务商区域后重新创建 Key。

### 返回余额不足或错误码 1008

检查创建当前 Key 的计费类型和账户。按量付费余额与 Token Plan 额度需要分别查看。

### 返回限速、1002 或 1041

请求达到速率或并发限制。降低并行请求、缩短上下文并稍后重试；持续出现时检查账户等级和官方限额。

### 返回 Token 超限或错误码 1039

当前对话、附件文本和预期输出超过模型上下文。新建对话、减少附件、缩短历史，或选择更长上下文的模型。

### 模型列表仍是旧型号

重新点击**添加**同步列表，确认 Base URL 没有被改坏。若远端列表暂未返回新模型，可使用内置预置模型或按官方完整 ID 手动添加。

### M3 没有思考或图片入口

M3 的官方能力比当前 Cherry Studio 自动识别规则更新。先更新客户端并重新同步；仍未显示时，不要强行覆盖模型类型，等待适配更新。

### MCP 调用中断或上下文错乱

先只启用一个工具，并确认使用 M3 或 M2.7。不要删除工具调用前一轮的 assistant 消息；必要时新建对话重新测试。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。模型能力见 [MiniMax Models](https://platform.minimax.io/docs/guides/models-intro)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
