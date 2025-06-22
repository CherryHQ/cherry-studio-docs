---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 火山エンジンでのネットワーク接続方法

### 1、「火山エンジン」アカウントのログイン/登録 <a href="#rclz7" id="rclz7"></a>

公式サイトにアクセス：[https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>火山エンジン公式サイト</p></figcaption></figure>

### 2、ネットワーク接続可能な「マイアプリ」を作成 <a href="#gvzaa" id="gvzaa"></a>

2.1、 火山エンジンにログインし、「火山方舟」ページへ移動： [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2、 **順番にクリック：**<mark style="color:red;">**「マイアプリ」→「アプリ作成」→「ノーコード」→「シングルチャット」**</mark> 

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3、情報入力とアプリ公開 <a href="#zzdfe" id="zzdfe"></a>

**アプリ名**：任意の名前を指定（<mark style="color:red;">**\*必須項目**</mark>、他は空欄可）

<mark style="color:red;">**重要：ネットワークプラグインを有効化（事前にアクティベートが必要）**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1、 ネットワークプラグイン機能のアクティベート（費用制限と無料枠に注意） <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>「今すぐ購入」をクリックし、以下の画面が表示されるまで手順を進めるとアクティベーション完了</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>ステータスを確認、これでアクティベーション成功</p></figcaption></figure>

その後、先ほどの「アプリ情報入力」画面に戻って操作を続行

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2、ネットワーク検索「詳細設定」説明 <a href="#sp6uz" id="sp6uz"></a>

推奨設定：

* 入出力を精密制御する場合：「**カスタム呼び出し**」を選択
* 簡便化したい場合：デフォルトの「**自動呼び出し**」を使用
* 情報鮮度を最優先する場合：「**強制有効化**」を選択

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3、アプリ公開 <a href="#fe1gf" id="fe1gf"></a>

右上の「公開」ボタンをクリックしアプリ作成完了

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4、API Keyの取得 <a href="#jtqlu" id="jtqlu"></a>

**「API呼び出しガイド」→「API Key選択＆コピー」→「表示して選択」**

API Keyをコピーし、cherry studioに貼り付け（詳細は以下画面参照）

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

注意：API Keyがない場合、ポップアップ右上の「**API Key作成**」から生成後コピー

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5、cherry studioでAPI Keyを使用したdeepseek-R1ネットワークアクセス <a href="#lrefj" id="lrefj"></a>

#### 5.1、cherry studio起動 → 「設定」→「任意名称入力」→「タイプ：openAI」 <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2、URLとキーの設定 <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">注意：URLが見つからない/北京ノードでない場合、こちらで確認（末尾の「/」忘れずに）：</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3、モデル名の追加 <a href="#qmh3i" id="qmh3i"></a>

注：小文字表記のモデル名をコピー（誤るとエラー発生）

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6、 動作プレビュー <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>