---
icon: file-lines
---

# 贡献文档

Cherry Studio 社区版文档由 Markdown 仓库维护，并通过 GitBook 展示。你可以通过 GitHub Pull Request 贡献，也可以在获得编辑权限后通过 GitBook Change Request 修改。

* 文档仓库：[CherryHQ/cherry-studio-docs](https://github.com/CherryHQ/cherry-studio-docs)
* 产品代码：[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)
* 对外文档：[docs.cherryai.com.cn](https://docs.cherryai.com.cn/)

批量更新、多语言修改和需要代码事实核对的页面，优先使用 GitHub；少量文案调整或需要可视化评论时，可以使用 GitBook。

## 开始前先确认范围

提交前回答四个问题：

1. 修改的是已有页面，还是需要新增页面？
2. 内容对应 Cherry Studio 的哪个版本或 `main` 中的哪项行为？
3. 哪些语种可以由提交者可靠校验？
4. 是否需要产品截图，截图能否补充文字无法说明的信息？

如果内容涉及当前功能、设置名称、模型能力或数据路径，应先在产品 `main` 代码和实际界面中核对。不要只复制旧文档、第三方文章或模型生成结果。

## 文档结构

简体中文位于仓库根目录，其他公开语种位于：

| 语种 | 目录 | 目录文件 |
| :--- | :--- | :--- |
| 简体中文 | 仓库根目录 | `SUMMARY.md` |
| 中文（繁體） | `i18n/traditional-chinese/` | `i18n/traditional-chinese/SUMMARY.md` |
| English | `i18n/english/` | `i18n/english/SUMMARY.md` |
| 日本語 | `i18n/japanese/` | `i18n/japanese/SUMMARY.md` |
| Русский | `i18n/russian/` | `i18n/russian/SUMMARY.md` |

GitBook 默认使用根目录的 `README.md` 作为首页、`SUMMARY.md` 作为侧栏目录。每种语言都有独立目录和 `SUMMARY.md`，页面层级与名称应在对应语言中保持一致。

## 路径一：通过 GitHub 贡献

### 1. Fork 与克隆

在 GitHub fork 文档仓库，然后执行：

```bash
git clone https://github.com/YOUR_GITHUB_NAME/cherry-studio-docs.git
cd cherry-studio-docs
git remote add upstream https://github.com/CherryHQ/cherry-studio-docs.git
git fetch upstream
git switch -c docs/short-description upstream/main
```

### 2. 修改已有页面

保留原有文件路径，直接编辑对应 Markdown。随意移动或重命名文件会改变页面 URL；如果确实需要调整路径，应在 PR 中列出旧地址与新地址，由维护者确认重定向。

修改多个语种时，分别编辑各自目录中的文件。不要用简体中文正文覆盖其他语种，也不要让英文或日文页面继续引用中文界面截图。

### 3. 新增页面

新增页面至少包含：

1. 简体中文 Markdown 文件。
2. `SUMMARY.md` 中位于正确章节的入口。
3. 能够校验的其他语种页面与对应 `SUMMARY.md` 入口。
4. 页面使用的本地图片。
5. 从相关上级页面或相邻教程进入新页面的链接。

文件名使用稳定、可读的英文或现有目录风格。不要把日期、版本号或营销标题写入路径，除非页面本身只适用于该版本。

如果暂时不能可靠翻译某种语言，不要提交未经检查的机器翻译。请在 PR 描述中列出待补语种，方便维护者安排后续工作。

## 一页合格的产品文档

文档的结构取决于任务，但通常应包含：

* **用途**：读者完成后能得到什么。
* **前提**：需要的版本、模型、账户、文件或权限。
* **步骤**：使用当前界面名称，按真实操作顺序编写。
* **结果**：说明成功时看到什么、生成什么或保存在哪里。
* **边界**：平台差异、费用、隐私、数据发送和不可逆操作。
* **排错**：覆盖最常见且能实际判断的失败原因。
* **下一步**：链接到紧接着要使用的功能。

说明“为什么这样做”时应简短并服务于决策。不要加入写作过程、内部讨论、未经验证的背景或重复的产品宣传。

### 文案要求

* 标题和按钮名称以当前 UI 为准。
* 一个步骤只描述一个动作，结果紧跟在动作之后。
* 动态价格、模型名单和活动信息只在必要时出现，并标明以服务商当前页面为准。
* 不把兼容接口等同于完整功能支持。
* 不承诺第三方服务永久免费、永久可用或一定返回相同结果。
* 高风险操作写明备份、权限和回滚方式。
* API Key、Token、Cookie、个人路径和真实对话不得出现在正文或代码示例中。

## 截图规范

截图只用于定位入口、解释复杂状态或展示结果。文字已经足够清楚时，不需要为了“看起来完整”而增加截图。

### 尺寸与构图

Cherry Studio 桌面截图统一采用：

* 物理尺寸：`1920 × 1200`
* 宽高比：`16:10`
* DPR：`2`
* 同一页面中的截图保持相同窗口尺寸、裁切范围和视觉比例

不要把同一组截图做成一张超宽、一张接近方形。尽量保留完整的操作上下文，同时让目标控件清晰可见。

### 多语言

简体中文、繁體中文、English、日本語和 Русский 页面应使用对应语言的产品 UI。对话内容、助手名称、示例文件名和结果文字也应与页面语言匹配。

如果某个界面在目标语言中确实没有翻译，应在 PR 中说明产品现状，不要用另一语言的截图假装已经本地化。

### 隐私与文件

* 使用虚构账户、助手、目录和对话内容。
* 隐藏 API Key、Token、邮箱、用户名、个人目录和通知。
* 不使用包含真实用户数据的数据库或知识库。
* 图片存入 `.gitbook/assets/`，使用唯一且有意义的文件名。
* 在 Markdown 中使用相对路径，并添加描述图片用途的 alt 文本。
* 不引用带时效签名的临时下载 URL、私有飞书链接或本机绝对路径。

推荐 PNG 或 WebP。截图应保持清晰，但避免保存无意义的大面积空白和不必要的超大文件。

## Markdown 与 GitBook

仓库使用常见 Markdown，并包含 GitBook 提示块和图片块。修改时应沿用附近页面的写法。

### 内部链接

使用相对路径：

```markdown
[智能体](../advanced-basic/agent.md)
```

目录首页可以链接到目录或 `README.md`，但要先确认目标文件存在。不要复制现网完整 URL 来替代仓库内页面链接，否则分支 Preview 和多语言路径容易跳回生产站。

### 提示块

只在信息确实需要突出时使用：

```markdown
{% hint style="warning" %}
执行前先备份数据。
{% endhint %}
```

同一页面不要堆叠大量提示块。普通步骤和补充说明直接使用段落或列表。

### 目录文件

`SUMMARY.md` 决定 GitBook 侧栏层级。新增、移动或改名页面时，应同步检查对应语种的 `SUMMARY.md`：

```markdown
* [Agent 案例](advanced-basic/agent-an-li/README.md)
  * [黄金市场复盘 Agent](advanced-basic/agent-an-li/gold-price-case.md)
```

同一个 Markdown 文件不能在同一份 `SUMMARY.md` 中重复引用。

## 本地检查

提交前至少执行：

```bash
git status --short
git diff --check
git diff -- SUMMARY.md
```

并人工确认：

* 所有新增 Markdown 和图片已被 Git 跟踪。
* `SUMMARY.md` 中的路径存在，缩进层级正确。
* 页面中的相对链接和图片路径存在。
* 五种语言没有互相串入正文或截图。
* 代码块、提示块和 frontmatter 均已闭合。
* 没有临时 URL、真实密钥、个人目录和编辑器生成的重复文件。

可以在 GitHub 中检查 Markdown 排版，但 GitHub 与 GitBook 的渲染并不完全相同。复杂提示块、图片尺寸、侧栏层级和页面跳转应在 GitBook Preview 中再核对。

## 创建 Pull Request

提交并推送分支：

```bash
git add path/to/page.md SUMMARY.md .gitbook/assets/
git commit -m "docs(section): update page title"
git push -u origin docs/short-description
```

PR 描述至少包含：

* 修改或新增了哪些页面。
* 对应的产品版本、代码位置或官方来源。
* 已完成和待补的语种。
* 新增或替换了哪些截图。
* 已执行的链接、结构和视觉检查。
* 页面路径或侧栏是否发生变化。

PR 尚未准备好时可以创建 Draft。维护者确认正文、事实、图片和语言后再合并。

## Preview 与正式发布

文档仓库连接 GitBook 后，GitHub 与 GitBook 可以双向同步，但**同步仓库和分支由 GitBook 管理员设置**。提交 PR 不会立即修改正式文档。

满足 GitBook 配置条件时，PR 中会出现带 Preview URL 的状态检查。需要注意：

* Preview 通常要求访问者登录 GitBook。
* 出于安全原因，fork 创建的 PR 默认可能不生成 Preview；管理员可以更改此设置。
* 站点未发布或使用特定访问限制时，Preview 也可能不可用。

因此，不要在 PR 描述中承诺任何人都能打开 GitBook Preview。没有自动 Preview 时，由维护者提供审核环境或在合并前使用内部预览。

PR 合并到 GitBook 当前连接的分支后，提交才会进入 GitBook 同步和发布流程。合并权限与正式发布由维护者控制。

GitBook 官方参考：

* [Git Sync](https://gitbook.com/docs/integrations/git-sync)
* [GitHub Pull Request Preview](https://gitbook.com/docs/getting-started/git-sync/github-pull-request-preview)
* [README 与 SUMMARY 配置](https://gitbook.com/docs/getting-started/git-sync/content-configuration)

## 路径二：通过 GitBook 编辑

需要 GitBook 编辑权限时，可以邮件联系 `support@cherry-ai.com`，标题写“申请 Cherry Studio Docs 编辑身份”，并说明：

* GitBook 账户邮箱。
* 希望维护的章节和语种。
* 相关文档或产品经验。
* 计划进行的修改。

获得权限后，在 GitBook 中创建 Change Request，而不是直接修改已发布内容。完成自检后邀请维护者 Review；Change Request 合并时，GitBook 会按管理员配置把改动同步到对应 Git 分支。

批量修改、跨语言重构或大量图片替换仍建议使用 GitHub 分支，便于逐文件审阅和自动检查。

## Review 后如何处理

维护者可能要求修正事实、减少截图、补充来源或统一语言。更新时：

1. 只修改反馈涉及的范围。
2. 保持五个语种结构一致。
3. 截图变化后重新检查语言、尺寸与隐私。
4. 回复说明修改内容和验证结果。

文档合并后若发现问题，继续用新的 PR 修复，不要通过删除历史或直接覆盖正式分支隐藏错误。

代码贡献请阅读[贡献代码](code.md)。不确定问题应写到哪里时，可先查看[反馈与建议](../question-contact/suggestions.md)。
