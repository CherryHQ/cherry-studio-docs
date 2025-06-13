---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# ネットワーク接続モード

{% hint style="info" %}
ネットワーク接続が必要なシナリオ例：

* 時効性のある情報：例）本日/今週/つい先ほどの金先物価格など
* リアルタイムデータ：例）天気、為替レートなどの動的値
* 新興知識：例）新事象、新概念、新技術など...
{% endhint %}

### 1. ネットワーク接続の有効化方法

Cherry Studioの質問入力ウィンドウで【地球アイコン】をクリックすると、ネットワーク接続が有効になります。

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>地球アイコンをクリック - ネットワーク接続を有効化</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>ネットワーク接続機能が有効化された状態</p></figcaption></figure>

### 2. 特記事項：ネットワーク接続には2つのモードがあります

#### モード1：モデルプロバイダーの大規模モデルが組み込みネットワーク機能を提供

この場合、ネットワーク接続を有効にすると、すぐにネットワークサービスを利用できます。

{% hint style="warning" %}
対話インターフェイスの上部、モデル名の後に地球アイコンが表示されているかどうかで、そのモデルがネットワーク接続をサポートしているかどうかを即座に判断できます。
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

モデル管理ページでも、この方法でネットワーク接続をサポートするモデルを迅速に識別できます。

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studioが現在サポートしているネットワーク対応モデルプロバイダー**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter（全モデルがネットワーク接続をサポート）</mark>
> * <mark style="color:green;">Tencent Hunyuan（騰訊混元）</mark>
> * <mark style="color:green;">Zhipu AI（智譜AI）</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian（阿里雲百煉）など</mark>

{% hint style="danger" %}
特記事項：

モデルに地球アイコンが表示されていなくても、ネットワーク接続が可能な特殊なケースがあります。以下の攻略ガイドで説明しているようなケースです。
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### モード2：Tavilyサービスを活用したネットワーク接続

ネットワーク機能を持たない大規模モデル（名前後に地球アイコンなし）を使用中に、リアルタイム情報を取得する必要がある場合、Tavilyウェブ検索サービスを利用します。

**Tavilyサービスの初回利用時**には設定画面がポップアップ表示されます。指示に従って操作してください（非常に簡単です）。

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>ポップアップで「設定へ」をクリック</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>「シークレットキーを取得」をクリック</p></figcaption></figure>

「シークレットキーを取得」をクリックすると、自動的に**Tavily公式サイト**のログイン/登録ページに移動します。登録してログインした後、APIキーを作成し、そのキーをCherry Studioにコピーします。

{% hint style="danger" %}
登録方法がわからない場合は、同ディレクトリ内のTavilyネットワーク接続登録ガイドを参照してください。
{% endhint %}

**Tavily登録参考ドキュメント：**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

以下の画面が表示されれば、登録は成功です。

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>キーをコピー</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>キーを貼り付けて完了</p></figcaption></figure>

再度試して効果を確認しましょう。結果から、ネットワーク検索が正常に行われており、検索結果数はデフォルト設定値（5件）となっています。

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
注意：Tavilyには月あたりの無料利用制限があり、超過すると有料となります～
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS：誤りを見つけた際は、お気軽にご連絡ください。