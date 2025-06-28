---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

# オンラインモード

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

## オンラインモード

{% hint style="info" %}
ネットワーク接続が必要なシナリオの例：

* 最新情報：今日/今週/直近の金先物価格など。
* リアルタイムデータ：天気、為替レートなどの動的な数値。
* 新興知識：新しいもの、新概念、新技術など...
{% endhint %}

#### 1. オンラインへの接続方法

Cherry Studioの質問ウィンドウで、地球のアイコンをクリックするとオンライン機能を開始できます。

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>地球アイコンをクリック - オンライン接続を開始</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>表示 - オンライン機能が有効化されました</p></figcaption></figure>

#### 2. 特别注意：オンライン機能には二つのモードがあります

**モード1：モデルプロバイダーの大規模モデルにデフォルトでオンライン機能が組み込まれている**

この場合、オンライン機能を開始するだけで、簡単に利用できます。

{% hint style="warning" %}
質問インターフェースの上部、モデル名の後に小さな地球マークが表示されているかどうかで、そのモデルがオンライン機能をサポートしているかをすばやく判断できます。
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

モデル管理ページでも、この方法で、どのモデルがオンライン機能をサポートしているか一目でわかります。

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**現在、Cherry Studioでオンライン機能をサポートしているモデルプロバイダーは以下の通りです**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter（すべてのモデルでオンライン機能をサポート）</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailianなど</mark>

{% hint style="danger" %}
特別注意：\
モデルに地球マークがない場合でもオンライン機能が利用できるケースがあります。以下の攻略チュートリアルで説明されています。
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

**モード2：モデルにオンライン機能がなく、Tavilyサービスで実現する**

オンライン機能を持たない大規模モデルを使用している場合（名前の後に地球マークがない）、リアルタイム情報を取得したいときにTavilyネットワーク検索サービスが必要です。

**初めてTavilyサービスを使用する際**、ポップアップが表示され設定を案内します。指示に従って操作してください - 非常に簡単です！

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>ポップアップで「設定へ」をクリック</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>APIキーを取得をクリック</p></figcaption></figure>

APIキーの取得をクリックすると、自動的に**Tavily公式サイト**のログインページにリダイレクトされます。登録し、ログイン後、APIキーを作成し、そのキーをCherry Studioにコピーしてください。

{% hint style="danger" %}
登録方法がわからない場合は、本ドキュメントの同じディレクトリにあるtavily登録チュートリアルを参照してください。
{% endhint %}

**tavily登録参考ドキュメント：**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

以下のインターフェイスが表示され、登録成功を示しています。

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>キーをコピー</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>キーを貼り付け、完了</p></figcaption></figure>

再度試して効果を確認しましょう。結果は、正常にオンライン検索が行われ、デフォルトで5件の検索結果が取得されています。

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
注意：Tavilyには毎月の無料利用制限があり、超過すると課金が必要です〜
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS：問題を見つけた場合は、お気軽にお問い合わせください。
