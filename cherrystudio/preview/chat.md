---
icon: message
---

# 对话界面

对话界面是 Cherry Studio 最常用的页面，但其结构包含**两个层次**：助手 → 话题。理解这一结构有助于更高效地使用各类对话功能。

> 推荐先阅读 [概念入门](../../advanced-basic/concepts-101.md) 了解助手 / 智能体 / 技能等相关概念。

## 第一次对话

开始前，请先在 `设置 → 模型服务` 中启用至少一个对话模型。还没有模型时，先完成[5 分钟快速开始](../../getting-started/quick-start.md)。

1. 点击顶部的 **对话**；
2. 选择系统默认助手；
3. 在输入区的模型选择器中选择一个已启用的对话模型；
4. 输入问题并发送。

可以用下面这句话测试：

> 请用三句话说明你能帮助我完成什么。

**成功标志**：消息区开始显示模型回复，并且没有连接、鉴权或余额错误。发送失败时展开错误详情，依次检查模型是否启用、API Key、服务商余额和网络连接。

完成第一次对话后，再按需学习附件、知识库、网络搜索、MCP 和助手参数，不需要在第一次使用时全部配置。

## 助手与话题的关系

简单类比：

* **助手 = 一个角色**（如"产品文档助理"、"代码 reviewer"）
* **话题 = 与该角色的一段对话**（如周一讨论"重构方案"、周二讨论"bug 报告"）

也就是说：**一个助手下可创建多个话题**，所有话题共用该助手的人设与参数（提示词、模型、温度等），无需每次重新设定 AI 的角色与风格。

### 助手

助手为 AI 设定固定角色 —— 由系统提示词 + 模型参数预设组成。

* **系统默认助手**：通用助手，未设特殊提示词，可直接使用
* **更专项的助手**：在对话页内打开 [助手库](assistants.md) 浏览现成预设，或自行创建

### 话题

每个助手下可创建多个话题（即多段独立对话）。话题之间相互独立，但共享所属助手的设置。

适用场景示例：

* 同一个"代码助手"下分别开"项目 A 重构"、"项目 B bug"两个话题，独立管理
* 同一个"翻译助手"下开多个话题，分别处理不同文章

<figure><img src="../../.gitbook/assets/cherry-assistants-v2.png" alt="V2 助手与话题列表"><figcaption><p>V2 对话页：左侧按助手组织话题，右侧进行对话</p></figcaption></figure>

## 对话框内按钮

V2 的输入区把操作分成两类：

* **独立控件**：新建话题、模型选择、展开 / 收起输入框和发送按钮。这些控件不参与工具栏固定与排序
* **可自定义工具**：附件、快捷短语、思考、网络搜索、知识库、生成图片、MCP，以及在对应会话中出现的斜杠命令或权限操作

点击输入框工具区的 `+`，选择 **自定义工具栏**，可以：

* 用开关固定或取消固定可自定义工具
* 拖动调整已固定工具的顺序
* 点击 **恢复默认** 回到默认布局

已固定的动作不会在 `+` 面板中重复出现；取消固定后仍可从 `+` 面板找到。聊天与智能体各自保存一套工具栏配置。

### 常用工具

| 名称 | 作用 |
|---|---|
| **上传附件** | 上传图片或文档；图片需模型支持视觉能力，文档会被解析为上下文 |
| **快捷短语** | 调用预设模板，详见 [快捷短语](../../pre-basic/settings/quick-phrase.md) |
| **网络搜索** | 把网页搜索结果作为上下文，需先在 [联网模式](../../pre-basic/websearch/) 中配置 |
| **知识库** | 将已建立的 [知识库](../../knowledge-base/knowledge-base.md) 用作上下文 |
| **MCP** | 启用 [MCP](../../advanced-basic/mcp/) 工具供模型调用 |
| **思考** | 所选模型支持推理时可用 |
| **生成图片** | 所选对话模型支持生图时可用；专门的生图模型请使用 [绘画](drawing.md) |
| **斜杠命令** | 仅在支持的 Agent 会话中出现；内置命令包括 `/clear`、`/compact`、`/context`、`/usage` 和 `/exit` |

模型选择器是输入区中的独立控件，也可使用 `chat.model.select` 对应的快捷键打开。V2 不提供通过 `@` 唤起模型选择器的面板；`/` 面板按当前会话提供可用命令。

{% hint style="warning" %}
V2 已从输入框工具栏移除 **清空当前话题** 与 **清除上下文**。需要干净上下文时，请新建话题；需要管理或删除话题时，请使用话题级菜单。
{% endhint %}

### Token 信息

`显示预估 Token 数` 会影响消息区域中的 Token 估算信息。V2 当前不会在输入框右下角显示“当前上下文数 / 最大上下文数 / 当前上下文 Token 数 / 预估 Token 数”四项计数。

{% hint style="info" %}
Token 信息仅为估算，不同模型的 Tokenizer 不同，实际计费以模型服务商为准。
{% endhint %}

## 对话设置

V2 将输入、消息和代码块的显示选项集中在 `设置 → 外观`。

<figure><img src="../../.gitbook/assets/cherry-chat-appearance-settings-v2.png" alt="V2 外观设置中的对话选项"><figcaption><p>设置 → 外观：输入、消息和代码块设置</p></figcaption></figure>

### 模型设置

模型设置与助手设置当中的 `模型设置` 参数同步，详见 [助手设置](chat.md#bian-ji-zhu-shou)。

{% hint style="info" %}
在对话设置当中，仅该模型设置作用于当前助手，其余设置作用于全局。如：设置消息样式为气泡后在任何助手的任何话题下都是气泡样式。
{% endhint %}

### 消息设置

#### <mark style="color:blue;">**`消息分割线`**</mark>:

使用分割线将消息正文与操作栏隔开。

{% tabs %}
{% tab title="打开时" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="关闭时" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`使用衬线字体`**</mark>：

字体样式切换，现在你也可以通过 [自定义css](../../pre-basic/personalization-settings/) 来更换字体。

#### <mark style="color:blue;">**`代码显示行号`**</mark>：

模型输出代码片段时显示代码块行号。

{% tabs %}
{% tab title="关闭时" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="打开时" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`代码块可折叠`**</mark>：

打开后，当代码片段中的代码较长时，将自动折叠代码块。

#### <mark style="color:blue;">**`代码块可换行`**</mark>：

打开后，当代码片段中的单行代码超出窗口时，将自动换行。

#### <mark style="color:blue;">**`思考内容自动折叠`**</mark>：

打开后，支持思考的模型在思考完成后会自动折叠思考过程。

#### <mark style="color:blue;">**`消息样式`**</mark>：

可将对话界面切换为气泡样式或列表样式。

#### <mark style="color:blue;">**`代码风格`**</mark>：

可切换代码片段的显示风格。

#### <mark style="color:blue;">**`消息字体大小`**</mark>：

调整对话界面字体的大小。

### 输入设置

#### <mark style="color:blue;">**`显示预估 Token 数`**</mark>：

在消息区域显示估算的 Token 信息，便于了解上下文消耗。该数值不是服务商的最终计费结果。

#### <mark style="color:blue;">**`长文本粘贴为文件`**</mark>：

当从其他地方复制长段文本粘贴到输入框时会自动显示为文件的样式，减少后续输入内容时的干扰。

#### <mark style="color:blue;">**`Markdown 渲染输入消息`**</mark>：

关闭时只渲染模型回复的消息，不渲染发送的消息。

{% tabs %}
{% tab title="关闭时" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="打开时" %}
<figure><img src="../../.gitbook/assets/image (6) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## 助手设置

在助手界面选择需要设置的<mark style="background-color:yellow;">助手名称</mark>→在<mark style="background-color:yellow;">右键菜单中</mark>选对应设置

### 编辑助手

{% hint style="info" %}
助手设置作用于该助手下的所有话题。
{% endhint %}

<figure><img src="../../.gitbook/assets/cherry-assistant-edit-v2.png" alt="V2 助手编辑面板"><figcaption><p>V2 助手编辑面板</p></figcaption></figure>

#### 提示词设置

#### <mark style="color:blue;">**`名称`**</mark>：

可自定义方便辨识的助手名称。

#### <mark style="color:blue;">**`提示词`**</mark>：

即 prompt ，可以参照智能体页面的提示词写法来编辑内容。

#### 模型设置

#### <mark style="color:blue;">**`默认模型`**</mark>：

可以为该助手固定一个默认模型。未单独指定时，使用 [全局默认对话模型](../../pre-basic/settings/default-models.md#mo-ren-zhu-shou-mo-xing)。

{% hint style="info" %}
助手的默认模型有两种，一为 [全局默认对话模型](../../pre-basic/settings/default-models.md#mo-ren-zhu-shou-mo-xing) ，另一为助手默认模型；助手的默认模型优先级高于全局默认对话模型。当不设置助手默认模型时，助手默认模型=全局默认对话模型。
{% endhint %}

#### <mark style="color:blue;">**`温度 (Temperature)`**</mark> ：

温度参数控制模型生成文本的随机性和创造性程度。V2 默认不覆盖模型自身的温度；只有启用该参数后，填写的数值才会随请求发送。常见表现为：

* 低温度值(0-0.3)：
  * 输出更确定、更专注
  * 适合代码生成、数据分析等需要准确性的场景
  * 倾向于选择最可能的词汇输出
* 中等温度值(0.4-0.7)：
  * 平衡了创造性和连贯性
  * 适合日常对话、一般性写作
  * 推荐用于聊天机器人对话(0.5左右)
* 高温度值(0.8-1.0)：
  * 产生更具创造性和多样性的输出
  * 适合创意写作、头脑风暴等场景
  * 但可能降低文本的连贯性

#### <mark style="color:blue;">**`Top P (核采样)`**</mark>：

V2 默认不覆盖模型自身的 Top P；只有启用该参数后，填写的数值才会随请求发送。界面保存值通常为 1，值越小，AI 生成的内容越集中；值越大，可选词汇范围越广。

核采样通过控制词汇选择的概率阈值来影响输出：

* 较小值(0.1-0.3)：
  * 仅考虑最高概率的词汇
  * 输出更保守、更可控
  * 适合代码注释、技术文档等场景
* 中等值(0.4-0.6)：
  * 平衡词汇多样性和准确性
  * 适合一般对话和写作任务
* 较大值(0.7-1.0)：
  * 考虑更广泛的词汇选择
  * 产生更丰富多样的内容
  * 适合创意写作等需要多样化表达的场景

{% hint style="info" %}
- 这两个参数可以独立使用或组合使用
- 根据具体任务类型选择合适的参数值
- 建议通过实验找到最适合特定应用场景的参数组合
- 以上内容仅供参考和了解概念，所给参数范围不一定适合所有模型，具体可参考模型相关文档给出的参数建议。
{% endhint %}

#### <mark style="color:blue;">**`开启消息长度限制 (MaxToken)`**</mark>

用于限制单次回答最多生成多少 [Token](../../question-contact/knowledge.md#shen-me-shi-tokens)。该参数会直接影响回复的最大长度，也可能影响费用与响应时间。

不同模型和服务商支持的上限差异很大，客户端中的可填写值也不代表服务端一定接受。请以当前模型服务商的官方文档为准。

具体设置多少取决于自己的需要，当然也可以参考以下建议。

{% hint style="success" %}
建议：

* 普通聊天：500-800
* 短文生成：800-2000
* 代码生成：2000-3600
* 长文生成：4000及以上 (需要模型本身支持)
{% endhint %}

{% hint style="warning" %}
一般情况下模型生成的回答将被限制在 MaxToken 的范围内，当然也有可能会出现被截断（如写长代码时）或表达不完整等情况出现，特殊情况下也需要根据实际情况来灵活调整。
{% endhint %}

#### <mark style="color:blue;">**`流式输出（Stream）`**</mark>

流式输出是一种数据处理方式，它允许数据以连续的流形式进行传输和处理，而不是一次性发送所有数据。这种方式使得数据可以在生成后立即被处理和输出，极大地提高了实时性和效率。

在 Cherry Studio 客户端中，可以把它简单理解为打字机效果。

关闭后(非流)：模型生成完信息后整段一次性输出（想象一下微信收到消息的感觉）；

打开时：逐字输出，可以理解为大模型每生成一个字就立马发送给你，直到全部发送完。

{% hint style="info" %}
如果某些特殊模型不支持流式输出需要将该开关关闭，比如**刚开始**只支持非流的o1-mini等。
{% endhint %}

#### <mark style="color:blue;">**`最大工具调用次数`**</mark>

限制模型在一次回复中连续调用工具的次数。启用 MCP 或其他工具时，可用它避免模型在异常情况下反复调用；设置过低也可能让复杂任务提前停止。

#### <mark style="color:blue;">**`自定义参数`**</mark>

在请求体（body）中加入额外请求参数，如 `presence_penalty` 等字段。大多数用户不需要修改。

> 上述top-p、maxtokens、stream等参数就是这些参数之一。

填法：参数名称—参数类型（文本、数字等）—值。可用参数以对应服务商的官方 API 文档为准，例如 [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create)。

{% hint style="info" %}
各个模型提供商都或多或少有自己独有的参数，需要到提供商的文档中寻找使用方法
{% endhint %}

{% hint style="info" %}
* 自定义参数优先级高于内置参数。即自定义参数如果与内置参数重复，则自定义参数会覆盖内置参数。

> 如：自定义参数中设置 `model` 为 `gpt-4o` 后，在对话中无论选择哪个模型都使用的是 `gpt-4o` 模型。

* 使用 <kbd>参数名称:undefined</kbd> 的设置可排除参数。
{% endhint %}

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。
