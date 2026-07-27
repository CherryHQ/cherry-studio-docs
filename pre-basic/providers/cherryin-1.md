---
icon: cherries
---

# CherryIN

CherryIN 是 Cherry Studio 内置的模型服务商模板，可以通过一个账户接入多种模型。V2 为它预设了 OpenAI Chat Completions 与 Anthropic Messages 端点，并提供账户登录、余额显示、充值入口和线路切换。

{% hint style="info" %}
CherryIN 与 [CherryAI 免费试用](cherryai/)不同。CherryIN 使用你自己的账户、凭证和余额；CherryAI 是应用内试用来源，不会出现在常规模型服务列表中。
{% endhint %}

## 选择登录方式

打开 `设置 → 模型服务 → CherryIN`。你可以使用以下任一方式。

### 方式一：登录 CherryIN 账户

1. 点击**登录 CherryIN**；
2. 在浏览器中完成登录和授权；
3. 返回 Cherry Studio；
4. 确认页面显示账户信息和余额；
5. 检查 CherryIN 顶部开关是否已经打开。

授权成功后，Cherry Studio 会获取账户可用的 API Key，并把 OAuth 获取的 Key 添加到 CherryIN 配置中。需要充值时，可以使用账户卡片中的**充值**按钮打开 CherryIN 控制台。

### 方式二：手动填写 API Key

1. 打开 [CherryIN Key 管理](https://open.cherryin.ai/console/token)；
2. 创建或复制一个可用 Key；
3. 返回 Cherry Studio 的 CherryIN 页面；
4. 在 API Key 区域添加该 Key；
5. 打开服务商开关。

{% hint style="danger" %}
不要把 API Key 粘贴到聊天消息、文档或问题截图中。需要排查时，只保留经过遮挡的前后少量字符。
{% endhint %}

## 选择连接线路

CherryIN 在 V2 中提供三组域名：

| 页面选项 | 域名 | 建议 |
|---|---|---|
| 加速线路 | `open.cherryin.cc` | 在中国大陆网络环境中优先尝试 |
| 国际线路 | `open.cherryin.net` | 海外或国际网络环境中优先尝试 |
| 备用线路 | `open.cherryin.ai` | 主线路暂时无法访问时尝试 |

如果页面显示线路下拉框，切换线路会同时替换该服务商各端点的域名，并保留原有路径。没有下拉框时，可以在接口地址区域检查当前 Base URL。

{% hint style="warning" %}
线路名称只表示预设入口，不保证在所有网络中速度相同。选择后请运行连接检查，以实际结果为准。
{% endhint %}

## 同步并启用模型

1. 在**模型列表**区域点击**添加**；
2. 查看同步预览中的新增、更新和移除项；
3. 应用变更；
4. 搜索准备使用的模型；
5. 打开目标模型的开关；
6. 运行模型健康检查。

CherryIN 的模型清单、价格和可用额度会调整，因此本文不写死具体模型。请查看 [CherryIN 模型与价格](https://open.cherryin.ai/pricing)，并以客户端同步结果为准。

## 接口与模型

CherryIN 模板预设 OpenAI 与 Anthropic 兼容端点。Cherry Studio 会结合模型信息和端点类型发送请求。

- 普通对话模型通常使用 OpenAI 兼容接口；
- Claude 等模型可使用 Anthropic 兼容接口；
- 部分 Gemini 或图像模型会使用专用路由；
- 同名模型由不同端点提供时，能力和参数可能不同。

不要仅凭模型名称判断 Agent、视觉、推理或工具调用能力。请查看模型标签并完成实际测试。

## 验证配置

建议依次完成：

1. 在鉴权区域运行连接检查；
2. 在模型列表运行健康检查；
3. 回到对话界面选择目标模型；
4. 发送一条简单文本消息；
5. 如果需要图片或工具调用，再分别进行最小测试。

只有服务商开关和模型开关都启用时，模型才会出现在模型选择器中。

## 账户与退出

通过账户登录后，Cherry Studio 可以显示 CherryIN 账户信息与余额。点击**退出登录**会清除本机保存的 CherryIN OAuth 登录状态，并移除由 OAuth 添加的 Key。

手动添加的 Key 与 OAuth Key 是不同来源。如果仍需使用手动 Key，请在退出后确认它仍处于启用状态。

## 常见问题

### 登录后没有返回 Cherry Studio

保留 Cherry Studio 运行，并在浏览器中重新完成授权。如果系统阻止了应用链接回调，请允许浏览器打开 Cherry Studio。

### 登录成功，但模型列表为空

先点击**添加**。如果仍为空，检查账户是否有可用 Key、当前线路是否可访问，以及 CherryIN 控制台是否向账户开放模型。

### 返回 401 或 403

Key 可能已失效、被停用或没有模型权限。重新登录，或在 Key 管理页面创建新 Key 后替换。

### 请求超时或无法连接

切换加速、国际或备用线路，然后重新运行连接检查。还应检查系统代理、防火墙和本地网络。

### Claude 或 Agent 请求失败

确认选择的模型带有工具调用能力，并检查请求是否使用 Anthropic 兼容端点。服务商支持 Anthropic 端点，不代表其中每个模型都支持 Agent。

更多通用配置与多 Key 说明见[模型服务](README.md)和[模型服务设置](../settings/providers.md)。仍无法使用时，提交 Cherry Studio 版本、操作系统、模型 ID 和脱敏后的错误信息，反馈渠道见[反馈与建议](../../question-contact/suggestions.md)。
