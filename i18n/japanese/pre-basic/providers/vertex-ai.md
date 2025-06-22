---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# Vertex AI

## チュートリアル概要

### 1. API Keyの取得

* GeminiのAPI Keyを取得する前に、Google Cloudプロジェクトが必要です（既にお持ちの場合はこの手順をスキップ可）
* [Google Cloud](https://console.cloud.google.com/projectcreate)でプロジェクトを作成し、プロジェクト名を入力して「プロジェクトを作成」をクリック

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AIコンソール](https://console.cloud.google.com/vertex-ai)にアクセス
* 作成したプロジェクトで[Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)を有効化

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. APIアクセス権限の設定

* [サービスアカウント](https://console.cloud.google.com/iam-admin/serviceaccounts)権限ページでサービスアカウントを作成

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* サービスアカウント管理ページで作成したアカウントを選択し、「鍵」をクリックして新規JSON形式鍵を作成

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* 作成成功後、鍵ファイルがJSON形式で自動的にPCに保存されます。**必ず安全に保管してください**

## 3. Cherry StudioでVertex AIを設定

* Vertex AIプロバイダを選択
* JSONファイルの対応するフィールドに入力

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[モデル](https://console.cloud.google.com/vertex-ai/model-garden)を追加をクリックすると、すぐに使い始められます！