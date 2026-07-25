---
icon: bolt
---

# MiniMax

Cherry Studio V2 內建 **MiniMax CN** 與 **MiniMax** 兩個服務商。兩者都能連線 MiniMax 的語言模型介面，但使用不同的開放平台、Base URL 和 API Key。

本頁介紹如何在 Cherry Studio 中使用 MiniMax M 系列進行對話、程式設計和 Agent 任務。MiniMax 的語音、圖片、影片和音樂生成使用獨立 API，不等同於此處的語言模型服務。

{% hint style="info" %}
中國大陸開放平台請選擇 **MiniMax CN**；國際開放平台請選擇 **MiniMax**。兩個平台的帳戶、Key、餘額和訂閱可能彼此獨立，請勿混用。
{% endhint %}

## 開始前的準備

根據帳戶所在平台準備憑證：

| 平台 | Cherry Studio 服務商 | 預設 Base URL |
| --- | --- | --- |
| 中國大陸 | MiniMax CN | `https://api.minimaxi.com/v1/` |
| 國際 | MiniMax | `https://api.minimax.io/v1/` |

- 中國大陸使用者可在 [MiniMax 開放平台](https://platform.minimaxi.com/)建立 API Key；
- 國際使用者可在 [MiniMax API Platform](https://platform.minimax.io/)建立 API Key；
- 確認 Key 對應按量付費餘額或有效的 Token Plan；
- 查看目前可用的模型、上下文和速率限制。

按量付費 API Key 與 Token Plan Key 使用不同的餘額或額度。連線成功但傳回額度錯誤時，應回到建立該 Key 的對應計費頁面檢查，而不是只查看另一個帳戶的餘額。

## 設定 MiniMax

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 中國大陸帳戶選擇 **MiniMax CN**，國際帳戶選擇 **MiniMax**；
4. 輸入對應平台建立的 API Key；
5. 保留內建的預設 Base URL；
6. 開啟頁面頂端的服務商開關；
7. 在模型列表點選**新增**，檢查同步預覽並套用變更；
8. 只啟用準備使用的模型。

{% hint style="danger" %}
不要把 API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。金鑰洩漏後應立即在對應的 MiniMax 開放平台刪除並重新建立。
{% endhint %}

如果將 `.com` 平台的 Key 填入 `.io` 服務商，或反向混用，通常會傳回未授權。請優先檢查是否選對服務商項目，不要任意覆寫內建位址。

## 選擇模型

Cherry Studio V2 目前為兩個 MiniMax 服務商預設以下主要模型：

| 模型 ID | 主要用途 |
| --- | --- |
| `MiniMax-M3` | 旗艦多模態程式設計與 Agent 模型，官方提供 1M 上下文 |
| `MiniMax-M2.7` | 程式設計、工具呼叫、辦公和複雜 Agent 工作流程 |
| `MiniMax-M2.7-highspeed` | 與 M2.7 同系列，優先考慮更低輸出延遲 |

同步列表中還可能出現 M2.5、M2.1 或其他模型。模型 ID 和生命週期以實際同步結果及 MiniMax 官方文件為準，不要依賴舊文件中的 `abab` 系列名稱。

- 日常綜合任務優先嘗試 M3；
- 主要處理程式碼和工具呼叫時，可以比較 M3 與 M2.7；
- 對輸出速度敏感時選擇 `MiniMax-M2.7-highspeed`；
- 需要可重現結果時請記錄完整模型 ID，不要只記錄顯示名稱。

## OpenAI 與 Anthropic 相容端點

兩個內建服務商都包含 OpenAI Chat Completions 與 Anthropic Messages 相容位址：

| 平台 | OpenAI 相容 | Anthropic 相容 |
| --- | --- | --- |
| 中國大陸 | `https://api.minimaxi.com/v1/` | `https://api.minimaxi.com/anthropic` |
| 國際 | `https://api.minimax.io/v1/` | `https://api.minimax.io/anthropic` |

Cherry Studio 預設使用 OpenAI Chat Completions。一般對話和模型同步可以先保留預設。

MiniMax 官方更建議使用 Anthropic 相容端點處理思考區塊與交錯思考。如果你在 Cherry Studio 中手動為模型切換端點類型，應同時確認：

- Base URL 與帳戶區域相符；
- 模型使用 Anthropic Messages 通訊協定；
- Key 來自同一個平台；
- 一般對話、思考顯示和工具呼叫都重新通過健康檢查。

不要只修改 Base URL 卻保留錯誤的通訊協定類型。OpenAI 與 Anthropic 相容介面的訊息結構並不完全相同。

## 思考內容與多輪工具呼叫

MiniMax M 系列會傳回推理內容。對於 M2 系列，Cherry Studio 能識別其為推理模型；M3 發布較新，目前的 V2 可能尚未完整顯示專用的思考控制項。

使用時建議：

- 將思考設定保持為**預設**；
- 不要為固定思考模型強制傳送關閉或自訂預算；
- 使用串流輸出處理長回覆；
- 不要任意修改溫度、Top P 和懲罰項；
- 切換通訊協定後重新測試思考內容是否正常顯示。

{% hint style="warning" %}
MiniMax 的多輪工具呼叫依賴完整的 assistant 訊息，包括思考內容和 `tool_calls`。Cherry Studio 會負責維護對話記錄；不要在工具執行途中手動刪除或重寫上一輪訊息，否則模型可能失去推理連續性。
{% endhint %}

如果使用 OpenAI 相容端點時看到 `<think>` 標籤，通常是服務商將思考內容放在 `content` 中。切換到 Anthropic 相容端點前，請先在獨立的服務商副本中測試，以免影響現有對話。

## 工具呼叫與 MCP

Cherry Studio V2 已識別 MiniMax M2、M2.x 和 M3 系列的工具呼叫能力，可用於 MCP 與 Agent 情境。

建議依以下順序驗證：

1. 選擇已同步並啟用的 M3 或 M2.7；
2. 完成一輪一般對話；
3. 啟用一個簡單的 MCP 工具；
4. 使用明確要求呼叫工具的提示詞；
5. 確認模型實際發起工具呼叫；
6. 再增加多個工具或長鏈路任務。

在長鏈路任務中應保留完整上下文。若模型重複呼叫同一個工具，可以先減少工具數量、縮短系統提示詞，並明確設定停止條件。

## 圖片、影片與檔案

MiniMax M3 官方支援文字、圖片和影片輸入，但目前 Cherry Studio V2 的自動視覺模型識別規則可能尚未包含 M3。因此：

- 如果輸入框顯示圖片或影片入口，先用小型檔案執行健康測試；
- 如果入口沒有出現，先更新 Cherry Studio 並重新同步模型；
- 不要只修改顯示名稱來偽裝模型能力；
- 目前版本仍無法使用時，等待用戶端更新調整。

MiniMax OpenAI 與 Anthropic 相容介面中的舊版 M2 模型通常只支援文字和工具呼叫，不要將 MiniMax 的獨立圖片、影片或語音生成模型當作聊天模型新增。

對於 PDF，Cherry Studio 目前會先在本機擷取文字，再將文字傳送給 MiniMax：

- 文字型 PDF 通常可以直接處理；
- 掃描文件需要先執行 OCR；
- 表格、複雜排版和圖片資訊可能在擷取時遺失；
- 擷取後的文字會占用上下文與輸入用量。

## 多模態生成不是聊天模型

MiniMax 還提供語音、圖片、影片和音樂生成 API，但這些介面有獨立的請求格式和任務流程。模型出現在開放平台不代表可以直接透過 Cherry Studio 的聊天服務商呼叫。

例如，將影片生成模型手動新增至對話模型列表，通常只會得到參數或端點錯誤。需要相關能力時，應使用 Cherry Studio 已調整的專用入口；目前沒有調整的介面不能以修改模型名稱取代。

## 知識庫與嵌入模型

MiniMax 內建服務商目前設定的是語言模型端點，不提供嵌入模型。使用知識庫或[全域記憶](../../advanced-basic/memory.md)時：

- 對話模型可以繼續選擇 MiniMax；
- 嵌入模型需要從其他服務商選擇；
- 兩類模型不必來自同一家服務商；
- 設定後分別執行模型健康檢查。

## 檢查連線

1. 確認選擇了正確的中國大陸或國際服務商；
2. 在 API Key 區域執行連線檢查；
3. 選擇一個已同步並啟用的模型；
4. 在模型列表執行健康檢查；
5. 回到對話介面傳送一則簡單訊息；
6. 再分別測試長回覆、思考顯示和 MCP。

連線檢查成功只表示基本憑證可用，不代表 Key 具有所有模型權限，也不代表 Token Plan 仍有可用額度。

## 常見問題

### 傳回未授權或錯誤碼 1004

API Key 無效、已刪除，或 Key 與 `.com` / `.io` 服務商不相符。確認服務商區域後重新建立 Key。

### 傳回餘額不足或錯誤碼 1008

檢查建立目前 Key 的計費類型和帳戶。按量付費餘額與 Token Plan 額度需要分別查看。

### 傳回限速、1002 或 1041

請求已達速率或並行限制。請降低並行請求、縮短上下文並稍後重試；持續發生時檢查帳戶等級和官方限額。

### 傳回 Token 超限或錯誤碼 1039

目前的對話、附件文字和預期輸出超過模型上下文。建立新對話、減少附件、縮短記錄，或選擇具有更長上下文的模型。

### 模型列表仍是舊型號

重新點選**新增**同步列表，確認 Base URL 沒有被錯誤修改。若遠端列表暫時未傳回新模型，可以使用內建預設模型或依官方完整 ID 手動新增。

### M3 沒有思考或圖片入口

M3 的官方能力比目前 Cherry Studio 自動識別規則更新。請先更新用戶端並重新同步；仍未顯示時，不要強制覆寫模型類型，等待更新調整。

### MCP 呼叫中斷或上下文錯亂

先只啟用一個工具，並確認使用 M3 或 M2.7。不要刪除工具呼叫前一輪的 assistant 訊息；必要時建立新對話重新測試。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。模型能力請參閱 [MiniMax Models](https://platform.minimax.io/docs/guides/models-intro)；意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
