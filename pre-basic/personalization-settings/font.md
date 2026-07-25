---
icon: book-font
---

# 字体推荐

Cherry Studio V2 可以直接读取系统中已安装的字体，并分别设置**全局字体**和**代码字体**。通常不需要再用自定义 CSS 修改字体。

## 在 Cherry Studio 中选择字体

1. 先把字体安装到操作系统。
2. 完全退出并重新打开 Cherry Studio。
3. 进入**设置 > 通用设置 > 显示与语言**。
4. 在**字体设置**中分别选择：
   - **全局字体**：界面、消息正文和大部分文本；
   - **代码字体**：代码块和代码编辑器。
5. 检查常用语言、数字、标点和代码是否显示正常。

两个字体选项右侧都有重置按钮，可以随时恢复默认值。

{% hint style="info" %}
字体列表来自操作系统。刚安装的字体没有出现时，请先完全退出 Cherry Studio；若仍未出现，再重启操作系统以刷新字体缓存。
{% endhint %}

## 如何选择

### 全局字体

优先考虑：

- 是否覆盖你常用的语言；
- 简体、繁体和日文字形是否符合阅读习惯；
- 小字号下是否清晰；
- 常规、粗体和斜体是否齐全；
- 中英文混排时高度和字重是否协调。

### 代码字体

优先检查：

- `0` 与 `O`、`1` 与 `l` / `I` 是否容易区分；
- 括号、引号、斜杠和运算符是否清楚；
- 是否需要显示中文、日文或俄文注释；
- 是否喜欢编程连字。

代码字体没有某个字符时，系统会尝试回退到其他字体，因此同一段代码可能出现字宽或风格不一致。

## 正文字体推荐

| 字体 | 适合语言 | 特点 | 官方来源 |
| --- | --- | --- | --- |
| Noto Sans | 英文、俄文及其他多种文字 | 覆盖范围广，适合多语言界面 | [Noto 官方文档](https://notofonts.github.io/noto-docs/website/use/) |
| Noto Sans SC | 简体中文 | 面向简体中文字形 | [Noto CJK 说明](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Noto Sans TC | 繁体中文 | 面向台湾繁体中文字形 | [Noto CJK 说明](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Noto Sans JP | 日文 | 面向日文字形 | [Noto CJK 说明](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Source Han Sans | 简体中文、繁体中文、日文、韩文 | Adobe 的 Pan-CJK 开源字体，提供地区变体 | [Source Han Sans](https://github.com/adobe-fonts/source-han-sans) |

如果经常在同一界面中混合英文、俄文与 CJK 文字，优先尝试 Noto 系列；它为不同文字提供风格相近的字体家族。

{% hint style="warning" %}
同一个汉字在简体中文、繁体中文和日文中可能采用不同字形。请选择与主要阅读语言对应的 `SC`、`TC` 或 `JP` 版本。
{% endhint %}

## 代码字体推荐

| 字体 | 适合场景 | CJK 支持 | 官方来源 |
| --- | --- | --- | --- |
| JetBrains Mono | 英文、俄文代码与终端内容 | 不以 CJK 为主要目标，CJK 注释通常依赖回退字体 | [JetBrains Mono](https://www.jetbrains.com/lp/mono/) |
| Sarasa Mono | 含中文或日文注释的代码 | 提供 `SC`、`TC`、`J` 等地区变体 | [Sarasa Gothic](https://github.com/be5invis/Sarasa-Gothic) |
| Monaspace | 喜欢多种风格、字符变体和编程连字 | 不以 CJK 为主要目标 | [Monaspace](https://github.com/githubnext/monaspace) |

### 快速选择

- 主要使用英文或俄文：先试 **JetBrains Mono**；
- 代码里经常包含简体中文：先试 **Sarasa Mono SC**；
- 代码里经常包含繁体中文：先试 **Sarasa Mono TC**；
- 代码里经常包含日文：先试 **Sarasa Mono J**；
- 想尝试不同代码风格或连字：选择 **Monaspace** 的一个家族。

Monaspace 包含多个风格兼容的家族。Cherry Studio 只负责选择字体家族，不提供字体特性开关；某些连字或字符变体能否显示，还取决于字体版本和渲染环境。

## 按文档语言选择

| 主要界面语言 | 全局字体建议 | 代码字体建议 |
| --- | --- | --- |
| 简体中文 | Noto Sans SC / Source Han Sans CN | Sarasa Mono SC |
| 中文（繁體） | Noto Sans TC / Source Han Sans TW | Sarasa Mono TC |
| English | Noto Sans | JetBrains Mono / Monaspace |
| 日本語 | Noto Sans JP / Source Han Sans JP | Sarasa Mono J |
| Русский | Noto Sans | JetBrains Mono / Monaspace |

这只是起点，并不要求全团队使用同一字体。最终应以实际显示效果和所在组织的字体规范为准。

## 安装建议

- 只从字体项目官网或官方发布页下载；
- 桌面应用通常安装 `OTF`、`TTF`、`TTC` 或可变字体文件，不要把网页专用的 `WOFF` / `WOFF2` 当作首选；
- 大型 CJK 字体包包含多个地区和字重，按实际需要安装即可；
- 更新字体前，先卸载旧版本，避免操作系统缓存出多个同名字体；
- 团队统一截图或演示时，应统一字体家族和版本。

本文推荐的项目都在官方页面提供开源许可信息。若要把字体重新打包进产品、模板或商业交付物，请仍以字体文件附带的许可证为准。

## 常见问题

### 字体安装后没有出现在列表中

完全退出 Cherry Studio 后重新打开。macOS 可在“字体册”确认字体是否启用；Windows 可在系统字体设置中确认；Linux 可刷新字体缓存后重启应用。

### 选择后部分字符仍是另一种字体

所选字体可能不包含这些字符，系统正在使用回退字体。换用覆盖目标语言的字体，或选择对应的 CJK 地区变体。

### 中文、繁体或日文字形看起来不对

检查是否选择了错误的 `SC`、`TC` 或 `JP` 版本。名称相近不代表字形标准相同。

### 代码列没有对齐

确认选择的是等宽字体，并检查代码中是否包含该字体不支持的 CJK 或特殊字符。回退字体可能破坏等宽效果。

### 字体太大或太小

字体家族和字号是两件事。全局界面过大或过小时，可在同一页面调整界面缩放；仅消息文字不合适时，应调整消息字体大小。

***

### 获取帮助与提交反馈

如果在配置或使用过程中遇到问题，请通过[反馈与建议](../../question-contact/suggestions.md)中列出的官方渠道联系我们。
