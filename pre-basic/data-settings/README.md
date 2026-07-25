---
icon: floppy-disk
---

# 数据设置

打开 `设置 → 数据设置` 可以查看数据目录、管理本地备份，并配置笔记软件导出。WebDAV 与 S3 页面在 V2 中已经可见，但备份恢复能力尚未开放。

<figure><img src="../../.gitbook/assets/cherry-storage-location-v2.png" alt="Cherry Studio V2 浅色模式的数据目录页面，用户名已替换为占位符"><figcaption><p>在数据设置中查看当前数据目录</p></figcaption></figure>

> 一句话：先确认数据位置，并在升级、迁移或重置前创建本地备份。

## 我应该用什么备份方案？

| 你的场景 | 推荐方案 |
|---|---|
| 升级、迁移或重置前保护数据 | 优先使用当前版本可用的本地备份或导出能力 |
| 希望用 WebDAV 跨设备恢复 | 查看 [WebDAV 备份](webdav.md) 的 V2 当前状态，等待功能开放 |
| 希望保存到 S3 兼容存储 | 查看 [S3 兼容存储](s3-compatible.md) 的 V2 当前状态，等待功能开放 |
| 想把对话内容自动归档到笔记软件 | [Notion](notion.md) / [Obsidian](obsidian.md) / [思源笔记](siyuan.md) |
| 想导入别人分享的助手 | [助手导入](assistants-subscribe.md) |

## 备份的是什么？

备份范围会随版本和所选备份模式变化。执行前请查看备份页面的范围说明；恢复后抽查模型服务、对话、知识库、笔记和文件是否完整。

{% hint style="warning" %}
备份文件会包含 Provider API 密钥等敏感信息。**请勿把备份文件分享给他人，也不要存储在不受信任的共享网盘**。
{% endhint %}

## 多久备份一次？

* **本地备份**：升级、迁移目录或重置数据前先创建
* **WebDAV / S3**：V2 功能开放后，再根据页面说明配置远端备份

## 数据存哪？

在 `设置 → 数据设置 → 数据目录` 查看实际位置。需要更换目录时，先阅读 [数据存储位置](../personalization-settings/storage.md)，做好备份，再使用路径右侧的迁移入口。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
