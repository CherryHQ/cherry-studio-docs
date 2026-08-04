---
description: Code CLI、API 网关与调用链
---

# 🧑‍💻 开发与诊断

这一组功能面向需要使用编程命令行、让其他本机程序调用模型，或排查请求问题的用户。日常聊天和内容工作不需要开启开发者模式。

## 三个入口

| 入口                | 用途                           | 使用前先确认          |
| ----------------- | ---------------------------- | --------------- |
| 【编码搭档】            | 安装、配置并启动常见 Code CLI          | 工具来源、账号、模型与工作目录 |
| 【设置】→【API 网关】     | 向本机程序提供兼容 API，也是 Agent 的运行依赖 | 状态、端口与密钥安全      |
| 【设置】→【系统】→【开发者模式】 | 查看调用链，定位模型与工具错误              | 日志中可能含敏感内容      |

<figure><img src="../../.gitbook/assets/clipboard (7).png" alt="API 网关的运行状态、地址、端口和密钥区域"><figcaption><p>API 网关页面集中显示运行状态、地址、端口和凭据。</p></figcaption></figure>

{% hint style="warning" %}
API 网关的密钥、调用链中的请求内容和 Code CLI 的工作目录都可能涉及敏感信息。截图、Issue 和群聊中只分享已遮挡的必要片段。
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>💻 编码搭档（Code CLI）</strong></td><td>管理安装来源、模型连接和启动目录</td><td><a href="https://app.gitbook.com/o/Cj2FUNM601oTkFwFFsXJ/s/0Ut5BptC3t8CtSU1UWpM/advanced-basic/developer-tools/code-cli">https://app.gitbook.com/o/Cj2FUNM601oTkFwFFsXJ/s/0Ut5BptC3t8CtSU1UWpM/advanced-basic/developer-tools/code-cli</a></td></tr><tr><td><strong>🌉 API 网关</strong></td><td>理解 Agent 依赖与本机 API 调用</td><td><a href="https://app.gitbook.com/o/Cj2FUNM601oTkFwFFsXJ/s/0Ut5BptC3t8CtSU1UWpM/advanced-basic/developer-tools/api-gateway">https://app.gitbook.com/o/Cj2FUNM601oTkFwFFsXJ/s/0Ut5BptC3t8CtSU1UWpM/advanced-basic/developer-tools/api-gateway</a></td></tr><tr><td><strong>🔎 调用链与开发者模式</strong></td><td>复现并定位一次具体请求</td><td><a href="https://app.gitbook.com/o/Cj2FUNM601oTkFwFFsXJ/s/0Ut5BptC3t8CtSU1UWpM/advanced-basic/developer-tools/trace">https://app.gitbook.com/o/Cj2FUNM601oTkFwFFsXJ/s/0Ut5BptC3t8CtSU1UWpM/advanced-basic/developer-tools/trace</a></td></tr></tbody></table>
