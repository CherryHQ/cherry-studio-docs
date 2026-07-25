---
icon: download
---

# 客户端下载

Cherry Studio 提供 Windows、macOS 和 Linux 安装包。为避免下载页中的具体版本号过期，本页只保留长期有效的官方入口；打开下载页面后，请选择最新稳定版及与你的系统架构匹配的文件。

## 官方下载入口

* [Cherry Studio 官网下载页](https://cherry-ai.com/download)
* [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases)
* [GitHub 最新稳定版](https://github.com/CherryHQ/cherry-studio/releases/latest)

{% hint style="warning" %}
只从 Cherry Studio 官网、`CherryHQ/cherry-studio` 官方仓库或下载页明确列出的镜像获取安装包。不要运行来源不明、被重新打包或要求关闭安全软件的安装程序。
{% endhint %}

## 选择稳定版还是预览版

| 类型 | 如何识别 | 适合谁 |
| :--- | :--- | :--- |
| 稳定版 | GitHub Releases 中标记为 **Latest**，版本号通常不含 `alpha`、`beta` 或 `rc` | 日常使用，推荐 |
| 预发布版 | 标记为 **Pre-release**，版本号可能包含 `alpha`、`beta` 或 `rc` | 希望提前测试新功能的用户 |
| 每日预览构建 | 来自官方 [V2 Daily Preview Build](https://github.com/CherryHQ/cherry-studio/actions/workflows/v2-daily-preview-build.yml) | 开发、测试和问题复现 |

预览版可能包含未完成的数据迁移、界面或兼容性改动。安装前先完成备份；重要数据环境优先使用稳定版。

## Windows

### 选择架构

打开 **设置 → 系统 → 系统信息**，查看“系统类型”：

* `x64` 或“基于 x64 的处理器”：下载 `x64`。
* `ARM64` 或“基于 ARM 的处理器”：下载 `arm64`。

大多数 Intel 和 AMD 电脑使用 `x64`。只有 Windows on ARM 设备使用 `arm64`。

### 选择安装包

| 文件类型 | 说明 |
| :--- | :--- |
| `*-x64-setup.exe` / `*-arm64-setup.exe` | 安装版；支持选择安装目录并创建快捷方式 |
| `*-x64-portable.exe` / `*-arm64-portable.exe` | 便携版；适合不希望执行安装流程的场景 |

{% hint style="warning" %}
Cherry Studio 不支持 Windows 7。请在受支持的 Windows 版本上安装。
{% endhint %}

安装步骤和系统安全提示见 [Windows 安装教程](../cherry-studio/installation/windows.md)。

## macOS

打开 **苹果菜单 → 关于本机**，查看“芯片”或“处理器”：

* 显示 Apple M 系列芯片：下载 `arm64`。
* 显示 Intel 处理器：下载 `x64`。

| 文件类型 | 说明 |
| :--- | :--- |
| `*-arm64.dmg` / `*-x64.dmg` | 推荐的图形化安装包 |
| `*-arm64.zip` / `*-x64.zip` | 压缩包版本 |

Apple Silicon 包适用于 M1、M2、M3、M4 等 Apple 芯片。架构选错时，应用可能无法打开或只能通过兼容层运行。

安装步骤和“无法验证开发者”等提示见 [macOS 安装教程](../cherry-studio/installation/macos.md)。

## Linux

在终端运行：

```bash
uname -m
```

* 输出 `x86_64`：选择 `x86_64` 或 `amd64`。
* 输出 `aarch64` / `arm64`：选择 `arm64` / `aarch64`。

官方 Release 通常提供：

| 文件类型 | 适合场景 |
| :--- | :--- |
| `.AppImage` | 跨发行版直接运行 |
| `.deb` | Debian、Ubuntu 及其衍生发行版 |
| `.rpm` | Fedora、RHEL、Rocky Linux 等 RPM 系发行版 |

不同格式的架构命名可能不同，例如 x64 在 `.deb` 文件名中常写作 `amd64`，在 AppImage 中可能写作 `x86_64`。

## 下载后检查

1. 确认文件来自官方域名或 `github.com/CherryHQ/cherry-studio`。
2. 再次核对操作系统、架构和安装包格式。
3. 如果 Release 页面提供 SHA-256 摘要，可在运行前与本地文件摘要比对。
4. 更新或测试预览版前，先备份 Cherry Studio 数据。

### 计算 SHA-256

{% tabs %}
{% tab title="Windows PowerShell" %}
```powershell
Get-FileHash .\Cherry-Studio-安装包文件名 -Algorithm SHA256
```
{% endtab %}

{% tab title="macOS" %}
```bash
shasum -a 256 ~/Downloads/Cherry-Studio-安装包文件名
```
{% endtab %}

{% tab title="Linux" %}
```bash
sha256sum ~/Downloads/Cherry-Studio-安装包文件名
```
{% endtab %}
{% endtabs %}

输出应与官方 Release 中对应文件的 SHA-256 完全一致。不一致时不要运行该文件，请重新从官方入口下载。

## 下一步

* [安装教程](../cherry-studio/installation/)
* [配置模型服务](../pre-basic/providers/)
* [对话界面](preview/chat.md)
