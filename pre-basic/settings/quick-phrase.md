---
icon: zap
---

# 快捷短语

快捷短语（Quick Phrase）是一组**预设的对话模板**，可在对话框中通过快捷菜单一键调用，避免重复输入。

### 添加快捷短语

打开 `设置 → 快捷短语`：

<figure><img src="../../.gitbook/assets/cherry-quickphrase.png" alt=""><figcaption><p>快捷短语管理面板</p></figcaption></figure>

1. 点击 **+ 添加快捷短语**
2. 填写：
   * **标题**：在调用菜单中显示的名字（如"翻译成英文"、"代码 review"）
   * **内容**：实际插入对话框的文本，可包含变量（见下）
3. 保存

### 在对话框中使用

* 在 [对话界面](../../cherrystudio/preview/chat.md) 的输入工具栏中，点击 ⚡ **快捷短语** 图标
* 选择你想用的短语 → 内容会自动插入到当前输入框
* 可在插入后继续编辑，再按发送

### 内容中支持的变量

| 变量 | 含义 |
|---|---|
| `{{clipboard}}` | 当前剪贴板内容 |
| `{{selection}}` | 当前选中文字（如来自 [划词助手](../../cherrystudio/preview/kuai-jie-zhu-shou.md#hua-ci-zhu-shou)） |
| `{{date}}` | 今天的日期 |
| `{{time}}` | 当前时间 |

具体支持的变量可能随版本变化，以应用内提示为准。

### 排序与编辑

* 拖拽列表项可调整顺序
* 点击短语行的 ✏️ 图标编辑、🗑 删除

### 提示与技巧

* 写一条"**根据下面的代码做 review，按 严重度 / 类型 / 修复建议 三列汇总：\n\n{{clipboard}}**"，复制代码后一键发出
* 与 [快捷助手](../../cherrystudio/preview/kuai-jie-zhu-shou.md) 配合使用：快捷助手吃剪贴板，快捷短语提供模板
* 多个短语可形成你的"提示词工程库"，建议按场景分类命名

如遇问题，请在 [反馈与建议](../../question-contact/suggestions.md) 中提交反馈。
