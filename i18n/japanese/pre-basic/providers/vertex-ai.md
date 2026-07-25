---
icon: cloud
---

# Vertex AI

Cherry Studio V2 の組み込み Vertex AI テンプレートは、Google Cloud の **Service Account** を使用して Vertex AI に接続します。プロジェクト ID、場所、Service Account のクライアントメールと秘密鍵が必要で、Gemini API Key は使用しません。

V2 は Vertex AI 上の Gemini モデルを呼び出せるだけでなく、利用可能な Claude モデルには Vertex Anthropic ルートを選択できます。最終的な利用範囲は、プロジェクト、場所、権限、Model Garden での実際の提供状況によって異なります。

{% hint style="info" %}
Google AI Studio の Gemini API Key をこのページの設定に直接使用することはできません。Gemini API Key だけを持っている場合は、[Google Gemini](google-gemini.md) プロバイダーを使用してください。
{% endhint %}

## 始める前の準備

Google Cloud で次の準備を行います。

- Google Cloud プロジェクトを選択または作成する
- プロジェクトの課金を有効にする
- Vertex AI API を有効にする
- Cherry Studio 専用の Service Account を作成する
- 対象モデルの呼び出しに必要な最小限の権限をアカウントへ付与する
- Service Account の JSON キーを作成し、安全にダウンロードする
- 対象モデルを利用できる Location を確認する

Google の公式クイックスタートでは、通常、呼び出し元に **Vertex AI User**（`roles/aiplatform.user`）権限が必要です。企業プロジェクトでカスタム IAM ロールを使用している場合は、組織のポリシーに従って管理者から権限を付与してもらってください。

関連するページ：

- [Vertex AI クイックスタート](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)
- [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)

## JSON キーからフィールドを確認する

Cherry Studio では、現在、次の内容を手動で入力する必要があります。

| Cherry Studio のフィールド | Service Account JSON または Google Cloud の値 |
| --- | --- |
| クライアントメール | `client_email` |
| 秘密鍵 | `private_key`（BEGIN/END 行を含む全体） |
| プロジェクトID | `project_id` |
| 場所 | 対象モデルを実際に利用できる Location（例：`us-central1`） |

秘密鍵をコピーするときは、元の改行と `-----BEGIN PRIVATE KEY-----`、`-----END PRIVATE KEY-----` を維持してください。

{% hint style="danger" %}
Service Account の秘密鍵は機密性の高い認証情報です。完全な JSON、`private_key`、またはクライアント設定ページをチャットメッセージ、ドキュメント、コードリポジトリ、問題報告用のスクリーンショットに含めないでください。漏えいした場合は、Google Cloud で直ちにそのキーを削除し、新しいキーを作成してください。
{% endhint %}

## Vertex AI を設定する

1. `設定 → モデルプロバイダー` を開きます。
2. 左側のフィルターを**すべてのプロバイダー**に切り替え、**VertexAI** を選択します。
3. **クライアントメール**に JSON の `client_email` を入力します。
4. **秘密鍵**に完全な `private_key` を入力します。
5. **プロジェクトID**に `project_id` を入力します。
6. **場所**に対象モデルを利用できる Location を入力します。
7. API アドレスは空のままにします。
8. 画面上部にあるプロバイダーのスイッチをオンにします。
9. 使用するモデルを追加して有効にします。

{% hint style="warning" %}
Vertex AI の API アドレスは、通常、プロジェクトと場所から自動生成されるため、手動入力はおすすめしません。リバースプロキシを使用し、その完全なパスを理解している場合にのみ変更してください。
{% endhint %}

## モデルを追加して選択する

モデルリストで**追加**をクリックし、同期プレビューを確認して変更を適用します。リモートから対象モデルが返されない場合は、**カスタム**をクリックし、Model Garden または Google の公式ドキュメントに記載されたモデル ID を入力できます。

- Gemini モデルは Google Generate Content 機能を使用します。
- Claude モデルは Vertex Anthropic ルートを使用します。
- モデルは現在のプロジェクトと Location で利用可能でなければなりません。
- サードパーティモデルは、別途有効化、認可、または規約への同意が必要な場合があります。
- モデル名、場所、バージョンをすべて一致させる必要があり、別のプロジェクトのモデル ID だけをコピーして使用することはできません。

旧ドキュメントにあった「Claude は現在サポートされていない」という説明は、V2 には該当しません。ただし、コードがルーティングに対応していても、Google Cloud プロジェクトにそのモデルの権限が付与されているとは限りません。

## 接続を確認する

1. 4 つの必須フィールドが、同じ Service Account とプロジェクトのものであることを確認します。
2. Vertex AI API が有効になっていることを確認します。
3. Service Account に必要な IAM 権限があることを確認します。
4. 追加して有効にしたモデルを 1 つ選択します。
5. 接続チェックを実行します。
6. 続いてモデルのヘルスチェックを実行します。
7. チャット画面に戻り、簡単なメッセージを送信します。

Gemini は利用できても Claude を利用できない場合は、Gemini の設定を変更するのではなく、Claude が現在のプロジェクト、場所、Model Garden で提供されているかを優先して確認してください。

## 複数のプロジェクトまたは場所を管理する

プロジェクトまたは場所ごとに異なる認証情報を使用する場合は、VertexAI プロバイダーを複製して個別に設定できます。

- 名前にプロジェクトまたは場所を含めます。
- 各複製には、その環境で利用できるモデルだけを残します。
- プロジェクト A の Service Account とプロジェクト B のプロジェクト ID を混在させないでください。
- キーをローテーションするときは、各複製を順番に検証します。
- 本番環境とテスト環境では別の Service Account を使用します。

これにより権限の範囲を抑え、クォータ、場所、モデルの利用可否に関する問題も区別しやすくなります。

## よくある質問

### VertexAI が設定されていないと表示される

プロジェクト ID、Location、クライアントメール、秘密鍵のいずれかが空です。秘密鍵が完全であることを確認し、フィールドからフォーカスを外した後、設定が保存されるまで待ってください。

### 401 または認証エラーが返される

Service Account キーが無効、削除済み、秘密鍵の形式が破損している、またはクライアントメールと秘密鍵が一致していません。同じ JSON ファイルを使ってフィールドを確認し直してください。

### 403 が返される

Vertex AI API が有効になっていない、Service Account に IAM 権限がない、または対象モデルがプロジェクトに提供されていません。Google Cloud でプロジェクト、API、ロールを確認してください。

### 404 または「モデルが存在しません」と返される

モデル ID、プロジェクト、Location が一致していません。Model Garden で対象モデルに対応する場所を確認してから、Cherry Studio を更新してください。

### 429 が返される

現在のプロジェクト、場所、またはモデルがクォータ制限に達しています。Google Cloud Console でクォータと使用量を確認してください。

### Gemini は利用できるが、Claude は利用できない

Claude モデルが現在のプロジェクトと場所で提供されていることを確認し、完全で正しいモデル ID を使用してください。Vertex AI の Gemini 権限によってサードパーティモデルの権限が自動的に付与されることはありません。

一般的な設定は[モデルプロバイダー](README.md)と[モデルプロバイダー設定](../../cherrystudio/preview/settings/providers.md)を参照してください。フィードバック先は[フィードバックとご提案](../../question-contact/suggestions.md)を参照してください。
