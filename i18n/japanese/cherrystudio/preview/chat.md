---
icon: message
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 対話インターフェース

## アシスタントとトピック

### アシスタント

`アシスタント` は、選択したモデルをカスタマイズするための設定です。プロンプトのプリセットやパラメーターのプリセットなど、これらの設定により、選択したモデルが期待通りに動作するよう調整されます。

`システムデフォルトのアシスタント` は、比較的汎用的なパラメーター（プロンプトなし）をプリセットしています。直接使用するか、[エージェントページ](agents.md) で必要なプリセットを探して使用できます。

### トピック

`アシスタント` は `トピック` の親集合です。1つのアシスタントの下に複数のトピック（つまり対話）を作成でき、すべての `トピック` は `アシスタント` のパラメーター設定やプリセットされたプロンプトなどのモデル設定を共有します。

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 対話ボックス内のボタン

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `新規トピック`: 現在のアシスタント内に新しいトピックを作成します。

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `画像またはドキュメントをアップロード`: 画像のアップロードはモデルのサポートが必要です。ドキュメントのアップロードは自動的にテキストに解析され、モデルにコンテキストとして提供されます。

![](../../.gitbook/assets/对话界面/网络搜索.png) `ウェブ検索`: 設定でウェブ検索関連情報を構成する必要があります。検索結果はコンテキストとして大規模モデルに返されます。詳細は [ネットワーク接続モード](../../websearch/) をご覧ください。

![](../../.gitbook/assets/对话界面/知识库.png) `ナレッジベース`: ナレッジベースを有効にします。詳細は [ナレッジベースチュートリアル](../../knowledge-base/knowledge-base.md) をご覧ください。

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP サーバー`: MCP サーバー機能を有効にします。詳細は [MCP 使用チュートリアル](../../advanced-basic/mcp/) をご覧ください。

![](../../.gitbook/assets/对话界面/生成图片.png) `画像を生成`: デフォルトでは表示されません。画像生成をサポートするモデル（例: Gemini）の場合、手動でアイコンをタップして有効にする必要があります。

{% hint style="info" %}
技術的な理由により、画像を生成するには手動でアイコンをタップする必要があります。このボタンは機能が最適化された後に削除されます。
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `モデルを選択`: 次の対話で、指定したモデルに切り替え、コンテキストを保持します。

![](../../.gitbook/assets/对话界面/快捷短语.png) `クイックフレーズ`: 設定で事前に一般的なフレーズをプリセットし、ここで呼び出して直接入力します。変数をサポートします。

![](../../.gitbook/assets/对话界面/清空消息.png) `メッセージをクリア`: このトピックの下のすべての内容を削除します。

![](../../.gitbook/assets/对话界面/展开.png) `拡大`: 対話ボックスを大きくして、長文の入力を可能にします。

![](../../.gitbook/assets/对话界面/清除上下文.png) `コンテキストをクリア`: 内容を削除せずに、モデルが取得できるコンテキストを切り詰めます。つまり、モデルは以前の対話内容を「忘れ」ます。

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `推定トークン数`: 推定トークン数を表示します。4つのデータはそれぞれ `現在のコンテキスト数`、`最大コンテキスト数`（∞ は無制限のコンテキストを意味）、`現在の入力ボックス内のメッセージ数`、`推定トークン数` です。

{% hint style="info" %}
この機能は推定トークン数のみに使用され、実際のトークン数は各モデルで異なります。モデルプロバイダーのデータを参照してください。
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `翻訳`: 現在の入力ボックス内の内容を英語に翻訳します。

## 対話設定

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### モデル設定

モデル設定はアシスタント設定の `モデル設定` パラメーターと同期します。詳細は [アシスタント設定](chat.md#bian-ji-zhu-shou) をご覧ください。

{% hint style="info" %}
対話設定では、モデル設定のみが現在のアシスタントに適用され、その他の設定はグローバルに適用されます。例：メッセージスタイルをバブルに設定すると、どのアシスタントのトピックでもバブルスタイルになります。
{% endhint %}

### メッセージ設定

#### <mark style="color:blue;">**`メッセージ区切り線`**</mark>:

区切り線を使用して、メッセージ本文と操作バーを分離します。

{% tabs %}
{% tab title="オン" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="オフ" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`セリフ体フォントを使用`**</mark>：

フォントスタイルを切り替えます。現在は [カスタム CSS](../../personalization-settings/) でフォントを変更することもできます。

#### <mark style="color:blue;">**`コードに行番号を表示`**</mark>：

モデル出力のコードスニペットにコードブロックの行番号を表示します。

{% tabs %}
{% tab title="オフ" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="オン" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`コードブロックを折り畳み可能`**</mark>：

オンにすると、コードスニペットが長い場合、自動的にコードブロックが折り畳まれます。

#### <mark style="color:blue;">**`コードブロックを折り返し可能`**</mark>：

オンにすると、コードスニペットの1行が長い場合（ウィンドウを超える）、自動的に折り返されます。

#### <mark style="color:blue;">**`思考内容を自動折り畳み`**</mark>：

オンにすると、思考をサポートするモデルで思考が完了した後、思考プロセスが自動的に折り畳まれます。

#### <mark style="color:blue;">**`メッセージスタイル`**</mark>：

対話インターフェースをバブルスタイルまたはリストスタイルに切り替えられます。

#### <mark style="color:blue;">**`コードスタイル`**</mark>：

コードスニペットの表示スタイルを切り替えます。

#### <mark style="color:blue;">**`数式レンダリングエンジン`**</mark>：

* KaTeX: レンダリング速度が速く、パフォーマンス最適化用に設計されています。
* MathJax: レンダリングが遅いですが、より多くの数学記号とコマンドをサポートし、機能が豊富です。

#### <mark style="color:blue;">**`メッセージフォントサイズ`**</mark>：

対話インターフェースのフォントサイズを調整します。

### 入力設定

#### <mark style="color:blue;">**`推定トークン数を表示`**</mark>：

入力ボックスに入力テキストで推定消費されるトークン数を表示します（実際のコンテキスト消費トークンではなく、参考用です）。

#### <mark style="color:blue;">**`長いテキストをファイルとして貼り付け`**</mark>：

他の場所から長いテキストをコピーして入力ボックスに貼り付けると、自動的にファイルスタイルで表示され、後続の入力の妨げを減らします。

#### <mark style="color:blue;">**`入力メッセージをMarkdownでレンダリング`**</mark>：

オフの場合、モデルの応答メッセージのみをレンダリングし、送信メッセージはレンダリングしません。

{% tabs %}
{% tab title="オフ" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="オン" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`スペースを3回素早く連打して翻訳`**</mark>：

対話インターフェースの入力ボックスでメッセージを入力した後、スペースを3回連続で連打すると、入力内容を英語に翻訳します。

{% hint style="warning" %}
注意：この操作は原文を上書きします。
{% endhint %}

#### <mark style="color:blue;">**`ターゲット言語`**</mark>：

入力ボックスの翻訳ボタンとスペース3回連打翻訳のターゲット言語を設定します。

## アシスタント設定

アシスタントインターフェースで設定する<mark style="background-color:yellow;">アシスタント名</mark>を選択→<mark style="background-color:yellow;">右クリックメニュー</mark>で対応する設定を選択

### アシスタントを編集

{% hint style="info" %}
アシスタント設定は、そのアシスタントの下のすべてのトピックに適用されます。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### プロンプト設定

#### <mark style="color:blue;">**`名称`**</mark>：

便利に識別できるようにアシスタント名をカスタマイズできます。

#### <mark style="color:blue;">**`プロンプト`**</mark>：

プロンプトのことです。エージェントページのプロンプトの書き方を参照して内容を編集できます。

#### モデル設定

#### <mark style="color:blue;">**`デフォルトモデル`**</mark>：

このアシスタントにデフォルトモデルを固定できます。エージェントページから追加するか、アシスタントをコピーする場合、初期モデルがこのモデルになります。この項目を設定しない場合、初期モデルはグローバル初期モデル（つまり [デフォルトアシスタントモデル](settings/default-models.md#mo-ren-zhu-shou-mo-xing) ）になります。

{% hint style="info" %}
アシスタントのデフォルトモデルには2種類あります：1つは [グローバルデフォルト対話モデル](settings/default-models.md#mo-ren-zhu-shou-mo-xing)、もう1つはアシスタントデフォルトモデルです。アシスタントデフォルトモデルの優先度はグローバルデフォルト対話モデルよりも高くなります。アシスタントデフォルトモデルを設定しない場合、アシスタントデフォルトモデル = グローバルデフォルト対話モデルになります。
{% endhint %}

#### <mark style="color:blue;">**`モデルを自動リセット`**</mark>：

オン時 – そのトピックの使用中に他のモデルに切り替えた場合、新規トピックを作成すると新規トピックのモデルがアシスタントのデフォルトモデルにリセットされます。オフ時は、新規トピックのモデルは前のトピックで使用したモデルを引き継ぎます。

> 例：アシスタントのデフォルトモデルが gpt-3.5-turbo の場合、そのアシスタントの下でトピック1を作成し、トピック1の対話中に gpt-4o に切り替えた場合：
>
> 自動リセットが有効：新規トピック2を作成すると、トピック2のデフォルト選択モデルは gpt-3.5-turbo；
>
> 自動リセットが無効：新規トピック2を作成すると、トピック2のデフォルト選択モデルは gpt-4o。

#### <mark style="color:blue;">**`温度 (Temperature)`**</mark> ：

温度パラメーターは、モデルが生成するテキストのランダム性と創造性を制御します（デフォルト値 0.7）。具体的には：

* 低温度値(0-0.3)：
  * 出力がより確定的で集中したものになる
  * コード生成、データ分析など精度が必要なシナリオに適する
  * 最も確率の高い単語を選択する傾向がある
* 中程度温度値(0.4-0.7)：
  * 創造性と一貫性のバランスが取れる
  * 日常会話、一般的な執筆に適する
  * チャットボット対話に推奨 (0.5 前後)
* 高温度値(0.8-1.0)：
  * より創造的で多様性のある出力を生成
  * 創造的執筆、ブレインストーミングなどのシナリオに適する
  * ただし、テキストの一貫性が低下する可能性あり

#### <mark style="color:blue;">**`Top P (核サンプリング)`**</mark>：

デフォルト値は 1。値が小さいほど、AI が生成する内容は単調になり、理解しやすくなります。値が大きいほど、AI の応答の語彙範囲が広がり、多様性が増します。

核サンプリングは、単語選択の確率しきい値を制御して出力に影響します：

* 小さい値(0.1-0.3)：
  * 最高確率の単語のみを考慮
  * 出力が保守的で制御可能
  * コードコメント、技術文書などのシナリオに適する
* 中程度値(0.4-0.6)：
  * 単語多様性と精度のバランス
  * 一般的な対話や執筆タスクに適する
* 大きい値(0.7-1.0)：
  * より広範な単語選択を考慮
  * より豊富で多様な内容を生成
  * 表現の多様性が必要な創造的執筆などに適する

{% hint style="info" %}
- これらのパラメーターは独立して使用するか、組み合わせて使用できます
- 特定のタスクタイプに適したパラメーター値を選択
- 特定のアプリケーションシナリオに最適なパラメーター組み合わせを実験的に見つけることを推奨
- 上記の内容は参照と概念理解のためのものであり、提示されたパラメーター範囲がすべてのモデルに適するとは限りません。モデル関連ドキュメントで提供される推奨パラメーターを参照してください。
{% endhint %}

#### <mark style="color:blue;">**`コンテキスト数 (Context Window)`**</mark>

コンテキストに保持するメッセージの数。値が大きいほど、コンテキストが長くなり、消費されるトークンが増えます：

* 5-10：通常の対話に適する
* \>10：より長いメモリが必要な複雑なタスク（例：執筆アウトラインに沿って段階的に長文を生成するタスクで、生成されたコンテキストの論理的一貫性を確保