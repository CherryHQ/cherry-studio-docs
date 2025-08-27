---
icon: message
---
<think>
We are translating the given Chinese document to Japanese. We must strictly follow the translation rules:
1. Translate only textual content displayed to users, preserving all Markdown formatting and structural elements.
2. Preserve code blocks, links, image paths, and other technical syntax unchanged.
3. Translate comments within code blocks if any, but in this document, there are no code blocks with comments.
4. Preserve all links, image paths, file names, URLs, and version numbers exactly as in the original.
5. Maintain GitBook-style hint blocks by translating the content inside `{% hint %}` tags but keeping the tags themselves.
6. The document does not have a frontmatter, so no issue.
7. Do not add any extra explanations; return only the translated content.
8. This is not a table of contents file, so we translate all headings and text.
9. Preserve GitHub-specific terminology (e.g., pull request, fork) but in this text, there aren't any such terms that need to remain in English. However, technical terms like "Token", "prompt", "model", etc., should remain as they are since they are universal in the AI context.
10. All URLs, file paths, and version numbers must be preserved unchanged.

Let's break down the document and translate section by section.

Note: The original document uses some Markdown extensions like tabs and hint blocks, which we must keep in structure.

We start:

# 对话界面 → # チャットインターフェース


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## 助手和话题 → ## アシスタントとトピック

### 助手 → ### アシスタント

Translate the paragraph about "助手" and "系统默认助手", keeping the code backticks and links.

`助手` 是对所选模型做一些个性化的设置... → 
`アシスタント`は、選択したモデルに対してパーソナライズ設定を行うもので、プロンプトのプリセットやパラメータのプリセットなどを通じて、選択したモデルが期待する作業により適合するようにします。

`系统默认助手` 预设了一个比较通用的参数... → 
`システムデフォルトのアシスタント`は、比較的汎用的なパラメータ（プロンプトなし）がプリセットされています。直接使用するか、[エージェントページ](agents.md)で必要なプリセットを探して使用できます。

### 话题 → ### トピック

`助手` 是 `话题` 的父集... → 
`アシスタント`は`トピック`の親集合です。単一のアシスタントで複数のトピック（つまり会話）を作成でき、すべての`トピック`は`アシスタント`のパラメータ設定やプロンプトプリセットなどのモデル設定を共有します。

Then we have two figures. Preserve the image paths.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 对话框内按钮 → ## ダイアログ内のボタン

<figure> with an image of the dialog box.

Then we have a series of buttons with images and descriptions. We must translate the text but keep the image paths and the icon representations.

Example: 
![](../../.gitbook/assets/对话界面/新话题.png) `新话题` 在当前助手内创建一个新话题。 → 
![](../../.gitbook/assets/对话界面/新话题.png) `新規トピック`：現在のアシスタント内に新しいトピックを作成します。

Similarly, for each button:

- `上传图片或文档` → `画像またはドキュメントをアップロード`
- `网络搜索` → `ウェブ検索`
- `知识库` → `ナレッジベース`
- `MCP 服务器` → `MCP サーバー` (note: MCP is an acronym, so it remains)
- `生成图片` → `画像を生成`
- `选择模型` → `モデルを選択`
- `快捷短语` → `クイックフレーズ`
- `清空消息` → `メッセージをクリア`
- `展开` → `展開`
- `清除上下文` → `コンテキストをクリア`
- `预估 Token 数` → `トークン数の見積もり`
- `翻译` → `翻訳`

Then, the hint block for the image generation button:
{% hint style="info" %}
由于技术原因... → 
{% hint style="info" %}
技術的な理由により、画像を生成するにはボタンを手動で点灯させる必要があります。この機能が最適化された後、このボタンは削除されます。
{% endhint %}

For the token estimation:
{% hint style="info" %}
此功能仅用于预估... → 
{% hint style="info" %}
この機能はトークン数の見積もりのみを目的としており、実際のトークン数はモデルごとに異なります。モデルプロバイダーのデータを参照してください。
{% endhint %}

## 对话设置 → ## チャット設定

<figure> with image.

### 模型设置 → ### モデル設定

Text: 模型设置与助手设置当中的... → 
モデル設定はアシスタント設定の`モデル設定`パラメータと同期しています。詳細は[アシスタント設定](chat.md#bian-ji-zhu-shou)を参照してください。

Then a hint block:
{% hint style="info" %}
在对话设置当中... → 
{% hint style="info" %}
チャット設定では、このモデル設定のみが現在のアシスタントに適用され、他の設定はグローバルに適用されます。例：メッセージスタイルをバブルに設定すると、どのアシスタントのどのトピックでもバブルスタイルになります。
{% endhint %}

### 消息设置 → ### メッセージ設定

#### <mark style="color:blue;">**`消息分割线`**</mark>: → #### <mark style="color:blue;">**`メッセージ分割線`**</mark>:

Translate description.

Then tabs:
{% tabs %}
{% tab title="打开时" %} → {% tab title="オン時" %}
{% tab title="关闭时" %} → {% tab title="オフ時" %}
With figures for each.

Similarly for the other settings:

- `使用衬线字体` → `セリフ体を使用`
- `代码显示行号` → `コードに行番号を表示`
- `代码块可折叠` → `コードブロックを折りたたみ可能`
- `代码块可换行` → `コードブロックを折り返し可能`
- `思考内容自动折叠` → `思考内容を自動折りたたみ`
- `消息样式` → `メッセージスタイル`
- `代码风格` → `コードスタイル`
- `数学公式引擎` → `数式レンダリングエンジン`
- `消息字体大小` → `メッセージフォントサイズ`

For the mathematical formula engines:
* KaTeX → KaTeX (remain)
* MathJax → MathJax (remain)
and translate the descriptions.

### 输入设置 → ### 入力設定

Similarly:
- `显示预估 Token 数` → `トークン数の見積もりを表示`
- `长文本粘贴为文件` → `長いテキストをファイルとして貼り付け`
- `Markdown 渲染输入消息` → `Markdownで入力メッセージをレンダリング`
- `快速敲击3次空格翻译` → `スペースを3回素早く押して翻訳`
- `目标语言` → `ターゲット言語`

With tabs and figures.

Hint block for the triple space translation:
{% hint style="warning" %}
注意：该操作会覆盖原文。 → 
{% hint style="warning" %}
注意：この操作は原文を上書きします。
{% endhint %}

## 助手设置 → ## アシスタント設定

Instructions about where to set: 在助手界面选择... → 
アシスタントインターフェースで設定したい<mark style="background-color:yellow;">アシスタント名</mark>を選択→<mark style="background-color:yellow;">右クリックメニュー</mark>で対応する設定を選択

### 编辑助手 → ### アシスタントの編集

Hint block:
{% hint style="info" %}
助手设置作用于该助手下的所有话题。 → 
{% hint style="info" %}
アシスタント設定は、そのアシスタント下のすべてのトピックに適用されます。
{% endhint %}

Then the figure.

#### 提示词设置 → #### プロンプト設定

- `名称` → `名前`
- `提示词` → `プロンプト`

#### 模型设置 → #### モデル設定

- `默认模型` → `デフォルトモデル`
- `自动重置模型` → `モデルを自動リセット`
- `温度 (Temperature)` → `温度 (Temperature)`
- `Top P (核采样)` → `Top P (核