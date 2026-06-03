---
icon: text-cursor-input
---

# 划词助手

划词助手（Selection Assistant）让你在**任意应用中选中文字**后，通过浮动工具栏调用 AI 做翻译/解释/改写/总结等操作，无需把内容粘贴回 Cherry Studio。

{% hint style="info" %}
**与 [快捷助手](kuai-jie-zhu-shou.md) 的区别**：

* **快捷助手**：用快捷键唤起一个**主动输入**窗口，你打字提问
* **划词助手**：选中文字后**自动浮出工具栏**，针对所选内容做操作
{% endhint %}

### 启用划词助手

打开 `设置 → 划词助手`：

<figure><img src="../../.gitbook/assets/cherry-selection-assistant.png" alt=""><figcaption><p>划词助手设置面板</p></figcaption></figure>

1. 打开 **启用划词助手** 开关
2. （macOS）首次启用会请求**辅助功能（Accessibility）权限** —— 必须在系统偏好设置中授予，划词助手才能监听全局选区
3. （可选）配置触发方式：
   * **选中即弹**：选中文字后立即弹出工具栏（默认）
   * **快捷键触发**：选中文字后按指定快捷键才弹（避免误触）

### 使用

1. 在任意应用（浏览器、邮件、PDF、IM 等）中选中一段文字
2. 浮动工具栏出现，包含若干预设操作（翻译、解释、改写、总结…）
3. 点击操作 → Cherry Studio 唤起小窗，把所选文字作为输入并按预设提示词处理

### 自定义操作

在 `设置 → 划词助手` 中可：

* 编辑内置操作的提示词
* 添加自定义操作（命名 + 提示词 + 默认模型）
* 调整操作在工具栏中的顺序

### 使用的模型

划词助手默认使用 [全局默认对话模型](../../pre-basic/settings/default-models.md)，也可针对每个操作单独指定模型。

### 提示与技巧

* macOS 上如划词工具栏不出现，检查 `系统设置 → 隐私与安全性 → 辅助功能` 中 Cherry Studio 是否打勾
* Windows 上无需特殊权限，开箱即用
* 把"翻译为中文 / 翻译为英文 / 改写为更正式"这三个高频操作排在工具栏前面，效率最高
* 配合 [快捷短语](../../pre-basic/settings/quick-phrase.md) 中的 `{{selection}}` 变量可做更复杂的链式处理

如遇问题，请在 [反馈与建议](../../question-contact/suggestions.md) 中提交反馈。
