---
description: 部署可供 Cherry Studio V2 使用的 SearXNG 執行個體，並完成 JSON、搜尋引擎和基本驗證設定。
icon: searchengin
---

# SearXNG 本機部署與設定

SearXNG 是開放原始碼的元搜尋引擎，可以將多個搜尋引擎的結果彙整到自己的執行個體中。Cherry Studio V2 可將自架的 SearXNG 設為關鍵字搜尋供應商，適合重視可控性和隱私，並具備基本容器維運能力的使用者。

{% hint style="info" %}
SearXNG 軟體本身是開放原始碼，但執行個體運作仍會占用本機或伺服器資源；它呼叫的上游搜尋引擎也可能有各自的存取限制。自架不代表搜尋品質、可用性或匿名性會自動獲得保障。
{% endhint %}

## 選擇 SearXNG 前先了解

與直接填寫 API Key 的搜尋服務不同，使用 SearXNG 需要先準備一個可存取的執行個體。

| 方案 | 適用情境 | 注意事項 |
| --- | --- | --- |
| 本機部署 | 個人使用、快速體驗 | 只有本機可以直接存取，電腦關機後服務會停止 |
| 區域網路部署 | 多台可信裝置共用 | 需要正確設定監聽位址和防火牆 |
| 公網自架 | 跨網路或團隊使用 | 必須考慮 HTTPS、驗證、速率限制、更新和記錄 |
| 公用執行個體 | 暫時測試 | 可能關閉 JSON API、限制頻率或隨時無法使用 |

不建議將陌生的公用執行個體作為長期預設供應商。執行個體管理員可能看到查詢和連線資訊，而且公用執行個體通常無法提供穩定性承諾。

## Cherry Studio 對執行個體的要求

可用的 SearXNG 執行個體需要符合：

- Cherry Studio 所在裝置能夠存取執行個體位址；
- `/config` 能傳回執行個體設定；
- `/search` 允許 `format=json`；
- 至少有一個已啟用的搜尋引擎同時屬於 `general` 和 `web` 類別；
- 搜尋結果中的網頁可從 Cherry Studio 所在網路存取；
- 如果反向代理啟用了 HTTP Basic Auth，需要在 Cherry Studio 中填寫相同憑證。

Cherry Studio 預設使用：

```text
http://localhost:8080
```

這只是預設位址。實際連接埠和網域必須與自己的部署一致。

## 使用官方容器範本部署

SearXNG 官方建議使用 Docker 或 Podman 的 Compose 範本。以下步驟適合已安裝 Docker 與 Docker Compose 的使用者；正式環境還需要自行完成備份、更新和存取控制。

### 1. 準備目錄和範本

```bash
mkdir -p ./searxng/core-config
cd ./searxng
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example
cp .env.example .env
```

開啟 `.env`，依範本說明檢查連接埠、執行個體位址和密鑰等設定。範本可能隨 SearXNG 更新，首次部署或升級前應閱讀[官方容器安裝文件](https://docs.searxng.org/admin/installation-docker.html)。

### 2. 開啟 JSON 輸出

在 `core-config/settings.yml` 中至少加入：

```yaml
use_default_settings: true

search:
  formats:
    - html
    - json
```

{% hint style="warning" %}
Cherry Studio 會請求 `format=json`。如果 SearXNG 的 `search.formats` 沒有 `json`，搜尋介面通常會傳回 `403 Forbidden`。
{% endhint %}

如果已有 `settings.yml`，請合併 `json` 項目，不要使用上述最小範例覆寫原有的引擎、代理、語言或安全設定。

### 3. 啟動執行個體

```bash
docker compose up -d
docker compose ps
```

如需查看記錄：

```bash
docker compose logs -f core
```

服務名稱可能隨官方範本調整。如果記錄命令提示找不到 `core`，請先執行 `docker compose ps`，再使用實際的服務名稱。

### 4. 驗證執行個體

先在瀏覽器中開啟執行個體首頁，再透過終端機驗證 JSON API。假設位址是 `http://127.0.0.1:8080`：

```bash
curl "http://127.0.0.1:8080/config"
curl "http://127.0.0.1:8080/search?q=Cherry+Studio&format=json"
```

兩個請求都應傳回 JSON。第二個回應還應包含可用的搜尋結果。

SearXNG 的介面和參數說明請參閱 [Search API](https://docs.searxng.org/dev/search_api.html)。

## 在 Cherry Studio 中設定

### 1. 開啟 SearXNG 設定

進入：

> **設定 → 網路搜尋 → SearXNG**

### 2. 填寫 API Host

填寫執行個體的根位址，不要手動附加 `/search` 或 `/config`。

本機範例：

```text
http://127.0.0.1:8080
```

公網範例：

```text
https://search.example.com
```

Cherry Studio 會自行串接 `/config` 和 `/search`。

{% hint style="info" %}
桌面版 Cherry Studio 直接在主機系統中執行。Docker 已將連接埠對應到主機時，通常使用 `127.0.0.1:對應連接埠`，不需要使用 `host.docker.internal`。
{% endhint %}

### 3. 填寫基本驗證

如果反向代理設定了 HTTP Basic Auth：

1. 在 SearXNG 設定中填寫使用者名稱；
2. 填寫對應的密碼；
3. 不要將 `使用者名稱:密碼` 寫入 API Host。

只要使用者名稱非空，Cherry Studio 就會對 `/config`、`/search` 和檢查請求傳送 Basic Auth 請求標頭。

HTTP Basic Auth 必須與 HTTPS 搭配用於公網連線。只使用 Basic Auth 而不使用 HTTPS，憑證可能在傳輸過程中被竊取。

### 4. 檢查連線

點選**檢查**按鈕。

檢查成功後，將 SearXNG 設為預設關鍵字搜尋供應商。接著在對話中開啟地球圖示即可使用。

## Cherry Studio 如何選擇搜尋引擎

如果未儲存過個別的引擎清單，Cherry Studio 會讀取：

```text
GET /config
```

並選擇同時符合以下條件的引擎：

- `enabled` 為 `true`；
- `categories` 包含 `general`；
- `categories` 包含 `web`。

接著，應用程式會發出類似的請求：

```text
GET /search?q=查詢內容&language=auto&format=json&engines=引擎清單
```

因此，在 SearXNG 網頁端變更一次性的搜尋偏好，不一定會改變 Cherry Studio 的請求。應在執行個體的 `settings.yml` 中長期啟用合適的引擎和類別。

### 只保留指定引擎

如果某些上游引擎在目前網路中無法存取，可以在 `settings.yml` 中調整引擎。設定範例：

```yaml
use_default_settings:
  engines:
    keep_only:
      - duckduckgo
      - wikipedia
```

引擎名稱、可用性和設定項目會隨 SearXNG 更新。請先在執行個體的 `/config` 或偏好設定中確認正確名稱，並參閱[引擎設定文件](https://docs.searxng.org/admin/settings/settings_engines.html)。

{% hint style="warning" %}
不要直接照搬不適合自己網路的固定引擎清單。搜尋引擎可能依地區限制存取、觸發驗證碼或變更介面，最終結果應以執行個體記錄和實際搜尋為準。
{% endhint %}

## 搜尋結果與網頁讀取

SearXNG 傳回標題、摘要和 URL 後，Cherry Studio 會嘗試讀取結果網頁正文，並只保留成功讀取的內容。

這表示：

- 最大結果數會限制應用程式處理的候選 URL 數量；
- 某些網頁需要登入、阻止自動存取或在目前網路無法連線時，讀取可能失敗；
- 如果所有候選網頁都讀取失敗，本次搜尋可能報錯或沒有可用結果；
- SearXNG 設定仍屬於關鍵字搜尋供應商；單獨貼上 URL 時使用的預設 URL 讀取供應商，仍需在網路搜尋設定中另外選擇。

## 公網部署的安全建議

不要將未受保護的 SearXNG 管理和搜尋介面直接暴露到公網。

至少應考慮：

- 使用可信憑證啟用 HTTPS；
- 在反向代理層設定存取驗證；
- 保留合理的速率限制和機器人防護；
- 限制管理連接埠和不必要的網路入口；
- 定期更新 SearXNG、容器映像和反向代理；
- 避免在存取記錄中長期保留敏感查詢；
- 只向可信使用者提供憑證，並定期輪替。

Cherry Studio 目前支援 HTTP Basic Auth，但不會替您完成伺服器端的 TLS、權限和速率限制設定。

## 常見問題

### 檢查傳回 403

最常見的原因是未開啟 JSON 輸出。確認 `settings.yml` 包含：

```yaml
search:
  formats:
    - html
    - json
```

儲存後重新啟動執行個體，再直接存取 `/search?q=test&format=json` 驗證。

公用執行個體也可能主動關閉 JSON API，此時只能更換執行個體或自行部署。

### 檢查傳回 401

執行個體或反向代理要求驗證：

- 在 Cherry Studio 中填寫正確的 Basic Auth 使用者名稱和密碼；
- 確認反向代理保護 `/config` 和 `/search` 時使用相同憑證；
- 檢查使用者名稱、密碼是否包含誤複製的空格；
- 不要將憑證串接到 URL 中。

### 提示沒有可用的 general/web 引擎

Cherry Studio 未從 `/config` 中找到同時屬於 `general` 與 `web` 的已啟用引擎。

檢查：

1. `/config` 是否正常傳回 `engines`；
2. 目標引擎是否為 `enabled: true`；
3. `categories` 是否同時包含 `general` 和 `web`；
4. 修改設定後是否已重新啟動或重新載入執行個體。

### 搜尋逾時或結果不穩定

查看 SearXNG 記錄，重點檢查：

- 上游搜尋引擎是否傳回 403、429 或驗證碼；
- DNS、代理和伺服器出口網路是否正常；
- 執行個體的請求逾時是否過短；
- 所選引擎是否適合目前地區；
- Cherry Studio 所在裝置是否能開啟搜尋結果網頁。

不要直接關閉所有速率限制和安全防護。先判斷限制發生在 SearXNG、反向代理、上游引擎或本機網路。

### 瀏覽器能搜尋，Cherry Studio 仍然失敗

瀏覽器頁面預設使用 HTML，而 Cherry Studio 要求 JSON。請分別測試：

```text
/config
/search?q=test&format=json
```

還需要確認 API Host 只填寫根位址、Basic Auth 正確，而且反向代理未個別攔截這兩個路徑。

### 傳回結果，但回答沒有引用

可能是結果頁面正文讀取失敗，或模型未正確使用搜尋結果。可以：

- 減少無法存取或需要登入的搜尋引擎；
- 提高最大結果數後重試；
- 更換更適合目前網路的引擎；
- 在問題中明確要求列出來源；
- 檢查模型是否支援工具呼叫。

## 更新與維護

更新服務前，先閱讀 SearXNG 的遷移說明並備份 `.env` 與 `core-config`。使用容器部署時，通常需要更新官方範本並拉取新映像；不要假定舊版 Compose 檔案永遠相容。

官方資料：

- [SearXNG 容器安裝](https://docs.searxng.org/admin/installation-docker.html)
- [SearXNG `settings.yml`](https://docs.searxng.org/admin/settings/settings.html)
- [搜尋輸出格式](https://docs.searxng.org/admin/settings/settings_search.html)
- [管理 API `/config`](https://docs.searxng.org/admin/api.html)
- [SearXNG GitHub](https://github.com/searxng/searxng)

## 相關文件

- [網路搜尋](README.md)
- [免費聯網模式](mian-fei-lian-wang-mo-shi.md)
- [網路搜尋黑名單](blacklist.md)

***

### 取得協助與提交意見

如果在設定或使用過程中遇到問題，請透過[意見回饋](../question-contact/suggestions.md)中列出的官方管道提交意見。請附上 Cherry Studio 版本、SearXNG 版本、錯誤碼和經過遮蔽處理的記錄，但不要提交真實網域憑證或驗證密碼。
