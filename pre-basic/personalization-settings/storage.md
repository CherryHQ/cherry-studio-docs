---
icon: floppy-disk
---

# 修改存储位置

Cherry Studio 默认把对话、助手、知识库和应用设置保存在当前系统的用户目录中。只有在系统盘空间不足、需要统一备份，或明确要使用其他磁盘时，才建议迁移。

## 默认存储位置

Cherry Studio 按系统规范把数据放在用户目录下：

* **macOS**：`~/Library/Application Support/CherryStudio`
* **Windows**：`%APPDATA%\CherryStudio`（也就是 `C:\Users\<你的用户名>\AppData\Roaming\CherryStudio`）
* **Linux**：`~/.config/CherryStudio`

也可以进入 **设置 → 数据设置**，在“应用数据”区域查看当前目录：

<figure><img src="../../.gitbook/assets/image (31).png" alt="数据设置中的应用数据目录"><figcaption><p>查看当前应用数据目录</p></figcaption></figure>

## 迁移前准备

迁移会移动当前 Cherry Studio 的全部应用数据，包括对话历史、助手、知识库和设置。开始前请：

1. 先完成一次 [WebDAV 备份](../data-settings/webdav.md) 或 [S3 兼容存储备份](../data-settings/s3-compatible.md)。
2. 确认新目录所在磁盘空间充足，并且当前账户拥有读写权限。
3. 如果使用外置硬盘，迁移后不要随意拔出或更改盘符。

{% hint style="warning" %}
迁移过程中不要退出 Cherry Studio、关闭电脑或断开目标磁盘。迁移完成后，按界面提示重启应用。
{% endhint %}

## 开始迁移

1. 进入 **设置 → 数据设置**。
2. 在“应用数据”区域点击迁移按钮。
3. 选择一个新的空目录，并确认迁移。
4. 等待迁移完成，然后按提示重启 Cherry Studio。

## 如何确认迁移成功

重启后再次进入 **设置 → 数据设置**。如果“应用数据”显示新目录，并且原有对话、助手和知识库都能正常打开，说明迁移已经完成。

如果迁移失败，Cherry Studio 会继续使用原数据目录。不要手动删除原目录；请先根据提示检查目标目录权限和剩余空间，再重新尝试。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
