---
icon: message
---
# Chat Interface


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Assistants and Topics

### Assistant

An `assistant` allows for personalized settings for a chosen model, such as preset prompts and parameter presets. These settings help the selected model work more in line with your expectations.

The `System Default Assistant` comes with a relatively general set of parameters (no prompt). You can use it directly or find the presets you need on the [Agents page](agents.md).

### Topic

An `assistant` is a superset of a `topic`. Multiple topics (i.e., conversations) can be created under a single assistant. All `topics` share the assistant's parameter settings and model settings, such as preset words (prompts).

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Buttons in the Chatbox

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `New Topic` creates a new topic within the current assistant.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Upload Image or Document`. Uploading images requires model support. Uploading documents will automatically parse them into text to be provided to the model as context.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Web Search` requires configuring web search-related information in the settings. Search results are returned to the large model as context. See [Web Search Mode](../../websearch/) for details.

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` enables the knowledge base feature. See [Knowledge Base Tutorial](../../knowledge-base/knowledge-base.md) for details.

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP Server` enables the MCP server feature. See [MCP Usage Tutorial](../../advanced-basic/mcp/) for details.

![](../../.gitbook/assets/对话界面/生成图片.png) `Generate Image` is displayed only when the selected **chat model** supports image generation. (For non-chat image generation models, please go to [Drawing](./drawing.md)).

![](../../.gitbook/assets/对话界面/选择模型.png) `Select Model` switches to the specified model for the subsequent conversation, while retaining the context.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Quick Phrases` requires presetting common phrases in the settings. They can be invoked here, directly input, and support variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Clear Messages` deletes all content in this topic.

![](../../.gitbook/assets/对话界面/展开.png) `Expand` enlarges the chatbox for entering long texts.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Clear Context` truncates the context available to the model without deleting content, meaning the model will "forget" previous conversation content.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimated Token Count` displays the estimated token count. The four values are `Current Context Count`, `Maximum Context Count` (∞ means infinite context), `Current Input Box Message Character Count`, and `Estimated Token Count`.

{% hint style="info" %}
This feature is only for estimating token count. The actual token count varies for each model, please refer to the data provided by the model provider.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Translate` translates the content in the current input box into English.

## Chat Settings

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Model Settings

Model settings are synchronized with the `Model Settings` in the Assistant settings. See [Assistant Settings](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
In chat settings, only the model settings apply to the current assistant. Other settings apply globally. For example, if you set the message style to speech bubble, it will be a speech bubble style in any topic of any assistant.
{% endhint %}

### Message Settings

#### <mark style="color:blue;">**`Message Separator`**</mark>:

Use a separator to distinguish the message body from the action bar.

{% tabs %}
{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Use Serif Font`**</mark>:

Font style switching. You can also change the font via [Custom CSS](../../personalization-settings/).

#### <mark style="color:blue;">**`Display Line Numbers for Code`**</mark>:

Displays line numbers for code blocks when the model outputs code snippets.

{% tabs %}
{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Collapsible Code Blocks`**</mark>:

When enabled, code blocks will automatically collapse if the code snippet is too long.

#### <mark style="color:blue;">**`Code Block Word Wrap`**</mark>:

When enabled, single lines of code within code snippets will automatically wrap if they exceed the window width.

#### <mark style="color:blue;">**`Auto-collapse Thinking Content`**</mark>:

When enabled, models that support "thinking" will automatically collapse the thinking process after completion.

#### <mark style="color:blue;">**`Message Style`**</mark>:

Can switch the chat interface to a bubble style or list style.

#### <mark style="color:blue;">**`Code Style`**</mark>:

Can switch the display style of code snippets.

#### <mark style="color:blue;">**`Math Formula Engine`**</mark>:

*   KaTeX renders faster because it is specifically designed for performance optimization;
*   MathJax renders slower but is more comprehensive, supporting more mathematical symbols and commands.

#### <mark style="color:blue;">**`Message Font Size`**</mark>:

Adjusts the font size of the chat interface.

### Input Settings

#### <mark style="color:blue;">**`Show Estimated Token Count`**</mark>:

Displays the estimated number of tokens consumed by the input text in the input box (not the actual context consumption, for reference only).

#### <mark style="color:blue;">**`Paste Long Text as File`**</mark>:

When copying and pasting a long passage of text from elsewhere into the input box, it will automatically appear as a file, reducing interference when entering subsequent content.

#### <mark style="color:blue;">**`Markdown Render Input Messages`**</mark>:

When off, only model replies are rendered, not sent messages.

{% tabs %}
{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Translate by Tapping Space 3 Times`**</mark>:

After entering a message in the chat interface input box, tapping the space bar three times consecutively will translate the input content into English.

{% hint style="warning" %}
Note: This operation will overwrite the original text.
{% endhint %}

#### <mark style="color:blue;">**`Target Language`**</mark>:

Sets the target language for the input box translation button and the "Translate by tapping space 3 times" feature.

## Assistant Settings

In the assistant interface, select the <mark style="background-color:yellow;">assistant name</mark> to be set → choose the corresponding setting from the <mark style="background-color:yellow;">right-click menu</mark>.

### Edit Assistant

{% hint style="info" %}
Assistant settings apply to all topics under that assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Prompt Settings

#### <mark style="color:blue;">**`Name`**</mark>:

Customizable assistant name for easy identification.

#### <mark style="color:blue;">**`Prompt`**</mark>:

This is the prompt. You can refer to the prompt writing style on the Agents page to edit the content.

#### Model Settings

#### <mark style="color:blue;">**`Default Model`**</mark>:

You can fix a default model for this assistant. When adding from the Agents page or copying an assistant, the initial model will be this model. If this item is not set, the initial model will be the global initial model (i.e., [Default Assistant Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
There are two types of default models for assistants: one is the [Global Default Chat Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing), and the other is the assistant's default model. The assistant's default model takes precedence over the global default chat model. If the assistant's default model is not set, then the assistant's default model = the global default chat model.
{% endhint %}

#### <mark style="color:blue;">**`Auto-reset Model`**</mark>:

When enabled - if another model is switched to during usage within this topic, creating a new topic will reset the new topic's model to the assistant's default model. When this item is disabled, the model for a new topic will follow the model used in the previous topic.

> For example, if the assistant's default model is gpt-3.5-turbo, and I create Topic 1 under this assistant, then switch to gpt-4o during the conversation in Topic 1:
>
> If auto-reset is enabled: when creating Topic 2, Topic 2 will default to gpt-3.5-turbo.
>
> If auto-reset is not enabled: when creating Topic 2, Topic 2 will default to gpt-4o.

#### <mark style="color:blue;">**`Temperature`**</mark>:

The temperature parameter controls the degree of randomness and creativity in the text generated by the model (default value is 0.7). Specifically:

*   Low temperature values (0-0.3):
    *   Output is more deterministic and focused.
    *   Suitable for tasks requiring accuracy, such as code generation and data analysis.
    *   Tends to select the most probable words for output.
*   Medium temperature values (0.4-0.7):
    *   Balances creativity and coherence.
    *   Suitable for daily conversations and general writing.
    *   Recommended for chatbot conversations (around 0.5).
*   High temperature values (0.8-1.0):
    *   Produces more creative and diverse outputs.
    *   Suitable for creative writing, brainstorming, and similar scenarios.
    *   May reduce the coherence of the text.

#### <mark style="color:blue;">**`Top P (Nucleus Sampling)`**</mark>:

The default value is 1. The smaller the value, the more monotonous and easier to understand the AI-generated content; the larger the value, the wider the range of vocabulary the AI uses, making it more diverse.

Nucleus sampling influences the output by controlling the probability threshold for word selection:

*   Smaller values (0.1-0.3):
    *   Considers only the highest probability words.
    *   Output is more conservative and controlled.
    *   Suitable for code comments, technical documentation, etc.
*   Medium values (0.4-0.6):
    *   Balances vocabulary diversity and accuracy.
    *   Suitable for general conversations and writing tasks.
*   Larger values (0.7-1.0):
    *   Considers a wider range of vocabulary choices.
    *   Produces richer and more diverse content.
    *   Suitable for creative writing and other scenarios requiring diverse expression.

{% hint style="info" %}
- These two parameters can be used independently or in combination.
- Choose appropriate parameter values based on the specific task type.
- It is recommended to experiment to find the optimal parameter combination for a particular application scenario.
- The above content is for reference and conceptual understanding only; the given parameter ranges may not be suitable for all models. Please refer to the model's documentation for specific parameter recommendations.
{% endhint %}

#### <mark style="color:blue;">**`Context Window`**</mark>

The number of messages to retain in context. A larger value means longer context and consumes more tokens:

*   5-10: Suitable for general conversations.
*   >10: For complex tasks requiring longer memory (e.g., generating long texts step-by-step according to an outline, where logical coherence of generated context is needed).
*   Note: More messages mean higher token consumption.

#### <mark style="color:blue;">**`Enable Message Length Limit (MaxToken)`**</mark>

The maximum [Token](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) count for a single response. In large language models, `max_tokens` is a key parameter that directly affects the quality and length of the model's generated response.

> For example: When testing if a model is connected in CherryStudio after entering the key, you only need to know if the model returns a message correctly, not specific content. In this case, setting `MaxToken` to 1 is sufficient.

Most models have a MaxToken limit of 32k Tokens, but some have 64k or even more. You need to check the corresponding introductory page for details.

The specific setting depends on your needs, but you can also refer to the suggestions below.

{% hint style="success" %}
Suggestions:

*   General chat: 500-800
*   Short text generation: 800-2000
*   Code generation: 2000-3600
*   Long text generation: 4000 and above (requires model support)
{% endhint %}

{% hint style="warning" %}
Generally, the model's response will be limited to the `MaxToken` range. However, truncation (e.g., when writing long code) or incomplete expressions may occur. In special cases, flexible adjustments need to be made based on actual circumstances.
{% endhint %}

#### <mark style="color:blue;">**`Stream Output (Stream)`**</mark>

Stream output is a data processing method that allows data to be transmitted and processed in a continuous stream, rather than sending all data at once. This method allows data to be processed and output immediately after it is generated, greatly improving real-time performance and efficiency.

In environments like the CherryStudio client, it simply means a "typewriter effect".

When off (non-streaming): The model generates the entire piece of information and outputs it all at once (imagine receiving a message on WeChat);

When on: Output character by character. This can be understood as the large model sending you each generated character immediately until all characters are sent.

{% hint style="info" %}
If certain specific models do not support stream output, this switch needs to be turned off, such as `o1-mini` which **initially** only supported non-streaming.
{% endhint %}

#### <mark style="color:blue;">**`Custom Parameters`**</mark>

Adds additional request parameters to the request body, such as `presence_penalty`, etc. Most people generally do not need to use this.

> The `top-p`, `maxtokens`, `stream` parameters mentioned above are among these parameters.

Filling method: Parameter Name — Parameter Type (text, number, etc.) — Value. Reference documentation: [Click to go](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Each model provider has its own unique parameters, more or less. You need to find the usage method in the provider's documentation.
{% endhint %}

{% hint style="info" %}
*   Custom parameters take precedence over built-in parameters. That is, if a custom parameter duplicates a built-in parameter, the custom parameter will override the built-in parameter.

> For example: if `model` is set to `gpt-4o` in custom parameters, then `gpt-4o` will be used in the conversation regardless of which model is selected.

*   Setting <kbd>Parameter Name:undefined</kbd> can exclude a parameter.
{% endhint %}