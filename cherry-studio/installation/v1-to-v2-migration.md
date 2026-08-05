---
description: 升级前先完成版本检查与双重备份，再按迁移向导导入数据，并核对 V2 的功能变化与手动配置项。
icon: arrow-right-arrow-left
---

# V1 升级到 V2：功能差异与迁移须知

{% hint style="danger" %}
V1 数据只能单向迁移到 V2。V2 中新增或修改的数据不会同步回 V1，V1 与 V2 的备份文件也不能跨版本恢复。升级前请同时保留一份完整备份，以及完全退出 Cherry Studio 后复制的整个 V1 数据目录。
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>下载 V2</strong></td><td>首次迁移应先安装 V2 2.0.0 系列。</td><td><a href="https://cherryai.com.cn/download">https://cherryai.com.cn/download</a></td></tr><tr><td><strong>继续使用 V1</strong></td><td>迁移前更新 V1，或迁移失败后临时返回 V1。</td><td><a href="https://cherryai.com.cn/download/v1">https://cherryai.com.cn/download/v1</a></td></tr></tbody></table>

### 目标与前置条件

本文适用于准备把现有 Cherry Studio V1 数据迁移到 V2 的用户。完成后，常用设置、模型服务、助手、会话、Agent、知识库和其他业务数据会进入 V2 的新数据结构。

开始前请确认：

* 当前 V1 版本不低于 1.9.12；建议先升级到最终版 1.9.13。
* 首次迁移使用 V2 2.0.0 系列，不能从 V1 直接跳到 2.0.1 或更高版本。
* 自定义数据目录和外置磁盘均可正常访问。
* 所有 Agent 任务、知识库导入、文件处理和内容生成都已结束。

{% hint style="warning" %}
迁移向导读取的是当前 V1 数据目录，而不是 V1 备份 ZIP。备份用于意外恢复，不能代替原数据目录参与迁移。
{% endhint %}

### 术语

| 术语     | 含义                                     |
| ------ | -------------------------------------- |
| 完整备份   | 包含业务数据和托管文件的备份；创建前应关闭【精简备份】。           |
| 数据目录副本 | 完全退出应用后复制的整个 V1 数据目录，用于保留可继续运行的 V1 状态。 |
| 单向迁移   | V1 数据导入 V2 后，V2 的新变化不会写回 V1。           |
| 迁移警告   | 某一类数据未完整迁移，但其余数据已完成；重启前应展开查看。          |

### 升级路线

<figure><img src="../../.gitbook/assets/clipboard (11).png" alt=""><figcaption></figcaption></figure>

先确认版本和备份，再启动 V2 迁移。出现错误时优先修复问题并重试；只有明确不需要旧数据时，才选择【直接使用 V2】。

### 操作步骤

{% stepper %}
{% step %}
#### 将 V1 更新到可迁移版本

打开 V1 的【关于】页面确认版本。低于 1.9.12 时，先从 [V1 下载页](https://cherryai.com.cn/download/v1) 安装 1.9.13，再重新启动一次 V1。
{% endstep %}

{% step %}
#### 创建完整备份

在 V1 的数据备份页面关闭【精简备份】，创建一份完整备份，并确认备份文件已经生成。把备份放在当前应用数据目录之外。
{% endstep %}

{% step %}
#### 复制整个 V1 数据目录

在 V1 的数据设置中确认当前数据目录，然后完全退出 Cherry Studio。复制整个目录并保留原有层级；不要只复制数据库文件，也不要修改副本内容。
{% endstep %}

{% step %}
#### 检查自定义目录和外置磁盘

如果数据目录位于移动硬盘、网络卷或其他自定义位置，先确认该位置已挂载并且可以读写。路径不可访问时不要改用默认目录继续迁移，否则 V2 可能按没有旧数据处理。
{% endstep %}

{% step %}
#### 首次启动 V2 2.0.0

从 [V2 下载页](https://cherryai.com.cn/download) 获取与当前系统和芯片匹配的安装包。完全退出 V1 后安装并启动 V2 2.0.0 系列。
{% endstep %}

{% step %}
#### 完成【数据迁移向导】

确认向导显示的数据位置正确，再选择【开始迁移】。迁移期间保持应用运行，不要移动数据目录、卸载 V1 或断开外置磁盘。
{% endstep %}

{% step %}
#### 查看结果并重启

迁移完成后先展开警告信息，再选择【重启应用】。进入 V2 后按本文的升级后检查清单逐项确认。
{% endstep %}
{% endstepper %}

### 关键截图
