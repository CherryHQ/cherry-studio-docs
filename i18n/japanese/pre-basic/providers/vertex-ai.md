---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# Vertex AI

## チュートリアルの概要

### 1. APIキーの取得

* GeminiのAPIキーを取得する前に、Google Cloudプロジェクトが必要です（既にお持ちの場合はこの手順をスキップしてください）
* [Google Cloud](https://console.cloud.google.com/projectcreate)にアクセスしてプロジェクトを作成し、プロジェクト名を入力して作成ボタンをクリック

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AIコンソール](https://console.cloud.google.com/vertex-ai)にアクセス
* 作成したプロジェクトで[Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)を有効化

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. APIアクセス権の設定

* [サービスアカウント](https://console.cloud.google.com/iam-admin/serviceaccounts)権限ページを開き、サービスアカウントを作成

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* サービスアカウント管理ページで作成したサービスアカウントを探し、`キー`をクリックして新しいJSON形式キーを作成

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* 作成に成功すると、キーファイルがJSON形式で自動的にダウンロードされます。**必ず安全な場所に保管してください**

## 3. Cherry StudioでのVertex AI設定

* Vertex AIプロバイダを選択
* JSONファイルの対応するフィールドを入力

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

クリックして[モデル](https://console.cloud.google.com/vertex-ai/model-garden)を追加すると、すぐに使い始められます！