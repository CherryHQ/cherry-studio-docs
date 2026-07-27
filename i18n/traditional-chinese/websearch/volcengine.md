---
description: 讓火山方舟模型使用 Cherry Studio 聯網工具
icon: globe-pointer
---

# 火山引擎模型聯網

Cherry Studio V2 可以讓火山方舟的對話模型使用外部網路搜尋。建議組合是：

```text
火山方舟模型
    + Cherry Studio 預設搜尋供應商
    + Cherry Studio 預設 URL 取得供應商
```

目前 V2 未將火山方舟 Web Search 註冊為獨立的網路搜尋供應商，也不會在內建 `doubao` 供應商中自動注入方舟的雲端 Web Search 工具。

{% hint style="warning" %}
舊教學中的「建立零程式碼應用程式 → 開通聯網外掛程式 → 將應用程式當作 OpenAI 模型接入」不是目前 V2 的建議路徑。介面、外掛程式和 API 已經變更，不應繼續照搬舊螢幕截圖與舊 API Host 寫法。
{% endhint %}

## 先區分兩套聯網能力

| 方式 | 由誰執行搜尋 | Cherry Studio V2 目前狀態 | 建議情境 |
| --- | --- | --- | --- |
| Cherry Studio 外部聯網 | ExaMCP、Tavily、SearXNG、博查等搜尋供應商 | 已支援 | 一般對話、希望統一管理搜尋服務 |
| 火山方舟雲端 Web Search | 火山方舟 Responses API 或應用程式外掛程式 | 沒有專用適配 | 已在方舟端開發應用程式，並願意自行驗證 API |

本文介紹第一種方式。它不要求在火山方舟建立「我的應用」，也不依賴舊版聯網外掛程式。

### Cherry Studio 外部聯網

目前模型未被識別為原生聯網模型時，Cherry Studio 會向模型提供：

- 搜尋關鍵字工具；
- 讀取 URL 工具。

模型透過 Function Calling 決定何時搜尋和讀取網頁。搜尋結果會傳回給模型，再由模型產生帶有引用的回答。

### 火山方舟雲端 Web Search

火山方舟官網提供 Responses API、Web Search、Knowledge Search、Remote MCP 等雲端工具。這些能力屬於方舟 API，不等同於 Cherry Studio 的網路搜尋設定。

目前內建 `doubao` 供應商預設使用：

```text
OpenAI Chat Completions
```

預設 API Host：

```text
https://ark.cn-beijing.volces.com/api/v3/
```

官網支援某項 Responses API 工具，不代表 Cherry Studio 已自動適配其請求欄位、事件串流和引用結果。

## 使用前準備

需要準備：

1. 火山引擎帳號；
2. 火山方舟 API Key；
3. 目前可用的 Model ID 或 Endpoint ID；
4. 支援 Function Calling 的對話模型；
5. 一個關鍵字搜尋供應商；
6. 一個 URL 取得供應商。

火山方舟基礎設定請參閱[火山引擎（方舟 / 豆包）](../pre-basic/providers/doubao.md)。

{% hint style="danger" %}
不要將火山方舟 API Key、搜尋服務 API Key 或帶有權杖的私人 URL 寫入聊天、螢幕截圖和公開文件。
{% endhint %}

## 設定火山方舟模型

### 1. 開通並複製模型識別碼

在火山方舟控制台：

1. 建立 API Key；
2. 開通準備使用的模型；
3. 複製目前的 Model ID；
4. 如果使用專用推論接入點，複製 `ep-...` 格式的 Endpoint ID；
5. 確認專案、地區、餘額和速率限制。

不要複製：

- 模型顯示名稱；
- 控制台頁面 URL；
- 舊應用程式的 Bot ID；
- 其他專案中的 Endpoint ID。

### 2. 在 Cherry Studio 啟用供應商

1. 開啟 `設定 → 模型服務`；
2. 將篩選切換為**全部服務商**；
3. 選擇 **Doubao / 豆包 / 火山引擎**；
4. 填寫方舟 API Key；
5. 保留預設 API Host；
6. 開啟供應商開關；
7. 手動新增目前的 Model ID 或 Endpoint ID；
8. 執行模型健康檢查。

先傳送一則一般文字訊息，確認對話可用，再設定聯網。

## 選擇適合聯網的模型

Cherry Studio 外部聯網應優先使用支援結構化 Function Calling 的模型。

目前 V2 會識別多種較新的 Doubao Seed 模型，例如符合以下系列命名的模型：

```text
doubao-seed-1.6...
doubao-seed-1.8...
doubao-seed-2.0...
doubao-seed-code...
```

具體 Model ID 會更新，應從火山方舟目前的模型頁面複製，不要照抄上述系列名稱作為完整 ID。

{% hint style="warning" %}
舊教學使用的 DeepSeek R1 在目前 V2 中被排除於結構化 Function Calling 模型之外，不適合作為 Cherry Studio 外部聯網的首選。即使一般對話可用，也可能不呼叫搜尋工具。
{% endhint %}

在模型管理中可以檢視或調整能力標記，但能力標記只影響用戶端判斷，不會讓模型獲得伺服器端原本不支援的 Function Calling。

## 設定網路搜尋

開啟：

```text
設定 → 網路搜尋
```

同時設定：

| 設定 | 作用 | 可選範例 |
| --- | --- | --- |
| 預設搜尋供應商 | 依關鍵字尋找網頁 | ExaMCP、Tavily、SearXNG、博查 |
| 預設 URL 取得供應商 | 讀取特定網頁正文 | Fetch、Jina |

這兩項缺一不可。

如果不想另外申請搜尋 API Key，可先使用：

```text
預設搜尋供應商：ExaMCP
預設 URL 取得供應商：Fetch
```

詳細說明：

- [聯網模式](README.md)
- [免費聯網模式](mian-fei-lian-wang-mo-shi.md)
- [SearXNG 設定](searxng.md)

## 在對話中啟用

1. 返回對話頁面；
2. 選擇已通過健康檢查的火山方舟模型；
3. 點選輸入框下方的**地球**圖示；
4. 確認圖示反白；
5. 傳送需要即時資料的問題。

測試問題：

```text
先聯網搜尋 Cherry Studio 最近一個正式版本，
只引用官方 GitHub Release，列出版本號、發布日期和主要變更。
```

檢查回答中是否：

- 實際呼叫了搜尋工具；
- 出現可開啟的引用；
- 引用來自指定的網站；
- 日期和版本號與原文一致；
- 未將舊知識當作即時結果。

## 聯網時發生了什麼

對於目前 V2 中沒有原生聯網適配的火山方舟模型，流程通常是：

1. 使用者開啟聯網並傳送問題；
2. Cherry Studio 將外部搜尋工具提供給模型；
3. 模型產生結構化工具呼叫；
4. Cherry Studio 呼叫預設搜尋供應商；
5. 模型依需要呼叫預設 URL 取得供應商；
6. 搜尋結果和網頁正文傳回給模型；
7. 模型產生最終回答與引用。

搜尋服務的 API Key 不會傳送給火山方舟模型，但搜尋結果正文會作為對話上下文傳送給火山方舟。

## 與舊版教學的差異

| 舊版做法 | 目前 V2 建議 |
| --- | --- |
| 建立零程式碼「我的應用」 | 直接使用方舟 Model ID 或 Endpoint ID |
| 在方舟應用程式中購買或啟用舊聯網外掛程式 | 在 Cherry Studio 設定外部搜尋供應商 |
| 新增自訂 OpenAI 供應商 | 優先使用內建 Doubao 供應商 |
| 將完整 `/chat/completions` 寫入 URL | 填寫 Base URL，由 V2 串接請求路徑 |
| 在 API Host 結尾新增 `#` | 不需要 |
| 將應用程式小字 ID 當作模型名稱 | 使用目前的 Model ID 或 Endpoint ID |
| 使用舊 DeepSeek R1 聯網範例 | 選擇支援 Function Calling 的目前模型 |

從舊設定遷移時，建議建立一個乾淨的 Doubao 供應商執行個體，或還原內建供應商預設值，不要在舊位址上繼續疊加相容參數。

## 不要手動標記「原生聯網」

模型詳細資料中的聯網能力標記會影響 Cherry Studio 選擇原生聯網或外部聯網。

不要為了顯示地球圖示，直接將一般火山方舟模型標記為原生聯網模型。目前 V2 沒有對應的方舟 Web Search 外掛程式適配，錯誤標記可能導致：

- Cherry Studio 不再注入外部搜尋工具；
- 方舟端又未收到正確的雲端 Web Search 工具；
- 聯網開關反白，但實際沒有搜尋。

如果誤改，請還原模型自動識別，再使用本頁的外部聯網設定。

## 如果必須使用方舟雲端 Web Search

火山方舟雲端 Web Search 主要透過 Responses API 或方舟應用程式設定。目前 Cherry Studio V2 內建 `doubao` 連線不提供專用設定頁面來設定這些工具。

在確認以下所有條件前，不建議將方舟雲端應用程式當作一般模型接入：

1. 已依火山方舟目前的官方文件開通 Web Search；
2. 已確認呼叫的是 Chat API、Responses API 或應用程式 Bot API；
3. 已取得對應的 Model ID、Endpoint ID 或 Bot ID；
4. 已確認請求位址和驗證方式；
5. 已確認傳回事件能由 Cherry Studio 目前的端點解析；
6. 已確認引用、串流輸出和工具結果格式；
7. 已了解模型與搜尋外掛程式的費用。

{% hint style="info" %}
這是進階相容情境，不屬於目前 V2 的內建聯網流程。方舟 API 升級後，歷史應用程式 URL 和參數可能失效。
{% endhint %}

火山方舟目前的工具說明可參閱[火山方舟產品文件](https://www.volcengine.com/docs/82379/)和[工具呼叫](https://www.volcengine.com/docs/82379/1958524)。

## 隱私與費用

使用 Cherry Studio 外部聯網時，資料可能分別傳送給：

- 火山方舟：使用者問題、搜尋結果和讀取到的網頁正文；
- 搜尋供應商：搜尋關鍵字；
- 目標網站：網頁請求；
- URL 取得供應商：目標 URL，取決於所選服務。

費用可能包括：

- 方舟模型輸入與輸出 Token；
- 搜尋服務呼叫；
- 方舟推論接入點或模型單元；
- 額外網路流量；
- 如果另外使用方舟 Web Search，相關外掛程式費用。

不要依據舊螢幕截圖中的免費次數或價格編列預算，應以各服務目前的控制台為準。

## 常見問題

### 點選地球圖示後跳轉到網路搜尋設定

目前模型沒有原生聯網適配，並且缺少**預設搜尋供應商**或**預設 URL 取得供應商**。同時設定兩項後重試。

### 一般對話可用，但沒有呼叫搜尋工具

依序檢查：

1. 地球圖示是否反白；
2. 目前模型是否支援 Function Calling；
3. Model ID 是否被錯誤標記為不支援工具；
4. 是否使用了舊 DeepSeek R1；
5. 問題是否明確要求先搜尋並引用；
6. 搜尋供應商是否檢查成功。

可以改用目前的 Doubao Seed 工具模型，並在新對話中重試。

### 模型只說「我會搜尋」，但沒有結果

這不是成功的工具呼叫。檢查訊息詳細資料中是否出現結構化工具過程；如果沒有，請更換工具呼叫能力較穩定的模型。

### 有搜尋結果，但引用無法開啟

可能是網頁失效、登入限制、反爬蟲、地區限制或 Fetch 讀取失敗。要求模型改用其他來源，並手動核對關鍵結論。

### 開啟後仍使用模型舊知識

明確提示：

```text
必須先聯網搜尋；如果搜尋失敗，請說明失敗，不要只憑既有知識回答。
```

如果仍無效，請建立新對話、更換模型或檢查搜尋供應商。

### 想使用火山方舟自己的 Web Search

Cherry Studio 目前沒有對應的內建設定。不要將模型能力開關當作適配器；應依方舟目前的 Responses API 或應用程式 API 文件自行驗證，或暫時使用 Cherry Studio 外部聯網。

### 傳回 401、403、404 或 429

這些通常是方舟模型連線問題，而不是網路搜尋設定本身：

- `401`：API Key 無效；
- `403`：專案、模型或 Endpoint 沒有權限；
- `404`：API Host、Model ID 或 Endpoint ID 錯誤；
- `429`：達到速率、並行或額度限制。

先關閉聯網，確認一般對話恢復，再分別排查模型和搜尋服務。

***

### 💡 取得協助與提交意見

如果您在設定或使用過程中遇到疑問、Bug 或功能建議，請參閱[意見回饋](../question-contact/suggestions.md)中的官方管道。
