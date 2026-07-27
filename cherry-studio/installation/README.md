---
icon: desktop-arrow-down
---

# 安装教程

本页说明 Cherry Studio 的通用安装流程，并引导你进入对应系统的详细教程。还没有安装包时，请先前往[客户端下载](../../cherrystudio/download.md)。

## 安装前

1. 确认安装包来自 Cherry Studio 官网或 `CherryHQ/cherry-studio` 官方 GitHub Releases。
2. 核对操作系统与 CPU 架构，避免混用 x64、ARM64、amd64 或 aarch64 包。
3. 关闭正在运行的 Cherry Studio。
4. 如果是升级、降级或测试预览版，先在 **设置 → 数据设置** 创建备份。

{% hint style="warning" %}
不要在没有备份的情况下从新版本降级到旧版本。新版本可能已经迁移本地数据库或配置，旧版本未必能够读取迁移后的数据。
{% endhint %}

## Windows

Windows 提供安装版和便携版：

* **Setup 安装版**：按照向导选择目录并完成安装，适合大多数用户。
* **Portable 便携版**：直接运行可执行文件，适合临时使用或不希望执行安装流程的场景。

Cherry Studio 不支持 Windows 7。首次运行时如果出现系统保护提示，请先核对安装包来源和文件摘要，再按 [Windows 安装教程](windows.md)处理。

## macOS

1. 下载与你的芯片匹配的 `.dmg`：Apple 芯片选择 `arm64`，Intel 芯片选择 `x64`。
2. 打开 DMG，将 Cherry Studio 拖入“应用程序”。
3. 从“应用程序”启动。

macOS 可能在首次运行时显示开发者验证或安全提示。处理方式见 [macOS 安装教程](macos.md)。

## Linux

Linux Release 通常提供 AppImage、deb 和 rpm 三种格式。选择一种即可，不要重复安装多个格式。

### AppImage

```bash
chmod +x ./Cherry-Studio-*.AppImage
./Cherry-Studio-*.AppImage
```

AppImage 不需要系统级安装。若无法启动，优先检查文件架构是否正确；部分发行版还需要安装 AppImage 所需的 FUSE 兼容组件。

### Debian / Ubuntu

```bash
sudo apt install ./Cherry-Studio-*-amd64.deb
```

ARM64 设备应使用文件名中包含 `arm64` 的 deb 包。

### Fedora / RHEL / Rocky Linux

```bash
sudo dnf install ./Cherry-Studio-*.rpm
```

根据设备选择 `x86_64` 或 `aarch64` 包。

## 升级

在同一系统和架构上安装较新稳定版时，本地数据通常会保留。为降低风险：

1. 先完成本地或远程备份。
2. 完全退出 Cherry Studio。
3. 使用与当前系统、架构一致的新安装包升级。
4. 启动后先检查模型服务、对话、知识库和智能体是否正常。

预发布版或每日预览构建可能包含尚未稳定的数据迁移。不要把唯一一份重要数据只留在预览版环境中。

## 安装后

首次启动后建议按顺序完成：

1. 在 **设置 → 模型服务** 添加服务商和模型。
2. 返回对话页面发送一条测试消息。
3. 确认数据存储和备份位置。
4. 再按需要启用知识库、智能体、MCP 或其他高级功能。

继续阅读：

* [配置模型服务](../../pre-basic/providers/)
* [对话界面](../../cherrystudio/preview/chat.md)
* [数据设置](../../pre-basic/data-settings/)
* [常见问题](../../question-contact/questions.md)
