# 火山引擎（方舟 / 豆包）

火山方舟是火山引擎的大型模型服務平台，提供豆包及多家第三方模型。Cherry Studio V2 內建的服務商 ID 為 `doubao`，介面中可能顯示為 **Doubao**、**豆包**或**火山引擎**。

V2 預設 API Host：

```text
https://ark.cn-beijing.volces.com/api/v3/
```

{% hint style="info" %}
目前 V2 內建服務商預設使用 OpenAI 相容 Chat Completions。火山方舟官網同時提供 Responses API、Files API 和雲端內建工具，但官網支援不代表這些功能已自動接入 Cherry Studio。
{% endhint %}

## 使用前準備

1. 註冊並登入火山引擎；
2. 進入火山方舟控制台；
3. 確認專案與地區；
4. 開通準備使用的模型或計費方式；
5. 建立 API Key；
6. 從目前的模型清單複製 Model ID；
7. 確認餘額、額度和速率限制。

火山方舟的模型、版本、價格和上線/下架狀態會調整。本文不固定列出價格或贈送額度，請以[模型清單](https://www.volcengine.com/docs/82379/1554711)和控制台為準。

## 取得 API Key

1. 開啟[火山方舟控制台](https://console.volcengine.com/ark/)；
2. 確認目前的專案和華北 2（北京）地區；
3. 開啟 [API Key 管理](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey)；
4. 點選**建立 API Key**；
5. 填寫容易識別的名稱；
6. 複製並妥善保存。

{% hint style="danger" %}
API Key 相當於帳戶認證資料。不要寫入聊天、文件、程式碼儲存庫或問題截圖；外洩後應立即在方舟控制台刪除或輪替。
{% endhint %}

## 取得 Model ID

火山方舟目前可以使用標準模型的 Model ID，也可以在部分情境中使用自訂推論端點 ID。

| 識別碼 | 常見格式 | 適用情境 |
| --- | --- | --- |
| Model ID | `doubao-seed-...` | 平台預設、按量呼叫的模型 |
| Endpoint ID | `ep-...` | 自訂模型、專用資源或已建立的推論端點 |

取得目前的 Model ID：

1. 開啟[模型清單](https://www.volcengine.com/docs/82379/1554711)；
2. 選擇目標模型和版本；
3. 確認它支援 Chat API；
4. 複製完整的 Model ID；
5. 不要複製模型顯示名稱或控制台頁面 URL。

如果組織使用自訂模型、模型單元或專用推論端點，應從[推論端點](https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint)複製 `ep-...` ID。

## 在 Cherry Studio 設定

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **Doubao / 火山引擎**；
4. 在 API Key 中貼上方舟金鑰；
5. 保留 API Host `https://ark.cn-beijing.volces.com/api/v3/`；
6. 開啟頁面頂部的服務商開關；
7. 點選**新增模型**；
8. 貼上目前的 Model ID 或 Endpoint ID；
9. 只啟用準備使用的模型；
10. 執行模型健康檢查。

V2 預設清單中包含一些舊豆包、DeepSeek 和 Embedding 模型。預設只是候選項目，不代表模型仍在線上。

## 同步與手動新增

火山方舟的模型目錄與自訂推論端點不一定能夠透過標準 OpenAI 模型清單完整傳回，因此同步結果可能為空或不完整。

最穩定的方式是：

1. 從方舟目前的模型頁複製 Model ID；
2. 在 Cherry Studio 手動新增；
3. 檢查模型能力標籤；
4. 執行健康檢查；
5. 刪除無法呼叫的舊預設。

{% hint style="warning" %}
不要因為某個舊 Model ID 仍顯示在 V2 預設中就繼續使用。方舟模型版本通常帶有日期後綴，舊版本可能已經下架。
{% endhint %}

## API Host

保留預設：

```text
https://ark.cn-beijing.volces.com/api/v3/
```

Cherry Studio 會依模型類型附加請求路徑。舊教學中將完整的 `/chat/completions` 寫入 API Host 並以 `#` 結尾，是歷史相容方式；V2 不需要這樣設定。

如果使用非北京地區、Proxy 或企業專用網域，應完整替換 API Host，並確認：

- API Key 屬於同一專案與地區；
- 網域支援 `/api/v3`；
- Proxy 能夠轉送串流回應；
- Model ID 或 Endpoint ID 在目標環境中有效。

## 對話模型

目前內建服務商主要透過 OpenAI 相容 Chat Completions 進行對話。

建議依下列順序測試：

1. 傳送一則簡短的純文字訊息；
2. 檢查串流輸出；
3. 增加系統提示詞；
4. 測試較長的上下文；
5. 再測試圖片、思考和工具呼叫。

火山方舟官網的新範例可能優先顯示 Responses API。不要因為 Responses 範例可用，就假設 V2 目前的對話已切換至同一介面或支援所有 Responses 專屬欄位。

## 思考模式

不同豆包版本使用的思考參數不同。Cherry Studio V2 會依 Model ID 適配：

- 較新的 Doubao Seed 模型使用 `reasoningEffort`；
- 部分舊思考模型使用 `thinking: enabled`；
- 支援自動思考的舊模型可以使用 `thinking: auto`；
- 其他組合可能不傳送思考欄位。

如果修改思考強度後發生錯誤：

1. 將思考設定恢復為**預設**；
2. 清除模型自訂參數；
3. 確認 Model ID 與官方目前版本一致；
4. 查看該模型的 Chat API 範例；
5. 重新執行健康檢查。

不要將 Responses API 的 `thinking` 範例原樣複製到 Chat Completions 模型。

## 視覺與多模態

只有方舟明確標記為視覺或多模態的模型才能接收圖片或影片。

在 Cherry Studio 中：

1. 新增目前的視覺 Model ID；
2. 確認模型顯示圖片能力；
3. 先上傳一張小圖片；
4. 檢查模型是否確實理解內容；
5. 再嘗試多張圖片或較大的附件。

方舟官網提供原生檔案和影片輸入功能，但目前 V2 能否直接使用仍取決於用戶端的附件格式適配。官網支援某種輸入，不代表 Cherry Studio 已經使用 Files API 上傳該內容。

## MCP 與工具呼叫

Cherry Studio MCP 使用模型的結構化 Function Calling。

1. 先完成一般對話；
2. 只啟用一個簡單的 MCP 工具；
3. 明確要求呼叫；
4. 檢查是否產生結構化呼叫；
5. 確認工具結果能夠傳回給模型；
6. 再增加工具。

火山方舟的 Web Search、Image Process、Knowledge Search 和 Remote MCP 屬於方舟雲端工具，主要透過 Responses API 設定。它們與 Cherry Studio 自行新增的 MCP 伺服器不是同一套設定。

模型只用文字描述「將要呼叫工具」不等於真實呼叫，應檢查 Model ID、介面和工具定義。

## Embedding 與知識庫

火山方舟提供文字和多模態向量化 API。V2 預設中可能保留舊的 Embedding Model ID，但應優先使用方舟目前文件列出的版本。

建立知識庫時：

1. 從方舟目前的向量化模型頁複製 Model ID；
2. 在 Cherry Studio 手動新增；
3. 確認模型被識別為 Embedding；
4. 偵測向量維度；
5. 執行健康檢查；
6. 匯入少量文件試執行；
7. 再批次匯入。

多模態向量化模型接受的輸入格式可能與 Cherry Studio 知識庫目前的文字分段不同。用於文件知識庫時，應先驗證純文字 Embedding。

Embedding 模型或向量維度一旦用於現有知識庫，就不應直接更換；否則通常需要重新建立向量索引。

目前 V2 未為 `doubao` 內建登記專用 Rerank 模型。需要重排時，應選擇已受 V2 支援且通過健康檢查的其他服務商。

## 圖片生成

火山方舟官網提供圖片生成 API，支援 Model ID 或圖片推論端點 ID。

但是，目前 V2 `main` 分支未為內建的 `doubao` 服務商登記專用圖片生成模型和傳輸鏈路。因此：

- 官網支援 Seedream 不代表 Cherry Studio 繪畫頁面會自動出現；
- 不要將圖片 Model ID 當作一般對話模型；
- 不要根據舊截圖手動猜測 Endpoint Type；
- 以目前繪畫頁面實際可選的服務商和模型為準。

如果後續 V2 版本加入方舟圖片適配，應重新同步或新增目前的 Model ID，並先使用單張、常見尺寸測試。

{% hint style="warning" %}
圖片生成可能依成功輸出張數計費。不要為了驗證相容性而連續重複提交工作。
{% endhint %}

## PDF 與附件

目前 V2 會先在本機擷取 PDF 文字，再傳送給方舟對話模型：

- 文字型 PDF 通常可以處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會占用模型上下文並產生費用；
- PDF 中的圖片需要單獨傳送給視覺模型。

這與方舟原生 Files API 或文件理解 API 不同。Cherry Studio 不會因為方舟支援檔案上傳，就自動將 PDF 作為方舟檔案物件處理。

上傳文件、圖片或知識庫內容前，應確認符合隱私、資料安全和組織合規要求。

## 計費、限流與用量

方舟可能同時受到以下因素限制：

- 帳戶餘額；
- 專案預算；
- 按量、模型單元或方案權益；
- RPM / TPM；
- 推論端點限流；
- 模型並行；
- 內容安全政策。

建議在控制台查看用量統計並設定預算警示。自訂 Endpoint 還應檢查其狀態、資源規格和限流設定。

## 常見問題

### 傳回 401

API Key 錯誤、已刪除、複製時帶入空格，或 Key 與 API Host 不相符。重新複製方舟 API Key。

### 傳回 403

專案、模型、Endpoint 或內容沒有權限。檢查模型開通狀態、專案、IAM 和內容安全政策。

### 傳回 404

API Host、Model ID 或 Endpoint ID 錯誤，或模型已下架。恢復預設位址，並從目前的模型頁重新複製 ID。

### 傳回 429

已達到模型、專案或推論端點的 RPM、TPM 或並行限制。降低並行數並等待恢復。

### 模型清單是空的

方舟不一定會透過標準模型清單傳回所有模型與自訂 Endpoint。直接從官方模型頁或推論端點頁複製 ID 後手動新增。

### 預設模型無法使用

V2 預設中可能包含已下架的舊日期版本。刪除失效模型，新增目前的 Model ID。

### Model ID 可用，但 Endpoint ID 無法使用

Endpoint 可能未啟動、未綁定正確模型、屬於其他專案，或資源已釋放。前往方舟控制台檢查 Endpoint 狀態。

### 思考參數錯誤

恢復為預設思考設定。新舊豆包模型的 `reasoningEffort` 與 `thinking` 參數不能混用。

### 一般對話可用，但 MCP 未呼叫

確認模型支援 Function Calling。方舟雲端 Remote MCP 與 Cherry Studio MCP 是不同功能，不能只在方舟控制台啟用。

### 無法新增 Embedding 模型

確認使用的是向量化 Model ID，並在模型管理中標記為 Embedding。不要將顯示名稱或 Endpoint 頁面 URL 當作模型 ID。

### Seedream 在官網可用，但繪畫頁面沒有

目前 V2 內建的 `doubao` 服務商尚未登記專用圖片生成鏈路。等待用戶端適配或使用繪畫頁面已有的服務商。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。火山方舟目前的功能請參閱[產品文件](https://www.volcengine.com/docs/82379/)、[模型清單](https://www.volcengine.com/docs/82379/1554711)、[API 參考](https://www.volcengine.com/docs/82379/1523520)、[管理推論端點](https://www.volcengine.com/docs/82379/1182403)和[圖片生成 API](https://www.volcengine.com/docs/82379/1824137)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
