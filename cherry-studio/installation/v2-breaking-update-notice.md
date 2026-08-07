---
description: 升级 V2 前必须了解的数据迁移、版本路径和回退限制。
icon: triangle-exclamation
---

# 破坏性更新提醒

V2 不是普通的覆盖更新。它更换了数据结构，也调整了助手、Agent、知识库、网络搜索和文件等功能的入口与行为。

{% hint style="danger" %}
V1 数据只能单向迁移到 V2。V2 中新增的会话、Agent、设置和文件不会同步回 V1，V1 与 V2 的备份也不能互相恢复。
{% endhint %}

## 保留数据的正确路径

**V1.9.13 → V2.0.0（完成一次数据迁移）→ V2.0.1**

| 当前情况           | 应该怎么做                                              |
| -------------- | -------------------------------------------------- |
| 仍在 V1，需要保留数据   | 先安装并运行 V2.0.0，完成迁移并重启后再升级 V2.0.1。                  |
| 已在 V2.0.0 完成迁移 | 可以直接升级 V2.0.1，无需再次迁移。                              |
| 不需要 V1 数据      | 可以在 V2.0.1 选择【跳过迁移】，从默认配置开始；V1 数据不会迁入，不建议普通用户这样操作。 |

{% hint style="warning" %}
首次迁移不能直接安装 V2.0.1。V2.0.x 补丁版暂时不能代替 V2.0.0 执行首次迁移。
{% endhint %}

## 升级前必须完成

1. 将 V1 更新到 1.9.13，并至少正常启动一次。
2. 关闭【精简备份】，创建 V1 完整备份。
3. 完全退出 Cherry Studio，再复制整个 V1 数据目录。
4. 使用自定义目录或外置磁盘时，确认路径已挂载且可以读写。

迁移向导读取当前 V1 数据目录，不读取备份 ZIP。备份用于意外恢复，不能代替原数据目录参与迁移。

## 升级后重点检查

* 模型服务、API Key 和默认模型；Anthropic OAuth 不会迁移，需要改用 API Key。
* 助手分组、提示词顺序、Agent 工具权限和知识库绑定。
* 知识库失败来源、网络搜索的关键词搜索与网址读取服务。
* 自定义 CSS、侧栏收藏和缺失文件。

完整对照见[【功能差异】](v1-v2-feature-differences.md)。

## 迁移失败或需要回退

* 优先使用【重试】，修复数据目录、磁盘或数据问题后继续。
* 【保存问题信息】只会保存到本地；文件可能包含路径、内容或凭据，只提供给 Cherry Studio 支持团队。
* 【跳过迁移】或【直接使用 V2】会从默认配置开始，V1 数据不会迁入。
* 正常返回 V1 不需要删除数据库，也不要把 V2 备份恢复到 V1。

{% hint style="danger" %}
不要自行删除或替换数据库。误操作、无法确认数据目录，或需要重新迁移时，请先保留所有备份和数据目录，再联系 Cherry Studio 支持团队。
{% endhint %}

## 继续阅读

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>功能差异</strong></td><td>查看自动迁移、需要复核和不会继承的内容。</td><td><a href="v1-v2-feature-differences.md">v1-v2-feature-differences.md</a></td></tr><tr><td><strong>V1 升级到 V2</strong></td><td>按正确版本顺序完成备份、迁移和验证。</td><td><a href="v1-to-v2-migration.md">v1-to-v2-migration.md</a></td></tr><tr><td><strong>V2 降级到 V1</strong></td><td>了解回退、备份和数据库处理注意事项。</td><td><a href="v2-to-v1-downgrade.md">v2-to-v1-downgrade.md</a></td></tr></tbody></table>

## 下载入口

* [V1 官方下载](https://cherryai.com.cn/download/v1)
* V2.0.0 中转版本：[GitCode 下载页](https://gitcode.com/CherryHQ/cherry-studio/releases/v2.0.0) · [GitHub 下载页](https://github.com/CherryHQ/cherry-studio/releases/tag/v2.0.0)
* [V2 最新版官方下载](https://cherryai.com.cn/download)
