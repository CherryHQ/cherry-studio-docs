---
icon: file-signature
---

# 反馈与建议

选择合适的渠道并提供可复现的信息，能显著提高问题被确认和处理的速度。

## 先选择反馈渠道

| 需求 | 推荐渠道 | 适合提交的内容 |
| :--- | :--- | :--- |
| 软件故障 | [GitHub Bug Report](https://github.com/CherryHQ/cherry-studio/issues/new/choose) | 崩溃、功能异常、回归问题、界面错误 |
| 功能建议 | [GitHub Feature Request](https://github.com/CherryHQ/cherry-studio/issues/new/choose) | 新功能、交互改进、现有能力增强 |
| 使用讨论 | [GitHub Discussions](https://github.com/CherryHQ/cherry-studio/discussions) | 使用方法、经验分享、方案讨论 |
| 安全漏洞 | [GitHub Security Advisory](https://github.com/CherryHQ/cherry-studio/security/advisories/new) | 可能泄露数据、绕过权限或执行未授权操作的漏洞 |
| 无法使用 GitHub | [support@cherry-ai.com](mailto:support@cherry-ai.com) | 无法登录 GitHub，或不适合公开发送的普通支持信息 |

{% hint style="warning" %}
安全漏洞不要提交到公开 Issue，也不要在群聊中公开复现细节。请使用私密的 Security Advisory。
{% endhint %}

## 提交前先做四件事

1. 更新到最新稳定版，并确认问题仍能复现。
2. 查看[常见问题](questions.md)，排除配置、额度、网络和模型服务商问题。
3. 搜索现有的 [Open Issues](https://github.com/CherryHQ/cherry-studio/issues)、[Closed Issues](https://github.com/CherryHQ/cherry-studio/issues?q=is%3Aissue%20state%3Aclosed) 和 [Discussions](https://github.com/CherryHQ/cherry-studio/discussions)。
4. 删除截图、日志和配置中的 API Key、Token、Cookie、个人文件路径及对话隐私。

已有相同问题时，优先补充新的复现信息，而不是重复创建 Issue。

## 报告 Bug

### 标题

标题应包含**功能、平台和现象**，让维护者不打开正文也能大致判断问题。

```text
[Bug] macOS：知识库重新索引后一直显示处理中
```

不要只写“不能用”“有问题”或“求修复”。

### 必填信息

一份可处理的 Bug 报告至少应包含：

* Cherry Studio 版本。
* Windows、macOS 或 Linux 及系统版本。
* 涉及的功能、模型服务商和模型名称；不要提供 API Key。
* 可稳定复现的操作步骤。
* 实际结果与预期结果。
* 问题从哪个版本或操作后开始出现。
* 已尝试的排查方法。
* 必要的截图、录屏和脱敏日志。

版本信息可以在**设置 → 关于**中查看。应用日志可以在**设置 → 数据设置 → 数据 → 应用日志**中打开。

### 推荐模板

```markdown
## 环境

- Cherry Studio：
- 系统：
- 安装来源：
- 模型服务商 / 模型：

## 复现步骤

1.
2.
3.

## 实际结果


## 预期结果


## 补充信息

- 是否稳定复现：
- 从哪个版本开始：
- 已尝试：
- 脱敏日志 / 截图：
```

### 最小复现

如果问题与特定助手、知识库、MCP 或自定义 CSS 有关，先尝试缩小变量：

* 新建一个空白助手或话题。
* 暂时关闭无关的 MCP、技能和联网搜索。
* 使用一小段不敏感的测试内容。
* 记录“启用哪个设置后问题出现”。

最小复现比完整环境截图更容易定位根因。

## 提交功能建议

功能建议不只要描述“想要什么”，还应解释“现在遇到了什么问题”。

建议包含：

1. **使用场景**：谁在什么工作流中遇到问题。
2. **当前障碍**：现有功能为什么不能满足需求。
3. **期望结果**：理想操作和输出是什么。
4. **替代方案**：目前如何绕过，有哪些缺点。
5. **范围与边界**：哪些情况必须支持，哪些可以暂不支持。
6. **示意材料**：必要时提供脱敏截图、流程图或交互草图。

一个 Issue 尽量只讨论一个独立需求。多个无关需求放在同一条中，会增加范围确认和排期难度。

项目方向可以参考 [Cherry Studio Roadmap](https://github.com/orgs/CherryHQ/projects/7)。Roadmap 不代表交付承诺，具体范围和时间以项目维护者的最新说明为准。

## 提问与讨论

普通使用问题可以进入 [GitHub Discussions](https://github.com/CherryHQ/cherry-studio/discussions)。提问时请同时说明：

* 目标是什么。
* 当前配置和操作路径。
* 已经尝试了什么。
* 卡在哪一步。
* 希望得到哪种帮助。

问题中如果已经包含稳定复现的软件缺陷，应改用 Bug Report；需要跟踪实现状态的新需求，应改用 Feature Request。

## 报告安全问题

发现以下情况时，请使用 [GitHub Security Advisory](https://github.com/CherryHQ/cherry-studio/security/advisories/new) 私密报告：

* API Key、Token 或本地数据可能被非预期读取。
* 权限确认可以被绕过。
* 不受信任内容可能触发未授权命令或文件操作。
* 更新包、依赖或网络通信存在可利用风险。

报告应包含影响范围、复现步骤、必要的验证材料和可能的缓解方式。不要提交真实用户数据或仍在使用的凭据。

非漏洞类的安全咨询可联系 [security@cherry-ai.com](mailto:security@cherry-ai.com)。

## 社区交流

社区群适合交流经验和互助，不是正式的问题跟踪系统。需要维护者确认、关联版本或持续跟踪的问题，仍应提交到 GitHub。

* [Telegram：CherryStudioAI](https://t.me/CherryStudioAI)
* [Discord：Cherry Studio](https://discord.gg/wez8HtpxqQ)
* [QQ 群：575014769](https://qm.qq.com/q/lo0D4qVZKi)

群聊邀请可能因平台规则或人数限制发生变化。若链接失效，请以 [Cherry Studio 官方仓库](https://github.com/CherryHQ/cherry-studio) README 中的最新入口为准。

## 保护隐私

提交前请检查：

* API Key、访问令牌、Cookie 和密码已完全遮挡。
* 文件路径中的姓名、公司名和项目名已脱敏。
* 对话、知识库和文档中没有不必要的个人或业务数据。
* 日志只保留与问题时间段相关的内容。
* 截图没有显示其他应用、浏览器标签或通知中的敏感信息。

如果凭据已经公开，不要只删除帖子；应立即在对应服务商后台撤销并重新生成。
