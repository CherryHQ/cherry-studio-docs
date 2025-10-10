---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---
# オンラインンモード


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




{% hint style="info" %}
ネットワーク接続が必要なシシナリオ例：

* タイムリーな情報：例）今日/今週/直近の金先物価格など
* リアルタイムデータ：例）天気、為替レートなどの動的値
* 新興知識：例）新事物、新概念、新技術など...
{% endhint %}

### 一、ネットワーク接続の有効化方法

Cherry Studioの質問ウィンドウで【地球アイコン】をクリックするとネットワーク接続が有効になります。

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>地球アイコンをクリック - ネットワーク接続を有効化</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>表示 - ネットワーク接続機能が有効化されました</p></figcaption></figure>

### 二、特記事項：ネットワーク接続の2つのモード

#### モード1：モデルプロバイダーが提供するネットワーク対応モデル

この場合、ネットワーク接続を有効にするだけで直接利用可能です。

{% hint style="warning" %}
質問インターフェース上部のモデル名横に地球マークが表示されているかどうかで、そのモデルのネットワーク対応状況を即座に判断できます。
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

モデル管理ページでも、この方法でネットワーク対応モデルを迅速に識別できます。

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio が現在サポートするネットワーク対応モデルプロバイダー:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter（全モデルネットワーク対応）</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian など</mark>

{% hint style="danger" %}
特記事項：
モデルに地球アイコンが表示されていなくてもネットワーク接続が可能な特殊ケースがあります（下記チュートリアル参照）。
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### モード2：Tavilyサービスによるネットワーク機能拡張

地球アイコンが表示されていないモデルでリアルタイム情報が必要な場合、Tavilyウェブ検索サービスを利用します。

**初回Tavily利用時**は設定ポップアップが表示されます。指示に従って操作してください。

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>ポップアップ表示 → [設定]をクリック</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>[キーを取得]をクリック</p></figcaption></figure>

キー取得クリック後、**Tavily公式サイト**の登録ページへ自動遷移します。登録後、APIキーを作成しCherry Studioにコピーします。

{% hint style="danger" %}
登録方法が不明な場合、同ディレクトリのtavily登録チュートリアルを参照してください。
{% endhint %}

**Tavily登録参考資料：**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

下記画面表示で登録成功です。

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>キーをコピー</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>キーを貼り付け → 設定完了</p></figcaption></figure>

再度実行すると、デフォルト設定値（5件）で正常に検索されます。

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
注意：Tavilyは月間無料利用制限があり、超過時は課金が発生します
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS：不具合を発見された場合はお知らせください。