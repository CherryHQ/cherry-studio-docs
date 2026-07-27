# MiniMax Token Plan（原 Coding Plan）

MiniMax 已將 Coding Plan 升級為 **Token Plan**。它面向個人開發者、AI 程式設計和日常高頻使用，可透過訂閱額度或 Credits 呼叫 MiniMax 模型。

Cherry Studio V2 沒有單獨的「Coding Plan」服務商。你需要在內建的 **MiniMax** 或 **MiniMax Global** 服務商中填入 Token Plan 專用 Key。

{% hint style="info" %}
本頁路徑是為了相容舊文件而保留。MiniMax 平台中的實際產品名稱、方案和額度應以目前的 **Token Plan** 頁面為準，不要繼續套用舊教學中的 M2.1、固定月費或「每 5 小時 40 次」等過時資訊。
{% endhint %}

## Token Plan 與一般 API 的差異

| 項目 | Token Plan | 一般按量 API |
| --- | --- | --- |
| Key 來源 | Token Plan / 訂閱管理 | 介面金鑰 |
| 常見 Key | `sk-cp...` | 一般 API Key |
| 計量方式 | 方案額度、Credits、滾動視窗 | 按實際 API 用量計費 |
| 有效期間 | 取決於訂閱、席位或 Credits | 取決於帳戶餘額和 Key 狀態 |
| 適用情境 | 個人互動、程式設計工具、日常使用 | 正式環境整合、穩定按量呼叫 |

兩類 Key **不互通**。將一般 API Key 用於 Token Plan，或將 Token Plan Key 當作一般按量 Key，可能會傳回 401、額度錯誤或採用錯誤的計費方式。

MiniMax 官方建議正式環境優先使用按量 API。Token Plan 可能有 RPM、TPM、滾動視窗、每週額度和尖峰時段動態限流，不適合作為無上限的批次服務。

## 選擇中國大陸或國際平台

| 帳號與訂閱 | Cherry Studio 服務商 | OpenAI Base URL | Anthropic Base URL |
| --- | --- | --- | --- |
| 中國大陸 MiniMax 平台 | MiniMax | `https://api.minimaxi.com/v1` | `https://api.minimaxi.com/anthropic` |
| MiniMax 國際平台 | MiniMax Global | `https://api.minimax.io/v1` | `https://api.minimax.io/anthropic` |

中國大陸站和國際站的帳號、Key 與 Base URL 不應混用。判斷依據是購買 Token Plan 和建立 Key 的平台，而不是目前所在的地區。

## 取得 Token Plan Key

### 中國大陸平台

1. 登入 [MiniMax 開放平台](https://platform.minimaxi.com/)；
2. 開啟 [Token Plan](https://platform.minimaxi.com/subscribe/token-plan)；
3. 購買方案、兌換權益或確認 Team 已指派席位；
4. 前往介面金鑰；
5. 選擇**建立 Token Plan Key**；
6. 複製新的 Key 並妥善保存。

### 國際平台

1. 登入 [MiniMax API Platform](https://platform.minimax.io/)；
2. 開啟 [Token Plan](https://platform.minimax.io/subscribe/token-plan)；
3. 購買方案、Credits 或確認 Team 席位；
4. 前往 API Keys；
5. 建立 **Token Plan Key**；
6. 複製新的 Key 並妥善保存。

{% hint style="danger" %}
不要將 Token Plan Key 寫入聊天、文件、程式碼儲存庫或問題截圖。Key 外洩後可能會消耗訂閱額度或 Credits；應立即在 MiniMax 平台刪除並重新建立。
{% endhint %}

只看 `sk-cp` 前綴不足以證明 Key 可用。還要確認訂閱有效、席位已指派、Credits 可用，並且 Key 來自正確的平台。

## 在 Cherry Studio 設定

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 中國大陸帳號選擇 **MiniMax**，國際帳號選擇 **MiniMax Global**；
4. 在 API Key 中貼上 Token Plan Key；
5. 檢查 Base URL 是否與帳號平台相符；
6. 開啟頁面頂部的服務商開關；
7. 點選**新增**或同步模型；
8. 檢查同步預覽並套用變更；
9. 只啟用目前方案允許使用的模型；
10. 執行模型健康檢查。

Cherry Studio 的 MiniMax 預設同時保留 OpenAI 與 Anthropic 相容位址。一般對話預設使用 OpenAI 相容鏈路，部分 Code Tools 可以使用 Anthropic 相容鏈路。

更多協定、視覺、思考、MCP 和 PDF 邊界請參閱 [MiniMax](minimax.md)。

## 選擇模型

Cherry Studio V2 目前的 MiniMax 預設包含：

- `MiniMax-M3`
- `MiniMax-M2.7`
- `MiniMax-M2.7-highspeed`

MiniMax Token Plan 的可用模型會隨方案和產品升級而變更。請以訂閱頁面、帳戶用量頁和實際模型同步結果為準。

建議：

1. 優先測試目前方案主推的 `MiniMax-M3`；
2. 需要相容舊有工作流程時，再測試 `MiniMax-M2.7`；
3. 只有方案明確包含高速模型時，才使用 `MiniMax-M2.7-highspeed`；
4. 不要手動新增舊版 `MiniMax-M2.1` 並假設它仍包含在方案中；
5. 同名模型在 Token Plan 與按量 API 下可能採用不同的額度規則。

{% hint style="warning" %}
模型出現在 Cherry Studio 預設或同步清單中，不代表你的 Token Plan 一定包含該模型。最終權限由 MiniMax 伺服器端判定。
{% endhint %}

## 思考、視覺與 MCP

### 思考

MiniMax M 系列會傳回思考內容。Cherry Studio 需要保留多輪對話中的思考區塊和工具呼叫資訊，才能維持後續請求的上下文連續性。

如果修改思考選項後傳回參數錯誤，請先恢復為**預設**並重試。Token Plan Key 不會改變模型本身接受的參數。

### 視覺

Token Plan 已擴展至多模態模型，但 Cherry Studio 目前能否直接傳送圖片，仍取決於具體的模型 ID 和 V2 的能力識別。

同步後確認模型顯示圖片能力，再使用小圖片測試。如果 `MiniMax-M3` 的視覺能力尚未被目前的 V2 正確識別，不要只修改顯示名稱來繞過限制。

### MCP

Cherry Studio MCP 使用模型的 Tool Calling。MiniMax Token Plan 另外提供官方 Web Search 和 Understand Image MCP，但它們與 Cherry Studio 自行設定的 MCP 伺服器不是同一個概念。

使用 Cherry Studio MCP 時：

1. 先完成一般對話；
2. 只啟用一個簡單工具；
3. 檢查模型是否確實產生結構化呼叫；
4. 再增加更多工具。

需要 MiniMax 官方 Token Plan MCP 時，應依照官方指南單獨設定，並注意它會消耗對應的方案資源。

## 查看用量

最可靠的方式是開啟 MiniMax 平台的 Token Plan 或訂閱管理頁面，查看：

- 目前方案或 Team 席位；
- 剩餘額度與 Credits；
- 各模型用量；
- 滾動視窗恢復時間；
- 週期額度；
- 高速模型資格；
- 訂閱到期時間。

不要只根據 Cherry Studio 的成功請求數來估算餘量。長上下文、視覺、生成類模型和不同模型可能會使用不同的額度池。

## 限額與 429

Token Plan 可能同時存在：

- RPM / TPM 短期限流；
- 5 小時滾動視窗；
- 每週額度；
- 多模態模型的獨立額度；
- 尖峰時段動態限流；
- 方案並行限制。

因此，`429 Too Many Requests` 不一定表示整個訂閱額度已用盡。

疑難排解順序：

1. 暫停一分鐘後重試；
2. 查看 Token Plan 用量頁；
3. 檢查滾動視窗和每週額度；
4. 減少並行、長上下文和自動重試；
5. 確認沒有多人共用同一個個人 Key；
6. 必要時升級方案或改用按量 API Key。

在同一個服務商中直接替換為一般 API Key，會改變額度和計費來源。操作前先確認帳戶餘額與預算。

## 常見問題

### 傳回 401

Key 錯誤、已刪除、訂閱到期、席位失效，或中國大陸與國際 Base URL 混用。請重新從對應平台複製 Token Plan Key。

### 傳回 403

目前方案、Team 政策或模型權限不允許該請求。檢查 Token Plan 權益和模型範圍。

### 傳回 404

Base URL、協定路徑或模型 ID 錯誤。恢復 MiniMax / MiniMax Global 預設位址，並重新同步模型。

### 傳回 429

可能是分鐘級限流、滾動視窗、每週額度或尖峰時段動態限流。請以 Token Plan 用量頁為準，不要只是一再傳送請求。

### 一般模型可用，但高速模型無法使用

目前方案可能不包含高速權益，或高速資源當下不可用。改用標準模型並檢查方案說明。

### 模型清單仍顯示舊模型

重新同步並檢查服務商是否連線至正確的平台。手動保留的舊模型不代表目前方案自動支援該模型。

### Key 檢查成功，但對話消耗了餘額

可能填入的是一般按量 API Key，而不是 Token Plan Key。立即檢查 MiniMax 帳單與 Key 類型。

### 用於正式環境後頻繁遭到限流

Token Plan 面向個人互動和開發工作流程。正式環境、批次或高並行服務應改用按量 API，並設定預算、監控和重試策略。

MiniMax Token Plan 目前的方案、模型和用量規則請參閱[中國大陸文件](https://platform.minimaxi.com/docs/token-plan/quickstart)或[國際文件](https://platform.minimax.io/docs/token-plan/quickstart)。一般服務商設定請參閱 [MiniMax](minimax.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
