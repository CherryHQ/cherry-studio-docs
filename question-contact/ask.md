---
icon: messages-question
---

# 如何高效提问

一份信息完整的问题说明，通常能更快得到有效回答。提交前请先搜索文档和已有 Issue，再按下面的清单整理信息。

## 提问前先检查

1. 在文档顶部搜索框输入错误码或功能名称。
2. 查看 [常见问题](questions.md) 是否已有解决方法。
3. 到 [GitHub Issues](https://github.com/CherryHQ/cherry-studio/issues) 搜索相同报错。
4. 如果是模型接口问题，先检查 Provider 的 API Key、余额、模型权限和官方状态。

## 问题描述模板

复制下面的模板，并删除不适用的项目：

```text
问题标题：

Cherry Studio 版本：
操作系统与版本：
使用的功能：
Provider 与模型：

期望结果：
实际结果：

复现步骤：
1.
2.
3.

是否每次都能复现：
完整错误信息：
已经尝试过的方法：
```

## 截图和日志要包含什么

* 保留模型名称、错误码、关键参数和完整报错；
* 截图要覆盖发生问题的界面，不要只截弹窗的一小部分；
* 必要时附上 [控制台错误信息](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)；
* 偶发问题请说明发生时间、操作顺序和当时的网络环境。

{% hint style="warning" %}
提交前请遮盖 API Key、访问令牌、邮箱、文件路径中的真实姓名、对话隐私和公司内部信息。不要为了展示错误而公开完整密钥。
{% endhint %}

## 到哪里提问

* [Telegram 频道](https://t.me/CherryStudioAI)
* [Discord 社区](https://discord.com/invite/wez8HtpxqQ)
* QQ 群：`611659451`
* [GitHub Issues](https://github.com/CherryHQ/cherry-studio/issues)：适合可复现的产品 Bug 和明确的功能建议

如果是软件 Bug，请优先提交可复现步骤、平台、软件版本和完整错误信息。模型回答质量、计费、额度或服务商账户问题，通常需要联系对应 Provider。

{% hint style="success" %}
**文档问题或改进建议**

可以联系 Telegram `@Wangmouuu`、QQ `1355873789`，或发送邮件至 `sunrise@cherry-ai.com`。
{% endhint %}
