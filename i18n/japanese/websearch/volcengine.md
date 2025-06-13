---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 火山エンジンのネットワーク接続手順

### 1. 「火山エンジン」アカウントの登録・ログイン <a href="#rclz7" id="rclz7"></a>

公式サイトにアクセス：[https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>火山エンジン公式サイト</p></figcaption></figure>

---

### 2. 「ネットワーク接続可能な」アプリケーションの作成 <a href="#gvzaa" id="gvzaa"></a>

**2.1** 火山エンジンにログイン後、「火山方舟」ページへ移動:  
[https://console.volcengine.com/ark](https://console.volcengine.com/ark)

**2.2** <mark style="color:red;">**「マイアプリ」→「アプリ作成」→「ノーコード」→「1対1チャット」**</mark>を順にクリック

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

---

### 3. 情報入力とアプリ公開 <a href="#zzdfe" id="zzdfe"></a>

**アプリ名**：要件に従い任意の名前を付与（<mark style="color:red;">**\*必須項目**</mark>、他は空欄可）

<mark style="color:red;">**重要: ネットワークプラグインを有効化（事前に有効化が必要）**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1 ネットワークプラグイン機能の有効化（費用と無料枠に注意） <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>「今すぐ購入」をクリックし、下図が表示されるまで進めれば有効化成功</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>ステータスを確認、これで有効化成功</p></figcaption></figure>

「アプリ情報入力」画面に戻り操作を続行

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2 ネットワーク検索「詳細設定」説明 <a href="#sp6uz" id="sp6uz"></a>

実情に応じて選択推奨：
* 入出力を精密制御する場合 → **カスタム呼び出し**
* 簡便化したい場合 → **自動呼び出し（デフォルト）**
* 費用を気にせず最新情報が必要な場合 → **強制起動**

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3 アプリの公開 <a href="#fe1gf" id="fe1gf"></a>

右上の「公開」ボタンをクリックしてアプリを作成

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

---

### 4. API Key の取得 <a href="#jtqlu" id="jtqlu"></a>

**「API 呼び出しガイド」→「API Keyを選択・コピー」→「確認・選択」**の順に操作

API Keyをコピー後、Cherry Studioに貼り付け（詳細手順は下図参照）

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

> **注意**：API Keyがない場合、ポップアップ右上の「**API Key作成**」から生成後コピー

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

---

### 5. Cherry StudioでAPI Keyを使ったDeepSeek-R1ネットワーク接続 <a href="#lrefj" id="lrefj"></a>

#### 5.1 Cherry Studio開く→「設定」→「任意の名称」→「タイプ：openAI」 <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2 URLとKeyの設定 <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">※URLが分からない場合、または北京ノードでない場合は下記位置を確認（末尾の「/」忘れに注意）:</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3 モデル名の追加 <a href="#qmh3i" id="qmh3i"></a>

**重要**：下部の小文字をモデル名としてコピー（誤るとエラー発生）

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

---

### 6. 動作プレビュー <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>