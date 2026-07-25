---
icon: gem
---

# Google Gemini

Cherry Studio V2 的 Gemini 內建範本用於連線 Google 官方 Gemini API，預設使用原生 **Google Generate Content** 端點。完成 API Key 設定後，可以同步目前帳戶可用的 Gemini 模型。

{% hint style="info" %}
Gemini API 與 Google Cloud Vertex AI 是兩種不同的連線方式。本頁使用 Google AI Studio 建立的 API Key；若使用 Google Cloud 專案、區域和服務帳戶，請參閱 Vertex AI 文件。
{% endhint %}

## 開始前的準備

- 可存取 Google AI Studio 和 Gemini API 的 Google 帳戶；
- 所在地區符合 Google 目前的[可用地區要求](https://ai.google.dev/gemini-api/docs/available-regions)；
- 已閱讀並接受 Gemini API 的相關條款；
- 已準備可用的 API Key 和模型配額。

Google AI Studio 可能會為新使用者自動建立預設 Google Cloud 專案和 API Key。已有專案的使用者也可以在 AI Studio 中匯入或選擇專案，不必為了 Cherry Studio 重複建立專案。

## 建立 API Key

1. 開啟 [Google AI Studio API Keys](https://aistudio.google.com/app/apikey)；
2. 登入並選擇準備使用的 Google Cloud 專案；
3. 建立新的 Gemini API Key；
4. 複製 Key，並立即儲存到安全的位置；
5. 回到 Cherry Studio 完成設定。

{% hint style="danger" %}
不要把 API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。Google 可能會封鎖已公開洩漏或不符合限制要求的 Key；洩漏後應在 AI Studio 中刪除並重新建立。
{% endhint %}

## 設定 Gemini

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，選擇 **Gemini**；
3. 輸入從 Google AI Studio 建立的 API Key；
4. 保留預設 Base URL `https://generativelanguage.googleapis.com`；
5. 開啟頁面頂端的服務商開關；
6. 在模型列表點選**新增**，檢查同步預覽並套用變更；
7. 啟用準備使用的模型。

Gemini 內建範本使用 Google 原生端點。不要將官方 Gemini API 改成 OpenAI Chat Completions 或 OpenAI Responses。

## 同步並選擇模型

點選**新增**後，Cherry Studio 會呼叫 Gemini 的模型列表介面，並將遠端結果與內建模型資訊合併後顯示。

- 只啟用實際需要的模型；
- 核對完整模型 ID，不要只看顯示名稱；
- Stable、Preview、Latest 和 Experimental 版本的穩定性與生命週期不同；
- 介面沒有傳回目標模型時，可以點選**自訂**並填寫 Google 官方文件中的模型 ID；
- 模型出現在列表中，不代表目前的 Key 一定具有呼叫權限或剩餘額度。

Google 會持續調整模型版本。請以 [Gemini 模型文件](https://ai.google.dev/gemini-api/docs/models/gemini)和實際同步結果為準，不要依賴舊截圖中的固定清單。

## 檢查連線

1. 在 API Key 區域執行連線檢查；
2. 選擇一個已同步並啟用的文字模型；
3. 確認檢查成功；
4. 在模型列表執行健康檢查；
5. 回到對話介面傳送一則簡單訊息。

如果準備使用圖片理解、圖片生成、推理或工具呼叫，請再分別測試對應功能。模型名稱相近，不代表能力和請求參數完全相同。

## 推理與工具呼叫

Cherry Studio 會根據模型登錄資訊顯示推理和工具能力，並為支援的 Gemini 模型轉換思考參數。使用時仍需符合：

- 目前的模型版本支援相應能力；
- API Key 對該模型具有權限和配額；
- 模型能力標籤與實際端點一致；
- MCP 或其他工具已經啟用；
- 請求參數沒有超過模型限制。

若升級模型後推理或工具呼叫異常，先重新同步模型，再用簡單對話和單一工具分別排查。

## 連線 Gemini 相容閘道

如果使用的不是 Google 官方 Gemini API：

1. 新增[自訂服務商](zi-ding-yi-fu-wu-shang.md)；
2. 將 Google Generate Content 設為主要端點；
3. 填寫閘道提供的 Base URL 和 API Key；
4. 同步或手動新增該閘道實際提供的模型；
5. 執行連線檢查和模型健康檢查。

使用獨立自訂服務商可以保留官方 Gemini 範本，也能避免將閘道路徑或模型 ID 混入官方設定。

## 常見問題

### 傳回 400

模型不支援目前的參數，或請求超過輸入限制。先用純文字短訊息測試，再逐步啟用圖片、推理和工具。

### 傳回 401 或 API Key 無效

Key 複製不完整、已刪除或已被封鎖。請到 Google AI Studio 檢查狀態；若 Key 曾公開洩漏，請重新建立。

### 傳回 403

帳戶、專案、地區或模型權限不符合要求。檢查目前 Key 所屬專案、[可用地區](https://ai.google.dev/gemini-api/docs/available-regions)和 Google 帳戶狀態。

### 傳回 404 或模型不存在

重新點選**新增**同步模型，核對完整模型 ID。Preview、Latest 或 Experimental 模型可能已經更名或停止提供。

### 傳回 429

目前專案或模型已達速率或配額限制。檢查 Google AI Studio 中的用量和計費狀態，稍後重試或更換有可用配額的模型。

### 無法同步模型

確認使用 Google AI Studio 建立的 Gemini API Key，並保留官方 Base URL。也可以參考官方[模型列表介面](https://ai.google.dev/api/models)核對 Key 是否能列出模型。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
