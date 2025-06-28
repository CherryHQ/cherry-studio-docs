---
icon: searchengin
---

# SearXNG セルフホスティング設定

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

## SearXNG のデプロイと設定

CherryStudio は SearXNG を介したウェブ検索をサポートしています。SearXNG はローカル環境またはサーバーにデプロイ可能なオープンソースプロジェクトであるため、APIプロバイダーを必要とする他の設定方法とは異なります。

**SearXNG プロジェクトリンク**: [SearXNG](https://github.com/searxng/searxng)

### SearXNG の利点

* オープンソースで無料、API不要
* 比較的高いプライバシー性
* 高度なカスタマイズが可能

### ローカルデプロイ

#### 一、Docker を使用した直接デプロイ

SearXNG は複雑な環境設定を必要としないため、docker compose を使用せずに空いているポートを提供するだけでデプロイできます。最も迅速な方法は Docker を使用して直接イメージをプルしデプロイすることです。

**1.** [**docker**](https://www.docker.com/) **のダウンロードとインストール**

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

インストール後にイメージ保存パスを選択:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

**2. SearXNG イメージの検索とプル**

検索バーに **searxng** と入力:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

イメージをプル:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

**3. イメージの実行**

プル後、**images** ページに移動:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

プルしたイメージを選択して実行:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

設定を開いて構成:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

`8085` ポートを例に:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

実行成功後にリンクをクリックすると SearXNG のフロントエンドインターフェースが開きます:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

このページが表示されればデプロイ成功:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

### サーバーデプロイ

Windows に Docker をインストールするのは面倒なため、ユーザーは SearXNG をサーバーにデプロイし、他の人と共有することも可能です。ただし、残念ながら SearXNG 自体は現在認証をサポートしていないため、技術的手段であなたがデプロイしたインスタンスをスキャンして悪用される可能性があります。

このため、Cherry Studio は現在 [HTTP基本認証（RFC7617）](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication) の設定をサポートしています。デプロイした SearXNG を公網環境に公開する場合は、**必ず** Nginx などのリバースプロキシソフトウェアで HTTP基本認証を設定してください。基本的な Linux 運用知識が必要ですが、以下に簡単なチュートリアルを提供します。

#### SearXNG のデプロイ

同様に、Docker を使用してデプロイします。サーバーに最新の Docker CE を[公式チュートリアル](https://docs.docker.com/engine/install)に従ってインストール済みと仮定し、Debian システムでの新規インストール向けのワンステップコマンドを提供します:

```bash
sudo apt update
sudo apt install git -y

# 公式リポジトリをクローン
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# サーバーの帯域幅が小さい場合は false に設定可能
export IMAGE_PROXY=true

# 設定ファイルを編集
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

ローカルリスニングポートの変更や既存の nginx の再利用が必要な場合は、`docker-compose.yaml` ファイルを編集してください。参考例:

```yaml
version: "3.7"

services:
# Caddy が必要なく、既存の Nginx を再利用する場合は以下を削除
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
# Caddy が必要なく、既存の Nginx を再利用する場合は以上を削除
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
    # ホストの8080ポートにマッピング。8000ポートをリスンしたい場合は "127.0.0.1:8000:8080" に変更
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
# Caddy が必要なく、既存の Nginx を再利用する場合は以下を削除
  caddy-data:
  caddy-config:
# Caddy が必要なく、既存の Nginx を再利用する場合は以上を削除
  valkey-data2:
```

`docker compose up -d` を実行して起動します。`docker compose logs -f searxng` でログを確認できます。

#### Nginx リバースプロキシと HTTP基本認証のデプロイ

宝塔パネルや1Panelなどのサーバーパネルを使用している場合は、ドキュメントを参照してサイトを追加し、nginxリバースプロキシを設定した後、nginx設定ファイルを修正してください。\
以下の例を参考に修正します:

```conf
server
{
    listen 443 ssl;

    # ホスト名
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL設定がある場合
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # パネルでリバースプロキシを設定すると、デフォルトでlocationブロックは以下のようになる
    location / {
        # locationブロックに以下の2行を追加し、他はそのままに
        # 設定ファイルが/etc/nginx/conf.d/に保存されていると仮定
        # 宝塔パネルの場合は/wwwなどのディレクトリに保存されるため注意
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

Nginx設定ファイルが`/etc/nginx/conf.d`に保存されていると仮定し、パスワードファイルを同じディレクトリに保存します。

コマンドを実行（`example_name`、`example_password`を設定するユーザー名とパスワードに置き換え）:

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Nginxを再起動（設定のリロードでも可）。

ウェブページを開くと、ユーザー名とパスワードの入力が求められます。設定したユーザー名とパスワードを入力して、SearXNG検索ページに正常にアクセスできるか確認してください。

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

### Cherry Studio の関連設定

SearXNGをローカルまたはサーバーにデプロイしたら、CherryStudioの関連設定を行います。

ネットワーク検索設定ページでSearxngを選択:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

ローカルデプロイのリンクを入力すると検証が失敗しますが、問題ありません:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

直接デプロイ後、デフォルトではjson戻り型が設定されていないため、データを取得できません。設定ファイルを修正する必要があります。

Dockerに戻り、Filesタブでタグ付きフォルダを探します:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

展開後、別のタグ付きフォルダを探します:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

さらに展開し、**settings.yml**設定ファイルを見つけます:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

ファイルエディターを開く:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

78行目を見ると、タイプがhtmlのみです:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

jsonタイプを追加して保存し、イメージを再実行:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Cherry Studioに戻って検証すると成功します:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

アドレスはローカル: [http://localhost](http://localhost):ポート番号\
またはDockerアドレス: [http://host.docker.internal](http://host.docker.internal):ポート番号 が使用可能です。

前述の例に従ってサーバーにデプロイし、リバースプロキシを正しく設定し、json戻り型を有効にしている場合、アドレスを入力して検証すると、HTTP基本認証が設定されているため401エラーコードが返されます:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

クライアント側でHTTP基本認証を設定し、設定したユーザー名とパスワードを入力します:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

検証を実行すると成功します。

#### その他の設定

これでSearXNGはデフォルトのネットワーク検索能力を備えています。検索エンジンのカスタマイズが必要な場合は各自設定してください。

ここでのプリファレンス設定は、大規模モデル呼び出し時の設定には影響しないことに注意してください。

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

大規模モデル呼び出し用の検索エンジンを設定するには、設定ファイルで設定する必要があります:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

設定言語のリファレンス:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

内容が長すぎて直接編集が不便な場合は、ローカルのIDEにコピーし、修正後に設定ファイルに貼り付けることができます。

### 検証失敗の一般的な原因

#### json形式が追加されていない

設定ファイルで戻り形式にjsonを追加します:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

#### 検索エンジンの設定が正しくない

Cherry Studio はデフォルトで categories に web general を含むエンジンを選択し、デフォルトでは google などのエンジンを選択します。大陸では google などのサイトに直接アクセスできないため失敗します。以下の設定を追加することで searxng が強制的に baidu エンジンを使用するようになり、問題が解決します:

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

#### アクセス速度が速すぎる

searxng の limiter 設定が API アクセスを妨げるため、設定で false に設定してください:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>
