# ModelScope（魔搭）

ModelScope 透過 API-Inference 將部分開源模型提供為可直接呼叫的線上 API。Cherry Studio V2 內建 ModelScope 服務商，支援 OpenAI 相容對話、視覺模型、嵌入模型和非同步圖片生成。

預設 Base URL：

```text
https://api-inference.modelscope.cn/v1/
```

{% hint style="info" %}
ModelScope 模型庫中的模型不一定都支援 API-Inference。只有模型頁面帶有 API-Inference 標記並提供呼叫範例的模型，才能直接接入 Cherry Studio。
{% endhint %}

## 使用前確認

ModelScope 免費 API-Inference 目前要求：

1. 註冊並登入 ModelScope；
2. 綁定阿里雲帳號；
3. 完成對應阿里雲帳號的實名驗證；
4. 建立 ModelScope Access Token；
5. 使用目前仍支援 API-Inference 的模型。

API-Inference 是體驗型免費服務，不提供正式環境 SLA。需要商業、高並行或穩定服務時，應使用商業 API 提供商或自行部署模型。

## 取得 Access Token

1. 登入 [ModelScope](https://modelscope.cn/)；
2. 開啟[存取權杖](https://modelscope.cn/my/myaccesstoken)；
3. 新增權杖並填寫容易識別的名稱；
4. 複製產生的 Access Token；
5. 將 Token 儲存在安全位置。

{% hint style="danger" %}
Access Token 相當於帳戶認證資料。不要寫入聊天、文件、程式碼儲存庫或問題截圖；外洩後應立即在 ModelScope 刪除並重新建立。
{% endhint %}

## 在 Cherry Studio 設定

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **ModelScope 魔搭**；
4. 在 API Key 中貼上 Access Token；
5. 保留 Base URL `https://api-inference.modelscope.cn/v1/`；
6. 開啟頁面頂部的服務商開關；
7. 點選**新增**或同步模型；
8. 檢查同步預覽並套用變更；
9. 只啟用準備使用的模型；
10. 執行模型健康檢查。

如果同步清單中包含舊模型，不要直接假設它仍可呼叫。ModelScope 會隨著新模型發布逐步調整或下架舊模型，應前往模型詳細資料頁確認 API-Inference 狀態。

## 尋找可用模型

1. 開啟 [ModelScope 模型庫](https://modelscope.cn/models)；
2. 篩選支援 **API-Inference** 的模型；
3. 開啟模型詳細資料頁；
4. 確認右側有 API 呼叫入口與範例；
5. 複製完整的 Model ID；
6. 在 Cherry Studio 同步或手動新增該 ID；
7. 執行健康檢查。

Model ID 通常包含組織與模型名稱，例如：

```text
Qwen/Qwen3.5-35B-A3B
```

大小寫、斜線和後綴都屬於 ID。不要將頁面顯示名稱、儲存庫 URL 或本機檔案名稱當作 API Model ID。

{% hint style="warning" %}
V2 內建模型清單只是候選項目，應以平台即時支援狀態為準。遇到 404 或模型無法使用時，先前往 ModelScope 模型頁核對，不要反覆重試已下架的模型。
{% endhint %}

## 對話模型

ModelScope 的 LLM API-Inference 使用 OpenAI 相容 Chat Completions。選擇模型時，應確認它是對話或指令模型，而不是基礎模型、Embedding 或圖片生成模型。

建議依下列順序測試：

1. 傳送一則簡短的純文字訊息；
2. 測試串流輸出；
3. 再增加系統提示詞；
4. 測試長上下文；
5. 最後測試思考、圖片或工具呼叫。

不同開源模型的參數和提示範本可能不同。ModelScope 官方建議以模型詳細資料頁的 API 範例為準，尤其是思考模型。

## 視覺模型

支援視覺的模型可以透過 OpenAI 相容訊息接收圖片 URL 或 Base64 圖片。

在 Cherry Studio 中：

1. 選擇明確支援視覺的 Model ID；
2. 確認模型顯示圖片能力；
3. 先上傳一張小圖片；
4. 檢查模型是否確實理解圖片；
5. 再嘗試多張圖片或高解析度圖片。

模型系列名稱相同不代表所有變體都支援視覺。圖片還會占用更多上下文和免費額度。

## 思考與工具呼叫

### 思考

思考模型可能會使用模型專屬參數或傳回格式。如果修改思考選項後發生錯誤：

1. 恢復為**預設**；
2. 清除自訂參數；
3. 對照模型頁範例；
4. 重新執行健康檢查。

### MCP 與工具呼叫

Cherry Studio MCP 要求模型能夠輸出結構化 Tool Calling。

1. 先完成一般對話；
2. 只啟用一個簡單的 MCP 工具；
3. 明確要求呼叫；
4. 檢查是否確實產生結構化呼叫；
5. 確認結果能夠傳回給模型；
6. 再增加工具。

ModelScope 平台的 MCP 廣場與 ModelScope 模型服務是兩項不同功能。模型 Access Token 可以用於相應的平台功能，但在 Cherry Studio 中仍需分別設定「模型服務」和「MCP 伺服器」。

## 圖片生成與編輯

Cherry Studio V2 為 ModelScope 實作了專用的非同步圖片生成鏈路：

1. 向 `/v1/images/generations` 提交工作；
2. 取得 `task_id`；
3. 輪詢 `/v1/tasks/{task_id}`；
4. 工作成功後讀取圖片 URL。

選擇 ModelScope 目前支援的 AIGC 模型後，可以在繪畫頁面使用：

- 圖片尺寸；
- 負面提示詞；
- 取樣步數；
- Guidance；
- Seed；
- 支援模型的圖片編輯輸入；
- 支援模型的 LoRA。

不同模型支援的尺寸、步數、Guidance 和編輯能力不同。應以模型詳細資料頁提供的範圍為準。

圖片工作採非同步執行，等待時間可能明顯長於對話。取消工作、網路中斷、額度不足或平台負載過高都可能導致輪詢失敗。

## 嵌入模型與知識庫

Cherry Studio 的 ModelScope 服務商實作了 OpenAI 相容 Embeddings 呼叫，但只有實際提供相容 Embedding API 的 ModelScope 模型才能使用。

1. 在模型頁確認工作類型與 API 範例；
2. 新增完整的 Model ID；
3. 確認 Cherry Studio 將其識別為嵌入模型；
4. 在知識庫中偵測維度；
5. 執行健康檢查；
6. 再匯入文件。

模型或維度一旦用於現有知識庫，就不應隨意更換；否則通常需要重新建立向量索引。

## PDF 與附件

目前 V2 會先在本機擷取 PDF 文字，再傳送給 ModelScope 對話模型：

- 文字型 PDF 通常可以處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會占用上下文與免費呼叫額度；
- PDF 中的圖片需要單獨傳送給視覺模型。

ModelScope 是雲端服務。上傳前應確認文件符合隱私和組織安全要求。

## 額度與限流

ModelScope 目前的免費 API-Inference 規則包括：

- 每位註冊使用者每天總計最多 2,000 次呼叫；
- 單一模型通常每天最多 200 次呼叫；
- 部分大型模型可能進一步限制為每天 100 次或更少；
- 並行數會隨平台負載動態調整；
- AIGC 模型可能有獨立限制；
- 具體模型額度可能隨時動態變更。

服務傳回的回應標頭可以包含：

| 回應標頭 | 含義 |
| --- | --- |
| `modelscope-ratelimit-requests-limit` | 使用者每日總額度 |
| `modelscope-ratelimit-requests-remaining` | 使用者每日剩餘額度 |
| `modelscope-ratelimit-model-requests-limit` | 目前模型每日額度 |
| `modelscope-ratelimit-model-requests-remaining` | 目前模型剩餘額度 |

Cherry Studio 目前不會將這些回應標頭當作完整帳單頁面顯示。判斷額度時，應綜合錯誤資訊、ModelScope 頁面和平台最新規則。

不應透過建立或切換備用帳號來規避平台限制。免費額度用於體驗和原型，批次呼叫應遷移至合適的商業服務。

## API-Inference 與 API-Provider

ModelScope 還提供 API-Provider，可以綁定外部 API 提供商。它與免費 API-Inference 的額度和計費來源不同。

- API-Inference：由 ModelScope 提供體驗型推論資源；
- API-Provider：呼叫綁定的外部提供商，不受免費 API-Inference 的同一限額約束，但受外部服務商的計費與限制。

本頁的預設 `api-inference.modelscope.cn` 設定指向 API-Inference。不要在不了解計費來源的情況下混用外部提供商認證資料。

## 常見問題

### 傳回 401

Access Token 錯誤、已刪除、包含空格或未正確傳送。重新複製 Token，並確認 Base URL 未被 Proxy 改寫。

### 傳回 403

帳號可能未綁定阿里雲、未完成實名驗證，或模型權限受限。先在 ModelScope 網頁完成帳戶要求。

### 傳回 404

模型 ID 錯誤、模型已下架或 Base URL 不正確。檢查完整 ID 和模型頁的 API-Inference 狀態。

### 傳回 429

可能已達到使用者總額度、單一模型額度、AIGC 獨立額度或動態並行限制。降低頻率並等待額度恢復；正式環境需求應改用商業服務。

### 模型清單是空的

檢查 Token、Base URL 和網路。也可以從模型頁複製目前支援的完整 Model ID 後手動新增。

### 預設模型無法使用

V2 預設可能早於平台下架或重新命名。以 ModelScope 目前的模型頁為準，重新同步或改用仍受支援的模型。

### 圖片生成持續等待

工作仍在佇列中、平台忙碌、輪詢網路失敗或額度不足。檢查 ModelScope 工作狀態並降低並行數。

### 圖片編輯參數錯誤

目標模型可能不支援編輯、輸入尺寸不合規，或需要特定的 `image_url`。請對照模型頁範例和參數範圍。

### MCP 無法使用

先確認模型支援工具呼叫。ModelScope MCP 廣場的服務還需要在 Cherry Studio 的 MCP 設定中單獨同步或新增。

### 需要穩定的高並行

免費 API-Inference 不適合 SLA 或商業高並行。請使用 ModelScope API-Provider、其他商業模型服務，或部署開源模型。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。ModelScope 的模型、介面與最新額度請參閱 [API-Inference 文件](https://modelscope.cn/docs/model-service/API-Inference/intro)和[使用限制](https://modelscope.cn/docs/model-service/API-Inference/limits)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
