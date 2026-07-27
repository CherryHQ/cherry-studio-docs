# GitHub Copilot

Cherry Studio 可以通过 GitHub 设备授权连接你的 Copilot 账号，并读取该账号当前可用的模型。你不需要手动创建 API Key，但 GitHub 账号必须具备有效的 Copilot 使用资格。

{% hint style="info" %}
GitHub Copilot、GitHub Models 和 GitHub Copilot CLI 是三个不同入口。本页介绍的是 `设置 → 模型服务 → GitHub Copilot`，用于在 Cherry Studio 对话中调用 Copilot 模型。
{% endhint %}

## 使用前确认

开始前请确认：

1. 已有可以正常登录的 GitHub 账号；
2. 账号已经启用 Copilot Free、Student、Pro、Pro+、Max，或由组织分配 Business / Enterprise 权限；
3. 组织或企业策略没有禁止相关模型或 Copilot 功能；
4. 当前网络能够访问 GitHub 登录与 Copilot 服务；
5. 了解当前方案的模型范围和 [GitHub AI Credits](https://docs.github.com/en/copilot/concepts/billing) 规则。

不同方案的模型、额度与计费规则会变化。Cherry Studio 会从 Copilot 接口同步账号当前可见且未被策略禁用的模型，不应以旧版教程中的固定模型清单为准。

GitHub Copilot Free 和 Student 目前主要通过自动模型选择提供有限模型访问；付费方案和组织方案的可选模型更多，但仍受账号、地区、组织策略和 GitHub 当前发布状态影响。

## 在 Cherry Studio 授权

1. 打开 `设置 → 模型服务`；
2. 将左侧筛选切换为**全部服务商**；
3. 选择 **GitHub Copilot**；
4. 点击**开始授权**；
5. 等待 Cherry Studio 生成 Device Code；
6. 复制授权码。应用通常会自动复制，也可以手动复制；
7. 点击**打开授权页面**；
8. 在浏览器中登录准备使用的 GitHub 账号；
9. 输入 Device Code 并确认授权；
10. 返回 Cherry Studio；
11. 点击**连接 GitHub**完成连接。

连接成功后，页面会显示 GitHub 用户名和头像，并自动启用服务商。

{% hint style="warning" %}
浏览器中已经登录的账号不一定是准备连接的账号。授权前检查用户名，尤其是在个人账号、工作账号和企业托管账号之间切换时。
{% endhint %}

## 授权过程中发生了什么

Cherry Studio 采用 GitHub Device Flow：

1. 向 GitHub 请求临时 Device Code；
2. 由你在 GitHub 页面确认授权；
3. 用授权结果换取 GitHub 访问令牌；
4. 再获取可用于 Copilot 请求的临时令牌；
5. 把 GitHub 访问令牌通过系统安全存储加密后保存在本机；
6. 后续同步模型或对话时刷新 Copilot 令牌。

因此，“GitHub 页面授权成功”只是第一步。Cherry Studio 还需要成功取得 Copilot 令牌，才能显示连接成功。

{% hint style="danger" %}
Device Code、访问令牌和 Copilot 令牌都不应发送给他人，也不要出现在文档、聊天、代码仓库或截图中。授权码虽然是临时的，仍可能在有效期内被滥用。
{% endhint %}

## 同步模型

授权成功后：

1. 确认 GitHub Copilot 服务商已开启；
2. 点击**添加**或同步模型；
3. 检查同步预览；
4. 应用变更；
5. 只启用准备使用的模型；
6. 对每个模型运行健康检查。

Cherry Studio 会访问 Copilot 的 `/models` 接口，并过滤：

- GitHub 策略标记为不可用的模型；
- 账户路由等非直接模型条目；
- 语音、转写等当前不适合对话列表的模型。

模型突然增加、减少或更名，通常由 GitHub 方案、组织策略或服务端发布变化引起。重新同步即可获取当前列表。

## 方案、模型与费用

GitHub Copilot 的使用量由 GitHub 账号负责计量，不会因为从 Cherry Studio 发起而变成免费调用。

- 不同方案包含不同的 GitHub AI Credits；
- 模型消耗取决于输入、输出、缓存 token 和模型价格；
- 组织或企业可以设置共享额度、用户预算和额外使用限制；
- 额度耗尽时，调用可能被阻止或产生额外费用；
- 部分旧年度方案在到期前仍可能使用旧的 premium request 计量。

模型是否出现在 Cherry Studio 中，不代表它在你的方案下成本相同。使用前请在 GitHub 账单和 Copilot 使用页面确认。

## 速率限制

GitHub Copilot 服务商页面提供 1–60 的**速率限制**滑块，默认值为 10。它控制 Cherry Studio 连续请求该服务商时的最小等待时间，单位为秒。

- 日常对话建议先保留默认值；
- 出现频率限制时，提高该值；
- 需要快速连续测试时可以降低，但不能绕过 GitHub 服务端限制；
- 多窗口、自动任务或并发请求仍可能累积到账号限制。

GitHub 自身还会根据容量、公平使用和滥用防护实施服务端限流。遇到限流时，应等待后重试，并检查使用量和方案，而不是持续快速重发。

## 选择模型与能力

### 普通对话

先选择模型列表中当前可用的模型，发送一条简短消息。基础对话成功后，再测试长上下文、图片或工具。

### 视觉理解

Cherry Studio 会为 Copilot 请求附带视觉支持请求头，但实际能否处理图片仍取决于具体模型和账号权限。

1. 选择明确支持图片的模型；
2. 上传一张小图片；
3. 确认模型真正理解图片内容；
4. 再测试多图或高分辨率图片。

同一个模型在 GitHub 更新前后可能出现能力差异，应以当前健康检查和实际结果为准。

### MCP 与工具调用

Cherry Studio MCP 需要模型支持结构化 Tool Calling。

1. 先完成普通对话；
2. 只启用一个简单 MCP 工具；
3. 明确要求模型调用工具；
4. 检查是否真正产生结构化调用；
5. 确认工具结果回传后模型能够继续回答；
6. 再逐步增加工具数量。

账号能使用 Copilot，不代表所有可见模型都支持工具。若模型只描述“将调用工具”却没有实际调用，应换用工具能力更强的模型。

### 思考与参数

不同 Copilot 模型使用的推理参数并不相同。Cherry Studio 会按模型识别应用相应配置，但服务端模型更新可能早于客户端识别规则。

遇到参数错误时：

1. 将思考选项恢复为**默认**；
2. 清除自定义参数；
3. 重新同步模型；
4. 重试健康检查；
5. 再逐项启用需要的参数。

## PDF 与附件

当前 V2 会先在本地提取 PDF 文本，再通过 Copilot 的 OpenAI 兼容接口发送给模型：

- 文本型 PDF 通常可以处理；
- 扫描件需要先做 OCR；
- 表格、复杂排版和图片信息可能丢失；
- 提取文本会消耗上下文和 GitHub AI Credits；
- PDF 中的图片需要单独发送给视觉模型。

上传文件前应确认内容符合组织的数据使用与保密要求。Copilot 是云端服务，请勿把它当作本地离线模型。

## 组织与企业账号

组织或企业可以控制 Copilot 功能、模型和网络访问。即使账号显示已分配 Copilot，也可能因为策略无法使用部分模型。

遇到组织账号问题时，请让管理员检查：

- 用户是否已分配 Copilot 席位；
- Copilot Chat 和相关模型是否启用；
- 是否有模型级策略限制；
- 预算或 GitHub AI Credits 是否耗尽；
- 企业网络是否只允许特定 Copilot 订阅端点；
- 防火墙、代理或 TLS 检查是否阻断 GitHub Copilot。

组织政策会应用到使用该身份认证的多个入口，不只 Cherry Studio。

## 代理与网络

授权和模型调用至少需要访问 GitHub 登录、GitHub API 与 Copilot 服务。公司代理、防火墙、VPN 或安全软件可能只放行部分地址，导致：

- Device Code 无法生成；
- 浏览器授权成功，但 Cherry Studio 连接失败；
- 可以获取用户信息，但无法获取 Copilot 令牌；
- 模型列表为空；
- 对话请求超时或被拒绝。

优先使用 Cherry Studio 当前支持的系统代理或 HTTP 代理，并让网络管理员按 [GitHub Copilot allowlist](https://docs.github.com/en/copilot/reference/copilot-allowlist-reference) 放行所需地址。

不要随意添加来源不明的自定义请求头。GitHub Copilot 页面提供的请求头编辑能力主要用于特殊代理或兼容场景，错误的 `Authorization`、`Host`、客户端标识或路由头可能导致认证失败。

## 退出与更换账号

要切换账号：

1. 在 GitHub Copilot 服务商页面点击**退出 GitHub**；
2. 确认用户名和头像已清除；
3. 在浏览器中切换到目标 GitHub 账号；
4. 重新执行设备授权；
5. 重新同步模型。

Cherry Studio 退出会删除本机保存的 Copilot 凭据和服务商密钥，但不等同于撤销 GitHub 账号中的 OAuth 授权。若设备丢失或怀疑凭据泄露，还应在 GitHub 的授权应用设置中撤销访问，并检查账号安全记录。

## 常见问题

### 获取 Device Code 失败

检查网络、代理、防火墙与 GitHub 服务状态。确认系统时间正确，并关闭可能拦截 GitHub 登录请求的安全软件后重试。

### GitHub 页面已授权，但连接失败

Cherry Studio 还未取得 GitHub 或 Copilot 令牌。返回应用后点击**连接 GitHub**；若超时，重新生成 Device Code，不要重复使用旧码。

### 显示用户名，但无法同步模型

GitHub 登录有效不代表账号具备 Copilot 权限。检查 Copilot 方案、组织席位、模型政策和使用额度，然后退出并重新授权。

### 模型列表为空

账号可能只有自动模型选择权限、组织禁用了模型，或 Copilot `/models` 请求被网络拦截。先在 GitHub 官方 Copilot 页面确认账号可用，再重新同步。

### 某个模型突然消失

GitHub 可能调整了模型发布状态、方案范围或组织策略。重新同步并检查 GitHub 当前模型清单。

### 返回 401 或 403

凭据过期、授权被撤销、账号没有 Copilot 权限或组织政策拒绝访问。退出后重新授权；仍失败时检查账号方案和管理员策略。

### 返回 429 或频率限制

等待后重试，提高 Cherry Studio 的速率限制值，并检查 GitHub AI Credits、预算与服务端限流状态。

### 图片或 MCP 不可用

确认所选模型支持相应能力。基础对话成功不代表模型支持视觉或工具调用。

### 公司网络中无法使用

让网络管理员检查 Copilot allowlist、订阅专属域名、代理身份验证和 TLS 检查。不要通过关闭全部安全策略解决问题。

更多一般设置请参阅[模型服务](README.md)和[模型服务设置](../settings/providers.md)。Copilot 方案、用量与策略请参阅 [GitHub Copilot 官方文档](https://docs.github.com/en/copilot)；意见反馈渠道请参阅[反馈与建议](../../question-contact/suggestions.md)。
