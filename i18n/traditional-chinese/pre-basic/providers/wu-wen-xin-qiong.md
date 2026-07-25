# 無問芯穹 GenStudio

無問芯穹 GenStudio 提供大型語言模型、視覺模型、Embedding、Rerank 等 API。Cherry Studio V2 已內建**無問芯穹（Infini）**服務商，透過 OpenAI 相容介面接入。

V2 預設 API Host：

```text
https://cloud.infini-ai.com/maas
```

Cherry Studio 會在請求時補齊 `/v1`，實際對話介面為：

```text
https://cloud.infini-ai.com/maas/v1/chat/completions
```

{% hint style="info" %}
使用內建服務商時，應優先保留預設 API Host。不要將模型廣場、控制台或文件頁面的 URL 填入 API Host。
{% endhint %}

## 使用前準備

1. 註冊並登入無問芯穹智算雲平台；
2. 確認目前帳號所屬租戶；
3. 建立 GenStudio API Key；
4. 在服務清單或模型廣場確認目標模型的 Model ID；
5. 查看模型價格、服務等級和速率限制；
6. 確認帳戶餘額或已購買的包並行服務仍可使用。

模型、價格和限額會調整。本文不固定列出「免費模型」或贈送額度，請以[服務清單](https://cloud.infini-ai.com/genstudio/usage/limit)和[預設模型清單](https://docs.infini-ai.com/gen-studio/models/supported-models.html)為準。

## 取得 API Key

1. 登入[智算雲平台](https://cloud.infini-ai.com/)；
2. 開啟 [API 金鑰管理](https://cloud.infini-ai.com/iam/secret/key)；
3. 建立新的 GenStudio API Key；
4. 複製完整金鑰；
5. 儲存至安全的密碼管理工具。

GenStudio 目前使用以 `sk-` 開頭的 API Key，並透過 Bearer 驗證傳送請求。

{% hint style="danger" %}
API Key 相當於帳戶認證資料。不要寫入聊天、文件、程式碼儲存庫、截圖或支援單；外洩後應立即刪除並重新建立。
{% endhint %}

## 在 Cherry Studio 設定

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇**無問芯穹 / Infini**；
4. 在 API Key 中貼上 GenStudio 金鑰；
5. 保留 API Host `https://cloud.infini-ai.com/maas`；
6. 開啟頁面頂部的服務商開關；
7. 點選**新增**或同步模型；
8. 查看同步預覽並套用變更；
9. 只啟用準備使用的模型；
10. 執行模型健康檢查。

健康檢查通過只代表目前的 Key、位址和測試模型可以完成基礎請求，不表示帳號擁有清單中所有模型的權限。

## 同步與新增模型

Cherry Studio 會使用 OpenAI 相容模型清單介面：

```text
GET /maas/v1/models
```

同步後建議：

1. 檢查新增、更新和移除項目；
2. 確認 Model ID 與服務清單完全一致；
3. 套用同步結果；
4. 刪除已下架的舊模型；
5. 分別測試對話、Embedding 和 Rerank 模型。

如果同步失敗，可以從服務清單或模型廣場複製 Model ID 後手動新增。Model ID 的大小寫、連字號、版本後綴和 `pro-` 前綴都屬於識別碼的一部分。

{% hint style="warning" %}
包並行服務通常使用以 `pro-` 開頭的專屬 Model ID。不要將一般按量模型和包並行模型視為同一個 ID。
{% endhint %}

V2 內建的候選模型可能早於平台目前的清單。實際使用時，應優先相信即時同步結果和服務清單。

## 選擇對話模型

GenStudio 對話模型使用 OpenAI 相容 Chat Completions。

首次測試建議：

1. 選擇目前帳戶明確可用的模型；
2. 傳送一則簡短的純文字訊息；
3. 檢查串流輸出；
4. 增加系統提示詞；
5. 再測試長上下文、思考、圖片和工具呼叫。

模型系列和版本會更新。不要依賴舊教學中的固定範例，直接從服務清單複製目前的 Model ID。

## 視覺模型

只有 GenStudio 明確標記為視覺語言模型的 Model ID 才能理解圖片。

在 Cherry Studio 中：

1. 同步最新模型；
2. 確認模型詳細資料包含圖片輸入能力；
3. 先上傳一張尺寸較小的圖片；
4. 詢問圖片中可直接驗證的內容；
5. 確認成功後再嘗試多張圖片或高解析度圖片。

同一系列的文字模型與視覺模型可能使用不同的 Model ID。模型名稱相近不代表輸入模態相同。

## 思考模式

GenStudio 提供多種推論模型，不同系列可能使用不同的思考參數和傳回格式。Cherry Studio 會依識別到的模型系列套用通用適配，但無問芯穹服務商目前沒有單獨的思考參數面板。

首次使用推論模型時：

1. 保持思考設定為**預設**；
2. 不新增自訂請求參數；
3. 確認基礎對話正常；
4. 再嘗試開啟或關閉思考；
5. 對照模型詳細資料檢查支援的參數。

如果開啟思考後傳回 400，應先恢復預設設定，而不是反覆修改 Model ID。

## MCP 與工具呼叫

GenStudio 的部分模型支援 Function Calling。Cherry Studio 可以透過 Chat Completions 將 MCP 工具定義傳送給模型，但最終能否穩定呼叫仍取決於具體模型。

建議依下列順序驗證：

1. 確認一般對話正常；
2. 只啟用一個參數簡單的 MCP 工具；
3. 明確要求模型呼叫該工具；
4. 檢查是否產生結構化工具呼叫；
5. 確認工具結果能夠傳回；
6. 再逐步增加工具。

模型只用文字描述「將要呼叫工具」不等於真實呼叫。出現這種情況時，應檢查模型詳細資料、工具定義和提示詞。

## Embedding 與知識庫

GenStudio 提供 OpenAI 相容 Embedding 介面：

```text
POST /maas/v1/embeddings
```

目前服務可能提供 `bge-m3` 等向量模型，實際 Model ID 應以服務清單為準。Cherry Studio 會根據模型 ID 和手動類型標記識別 Embedding 模型。

建立知識庫前：

1. 同步或手動新增 Embedding 模型；
2. 確認模型被識別為**嵌入**類型；
3. 執行健康檢查；
4. 偵測向量維度；
5. 使用少量文件建立測試知識庫；
6. 驗證召回結果後再批次匯入。

向量維度是知識庫索引的一部分。知識庫建立後更換 Embedding 模型或維度，通常需要重新建立索引。

## Rerank

GenStudio 提供 Rerank 介面：

```text
POST /maas/v1/rerank
```

官方目前的範例模型為 `bge-reranker-v2-m3`，但可用狀態仍應以服務清單為準。

在 Cherry Studio 中：

1. 同步或手動新增 Rerank 模型；
2. 確認模型被識別為**重排序**類型；
3. 在知識庫設定中選擇該模型；
4. 使用少量查詢比較啟用前後的結果；
5. 再決定是否用於正式知識庫。

Embedding 和 Rerank 使用不同的模型與端點。Embedding 可用不代表 Rerank 一定可用，應分別驗證。

## 圖片與影片生成

GenStudio 平台還提供圖片和影片生成功能，但 Cherry Studio V2 目前內建的無問芯穹服務商主要透過 OpenAI 相容的對話、Embedding 和 Rerank 介面運作，未登記無問芯穹專用的圖片或影片生成傳輸層。

因此：

- 不要將圖片或影片生成模型當作對話模型新增；
- 以 Cherry Studio 繪畫頁面實際可選的服務商和模型為準；
- 官網存在某個生成模型，不代表目前 V2 已完成對應適配。

## PDF 與附件

Cherry Studio V2 會先在本機擷取 PDF 文字，再將擷取結果傳送給對話模型：

- 文字型 PDF 通常可以直接處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會占用模型上下文和 Token；
- PDF 中的圖片需要單獨傳送給視覺模型。

無問芯穹是雲端服務。上傳文件、圖片或知識庫內容前，應確認符合隱私、著作權和組織安全要求。

## 計費與限流

GenStudio 的 API 呼叫會受到帳戶服務等級、模型價格和頻率限制影響。平台可能同時限制：

- RPM：每分鐘請求數；
- RPD：每天請求數；
- TPM：每分鐘 Token 數；
- 包並行服務的並行槽位。

目前的計費與限制可能會隨時間調整。自動工作上線前應：

1. 查看最新計費規則；
2. 確認帳戶餘額；
3. 設定並行和重試上限；
4. 監控 Token 用量；
5. 遇到 429 時採用退避重試；
6. 保留回應的 `id` 和 `traceresponse` 以便疑難排解。

不要透過建立多個 Key 來規避租戶層級限制；同一租戶下的 Key 可能共用額度。

## 常見問題

### 傳回 401

API Key 錯誤、已刪除、複製時帶入空格，或請求未正確使用 Bearer 驗證。重新複製或建立 Key。

### 傳回 403

帳號、租戶或目標模型沒有權限。檢查模型是否需要申請、帳戶狀態和目前租戶。

### 傳回 404

API Host、介面路徑或 Model ID 錯誤。恢復內建預設位址，並從服務清單複製完整的 Model ID。

### 傳回 429

已達到 RPM、RPD、TPM 或包並行限制。降低並行數、縮短上下文並等待恢復。

### 傳回 400

模型不支援目前的參數、圖片格式或思考設定。清除自訂參數，恢復預設思考設定後重新測試。

### 模型清單是空的

檢查 API Key、API Host、網路 Proxy 和租戶權限。也可以從服務清單複製 Model ID 後手動新增。

### 預設模型無法呼叫

V2 內建候選項目可能已經下架、重新命名或不在目前帳號權限內。同步最新清單並刪除失效模型。

### 包並行模型呼叫失敗

確認購買狀態仍然有效，並使用平台分配的完整專屬 Model ID；不要移除 `pro-` 前綴。

### Embedding 模型出現在對話清單

檢查模型類型標記。Model ID 應包含平台提供的完整名稱，並在模型管理中設為 Embedding，而不是一般對話模型。

### Rerank 健康檢查未執行

目前 V2 的通用模型連線檢查會略過 Rerank。應在知識庫檢索流程中實際驗證重排請求。

### 上傳檔案後傳回不支援

先確認檔案已成功擷取文字，再檢查目前的對話模型是否支援對應輸入。掃描 PDF 需要 OCR，圖片需要視覺模型。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。無問芯穹目前的功能與設定請參閱[GenStudio API 快速整合](https://docs.infini-ai.com/gen-studio/api/get-started/)、[Cherry Studio 整合教學](https://docs.infini-ai.com/gen-studio/integrations/use-cherrystudio.html)、[預設模型清單](https://docs.infini-ai.com/gen-studio/models/supported-models.html)、[Rerank 教學](https://docs.infini-ai.com/gen-studio/api/retrieval/tutorial-rerank.html)、[計費規則](https://docs.infini-ai.com/gen-studio/api/usage-and-billing/billing.html)和[呼叫限制](https://docs.infini-ai.com/gen-studio/api/usage-and-billing/rate-limit.html)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
