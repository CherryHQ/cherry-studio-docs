---
icon: radio
---

# 频道（Cherry Claw）

频道（在产品内的代号是 **Cherry Claw**）让你把已经训练好的 [Cherry Agent](agent.md) 接入到 IM 平台，作为机器人与真实用户对话。当前 v1.9.9 支持的平台：

* **飞书 / Lark**（中国版 + 国际版）
* **Telegram**
* **QQ**（官方机器人 API）
* **微信**（通过 iLink Bot API）
* **Discord**
* **Slack**

### 前置要求

1. 已完成 [Cherry Agent](agent.md) 创建与测试
2. 已启用 [API 服务器](api-server.md)
3. 拥有目标平台的机器人凭据（每个平台不同，详见下方"按平台准备凭据"）

### 频道在哪儿

打开 `设置 → 频道`，可以看到所有支持平台的列表：

<figure><img src="../.gitbook/assets/cherry-channels-list.png" alt=""><figcaption><p>频道菜单：每个平台都有一行简介，未绑定时右侧为空态</p></figcaption></figure>

### 创建一个频道（以飞书为例）

1. 在左侧列表中点击 **飞书**
2. 在右侧空态点击 **+ 添加**，弹出添加表单：

<figure><img src="../.gitbook/assets/cherry-channels-feishu-form.png" alt=""><figcaption><p>飞书频道字段</p></figcaption></figure>

各字段含义：

| 字段 | 说明 |
|---|---|
| **名称** | 频道的展示名，便于在多频道时辨识 |
| **绑定 Agent** | 选择一个已创建的 Cherry Agent。若不绑定，则使用通用模型回复 |
| **应用 ID / 应用密钥** | 飞书开放平台 → 自建应用 → 凭证与基础信息 |
| **加密密钥 / 验证令牌** | 飞书开放平台 → 事件订阅，可选 |
| **域名** | `飞书（中国）` / `Lark（国际版）`，二选一 |
| **允许的聊天 ID** | 留空表示不限制；填入则只在指定群/单聊中响应 |
| **频道权限模式** | `继承智能体设置` / 自定义。建议保持继承 |

填写完毕后点击 **保存**。频道启用后会自动开始订阅飞书消息事件。

### 按平台准备凭据

#### 飞书 / Lark

* 在 [开放平台](https://open.feishu.cn) 创建一个 **自建应用**
* 复制 **App ID** 与 **App Secret**
* 在 **事件订阅** 中**启用长连接（WebSocket）**，无需公网回调
* 在 **权限管理** 中至少开启：接收单聊消息、接收群聊消息、发送消息

#### Telegram

* 与 [@BotFather](https://t.me/BotFather) 对话，`/newbot` 创建机器人
* 复制 **Bot Token**
* 表单中填入 Bot Token 即可

#### Discord

* 在 [Discord Developer Portal](https://discord.com/developers/applications) 新建 Application
* 在 Bot 子页生成 **Bot Token**
* 邀请机器人到你的服务器
* 表单填入 Bot Token

#### Slack

* 在 [Slack API](https://api.slack.com/apps) 新建 App
* 启用 Socket Mode，生成 App-Level Token + Bot Token
* 表单填入两个 Token

#### QQ

* 在 QQ 开放平台申请机器人 → 创建应用 → 复制 **AppId** 与 **ClientSecret**
* 表单填入这两个字段

#### 微信

* 通过 iLink Bot API 申请微信机器人接入凭据
* 在 `token 路径` 字段填入 token 文件本地路径

### 一个 Agent 可以接多个频道吗？

可以。你可以让同一个"研报助手"Agent 同时接入飞书内部群（向同事汇报）和你的 Telegram 私聊（向自己推送），互不干扰。每个频道独立维护会话与权限。

### 与定时任务联动

* 频道可以 **接收** 用户消息触发 Agent 回复
* [定时任务](scheduled-tasks.md) 可以 **主动** 调用 Agent 并通过频道把结果发送到 IM 平台
* 二者组合可实现完整的"日报机器人"形态

### 常见问题

#### 添加后机器人没反应

* 确认 [API 服务器](api-server.md) 处于 **运行中** 状态
* 确认绑定的 Agent 模型 Provider 余额充足
* 检查"允许的聊天 ID"是否填错（留空表示不限）

#### 飞书机器人加入群但收不到 @ 消息

* 在飞书开放平台 → 权限管理，确认开启了"获取群组中的所有消息"
* 在群中右键机器人 → 设置，开启"机器人可在本群被 @"

#### 微信频道掉线

* 微信机器人接入相对脆弱，建议优先使用飞书 / Telegram
* 长期未用会被微信主动下线，重新登录 iLink 即可

{% hint style="warning" %}
不同平台对自建机器人有不同的合规要求。在企业内部群启用前请确认已获取所在组织 / 平台的许可。
{% endhint %}

如遇问题，请在 [反馈与建议](../question-contact/suggestions.md) 中提交反馈。
