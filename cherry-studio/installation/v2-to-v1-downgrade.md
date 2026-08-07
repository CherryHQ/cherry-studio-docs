---
description: 返回原 V1 数据，并安全处理 V2 备份、数据库和 Agent 数据。
icon: arrow-rotate-left
---

# V2 降级到 V1

降级适合 V2 暂时影响关键工作、且你仍保留可用 V1 数据的情况。它不会把 V2 数据转换成 V1 格式。

{% hint style="danger" %}
V2 中新增的会话、Agent、设置和文件不会回到 V1。V2 备份也不能恢复到 V1；降级前请分别保留最新 V2 备份和原始 V1 备份或数据目录副本。
{% endhint %}

## 正常降级

{% stepper %}
{% step %}
### 停止任务并备份 V2

结束正在运行的对话、Agent 和文件处理任务。在【设置】→【数据】创建新的 V2 完整备份，并保存到应用数据目录之外。
{% endstep %}

{% step %}
### 确认 V1 数据仍在

找到升级前保留的 V1 数据目录副本或 V1 备份。只有 V1 备份时，需在兼容的 V1 中恢复，不能导入 V2。
{% endstep %}

{% step %}
### 下载并安装 V1

完全退出 V2，从 [V1 官方下载](https://cherryai.com.cn/download/v1) 获取与当前系统匹配的安装包并完成安装。
{% endstep %}

{% step %}
### 使用原 V1 数据启动

启动 V1，并使用升级前的 V1 数据目录。不要用 V2 数据库或 V2 备份覆盖它。
{% endstep %}

{% step %}
### 检查后再继续工作

检查常用会话、模型服务、知识库和文件。确认 V1 数据正常前，不要删除任何 V1 或 V2 备份。
{% endstep %}
{% endstepper %}

{% hint style="info" %}
正常降级不需要删除数据库。保留 V2 数据可以方便以后返回 V2，也能避免误删尚未导出的内容。
{% endhint %}

## 什么时候才处理 V2 数据库

只有以下情况才需要处理：

* 明确放弃当前全部 V2 数据，只保留 V1 数据；
* 需要重新执行一次 V1 → V2 迁移。

这不是普通降级步骤。操作会影响 V2 的全部会话、Agent、设置和其他数据，不是只清理某一批测试记录。

### 安全处理方法

1. 完全退出 V1 和 V2，确认没有后台任务。
2. 打开 V1 1.9.13 的【设置】→【数据】→【应用数据】，进入当前应用数据目录。
3. 将以下项目移到桌面或其他安全位置，不要直接删除：
   * `Data/cherrystudio.sqlite`
   * `Data/cherrystudio.sqlite-shm` 和 `Data/cherrystudio.sqlite-wal`（如存在）
   * `Data/Agents/.claude`
4. 启动 V1 并检查原 V1 数据。需要重新迁移时，再启动 V2 完成迁移。
5. 只有确认 V1 数据可用、V2 备份也能找到后，才决定是否删除此前移出的文件。

{% hint style="danger" %}
不要在应用运行时移动数据库，不要只移动 `cherrystudio.sqlite` 而遗漏同目录下的 `-shm` 或 `-wal` 文件，也不要把 V2 数据库替换成 V1 数据库。无法判断当前数据目录或文件用途时，停止操作并联系 Cherry Studio 支持团队。
{% endhint %}

## 常见问题

<details>

<summary>V2 的新对话可以带回 V1 吗？</summary>

不可以。请在 V2 中导出需要保留的内容，V1 只继续使用原 V1 数据。

</details>

<details>

<summary>下载 V1 会自动转换 V2 数据吗？</summary>

不会。安装包只安装应用，不会转换数据或备份格式。

</details>

<details>

<summary>可以直接删除数据库再试吗？</summary>

不建议。先移出并保留，完成验证后再决定是否删除；误删且没有可用备份时，V2 数据可能无法恢复。

</details>

<details>

<summary>降级后再次回到 V2，应该安装哪个版本？</summary>

如果继续使用此前已完成迁移的 V2 数据，可以直接安装 V2.0.1。如果要把当前 V1 数据重新迁入 V2，仍须按 **V1.9.13 → V2.0.0（完成一次数据迁移）→ V2.0.1** 操作；V2.0.x 补丁版暂时不能代替 V2.0.0 执行首次或重新迁移。

</details>

## 参考资料

* [Cherry Studio V1 官方下载](https://cherryai.com.cn/download/v1)
* [Cherry Studio V2 官方下载](https://cherryai.com.cn/download)
* V2.0.0 中转版本：[GitCode 下载页](https://gitcode.com/CherryHQ/cherry-studio/releases/v2.0.0) · [GitHub 下载页](https://github.com/CherryHQ/cherry-studio/releases/tag/v2.0.0)
* [问题反馈与功能建议](../../question-contact/suggestions.md)
