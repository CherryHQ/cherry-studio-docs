---
icon: message
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 会話インターフェース

## アシスタントとトピック

### アシスタント

`アシスタント`は、選択したモデルにパーソナライズされた設定を適用するための機能です。プロンプトのプリセットやパラメータ設定などを通じて、モデルの動作を期待するワークフローに合わせて調整できます。

`システムデフォルトアシスタント`は一般的なパラメータ（プロンプトなし）がプリセットされています。直接使用するか、[エージェントページ](agents.md)で必要なプリセットを探して使用できます。

### トピック

`アシスタント`は`トピック`の親集合です。1つのアシスタント配下で複数のトピック（会話）を作成でき、すべての`トピック`は`アシスタント`のパラメータ設定やプロンプトプリセットなどのモデル設定を共有します。

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## ダイアログ内ボタン

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `新トピック` 現在のアシスタント内に新しいトピックを作成。

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `画像/ドキュメントアップロード` 画像アップロードはモデル対応が必要。ドキュメントは自動でテキスト解析されモデルにコンテキストとして提供。

![](../../.gitbook/assets/对话界面/网络搜索.png) `ネット検索` 設定で検索関連情報を設定必須。検索結果はモデルにコンテキストとして渡されます。詳細は[ネットワークモード](../../websearch/)参照。

![](../../.gitbook/assets/对话界面/知识库.png) `ナレッジベース` ナレッジベースを有効化。詳細は[ナレッジベースチュートリアル](../../knowledge-base/knowledge-base.md)参照。

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCPサーバー` MCPサーバー機能を有効化。詳細は[MCPチュートリアル](../../advanced-basic/mcp/)参照。

![](../../.gitbook/assets/对话界面/生成图片.png) `画像生成` デフォルト非表示。画像生成対応モデル（Gemini等）で手動有効化後に使用可能。

{% hint style="info" %}
技術的理由により、画像生成には手動でボタンを有効化する必要があります。この機能最適化後は削除予定。
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `モデル選択` 以降の会話で指定モデルに切り替え（コンテキスト保持）。

![](../../.gitbook/assets/对话界面/快捷短语.png) `クイックフレーズ` 設定でプリセットした常用フレーズを呼び出し（変数対応）。

![](../../.gitbook/assets/对话界面/清空消息.png) `メッセージ消去` 該当トピックの全内容を削除。

![](../../.gitbook/assets/对话界面/展开.png) `拡張` 長文入力用にダイアログ拡大。

![](../../.gitbook/assets/对话界面/清除上下文.png) `コンテキスト消去` 内容削除なしでモデルが認識するコンテキストを切断（過去会話を「忘れる」）。

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `トークン数推定` 推定トークン数表示: `現在のコンテキスト数`、`最大コンテキスト数`（∞は無限コンテキスト）、`現在入力メッセージ文字数`、`推定トークン数`。

{% hint style="info" %}
トークン推定機能であり、実際のトークン数はモデル毎に異なります。モデルプロバイダのデータを基準にしてください。
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `翻訳` 入力内容を英語に翻訳。

## 会話設定

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### モデル設定

アシスタント設定の`モデル設定`と同期。詳細は[アシスタント設定](chat.md#bian-ji-zhu-shou)参照。

{% hint style="info" %}
会話設定のモデル設定は現在のアシスタントのみに適用され、その他の設定はグローバル適用されます（例：メッセージスタイル変更後は全トピックで有効）。
{% endhint %}

### メッセージ設定

#### <mark style="color:blue;">**`メッセージ区切り線`**</mark>:

本文と操作バーを区切る線を表示。

{% tabs %}
{% tab title="開いている時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="閉じている時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`セリフ体フォント使用`**</mark>：

フォントスタイル切替。[カスタムCSS](../../personalization-settings/)でも変更可能。

#### <mark style="color:blue;">**`コード行番号表示`**</mark>：

コードブロックに行番号を表示。

{% tabs %}
{% tab title="閉じている時" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="開いている時" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`コードブロック折りたたみ`**</mark>：

有効時、長いコードを自動折りたたみ。

#### <mark style="color:blue;">**`コードブロック折り返し`**</mark>：

有効時、長い行を自動折り返し。

#### <mark style="color:blue;">**`思考内容自動折りたたみ`**</mark>：

有効時、思考対応モデルの思考過程を自動折りたたみ。

#### <mark style="color:blue;">**`メッセージスタイル`**</mark>：

バブルスタイル/リストスタイル切替。

#### <mark style="color:blue;">**`コードスタイル`**</mark>：

コード表示スタイル切替。

#### <mark style="color:blue;">**`数式レンダリングエンジン`**</mark>：

* KaTeX: 高速レンダリング（性能最適化設計）
* MathJax: 低速だが高機能（記号・コマンド対応広範）

#### <mark style="color:blue;">**`メッセージフォントサイズ`**</mark>：

会話インターフェースのフォントサイズ調整。

### 入力設定

#### <mark style="color:blue;">**`推定トークン数表示`**</mark>：

入力テキストの推定消費トークン数表示（実際のコンテキスト消費トークンではなく参考値）。

#### <mark style="color:blue;">**`長文をファイル形式で貼り付け`**</mark>：

長文貼り付け時、ファイル形式で表示し入力干渉を低減。

#### <mark style="color:blue;">**`Markdownレンダリング（送信メッセージ）`**</mark>：

無効時はモデル返信メッセージのみレンダリング。

{% tabs %}
{% tab title="閉じている時" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="開いている時" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`スペース3連打翻訳`**</mark>：

入力後スペース3連打で英語翻訳（原文上書き）。

{% hint style="warning" %}
注意：原文が上書きされます。
{% endhint %}

#### <mark style="color:blue;">**`ターゲット言語`**</mark>：

翻訳ボタン/スペース3連打翻訳のターゲット言語設定。

## アシスタント設定

アシスタント画面で設定対象の<mark style="background-color:yellow;">アシスタント名</mark>を選択→<mark style="background-color:yellow;">右クリックメニュー</mark>から設定

### アシスタント編集

{% hint style="info" %}
アシスタント設定は該当アシスタント配下の全トピックに適用。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### プロンプト設定

#### <mark style="color:blue;">**`名前`**</mark>：

識別しやすいカスタム名設定。

#### <mark style="color:blue;">**`プロンプト`**</mark>：

エージェントページの記法を参考に編集可能。

#### モデル設定

#### <mark style="color:blue;">**`デフォルトモデル`**</mark>：

アシスタント専用デフォルトモデル固定（エージェント追加時/複製時の初期モデル）。未設定時はグローバル初期モデル（[デフォルトアシスタントモデル](settings/default-models.md#mo-ren-zhu-shou-mo-xing)）を使用。

{% hint style="info" %}
アシスタントデフォルトモデルは[グローバルデフォルトモデル](settings/default-models.md#mo-ren-zhu-shou-mo-xing)より優先度高。未設定時はグローバル値適用。
{% endhint %}

#### <mark style="color:blue;">**`モデル自動リセット`**</mark>：

有効時: トピックで別モデル使用後、新規トピック作成時はアシスタントデフォルトモデルにリセット。無効時は直前トピックのモデルを継承。

> 例：デフォルトモデルgpt-3.5-turboのアシスタントで：
>
> トピック1でgpt-4oに切替後、トピック2作成時:
>
> 自動リセット有効: gpt-3.5-turboで初期化
> 自動リセット無効: gpt-4oを継承

#### <mark style="color:blue;">**`温度 (Temperature)`**</mark> ：

テキスト生成のランダム性/創造性制御（デフォルト0.7）:

* 低温(0-0.3):
  * 高精度出力（コード生成/データ分析向け）
  * 高確率語彙を選択
* 中温(0.4-0.7):
  * 創造性/一貫性のバランス（日常会話向け）
* 高温(0.8-1.0):
  * 高創造性出力（ブレインストーミング向け）
  * 一貫性低下の可能性

#### <mark style="color:blue;">**`Top P (核サンプリング)`**</mark>：

デフォルト1。値↓=出力単調化/理解容易化、値↑=語彙多様化。

* 小値(0.1-0.3):
  * 高確率語彙のみ（技術文書向け）
* 中値(0.4-0.6):
  * バランス調整（汎用タスク向け）
* 大値(0.7-1.0):
  * 広範囲語彙（創造的文章向け）

{% hint style="info" %}
- パラメータは単独/併用可能
- タスクに応じた値選択を推奨
- 実験による最適値探索を推奨
- パラメータ範囲はモデル依存（公式ドキュメント参照）
{% endhint %}

#### <mark style="color:blue;">**`コンテキスト数 (Context Window)`**</mark>

保持するメッセージ数（値↑=コンテキスト長↑/トークン消費↑）:

* 5-10: 通常会話向け
* >10: 複雑タスク向け（長文生成など）
* ※メッセージ数↑=トークン消費↑

#### <mark style="color:blue;">**`メッセージ長制限 (MaxToken)`**</mark>

単一応答の最大[トークン数](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens)。生成回答の質/長さに直結。

> 例：モデル接続テスト時（内容不要）はMaxToken=1で設定可能。

主要モデル上限目安：
- 標準: 32kトークン
- 大規模: 64k～（モデル仕様要確認）

使用目安:
* 通常会話: 500-800
* 短文生成: 800-2000
* コード生成: 2000-3600
* 長文生成: 4000～（モデル対応要）

{% hint style="warning" %}
MaxToken範囲で回答生成されるが、切断/不完全表現が発生する可能性あり（状況に応じ調整必要）。
{% endhint %}

#### <mark style="color:blue;">**`ストリーミング出力（Stream）`**</mark>

データを逐次処理・転送する方式（タイプライター効果）。リアルタイム性↑/効率性↑。

* 無効時: 全生成後に一括出力（メッセージ受信感覚）
* 有効時: 逐次出力（生成毎に即時送信）

{% hint style="info" %}
非ストリーム専用モデル（初期o1-mini等）は無効化必須。
{% endhint %}

#### <mark style="color:blue;">**`カスタムパラメータ`**</mark>

リクエストボディに追加パラメータ（`presence_penalty`等）を付加（高度設定）。

> top-p/maxtokens/stream等も同類パラメータ。
>
> 記法: パラメータ名—型（テキスト/数値等）—値。参考：[ドキュメント](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
各プロバイダ固有パラメータあり（公式ドキュメント参照必須）。

* カスタムパラメータ > 組み込みパラメータ優先（重複時上書き）
  > 例：`model`設定で全対話固定化可能
* `<kbd>パラメータ名:undefined</kbd>`でパラメータ除外可能。
{% endhint %}