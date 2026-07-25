---
icon: key
---

# OpenAI

Cherry Studio V2 的 OpenAI 內建範本用於連接 OpenAI 官方 API，預設使用 **OpenAI Responses** 介面。準備好 OpenAI API Key 後，即可同步帳戶可用的模型並在對話中使用。

{% hint style="warning" %}
OpenAI 範本不再用於第三方 OpenAI 相容閘道。如果你的 Base URL 不是 OpenAI 官方位址，請建立[自訂服務商](zi-ding-yi-fu-wu-shang.md)，並依照閘道要求選擇 OpenAI Chat Completions 或 OpenAI Responses。
{% endhint %}

## 開始前準備

- 可以存取 OpenAI API 的帳戶；
- 在 [OpenAI API Keys](https://platform.openai.com/api-keys) 建立的 API Key；
- 已為 API 帳戶開通的模型和可用額度；
- 符合 OpenAI 最新地區與帳戶要求的網路環境。

ChatGPT 網頁版或用戶端的登入狀態不會自動寫入 Cherry Studio。Cherry Studio 需要 API Key 才能呼叫 OpenAI API。

## 設定 OpenAI

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，並選擇 **OpenAI**；
3. 輸入 API Key；
4. 保留預設 Base URL `https://api.openai.com`；
5. 開啟頁面頂端的服務商開關；
6. 在模型清單中點選**新增**，檢查同步預覽並套用變更；
7. 啟用準備使用的模型。

{% hint style="danger" %}
API Key 只會在建立時完整顯示。不要將它寫入聊天訊息、文件、程式碼儲存庫或問題截圖；如果 Key 洩漏，應立即在 OpenAI 控制台撤銷並重新建立。
{% endhint %}

## 為什麼預設使用 Responses

V2 的 OpenAI 範本預設使用 `openai-responses` 端點。此範本針對 OpenAI 官方目前的介面，應用程式會根據模型能力處理文字、推理、工具呼叫等請求。

如果第三方閘道只支援 `/v1/chat/completions`：

1. 不要修改 OpenAI 內建範本來連接它；
2. 點選服務商清單搜尋框旁的 `+`；
3. 建立自訂服務商；
4. 將 OpenAI Chat Completions 設為主要端點；
5. 填寫閘道提供的 Base URL、API Key 和模型 ID。

這樣可以保留官方 OpenAI 範本，也能避免 Responses 與 Chat Completions 的協定不相容。

## 同步並啟用模型

點選**新增**後，Cherry Studio 會從服務商同步模型清單，並在套用前顯示新增、更新和移除項目。

- 只啟用實際需要的模型，讓模型選擇器更加簡潔；
- 同名模型有多個版本時，請核對完整模型 ID；
- 介面未傳回模型時，可以點選**自訂**並手動填寫官方模型 ID；
- 不要將其他閘道的模型 ID 直接新增到 OpenAI 官方範本。

模型是否可用由 OpenAI 帳戶權限決定。Cherry Studio 能夠識別模型，不代表你的帳戶已經取得存取權限。

## 檢查連線

1. 在 API Key 區域點選連線檢查；
2. 選擇一個已同步且已啟用的模型；
3. 確認檢查成功；
4. 再執行模型健康檢查；
5. 返回對話介面傳送一則簡單訊息。

如果使用推理或工具呼叫模型，請再分別測試一次思考設定和工具呼叫，不要只根據模型名稱判斷能力。

## 選用設定

OpenAI 範本支援服務層級等請求選項。對話頂端的模型設定中可能會顯示**服務層級**，預設使用**自動**即可。

只有在你明確了解 OpenAI 對相應模型的支援和計費方式時，才選擇其他層級。服務商請求設定中的能力開關也不應任意更改；錯誤宣告支援項目可能導致請求失敗。

## 常見問題

### 頁面提示「不再支援舊的呼叫方式」

這是 V2 對 OpenAI 內建範本的提示。OpenAI 官方 API 請使用目前的範本；第三方相容 API 請建立自訂服務商。

### 傳回 401

API Key 無效、已撤銷或複製不完整。請重新建立 Key，並確認沒有多餘的空格。

### 傳回 403

帳戶、地區、組織或模型權限可能不符合要求。請前往 OpenAI 控制台檢查帳戶狀態和模型存取權限。

### 傳回餘額或配額錯誤

檢查 API 帳戶的額度、計費狀態和使用限制。切換模型不會繞過帳戶層級的限制。

### 傳回 404 或模型不存在

重新點選**新增**以同步清單，並核對模型 ID。如果正在連接第三方閘道，請改用自訂服務商並選擇正確的端點。

### 模型可以對話，但無法呼叫工具

檢查模型能力標籤和 OpenAI 對該模型的工具支援。先使用一個簡單工具測試，再逐步增加 MCP 或其他工具。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見回饋管道請參閱[意見回饋與建議](../../question-contact/suggestions.md)。
