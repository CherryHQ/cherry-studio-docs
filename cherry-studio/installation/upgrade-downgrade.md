---
description: 选择版本切换路径，并在操作前保护好 V1 与 V2 数据。
icon: arrows-rotate
---

# 升级与降级

根据当前版本和目标选择对应说明。V1 与 V2 使用不同的数据结构，跨大版本切换前必须先备份。

{% hint style="danger" %}
V1 与 V2 的数据和备份格式不互通。V2 中新增的会话、Agent、设置和文件不会自动回写到 V1。
{% endhint %}

## 保留 V1 数据的升级路径

{% hint style="warning" %}
正确路径是：**V1.9.13 → V2.0.0（完成一次数据迁移）→ V2.0.1**。首次迁移不能直接安装 V2.0.1；V2.0.x 补丁版暂时不能代替 V2.0.0 执行首次迁移。
{% endhint %}

| 当前情况           | 应该怎么做                                        |
| -------------- | -------------------------------------------- |
| 已在 V2.0.0 完成迁移 | 可以直接升级 V2.0.1。                               |
| 仍在 V1，需要保留数据   | 先安装并运行 V2.0.0，完成迁移后再升级 V2.0.1。               |
| 不需要 V1 数据      | 可以在 V2.0.1 选择【跳过迁移】，但 V1 数据不会迁入；不建议普通用户这样操作。 |

## 选择路径

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>破坏性更新提醒</strong></td><td>先确认迁移网关、数据不互通和回退限制。</td><td><a href="v2-breaking-update-notice.md">v2-breaking-update-notice.md</a></td></tr><tr><td><strong>功能差异</strong></td><td>了解界面、Agent、知识库等变化和升级后需要复核的项目。</td><td><a href="v1-v2-feature-differences.md">v1-v2-feature-differences.md</a></td></tr><tr><td><strong>V1 升级到 V2</strong></td><td>备份 V1 数据，经过 V2.0.0 完成迁移，再升级 V2.0.1。</td><td><a href="v1-to-v2-migration.md">v1-to-v2-migration.md</a></td></tr><tr><td><strong>V2 降级到 V1</strong></td><td>返回原 V1 数据，并了解什么时候才需要处理 V2 数据库。</td><td><a href="v2-to-v1-downgrade.md">v2-to-v1-downgrade.md</a></td></tr></tbody></table>

## 切换前准备

1. 结束正在运行的对话、Agent、知识库导入和文件处理任务。
2. 为当前版本创建一份新的完整备份，并保存在应用数据目录之外。
3. 记录当前应用数据目录；使用自定义目录或外置磁盘时，确认路径可以正常访问。

{% hint style="warning" %}
不要为了“彻底卸载”手动删除应用数据。数据库处理只适用于明确放弃全部 V2 数据或重新迁移的情况，详见[【V2 降级到 V1】](v2-to-v1-downgrade.md)。
{% endhint %}

## 下载入口

* [Cherry Studio V2 官方下载](https://cherryai.com.cn/download)
* [Cherry Studio V1 官方下载](https://cherryai.com.cn/download/v1)
* V2.0.0 中转版本：[GitCode 下载页](https://gitcode.com/CherryHQ/cherry-studio/releases/v2.0.0) · [GitHub 下载页](https://github.com/CherryHQ/cherry-studio/releases/tag/v2.0.0)
