---
icon: download
---

# 客户端下载

## 选择稳定版还是 V2 Beta

| 版本 | 适合谁 | 下载 |
|---|---|---|
| 稳定版 | 日常使用和重要数据 | [官网下载](https://cherryai.com.cn/download) · [GitHub Latest](https://github.com/CherryHQ/cherry-studio/releases/latest) |
| V2 测试版 | 体验新版界面、验证迁移和反馈问题 | 在 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 中选择最新的 V2 预发布版本 |

版本号、安装包和发布说明会持续变化，请以 GitHub Releases 中标记的 **Latest** 和 **Pre-release** 为准，不要根据旧截图中的版本号选择安装包。

{% hint style="danger" %}
V2 Beta 仅供测试，不应替代稳定版承载重要数据。官方发布说明明确提示：Beta 期间产生的数据可能在后续 Beta 或 V2 正式版中被清除。安装或迁移前务必先备份。
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
5. 升级、切换稳定版/V2 或更换架构前先备份数据。

## 安装教程

* [Windows 安装](../cherry-studio/installation/windows.md)
* [macOS 安装](../cherry-studio/installation/macos.md)
* [Linux 安装](../cherry-studio/installation/linux.md)

## 下载后的下一步

安装并看到 Cherry Studio 主界面后，继续完成[快速开始](../getting-started/quick-start.md)：添加模型服务、启用一个对话模型并发送测试消息。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到疑问，请参考 [反馈与建议](../question-contact/suggestions.md)。
