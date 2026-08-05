---
description: 从官网获取最新版或旧版安装包，并在切换版本前保护好本地数据。
icon: arrows-rotate
---

# 升级与降级

{% hint style="info" %}
日常使用建议保持在最新版。只有在新版本暂时影响当前工作，或必须继续使用旧版功能时，再考虑降级。
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>升级到最新版</strong></td><td>获取正式版安装包，适合日常更新和重新安装。</td><td><a href="https://cherryai.com.cn/download">https://cherryai.com.cn/download</a></td></tr><tr><td><strong>下载旧版</strong></td><td>仅在确有需要时使用；操作前先备份数据。</td><td><a href="https://cherryai.com.cn/download/v1">https://cherryai.com.cn/download/v1</a></td></tr></tbody></table>

### 切换前先做一件事

升级通常可以直接安装；降级前则应先留下可恢复的备份。

操作路径：打开 【设置】→【数据设置】→【本地备份】，选择备份目录并完成一次备份。备份完成后，确认目录中已经出现新的备份文件，再继续安装。

{% hint style="warning" %}
版本跨度较大时，设置项、知识库或 Agent 数据的格式可能不同。降级前不要跳过备份，也不要手动删除应用数据目录。
{% endhint %}

### 升级到最新版

{% stepper %}
{% step %}
#### 保存正在进行的工作

结束仍在运行的 Agent 任务，保存尚未导出的文件，并等待正在生成的内容完成。
{% endstep %}

{% step %}
#### 打开官网升级入口

访问 [Cherry Studio 官方下载页](https://cherryai.com.cn/download)，按当前电脑选择 Windows、macOS 或 Linux 安装包。
{% endstep %}

{% step %}
#### 选择正确的安装包

* macOS：根据芯片选择 Apple 芯片或 Intel 芯片版本；不确定时，可在系统的 【关于本机】中查看。
* Windows：选择与当前系统架构匹配的版本。
* Linux：选择与当前发行版和安装方式匹配的安装包。
{% endstep %}

{% step %}
#### 关闭应用并安装

完全退出 Cherry Studio，再打开刚下载的安装包，按照系统提示完成安装。
{% endstep %}

{% step %}
#### 启动后做一次检查

确认对话可以正常发送，再检查常用的模型服务、知识库和 Agent。若都能正常打开，本次升级就完成了。
{% endstep %}
{% endstepper %}

{% hint style="success" %}
想减少手动检查更新的次数，可以在 【设置】→【常规设置】中开启 【自动更新】。
{% endhint %}

### 降级到旧版

{% stepper %}
{% step %}
#### 完成本地备份

按照上方路径创建备份，并把备份文件保存在应用数据目录之外。
{% endstep %}

{% step %}
#### 打开官网旧版入口

访问 [Cherry Studio 旧版下载页](https://cherryai.com.cn/download/v1)，选择与当前电脑匹配的安装包。
{% endstep %}

{% step %}
#### 退出 Cherry Studio

确认没有 Agent 任务、文件处理或知识库导入仍在运行，然后完全退出应用。
{% endstep %}

{% step %}
#### 安装并检查常用数据

按照系统提示安装旧版。首次启动后，先检查对话、模型服务、知识库和 Agent，再继续日常工作。
{% endstep %}
{% endstepper %}

{% hint style="danger" %}
如果旧版启动异常、数据缺失或设置无法读取，请停止继续使用，不要反复覆盖安装。重新安装最新版后，再从 【设置】→【数据设置】→【备份文件管理】恢复降级前的备份。
{% endhint %}

### 怎么选

| 你的情况            | 建议                        |
| --------------- | ------------------------- |
| 希望获得新功能、修复和后续更新 | 升级到最新版                    |
| 新版本暂时影响关键工作     | 先备份，再短期降级                 |
| 只是遇到一次报错或模型不可用  | 先查看 【问题 & 反馈】；这类问题不一定需要降级 |
| 需要在多台电脑使用       | 每台电脑分别选择对应系统和芯片的安装包，不要混用  |

### 常见问题

<details>

<summary>升级或降级前需要卸载当前版本吗？</summary>

先关闭 Cherry Studio，再按安装包和操作系统的提示处理。不要为了“彻底卸载”而手动删除应用数据；降级前尤其要先完成备份。

</details>

<details>

<summary>安装后模型不能用了，应该先恢复备份吗？</summary>

先检查网络和 【设置】→【模型服务】中的服务状态、密钥与模型是否仍然可用。只有确认本地数据异常时，才考虑恢复备份。

</details>

<details>

<summary>旧版可以一直使用吗？</summary>

旧版适合临时回退或兼容特定工作。确认影响问题已经解决后，建议回到最新版，以便继续获得功能更新和问题修复。

</details>
