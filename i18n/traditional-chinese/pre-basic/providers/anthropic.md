---
icon: key
---

# Anthropic

Cherry Studio V2 的 Anthropic 內建範本用於連接 Anthropic 官方 API，預設使用 **Anthropic Messages** 端點。完成 API Key 設定後，即可同步 Claude 模型並用於對話、推理和工具呼叫。

{% hint style="info" %}
服務商具有 Anthropic 端點，不代表其中每個模型都支援工具呼叫或 Agent。請查看模型能力標籤，並在使用前完成一次實際工具測試。
{% endhint %}

## 開始前準備

- 可以使用 Anthropic API 的帳戶；
- 在 [Anthropic API Keys](https://console.anthropic.com/settings/keys) 建立的 API Key；
- 帳戶已開通的模型和可用額度；
- 符合 Anthropic 最新帳戶與地區要求的網路環境。

Anthropic API Key 與網頁版登入狀態是不同的設定。Cherry Studio 需要可用於 API 請求的 Key。

## 設定 Anthropic

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，並選擇 **Anthropic**；
3. 輸入 API Key；
4. 保留預設 Base URL `https://api.anthropic.com`；
5. 開啟頁面頂端的服務商開關；
6. 在模型清單中點選**新增**，檢查同步預覽並套用變更；
7. 啟用準備使用的 Claude 模型。

{% hint style="danger" %}
不要將 API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。如果 Key 洩漏，應立即在 Anthropic Console 撤銷並重新建立。
{% endhint %}

## 同步並選擇模型

Anthropic 的模型名稱和版本會調整，因此本文不會固定列出具體清單。點選**新增**以同步帳戶目前可用的模型，並核對完整模型 ID。

- 只啟用實際需要的模型；
- 同系列的不同版本可能具有不同的上下文、推理和工具能力；
- 介面未傳回模型時，可以點選**自訂**並填寫 Anthropic 官方文件中的模型 ID；
- 不要將第三方閘道的模型 ID 直接新增到 Anthropic 官方範本。

模型出現在 Cherry Studio 登錄資料中，不代表你的 Anthropic 帳戶已經取得存取權限。

## 檢查連線

1. 在 API Key 區域發起連線檢查；
2. 選擇一個已同步且已啟用的模型；
3. 確認檢查成功；
4. 在模型清單中執行健康檢查；
5. 返回對話介面傳送一則簡單訊息。

如果準備使用 MCP 或 Agent，請再啟用一個簡單工具，並驗證模型是否實際發起呼叫。

## Agent 與工具呼叫

Anthropic 範本會出現在模型服務清單的**支援 Agent**篩選中，因為它具有 Anthropic 相容端點。使用時仍需同時符合：

- 目標模型帶有工具呼叫能力；
- 目前 API 端點開放工具呼叫；
- MCP 或其他工具已正確啟用；
- 助手沒有關閉工具；
- 請求未遭服務商權限或安全政策阻止。

如果模型只輸出工具呼叫計畫，卻沒有實際執行，請先用單一簡單工具排查，再檢查模型能力和端點。

## Prompt Cache

Anthropic 端點可以在 Cherry Studio 的**API 設定**中設定 Prompt Cache：

- **快取權杖閾值**：訊息超過該數量後才啟用快取；設為 `0` 表示關閉；
- **快取系統訊息**：決定是否快取系統提示詞；
- **快取最近 N 則訊息**：控制最近對話訊息的快取數量。

{% hint style="warning" %}
快取是否生效、如何計費以及支援哪些模型，均由服務商決定。不了解服務商規則時請保留預設值；錯誤設定不一定能降低成本。
{% endhint %}

## 連接 Anthropic 相容閘道

如果你使用的不是 Anthropic 官方 API：

1. 在左側服務商清單中以滑鼠右鍵點選 Anthropic；
2. 選擇複製或新增同類服務商；
3. 為副本填寫閘道提供的 Base URL 和 API Key；
4. 保留 Anthropic Messages 作為主要端點；
5. 同步或手動新增該閘道實際提供的模型。

使用獨立副本可以避免覆寫 Anthropic 官方範本，也方便分別排查端點和權限。

## 常見問題

### 傳回 401

API Key 無效、已撤銷或複製不完整。請重新建立 Key，並確認沒有多餘的空格。

### 傳回 403

帳戶、地區、工作區或模型權限可能不符合要求。請前往 Anthropic Console 檢查帳戶狀態。

### 傳回 404 或模型不存在

重新點選**新增**以同步清單，並核對完整模型 ID。使用第三方閘道時，請確認 Base URL 和 Anthropic Messages 路徑符合閘道文件。

### 模型沒有出現在 Agent 篩選中

Agent 篩選會根據服務商是否具有 Anthropic 端點進行判斷。自訂閘道需要正確設定 Anthropic Messages 端點；模型本身還需要工具呼叫能力。

### Prompt Cache 沒有效果

確認快取閾值大於 `0`，並檢查服務商和模型是否支援快取。短對話可能無法達到設定的閾值。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見回饋管道請參閱[意見回饋與建議](../../question-contact/suggestions.md)。
