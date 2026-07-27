---
description: 在 Windows 上选择、安装和更新 Cherry Studio
icon: windows
---

# Windows

本页说明如何在 Windows 上选择安装包、完成安装，并处理首次启动时常见的安全提示或运行库问题。还没有安装包时，请先前往[客户端下载](../../cherrystudio/download.md)。

{% hint style="warning" %}
Cherry Studio 不支持 Windows 7。请只从 Cherry Studio 官网或 `CherryHQ/cherry-studio` 官方 GitHub Releases 下载安装包。
{% endhint %}

## 选择安装包

Windows Release 提供 x64、ARM64 两种架构，以及 Setup、Portable 两种包型。

| 安装包 | 适合场景 |
| --- | --- |
| `x64-setup.exe` | 使用 Intel 或 AMD 处理器的常见 Windows 电脑；适合大多数用户 |
| `arm64-setup.exe` | 使用 ARM 处理器的 Windows 电脑，例如部分 Snapdragon 设备 |
| `x64-portable.exe` | x64 电脑；无需安装，希望把程序和数据放在指定目录 |
| `arm64-portable.exe` | ARM64 电脑；无需安装，希望把程序和数据放在指定目录 |

不确定架构时，打开 **设置 → 系统 → 系统信息**，查看“系统类型”：

* 显示“基于 x64 的处理器”时选择 x64。
* 显示“基于 ARM 的处理器”时选择 ARM64。

Setup 安装版适合日常使用；Portable 便携版更适合临时测试、U 盘携带或需要独立数据目录的场景。

## 校验下载文件

官方 GitHub Release 会为安装包提供 SHA256。下载完成后，可以在 PowerShell 中运行：

```powershell
Get-FileHash ".\Cherry-Studio-*-setup.exe" -Algorithm SHA256
```

使用便携版时，把文件名改为对应的 `*-portable.exe`。输出值应与 Release 页面列出的 SHA256 完全一致。

如果浏览器或 Windows 提示文件来源未知，先核对下载域名、文件名和 SHA256；来源无法确认时不要继续运行。

## 安装 Setup 版

1. 完全退出正在运行的 Cherry Studio。
2. 双击 `*-setup.exe`。
3. 按安装向导选择安装目录。
4. 确认选项并完成安装。
5. 从桌面快捷方式或开始菜单启动 Cherry Studio。

升级已有安装时，使用相同系统架构的新版本 Setup 安装包即可。升级前建议先在 **设置 → 数据设置** 创建备份。

## 使用 Portable 版

1. 新建一个可写目录，例如 `D:\Apps\CherryStudio`。
2. 把 `*-portable.exe` 放入该目录。
3. 双击可执行文件启动。
4. 不要在程序运行时移动可执行文件或它的数据目录。

未另行设置数据位置时，便携版会在可执行文件所在目录下使用 `data` 目录保存应用数据。备份或迁移便携版时，应同时保留可执行文件和这个目录。

{% hint style="info" %}
不要把便携版放进需要管理员权限才能写入的目录。若希望长期使用、自动创建快捷方式并通过安装向导升级，建议改用 Setup 安装版。
{% endhint %}

## 首次启动

首次启动后，建议先完成以下检查：

1. 打开 **设置 → 模型服务**，添加服务商并启用至少一个模型。
2. 返回对话页面，发送一条测试消息。
3. 打开 **设置 → 数据设置**，确认备份方式和数据位置。

如果 Windows Defender SmartScreen 显示保护提示，先确认文件来自官方渠道并通过 SHA256 校验，再根据系统提示查看详细信息。不要为来源不明的安装包关闭系统安全功能。

## Visual C++ 运行库

Cherry Studio 的部分原生组件依赖 Microsoft Visual C++ Redistributable。安装或启动时如果系统提示缺少运行库：

1. 优先允许 Cherry Studio 安装程序完成依赖安装。
2. 如果自动安装失败，前往 [Microsoft Visual C++ Redistributable 官方页面](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist)。
3. 下载与系统架构一致的 x64 或 ARM64 版本，安装后重新启动 Cherry Studio。

不要从第三方软件下载站获取运行库。

## 更新与切换版本

更新前：

1. 在 **设置 → 数据设置** 创建备份。
2. 完全退出 Cherry Studio。
3. 下载与当前电脑架构一致的新安装包。

Setup 用户可以直接运行新版本安装包。Portable 用户应保留原有 `data` 目录，并用新版本可执行文件替换旧文件。

从新版本降级到旧版本可能遇到数据库或配置不兼容。除非已经备份并明确了解影响，否则不建议降级。预发布版或每日预览构建也不应作为重要数据的唯一运行环境。

## 常见问题

### 双击后没有启动

依次检查：

1. 安装包架构是否与系统一致。
2. 文件是否完整，SHA256 是否匹配。
3. Visual C++ Redistributable 是否已正确安装。
4. 安全软件是否隔离了程序文件。
5. 是否已有 Cherry Studio 进程正在运行。

如果仍无法启动，请记录 Windows 版本、系统架构、Cherry Studio 版本和错误提示，再通过[反馈与建议](../../question-contact/suggestions.md)提交。

### Portable 版启动后像全新安装

检查可执行文件旁的 `data` 目录是否仍在、当前目录是否可写，以及是否移动了可执行文件。恢复前先复制现有目录，避免覆盖仍可用的数据。

### 安装后如何开始使用

继续阅读：

* [配置模型服务](../../pre-basic/providers/)
* [对话界面](../../cherrystudio/preview/chat.md)
* [数据设置](../../pre-basic/data-settings/)
