---
icon: windows
---

# Windows 安装

## 1. 选择安装包

从[官方下载页](https://cherryai.com.cn/download)或 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 下载：

| 设备 | 安装包 |
|---|---|
| 大多数 Intel / AMD 电脑 | `x64-setup.exe` |
| Windows ARM 设备 | `arm64-setup.exe` |
| 不希望安装 | 与设备架构匹配的 `portable.exe` |

不确定架构时，打开 `设置 → 系统 → 系统信息 → 系统类型`。Windows 7 不受支持。

## 2. 完成安装

1. 双击下载的安装程序；
2. Windows 弹出用户账户控制提示时，确认发布者和文件来源后选择 **是**；
3. 按安装向导完成安装；
4. 从开始菜单或桌面启动 Cherry Studio。

如果 Windows SmartScreen 显示保护提示，请先确认文件来自 CherryHQ 官方下载地址，再选择 **更多信息 → 仍要运行**。来源不明的安装包不要继续。

## 3. 常见问题

### 提示缺少 Visual C++ 运行库

按提示安装 Microsoft Visual C++ Redistributable，完成后重新启动 Cherry Studio。仍然失败时，可从 Microsoft 官方页面重新安装对应架构的运行库。

### 安装版和便携版怎么选？

* **安装版**：适合日常使用，开始菜单、卸载和更新体验更完整；
* **便携版**：适合临时测试。数据目录和自动更新行为可能与安装版不同，迁移前请先备份。

### 双击后没有反应

确认安装包架构正确，并检查安全软件是否拦截。仍无法启动时，请在反馈中提供 Windows 版本、芯片架构、安装包文件名和错误截图。

## 成功标志与下一步

看到 Cherry Studio 主界面即表示客户端安装成功。接着按[快速开始](../../getting-started/quick-start.md)添加一个对话模型并发送测试消息。
