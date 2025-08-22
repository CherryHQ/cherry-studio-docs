---
icon: message
---
# Project Introduction


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="warning" %}
This document is translated from Chinese by AI and has not yet been reviewed. I will try to check the document one by one to ensure the translation is reasonable.
{% endhint %}

<figure><img src=".gitbook/assets/docs-readme-banner1.png" alt=""><figcaption></figcaption></figure>

Cherry Studio is an all-in-one AI assistant platform integrating multi-model conversations, knowledge base management, AI painting, translation, and more.

### Star History

![Star History](https://urlscan.io/liveshot/?width=1300&height=620&url=https://cherrystarhistory.ocool.online/)

## Follow Our Social Accounts

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">Xiaohongshu</a></td><td><a href=".gitbook/assets/1.png">1.png</a></td><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link</a></td></tr></tbody></table>
# Chat Interface

## Assistants and Topics

### Assistant

`Assistant` is used to make personalized settings for the selected model, such as prompt presets and parameter presets. These settings help the selected model better meet your expected work.

The `System Default Assistant` has a more general parameter preset (no prompt). You can use it directly or find the preset you need on the [Agents page](agents.md).

### Topic

`Assistant` is the parent of `Topic`. Multiple topics (i.e., conversations) can be created under a single assistant. All `topics` share the assistant's parameter settings and preset words (prompt) and other model settings.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Buttons in Chat Box

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `New Topic` creates a new topic within the current assistant.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Upload Image or Document` requires the model to support image uploads. Uploading documents will automatically parse them into text to provide as context to the model.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Web Search` requires configuring web search information in the settings. Search results are returned to the large model as context. See [Web Search Mode](../../websearch/) for details.

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` enables the knowledge base. See [Knowledge Base Tutorial](../../knowledge-base/knowledge-base.md) for details.

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP Server` enables the MCP server function. See [MCP Usage Tutorial](../../advanced-basic/mcp/) for details.

![](../../.gitbook/assets/对话界面/生成图片.png) `Generate Image` is not displayed by default. For models that support image generation (e.g., Gemini), you need to manually light it up to generate images.

{% hint style="info" %}
Due to technical reasons, you must manually light up the button to generate images. This button will be removed after this feature is optimized.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Select Model` switches to the specified model for the subsequent conversation, preserving context.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Quick Phrases` requires presetting common phrases in the settings, which can then be called here, directly input, and support variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Clear Messages` deletes all content under this topic.

![](../../.gitbook/assets/对话界面/展开.png) `Expand` makes the chat box larger for entering long texts.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Clear Context` truncates the context available to the model without deleting content, meaning the model will "forget" previous conversation content.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimated Token Count` displays the estimated Token count. The four data points are `current context count`, `maximum context count` (∞ means infinite context), `number of characters in current input box message`, and `estimated Token count`.

{% hint style="info" %}
This function is only used to estimate the Token count. The actual Token count varies for each model. Please refer to the data provided by the model provider.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Translate` translates the content in the current input box into English.

## Chat Settings

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Model Settings

Model settings are synchronized with the `Model Settings` parameters in Assistant settings. See [Assistant Settings](chat.md#bian-ji-zhu-shou) for details.

{% hint style="info" %}
In chat settings, only the model settings apply to the current assistant; other settings apply globally. For example, if you set the message style to "bubble," it will be a bubble style in any topic of any assistant.
{% endhint %}

### Message Settings

#### <mark style="color:blue;">**`Message Divider`**</mark>:

Uses a divider to separate the message body from the action bar.

{% tabs %}
{% tab title="When Open" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When Closed" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Use Serif Font`**</mark>:

Font style switch. Now you can also change fonts via [custom CSS](../../personalization-settings/).

#### <mark style="color:blue;">**`Show Line Numbers in Code`**</mark>:

Displays line numbers in code blocks when the model outputs code snippets.

{% tabs %}
{% tab title="When Closed" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When Open" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Code Block Collapsible`**</mark>:

When enabled, if the code in a code snippet is long, the code block will automatically collapse.

#### <mark style="color:blue;">**`Code Block Word Wrap`**</mark>:

When enabled, if a single line of code in a code snippet is too long (exceeds the window), it will automatically wrap.

#### <mark style="color:blue;">**`Auto-collapse Thought Content`**</mark>:

When enabled, models that support thinking will automatically collapse the thought process after completion.

#### <mark style="color:blue;">**`Message Style`**</mark>:

Can switch the chat interface to bubble style or list style.

#### <mark style="color:blue;">**`Code Style`**</mark>:

Can switch the display style of code snippets.

#### <mark style="color:blue;">**`Math Formula Engine`**</mark>:

*   KaTeX renders faster because it is specifically designed for performance optimization;
*   MathJax renders slower but is more comprehensive, supporting more mathematical symbols and commands.

#### <mark style="color:blue;">**`Message Font Size`**</mark>:

Adjusts the font size of the chat interface.

### Input Settings

#### <mark style="color:blue;">**`Show Estimated Token Count`**</mark>:

Displays the estimated Token count of the input text in the input box (not the actual context consumption, for reference only).

#### <mark style="color:blue;">**`Paste Long Text as File`**</mark>:

When pasting a long text from elsewhere into the input box, it will automatically appear as a file style, reducing interference when entering subsequent content.

#### <mark style="color:blue;">**`Markdown Render Input Messages`**</mark>:

When disabled, only model replies are rendered, not sent messages.

{% tabs %}
{% tab title="When Closed" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When Open" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Triple Space to Translate`**</mark>:

After entering a message in the chat interface input box, hitting the spacebar three times quickly can translate the input content into English.

{% hint style="warning" %}
Note: This operation will overwrite the original text.
{% endhint %}

#### <mark style="color:blue;">**`Target Language`**</mark>:

Sets the target language for the input box translation button and the triple space translation.

## Assistant Settings

In the assistant interface, select the <mark style="background-color:yellow;">assistant name</mark> to be set → select the corresponding setting in the <mark style="background-color:yellow;">right-click menu</mark>

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

You can fix a default model for this assistant. When adding from the Agents page or duplicating an assistant, the initial model will be this one. If this item is not set, the initial model will be the global initial model (i.e., [Default Assistant Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
There are two types of default models for assistants: one is the [global default chat model](settings/default-models.md#mo-ren-zhu-shou-mo-xing), and the other is the assistant's default model; the assistant's default model takes precedence over the global default chat model. If the assistant's default model is not set, the assistant's default model = global default chat model.
{% endhint %}

#### <mark style="color:blue;">**`Auto-reset Model`**</mark>:

When enabled - If you switch to another model during use within a topic, creating a new topic will reset the new topic's model to the assistant's default model. When this item is disabled, the model for a new topic will follow the model used in the previous topic.

> For example, if the assistant's default model is gpt-3.5-turbo, and I create topic 1 under this assistant, and switch to gpt-4o during the conversation in topic 1:
>
> If auto-reset is enabled: when creating topic 2, topic 2's default selected model will be gpt-3.5-turbo;
>
> If auto-reset is not enabled: when creating topic 2, topic 2's default selected model will be gpt-4o.

#### <mark style="color:blue;">**`Temperature`**</mark>:

The temperature parameter controls the degree of randomness and creativity in the text generated by the model (default value is 0.7). Specifically:

*   Low temperature values (0-0.3):
    *   Output is more deterministic and focused
    *   Suitable for scenarios requiring accuracy, such as code generation, data analysis
    *   Tends to select the most probable words for output
*   Medium temperature values (0.4-0.7):
    *   Balances creativity and coherence
    *   Suitable for daily conversations, general writing
    *   Recommended for chatbot conversations (around 0.5)
*   High temperature values (0.8-1.0):
    *   Produces more creative and diverse output
    *   Suitable for creative writing, brainstorming, etc.
    *   But may reduce text coherence

#### <mark style="color:blue;">**`Top P (Nucleus Sampling)`**</mark>:

The default value is 1. The smaller the value, the more monotonous and easier to understand the AI-generated content; the larger the value, the wider the range of vocabulary the AI responds with, and the more diverse it is.

Nucleus sampling influences output by controlling the probability threshold for vocabulary selection:

*   Smaller values (0.1-0.3):
    *   Only considers the highest probability vocabulary
    *   Output is more conservative and controllable
    *   Suitable for scenarios like code comments, technical documentation
*   Medium values (0.4-0.6):
    *   Balances vocabulary diversity and accuracy
    *   Suitable for general conversation and writing tasks
*   Larger values (0.7-1.0):
    *   Considers a wider range of vocabulary choices
    *   Produces richer and more diverse content
    *   Suitable for creative writing and other scenarios requiring diverse expression

{% hint style="info" %}
- These two parameters can be used independently or in combination.
- Choose appropriate parameter values based on the specific task type.
- It is recommended to find the most suitable parameter combination for a specific application scenario through experimentation.
- The above content is for reference and conceptual understanding only; the given parameter ranges may not be suitable for all models. Please refer to the model's relevant documentation for specific parameter recommendations.
{% endhint %}

#### <mark style="color:blue;">**`Context Window`**</mark>

The number of messages to retain in context. A larger value means longer context and more tokens consumed:

*   5-10: Suitable for general conversations
*   >10: For complex tasks requiring longer memory (e.g., generating long texts step-by-step according to a writing outline, needing to ensure logical coherence of generated context)
*   > Note: More messages mean higher token consumption

#### <mark style="color:blue;">**`Enable Message Length Limit (MaxToken)`**</mark>

The maximum [Token](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) count for a single response. In large language models, MaxToken (maximum tokens) is a key parameter that directly affects the quality and length of the model's generated responses.

> For example, in CherryStudio, after filling in the key, when testing if the model is connected, you only need to know if the model returns messages correctly without needing specific content. In this case, setting MaxToken to 1 is sufficient.

Most models have a MaxToken limit of 32k Tokens, but some have 64k or even more. You need to check the corresponding introduction page for specifics.

The specific setting depends on your needs, but you can also refer to the following suggestions.

{% hint style="success" %}
Suggestions:

*   General chat: 500-800
*   Short text generation: 800-2000
*   Code generation: 2000-3600
*   Long text generation: 4000 and above (requires model support)
{% endhint %}

{% hint style="warning" %}
Generally, the model's generated response will be limited to the MaxToken range. However, it may sometimes be truncated (e.g., when writing long code) or incomplete. In special cases, adjustments may need to be made flexibly based on actual circumstances.
{% endhint %}

#### <mark style="color:blue;">**`Streaming Output (Stream)`**</mark>

Streaming output is a data processing method that allows data to be transmitted and processed in a continuous flow, rather than sending all data at once. This method allows data to be processed and output immediately after generation, greatly improving real-time performance and efficiency.

In clients like CherryStudio, it's simply a "typing effect."

When off (non-streaming): The model generates information and then outputs the entire segment at once (imagine how you receive messages on WeChat);

When on: Output character by character. This can be understood as the large model sending you each character as soon as it's generated, until all are sent.

{% hint style="info" %}
If certain special models do not support streaming output, this switch needs to be turned off, such as o1-mini and others that **initially** only supported non-streaming.
{% endhint %}

#### <mark style="color:blue;">**`Custom Parameters`**</mark>

Adds extra request parameters to the request body, such as `presence_penalty` and other fields. Most people generally don't need this.

> The top-p, maxtokens, stream, and other parameters mentioned above are among these parameters.

Fill-in method: Parameter Name — Parameter Type (text, number, etc.) — Value. Reference document: [Click to go](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Each model provider may have its own unique parameters, and you need to find their usage in the provider's documentation.
{% endhint %}

{% hint style="info" %}
*   Custom parameters have higher priority than built-in parameters. This means if a custom parameter duplicates a built-in parameter, the custom parameter will overwrite the built-in one.

> For example, if you set `model` to `gpt-4o` in custom parameters, no matter which model is selected in the conversation, the `gpt-4o` model will be used.

*   Parameters can be excluded by setting <kbd>Parameter Name:undefined</kbd>.
{% endhint %}