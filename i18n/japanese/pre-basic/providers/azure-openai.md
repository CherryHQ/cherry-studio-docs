---
icon: cloud
---

# Azure OpenAI

Cherry Studio V2 の組み込み Azure OpenAI テンプレートは、Microsoft Azure にデプロイしたモデルへの接続に使用します。**API Version** に応じて Azure Responses またはデプロイ形式の呼び出し方法を選択するため、Base URL、API Version、モデル ID を Azure リソースの設定と一致させる必要があります。

{% hint style="info" %}
Azure OpenAI と OpenAI の公式 API は別のサービスです。Azure リソースの Endpoint、API Key、API Version、デプロイ名を OpenAI テンプレートに直接入力することはできません。
{% endhint %}

## 始める前の準備

[Azure Portal](https://portal.azure.com/) で次の情報を準備してください。

- Azure AI Foundry または Azure OpenAI リソースの Endpoint
- そのリソースの API Key
- 現在のリソースが対応する API Version
- 呼び出し可能なモデルのデプロイが 1 つ以上

日付形式の API Version を使用する場合は、各モデルの**デプロイ名**も確認してください。デプロイ名は Azure でユーザーが設定するため、基になるモデル名とは異なる場合があります。

## Azure OpenAI を設定する

1. `設定 → モデルプロバイダー` を開きます。
2. 左側のフィルターを**すべてのプロバイダー**に切り替え、**Azure OpenAI** を選択します。
3. Azure リソースの API Key を入力します。
4. Base URL にリソースの Endpoint を入力します。例：`https://<resource>.openai.azure.com`
5. Azure リソースが現在対応している API Version を入力します。
6. 画面上部にあるプロバイダーのスイッチをオンにします。
7. 使用するモデルを追加して有効にします。
8. 接続チェックとモデルのヘルスチェックを実行します。

{% hint style="warning" %}
Base URL にはリソースの Endpoint だけを入力してください。`/openai`、`/v1`、`/chat/completions`、デプロイパスを追加しないでください。Cherry Studio は現在の設定に応じてリクエストパスを補います。
{% endhint %}

{% hint style="danger" %}
Azure API Key をチャットメッセージ、ドキュメント、コードリポジトリ、または問題報告用のスクリーンショットに含めないでください。Key が漏えいした場合は、Azure Portal ですぐに再生成してください。
{% endhint %}

## API Version を選ぶ

Cherry Studio は API Version に応じて呼び出し方法を選択します。

| API Version | Cherry Studio の処理方法 | モデル設定の要点 |
| --- | --- | --- |
| `v1` または `preview` | Azure Responses 方式を使用 | 現在の Azure リソースが提供するモデルルーティングに合わせて設定 |
| 日付形式のバージョン（例：`2024-xx-xx-preview`） | Azure のデプロイ形式 URL を使用 | モデル ID を Azure のデプロイ名と一致させる |

API Version には、Azure リソースが実際に対応している値を指定する必要があります。画面の例は形式を示すだけで、そのバージョンが使用中のリソースに適用できるとは限りません。

既存の接続をアップグレードした後に突然 404 が返される場合は、Azure Portal または [Azure OpenAI ドキュメント](https://learn.microsoft.com/azure/ai-services/openai/)で現在の Endpoint、API Version、デプロイ名を確認してから Cherry Studio の設定を変更してください。

## モデルを追加して有効にする

モデルリストで**追加**をクリックし、同期プレビューを確認して変更を適用します。Azure から利用可能なリストが返されない場合は、**カスタム**をクリックしてモデルを手動で入力できます。

日付形式の API Version を使用する場合：

- **モデル ID**には Azure のデプロイ名を入力します。
- 基になるモデルファミリー名がデプロイ名と同じ場合を除き、モデルファミリー名だけを入力しないでください。
- 複数のデプロイは個別に追加する必要があります。
- Azure のデプロイを削除または改名した場合は、Cherry Studio のモデルも合わせて変更してください。

たとえば、Azure でモデルのデプロイ名を `support-prod` に設定した場合、Cherry Studio のモデル ID にも `support-prod` を入力します。基になるモデル名から推測しないでください。

## 接続を確認する

1. Base URL に API パスが追加されていないことを確認します。
2. API Key が同じ Azure リソースのものであることを確認します。
3. API Version がそのリソースでサポートされていることを確認します。
4. 追加して有効にしたモデルを 1 つ選択します。
5. 接続チェックを実行します。
6. 続いてモデルのヘルスチェックを実行します。
7. チャット画面に戻り、簡単なメッセージを送信します。

接続チェックに成功しても、認証情報と基本リクエストが利用できることしか確認できません。画像、推論、ツール呼び出しを使用する場合は、対象のモデルとデプロイがそれぞれの機能に対応しているか個別に検証してください。

## 複数のリソースまたはデプロイを管理する

Azure リソースごとに Endpoint、Key、API Version が異なる場合は、Azure OpenAI プロバイダーを複製して個別に設定できます。

- 各複製に識別しやすい名前を付けます。
- 各複製には、そのリソースに実在するデプロイだけを残します。
- 別のリソースの Key やデプロイ名を 1 つの複製内に混在させないでください。
- API Version を更新するときは、まず 1 つの複製でテストしてからほかの接続を更新します。

これにより、本番、テスト、異なる地域のリソースを分離でき、クォータや権限の問題も特定しやすくなります。

## よくある質問

### 401 が返される

API Key が無効、正しくコピーされていない、または Key と Base URL が同じ Azure リソースに属していません。リソースの Keys and Endpoint ページで改めて確認してください。

### 404 が返される

Base URL、API Version、モデルのデプロイ名を順番に確認してください。余分なパスを追加した、日付形式のバージョンがサポートされていない、基になるモデル名をデプロイ名として使用した、といった原因がよくあります。

### 429 が返される

現在のリソース、地域、またはデプロイがレート制限かクォータ制限に達しています。Azure Portal でクォータと使用量を確認してください。Cherry Studio でモデル名を切り替えても、リソースの制限を回避することはできません。

### モデルを同期できない

Azure の構成によっては、そのまま使用できるモデルリストが返されません。**カスタム**をクリックし、Azure に実在するデプロイをモデルとして追加してからヘルスチェックを実行してください。

### `v1`、`preview`、日付形式のどれを選ぶべきか

Azure リソースと公式ドキュメントが現在対応する方式に従ってください。`v1` または `preview` は Responses 方式を使用し、日付形式のバージョンはデプロイ形式 URL を使用します。モデル名だけを基に API Version を変更しないでください。

一般的な設定は[モデルプロバイダー](README.md)と[モデルプロバイダー設定](../../cherrystudio/preview/settings/providers.md)を参照してください。フィードバック先は[フィードバックとご提案](../../question-contact/suggestions.md)を参照してください。
