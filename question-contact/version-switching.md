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

V2.0.2 已支持从 V1.9.13 直接迁移，不再需要 V2.0.0 中转。

| 当前情况 | 应该怎么做 |
| --------------- | ---------------------------------- |
| 仍在 V1，需要保留数据 | 将 V1 更新到 1.9.13，再直接安装 V2.0.2 完成迁移。 |
| 已经在使用 V2 | 正常升级 V2.0.2，继续使用当前 V2 数据。 |
| 之前迁移 V1 失败或遗漏数据 | 完整备份当前 V2 后，才可使用【重新迁移】。 |
| 不需要 V1 数据 | 可以选择【忽略并使用默认值】，但 V1 数据不会迁入。 |

{% hint style="danger" %}
【设置】→【数据】中的【重新迁移】会永久删除当前 V2 数据，再从原始 V1 数据重新导入。它不会合并两边的数据；不是 V1 迁移失败或遗漏数据时，一定不要点击。
{% endhint %}

## 下载入口

* [V1 官方下载](https://cherryai.com.cn/download/v1)
* V2.0.2 发布页：[GitCode](https://gitcode.com/CherryHQ/cherry-studio/releases/v2.0.2) · [GitHub](https://github.com/CherryHQ/cherry-studio/releases/tag/v2.0.2)
* [V2 官方下载](https://cherryai.com.cn/download)

更多备份、迁移失败与数据库注意事项见 [【升级与降级】](../cherry-studio/installation/upgrade-downgrade.md)。
