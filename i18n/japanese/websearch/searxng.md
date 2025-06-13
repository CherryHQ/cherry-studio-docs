---
icon: searchengin
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# SearXNGのデプロイと設定

CherryStudioはSearXNGによるウェブ検索をサポートしています。SearXNGはローカルでもサーバーでもデプロイできるオープンソースプロジェクトであり、APIプロバイダーを必要とする他の設定方法とは異なります。

**SearXNGプロジェクトリンク**: [SearXNG](https://github.com/searxng/searxng)

## SearXNGの利点

* オープンソースで無料、API不要
* 比較的高いプライバシー性
* 高度なカスタマイズが可能

## ローカルデプロイ

### 一、Docker直接デプロイ

SearXNGは複雑な環境設定を必要としないため、docker composeを使用せずに単純に空きポートを提供するだけでデプロイできます。最も迅速な方法はDockerで直接イメージを取得してデプロイすることです。

#### 1. [Docker](https://www.docker.com/)のダウンロードとインストール、設定

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

インストール後、イメージ保存パスを選択:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. SearXNGイメージの検索と取得

検索バーに **searxng** と入力:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

イメージの取得:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. イメージの実行

取得後に **images** ページへ:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

取得したイメージを選択して実行:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

設定項目を開いて設定:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

例としてポート `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

実行成功後、リンクをクリックしてSearXNGフロントエンドインターフェースを開く:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

このページが表示されればデプロイ成功:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## サーバーデプロイ

WindowsでのDockerインストールが面倒な場合、ユーザーはサーバーにSearXNGをデプロイすることも可能で、これにより他の人と共有できます。ただし残念ながら、SearXNG自体はまだ認証をサポートしておらず、技術的手段でスキャンされ悪用される可能性があります。

このため、Cherry Studioは現在[HTTP基本認証（RFC7617）](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication)の設定をサポートしています。SearXNGをパブリックネットワーク環境に公開する場合は、NginxなどのリバースプロキシソフトウェアでHTTP基本認証を設定してください。以下に簡単なチュートリアルを提供しますが、基本的なLinux運用知識が必要です。

### SearXNGのデプロイ

同様に、Dockerを使ってデプロイします。サーバーに最新版Docker CEがインストール済みと仮定（[公式チュートリアル](https://docs.docker.com/engine/install)参照）。Debianシステムでの新規インストール用コマンド:

```bash
sudo apt update
sudo apt install git -y

# 公式リポジトリのクローン
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# サーバーバンド幅が小さい場合はfalseに設定可能
export IMAGE_PROXY=true

# 設定ファイルの変更
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# see https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url is defined in the SEARXNG_BASE_URL environment variable, see .env and docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # can be disabled for a private instance
  image_proxy: $IMAGE_PROXY
ui:
  static_use_hash: true
redis:
  url: redis://redis:6379/0
search:
  formats:
    - html
    - json
EOF
```

ローカルリスンポートの変更や既存nginxの再利用が必要な場合は、`docker-compose.yaml`ファイルを編集:

```yaml
version: "3.7"

services:
# 既存のNginxを再利用する場合は以下を削除
  caddy:
    container_name: caddy
    image: docker.io/library/caddy:2-alpine
    network_mode: host
    restart: unless-stopped
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy-data:/data:rw
      - caddy-config:/config:rw
    environment:
      - SEARXNG_HOSTNAME=${SEARXNG_HOSTNAME:-http://localhost}
      - SEARXNG_TLS=${LETSENCRYPT_EMAIL:-internal}
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"
# 既存のNginxを再利用する場合は以上を削除
  redis:
    container_name: redis
    image: docker.io/valkey/valkey:8-alpine
    command: valkey-server --save 30 1 --loglevel warning
    restart: unless-stopped
    networks:
      - searxng
    volumes:
      - valkey-data2:/data
    cap_drop:
      - ALL
    cap_add:
      - SETGID
      - SETUID
      - DAC_OVERRIDE
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

  searxng:
    container_name: searxng
    image: docker.io/searxng/searxng:latest
    restart: unless-stopped
    networks:
      - searxng
    # デフォルトはホスト8080ポート、8000でリッスンする場合は"127.0.0.1:8000:8080"に変更
    ports:
      - "127.0.0.1:8080:8080"
    volumes:
      - ./searxng:/etc/searxng:rw
    environment:
      - SEARXNG_BASE_URL=https://${SEARXNG_HOSTNAME:-localhost}/
      - UWSGI_WORKERS=${SEARXNG_UWSGI_WORKERS:-4}
      - UWSGI_THREADS=${SEARXNG_UWSGI_THREADS:-4}
    cap_drop:
      - ALL
    cap_add:
      - CHOWN
      - SETGID
      - SETUID
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

networks:
  searxng:

volumes:
# 既存のNginxを再利用する場合は以下を削除
  caddy-data:
  caddy-config:
# 既存のNginxを再利用する場合は以上を削除
  valkey-data2:
```

`docker compose up -d` で起動。`docker compose logs -f searxng` でログ確認。

### NginxリバースプロキシとHTTP基本認証のデプロイ

宝塔パネルや1Panelなどのサーバーパネルを使用している場合は、ドキュメントを参照してサイトを追加しnginxリバースプロキシを設定し、nginx設定ファイルを以下の例を参考に変更:

```conf
server
{
    listen 443 ssl;

    # ホスト名
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL設定時には以下2行が必要
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # デフォルトのリバースプロキシ設定
    location / {
        # locationブロックに以下2行を追加
        # 設定ファイルが/etc/nginx/conf.d/にあると仮定
        auth_basic "ユーザー名とパスワードを入力してください";
        auth_basic_user_file /etc/nginx/conf.d/search.htpasswd;

        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_protocol_addr;
        proxy_pass http://127.0.0.1:8000;
        client_max_body_size 0;
    }

    # access_log  ...;
    # error_log  ...;
}
```

Nginx設定ファイルが`/etc/nginx/conf.d`にあると仮定し、パスワードファイルも同ディレクトリに保存。

以下コマンド実行（`example_name`、`example_password`を設定するユーザー名とパスワードに置換）:

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Nginx再起動（設定再読み込みでも可）。

これでWebページを開くとユーザー名とパスワードが要求されます。設定した認証情報を入力してSearXNG検索ページにアクセスできるか確認してください。

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio関連設定

SearXNGのローカルまたはサーバーデプロイが成功したら、CherryStudioの関連設定を行います。

ネットワーク検索設定ページでSearxngを選択:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

ローカルデプロイのリンクを入力すると認証失敗と表示されますが問題ありません:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

デプロイ直後はデフォルトでjson返却形式が設定されていないため、設定ファイルの変更が必要です。

DockerのFilesタブでタグ付きフォルダを検索:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

展開後、別のタグ付きフォルダを検索:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

**settings.yml**設定ファイルを発見:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

ファイルエディターで開く:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

78行目を見つけ、タイプがhtmlのみ:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

jsonタイプを追加して保存後、イメージを再実行:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Cherry Studioで再認証、成功:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

アドレスはローカル: <http://localhost> : ポート番号 または dockerアドレス: <http://host.docker.internal> : ポート番号 を入力。

サーバーにデプロイしてリバースプロキシを設定しjson返却形式を有効にしている場合、HTTP基本認証を設定しているので認証時には401エラーが返されます:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

クライアントでHTTP基本認証を設定、設定したユーザー名とパスワードを入力:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

認証を実行、成功するはずです。

### その他の設定

SearXNGはデフォルトでネットワーク検索能力を持っていますが、検索エンジンのカスタマイズが必要な場合は個別に設定してください。

ここでの設定は大規模モデルの呼び出し時の設定には影響しないことに注意:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

大規模モデルで使用する検索エンジンの設定は、設定ファイルで行います:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

言語設定のリファレンス:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

内容が長すぎて直接編集が不便な場合は、ローカルのIDEにコピーして編集後、設定ファイルに貼り付けてください。

## 認証失敗の一般的な原因

### json形式が返却形式に追加されていない

設定ファイルで返却形式にjsonを追加:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### 検索エンジンが正しく設定されていない

Cherry Studioはデフォルトでwebとgeneralの両方のカテゴリを含むエンジンを選択します。デフォルトではgoogleなどが選択されますが、中国本土では直接アクセスできないため失敗します。以下の設定を追加してsearxngがbaiduエンジンを強制的に使用するようにすれば問題解決:

```
use_default_settings:
  engines:
    keep_only:
      - baidu
engines:
  - name: baidu
    engine: baidu 
    categories: 
      - web
      - general
    disabled: false
```

### アクセス速度が速すぎる

searxngのlimiter設定がAPIアクセスを妨げているため、設定でfalseに設定してみてください:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>