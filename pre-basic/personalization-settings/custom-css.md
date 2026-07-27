---
icon: file-code
---

# 自定义 CSS

自定义 CSS 可以覆盖 Cherry Studio 的界面样式，适合调整内置设置没有提供的颜色、间距、圆角和组件外观。

{% hint style="warning" %}
自定义 CSS 属于进阶功能。应用升级后，组件结构、类名和变量可能变化；一段当前有效的样式不保证在后续版本中继续生效。
{% endhint %}

## 什么时候需要使用

在编写 CSS 前，先检查**设置 > 通用设置 > 显示与语言**。V2 已内置以下选项：

- 浅色、深色和跟随系统主题；
- 主题强调色；
- 界面缩放；
- 全局字体和代码字体；
- 话题位置与显示方式。

这些内置选项更稳定，也能直接重置。只有内置设置无法实现目标时，再使用自定义 CSS。

## 打开 CSS 编辑器

1. 点击 Cherry Studio 左下角的**设置**。
2. 进入**通用设置**。
3. 在第二级菜单中选择**自定义 CSS**。
4. 在编辑器中输入或粘贴 CSS。

编辑内容会保存到本地设置，并在内容变化后应用到界面，无需单独点击保存按钮。

建议先保留当前 CSS 的副本，再逐段修改。每添加一小段就检查聊天、设置、弹窗和辅助窗口，发生异常时更容易定位。

## 从最小样式开始

下面的示例只调整用户消息背景和常用圆角：

```css
:root {
  --chat-background-user: rgba(0, 185, 107, 0.08);
  --list-item-border-radius: 12px;
}
```

若要分别设置浅色和深色主题，可以使用根元素的主题类：

```css
:root:not(.dark) {
  --chat-background-user: rgba(0, 120, 80, 0.08);
}

:root.dark {
  --chat-background-user: rgba(90, 220, 160, 0.12);
}
```

{% hint style="info" %}
Cherry Studio V2 使用 `.light` / `.dark` 类表示当前主题。旧主题中常见的 `body[theme-mode="dark"]` 写法不应再作为新样式的基础。
{% endhint %}

## 常用语义变量

优先覆盖语义变量，比直接定位内部类名更不容易失效。

| 变量 | 作用 |
| --- | --- |
| `--color-primary` | 主要强调色 |
| `--color-background` | 主背景色 |
| `--color-background-subtle` | 次级背景色 |
| `--color-foreground` | 主要文字颜色 |
| `--color-foreground-secondary` | 次要文字颜色 |
| `--color-border` | 常用边框颜色 |
| `--color-card` | 卡片背景色 |
| `--color-popover` | 弹出层背景色 |
| `--chat-background-user` | 用户消息背景色 |
| `--chat-background-assistant` | 助手消息背景色 |
| `--font-family` | 全局字体栈 |
| `--code-font-family` | 代码字体栈 |

例如，下面的样式为两种主题分别设置背景和边框：

```css
:root:not(.dark) {
  --color-background: #f7f8f6;
  --color-background-subtle: #f0f2ef;
  --color-border: rgba(20, 35, 28, 0.12);
}

:root.dark {
  --color-background: #171a18;
  --color-background-subtle: #1e221f;
  --color-border: rgba(235, 255, 244, 0.12);
}
```

{% hint style="warning" %}
主题色和字体已有内置设置。若同时在 CSS 中覆盖相同变量，最终效果会取决于选择器优先级和加载顺序，可能与设置页显示的值不一致。
{% endhint %}

## 修改具体组件

当变量无法完成目标时，可以使用浏览器开发者工具检查元素，再编写选择器。

```css
/* 示例：让设置页中的卡片边框更明显 */
[class*="border-border"] {
  border-color: color-mix(in srgb, var(--color-border) 75%, var(--color-foreground) 25%);
}
```

这类选择器比语义变量更容易受版本升级影响。请遵循以下原则：

- 尽量限定作用范围，避免直接覆盖所有 `div`、`button` 或 `input`；
- 少用依赖层级和序号的选择器，例如 `:nth-child()`；
- 不要假设自动生成的类名长期不变；
- 避免大范围使用 `!important`；
- 为每组规则添加简短注释，说明目的；
- 修改后同时检查浅色和深色主题。

上面的组件选择器仅用于说明写法，不代表稳定的公开接口。

## 查找当前变量

Cherry Studio 正在迁移到新的 V2 设计系统，因此变量分为两类：

- [V2 主题变量](https://github.com/CherryHQ/cherry-studio/blob/main/packages/ui/src/styles/theme.css)；
- [兼容旧界面的变量](https://github.com/CherryHQ/cherry-studio/blob/main/src/renderer/assets/styles/legacy-vars.css)。

兼容变量仍在使用，但未来可能移除。新主题应优先采用 V2 语义变量，并在每次大版本升级后重新检查效果。

编辑器顶部的 **cherrycss.com** 链接可以打开社区主题站。使用社区主题前，请先阅读完整 CSS，并确认来源可信。

## 安全建议

CSS 本身不是 JavaScript，但仍可能通过 `url()`、`@import` 或外部字体请求网络资源。使用第三方主题时：

- 检查是否引用陌生域名；
- 不要在 CSS 中写入令牌、Cookie、用户名或本地路径；
- 优先把需要的图片和字体保存到可信位置；
- 保留原始主题来源和版本号；
- 不要运行主题作者额外提供但用途不明的控制台脚本。

## 恢复默认样式

正常情况下：

1. 打开**设置 > 通用设置 > 自定义 CSS**。
2. 复制并备份仍需保留的内容。
3. 清空编辑器中的全部 CSS。
4. 确认界面恢复；必要时重新启动应用。

如果错误样式遮挡了设置按钮或让页面无法操作，请参阅[清除 CSS 设置](clear-css.md)。

## 常见问题

### 输入 CSS 后没有变化

先确认语法完整，没有遗漏右花括号。然后检查选择器是否仍与当前版本的元素匹配，以及变量名是否存在。

### 浅色主题正常，深色主题异常

把两种主题的规则拆开，分别使用 `:root:not(.dark)` 和 `:root.dark`，并检查文字与背景的对比度。

### 修改主题色没有效果

主题色会由内置设置写入运行时变量。优先使用**显示与语言 > 主题色**；如果必须由 CSS 覆盖，需要检查 `--cs-theme-primary` 与选择器优先级，但不建议同时维护两套值。

### 升级后布局错乱

先暂时清空全部自定义 CSS，确认问题是否消失。随后逐段恢复，删除依赖旧类名、旧 DOM 层级或兼容变量的规则。

### 辅助窗口显示异常

自定义 CSS 也可能应用到快捷助手、划词工具等窗口。避免使用过宽的全局选择器，并逐个检查常用窗口。

***

### 获取帮助与提交反馈

如果在配置或使用过程中遇到问题，请通过[反馈与建议](../../question-contact/suggestions.md)中列出的官方渠道联系我们。
