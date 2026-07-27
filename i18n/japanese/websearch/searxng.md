---
description: Cherry Studio V2 で使用できる SearXNG インスタンスをデプロイし、JSON、検索エンジン、Basic 認証を設定します。
icon: searchengin
---

# SearXNG のローカルデプロイと設定

SearXNG は、複数の検索エンジンの結果を自分のインスタンスへ集約できるオープンソースのメタ検索エンジンです。Cherry Studio V2 では、セルフホストした SearXNG をキーワード検索プロバイダーとして設定できます。制御性とプライバシーを重視し、基本的なコンテナ運用ができるユーザーに適しています。

{% hint style="info" %}
SearXNG 自体はオープンソースですが、インスタンスの実行にはローカルまたはサーバーのリソースを使用します。また、上流の検索エンジンにも個別のアクセス制限があります。セルフホストによって検索品質、可用性、匿名性が自動的に保証されるわけではありません。
{% endhint %}

## SearXNG を選ぶ前に

API Key を入力するだけの検索サービスとは異なり、SearXNG ではまずアクセス可能なインスタンスを用意する必要があります。

| 方法 | 用途 | 注意点 |
| --- | --- | --- |
| ローカルデプロイ | 個人利用、短時間の試用 | 直接アクセスできるのはローカルマシンだけで、電源を切ると停止 |
| LAN デプロイ | 複数の信頼できる機器で共有 | 待ち受けアドレスとファイアウォールを正しく設定する必要がある |
| インターネット上でセルフホスト | ネットワークを越えた利用、チーム利用 | HTTPS、認証、レート制限、更新、ログを考慮する必要がある |
| 公開インスタンス | 一時的なテスト | JSON API が無効、レート制限あり、または予告なく停止する場合がある |

不明な公開インスタンスを長期のデフォルトプロバイダーとして使用することは推奨しません。インスタンスの管理者はクエリや接続情報を確認できる可能性があり、公開インスタンスには通常、安定性の保証がありません。

## Cherry Studio がインスタンスに求める条件

利用可能な SearXNG インスタンスは、次の条件を満たす必要があります。

- Cherry Studio を実行する機器からインスタンスのアドレスへアクセスできる
- `/config` がインスタンス設定を返す
- `/search` で `format=json` が許可されている
- 有効な検索エンジンのうち少なくとも 1 つが `general` と `web` の両方のカテゴリーに属している
- Cherry Studio 側のネットワークから検索結果の Web ページへアクセスできる
- リバースプロキシで HTTP Basic Auth を有効にしている場合、Cherry Studio に同じ認証情報を入力する

Cherry Studio のデフォルト：

```text
http://localhost:8080
```

これはプリセットアドレスにすぎません。実際のポートとドメインは、自分のデプロイに合わせてください。

## 公式コンテナテンプレートでデプロイ

SearXNG 公式は、Docker または Podman の Compose テンプレートを推奨しています。以下の手順は Docker と Docker Compose をインストール済みのユーザー向けです。本番環境では、バックアップ、更新、アクセス制御も設定してください。

### 1. ディレクトリとテンプレートを準備

```bash
mkdir -p ./searxng/core-config
cd ./searxng
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example
cp .env.example .env
```

`.env` を開き、テンプレートの説明に従ってポート、インスタンスアドレス、シークレットなどを確認します。テンプレートは SearXNG の更新に伴って変更される場合があります。初回デプロイまたはアップグレード前に、[公式コンテナインストールドキュメント](https://docs.searxng.org/admin/installation-docker.html)を読んでください。

### 2. JSON 出力を有効化

`core-config/settings.yml` に少なくとも次を追加します。

```yaml
use_default_settings: true

search:
  formats:
    - html
    - json
```

{% hint style="warning" %}
Cherry Studio は `format=json` を指定してリクエストします。SearXNG の `search.formats` に `json` がない場合、検索インターフェースは通常 `403 Forbidden` を返します。
{% endhint %}

既存の `settings.yml` がある場合は、`json` 項目をマージしてください。上記の最小例で既存のエンジン、プロキシ、言語、セキュリティ設定を上書きしないでください。

### 3. インスタンスを起動

```bash
docker compose up -d
docker compose ps
```

ログを確認する場合：

```bash
docker compose logs -f core
```

サービス名は公式テンプレートの更新によって変わる場合があります。`core` が見つからないと表示されたら、まず `docker compose ps` を実行し、実際のサービス名を使用してください。

### 4. インスタンスを検証

まずブラウザーでインスタンスのトップページを開き、次にターミナルで JSON API を確認します。アドレスが `http://127.0.0.1:8080` の場合：

```bash
curl "http://127.0.0.1:8080/config"
curl "http://127.0.0.1:8080/search?q=Cherry+Studio&format=json"
```

両方のリクエストが JSON を返す必要があります。2 つ目のレスポンスには利用可能な検索結果も含まれている必要があります。

SearXNG のインターフェースとパラメーターについては、[Search API](https://docs.searxng.org/dev/search_api.html)を参照してください。

## Cherry Studio での設定

### 1. SearXNG 設定を開く

次の画面を開きます。

> **設定 → Web 検索 → SearXNG**

### 2. API Host を入力

インスタンスのルートアドレスを入力し、`/search` や `/config` は手動で追加しないでください。

ローカルの例：

```text
http://127.0.0.1:8080
```

インターネット上の例：

```text
https://search.example.com
```

Cherry Studio が `/config` と `/search` を追加します。

{% hint style="info" %}
デスクトップ版 Cherry Studio はホスト OS 上で直接動作します。Docker がホストへポートをマッピングしている場合は、通常 `127.0.0.1:マッピング先ポート` を使用し、`host.docker.internal` は必要ありません。
{% endhint %}

### 3. Basic 認証を入力

リバースプロキシで HTTP Basic Auth を設定している場合：

1. SearXNG 設定にユーザー名を入力します。
2. 対応するパスワードを入力します。
3. `ユーザー名:パスワード` を API Host に含めないでください。

ユーザー名が空でなければ、Cherry Studio は `/config`、`/search`、検出リクエストへ Basic Auth ヘッダーを送信します。

インターネット経由では、HTTP Basic Auth を必ず HTTPS と組み合わせてください。HTTPS なしで Basic Auth だけを使用すると、転送中に認証情報を盗まれる可能性があります。

### 4. 接続を確認

**確認**ボタンをクリックします。

確認に成功したら、SearXNG をデフォルトのキーワード検索プロバイダーに設定します。その後、チャットで地球アイコンを有効にすると使用できます。

## Cherry Studio の検索エンジン選択

個別のエンジン一覧を保存していない場合、Cherry Studio は次を読み取ります。

```text
GET /config
```

そして、次のすべてを満たすエンジンを選択します。

- `enabled` が `true`
- `categories` に `general` が含まれる
- `categories` に `web` が含まれる

続いて、次のようなリクエストを送信します。

```text
GET /search?q=クエリ&language=auto&format=json&engines=エンジン一覧
```

そのため、SearXNG の Web 画面で一時的な検索設定を変更しても、Cherry Studio のリクエストが変わるとは限りません。適切なエンジンとカテゴリーは、インスタンスの `settings.yml` で継続的に有効にしてください。

### 指定したエンジンだけを残す

現在のネットワークから一部の上流エンジンへアクセスできない場合は、`settings.yml` でエンジンを調整できます。設定例：

```yaml
use_default_settings:
  engines:
    keep_only:
      - duckduckgo
      - wikipedia
```

エンジン名、可用性、設定項目は SearXNG の更新によって変わります。インスタンスの `/config` または設定画面で正確な名前を確認し、[エンジン設定ドキュメント](https://docs.searxng.org/admin/settings/settings_engines.html)を参照してください。

{% hint style="warning" %}
自分のネットワークに適さない固定のエンジン一覧をそのままコピーしないでください。検索エンジンはリージョンによるアクセス制限、CAPTCHA、インターフェース変更が発生する場合があります。インスタンスのログと実際の検索結果を基準にしてください。
{% endhint %}

## 検索結果と Web ページの読み取り

SearXNG がタイトル、要約、URL を返した後、Cherry Studio は結果ページの本文を読み取り、読み取りに成功した内容だけを保持します。

つまり：

- 最大結果数によって、アプリが処理する候補 URL 数が制限される
- ログインが必要、自動アクセスを拒否、または現在のネットワークから到達できない Web ページは読み取りに失敗する場合がある
- すべての候補 Web ページの読み取りに失敗した場合、検索がエラーになるか、利用可能な結果がない場合がある
- SearXNG はキーワード検索プロバイダーの設定であり、単独で貼り付けた URL に使用するデフォルト URL 読み取りプロバイダーは Web 検索設定で別に選択する必要がある

## インターネット公開時のセキュリティ

保護されていない SearXNG の管理および検索インターフェースを、インターネットへ直接公開しないでください。

少なくとも次を検討してください。

- 信頼できる証明書で HTTPS を有効にする
- リバースプロキシ層でアクセス認証を設定する
- 適切なレート制限とボット対策を維持する
- 管理ポートと不要なネットワーク入口を制限する
- SearXNG、コンテナイメージ、リバースプロキシを定期的に更新する
- 機密性の高いクエリをアクセスログに長期間保存しない
- 信頼できるユーザーだけに認証情報を提供し、定期的にローテーションする

現在の Cherry Studio は HTTP Basic Auth に対応していますが、サーバー側の TLS、権限、レート制限は設定しません。

## よくある問題

### 確認で 403 が返される

最も一般的な原因は JSON 出力が有効になっていないことです。`settings.yml` に次が含まれていることを確認します。

```yaml
search:
  formats:
    - html
    - json
```

保存してインスタンスを再起動し、`/search?q=test&format=json` へ直接アクセスして確認します。

公開インスタンスが JSON API を無効にしている場合もあります。この場合は別のインスタンスへ変更するか、自分でデプロイしてください。

### 確認で 401 が返される

インスタンスまたはリバースプロキシが認証を要求しています。

- Cherry Studio に正しい Basic Auth のユーザー名とパスワードを入力する
- リバースプロキシが `/config` と `/search` を同じ認証情報で保護していることを確認する
- ユーザー名とパスワードに誤ってコピーした空白がないか確認する
- 認証情報を URL に含めない

### 利用可能な general/web エンジンがないと表示される

Cherry Studio は、`/config` から `general` と `web` の両方に属する有効なエンジンを見つけられていません。

確認項目：

1. `/config` が `engines` を正しく返すか
2. 対象エンジンが `enabled: true` か
3. `categories` に `general` と `web` の両方が含まれるか
4. 設定変更後にインスタンスを再起動または再読み込みしたか

### 検索がタイムアウトする、または結果が不安定

SearXNG のログで、特に次を確認してください。

- 上流の検索エンジンが 403、429、CAPTCHA を返していないか
- DNS、プロキシ、サーバーの送信ネットワークが正常か
- インスタンスのリクエストタイムアウトが短すぎないか
- 選択したエンジンが現在のリージョンに適しているか
- Cherry Studio を実行する機器から検索結果の Web ページを開けるか

すべてのレート制限とセキュリティ保護を直接無効にしないでください。まず、制限が SearXNG、リバースプロキシ、上流エンジン、ローカルネットワークのどこで発生しているかを判断します。

### ブラウザーでは検索できるが Cherry Studio では失敗する

ブラウザー画面ではデフォルトで HTML を使用しますが、Cherry Studio には JSON が必要です。次を個別にテストします。

```text
/config
/search?q=test&format=json
```

また、API Host にルートアドレスだけが入力されていること、Basic Auth が正しいこと、リバースプロキシがこの 2 つのパスだけを遮断していないことも確認してください。

### 結果は返るが回答に引用がない

結果ページ本文の読み取りに失敗したか、モデルが検索結果を正しく使用していない可能性があります。次を試せます。

- アクセス不能またはログインが必要な検索エンジンを減らす
- 最大結果数を増やして再試行する
- 現在のネットワークに適したエンジンへ変更する
- 質問で情報源を列挙するよう明示する
- モデルがツール呼び出しに対応しているか確認する

## 更新と保守

サービスを更新する前に、SearXNG の移行手順を読み、`.env` と `core-config` をバックアップしてください。コンテナデプロイでは通常、公式テンプレートの更新と新しいイメージの取得が必要です。古い Compose ファイルが常に互換であるとは限りません。

公式資料：

- [SearXNG コンテナインストール](https://docs.searxng.org/admin/installation-docker.html)
- [SearXNG `settings.yml`](https://docs.searxng.org/admin/settings/settings.html)
- [検索出力形式](https://docs.searxng.org/admin/settings/settings_search.html)
- [管理 API `/config`](https://docs.searxng.org/admin/api.html)
- [SearXNG GitHub](https://github.com/searxng/searxng)

## 関連ドキュメント

- [Web 検索](README.md)
- [無料 Web 検索モード](./mian-fei-lian-wang-mo-shi.md)
- [Web 検索ブラックリスト](blacklist.md)

***

### ヘルプとフィードバック

設定または使用中に問題が発生した場合は、[フィードバックと提案](../question-contact/suggestions.md)に記載された公式窓口から報告してください。Cherry Studio のバージョン、SearXNG のバージョン、エラーコード、機密情報を除いたログを添付し、実際のドメイン認証情報や認証パスワードは送信しないでください。
