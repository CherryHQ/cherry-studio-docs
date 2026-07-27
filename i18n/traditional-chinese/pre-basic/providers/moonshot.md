---
icon: moon
---

# Moonshot AI (Kimi)

Cherry Studio V2 的 Moonshot AI 內建範本用於連線 Kimi API 開放平台。範本預設使用 OpenAI Chat Completions 通訊協定，同時提供 Moonshot 的 Anthropic 相容端點。

目前的 Kimi 模型涵蓋一般對話、長程程式設計、視覺理解和 Agent 等情境。不同世代的模型使用不同的思考參數，設定時應先確認模型 ID，再選擇 Cherry Studio 中的思考選項。

{% hint style="info" %}
Kimi 網頁版、Kimi 會員、Kimi Code 與 Kimi API 開放平台是不同產品。網頁版或會員登入狀態不會自動寫入 Cherry Studio；透過 Cherry Studio 呼叫需要另外建立 API Key，並依開放平台規則計費。
{% endhint %}

## 開始前的準備

- 可登入 [Kimi API 開放平台](https://platform.kimi.com/)的帳戶；
- 在 [API Keys](https://platform.moonshot.cn/console/api-keys) 建立的 API Key；
- 帳戶具有目標模型所需的餘額和存取權限；
- 已查看目前的[模型列表](https://platform.kimi.com/docs/models)和參數限制。

建議為 Cherry Studio 單獨建立 Key，以便區分用量和撤銷權限。

## 設定 Moonshot AI

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，選擇 **月之暗面**；
3. 輸入 Kimi API Key；
4. 保留預設 Base URL `https://api.moonshot.cn`；
5. 開啟頁面頂端的服務商開關；
6. 在模型列表點選**新增**，檢查同步預覽並套用變更；
7. 只啟用準備使用的模型。

{% hint style="danger" %}
不要把 API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。金鑰洩漏後應立即在開放平台刪除並重新建立。
{% endhint %}

官方 SDK 文件中的位址通常寫成 `https://api.moonshot.cn/v1`。Cherry Studio 範本會處理介面路徑，因此使用內建範本時保留頁面中的預設位址即可，不要重複附加請求路徑。

## 選擇模型

以實際同步列表為準。目前主要模型可依以下方式選擇：

| 模型 ID | 主要用途 | Cherry Studio 使用提示 |
| --- | --- | --- |
| `kimi-k3` | 旗艦通用模型，1M 上下文，適合長程程式設計、知識工作和複雜推理 | 目前 V2 建議將思考保持為**預設** |
| `kimi-k2.7-code` | 256K 上下文的程式設計與 Agent 模型 | 一律思考，保持**預設** |
| `kimi-k2.7-code-highspeed` | 與 K2.7 Code 同系列、輸出更快 | 資源忙碌時可能波動 |
| `kimi-k2.6` | 256K 上下文，適合一般對話、視覺和 Agent | 可使用預設思考，或視需要關閉 |

Kimi K3、K2.7 Code 與 K2.6 官方均支援文字、圖片和影片輸入；特定附件入口還取決於目前的 Cherry Studio 版本能否正確識別模型能力。

模型名稱、存取條件和生命週期會發生變化。不要只根據舊截圖手動輸入模型 ID；請優先重新點選**新增**同步列表，並以 Kimi 官方文件為準。

## 設定思考模式

Kimi 不同模型系列使用不同的推理參數：

- Kimi K3 一律開啟思考，透過頂層 `reasoning_effort` 使用 `low`、`high` 或 `max`，預設為 `max`；
- Kimi K2.7 Code 一律開啟思考，不支援關閉；
- Kimi K2.6 使用 `thinking` 控制開啟或關閉思考。

{% hint style="warning" %}
目前的 Cherry Studio V2 會將 Kimi K2.5 及更新模型統一識別為 Kimi 思考模型，並為非預設選項傳送 `thinking` 參數。Kimi K3 使用的是 `reasoning_effort`，K2.7 Code 又不允許關閉思考，因此使用 K3 或 K2.7 Code 時請保持**預設**，避免請求因參數不相容而傳回 400。
{% endhint %}

Kimi K3 的低、高、最高三種推理強度目前可能尚未完整顯示在 Cherry Studio 的思考選單中。保持預設時，K3 會使用服務商預設的 `max`；若必須精確控制強度，應等待 Cherry Studio 更新相應的調整。

使用 K2.6 時：

- **預設**：不覆寫服務商的預設行為；
- **關閉**：傳送停用思考參數；
- **自動**：目前的 V2 會傳送啟用思考參數。

K2.5 及更新模型具有固定或受限的取樣參數。遇到參數錯誤時，請先將溫度、Top P 和懲罰項恢復為預設值。

## 使用圖片、影片與檔案

官方模型能力與用戶端目前的識別結果需要分別確認：

1. 重新同步模型列表；
2. 選擇目標模型；
3. 檢查輸入框是否出現圖片或檔案入口；
4. 先上傳一張一般圖片進行健康測試；
5. 再測試影片或大型附件。

目前的 V2 已能自動識別 K2.6 的視覺能力；K3 和 K2.7 Code 的官方能力較新，目前版本可能暫未顯示完整的視覺標記。若附件入口沒有出現，請先更新 Cherry Studio 和模型列表；仍無法使用時，可暫時使用 `kimi-k2.6`，不要將不支援的內容強制以文字傳送。

對於 PDF，Moonshot 內建範本目前不會直接使用 Kimi 的原生檔案上傳介面。Cherry Studio 會先在本機擷取 PDF 文字，再將文字傳送給模型：

- 文字型 PDF 通常可以直接處理；
- 掃描文件可能需要先執行 OCR；
- 表格、複雜排版和圖片資訊可能在擷取時遺失；
- 擷取後的文字會占用模型輸入 Token。

## 工具呼叫與 MCP

Kimi 官方模型支援工具呼叫，但 Cherry Studio 是否顯示 MCP 能力仍取決於模型能力識別。

建議依以下順序驗證：

1. 先完成一輪一般對話；
2. 啟用一個簡單的 MCP 工具；
3. 使用明確要求呼叫工具的提示詞；
4. 確認模型實際發起呼叫；
5. 再增加多個工具或長鏈路任務。

目前的 V2 已包含 Kimi K2 系列的工具識別規則，但 K3 和 K2.7 Code 的自動識別可能落後於官方模型發布。若 MCP 入口缺失，請先更新 Cherry Studio；仍無法識別時，暫時使用已被目前版本識別的模型完成任務。

當 MCP 傳回圖片、音訊或包含大量二進位資料的資源時，Cherry Studio 會將結果轉換成文字摘要，避免 base64 內容超過 Kimi 請求大小限制。此時模型能看到工具結果的文字說明，但不能直接分析被取代的原始媒體。

## 知識庫與嵌入模型

Moonshot AI 內建範本目前設定的是對話端點，不提供嵌入模型。使用知識庫或[全域記憶](../../advanced-basic/memory.md)時：

- 對話模型可以繼續選擇 Kimi；
- 嵌入模型需要從其他服務商選擇；
- 對話模型和嵌入模型不必來自同一家服務商；
- 設定後分別執行模型健康檢查。

## 檢查連線

1. 在 API Key 區域執行連線檢查；
2. 選擇一個已同步並啟用的模型；
3. 確認檢查成功；
4. 在模型列表執行健康檢查；
5. 回到對話介面傳送一則簡單訊息；
6. 再分別測試思考、附件和 MCP。

連線檢查成功只表示基本憑證可用，不代表帳戶已取得所有模型權限，也不代表每種模型能力都已被目前的用戶端識別。

## 常見問題

### 傳回 401

API Key 無效、已刪除或複製不完整。請重新建立 Key，並確認沒有多餘空格。

### 傳回餘額或存取條件錯誤

檢查開放平台餘額、帳戶等級和目標模型的存取條件。Kimi 網頁版會員餘額不能取代 API 餘額。

### 傳回 404 或模型不存在

模型 ID 已變更、已下線或帳戶尚無權存取。重新點選**新增**同步列表，並在[模型列表](https://platform.kimi.com/docs/models)核對。

### 傳回 400 或提示 `thinking` 參數無效

如果使用 Kimi K3 或 K2.7 Code，請將思考選項改為**預設**，並將溫度、Top P 等參數恢復為預設值。K3 不接受 K2.6 使用的 `thinking` 開關。

### 傳回 429 或請求忙碌

帳戶已達並行、RPM、TPM 或 TPD 限制，或高速模型資源暫時忙碌。請降低並行請求、縮短上下文或稍後重試。

### K3 或 K2.7 Code 沒有圖片、影片或 MCP 入口

這是官方模型能力與目前 Cherry Studio 自動識別規則尚未同步的表現。更新 Cherry Studio 並重新同步模型；若仍無入口，暫時使用 K2.6，等待用戶端更新調整。

### PDF 內容識別不完整

確認 PDF 是否為掃描文件。請先執行 OCR，或將關鍵頁面轉換成圖片後，使用已被 Cherry Studio 識別為視覺模型的 Kimi 模型。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。Kimi 參數差異請參閱[模型參數參考](https://platform.kimi.com/docs/api/models-overview)；意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
