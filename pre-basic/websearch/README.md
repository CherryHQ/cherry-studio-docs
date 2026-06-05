---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

# 联网模式

{% hint style="info" %}
联网模式让 AI 在回答前先去搜索最新内容，适合以下场景：

* **时效性信息**：今日 / 本周 / 刚刚发生的新闻、价格、汇率等
* **实时数据**：天气、股价、商品库存等动态数值
* **新兴知识**：刚出现的工具、概念、技术
{% endhint %}

## 如何开启联网

在对话输入框的工具栏中点击 🌐 **小地球** 图标，即可对当前对话开启联网。

<figure><img src="../../.gitbook/assets/image (94).png" alt=""><figcaption><p>点击地球图标开启联网</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (96).png" alt=""><figcaption><p>开启状态</p></figcaption></figure>

## 联网的两条技术路径

Cherry Studio 通过**两种方式**实现联网，根据你选的模型自动决定：

### 路径 1：模型自带联网功能（推荐）

部分大模型服务商在自家模型中**原生集成了搜索能力**。这类模型在模型名旁边会显示**小地球图标 🌐**。

开启对话联网后，AI 直接调用模型自身的搜索能力，**无需任何额外配置**。

<figure><img src="../../.gitbook/assets/image (100) (1).png" alt=""><figcaption><p>模型名后的小地球图标</p></figcaption></figure>

在 `设置 → 模型服务` 中也能据此区分。

<figure><img src="../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

**已知支持原生联网的模型 / 服务商**：

* Google Gemini（部分版本）
* OpenRouter（全部模型支持）
* 腾讯混元
* 智谱 AI
* 阿里云百炼（部分模型）
* xAI Grok

{% hint style="info" %}
还有少数模型即使没显示小地球图标，也能联网（取决于服务商配置）。例如 [火山引擎接入联网](volcengine.md) 中介绍的一类情况。
{% endhint %}

### 路径 2：通过外部搜索服务（用于不带联网功能的模型）

如果你选的模型本身不带联网（多数开源 / 经典模型都如此），Cherry Studio 会**调用配置好的外部搜索服务**，把搜索结果作为上下文喂给模型。

打开 `设置 → 网络搜索` 添加并启用任意一家搜索服务。Cherry Studio 内置支持：

| 搜索服务 | 类型 | 备注 |
|---|---|---|
| **Tavily** | 云端 | 老牌、免费额度足够日常用 [→ 注册教程](tavily.md) |
| **Bocha (博查)** | 云端 | 国内访问友好，中文场景效果好 |
| **Exa** | 云端 | 偏学术 / 技术内容 |
| **Exa MCP** | 云端 | Exa 的 MCP 接口版 |
| **Zhipu (智谱)** | 云端 | 智谱自家的搜索 API |
| **Querit** | 云端 | 国内访问友好 |
| **SearXNG** | 自部署 | 开源元搜索引擎，可完全本地化 [→ 部署教程](searxng.md) |
| **Google / Bing / Baidu** | 本地浏览器 | 直接打开浏览器搜索页，**不读取内容回传给 AI**，仅作为辅助查找 |

#### 首次启用 Tavily（最常见的零配置选择）

1. 在对话框点击 🌐 后，若发现尚未配置任何外部搜索服务，会弹窗提示
2. 点击 **去设置** → 进入网络搜索配置
3. 选择 Tavily，点击 **获取秘钥** 跳转 Tavily 官网注册
4. 在 Tavily 控制台创建 API Key
5. 复制 Key 回填到 Cherry Studio

<figure><img src="../../.gitbook/assets/image (102) (1).png" alt=""><figcaption><p>弹窗：去设置</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (103).png" alt=""><figcaption><p>点击获取秘钥</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (103) (1).png" alt=""><figcaption><p>跳转获取秘钥</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (105).png" alt=""><figcaption><p>复制 API Key</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (108).png" alt=""><figcaption><p>回填 API Key</p></figcaption></figure>

详细注册流程见 [Tavily 联网登录注册教程](tavily.md)。

{% hint style="warning" %}
Tavily 免费额度有每月调用次数限制，超出后需付费。如长期重度使用建议改用 [SearXNG 本地部署](searxng.md) 或 Bocha 等其他方案。
{% endhint %}

## 搜索结果黑名单

不想让某些不靠谱的网站出现在搜索结果里？参考 [网络搜索黑名单配置](blacklist.md) 把它们屏蔽掉。

## 免费联网模式

如果你不想花一分钱也想用上搜索能力，看 [免费联网模式](mian-fei-lian-wang-mo-shi.md)。

## 工作机制

无论走哪条路径，对话流程都是：

1. 你问"今天上海天气怎么样？"
2. Cherry Studio 把问题先发给搜索服务
3. 搜索服务返回 N 条相关网页摘要
4. Cherry Studio 把这些摘要拼到提示词里发给 AI 模型
5. AI 基于实时数据回答你

<figure><img src="../../.gitbook/assets/image (107).png" alt=""><figcaption><p>联网搜索结果示例</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (106).png" alt=""><figcaption><p>联网回答示例</p></figcaption></figure>

> 如发现错误或有改进建议，欢迎到 [反馈与建议](../../question-contact/suggestions.md) 提交。
