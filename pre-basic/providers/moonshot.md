---
icon: moon
---

# Moonshot AI (Kimi)

Cherry Studio V2 的 Moonshot AI 内置模板用于连接 Kimi API 开放平台。模板默认使用 OpenAI Chat Completions 协议，同时提供 Moonshot 的 Anthropic 兼容端点。

当前 Kimi 模型覆盖通用对话、长程编程、视觉理解和 Agent 等场景。不同代际模型使用的思考参数并不相同，配置时应先确认模型 ID，再选择 Cherry Studio 中的思考选项。

{% hint style="info" %}
Kimi 网页端、Kimi 会员、Kimi Code 与 Kimi API 开放平台是不同产品。网页端或会员登录状态不会自动写入 Cherry Studio；通过 Cherry Studio 调用需要单独创建 API Key，并按开放平台规则计费。
{% endhint %}

## 开始前准备

- 可登录 [Kimi API 开放平台](https://platform.kimi.com/)的账户；
- 在 [API Keys](https://platform.moonshot.cn/console/api-keys) 创建的 API Key；
- 账户具有目标模型所需的余额和访问权限；
- 已查看当前的[模型列表](https://platform.kimi.com/docs/models)和参数限制。

建议为 Cherry Studio 单独创建 Key，便于区分用量和撤销权限。

## 配置 Moonshot AI

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**，选择 **Moonshot AI**；
3. 输入 Kimi API Key；
4. 保留默认 Base URL `https://api.moonshot.cn`；
5. 打开页面顶部的服务商开关；
6. 在模型列表点击**添加**，检查同步预览并应用变更；
7. 只启用准备使用的模型。

{% hint style="danger" %}
不要把 API Key 写入聊天消息、文档、代码仓库或问题截图。密钥泄露后应立即在开放平台删除并重新创建。
{% endhint %}

官方 SDK 文档中的地址通常写为 `https://api.moonshot.cn/v1`。Cherry Studio 模板会处理接口路径，因此使用内置模板时保留页面中的默认地址即可，不要重复追加请求路径。

## 选择模型

以实际同步列表为准。当前主要模型可按以下方式选择：

| 模型 ID | 主要用途 | Cherry Studio 使用提示 |
| --- | --- | --- |
| `kimi-k3` | 旗舰通用模型，1M 上下文，适合长程编程、知识工作和复杂推理 | 当前 V2 建议将思考保持为**默认** |
| `kimi-k2.7-code` | 256K 上下文的编程与 Agent 模型 | 始终思考，保持**默认** |
| `kimi-k2.7-code-highspeed` | 与 K2.7 Code 同系列、输出更快 | 资源繁忙时可能波动 |
| `kimi-k2.6` | 256K 上下文，适合通用对话、视觉和 Agent | 可使用默认思考，或按需关闭 |

Kimi K3、K2.7 Code 与 K2.6 官方均支持文本、图片和视频输入；具体附件入口还取决于当前 Cherry Studio 版本能否正确识别模型能力。

模型名称、访问条件和生命周期会变化。不要只根据旧截图手动输入模型 ID；优先重新点击**添加**同步列表，并以 Kimi 官方文档为准。

## 设置思考模式

Kimi 不同模型系列使用不同的推理参数：

- Kimi K3 始终开启思考，通过顶层 `reasoning_effort` 使用 `low`、`high` 或 `max`，默认是 `max`；
- Kimi K2.7 Code 始终开启思考，不支持关闭；
- Kimi K2.6 使用 `thinking` 控制开启或关闭思考。

{% hint style="warning" %}
当前 Cherry Studio V2 会把 Kimi K2.5 及更新模型统一识别为 Kimi 思考模型，并为非默认选项发送 `thinking` 参数。Kimi K3 使用的是 `reasoning_effort`，K2.7 Code 又不允许关闭思考，因此使用 K3 或 K2.7 Code 时请保持**默认**，避免请求因参数不兼容而返回 400。
{% endhint %}

Kimi K3 的低、高、最高三档推理强度目前可能尚未完整显示在 Cherry Studio 的思考菜单中。保持默认时，K3 会使用服务商默认的 `max`；若必须精确控制强度，应等待 Cherry Studio 更新相应适配。

使用 K2.6 时：

- **默认**：不覆盖服务商默认行为；
- **关闭**：发送禁用思考参数；
- **自动**：当前 V2 会发送启用思考参数。

K2.5 及更新模型具有固定或受限的采样参数。遇到参数错误时，先恢复温度、Top P 和惩罚项的默认值。

## 使用图片、视频与文件

官方模型能力与客户端当前识别结果需要分别确认：

1. 重新同步模型列表；
2. 选择目标模型；
3. 检查输入框是否出现图片或文件入口；
4. 先上传一张普通图片进行健康测试；
5. 再测试视频或大型附件。

当前 V2 已能自动识别 K2.6 的视觉能力；K3 和 K2.7 Code 的官方能力较新，当前版本可能暂未显示完整的视觉标记。若附件入口没有出现，先更新 Cherry Studio 和模型列表；仍不可用时，可暂用 `kimi-k2.6`，不要把不支持的内容强行发送为文本。

对于 PDF，Moonshot 内置模板当前不会直接使用 Kimi 的原生文件上传接口。Cherry Studio 会先在本地提取 PDF 文本，再把文本发送给模型：

- 文本型 PDF 通常可以直接处理；
- 扫描件可能需要先做 OCR；
- 表格、复杂排版和图片信息可能在提取时丢失；
- 提取后的文本会占用模型输入 Token。

## 工具调用与 MCP

Kimi 官方模型支持工具调用，但 Cherry Studio 是否显示 MCP 能力还依赖模型能力识别。

建议按以下顺序验证：

1. 先完成一轮普通对话；
2. 启用一个简单的 MCP 工具；
3. 使用明确要求调用工具的提示词；
4. 确认模型实际发起调用；
5. 再增加多个工具或长链路任务。

当前 V2 已包含 Kimi K2 系列的工具识别规则，但 K3 和 K2.7 Code 的自动识别可能滞后于官方模型发布。若 MCP 入口缺失，先更新 Cherry Studio；仍无法识别时，暂用已被当前版本识别的模型完成任务。

当 MCP 返回图片、音频或含大体积二进制数据的资源时，Cherry Studio 会把结果转换成文本摘要，避免 base64 内容超过 Kimi 请求大小限制。此时模型能看到工具结果的文字说明，但不能直接分析被替换掉的原始媒体。

## 知识库与嵌入模型

Moonshot AI 内置模板当前配置的是对话端点，不提供嵌入模型。使用知识库或[全局记忆](../../advanced-basic/memory.md)时：

- 对话模型可以继续选择 Kimi；
- 嵌入模型需要从其他服务商选择；
- 对话模型和嵌入模型不必来自同一家服务商；
- 配置后分别运行模型健康检查。

## 检查连接

1. 在 API Key 区域运行连接检查；
2. 选择一个已同步并启用的模型；
3. 确认检查成功；
4. 在模型列表运行健康检查；
5. 回到对话界面发送一条简单消息；
6. 再分别测试思考、附件和 MCP。

连接检查成功只说明基本凭据可用，不代表账户已获得所有模型权限，也不代表每种模型能力都已被当前客户端识别。

## 常见问题

### 返回 401

API Key 无效、已删除或复制不完整。重新创建 Key，并确认没有多余空格。

### 返回余额或访问条件错误

检查开放平台余额、账户等级和目标模型的访问条件。Kimi 网页端会员余额不能替代 API 余额。

### 返回 404 或模型不存在

模型 ID 已变更、已下线或账户尚无权访问。重新点击**添加**同步列表，并在[模型列表](https://platform.kimi.com/docs/models)核对。

### 返回 400 或提示 `thinking` 参数无效

如果使用 Kimi K3 或 K2.7 Code，将思考选项改为**默认**，并恢复温度、Top P 等参数的默认值。K3 不接受 K2.6 使用的 `thinking` 开关。

### 返回 429 或请求繁忙

账户达到并发、RPM、TPM 或 TPD 限制，或高速模型资源暂时繁忙。降低并发、缩短上下文或稍后重试。

### K3 或 K2.7 Code 没有图片、视频或 MCP 入口

这是官方模型能力与当前 Cherry Studio 自动识别规则没有同步的表现。更新 Cherry Studio 并重新同步模型；若仍无入口，暂用 K2.6，等待客户端适配更新。

### PDF 内容识别不完整

确认 PDF 是否为扫描件。先执行 OCR，或把关键页面转换为图片后使用已被 Cherry Studio 识别为视觉模型的 Kimi 模型。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。Kimi 参数差异见[模型参数参考](https://platform.kimi.com/docs/api/models-overview)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
