---
description: 把 Cherry Studio V2 的话题、消息或笔记导出到本机 Obsidian 保管库。
icon: gem
---

# Obsidian 配置与导出

Cherry Studio V2 可以把完整话题、单条消息或 Cherry Studio 笔记导出为 Obsidian 中的 Markdown 文件。导出使用 Obsidian 内置的 `obsidian://` URI 和系统剪贴板，不需要安装第三方 Obsidian 插件。

配置入口位于 **设置 > 集成 > Obsidian**。**数据设置 > 导出菜单**只控制“导出到 Obsidian”是否出现在菜单中。

{% hint style="warning" %}
“新建（如果存在就覆盖）”会替换同路径的现有 Markdown 文件。第一次使用时请新建测试文件夹，并先备份重要 Vault。
{% endhint %}

## 使用前准备

1. 在当前电脑安装并至少启动一次 Obsidian。
2. 在 Obsidian 中打开目标本地 Vault。
3. 确认 Vault 的文件夹仍存在，并且当前用户可读写。
4. 重新打开 Cherry Studio 的 Obsidian 设置。

Cherry Studio 会读取 Obsidian 的本机配置，列出这台电脑上已经登记的 Vault：

- Windows：读取用户应用数据中的 Obsidian 配置；
- macOS：读取 `~/Library/Application Support/obsidian/obsidian.json`；
- Linux：兼容常见 XDG、Snap 和 Flatpak 配置位置。

只同步到其他电脑、但从未在当前 Obsidian 客户端中打开过的 Vault，不会自动出现在列表中。

## 选择默认 Vault

1. 打开 **设置 > 集成 > Obsidian**。
2. 在 **默认 Obsidian 仓库**中选择目标 Vault。
3. 返回对话页面。

如果尚未选择默认值，Cherry Studio 会在发现 Vault 后使用列表中的第一个。导出时仍可在弹窗里临时改选其他 Vault。

{% hint style="info" %}
Cherry Studio 界面中的“仓库”和“保管库”都指 Obsidian Vault。这里选择的是 Vault 名称，不是 Obsidian Sync 的远程 Vault 或账户。
{% endhint %}

## 启用导出菜单

如果菜单中没有“导出到 Obsidian”：

1. 打开 **设置 > 数据设置 > 导出菜单**。
2. 开启 **导出到 Obsidian**。
3. 返回对话或笔记，重新打开导出菜单。

这个开关只控制入口可见性，不会影响 Vault 发现或 `obsidian://` 协议。

## 打开导出弹窗

### 导出完整话题

在左侧话题列表打开目标话题的菜单，选择 **导出到 Obsidian**。

完整话题会按消息顺序转换为 Markdown。默认处理方式为 **新建（如果存在就覆盖）**。

### 导出单条消息

打开消息菜单，选择 **导出到 Obsidian**。

单条消息只导出当前消息内容。弹窗仍允许修改标题、目标路径和处理方式。

### 导出 Cherry Studio 笔记

在笔记菜单中选择 **导出到 Obsidian**。笔记使用当前 Markdown 内容，不显示“导出思维链”开关。

## 配置导出弹窗

| 字段 | 作用 |
| --- | --- |
| 标题 | 新建文件的文件名来源，也是新建模式下的 YAML `title` |
| 保管库 | 本次导出的目标 Obsidian Vault |
| 路径 | Vault 根目录、现有文件夹或现有 `.md` 文件 |
| 标签 | 新建模式下写入 YAML `tags`，多个标签使用英文逗号分隔 |
| 创建时间 | 新建模式下写入 YAML `created` |
| 来源 | 新建模式下写入 YAML `source`，默认是 `Cherry Studio` |
| 处理方式 | 新建/覆盖、前置或追加 |
| 导出思维链 | 对话或消息存在思考内容时决定是否一并导出 |

标题不能为空。新建文件时，Cherry Studio 会移除各平台不允许的文件名字符，并把过长名称截断。

### 选择路径

路径选择器会读取目标 Vault 中的文件夹和 Markdown 文件，并忽略以 `.` 开头的隐藏项目。

- 选择 **根目录**或某个文件夹时，会根据标题生成新的 `.md` 文件名。
- 选择现有 `.md` 文件时，会直接使用该文件路径，标题自动改为文件名，并默认切换为 **追加**。
- 切换 Vault 后，需要重新选择路径。

目录树为空时，先确认 Vault 路径仍然存在，并检查 Cherry Studio 是否有读取该目录的权限。

## 三种处理方式

| 处理方式 | 现有同名文件 | 写入位置 | YAML Properties |
| --- | --- | --- | --- |
| 新建（如果存在就覆盖） | 覆盖现有内容 | 替换整个文件 | 写入 `title`、`created`、`source`、`tags` |
| 前置 | 保留现有内容 | 把新内容加到开头 | 不写入新的 Properties |
| 追加 | 保留现有内容 | 把新内容加到末尾 | 不写入新的 Properties |

前置和追加会在新旧内容之间加入 Markdown 分隔线。它们不会尝试合并标题或重新生成现有 YAML。

{% hint style="warning" %}
选择文件夹并使用“新建（如果存在就覆盖）”时，标题会决定目标文件名。目标目录中已有同名文件就会被替换。
{% endhint %}

## 导出思考内容

对话和消息导出弹窗提供 **导出思维链**开关：

- 关闭：只导出正常回答内容；
- 开启：消息存在思考 / 推理内容时一并写入。

导出内容会成为普通 Markdown。要把文件共享给他人或公开发布时，先检查其中是否包含草稿、中间过程或敏感信息。

该开关不会生成原本不存在的思考内容，也不会出现在 Cherry Studio 笔记导出中。

## 导出是如何完成的

点击确认后，Cherry Studio 会：

1. 把 Markdown 内容写入系统剪贴板；
2. 构造包含 Vault、文件路径和处理方式的 `obsidian://new` URI；
3. 请求系统打开 Obsidian；
4. 由 Obsidian 从剪贴板创建、覆盖、前置或追加文件。

因此 Cherry Studio 中的成功提示表示导出请求已经发出，不等于文件一定已经写入。切换到 Obsidian 后，应确认目标文件存在且内容正确。

这一流程基于 [Obsidian 官方 URI](https://help.obsidian.md/Extending%2BObsidian/Obsidian%2BURI)提供的 `clipboard`、`append` 和 `overwrite` 等参数。

## 常见问题

### 设置中显示“未找到 Obsidian 仓库”

先在同一系统用户下启动 Obsidian，打开目标本地 Vault，再重新进入 Cherry Studio 设置。只有 Obsidian 本机配置中登记过的 Vault 才会被发现。

### Vault 能看到，但路径列表为空

Vault 文件夹可能已移动、离线或没有读取权限。回到 Obsidian 确认 Vault 可以正常打开，并检查外置磁盘或网络目录是否在线。

### 点击导出后 Obsidian 没有打开

系统可能没有注册 `obsidian://` 协议。Windows 和 macOS 通常在运行 Obsidian 后自动注册；Linux 需要确保桌面文件的 `Exec` 支持 `%u` 参数。可参阅 Obsidian 官方 URI 文档中的注册说明。

### Cherry Studio 提示成功，但没有生成笔记

成功提示只表示 URI 已发出。检查 Obsidian 是否弹出、目标 Vault 是否正确，以及系统是否允许 Cherry Studio 打开外部协议。还应确认剪贴板没有被安全软件阻止或立即改写。

### 导出覆盖了旧笔记

“新建（如果存在就覆盖）”会替换同路径文件。可从 Vault 备份、版本控制或 Obsidian Sync 版本历史恢复；后续改用不同标题、其他文件夹、前置或追加。

### 前置或追加后没有 Properties

这是当前设计。只有新建/覆盖模式会生成 YAML Properties；前置和追加只写入分隔线与 Markdown 正文。

### 对话菜单中没有 Obsidian

进入 **设置 > 数据设置 > 导出菜单**，打开 **导出到 Obsidian**。若已开启，重新进入当前对话再打开菜单。

### Linux 上仍然找不到 Vault

确认 Obsidian 的安装方式和配置路径。Cherry Studio 会检查常见 XDG、Snap 与 Flatpak 位置，但自定义便携版或非标准路径可能无法自动发现。

如仍无法解决，请通过[反馈与建议](../../question-contact/suggestions.md)提交 Cherry Studio 与 Obsidian 版本、操作系统、安装方式、是否能打开 `obsidian://` 链接，以及已脱敏的 Vault 名称和路径。
