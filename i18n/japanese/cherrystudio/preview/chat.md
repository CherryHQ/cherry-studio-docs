---
icon: message
---
# 对话インターフェース


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## アシスタントとトピック

### アシスタント

`アシスタント`は、選択したモデルに個別の設定（プロンプトのプリセットやパラメータ設定など）を適用して使用する機能です。これらの設定により、モデルの動作を期待する方向に調整できます。

`システムデフォルトアシスタント`は汎用的なパラメータ（プロンプトなし）をプリセットしています。直接使用するか、[エージェントページ](agents.md)から必要なプリセットを探して使用できます。

### トピック

`アシスタント`は`トピック`の親集合です。1つのアシスタントで複数のトピック（会話）を作成でき、すべての`トピック`はアシスタントのパラメータ設定やプロンプト（prompt）などのモデル設定を共有します。

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## ダイアログ内ボタン

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `新トピック`: 現在のアシスタント内に新しいトピックを作成します。

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `画像/ドキュメントアップロード`: 画像アップロードはモデルサポートが必要です。ドキュメントは自動でテキスト化されコンテキストとして提供されます。

![](../../.gitbook/assets/对话界面/网络搜索.png) `ウェブ検索`: 設定で検索情報を構成後、結果がコンテキストとして大規模モデルに渡されます。詳細は[ネットワークモード](../../websearch/)を参照。

![](../../.gitbook/assets/对话界面/知识库.png) `ナレッジベース`: ナレッジベースを有効化。詳細は[ナレッジベースチュートリアル](../../knowledge-base/knowledge-base.md)を参照。

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCPサーバー`: MCPサーバー機能を有効化。詳細は[MCP使用チュートリアル](../../advanced-basic/mcp/)を参照。

![](../../.gitbook/assets/对话界面/生成图片.png) `画像生成`: デフォルト非表示。画像生成対応モデル（Geminiなど）で手動有効化後に使用可能。

{% hint style="info" %}
技術的制約により、画像生成には手動でのボタン有効化が必要です。機能最適化後、この制限は解除されます。
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `モデル選択`: 現在のコンテキストを保持したまま、指定モデルに切り替えます。

![](../../.gitbook/assets/对话界面/快捷短语.png) `クイックフレーズ`: 設定でプリセットした定型句を直接入力（変数対応）。

![](../../.gitbook/assets/对话界面/清空消息.png) `メッセージ消去`: 該当トピックの全内容を削除します。

![](../../.gitbook/assets/对话界面/展开.png) `拡大`: 長文入力のためダイアログを拡大します。

![](../../.gitbook/assets/对话界面/清除上下文.png) `コンテキスト消去`: 内容を削除せず、モデルが取得できるコンテキストを切断（以前の会話を"忘れる"）。

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `トークン数推定`: `現在コンテキスト数`、`最大コンテキスト数`（∞＝無制限）、`入力中文字数`、`推定トークン数`を表示。

{% hint style="info" %}
これは推定値です。実際のトークン数はモデルごとに異なります。公式数値をご確認ください。
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `翻訳`: 入力内容を英語に翻訳します。

## 会話設定

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### モデル設定

モデル設定はアシスタント設定の`モデル設定`と同期します。詳細は[アシスタント編集](chat.md#bian-ji-zhu-shou)参照。

{% hint style="info" %}
会話設定で有効なのはモデル設定のみ（現在のアシスタント適用）。他の設定はグローバル設定です（例：メッセージスタイル変更は全トピックに適用）。
{% endhint %}

### メッセージ設定

#### <mark style="color:blue;">**`メッセージ区切り線`**</mark>:

本文と操作バーの間に区切り線を表示。

{% tabs %}
{% tab title="オン時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="オフ時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`セリフフォント使用`**</mark>：

フォントスタイル切替。[カスタムCSS](../../personalization-settings/)でも変更可能。

#### <mark style="color:blue;">**`コード行番号表示`**</mark>：

コードブロックに行番号を表示。

{% tabs %}
{% tab title="オフ時" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="オン時" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`コード折り畳み可能`**</mark>：

長いコードブロックを自動折り畳み。

#### <mark style="color:blue;">**`コード折り返し`**</mark>：

長いコード行の自動折り返し。

#### <mark style="color:blue;">**`思考内容自動折り畳み`**</mark>：

思考プロセス対応モデルで、思考完了後自動折り畳み。

#### <mark style="color:blue;">**`メッセージスタイル`**</mark>：

バブルスタイル/リストスタイル切替。

#### <mark style="color:blue;">**`コードスタイル`**</mark>：

コード表示スタイル切替。

#### <mark style="color:blue;">**`数式エンジン`**</mark>：

* KaTeX: 高速レンダリング（性能最適化）
* MathJax: 低速だが高機能（記号/コマンド対応広範）

#### <mark style="color:blue;">**`メッセージフォントサイズ`**</mark>：

会話画面のフォントサイズ調整。

### 入力設定

#### <mark style="color:blue;">**`トークン数推定表示`**</mark>：

入力テキストの推定トークン数表示（実際のコンテキスト消費値とは異なります）。

#### <mark style="color:blue;">**`長文貼り付けをファイル化`**</mark>：

長文貼り付け時にファイル形式で表示（入力妨害軽減）。

#### <mark style="color:blue;">**`送信メッセージのMarkdownレンダリング`**</mark>：

オフ時、送信メッセージはレンダリングされません。

{% tabs %}
{% tab title="オフ時" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="オン時" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`スペース3連打翻訳`**</mark>：

入力後スペース3回連打で英語翻訳。

{% hint style="warning" %}
注意：原文が上書きされます。
{% endhint %}

#### <mark style="color:blue;">**`ターゲット言語`**</mark>：

翻訳ボタン/スペース連打時の翻訳先言語設定。

## アシスタント設定

対象アシスタントの<mark style="background-color:yellow;">名称選択</mark>→<mark style="background-color:yellow;">右クリックメニュー</mark>から設定

### アシスタント編集

{% hint style="info" %}
設定は当該アシスタントの全トピックに適用されます。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### プロンプト設定

#### <mark style="color:blue;">**`名称`**</mark>：

識別しやすいアシスタント名を設定。

#### <mark style="color:blue;">**`プロンプト`**</mark>：

prompt編集。エージェントページのプロンプト例を参考に設定可能。

#### モデル設定

#### <mark style="color:blue;">**`デフォルトモデル`**</mark>：

アシスタント専用デフォルトモデル設定。エージェントページ追加時/複製時はこのモデルが初期値。未設定時はグローバル初期モデル([デフォルトアシスタントモデル](settings/default-models.md#mo-ren-zhu-shou-mo-xing))適用。

{% hint style="info" %}
デフォルトモデルは2種類: [グローバルデフォルト](settings/default-models.md#mo-ren-zhu-shou-mo-xing)とアシスタントデフォルト。アシスタントデフォルトが優先されます。
{% endhint %}

#### <mark style="color:blue;">**`モデル自動リセット`**</mark>：

オン時 - トピック内でモデル切替後、新規トピック作成時にはアシスタントデフォルトモデルにリセット。オフ時は前トピックのモデルを引き継ぎます。

> 例: デフォルト=gpt-3.5-turboのアシスタントで：
> 
> トピック1でgpt-4oに切替後：
> 
> 自動リセットオン → トピック2作成時: gpt-3.5-turbo
> 
> 自動リセットオフ → トピック2作成時: gpt-4o

#### <mark style="color:blue;">**`温度 (Temperature)`**</mark> ：

テキスト生成のランダム性/創造性制御（初期値=0.7）:

* 低値(0-0.3):
  * 出力が確定的/集中
  * コード生成/データ分析向け
* 中値(0.4-0.7):
  * 創造性/一貫性のバランス
  * 日常会話/一般ライティング向け
* 高値(0.8-1.0):
  * 創造的/多様な出力
  * ブレインストーミング向け
  * 一貫性低下の可能性

#### <mark style="color:blue;">**`Top P (核サンプリング)`**</mark>：

初期値=1。値が小さいほど単調で理解しやすい出力。値が大きいほど多様な出力。

核サンプリングによる語彙選択:

* 小値(0.1-0.3):
  * 高確率語彙のみ採用
  * 保守的/制御容易
* 中値(0.4-0.6):
  * 多様性/正確性のバランス
* 大値(0.7-1.0):
  * 幅広い語彙採用
  * 豊富な表現生成

{% hint style="info" %}
- パラメータは単独/併用可能
- タスクに適した値選択
- 実際に試して最適値を見つけることを推奨
- パラメータ範囲はモデル依存。公式ドキュメントを参照。
{% endhint %}

#### <mark style="color:blue;">**`コンテキスト量 (Context Window)`**</mark>

保持するメッセージ数（数値↑=コンテキスト長↑=トークン消費↑）:

* 5-10: 通常会話向け
* \>10: 複雑タスク向け（長文生成など）
* 注意: メッセージ数↑=トークン消費↑

#### <mark style="color:blue;">**`メッセージ長制限 (MaxToken)`**</mark>

単一応答の最大[トークン](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens)数。出力の長さ/品質に直結します。

> 例: モデル接続テスト時、内容不要ならMaxToken=1に設定可能。

主要モデルのMaxToken上限:
- 標準: 32kトークン
- 上位モデル: 64k+ （仕様要確認）

{% hint style="success" %}
推奨値:
* 通常会話: 500-800
* 短文生成: 800-2000
* コード生成: 2000-3600
* 長文生成: 4000+（モデル対応要）
{% endhint %}

{% hint style="warning" %}
出力がMaxTokenで制限されると、コード断片化/不完全表現が発生する可能性があります。状況に応じ調整が必要。
{% endhint %}

#### <mark style="color:blue;">**`ストリーミング出力（Stream）`**</mark>

リアルタイム処理方式。データ生成順次出力（タイプライター効果）。オフ時は全文一括出力。

{% hint style="info" %}
非ストリーミング専用モデル（例: o1-mini初期版）ではこの設定をオフにしてください。
{% endhint %}

#### <mark style="color:blue;">**`カスタムパラメータ`**</mark>

リクエストボディ(body)に追加パラメータ注入（例: `presence_penalty`）。上級者向け。

> top-p/maxtokens/streamなどもこれらのパラメータです。
> 
> 書式: パラメータ名—型（テキスト/数値等）—値。参考: [APIドキュメント](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
各プロバイダ固有のパラメータあり。公式ドキュメント参照が必要です。
{% endhint %}

{% hint style="info" %}
* カスタムパラメータは組み込みパラメータより優先されます（例: カスタム`model`設定で選択モデル無効化）。
* `<kbd>パラメータ名:undefined</kbd>`でパラメータ除外可能。
{% endhint %}