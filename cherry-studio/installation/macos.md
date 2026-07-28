---
icon: apple
---

# macOS 安装

## 1. 确认芯片类型

点击 ` → 关于本机`：

| Mac | 安装包 |
|---|---|
| Apple M1、M2、M3、M4 等 | `arm64.dmg` |
| Intel 处理器 | `x64.dmg` |

从[官方下载页](https://cherryai.com.cn/download)或 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 下载对应安装包。

## 2. 安装应用

1. 双击打开 `.dmg`；
2. 把 Cherry Studio 图标拖到 **Applications（应用程序）**；
3. 等待复制完成；
4. 从“应用程序”文件夹启动 Cherry Studio。

不要长期从 DMG 窗口直接运行应用，否则更新、权限和数据保存可能出现异常。

## 3. 首次启动与安全提示

如果 macOS 阻止打开：

1. 先确认安装包来自 CherryHQ 官方下载地址；
2. 打开 `系统设置 → 隐私与安全性`；
3. 在安全提示附近选择 **仍要打开**；
4. 再次确认启动。

只有确认文件来源可信时才应绕过 Gatekeeper。不要执行来源不明的终端命令来解除系统安全限制。

Cherry Studio 需要访问文件夹、麦克风或通知时，macOS 会按功能分别询问权限。只授予当前确实需要的权限，之后可在“隐私与安全性”中修改。

## 常见问题

### 提示应用已损坏或无法验证开发者

先重新从官方渠道下载与芯片匹配的安装包，并确认下载完整。仍然失败时，请记录 macOS 版本、芯片类型、应用版本和完整提示，再通过反馈渠道报告。

### 下载了错误架构

删除错误版本，重新下载对应芯片的 DMG。Apple Silicon 设备虽然可能通过 Rosetta 运行 x64 应用，但优先使用 arm64 原生版本。

## 成功标志与下一步

看到 Cherry Studio 主界面即表示客户端安装成功。接着按[快速开始](../../getting-started/quick-start.md)添加一个对话模型并发送测试消息。
