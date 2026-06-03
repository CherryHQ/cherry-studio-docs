# Anthropic

Anthropic 的 Claude 是当前最适合作为 [Cherry Agent](../../advanced-basic/agent.md) 后端的模型之一，因为 Agent 需要 Anthropic 协议端点。

## 获取 API Key

* 前往 [Anthropic Console](https://console.anthropic.com/) 注册账号
* 进入 `Settings → API Keys` → `Create Key`，复制生成的 `sk-ant-...` 密钥

## 在 Cherry Studio 配置

* 打开 `设置 → 模型服务`，找到 **Anthropic** Provider 进入详情页
* 在 **API 密钥** 中填入 `sk-ant-...`
* **API 地址** 默认 `https://api.anthropic.com`，无需修改
* 点击 **获取模型列表**，添加 `claude-opus-4`、`claude-sonnet-4`、`claude-haiku-4` 等模型

## 推荐用法

| 模型 | 适合场景 |
|---|---|
| `claude-opus-4` | 最强推理 / 编程 / 复杂 Agent 任务 |
| `claude-sonnet-4` | 通用对话与日常 Agent，性价比首选 |
| `claude-haiku-4` | 高吞吐场景、低成本快速回复 |

## Agent 场景配置

把该 Provider 在 [Cherry Agent](../../advanced-basic/agent.md) 配置时选为默认模型来源，即可直接获得 Anthropic 协议 Agent 能力。

{% hint style="info" %}
* 中国大陆无法直接访问 Anthropic API，需自备代理（参考 [常规设置 → 代理模式](../settings/general.md)）
* 订阅了 Claude Code 的用户也可用同一 key + endpoint 接入 Cherry Studio
* Claude 模型按 token 计费，长上下文请关注用量
{% endhint %}
