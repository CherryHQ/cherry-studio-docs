---
description: 根据当前版本选择正确的升级、迁移或降级路径。
icon: arrow-right-arrow-left
---

# 版本升级与降级

跨 V1、V2 切换时，请先选择对应说明：

* [功能差异](../cherry-studio/installation/v1-v2-feature-differences.md)
* [V1 升级到 V2](../cherry-studio/installation/v1-to-v2-migration.md)
* [V2 降级到 V1](../cherry-studio/installation/v2-to-v1-downgrade.md)

{% hint style="danger" %}
切换版本前，先在应用内创建完整备份，再完全退出 Cherry Studio 并复制整个数据目录。V1 与 V2 的备份不能互相恢复。
{% endhint %}

## V1 数据迁移到 V2

正确路径是：**V1.9.13 → V2.0.0（完成一次数据迁移）→ V2.0.1**。

| 当前情况           | 应该怎么做                                        |
| -------------- | -------------------------------------------- |
| 已在 V2.0.0 完成迁移 | 可以直接升级 V2.0.1。                               |
| 仍在 V1，需要保留数据   | 先安装并运行 V2.0.0，完成迁移后再升级 V2.0.1。               |
| 不需要 V1 数据      | 可以在 V2.0.1 选择【跳过迁移】，但 V1 数据不会迁入；不建议普通用户这样操作。 |

{% hint style="warning" %}
V2.0.1 不能代替 V2.0.0 执行首次迁移。V2.0.x 补丁版暂时仍受这一限制。
{% endhint %}

## 下载入口

* [V1 官方下载](https://cherryai.com.cn/download/v1)
* V2.0.0 中转版本：[GitCode 下载页](https://gitcode.com/CherryHQ/cherry-studio/releases/v2.0.0) · [GitHub 下载页](https://github.com/CherryHQ/cherry-studio/releases/tag/v2.0.0)
* [V2 最新版官方下载](https://cherryai.com.cn/download)

更多备份、迁移失败与数据库注意事项见[【升级与降级】](../cherry-studio/installation/upgrade-downgrade.md)。
