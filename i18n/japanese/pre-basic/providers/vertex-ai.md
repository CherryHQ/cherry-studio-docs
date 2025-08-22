---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## チュートリアルの概要

### 1. API Keyの取得

* GeminiのAPI Keyを取得するには、Google Cloudプロジェクトが必要です（既にお持ちの場合はこの手順は不要です）
* [Google Cloud](https://console.cloud.google.com/projectcreate)にアクセスしてプロジェクトを作成し、プロジェクト名を入力して「プロジェクトを作成」をクリックしてください

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AIコンソール](https://console.cloud.google.com/vertex-ai)にアクセス
* 作成したプロジェクトで[Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)を有効化してください

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. APIアクセス権限の設定

* [サービスアカウント](https://console.cloud.google.com/iam-admin/serviceaccounts)権限画面を開き、サービスアカウントを作成

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* サービスアカウント管理ページで作成したサービスアカウントを選択し、`キー`をクリックして新しいJSON形式のキーを作成

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* 作成に成功すると、キーファイルがJSON形式で自動的にPCに保存されます。必ず**適切に保管してください**

## 3. Cherry StudioでのVertex AI設定

* Vertex AIプロバイダーを選択
* JSONファイルの対応するフィールドを入力

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[モデル](https://console.cloud.google.com/vertex-ai/model-garden)をクリックして追加すると、すぐに使い始められます！