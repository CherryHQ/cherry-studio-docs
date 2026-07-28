---
icon: download
---

# 客户端下载

## 选择稳定版还是 V2 Beta

| 版本 | 适合谁 | 下载 |
|---|---|---|
| 稳定版 | 日常使用和重要数据 | [官网下载](https://cherryai.com.cn/download) · [GitHub Latest](https://github.com/CherryHQ/cherry-studio/releases/latest) |
| ⚠️ **V2 测试版（高风险）** | 仅限能够承担数据丢失风险、并使用隔离环境的测试者 | 在 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 中选择最新的 V2 预发布版本 |

版本号、安装包和发布说明会持续变化，请以 GitHub Releases 中标记的 **Latest** 和 **Pre-release** 为准，不要根据旧截图中的版本号选择安装包。

{% hint style="danger" %}
### ⚠️ V2 Beta 可能造成严重数据丢失

V2 Beta 和其中的**工作（Agent）**仍在测试。Agent 在获得权限后可以读写、移动或删除文件，也可以执行终端命令；模型可能误解指令，测试版也可能存在权限范围或文件操作缺陷。最坏情况下可能出现大范围文件被删除、系统无法正常使用，甚至需要从备份恢复或重装系统。

这里的风险主要是**数据和软件环境损坏**，不是物理损坏电脑硬件。即使如此，后果仍可能非常严重。不能接受该风险时，请使用稳定版。

安装或启用 V2 Beta 前，必须做到：

1. 把重要文件和 Cherry Studio 数据完整备份到**断开连接的外部存储**，并确认备份可以恢复；
2. 优先使用虚拟机、测试电脑或隔离的普通用户账户，不要以管理员身份运行；
3. 只把专门建立的临时文件夹设为 Agent 工作区，**不要选择系统盘根目录、用户主目录、桌面、文档目录或整块移动硬盘**；
4. 默认使用计划模式或普通模式，不要在真实重要数据上启用全自动模式；
5. 不要让 Agent 执行“清理整块磁盘”“删除所有无用文件”等宽泛任务。看到 `rm -rf`、`Remove-Item -Recurse`、`rmdir /s` 等递归删除命令时，应立即取消并人工核对目标路径。

如发现异常删除，立即停止 Agent 和 Cherry Studio，避免继续向受影响磁盘写入数据，再使用备份或专业恢复工具处理。工作权限说明见[工作（Agent）](../advanced-basic/agent.md)。
{% endhint %}

## 如何选择安装包

### Windows

* 普通 Intel/AMD 电脑：`x64-setup.exe`
* Windows ARM 设备：`arm64-setup.exe`
* 不想安装：选择对应架构的 `portable.exe`

Windows 7 不受支持。安装版通常更适合日常使用；便携版的数据位置和自动更新行为可能不同。

### macOS

* Apple M 系列芯片：`arm64.dmg`
* Intel 芯片：`x64.dmg`

在 ` → 关于本机` 查看芯片类型。下载后把 Cherry Studio 拖入“应用程序”文件夹。

### Linux

发布页通常提供：

* `x86_64.AppImage` / `arm64.AppImage`
* `amd64.deb` / `arm64.deb`
* `x86_64.rpm` / `aarch64.rpm`

按发行版包管理器和 CPU 架构选择。AppImage 首次运行前可能需要添加可执行权限。

## 安全下载建议

1. 优先使用官网或 `CherryHQ/cherry-studio` 官方 GitHub Releases；
2. 不要从来历不明的网盘或群文件安装；
3. 文件名中的版本和架构应与发布页一致；
4. 需要校验时，使用 Release 页面提供的 SHA256；
5. 升级、切换稳定版/V2 或更换架构前先备份数据；
6. 测试 V2 的 Agent 时使用隔离工作区，并逐项审核文件修改和命令执行。

## 安装教程

* [Windows 安装](../cherry-studio/installation/windows.md)
* [macOS 安装](../cherry-studio/installation/macos.md)
* [Linux 安装](../cherry-studio/installation/linux.md)

## 下载后的下一步

安装并看到 Cherry Studio 主界面后，继续完成[快速开始](../getting-started/quick-start.md)：添加模型服务、启用一个对话模型并发送测试消息。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到疑问，请参考 [反馈与建议](../question-contact/suggestions.md)。
