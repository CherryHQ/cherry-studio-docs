---
icon: square-code
---

# 贡献代码

Cherry Studio 接受功能、问题修复、测试、性能、可访问性和开发工具等代码贡献。当前 V2 的日常开发位于 `main` 分支；开始前请先确认问题、改动范围和验证方法。

项目仓库：[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

## 开始前

请先阅读：

* [贡献者指南](https://github.com/CherryHQ/cherry-studio/blob/main/CONTRIBUTING.md)
* [行为准则](https://github.com/CherryHQ/cherry-studio/blob/main/CODE_OF_CONDUCT.md)
* [开发指南](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/development.md)
* [项目开发约定](https://github.com/CherryHQ/cherry-studio/blob/main/CLAUDE.md)
* [开源许可协议](https://github.com/CherryHQ/cherry-studio/blob/main/LICENSE)

如果准备实现较大的功能、改变用户流程或重构公共接口，建议先搜索 [Issues](https://github.com/CherryHQ/cherry-studio/issues) 和现有 Pull Request。没有相关讨论时，先提交 Issue 说明问题、目标和方案，可减少重复工作和方向偏差。

适合第一次参与的任务可以从以下标签开始：

* [good first issue](https://github.com/CherryHQ/cherry-studio/labels/good%20first%20issue)
* [help wanted](https://github.com/CherryHQ/cherry-studio/labels/help%20wanted)
* [kind/bug](https://github.com/CherryHQ/cherry-studio/labels/kind%2Fbug)

## 选择正确分支

| 改动 | 基础分支 | PR 目标分支 |
| :--- | :--- | :--- |
| 当前功能、V2 开发、重构、优化和问题修复 | `main` | `main` |
| 已发布 V1 的最小维护修复 | `v1` | `v1` |

V1 修复不会自动进入 `main`。同一问题也存在于当前开发分支时，需要另开一个面向 `main` 的前向移植 PR。

不要直接向上游分支提交。先 fork 仓库，再从正确基础分支创建自己的短期功能分支。

## 准备开发环境

当前 `main` 在 `.node-version` 中固定 Node.js `24.11.1`，并在 `package.json` 中固定 pnpm `10.27.0`。这些版本会随仓库更新；每次开始工作都以你本地分支中的文件为准。

### Windows：先启用符号链接

仓库使用符号链接同步部分文件。Windows 用户应在克隆前：

1. 在系统设置中启用**开发人员模式**，或授予创建符号链接权限。
2. 执行：

```powershell
git config --global core.symlinks true
```

3. 再克隆仓库。已经在未启用符号链接时克隆的仓库，建议启用后重新克隆。

### Fork 与克隆

先在 GitHub 中 fork `CherryHQ/cherry-studio`，然后执行：

```bash
git clone https://github.com/YOUR_GITHUB_NAME/cherry-studio.git
cd cherry-studio
git remote add upstream https://github.com/CherryHQ/cherry-studio.git
git fetch upstream
git switch -c fix/short-description upstream/main
```

将 `YOUR_GITHUB_NAME` 和分支名替换为自己的值。功能分支可以使用 `feat/`，问题修复可以使用 `fix/`，文档改动可以使用 `docs/`。

### 安装 Node.js 与依赖

使用支持 `.node-version` 或 `.nvmrc` 的版本管理器安装仓库要求的 Node.js。例如：

```bash
nvm install
nvm use
corepack enable
corepack pnpm install
```

请通过 Corepack 使用仓库锁定的 pnpm，不要用其他全局 pnpm 重写 `pnpm-lock.yaml`。除非确实修改依赖，否则 PR 不应包含无关的锁文件变化。

### 创建本地环境文件

```bash
cp .env.example .env
```

`.env` 已被 Git 忽略。只填写本地开发需要的值，不要把真实 API Key、Token、Cookie 或其他凭据提交到代码、测试、日志和截图中。

### 启动应用

```bash
corepack pnpm dev
```

首次启动会先生成 OpenAPI 文件，再打开 Electron 开发实例。调试主进程或渲染进程时，可以使用：

```bash
corepack pnpm debug
```

如果依赖安装或启动失败，先核对 Node.js 与 pnpm 版本、确认锁文件没有被其他包管理器修改，再查看终端中的第一条错误。

## 开始修改

### 先理解局部约定

Cherry Studio 是包含 Electron 主进程、预加载层、React 渲染层和多个共享包的 monorepo。编辑某个目录前：

1. 阅读该目录及父目录中的 `README.md`。
2. 查看附近同类实现和测试。
3. 搜索 `@deprecated` 标记，避免继续扩展正在淘汰的接口。
4. 只修改解决当前问题所需的文件。

渲染层不应直接访问 Node.js API；需要跨进程能力时，应沿用 preload 与 IPC 边界。日志应使用项目的 `loggerService`，不要新增 `console.log`。

### 保持改动可测试

修复问题时，优先添加能复现问题的测试；新增行为时，为成功、失败和边界情况补充测试。项目使用 Vitest，并按区域提供测试命令：

```bash
corepack pnpm test:main
corepack pnpm test:renderer
corepack pnpm test:aicore
corepack pnpm test:shared
```

不必每次运行所有区域。开发中先运行与改动最接近的测试，提交前再运行完整检查。

### 用户可见文本

新增或修改界面文字时，应使用现有国际化机制，不要在组件中直接写只适用于一种语言的字符串。至少运行：

```bash
corepack pnpm i18n:check
corepack pnpm i18n:hardcoded:strict
```

需要同步新键时，先阅读仓库的[国际化指南](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/i18n.md)，再使用对应脚本。

### 数据库结构

修改 Drizzle Schema 时，应生成并提交对应迁移：

```bash
corepack pnpm db:migrations:generate
corepack pnpm db:migrations:check
```

如果 rebase 后迁移编号冲突，不要只改 SQL 文件名或手工编辑 snapshot。按仓库数据迁移文档重新生成，并确认迁移链和 Schema 一致。

## 提交前检查

先查看实际改动：

```bash
git status --short
git diff --check
git diff
```

确认没有临时文件、凭据、个人路径、无关格式化或意外的锁文件变化。

根据改动运行最相关的测试，然后运行仓库提供的完整检查：

```bash
corepack pnpm build:check
```

`build:check` 会执行代码规范、类型、OpenAPI、文档链接和测试等检查。数据库、严格国际化、技能或特定包的检查可能由 CI 另外执行；如果改动涉及这些区域，也应提前运行对应命令。

{% hint style="info" %}
检查脚本和 Node.js 版本会随 `main` 更新。本文命令与仓库冲突时，以当前分支的 `package.json`、`.node-version`、`CONTRIBUTING.md` 和 CI 配置为准。
{% endhint %}

## 创建提交

项目要求小而聚焦的 Conventional Commit，并要求提交包含 DCO sign-off：

```bash
git add path/to/changed-file
git commit --signoff -m "fix(module-name): describe the change"
```

常用类型包括 `feat`、`fix`、`refactor`、`docs`、`test` 和 `chore`。Scope 应指向具体模块，并使用简短的 kebab-case 名称，不要使用 `main` 这类泛化范围。

`--signoff` 会在提交信息中加入：

```text
Signed-off-by: Your Name <your.email@example.com>
```

它表示你有权按项目许可提交这项贡献，不等同于 GPG 或 SSH 加密签名。

## 与上游同步

创建 PR 前，将分支更新到最新 `main`：

```bash
git fetch upstream
git rebase upstream/main
```

解决冲突并重新运行相关检查后，再推送自己的分支：

```bash
git push -u origin fix/short-description
```

如果已经推送过并因 rebase 需要更新远端，确认分支只由自己使用后再采用安全的 `--force-with-lease`；不要对共享分支直接强制推送。

## 提交 Pull Request

创建 PR 时：

1. 基础仓库选择 `CherryHQ/cherry-studio`。
2. V2 和当前开发改动的 base 选择 `main`。
3. 按 PR 模板填写改动前后、实现原因、权衡、相关 Issue、Breaking Change 和 Release Note。
4. 用户可见改动附上截图或录屏，并说明测试系统和验证步骤。
5. 只在所有必需内容就绪后请求 Review。

尚未确定方向或仍在开发时，可以先创建 **Draft PR**。Draft PR 会跳过项目 CI，也不会自动分配 Review；准备完成后再标记为 Ready for review。

新贡献者的非 Draft PR 可能先获得 `needs-ok-to-test` 标签，CI 不会立即运行。维护者在 PR 中添加 `/ok-to-test` 后才会创建测试流水线。这是正常的安全流程，不需要反复关闭或重开 PR。

## 处理 Review

收到意见后：

1. 逐条确认问题和期望行为。
2. 在原分支提交小而清晰的后续修改。
3. 重新运行受影响的测试。
4. 回复说明修改位置和验证结果。
5. 将已解决的讨论交给 Reviewer 确认。

不要为了“让 CI 变绿”而删除有效测试、放宽类型或绕过安全检查。若失败与当前 PR 无关，应在 PR 中给出日志和复现依据，请维护者判断。

## 常见问题

### 安装依赖后锁文件大面积变化

通常是 Node.js 或 pnpm 版本不匹配。恢复自己无意产生的锁文件改动，按 `.node-version` 和 `packageManager` 重新准备环境，再运行 `corepack pnpm install`。

### Windows 中技能或同步文件异常

确认在克隆前已启用开发人员模式和 `core.symlinks=true`。如果仓库中的符号链接已经被检出为普通文件，启用后重新克隆。

### CI 一直没有开始

先检查 PR 是否仍为 Draft。新贡献者还应查看是否存在 `needs-ok-to-test` 标签；等待维护者执行 `/ok-to-test`。

### 不确定是否需要新增 Issue

小型、明确的问题修复可以直接提交 PR，并在描述中给出复现步骤。较大功能、接口变化或有多种方案的改动，建议先用 Issue 取得共识。

文档贡献请阅读[贡献文档](docs.md)。其他问题可以通过[反馈与建议](../question-contact/suggestions.md)联系社区。
