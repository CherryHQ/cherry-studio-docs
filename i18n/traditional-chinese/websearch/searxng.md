---
icon: searchengin
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# SearXNG 部署與配置

CherryStudio 支援透過 SearXNG 進行網路搜尋，SearXNG 是可本地部署或在伺服器上部署的開源項目，因此與其他需要 API 提供商的配置方式略有不同。

**SearXNG 專案連結**：[SearXNG](https://github.com/searxng/searxng)

## SearXNG 的優勢

* 開源免費，無需 API
* 隱私性相對較高
* 可高度自訂化

## 本地部署

### 一、Docker 直接部署

由於 SearXNG 不需要複雜的環境配置，可以不使用 docker compose，僅需提供閒置連接埠即可部署，因此最快捷方式是直接透過 Docker 拉取鏡像部署。

#### 1. 下載安裝並配置 [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

安裝後選擇鏡像儲存路徑：

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. 搜尋並拉取 SearXNG 鏡像

搜尋欄輸入 **searxng**：

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

拉取鏡像：

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. 執行鏡像

拉取成功後至 **images** 頁面：

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

選擇鏡像點選執行：

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

開啟設定項配置：

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

以 `8085` 連接埠為例：

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

執行成功後點選連結開啟 SearXNG 前端介面：

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

出現此頁面表示部署成功：

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## 伺服器部署

鑑於 Windows 下安裝 Docker 較為繁瑣，使用者可將 SearXNG 部署在伺服器上，亦可共享給他人使用。但 SearXNG 目前不支援鑑權機制，可能導致他人透過技術手段掃描並濫用您部署的實例。

為此，Cherry Studio 現已支援配置 [HTTP 基本認證（RFC7617）](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Authentication)，若需將部署的 SearXNG 暴露於公網環境，請**務必**透過 Nginx 等反向代理軟體配置 HTTP 基本認證。以下提供簡要教學，需具備基礎 Linux 運維知識。

### 部署 SearXNG

類似本地部署，使用 Docker 部署。假設已按[官方教學](https://docs.docker.com/engine/install)在伺服器安裝最新版 Docker CE，以下提供適用於 Debian 系統的全套指令：

```bash
sudo apt update
sudo apt install git -y

# 拉取官方儲存庫
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# 若伺服器頻寬較小可設為 false
export IMAGE_PROXY=true

# 修改設定檔
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

如需修改本地監聽連接埠或復用現有 Nginx，可編輯 `docker-compose.yaml` 檔案，參照如下：

```yaml
version: "3.7"

services:
# 若不需要 Caddy 且復用現有 Nginx，請移除此段落
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
# 若不需要 Caddy 且復用現有 Nginx，請移除此段落
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
    # 預設對應宿主機 8080 連接埠，若要監聽 8000 請改為 "127.0.0.1:8000:8080"
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
# 若不需要 Caddy 且復用現有 Nginx，請移除此段落
  caddy-data:
  caddy-config:
# 若不需要 Caddy 且復用現有 Nginx，請移除此段落
  valkey-data2:
```

執行 `docker compose up -d` 啟動。執行 `docker compose logs -f searxng` 可檢視日誌。

### 部署 Nginx 反向代理與 HTTP 基本認證

若使用伺服器面板程式（如寶塔面板或 1Panel），請參閱文件新增網站並配置 Nginx 反向代理，隨後修改 Nginx 設定檔：
```conf
server
{
    listen 443 ssl;

    # 此行為您的主機名稱
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # 若已配置 SSL 應有下列兩行
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # 預設反向代理配置，保留原始 location 區塊
    location / {
        # 只需在 location 區塊新增下列兩行
        # 此範例假設備份檔儲存於 /etc/nginx/conf.d/
        # 寶塔面板可能儲存在 /www 等路徑，請注意
        auth_basic "請輸入使用者名稱與密碼";
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

假設 Nginx 設定檔儲存於 `/etc/nginx/conf.d`，將密碼檔存放於同目錄。

執行指令（自行替換 `example_name` 與 `example_password` 為實際帳密）：
```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

重啟 Nginx（或重新載入設定）。

開啟網頁時將提示輸入帳密，使用設定的帳密登入以驗證配置。

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio 相關配置

SearXNG 成功部署於本地或伺服器後，進入 CherryStudio 配置階段。

至網路搜尋設定頁面，選擇 Searxng：

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

輸入本地部署連結可能驗證失敗（正常現象）：

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

因預設未配置 JSON 回傳類型，需修改設定檔。

回到 Docker，於 Files 標籤頁尋找帶標籤的資料夾：

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

展開後繼續向下瀏覽，找到另一個帶標籤資料夾：

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

展開後尋找 **settings.yml** 設定檔：

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

開啟檔案編輯器：

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

找到第 78 行，目前類型僅有 html：

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

新增 json 類型後儲存，重新執行鏡像：

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

返回 Cherry Studio 重新驗證，驗證成功：

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

地址可填寫：
- 本地： <http://localhost> :連接埠號
- Docker 地址：<http://host.docker.internal> :連接埠號

若已在伺服器部署並配置反向代理，且開啟 json 回傳類型。輸入地址後因 HTTP 基本認證，驗證將返回 401 錯誤：

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

於用戶端配置 HTTP 基本認證，輸入設定的帳密：

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

再次驗證應成功通過。

### 其他配置

此時 SearXNG 已具備預設搜尋能力，如需客製化搜尋引擎需另行配置。

需注意此處首選項不影響大模型呼叫配置：

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

配置大模型呼叫的搜尋引擎需於設定檔設定：

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

配置語言參考：

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

若內容過長修改不便，可複製至本地 IDE 修改後貼回。

## 驗證失敗常見原因

### 未新增 JSON 回傳格式

於設定檔新增 json 格式：

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### 未正確配置搜尋引擎

Cherry Studio 預設選取 categories 同時包含 web general 的引擎，若無法存取 Google 等網站（如中國大陸地區）會導致失敗。新增下列配置強制使用 Baidu 引擎即可：
```yaml
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

### 存取速率過快

searxng 的 limiter 配置阻擋 API 存取，請於設定中設為 false：

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>