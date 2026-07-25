# 阿里雲百煉

阿里雲百煉（Alibaba Cloud Model Studio）提供千問和多家第三方模型。Cherry Studio V2 內建百煉服務商，支援 OpenAI 相容對話、Anthropic 相容呼叫、Embedding、Rerank，以及專用的圖片生成和編輯鏈路。

V2 的華北 2（北京）預設位址為：

| 協定 | 預設 Base URL |
| --- | --- |
| OpenAI 相容 | `https://dashscope.aliyuncs.com/compatible-mode/v1/` |
| Anthropic 相容 | `https://dashscope.aliyuncs.com/apps/anthropic` |

{% hint style="info" %}
百煉的 API Key、Base URL 和模型清單依地區隔離，不能跨地區混用。北京 Key 搭配新加坡位址，或新加坡 Key 搭配北京位址，通常會傳回 401。
{% endhint %}

## 使用前準備

首次使用百煉 API，通常需要：

1. 註冊並登入阿里雲帳號；
2. 完成帳號實名驗證；
3. 開通阿里雲百煉；
4. 選擇準備使用的地區；
5. 建立 API Key；
6. 確認帳戶餘額、免費額度或訂閱權益；
7. 記錄對應的業務空間 ID。

模型、價格、免費額度和地區可用性會調整。本文不固定列出費用，請以[百煉模型清單](https://help.aliyun.com/zh/model-studio/models)和控制台帳單為準。

## 選擇地區與 Base URL

百煉正在推廣業務空間專屬網域。它通常比舊 DashScope 公共網域更穩定，並且需要將 `{WorkspaceId}` 替換為實際的業務空間 ID。

常見 OpenAI 相容位址：

| 地區 | Base URL |
| --- | --- |
| 華北 2（北京）預設 | `https://dashscope.aliyuncs.com/compatible-mode/v1/` |
| 華北 2（北京）專屬網域 | `https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1/` |
| 新加坡 | `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/` |
| 日本（東京） | `https://{WorkspaceId}.ap-northeast-1.maas.aliyuncs.com/compatible-mode/v1/` |
| 德國（法蘭克福） | `https://{WorkspaceId}.eu-central-1.maas.aliyuncs.com/compatible-mode/v1/` |
| 美國（維吉尼亞） | `https://dashscope-us.aliyuncs.com/compatible-mode/v1/` |

對應的 Anthropic 相容位址通常會將末尾路徑替換為 `/apps/anthropic`。不同模型支援的地區和協定可能不同，應從模型詳細資料頁複製位址，不要根據模型名稱推測。

{% hint style="warning" %}
不要將 `{WorkspaceId}` 原樣填入 Cherry Studio。業務空間 ID 可以在百煉的業務空間管理頁面查看，通常類似 `llm-...`。
{% endhint %}

## 取得 API Key

1. 開啟[百煉 API Key 管理](https://bailian.console.aliyun.com/?tab=model#/api-key)；
2. 在頁面右上角確認目標地區；
3. 點選**建立 API Key**；
4. 選擇所屬業務空間；
5. 選擇全部權限，或依組織要求設定 IP 白名單和模型範圍；
6. 填寫容易識別的描述；
7. 建立後立即複製並妥善保存。

新建立的按量付費 Key 可能以 `sk-ws` 開頭，並且只會在建立時顯示一次；舊版 `sk-` Key 仍可能繼續使用。

{% hint style="danger" %}
API Key 相當於帳戶認證資料。不要寫入聊天、文件、程式碼儲存庫或問題截圖；外洩後應立即在百煉控制台重設或刪除。
{% endhint %}

## 在 Cherry Studio 設定

### 使用北京預設位址

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **Bailian / 阿里雲百煉**；
4. 貼上北京地區的 API Key；
5. 保留 OpenAI Base URL `https://dashscope.aliyuncs.com/compatible-mode/v1/`；
6. 開啟頁面頂部的服務商開關；
7. 點選**新增**或同步模型；
8. 檢查同步預覽並套用變更；
9. 只啟用準備使用的模型；
10. 執行模型健康檢查。

### 使用其他地區或專屬網域

1. 在百煉控制台複製目標業務空間的 API Host；
2. 在 Cherry Studio 將 OpenAI Base URL 改為對應的 `/compatible-mode/v1/` 位址；
3. 如果要使用 Anthropic 相容工作流程，同時更新 Anthropic Base URL；
4. 使用**同一地區、同一計費方案**下建立的 API Key；
5. 重新同步模型；
6. 對每個模型執行健康檢查。

V2 會從使用者設定的 OpenAI Base URL 推導圖片介面主機。因此，改用專屬網域後，圖片請求也會跟隨該網域，而不會強制返回北京公共網域。

## 同步與新增模型

百煉的模型範圍會頻繁更新，V2 內建清單只用於首次顯示。同步時應以百煉目前傳回的結果為準。

建議：

1. 先確認地區與 Key 相符；
2. 同步模型；
3. 查看新增、更新和移除項目；
4. 套用同步結果；
5. 檢查模型能力標籤；
6. 刪除自己手動保留的過期模型；
7. 逐一執行健康檢查。

如果同步結果不完整，可以從百煉模型頁複製完整的 Model ID 後手動新增。大小寫、斜線和版本後綴都屬於 ID，例如第三方模型可能帶有組織前綴。

{% hint style="warning" %}
模型出現在 V2 預設或另一個地區，不代表目前的 API Key 有權呼叫。最終權限由百煉伺服器端、業務空間權限和地區模型清單共同決定。
{% endhint %}

## 對話模型

一般聊天使用 OpenAI 相容 Chat Completions。

建議依下列順序測試：

1. 傳送一則簡短的純文字訊息；
2. 檢查串流輸出；
3. 增加系統提示詞；
4. 測試較長的上下文；
5. 再測試圖片、思考和工具呼叫。

百煉同時提供千問和第三方模型。經由百煉呼叫同一廠商的模型時，也應使用百煉模型頁提供的 Model ID 和參數，不要照搬其他平台的 ID。

## Anthropic 相容與 Code Tools

百煉提供 Anthropic 相容 Messages API，可用於支援自訂 Anthropic 位址的程式設計工具或 Agent 工作流程。

在 Cherry Studio 中：

1. 確認目標模型支援 Anthropic 相容協定；
2. 填寫與地區對應的 Anthropic Base URL；
3. 保持 API Key 與地區一致；
4. 先執行一般對話；
5. 再於 Code Tools 或 Agent 情境中測試。

OpenAI 與 Anthropic 相容位址不是同一條路徑。只修改 OpenAI Base URL，不會自動保證 Anthropic 工作流程指向同一地區。

## 思考模式

百煉上的千問、DeepSeek、GLM、Kimi 等模型可能使用不同的思考參數。Cherry Studio V2 會依模型系列適配 `enable_thinking`、思考預算等參數。

如果開啟思考後發生錯誤：

1. 將思考設定恢復為**預設**；
2. 清除模型自訂參數；
3. 確認使用的是目前的 Model ID；
4. 查看該模型在目前地區的官方範例；
5. 重新執行健康檢查。

有些模型只能開啟或關閉思考，不能選擇 `low`、`medium`、`high` 等強度。不要將其他平台的推論參數直接複製到百煉。

## 視覺與多模態

只有明確支援圖片、音訊或影片輸入的模型才能接收對應附件。

測試視覺模型時：

1. 同步最新的 Model ID；
2. 確認模型顯示圖片能力；
3. 先上傳一張小圖片；
4. 檢查模型是否確實理解內容；
5. 再嘗試多張圖片、影片或高解析度檔案。

同一系列的文字版、視覺版和 Omni 版可能是不同模型。附件會增加上下文、網路耗時和費用。

## MCP 與工具呼叫

Cherry Studio MCP 要求模型支援結構化 Tool Calling。

1. 先確認一般對話正常；
2. 只啟用一個簡單的 MCP 工具；
3. 明確要求呼叫；
4. 檢查是否產生結構化呼叫；
5. 確認工具結果能夠傳回給模型；
6. 再增加工具。

模型用文字描述「將要呼叫工具」不等於真實呼叫。出現這種情況時，應檢查模型能力、協定、提示詞和工具定義。

## Embedding、Rerank 與知識庫

百煉提供文字與多模態 Embedding，以及文字和多模態 Rerank。目前模型頁的推薦項目可能包括：

- 文字 Embedding：`text-embedding-v4`；
- 文字 Rerank：`qwen3-rerank`；
- 多模態 Embedding：`qwen3-vl-embedding`；
- 多模態 Rerank：`qwen3-vl-rerank`。

這些是平台範例，不是永久清單。`gte-rerank` 已於 2026 年 5 月 30 日下架，不應繼續依舊教學設定。

建立知識庫時：

1. 新增目前可用的 Embedding 模型；
2. 確認 Cherry Studio 將其識別為嵌入模型；
3. 偵測向量維度；
4. 執行健康檢查；
5. 再新增並測試 Rerank 模型；
6. 匯入少量文件試執行；
7. 確認檢索與重排結果後再批次匯入。

Embedding 模型或向量維度一旦用於現有知識庫，就不應直接更換；否則通常需要重新建立向量索引。

百煉不同地區的 Rerank 端點和能力可能不同。如果模型可以新增但重排請求失敗，應先關閉 Rerank 以確保基本檢索可用，再核對目前的 V2 版本、地區介面與模型權限。

## 圖片生成與編輯

Cherry Studio V2 為百煉實作了專用圖片傳輸鏈路：

1. 根據模型選擇原生 DashScope 圖片介面；
2. 非同步模型在請求中啟用 `X-DashScope-Async`；
3. 取得 `task_id`；
4. 輪詢工作狀態；
5. 成功後讀取圖片 URL。

V2 只會為已適配的模型顯示對應模式和參數，例如：

- 文字生成圖片；
- 圖片編輯；
- 圖片翻譯；
- 尺寸；
- Seed；
- 負面提示詞；
- 浮水印；
- 部分模型的參考圖片或功能類型。

並非百煉官網出現的每個圖片模型都已被目前的 V2 適配。應優先從 Cherry Studio 繪畫頁面可選的百煉模型開始測試。

{% hint style="warning" %}
圖片工作可能依成功輸出的張數計費。首次測試時將輸出數量設為 1，並避免在等待非同步結果時重複提交。
{% endhint %}

取消 Cherry Studio 中的等待只會停止本機輪詢；DashScope 沒有可供目前 V2 呼叫的通用工作取消介面，已提交的工作仍可能繼續執行並產生費用。

## PDF 與附件

目前 V2 會先在本機擷取 PDF 文字，再傳送給百煉對話模型：

- 文字型 PDF 通常可以處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會占用模型上下文並產生費用；
- PDF 中的圖片需要單獨傳送給視覺模型。

百煉是雲端服務。上傳文件、圖片或知識庫內容前，應確認符合隱私、資料跨境和組織安全要求；尤其要注意所選地區的資料處理範圍。

## 額度、權限與限流

百煉可能同時受到以下因素限制：

- 帳戶餘額與免費額度；
- 業務空間預算；
- Key 的 IP 白名單；
- Key 的模型權限；
- RPM / TPM；
- 並行工作數；
- 圖片工作佇列；
- 地區資源可用性。

建議在控制台設定預算和用量警示，避免多個自動工作共用同一個 Key 無限重試。

## 常見問題

### 傳回 401

API Key 錯誤、已重設，或 Key 與 Base URL 的地區不符。先確認地區，再重新複製對應的 Key。

### 傳回 403

Key 沒有模型權限、IP 不在白名單、業務空間未授權，或帳號狀態受限。檢查 Key 權限與業務空間政策。

### 傳回 404

Base URL、Workspace ID、協定路徑或 Model ID 錯誤。不要將控制台頁面 URL 當作 API 位址。

### 傳回 429

達到 RPM、TPM、並行或工作佇列限制。降低並行數、縮短上下文並等待恢復；不要立即循環重試。

### 提示餘額不足或額度用盡

檢查帳戶餘額、免費額度、業務空間預算和模型計費方式。不同模型可能使用不同的額度池。

### 模型清單是空的

檢查地區、API Key、Base URL 和網路 Proxy。也可以從目前地區的模型頁複製完整 Model ID 後手動新增。

### 預設模型無法使用

V2 預設可能早於百煉模型下架或地區變更。重新同步，並以目前地區的模型清單為準。

### 一般聊天可用，但 Agent 或 Code Tools 無法使用

檢查 Anthropic Base URL 是否仍指向北京預設位址，以及目標模型是否支援 Anthropic 相容協定和工具呼叫。

### 圖片生成傳回的位址錯誤

檢查 OpenAI Base URL 是否包含正確的業務空間網域和 `/compatible-mode/v1/` 後綴。V2 會從它推導原生圖片介面主機。

### 圖片工作持續等待

工作可能仍在佇列中、輪詢網路失敗、額度不足或模型忙碌。先查看錯誤資訊和百煉工作狀態，不要重複提交。

### 可以選擇 Rerank 模型，但沒有生效

先確認模型未下架、地區介面相容，並檢查知識庫是否確實啟用了 Rerank。必要時暫時關閉重排，先驗證 Embedding 檢索。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。百煉目前的地區、Key 與模型請參閱[地區與接入網域](https://help.aliyun.com/zh/model-studio/regions/)、[取得 API Key](https://help.aliyun.com/zh/model-studio/get-api-key/)、[選擇模型](https://help.aliyun.com/zh/model-studio/models)、[向量與重排序](https://help.aliyun.com/zh/model-studio/embedding-rerank-model/)和[圖片生成與編輯](https://help.aliyun.com/zh/model-studio/image-model)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
