---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## チュートリアルの概要

### 1. APIキーの取得

* GeminiのAPIキーを取得するには、事前にGoogle Cloudプロジェクトが必要です（既にお持ちの場合はこの手順は不要です）
* [Google Cloud](https://console.cloud.google.com/projectcreate)でプロジェクトを作成し、プロジェクト名を入力後「プロジェクトを作成」をクリック

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AIコンソール](https://console.cloud.google.com/vertex-ai)にアクセス
* 作成したプロジェクト内で[Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)を有効化

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. APIアクセス権限の設定

* [サービスアカウント](https://console.cloud.google.com/iam-admin/serviceaccounts)権限ページで新規サービスアカウントを作成

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* サービスアカウント管理画面で作成したアカウントを選択し、`鍵` → `新しい鍵を追加`からJSON形式の鍵を作成

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* 作成後、鍵ファイルがJSON形式で自動ダウンロードされます。**厳重に保管してください**

## 3. Cherry StudioでのVertex AI設定

* プロバイダーでVertex AIを選択
* JSONファイルの対応項目を入力

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[モデル追加](https://console.cloud.google.com/vertex-ai/model-garden)をクリックすれば、すぐに利用開始できます！