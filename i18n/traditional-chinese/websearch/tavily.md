---
description: 在 Cherry Studio V2 中設定 Tavily，取得穩定的關鍵字網路搜尋能力。
icon: magnifying-glass
---

# Tavily 網路搜尋

Tavily 是面向 AI 應用程式的網路搜尋服務。在 Cherry Studio V2 中，它負責依關鍵字尋找網頁，並將標題、摘要和連結交給模型產生回答。

{% hint style="info" %}
Tavily 在目前版本中是**關鍵字搜尋供應商**，不能取代網頁讀取服務。如果希望模型繼續讀取某個結果頁面的完整內容，還需要另外設定預設 URL 讀取供應商，例如 Fetch 或 Jina。
{% endhint %}

## 使用前準備

設定 Tavily 需要：

- 一個可正常使用的 Tavily 帳號；
- 一組 Tavily API Key；
- Cherry Studio 中至少一個可對話的模型；
- 如需讀取特定網頁，再設定一個 URL 讀取供應商。

Tavily 依 API Credits 計量使用。免費額度、付費方案和呼叫限制可能調整，請以 [Tavily Pricing](https://www.tavily.com/pricing) 和控制台中的即時資訊為準。

## 取得 API Key

1. 開啟 [Tavily Platform](https://app.tavily.com/home)。
2. 依頁面提示註冊或登入帳號。
3. 在控制台的 API Keys 區域建立或找到可用的 Key。
4. 複製 Key，準備貼到 Cherry Studio。

Tavily 的註冊和驗證流程可能隨時間變更，因此本文不固定描述驗證碼、雙重驗證或第三方登入介面。遇到差異時，請以 Tavily 目前頁面的提示為準。

{% hint style="danger" %}
API Key 相當於帳號憑證。不要將真實 Key 放入螢幕截圖、聊天記錄、公開文件或程式碼儲存庫；如果懷疑洩漏，應立即在 Tavily 控制台撤銷舊 Key 並建立新 Key。
{% endhint %}

## 在 Cherry Studio 中設定

### 1. 開啟網路搜尋設定

進入：

> **設定 → 網路搜尋**

在供應商清單中找到 **Tavily**。

### 2. 填寫 API Key

將 Tavily 控制台中的 Key 貼到 **API 金鑰**輸入框。

如果已儲存多組 Key，可以在 Key 清單中切換或管理。多組 Key 適合輪替憑證，但不會增加單一 Tavily 帳號的總額度。

### 3. 檢查 API Host

預設 API Host 為：

```text
https://api.tavily.com
```

通常保留預設值即可。只有在使用相容代理或閘道時才需要修改；自訂位址必須能夠相容 Tavily 的 `/search` 介面和 Bearer 驗證。

{% hint style="warning" %}
錯誤的 API Host、重複串接 `/search`，或代理未轉送 `Authorization` 請求標頭，都會導致連線檢查或實際搜尋失敗。
{% endhint %}

### 4. 檢查設定

點選 Tavily 卡片中的**檢查**按鈕。

- 檢查成功：表示目前的 API Host 和 Key 可以完成基本請求；
- 檢查失敗：先核對 Key、Host、網路代理和 Tavily 帳號狀態，再查看下方的疑難排解。

### 5. 設為預設關鍵字搜尋供應商

將 Tavily 設為**預設搜尋供應商**。Cherry Studio 在需要外部關鍵字搜尋時會使用它。

如果還需要模型開啟搜尋結果中的網頁，請同時選擇預設的 **URL 讀取供應商**。常見組合為：

| 用途 | 建議選擇 |
| --- | --- |
| 關鍵字搜尋 | Tavily |
| URL 讀取 | Fetch 或 Jina |

搜尋供應商與 URL 讀取供應商是兩個獨立設定；只設定 Tavily 不代表應用程式能夠讀取任意網頁全文。

## 調整通用搜尋設定

Cherry Studio 的網路搜尋設定會統一套用於 Tavily 等外部供應商。

### 最大結果數

可以設定每次搜尋傳回的最大結果數。結果越多，模型可參考的資訊通常越豐富，但搜尋耗時、上下文長度和 API 用量也可能增加。

建議先使用預設值；回答缺少來源時再逐步增加。

### 搜尋結果壓縮

可以依任務選擇不壓縮或截斷搜尋結果。壓縮有助於減少上下文占用，但過度截斷可能遺失關鍵細節。

### 網路搜尋黑名單

黑名單會在 Tavily 傳回結果後，由 Cherry Studio 篩選不希望使用的網址。設定方法請參閱[網路搜尋黑名單](blacklist.md)。

{% hint style="info" %}
目前 Cherry Studio 的 Tavily 適配器只向 Tavily 傳送查詢內容和最大結果數。Tavily 官方 API 提供的 `search_depth`、`topic`、`include_domains`、`exclude_domains`、`include_answer` 等進階參數，暫未在 V2 設定介面中單獨開放。
{% endhint %}

## 在對話中使用

1. 開啟一個助理或新對話。
2. 選擇要使用的模型。
3. 點選輸入框附近的**地球圖示**，開啟網路搜尋。
4. 輸入需要最新資料或外部來源的問題並傳送。
5. 檢查回答中的來源編號和連結。

例如：

```text
請搜尋 Cherry Studio 最近一個正式版本的更新內容，
依功能分類摘要，並在每項結論後標示來源。
```

如果模型本身支援原生聯網，Cherry Studio 會優先依該模型的能力處理；對於沒有原生聯網能力、但支援工具呼叫的模型，Tavily 可作為外部關鍵字搜尋供應商使用。

有關兩類聯網方式的差異，請參閱[網路搜尋](README.md)。

## 目前整合能力

| 能力 | 目前 V2 支援情況 |
| --- | --- |
| 關鍵字搜尋 | 支援 |
| 傳回網頁標題、摘要和 URL | 支援 |
| 設定最大結果數 | 支援，使用通用網路搜尋設定 |
| 多組 API Key | 支援 |
| 自訂 API Host | 支援 |
| 讀取指定 URL 的正文 | 不支援，需要設定 Fetch 或 Jina |
| Tavily Search 進階參數 | 暫未在介面開放 |
| Tavily Extract、Crawl、Map、Research | 目前 Tavily 適配器尚未接入 |

Cherry Studio 目前向 Tavily 的 `/search` 介面發出請求，並使用 Bearer API Key 驗證。有關介面能力，請參閱 [Tavily Search API](https://docs.tavily.com/documentation/api-reference/endpoint/search)。

## 常見問題

### 檢查按鈕提示驗證失敗

通常與 API Key 有關：

1. 重新從 Tavily 控制台複製 Key，避免多餘空格；
2. 確認 Key 尚未被撤銷；
3. 確認目前帳號或團隊仍允許使用該 Key；
4. 如果懷疑洩漏，撤銷舊 Key 後建立新 Key。

### 提示額度不足或請求過於頻繁

檢查 Tavily 控制台中的 Credits、帳單和速率限制。等待額度恢復、降低搜尋頻率，或依實際需要調整方案。

不要透過持續重試繞過限制；這會產生更多無效請求。

### 檢查成功，但對話沒有聯網

依序確認：

- Tavily 已設為預設關鍵字搜尋供應商；
- 目前對話的地球圖示已開啟；
- 目前模型支援工具呼叫，或本身支援原生聯網；
- 問題確實需要外部搜尋；
- 沒有被助理設定或模型設定停用工具。

### 有搜尋結果，但模型無法讀取網頁詳細資料

Tavily 在目前版本中只負責關鍵字搜尋。請再將 Fetch 或 Jina 設為預設 URL 讀取供應商，然後重試。

### 搜尋結果為空或不夠相關

可以：

- 將問題改寫成明確的搜尋關鍵字；
- 補充時間、地區、產品名稱或版本號；
- 適度提高最大結果數；
- 檢查黑名單是否誤篩選了目標網站；
- 對重要結論更換搜尋詞再次核對。

### 自訂 API Host 後失敗

還原預設位址：

```text
https://api.tavily.com
```

如果必須使用代理或閘道，請確認它：

- 支援 `POST /search`；
- 能轉送 Bearer 驗證；
- 傳回與 Tavily Search API 相容的 JSON；
- 沒有額外串接或刪除路徑。

## 安全、隱私與準確性

- 搜尋詞會傳送給 Tavily；不要在查詢中包含密碼、API Key、個人隱私或未公開的業務資料。
- 網路結果可能過時、錯誤或互相矛盾。涉及醫療、法律、財務等高風險結論時，應開啟原始來源並進行人工核驗。
- Tavily 的額度和計費由供應商管理。大量使用前，先在控制台確認目前方案和消耗規則。
- 定期輪替不再需要的 Key；洩漏處理可參閱 [Tavily API Key Management](https://docs.tavily.com/documentation/best-practices/api-key-management)。

## 相關文件

- [網路搜尋](README.md)
- [免費聯網模式](mian-fei-lian-wang-mo-shi.md)
- [網路搜尋黑名單](blacklist.md)
- [Tavily Quickstart](https://docs.tavily.com/documentation/quickstart)

***

### 取得協助與提交意見

如果在設定或使用過程中遇到問題，請透過[意見回饋](../question-contact/suggestions.md)中列出的官方管道提交意見。回報時建議說明 Cherry Studio 版本、模型名稱、錯誤提示和是否使用代理，但不要附上真實 API Key。
