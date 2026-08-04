# 💡 问题反馈与功能建议

Cherry Studio 提供三种反馈方式：由 Cherry Assistant 引导提交、前往 GitHub Issue、中文界面的反馈问卷。入口是【设置】→【关于我们】→【反馈】。

<figure><img src="../.gitbook/assets/clipboard (8).png" alt="Cherry Studio 反馈方式选择，Agent 提交为推荐入口"><figcaption><p>不确定该怎样整理问题时，优先选择【使用 Agent 提交】。</p></figcaption></figure>

## 选哪一种

| 方式             | 适合情况               | 会发生什么                                  |
| -------------- | ------------------ | -------------------------------------- |
| 【使用 Agent 提交】  | 不确定问题类型、希望自动整理信息   | Cherry Assistant 诊断、脱敏预览，并在确认后提交或生成诊断包 |
| 【GitHub Issue】 | 已确认要公开跟踪 Bug 或功能建议 | 打开官方 Issue 类型选择页                       |
| 【反馈问卷】         | 中文用户提交一般反馈         | 打开官方飞书问卷                               |

## 推荐：使用 Agent 提交

{% stepper %}
{% step %}
### 1. 打开【设置】→【关于我们】→【反馈】

选择带有【推荐】标记的【使用 Agent 提交】。
{% endstep %}

{% step %}
### 2. 描述问题或建议

说明目标、实际结果、期望结果和复现步骤。Cherry Assistant 会先检查当前安装包信息，并按需要请求读取错误、日志、MCP 状态或模型连接。
{% endstep %}

{% step %}
### 3. 决定是否提供诊断

只授权与问题相关的项目。Cherry Assistant 会遮挡凭据并展示预览；确认内容无误后再提交。
{% endstep %}

{% step %}
### 4. 选择提交结果

默认反馈流程走官方反馈渠道，也可以生成诊断 ZIP 留给你手动发送。若明确要公开到 GitHub，请直接说“提交 GitHub Issue”。
{% endstep %}
{% endstepper %}

## 提交 GitHub Issue

Bug 报告应包含平台、当前版本、问题描述、复现步骤、期望结果和相关日志；功能建议应先讲清当前痛点，再说明期望方案和考虑过的替代办法。

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>创建 Issue</strong></td><td>选择 Bug、功能建议或讨论模板</td><td><a href="https://github.com/CherryHQ/cherry-studio/issues/new/choose">https://github.com/CherryHQ/cherry-studio/issues/new/choose</a></td></tr><tr><td><strong>搜索已有 Issue</strong></td><td>查看是否已有相同问题</td><td><a href="https://github.com/CherryHQ/cherry-studio/issues">https://github.com/CherryHQ/cherry-studio/issues</a></td></tr><tr><td><strong>Discussions</strong></td><td>用法讨论和开放问题</td><td><a href="https://github.com/CherryHQ/cherry-studio/discussions">https://github.com/CherryHQ/cherry-studio/discussions</a></td></tr></tbody></table>

{% hint style="danger" %}
GitHub Issue 是公开内容。不要上传 API Key、机器人 Token、完整诊断包、私人聊天、公司数据或未脱敏日志。需要私密诊断时优先使用应用内 Agent 反馈流程。
{% endhint %}

## 功能建议怎样更容易理解

* 先写正在做的工作，而不是先写按钮位置；
* 说明现有方案为什么不够；
* 给出期望结果和成功标准；
* 附上界面草图或相似体验时标明参考重点；
* 说明是否有临时替代方法；
* 避免把多个无关建议放进同一个 Issue。

<details>

<summary>提交后多久会处理？</summary>

处理时间取决于问题影响、复现难度、维护计划和可用资源。补充稳定复现、脱敏日志和明确用户影响，比重复催促更有帮助。

</details>
