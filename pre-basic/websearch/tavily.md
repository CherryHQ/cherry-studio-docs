---
description: 在 Cherry Studio V2 中配置 Tavily，获得稳定的关键词网络搜索能力。
icon: magnifying-glass
---

# Tavily 网络搜索

Tavily 是面向 AI 应用的网络搜索服务。在 Cherry Studio V2 中，它负责根据关键词查找网页，并把标题、摘要和链接交给模型生成回答。

{% hint style="info" %}
Tavily 在当前版本中是**关键词搜索服务商**，不能代替网页读取服务。若希望模型继续读取某个结果页的完整内容，还需另外设置默认的 URL 读取服务商，例如 Fetch 或 Jina。
{% endhint %}

## 使用前准备

配置 Tavily 需要：

- 一个可正常使用的 Tavily 账号；
- 一枚 Tavily API Key；
- Cherry Studio 中至少一个可对话的模型；
- 如需读取具体网页，再配置一个 URL 读取服务商。

Tavily 按 API Credits 计量使用。免费额度、付费方案和调用限制可能调整，请以 [Tavily Pricing](https://www.tavily.com/pricing) 和控制台中的实时信息为准。

## 获取 API Key

1. 打开 [Tavily Platform](https://app.tavily.com/home)。
2. 按页面提示注册或登录账号。
3. 在控制台的 API Keys 区域创建或找到可用的 Key。
4. 复制 Key，准备粘贴到 Cherry Studio。

Tavily 的注册和验证流程可能随时间变化，因此本文不固定描述验证码、双重验证或第三方登录界面。遇到差异时，请以 Tavily 当前页面提示为准。

{% hint style="danger" %}
API Key 相当于账号凭证。不要把真实 Key 放进截图、聊天记录、公开文档或代码仓库；怀疑泄露时，应立即在 Tavily 控制台撤销旧 Key并创建新 Key。
{% endhint %}

## 在 Cherry Studio 中配置

### 1. 打开网络搜索设置

进入：

> **设置 → 网络搜索**

在服务商列表中找到 **Tavily**。

### 2. 填写 API Key

把 Tavily 控制台中的 Key 粘贴到 **API 密钥**输入框。

如果已经保存过多枚 Key，可以在 Key 列表中切换或管理。多 Key 适合轮换凭证，但不会增加单个 Tavily 账号的总额度。

### 3. 检查 API Host

默认 API Host 为：

```text
https://api.tavily.com
```

通常保留默认值即可。只有在使用兼容的代理或网关时才需要修改；自定义地址必须能够兼容 Tavily 的 `/search` 接口和 Bearer 鉴权。

{% hint style="warning" %}
错误的 API Host、重复拼接 `/search`、代理未透传 `Authorization` 请求头，都会导致连接检测或实际搜索失败。
{% endhint %}

### 4. 检测配置

点击 Tavily 卡片中的**检查**按钮。

- 检查成功：说明当前 API Host 和 Key 可以完成基本请求；
- 检查失败：先核对 Key、Host、网络代理和 Tavily 账号状态，再查看下方故障排查。

### 5. 设为默认关键词搜索服务商

将 Tavily 设为**默认搜索服务商**。Cherry Studio 在需要外部关键词搜索时会使用它。

如果还需要模型打开搜索结果中的网页，请同时选择默认的 **URL 读取服务商**。常见组合为：

| 用途 | 推荐选择 |
| --- | --- |
| 关键词搜索 | Tavily |
| URL 读取 | Fetch 或 Jina |

搜索服务商与 URL 读取服务商是两个独立设置，只配置 Tavily 并不代表应用能够读取任意网页全文。

## 调整通用搜索设置

Cherry Studio 的网络搜索设置会统一作用于 Tavily 等外部服务商。

### 最大结果数

可设置每次搜索返回的最大结果数。结果越多，模型可参考的信息通常越丰富，但搜索耗时、上下文长度和 API 用量也可能增加。

建议先使用默认值；回答缺少来源时再逐步增加。

### 搜索结果压缩

可以根据任务选择不压缩或截断搜索结果。压缩有助于减少上下文占用，但过度截断可能丢失关键细节。

### 网络搜索黑名单

黑名单会在 Tavily 返回结果后，由 Cherry Studio 过滤不希望使用的网址。配置方法见[网络搜索黑名单](blacklist.md)。

{% hint style="info" %}
当前 Cherry Studio 的 Tavily 适配器只向 Tavily 发送查询内容和最大结果数。Tavily 官方 API 提供的 `search_depth`、`topic`、`include_domains`、`exclude_domains`、`include_answer` 等高级参数，暂未在 V2 设置界面中单独开放。
{% endhint %}

## 在对话中使用

1. 打开一个助手或新对话。
2. 选择要使用的模型。
3. 点击输入框附近的**地球图标**，开启网络搜索。
4. 输入需要最新资料或外部来源的问题并发送。
5. 检查回答中的来源编号和链接。

例如：

```text
请搜索 Cherry Studio 最近一个正式版本的更新内容，
按功能分类总结，并在每项结论后标注来源。
```

如果模型本身支持原生联网，Cherry Studio 会优先按照该模型的能力处理；对于没有原生联网能力、但支持工具调用的模型，Tavily 可作为外部关键词搜索服务商使用。

有关两类联网方式的区别，见[网络搜索](README.md)。

## 当前集成能力

| 能力 | 当前 V2 支持情况 |
| --- | --- |
| 关键词搜索 | 支持 |
| 返回网页标题、摘要和 URL | 支持 |
| 设置最大结果数 | 支持，使用通用网络搜索设置 |
| 多枚 API Key | 支持 |
| 自定义 API Host | 支持 |
| 读取指定 URL 的正文 | 不支持，需配置 Fetch 或 Jina |
| Tavily Search 高级参数 | 暂未在界面开放 |
| Tavily Extract、Crawl、Map、Research | 当前 Tavily 适配器未接入 |

Cherry Studio 当前向 Tavily 的 `/search` 接口发起请求，并使用 Bearer API Key 鉴权。有关接口能力可参考 [Tavily Search API](https://docs.tavily.com/documentation/api-reference/endpoint/search)。

## 常见问题

### 检查按钮提示认证失败

通常与 API Key 有关：

1. 重新从 Tavily 控制台复制 Key，避免多余空格；
2. 确认 Key 尚未被撤销；
3. 确认当前账号或团队仍允许使用该 Key；
4. 如怀疑泄露，撤销旧 Key 后创建新 Key。

### 提示额度不足或请求过于频繁

检查 Tavily 控制台中的 Credits、账单和速率限制。等待额度恢复、降低搜索频率，或按实际需要调整方案。

不要通过持续重试绕过限制；这会产生更多无效请求。

### 检查成功，但对话没有联网

依次确认：

- Tavily 已设为默认关键词搜索服务商；
- 当前对话的地球图标已开启；
- 当前模型支持工具调用，或本身支持原生联网；
- 问题确实需要外部搜索；
- 没有被助手设置或模型设置禁用工具。

### 有搜索结果，但模型无法读取网页详情

Tavily 在当前版本中只负责关键词搜索。请再把 Fetch 或 Jina 设为默认 URL 读取服务商，然后重试。

### 搜索结果为空或不够相关

可以：

- 把问题改写成明确的搜索关键词；
- 补充时间、地区、产品名或版本号；
- 适度提高最大结果数；
- 检查黑名单是否误过滤了目标网站；
- 对重要结论换一个搜索词再次核对。

### 自定义 API Host 后失败

恢复默认地址：

```text
https://api.tavily.com
```

如果必须使用代理或网关，确认它：

- 支持 `POST /search`；
- 能透传 Bearer 鉴权；
- 返回与 Tavily Search API 兼容的 JSON；
- 没有额外拼接或删除路径。

## 安全、隐私与准确性

- 搜索词会发送给 Tavily；不要在查询中包含密码、API Key、个人隐私或未公开的业务数据。
- 网络结果可能过时、错误或互相矛盾。涉及医疗、法律、财务等高风险结论时，应打开原始来源并进行人工核验。
- Tavily 的额度和计费由服务商管理。大量使用前，先在控制台确认当前方案和消耗规则。
- 定期轮换不再需要的 Key；泄露处理可参考 [Tavily API Key Management](https://docs.tavily.com/documentation/best-practices/api-key-management)。

## 相关文档

- [网络搜索](README.md)
- [免费联网模式](free-search.md)
- [网络搜索黑名单](blacklist.md)
- [Tavily Quickstart](https://docs.tavily.com/documentation/quickstart)

***

### 获取帮助与提交反馈

如果在配置或使用过程中遇到问题，请通过[反馈与建议](../../question-contact/suggestions.md)中列出的官方渠道提交反馈。反馈时建议说明 Cherry Studio 版本、模型名称、错误提示和是否使用代理，但不要附上真实 API Key。
