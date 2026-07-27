# 華為雲 ModelArts Studio（MaaS）

華為雲 ModelArts Studio（MaaS）提供內建模型和自訂部署模型的推論 API。Cherry Studio V2 目前沒有內建「華為雲」服務商，需要建立一個 **OpenAI 相容自訂服務商**。

{% hint style="info" %}
舊教學要求將完整的 `/chat/completions` 位址填入 API Host 並附加 `#`。V2 不需要這種歷史相容寫法，應從完整呼叫位址中移除 `/chat/completions`，只保留 Base URL。
{% endhint %}

## 先選擇接入方式

華為雲 MaaS 常見兩類呼叫方式：

| 方式 | 位址特徵 | Cherry Studio 設定 |
| --- | --- | --- |
| MaaS 標準 API | 多個內建模型共用 `/v1` 或 `/v2` Base URL | 通常一個自訂服務商即可 |
| 自訂即時推論服務 | 每個服務可能有獨立 URL、Endpoint 或路徑 | 不同 Base URL 需要分別建立服務商 |

本文只適用於使用 Bearer API Key 的 OpenAI 相容 MaaS 服務。舊版 ModelArts 的 IAM Token、AppKey/AppSecret、AppCode 或簽章驗證不能直接填入 Cherry Studio 的一般 API Key 輸入欄位。

## 地區與版本

MaaS 的可用地區、API Key 和模型清單彼此關聯，不能跨地區混用。

華為雲目前國際站文件中的 MaaS Standard API V2 範例為：

```text
https://api-ap-southeast-1.modelarts-maas.com/v2/chat/completions
```

在 Cherry Studio 中應填寫：

```text
https://api-ap-southeast-1.modelarts-maas.com/v2
```

MaaS Standard API V1 已不再持續演進。新設定應優先使用控制台提供的 V2 位址；現有 V1 服務仍應以控制台「呼叫說明」為準。

{% hint style="warning" %}
不要直接照抄本文的範例位址。先在自己的華為雲地區和服務頁面查看呼叫說明；如果控制台提供的網域或版本不同，應使用控制台位址。
{% endhint %}

## 開通 MaaS

1. 註冊並登入[華為雲](https://auth.huaweicloud.com/authui/login)；
2. 切換至 MaaS 目前支援的地區；
3. 開啟 ModelArts Studio（MaaS）；
4. 依控制台提示完成 IAM 授權；
5. 在模型廣場選擇模型；
6. 開通內建服務，或部署為即時推論服務；
7. 等待服務狀態變為可呼叫。

自訂部署會使用運算和儲存資源並產生費用。不要在不了解計費方式的情況下選擇「全部部署」。

## 建立 API Key

### 內建 MaaS 服務

1. 開啟 MaaS 的 API Key 管理；
2. 點選**建立 API Key**；
3. 設定標籤；
4. 視需要設定 IP、模型或自訂 Endpoint 白名單；
5. 建立後立即複製並保存。

### 自訂即時推論服務

1. 開啟 `模型推論 → 即時推論 → 我的服務`；
2. 找到正在執行的服務；
3. 選擇`更多 → 查看呼叫說明`；
4. 點選**建立 API Key**；
5. 設定權限並複製 Key；
6. 同時複製完整的 API URL 和模型參數。

MaaS Key 建立後可能需要幾分鐘才會生效。

{% hint style="danger" %}
API Key 只會在建立時顯示一次。不要寫入聊天、文件、程式碼儲存庫或問題截圖；遺失或外洩後應刪除並重新建立。
{% endhint %}

## 從完整 URL 擷取 Base URL

假設控制台提供的完整位址是：

```text
https://example.com/v2/chat/completions
```

Cherry Studio 應填寫：

```text
https://example.com/v2
```

處理規則：

1. 刪除末尾的 `/chat/completions`；
2. 保留 `/v1` 或 `/v2`；
3. 不附加 `#`；
4. 不將模型名稱拼接至 URL；
5. 不將控制台網頁 URL 當作 API URL。

如果自訂服務的呼叫說明使用不同路徑，應先確認它相容於 OpenAI Chat Completions。非相容介面無法只靠刪除路徑接入。

## 在 Cherry Studio 建立自訂服務商

1. 開啟 `設定 → 模型服務`；
2. 點選**新增服務商**；
3. 輸入名稱，例如 `Huawei Cloud MaaS`；
4. 選擇 **OpenAI 相容**類型；
5. 貼上 MaaS API Key；
6. 填寫擷取後的 Base URL；
7. 開啟服務商開關；
8. 同步模型或手動新增 Model ID；
9. 只啟用準備使用的模型；
10. 執行模型健康檢查。

如果所有模型共用同一個 MaaS Standard API Base URL，可以放在同一個服務商中。只有 Base URL、驗證或 Proxy 路徑不同時，才需要另外建立服務商。

## 取得與同步模型

MaaS 標準 API 提供模型清單介面：

```text
GET /v1/models
GET /v2/models
```

具體使用哪個版本取決於控制台提供的 Base URL。

同步後：

1. 檢查傳回的 Model ID；
2. 套用同步結果；
3. 確認模型類型；
4. 逐一執行健康檢查。

如果自訂服務未提供模型清單介面：

1. 在「呼叫說明」中複製 `model` 參數；
2. 在 Cherry Studio 手動新增；
3. 保持大小寫與標點完全一致；
4. 執行健康檢查。

{% hint style="warning" %}
API Key 可以設定模型和自訂 Endpoint 白名單。模型存在但傳回 401 時，應同時檢查 Key 權限，而不只是重新複製 Key。
{% endhint %}

## 對話模型

MaaS 標準 API 使用 OpenAI 相容 Chat Completions。

建議依下列順序測試：

1. 傳送一則簡短的純文字訊息；
2. 檢查串流輸出；
3. 增加系統提示詞；
4. 測試較長的上下文；
5. 再測試思考、圖片和工具呼叫。

不同模型允許的 `role`、上下文長度和輸出參數不同。遇到 400 時，應對照該模型的 MaaS API 呼叫規範。

## 思考模式

華為雲 MaaS 上的不同模型可能使用：

- `reasoning_content`
- `thinking`
- `chat_template_kwargs`
- 模型專屬開關

Cherry Studio 目前沒有華為雲專用參數適配。V2 為一般 OpenAI 相容服務商產生的思考參數，未必與某個 MaaS 模型完全一致。

如果開啟思考後發生錯誤：

1. 將思考設定恢復為**預設**；
2. 清除模型自訂參數；
3. 先確認一般對話可用；
4. 查看 MaaS 中該模型的請求範例；
5. 只新增官方明確要求的參數。

不要將一個模型的 `chat_template_kwargs` 複製給其他模型。

## 視覺與多模態

只有 MaaS 明確標記為視覺或多模態的模型才能接收圖片。

測試時：

1. 新增準確的 Model ID；
2. 確認 Cherry Studio 顯示圖片能力；
3. 先上傳一張小圖片；
4. 檢查模型是否確實理解內容；
5. 再嘗試多張圖片或大型檔案。

即使自訂即時服務部署了視覺模型，也必須使用 OpenAI 相容的圖片訊息格式，才能直接從 Cherry Studio 接入。

## MCP 與工具呼叫

MaaS Standard API V2 的部分模型支援 Tool Calling，但最終能力取決於模型。

1. 先完成一般對話；
2. 只啟用一個簡單的 MCP 工具；
3. 明確要求呼叫；
4. 檢查是否產生結構化呼叫；
5. 確認工具結果能夠傳回給模型；
6. 再增加工具。

模型只用文字描述「將要呼叫工具」不等於真實呼叫。應檢查模型、API 版本和工具格式。

## Embedding、Rerank 與圖片生成

Cherry Studio 目前沒有華為雲專用的 Embedding、Rerank 或圖片生成適配。

只有符合下列條件時才應嘗試：

1. MaaS 服務提供對應的 OpenAI 相容介面；
2. Cherry Studio 能夠為模型選擇正確的 Endpoint Type；
3. 請求和回應格式與 V2 相容；
4. 健康檢查或實際小型樣本測試通過。

不要因為 MaaS 控制台支援某種模型，就假設 Cherry Studio 知識庫或繪畫頁面已經接入。

對於知識庫，最穩妥的做法是使用已由 V2 明確支援的 Embedding 與 Rerank 服務商；對於圖片生成，則使用繪畫頁面實際列出的服務商和模型。

## PDF 與附件

目前 V2 會先在本機擷取 PDF 文字，再傳送給 MaaS 對話模型：

- 文字型 PDF 通常可以處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會占用模型上下文並產生費用；
- PDF 中的圖片需要單獨傳送給視覺模型。

這不等同於華為雲原生檔案上傳或文件理解 API。

上傳文件、圖片或知識庫內容前，應確認符合資料地區、隱私和組織安全要求。

## 自訂即時服務

自訂即時服務還需要注意：

- 服務是否正在執行；
- 資源池和 OBS 是否與 MaaS 位於同一地區；
- Endpoint 是否在 Key 白名單中；
- 是否已開啟內容審核；
- QPS 和逾時；
- 運算與儲存費用；
- 服務升級或停止狀態。

如果每個自訂服務的 Base URL 不同，應為每個 URL 分別建立服務商。多個模型共用同一個標準 Base URL 時，不需要重複建立。

## 常見問題

### 傳回 401

API Key 錯誤、尚未生效、地區不符，或 IP、模型、Endpoint 不在 Key 白名單中。檢查 Key 權限後重試。

### 傳回 403

IAM 授權、模型權限、內容審核或帳戶狀態受限。前往 MaaS 控制台查看具體錯誤碼。

### 傳回 404

Base URL、API 版本、路徑或 Model ID 錯誤。重新從「查看呼叫說明」複製完整 URL，並依規則刪除 `/chat/completions`。

### 傳回 429

已達到 MaaS、模型或自訂即時服務的 QPS / 並行限制。降低並行數並等待恢復。

### 傳回 400

模型不接受目前的訊息角色、附件或思考參數。先清除自訂參數並測試最小化的純文字請求。

### 模型清單是空的

自訂服務可能未提供 `/models`。從呼叫說明複製 `model` 參數後手動新增。

### Key 剛建立就提示無效

MaaS Key 可能需要幾分鐘才會生效。確認 Key、地區和 Base URL 後稍候再試。

### 每個模型都要建立服務商嗎

不一定。共用同一個 MaaS Standard API Base URL 和 Key 的模型可以放在同一個服務商；只有呼叫位址或驗證不同時才需要拆分。

### 舊教學為什麼要求附加 `#`

那是舊版 Cherry Studio 使用完整介面位址時的歷史相容方式。V2 應填寫移除 `/chat/completions` 後的 Base URL，不再附加 `#`。

### 自訂服務在網頁中可以呼叫，但 Cherry Studio 無法使用

該服務可能使用非 OpenAI 格式、舊版 AppCode/簽章驗證、自訂路徑，或 Key 白名單未包含 Endpoint。一般自訂服務商無法自動適配這些差異。

### 開啟思考後發生參數錯誤

恢復預設思考設定。目前 V2 沒有華為雲 MaaS 專用的思考參數適配。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。華為雲 MaaS 目前的呼叫方式請參閱[API 呼叫規範](https://support.huaweicloud.com/intl/zh-cn/model-call-maas/model-call-017.html)、[MaaS Standard API V2](https://support.huaweicloud.com/intl/zh-cn/model-call-maas/model-call-019.html)、[呼叫模型服務](https://support.huaweicloud.com/intl/zh-cn/inference-maas/maas-modelarts-0011.html)和[API URL 格式說明](https://support.huaweicloud.com/intl/zh-cn/maas_faq/maas_faq_0005.html)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
