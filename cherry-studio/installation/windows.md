---
description: Windows 版本安装教程
icon: windows
---

# Windows 安装

## 1. 选择安装包

打开[官方下载页](https://cherryai.com.cn/download/v2)，选择 **Windows**。

![Cherry Studio 官方下载页的 Windows 下载选项](https://3562065924-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0Ut5BptC3t8CtSU1UWpM%2Fuploads%2FI5oqtsjL2dau2qnTeQS7%2Fcherry-v2-download-windows-zh-cn.jpg?alt=media\&token=c64dca98-15a9-4ae9-a6e2-82f026c61329)

_官网的 Windows 下载选项_

大多数 Intel / AMD 电脑选择 **Windows 标准版**；Windows ARM 设备选择带有 **ARM** 标记的版本。如需不安装到系统的便携使用方式，再选择相同架构的便携版。

不确定设备架构时，打开 Windows 的“设置 → 系统 → 系统信息”，查看“系统类型”。

## 2. 安装并启动

1. 双击下载的安装程序；
2. Windows 显示用户账户控制提示时，确认文件来自官方渠道后选择继续；
3. 按安装向导完成安装；
4. 从开始菜单启动 Cherry Studio。

## 常见问题

### 提示缺少运行库

安装程序会检测与设备架构匹配的 Microsoft Visual C++ 运行库；缺少时会自动下载并安装。

如果自动下载或安装失败，请根据错误提示打开微软官方下载地址，完成安装后重新运行 Cherry Studio 安装程序：

* [x64 运行库](https://aka.ms/vs/17/release/vc_redist.x64.exe)
* [ARM64 运行库](https://aka.ms/vs/17/release/vc_redist.arm64.exe)

### 无法启动

先确认安装包的架构与设备匹配，并检查安全软件是否拦截。仍无法启动时，请在反馈中附上 Windows 版本、设备架构、安装包名称和完整错误提示。

## 下一步

看到 Cherry Studio 主界面后，继续完成快速开始。
