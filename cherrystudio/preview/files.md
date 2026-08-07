---
icon: folder
---

# 文件

文件页面是 Cherry Studio 的 **附件总仓库** —— 你在对话中拖进来的图片、PDF、文档，在绘画中生成的图，在知识库中导入的资料，都能在这里集中查看与管理。

可以理解成 Cherry Studio 内部的"我的电脑"。

## 进入文件页面

顶部 Tab 的 `+` →【启动台】→ 点击【文件】。

<figure><img src="../../.gitbook/assets/v2/files-overview.png" alt=""><figcaption><p>文件页面：左侧按类型分类，顶部排序与全选 / 多选</p></figcaption></figure>

## 在这里可以做什么

* **按类型筛选**：左侧按类型分类 —— `文档`、`图片`、`文本`、`音频`、`视频`、`其他`、`所有文件`
* **排序**：顶部支持 `文件名` / `大小` / `类型` / `修改时间` 四种排序方式
* **批量操作**：右上 `全选` 复选框配合 `⋯` 菜单做批量删除
* **上传**：把文件直接拖入页面即可上传，或点击 `上传文件`
* **预览**：单击文件直接预览（图片、PDF 等支持的格式）
* **重命名**：右键 → 重命名
* **删除**：右键 → 删除，删除的文件会进入 **回收站**（详见下方说明）
* **打开所在位置**：右键 →【打开所在文件夹】（macOS = 访达，Windows = 资源管理器）

{% hint style="info" %}
若某个文件被标记为 **缺失**，说明它的本地原文件已被移动或删除；这类文件只能定位位置或从库中移除记录。
{% endhint %}

## 回收站

删除文件后，它不会立刻消失，而是先进入【回收站】。你可以在回收站中：

* **恢复**：把误删的文件放回原处
* **永久删除**：单独彻底清除某个文件
* **清空回收站**：一次性永久清除回收站中的全部文件

<figure><img src="../../.gitbook/assets/v2/files-trash.png" alt=""><figcaption><p>回收站：可恢复、永久删除，或清空全部</p></figcaption></figure>

{% hint style="warning" %}
**永久删除无法撤销。** 删除文件也会同时移除它在所有相关消息中的引用，请确认后再操作。
{% endhint %}

## 文件存在哪？

Cherry Studio 把所有附件存在本地的应用数据目录中。具体路径：

* **macOS**：`~/Library/Application Support/CherryStudio`
* **Windows**：`%APPDATA%\CherryStudio`
* **Linux**：`~/.config/CherryStudio`

想换到别的盘？看 [修改存储位置](../../pre-basic/personalization-settings/storage.md)。

## 提示与技巧

* 长期不用的对话 / 知识库会越攒越多文件，定期到这里清一下能省不少磁盘
* 重要文件建议同时备份到云盘（WebDAV / S3 等），见 [数据设置](../../pre-basic/data-settings/)
* 文件名乱码？通常是从外部拖入时编码问题，建议先重命名再用

***

### 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
