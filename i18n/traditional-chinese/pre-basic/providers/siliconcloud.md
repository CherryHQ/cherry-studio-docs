# 矽基流動

矽基流動（SiliconFlow）提供對話、視覺、Embedding、Rerank 和圖片生成 API。Cherry Studio V2 內建矽基流動服務商，並為對話、Embedding 和圖片生成實作了專用適配。

V2 預設 API Host：

```text
https://api.siliconflow.cn
```

實際的 OpenAI 相容請求使用 `/v1` 路徑，例如 `https://api.siliconflow.cn/v1/chat/completions`。

{% hint style="info" %}
首次設定時應保留 V2 預設位址。不要將控制台頁面、模型廣場 URL 或文件位址填入 API Host。
{% endhint %}

## 使用前準備

1. 註冊並登入 SiliconFlow；
2. 完成平台要求的帳戶驗證；
3. 建立 API Key；
4. 儲值或確認帳戶仍有可用餘額；
5. 查看準備使用的模型是否仍在線上；
6. 確認模型的價格和速率限制。

SiliconFlow 會調整模型、能力、價格和上線/下架狀態。本文不固定列出贈金、免費模型或價格，請以[模型廣場](https://cloud.siliconflow.cn/models)和控制台為準。

## 取得 API Key

1. 登入 [SiliconFlow 控制台](https://cloud.siliconflow.cn/)；
2. 開啟 [API 金鑰](https://cloud.siliconflow.cn/account/ak)；
3. 點選**新增金鑰**；
4. 填寫容易識別的名稱；
5. 複製產生的 Key；
6. 儲存至安全的密碼管理工具。

{% hint style="danger" %}
API Key 相當於帳戶認證資料。不要寫入聊天、文件、程式碼儲存庫或問題截圖；外洩後應立即刪除並重新建立。
{% endhint %}

## 在 Cherry Studio 設定

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **Silicon / 矽基流動**；
4. 在 API Key 中貼上 SiliconFlow 金鑰；
5. 保留 API Host `https://api.siliconflow.cn`；
6. 開啟頁面頂部的服務商開關；
7. 點選**新增**或同步模型；
8. 檢查同步預覽並套用變更；
9. 只啟用準備使用的模型；
10. 執行模型健康檢查。

連線檢查只代表金鑰和基礎請求可用，不表示帳戶能夠呼叫清單中的每個模型。最終權限、餘額和速率由 SiliconFlow 判定。

## 同步與新增模型

Cherry Studio 會從 SiliconFlow 的模型清單介面讀取目前的模型。SiliconFlow 的 `/v1/models` 還支援依下列類型篩選：

- `chat`
- `embedding`
- `reranker`
- `text-to-image`
- `image-to-image`
- 其他音訊與影片類型

同步後建議：

1. 查看新增、更新和移除項目；
2. 確認每個模型的類型；
3. 套用同步結果；
4. 刪除自己手動保留的舊模型；
5. 分別執行健康檢查。

V2 內建模型只是候選項目，應以平台即時傳回的結果為準。如果模型未被自動識別為 Embedding、Rerank、視覺或圖片生成，可以在模型管理中核對能力，但不要只修改顯示名稱來繞過介面差異。

{% hint style="warning" %}
Model ID 必須與 SiliconFlow 目前的清單完全一致，包括 `Pro/` 前綴、組織名稱、大小寫、斜線和版本後綴。
{% endhint %}

## 選擇對話模型

SiliconFlow 對話使用 OpenAI 相容 Chat Completions。

建議依下列順序測試：

1. 傳送一則簡短的純文字訊息；
2. 檢查串流輸出；
3. 增加系統提示詞；
4. 測試較長的上下文；
5. 再測試圖片、思考和工具呼叫。

`Pro/` 版本與一般版本可能具有不同的價格、吞吐量或可用性。應將它們視為不同的 Model ID，並分別執行健康檢查。

## 視覺模型

只有 SiliconFlow 明確標記為視覺語言模型的 Model ID 才能接收圖片。

在 Cherry Studio 中：

1. 同步最新模型；
2. 選擇顯示圖片能力的模型；
3. 先上傳一張小圖片；
4. 檢查模型是否確實理解圖片；
5. 再嘗試多張圖片或高解析度圖片。

同一模型系列的文字版與視覺版可能是不同的 ID。圖片還會增加請求內容大小、上下文消耗和費用。

## 思考模式

SiliconFlow 的部分 DeepSeek、GLM、Qwen 和混元模型使用 `enable_thinking` 與 `thinking_budget`。

Cherry Studio V2 對受支援的 SiliconFlow 思考模型會：

- 使用 `enable_thinking` 開關；
- 設定思考預算時，將非零預算至少提高至 32,768；
- 關閉思考時傳送 `enable_thinking: false`。

這表示 V2 目前不適合在 SiliconFlow 上精確設定較小的思考預算。需要減少消耗時，優先關閉思考、縮短上下文或改用非思考模型。

如果開啟思考後發生錯誤：

1. 將思考設定恢復為**預設**；
2. 清除模型自訂參數；
3. 確認 Model ID 仍在線上；
4. 對照 SiliconFlow 目前的模型說明；
5. 重新執行健康檢查。

## MCP 與工具呼叫

SiliconFlow Chat Completions 支援 `tools`，但最終能否正確呼叫仍取決於具體模型。

1. 先確認一般對話正常；
2. 只啟用一個簡單的 MCP 工具；
3. 明確要求呼叫；
4. 檢查是否產生結構化呼叫；
5. 確認工具結果能夠傳回給模型；
6. 再增加工具。

模型只用文字描述「將要呼叫工具」不等於真實呼叫。出現這種情況時，應檢查模型能力、提示詞和工具定義。

## Embedding、Rerank 與知識庫

SiliconFlow 提供：

```text
POST /v1/embeddings
POST /v1/rerank
```

目前可見的範例模型可能包括 `BAAI/bge-m3`、Qwen Embedding、Qwen Reranker 和 BGE Reranker，但實際清單應從模型廣場或同步結果取得。

建立知識庫時：

1. 同步模型；
2. 選擇明確識別為 Embedding 的模型；
3. 偵測向量維度；
4. 執行健康檢查；
5. 再選擇目前可用的 Rerank 模型；
6. 匯入少量文件試執行；
7. 確認檢索與重排結果後再批次匯入。

部分 Qwen Embedding 模型允許選擇輸出維度。維度一旦用於現有知識庫，就不應直接修改；否則通常需要重新建立向量索引。

Rerank 與 Embedding 使用不同的端點和模型。Embedding 可用不代表 Rerank 一定可用，應分別檢查。

## 圖片生成與編輯

Cherry Studio V2 為 SiliconFlow 實作了專用圖片模型，請求會傳送至：

```text
POST /v1/images/generations
```

目前 V2 模型註冊資訊主要涵蓋 Qwen Image 的生成與編輯。官網出現的其他圖片模型不一定已被目前版本正確識別，應以 Cherry Studio 繪畫頁面的可選項目為準。

根據模型能力，V2 可以傳遞：

- `image_size`
- `batch_size`
- `seed`
- `negative_prompt`
- `num_inference_steps`
- `guidance_scale`
- `cfg`
- `prompt_enhancement`
- 最多三張編輯輸入圖片

SiliconFlow 使用明確的 `image_size`，V2 不會將單獨的寬高比參數自動轉換為有效請求。目前的專用適配也不支援遮罩輸入。

{% hint style="warning" %}
圖片模型可能依輸出張數計費。首次測試時將批次數量設為 1，並使用模型支援的常見尺寸。
{% endhint %}

如果傳回的是圖片 URL，應及時儲存結果。暫時連結的有效期間由 SiliconFlow 決定。

## PDF 與附件

目前 V2 會先在本機擷取 PDF 文字，再傳送給 SiliconFlow 對話模型：

- 文字型 PDF 通常可以處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會占用模型上下文並產生費用；
- PDF 中的圖片需要單獨傳送給視覺模型。

SiliconFlow 是雲端服務。上傳文件、圖片或知識庫內容前，應確認符合隱私、著作權和組織安全要求。

## 速率、餘額與疑難排解資訊

SiliconFlow 的限流可能依模型分別計算，並同時受到 RPM、TPM、RPD、TPD、IPM 或 IPD 等指標影響。

建議：

1. 在控制台查看餘額與模型價格；
2. 為自動工作設定並行和重試上限；
3. 遇到 429 時降低頻率並等待；
4. 定期同步模型；
5. 儲存錯誤回應中的 `x-siliconcloud-trace-id`，以便提交支援單。

不要透過建立多個 Key 來規避帳戶層級限流；平台限制通常不是依單一 Key 個別計算。

## 常見問題

### 傳回 401

API Key 錯誤、已刪除、複製時帶入空格，或請求未正確使用 Bearer 驗證。重新複製或建立 Key。

### 傳回 403

帳戶、模型或內容沒有權限。檢查實名驗證、餘額、模型資格和平台政策。

### 傳回 404

API Host、Model ID 或介面類型錯誤。恢復 V2 預設位址，並重新同步模型。

### 傳回 429

已達到模型的 RPM、TPM、RPD、TPD、IPM 或 IPD 限制。降低並行數、縮短上下文並等待恢復。

### 傳回 503 或 504

模型忙碌或上游逾時。降低並行數後重試；持續失敗時，改用其他在線模型並記錄 Trace ID。

### 模型清單是空的

檢查 API Key、API Host 和網路 Proxy。也可以從模型廣場複製完整的 Model ID 後手動新增。

### 預設模型無法使用

V2 預設可能早於模型下架、重新命名或權限變更。以即時同步結果為準，移除失效模型。

### 思考預算與設定不一致

V2 目前會將受支援 SiliconFlow 模型的非零思考預算至少提高至 32,768。這是用戶端適配行為；需要減少消耗時，應關閉思考或改用非思考模型。

### Embedding 可用，但 Rerank 無法使用

兩者使用不同的模型和介面。確認 Rerank Model ID、餘額和能力標籤，並單獨執行健康檢查。

### 圖片模型在官網存在，但繪畫頁面沒有

目前 V2 尚未為該模型登記圖片生成模式。不要將它當作對話模型使用；等待適配或選擇繪畫頁面已有的模型。

### 圖片編輯只處理了第一張圖片

確認模型是否支援多圖編輯。V2 最多傳送三張輸入圖片，但具體模型可能只接受一張。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。SiliconFlow 目前的介面與模型請參閱[模型清單](https://docs.siliconflow.cn/cn/api-reference/models/get-model-list)、[Chat Completions](https://docs.siliconflow.cn/cn/api-reference/chat-completions/chat-completions)、[Embedding](https://docs.siliconflow.cn/cn/api-reference/embeddings/create-embeddings)、[Rerank](https://docs.siliconflow.cn/cn/api-reference/rerank/create-rerank)和[圖片生成](https://docs.siliconflow.cn/cn/userguide/capabilities/images)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
