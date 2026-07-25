---
icon: file-lines
---

# 贡献文档

Cherry Studio 社区文档存放在 [CherryHQ/cherry-studio-docs](https://github.com/CherryHQ/cherry-studio-docs)。正文、图片和目录结构的修改都应通过分支与 Pull Request 提交，以便预览、审阅和追溯。

## 推荐流程

1. Fork 文档仓库，并从最新 `main` 创建独立分支。
2. 在 Markdown 中完成修改；图片放入 `.gitbook/assets`，使用相对路径引用。
3. 核对页面中的入口名称、操作路径和截图是否与当前版本一致。
4. 本地检查内部链接、图片路径和 Markdown 格式。
5. 向 `CherryHQ/cherry-studio-docs:main` 提交 Pull Request，并在说明中列出修改范围、验证版本和截图状态。
6. 等待 Review 与 Preview 验证。未经维护者确认，不要自行宣称内容已经发布。

## V2 文档要求

* 功能事实以 Cherry Studio V2 最新代码和实际界面为准。
* 操作步骤应写明入口、前置条件、成功结果和常见问题。
* 不要在正文或截图中包含 API Key、访问令牌、本地用户名、私人路径或其他敏感信息。
* 模型列表、价格、下载版本等动态信息应注明日期，并尽量链接官方来源。
* 旧版行为若已移除，应明确标注，避免继续给出不可执行的操作。

## 获取协作权限

仅提交 PR 不需要 GitBook 编辑权限。若确实需要进入 GitBook 工作区，可邮件联系 `support@cherry-ai.com`：

* 标题：申请 Cherry Studio Docs 编辑身份
* 正文：说明 GitHub 账号、申请理由和计划维护的页面

详细问题和功能建议请使用[反馈与建议](../question-contact/suggestions.md)中的官方渠道。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../question-contact/suggestions.md) 中提供的官方渠道。
