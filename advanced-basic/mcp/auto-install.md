# 自动安装 MCP

Cherry Studio 内置的 `@cherry/mcp-auto-install` 可以帮助模型发现 MCP 服务器、读取配置说明并生成启动命令。它适合在不确定包名或配置格式时作为安装助手使用。

{% hint style="warning" %}
该功能仍处于测试阶段。当前 V2 以 JSON 模式运行安装助手，它不会保证把生成的服务器配置直接写入 Cherry Studio。请把它理解为“发现与生成配置”，并在导入前人工检查结果。
{% endhint %}

## 工作流程

一次完整的辅助安装通常分为四步：

1. 模型使用安装助手搜索可用服务器并读取配置说明。
2. 安装助手返回建议的命令、参数和环境变量。
3. 你检查包来源和配置内容，再将 JSON 导入 Cherry Studio。
4. 在 MCP 设置中启用新服务器并检查工具与日志。

安装助手本身通过以下预设启动：

```text
npx -y @mcpmarket/mcp-auto-install connect --json
```

Cherry Studio 会管理它使用的本地注册表路径，无需手动填写 `MCP_REGISTRY_PATH`。

## 启用安装助手

1. 打开 **设置 → MCP 服务器**。
2. 在内置服务器中搜索 `@cherry/mcp-auto-install`。
3. 点击 **安装**，然后在已安装列表中启用它。
4. 在目标助手或智能体的工具设置中添加 `@cherry/mcp-auto-install`。
5. 选择支持工具调用的模型。

首次启动需要运行 NPX 包。Cherry Studio 会优先使用系统中的 NPX；如果不可用，会尝试内置 Bun。依赖异常时，可在 MCP 设置中运行依赖安装器并重启应用。

## 生成服务器配置

向模型说明用途、运行平台和输出格式，比只说“安装一个 MCP”更容易得到可用结果。例如：

```text
请使用 MCP 自动安装工具，查找一个可以只读访问本地 SQLite 数据库的 MCP 服务器。
我的系统是 macOS。

先说明包来源和所需权限，再生成可导入 Cherry Studio 的 JSON 配置。
不要替我启用服务器，也不要填写真实密钥。
```

安装助手可提供以下能力：

- 列出注册表中可发现的 MCP 服务器；
- 读取某个服务器的 README 和配置建议；
- 根据服务器生成命令、参数和环境变量；
- 管理安装助手自己的本地服务器注册信息。

模型返回配置后，至少检查：

- npm 包名、发布者和文档地址是否可信；
- `command` 与 `args` 是否和项目官方说明一致；
- 是否包含下载脚本、Shell 命令或不需要的高权限参数；
- 环境变量名称是否正确，是否仍有占位值；
- 服务器将访问哪些本地文件、网络服务或账号。

## 导入 Cherry Studio

让模型把结果整理成下面的结构，每次只保留一个服务器：

```json
{
  "mcpServers": {
    "example-server": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"],
      "env": {
        "EXAMPLE_API_KEY": "在 Cherry Studio 中替换"
      }
    }
  }
}
```

然后：

1. 打开 **设置 → MCP 服务器**。
2. 点击 **添加 → 从 JSON 导入**。
3. 粘贴已经检查过的配置。
4. 导入后打开服务器详情，替换占位值并保存。
5. 启用服务器，在 **工具**页检查实际暴露的工具。
6. 完成测试后，再把服务器添加到需要使用它的助手或智能体。

{% hint style="danger" %}
NPX 可以下载并执行第三方代码。不要仅凭模型推荐就运行陌生包，也不要把 API Key 直接发给模型。应先核对软件包、版本、源码或官方文档，再在 Cherry Studio 的服务器设置中填写密钥。
{% endhint %}

## 自定义搜索范围

安装助手默认从 `@modelcontextprotocol` npm scope 发现服务器。需要搜索其他 scope 时，在 `@cherry/mcp-auto-install` 的服务器详情中添加环境变量：

```text
MCP_PACKAGE_SCOPES=@modelcontextprotocol,@your-scope
```

多个 scope 使用英文逗号分隔。扩大搜索范围也会增加第三方包数量，应同时提高来源审核标准。

## 常见问题

### 对话中没有调用安装助手

确认 `@cherry/mcp-auto-install` 已启用并添加到当前助手或智能体，同时使用支持工具调用的模型。可以在提示词中明确要求“先调用 MCP 自动安装工具”。

### 提示找不到 NPX 或启动失败

在 MCP 设置中运行依赖安装器，然后重启 Cherry Studio。仍然失败时，打开服务器日志，检查 NPX、内置 Bun、网络代理和 npm registry。

### 找不到目标服务器

默认搜索范围有限。先确认包所在的 npm scope，再通过 `MCP_PACKAGE_SCOPES` 添加该 scope。也可以绕过自动安装，直接按项目官方文档[手动配置 MCP](config.md)。

### 已生成配置，但服务器列表没有新增

这是当前 JSON 模式下的正常情况。复制模型整理后的 `mcpServers` JSON，通过 **添加 → 从 JSON 导入** 完成安装。

### 导入后无法启用

安装助手生成的是建议配置，仍可能缺少路径、密钥或平台参数。根据目标服务器的官方文档修正配置，并参考 [MCP 服务器常见问题](faq.md) 检查日志。

## 相关文档

- [`@mcpmarket/mcp-auto-install` 包说明](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install)
- [配置和使用 MCP](config.md)
- [内置 MCP 服务器](builtin.md)
- [MCP 服务器常见问题](faq.md)
- [反馈与建议](../../question-contact/suggestions.md)
