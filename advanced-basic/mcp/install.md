# MCP 环境安装

Cherry Studio 可以管理两种常用的 MCP 运行时：

- **UV**：运行通过 `uv` 或 `uvx` 启动的 Python MCP 服务器；
- **Bun**：运行 JavaScript 工具，并在系统没有 NPX 时作为部分 NPX 服务器的后备运行时。

{% hint style="info" %}
不是所有 MCP 服务器都需要安装 UV 和 Bun。远程 SSE / Streamable HTTP 服务器，以及多数 Cherry Studio 内置服务器，不依赖这两个运行时。请根据服务器文档中的 `command` 决定需要安装什么。
{% endhint %}

## 使用应用内安装器

1. 打开 **设置 → 环境依赖**。
2. 找到 **UV** 或 **Bun**。
3. 对显示为 **未安装** 的项目点击 **安装**。
4. 等待状态变为 **已安装**。

MCP 服务器页在缺少环境依赖时也会显示警告入口，点击后会跳转到同一个环境依赖页面。

应用内安装器会下载适合当前操作系统与 CPU 架构的可执行文件，并保存到 Cherry Studio 的私有目录：

{% tabs %}
{% tab title="Windows" %}
`C:\Users\<用户名>\.cherrystudio\bin`
{% endtab %}

{% tab title="macOS / Linux" %}
`~/.cherrystudio/bin`
{% endtab %}
{% endtabs %}

安装完成后，可以点击依赖项旁边的文件夹图标打开该目录。

## 系统命令与私有运行时

运行 STDIO 服务器时，Cherry Studio 的查找顺序是：

### `uv` 和 `uvx`

1. 先在登录 Shell 环境中查找系统安装的 `uv` 或 `uvx`；
2. 找不到时，再使用 `~/.cherrystudio/bin` 中由 Cherry Studio 安装的 UV。

### `npx`

1. 先在登录 Shell 环境中查找系统安装的 `npx`；
2. 找不到时，再尝试使用 Cherry Studio 安装的 Bun 运行该包。

因此，已经正确安装在系统 PATH 中的 UV、UVX 或 NPX 也可以被使用。**环境依赖**页面的“已安装”状态只检查 Cherry Studio 私有目录，不代表系统命令一定不可用。

{% hint style="warning" %}
如果刚刚在系统中安装或修改了 Node.js、NPX、UV 或 UVX，请完全退出并重新打开 Cherry Studio，让应用重新读取登录 Shell 环境。
{% endhint %}

## 如何判断需要哪个运行时

查看 MCP 开发者提供的配置：

| 配置中的命令 | 需要的环境 |
| --- | --- |
| `uvx` 或 `uv` | UV |
| `npx` | Node.js 提供的 NPX，或 Cherry Studio 的 Bun 后备 |
| `bun` 或 `bunx` | Bun |
| `node` | 系统 Node.js |
| 其他命令 | 按开发者文档安装对应程序 |
| 只有远程 URL | 通常不需要本地运行时 |

Cherry Studio 的环境依赖页不会安装 Node.js 或任意第三方系统命令。

## 手动安装作为兜底

如果应用内下载失败，可以按运行时的官方文档在系统中安装：

- [UV 官方安装说明](https://docs.astral.sh/uv/getting-started/installation/)
- [Bun 官方安装说明](https://bun.com/docs/installation)
- [Node.js 下载](https://nodejs.org/en/download)

安装后在系统终端验证：

```bash
uv --version
bun --version
npx --version
```

只需要验证实际会使用的命令。验证成功后重启 Cherry Studio，再启用 MCP 服务器。

高级用户也可以把与当前系统和架构匹配的可执行文件放入 `~/.cherrystudio/bin`，Windows 则使用对应用户目录。不要从不可信来源下载二进制文件。

## 常见问题

### 点击安装后失败

依次检查：

- 当前网络能否访问运行时下载源；
- 代理、防火墙或安全软件是否拦截 Cherry Studio；
- 用户目录是否有写入权限；
- 操作系统与 CPU 架构是否有对应安装包；
- 磁盘空间是否充足。

### 已安装，但服务器仍提示找不到命令

确认服务器详情中的 **命令** 拼写正确，例如 `uvx` 不要写成完整的参数串。参数应逐行填写在 **参数** 字段。

如果使用系统安装的命令，在终端验证后重启 Cherry Studio。如果使用应用内运行时，打开依赖项目录确认对应可执行文件存在。

### UV 和 Bun 都已安装，服务器仍无法启动

运行时只负责启动程序，不能修复错误参数、缺少 API Key 或服务器自身故障。打开 MCP 服务器详情中的日志，并参考 [MCP 服务器常见问题](faq.md)。

## 相关文档

- [MCP 使用教程](README.md)
- [配置和使用 MCP](config.md)
- [MCP 服务器常见问题](faq.md)
- [反馈与建议](../../question-contact/suggestions.md)
