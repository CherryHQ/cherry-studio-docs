# MiniMax Token Plan（原 Coding Plan）

MiniMax 已将 Coding Plan 升级为 **Token Plan**。它面向个人开发者、AI 编程和日常高频使用，以订阅额度或 Credits 调用 MiniMax 模型。

Cherry Studio V2 没有单独的“Coding Plan”服务商。你需要在内置的 **MiniMax** 或 **MiniMax Global** 服务商中填写 Token Plan 专用 Key。

{% hint style="info" %}
本页路径为兼容旧文档保留。MiniMax 平台中的实际产品名称、套餐和额度以当前 **Token Plan** 页面为准，不要继续套用旧教程里的 M2.1、固定月费或“每 5 小时 40 次”等过期信息。
{% endhint %}

## Token Plan 与普通 API 的区别

| 项目 | Token Plan | 普通按量 API |
| --- | --- | --- |
| Key 来源 | Token Plan / 订阅管理 | 接口密钥 |
| 常见 Key | `sk-cp...` | 普通 API Key |
| 计量方式 | 套餐额度、Credits、滚动窗口 | 按实际 API 用量计费 |
| 有效期 | 依赖订阅、席位或 Credits | 依赖账户余额和 Key 状态 |
| 适用场景 | 个人交互、编程工具、日常使用 | 生产集成、稳定按量调用 |

两类 Key **不互通**。把普通 API Key 填进 Token Plan 用法，或把 Token Plan Key 当作普通按量 Key，可能返回 401、额度错误或走错计费方式。

MiniMax 官方建议生产环境优先使用按量 API。Token Plan 可能有 RPM、TPM、滚动窗口、周额度和高峰期动态限流，不适合作为无上限的批量服务。

## 选择中国大陆或国际平台

| 账号与订阅 | Cherry Studio 服务商 | OpenAI Base URL | Anthropic Base URL |
| --- | --- | --- | --- |
| 中国大陆 MiniMax 平台 | MiniMax | `https://api.minimaxi.com/v1` | `https://api.minimaxi.com/anthropic` |
| MiniMax 国际平台 | MiniMax Global | `https://api.minimax.io/v1` | `https://api.minimax.io/anthropic` |

中国大陆站和国际站的账号、Key 与 Base URL 不应混用。判断依据是购买 Token Plan 和创建 Key 的平台，不是当前所在地区。

## 获取 Token Plan Key

### 中国大陆平台

1. 登录 [MiniMax 开放平台](https://platform.minimaxi.com/)；
2. 打开 [Token Plan](https://platform.minimaxi.com/subscribe/token-plan)；
3. 购买套餐、兑换权益或确认 Team 已分配席位；
4. 前往接口密钥；
5. 选择**创建 Token Plan Key**；
6. 复制新 Key 并安全保存。

### 国际平台

1. 登录 [MiniMax API Platform](https://platform.minimax.io/)；
2. 打开 [Token Plan](https://platform.minimax.io/subscribe/token-plan)；
3. 购买套餐、Credits 或确认 Team 席位；
4. 前往 API Keys；
5. 创建 **Token Plan Key**；
6. 复制新 Key 并安全保存。

{% hint style="danger" %}
不要把 Token Plan Key 写入聊天、文档、代码仓库或问题截图。Key 泄露后可能消耗订阅额度或 Credits；应立即在 MiniMax 平台删除并重新创建。
{% endhint %}

只看 `sk-cp` 前缀不足以证明 Key 可用。还要确认订阅有效、席位已分配、Credits 可用，并且 Key 来自正确平台。

## 在 Cherry Studio 配置

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 中国大陆账号选择 **MiniMax**，国际账号选择 **MiniMax Global**；
4. 在 API Key 中粘贴 Token Plan Key；
5. 检查 Base URL 是否与账号平台匹配；
6. 打开页面顶部的服务商开关；
7. 点击**添加**或同步模型；
8. 检查同步预览并应用变更；
9. 只启用套餐当前允许使用的模型；
10. 运行模型健康检查。

Cherry Studio 的 MiniMax 预设同时保留 OpenAI 与 Anthropic 兼容地址。普通对话默认使用 OpenAI 兼容链路，部分 Code Tools 可以使用 Anthropic 兼容链路。

更多协议、视觉、思考、MCP 和 PDF 边界请参阅 [MiniMax](minimax.md)。

## 选择模型

Cherry Studio V2 当前的 MiniMax 预设包含：

- `MiniMax-M3`
- `MiniMax-M2.7`
- `MiniMax-M2.7-highspeed`

MiniMax Token Plan 的可用模型会随套餐和产品升级变化。以订阅页面、账户用量页和实际模型同步结果为准。

建议：

1. 优先测试当前套餐主推的 `MiniMax-M3`；
2. 需要兼容旧工作流时再测试 `MiniMax-M2.7`；
3. 只有套餐明确包含高速模型时，才使用 `MiniMax-M2.7-highspeed`；
4. 不要手动添加旧版 `MiniMax-M2.1` 并假定仍包含在套餐中；
5. 同名模型在 Token Plan 与按量 API 下可能有不同额度规则。

{% hint style="warning" %}
模型出现在 Cherry Studio 预设或同步列表中，不代表你的 Token Plan 一定包含它。最终权限由 MiniMax 服务端判断。
{% endhint %}

## 思考、视觉与 MCP

### 思考

MiniMax M 系列会返回思考内容。Cherry Studio 需要保留多轮对话中的思考块和工具调用信息，才能维持后续请求的上下文连续性。

如果修改思考选项后返回参数错误，先恢复为**默认**并重试。Token Plan Key 不会改变模型本身接受的参数。

### 视觉

Token Plan 已扩展到多模态模型，但 Cherry Studio 当前能否直接发送图片，还取决于具体模型 ID 和 V2 的能力识别。

同步后确认模型显示图片能力，再用小图片测试。若 `MiniMax-M3` 的视觉能力尚未被当前 V2 正确识别，不要只修改显示名称绕过限制。

### MCP

Cherry Studio MCP 使用模型的 Tool Calling。MiniMax Token Plan 另外提供官方 Web Search 和 Understand Image MCP，但它们与 Cherry Studio 自己配置的 MCP 服务器不是同一个概念。

使用 Cherry Studio MCP 时：

1. 先完成普通对话；
2. 只启用一个简单工具；
3. 检查模型是否真正产生结构化调用；
4. 再增加更多工具。

需要 MiniMax 官方 Token Plan MCP 时，应按官方指南单独配置，并注意它会消耗对应套餐资源。

## 查看用量

最可靠的方式是打开 MiniMax 平台的 Token Plan 或订阅管理页面，查看：

- 当前套餐或 Team 席位；
- 剩余额度与 Credits；
- 各模型用量；
- 滚动窗口恢复时间；
- 周期额度；
- 高速模型资格；
- 订阅到期时间。

不要只根据 Cherry Studio 的成功请求数估算余量。长上下文、视觉、生成类模型和不同模型可能使用不同额度池。

## 限额与 429

Token Plan 可能同时存在：

- RPM / TPM 短期限流；
- 5 小时滚动窗口；
- 周额度；
- 多模态模型的独立额度；
- 高峰期动态限流；
- 套餐并发限制。

因此，`429 Too Many Requests` 不一定表示整个订阅额度已耗尽。

排查顺序：

1. 暂停一分钟后重试；
2. 查看 Token Plan 用量页；
3. 检查滚动窗口和周额度；
4. 减少并发、长上下文和自动重试；
5. 确认没有多人共享同一个个人 Key；
6. 必要时升级套餐或改用按量 API Key。

在同一个服务商中直接替换为普通 API Key，会改变额度和计费来源。操作前先确认账户余额与预算。

## 常见问题

### 返回 401

Key 错误、已删除、订阅到期、席位失效，或中国大陆与国际 Base URL 混用。重新从对应平台复制 Token Plan Key。

### 返回 403

当前套餐、Team 策略或模型权限不允许该请求。检查 Token Plan 权益和模型范围。

### 返回 404

Base URL、协议路径或模型 ID 错误。恢复 MiniMax / MiniMax Global 预设地址，并重新同步模型。

### 返回 429

可能是分钟级限流、滚动窗口、周额度或高峰期动态限流。以 Token Plan 用量页为准，不要只反复发送请求。

### 普通模型可用，高速模型不可用

当前套餐可能不包含高速权益，或高速资源在当时不可用。改用标准模型并检查套餐说明。

### 模型列表仍显示旧模型

重新同步并检查服务商是否连接到正确平台。手动保留的旧模型不会自动代表当前套餐支持。

### Key 检测成功，但对话消耗了余额

可能填入了普通按量 API Key，而不是 Token Plan Key。立即检查 MiniMax 账单与 Key 类型。

### 用于生产后频繁限流

Token Plan 面向个人交互和开发工作流。生产、批量或高并发服务应改用按量 API，并设置预算、监控和重试策略。

MiniMax Token Plan 当前套餐、模型和用量规则请参阅[中国大陆文档](https://platform.minimaxi.com/docs/token-plan/quickstart)或[国际文档](https://platform.minimax.io/docs/token-plan/quickstart)。一般服务商配置请参阅 [MiniMax](minimax.md)和[模型服务设置](../settings/providers.md)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
