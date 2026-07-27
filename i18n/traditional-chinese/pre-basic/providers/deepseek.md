---
icon: whale
---

# DeepSeek

Cherry Studio V2 的 DeepSeek 內建範本用於連線 DeepSeek 官方 API。目前範本預設使用 **OpenAI Chat Completions**，同時包含 DeepSeek 官方 Anthropic 相容端點，並針對 DeepSeek V4 的思考開關與推理強度進行調整。

{% hint style="info" %}
如果只想先體驗模型，可以使用 Cherry Studio 內建的 [CherryAI 免費試用](cherryin/README.md)。本頁適用於已擁有 DeepSeek 官方 API Key 的使用者。
{% endhint %}

## 開始前的準備

- 可登入 [DeepSeek 開放平台](https://platform.deepseek.com/)的帳戶；
- 在 [API Keys](https://platform.deepseek.com/api_keys) 建立的 API Key；
- 帳戶具有可用餘額或配額；
- 已確認目前可用的模型和官方 API 變更。

DeepSeek 網頁版或 App 的登入狀態不會自動寫入 Cherry Studio。呼叫官方 API 需要另外建立 API Key。

## 設定 DeepSeek

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，選擇 **deepseek**；
3. 輸入 DeepSeek API Key；
4. 保留預設 Base URL `https://api.deepseek.com`；
5. 開啟頁面頂端的服務商開關；
6. 在模型列表點選**新增**，檢查同步預覽並套用變更；
7. 啟用準備使用的模型。

{% hint style="danger" %}
不要把 API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。洩漏後應立即在 DeepSeek 開放平台刪除並重新建立。
{% endhint %}

## 選擇目前的模型

DeepSeek 官方目前提供以下主要模型 ID：

| 模型 ID | 適用情境 |
| --- | --- |
| `deepseek-v4-flash` | 日常對話、快速任務、對延遲敏感的工作 |
| `deepseek-v4-pro` | 複雜推理、程式碼、長上下文和 Agent 任務 |

舊模型別名 `deepseek-chat` 和 `deepseek-reasoner` 已於 2026 年 7 月停止提供。若舊設定傳回模型不存在，請重新點選**新增**同步列表，改用目前的 V4 模型 ID。

{% hint style="warning" %}
模型列表和生命週期可能繼續變動。請以 [DeepSeek API 文件](https://api-docs.deepseek.com/)和實際同步結果為準，不要依賴舊截圖中的固定模型名稱。
{% endhint %}

## 設定思考模式

DeepSeek V4 同時支援思考與非思考模式，並預設啟用思考。Cherry Studio 會在輸入框的思考按鈕中顯示適用選項：

- **預設**：使用服務商的預設行為；
- **關閉**：傳送停用思考參數；
- **高**：使用 DeepSeek 的 `high` 推理強度；
- **極力思考**：對應 DeepSeek 的 `max` 推理強度。

`極力思考` 通常會消耗更多推理時間和 Token。日常問答可以先使用預設或關閉；複雜程式碼、規劃和 Agent 任務再提高強度。

在思考模式下，部分取樣參數可能不會生效。遇到結果差異時，先保留預設參數，只調整思考開關和強度。

## 工具呼叫與 Agent

DeepSeek V4 支援思考模式下的工具呼叫，Cherry Studio 也會保留工具呼叫過程所需的思考內容。使用前仍應完成實際測試：

1. 啟用一個簡單的 MCP 工具；
2. 選擇 `deepseek-v4-pro` 或 `deepseek-v4-flash`；
3. 先使用預設思考強度；
4. 發出明確需要工具的請求；
5. 確認模型實際呼叫工具，而不是只輸出呼叫計畫。

若連續工具呼叫傳回 400，請先更新 Cherry Studio 與模型列表，再檢查閘道是否確實為 DeepSeek 官方端點。

## 檢查連線

1. 在 API Key 區域執行連線檢查；
2. 選擇一個已同步並啟用的 V4 模型；
3. 確認檢查成功；
4. 在模型列表執行健康檢查；
5. 回到對話介面傳送一則簡單訊息；
6. 再分別測試思考模式和工具呼叫。

連線檢查成功不代表帳戶有無限配額，也不代表所有模型都已開放。

## 知識庫與嵌入模型

DeepSeek 內建範本目前只設定對話端點，不提供嵌入模型。使用[全域記憶](../../advanced-basic/memory.md)或知識庫時：

- 對話模型可以繼續選擇 DeepSeek；
- 嵌入模型需要從其他服務商選擇；
- 嵌入模型和對話模型不必來自同一家服務商；
- 設定完成後分別執行模型健康檢查。

## 連線 DeepSeek 相容閘道

如果使用的不是 DeepSeek 官方 API：

1. 新增[自訂服務商](zi-ding-yi-fu-wu-shang.md)；
2. 依閘道文件選擇 OpenAI Chat Completions 或 Anthropic Messages；
3. 填寫閘道提供的 Base URL 和 API Key；
4. 同步或手動新增閘道實際提供的模型 ID；
5. 驗證閘道是否完整支援思考參數和工具呼叫。

不要直接覆蓋 DeepSeek 官方範本。使用獨立服務商更容易區分官方帳戶、第三方模型名稱和通訊協定差異。

## 常見問題

### 傳回 401

API Key 無效、已刪除或複製不完整。請重新建立 Key，並確認沒有多餘空格。

### 傳回餘額或配額錯誤

請到 DeepSeek 開放平台檢查餘額、用量和帳戶狀態。切換模型不會繞過帳戶層級的限制。

### 傳回 404 或模型不存在

重新點選**新增**同步模型，並確認使用 `deepseek-v4-flash` 或 `deepseek-v4-pro`。舊別名已停止提供。

### 傳回 429 或伺服器忙碌

目前請求已達速率限制或服務暫時壅塞。請稍後重試、減少並行請求，或檢查帳戶限制。

### 思考按鈕沒有顯示完整選項

確認模型 ID 是目前的 V4 ID，並重新同步模型。手動新增時不要修改模型 ID；顯示名稱可以自訂。

### 工具呼叫只輸出文字

確認模型支援工具呼叫、MCP 已啟用，並使用 DeepSeek 官方端點或明確支援完整工具通訊協定的閘道。先用單一簡單工具排查。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
