---
icon: linux
---

# Linux 安装

Cherry Studio 通常提供 AppImage、deb 和 rpm 等格式。具体文件名和支持架构以 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 当前发布页为准。

## 选择安装包

| 系统 | 常用格式 |
|---|---|
| Ubuntu、Debian、Linux Mint | `amd64.deb` 或 `arm64.deb` |
| Fedora、RHEL、openSUSE | `x86_64.rpm` 或 `aarch64.rpm` |
| 其他发行版或便携使用 | `x86_64.AppImage` 或 `arm64.AppImage` |

在终端运行 `uname -m` 可以确认架构：`x86_64` 对应 x64，`aarch64` 或 `arm64` 对应 ARM64。

## AppImage

1. 下载与架构匹配的 AppImage；
2. 在文件属性中允许“作为程序执行”，或者运行 `chmod +x 文件名.AppImage`；
3. 双击文件或从终端启动。

部分发行版运行 AppImage 时需要额外安装 FUSE。若出现与 `libfuse` 有关的错误，请按当前发行版文档安装相应兼容包。

## deb 或 rpm

建议使用发行版自带的软件中心打开安装包。熟悉终端的用户也可以使用系统包管理器安装，这样更容易自动处理依赖。

## 成功标志与下一步

看到 Cherry Studio 主界面即表示安装完成。接着按[5 分钟快速开始](../../getting-started/quick-start.md)添加一个对话模型并发送测试消息。

如果程序打不开：

* 确认安装包架构与系统一致；
* 从终端启动并查看具体错误；
* 检查系统是否缺少 FUSE、图形库或系统 WebView 相关依赖；
* 到[反馈与建议](../../question-contact/suggestions.md)提交发行版、桌面环境、架构和完整错误日志。
