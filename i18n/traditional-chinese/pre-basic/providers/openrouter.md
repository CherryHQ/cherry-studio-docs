---
icon: route
---

# OpenRouter

OpenRouter 是多模型統一閘道。Cherry Studio V2 的 OpenRouter 內建範本使用一組 API Key 同步 OpenRouter 的對話和嵌入模型，並針對推理內容、網路搜尋外掛程式和模型能力進行調整。

{% hint style="warning" %}
OpenRouter 不是模型原廠。請求會經過 OpenRouter，並可能路由至多個上游推理服務商。使用敏感資料前，應在 OpenRouter 控制台檢查隱私、記錄和服務商路由策略。
{% endhint %}

## 開始前的準備

- 可登入 [OpenRouter](https://openrouter.ai/)的帳戶；
- 在 [OpenRouter Keys](https://openrouter.ai/settings/keys) 建立的 API Key；
- 帳戶具有可用餘額或免費模型配額；
- 已確認模型價格、上下文、工具與資料策略。

建議為 Cherry Studio 單獨建立 Key，並在 OpenRouter 中設定合適的額度上限。這樣更容易區分用量，也能降低金鑰洩漏後的風險。

## 設定 OpenRouter

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，選擇 **OpenRouter**；
3. 輸入 OpenRouter API Key；
4. 保留預設 Base URL `https://openrouter.ai/api/v1/`；
5. 開啟頁面頂端的服務商開關；
6. 在模型列表點選**新增**，檢查同步預覽並套用變更；
7. 只啟用準備使用的模型。

{% hint style="danger" %}
不要把 API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。洩漏後應立即在 OpenRouter 中撤銷並重新建立。
{% endhint %}

## 瞭解模型 ID

OpenRouter 模型 ID 通常使用 `<組織>/<模型>` 格式，例如：

| 類型 | 範例 |
| --- | --- |
| 固定模型 | `openai/gpt-oss-120b` |
| 服務商最新別名 | `~anthropic/claude-sonnet-latest` |
| 自動路由 | `openrouter/auto` |
| 免費路由 | `openrouter/free` |
| 免費變體 | 在特定模型 ID 後使用 `:free` |

- 完整模型 ID 決定上游模型和路由行為；
- `latest`、自動路由和免費路由的實際模型可能會變更；
- 需要可重複結果時，請選擇固定版本而不是動態別名；
- 免費變體可能有速率、可用性或資料策略限制；
- 不要只根據顯示名稱判斷價格與能力。

點選**新增**會同步目前的模型，不必將數百個模型全部啟用。優先保留團隊實際使用的少量模型，模型選擇器會更清楚。

## 對話與嵌入模型

Cherry Studio 會分別請求 OpenRouter 的對話模型和嵌入模型介面，並將結果合併至同步列表。

- 對話模型可用於助手、翻譯和一般對話；
- 支援工具呼叫的模型可用於 MCP 或 Agent 情境；
- 嵌入模型可用於知識庫和[全域記憶](../../advanced-basic/memory.md)；
- 同一個 Key 對不同模型的權限、價格和限制可能不同；
- 模型出現在列表中，不代表每個上游服務商都可用。

為知識庫選擇模型時，請確認它確實是嵌入模型，不要只根據服務商名稱判斷。

## 設定思考模式

OpenRouter 會將不同模型的推理參數統一為 `reasoning` 設定。Cherry Studio 根據模型能力傳送關閉、強度或預算設定，並保留跨輪工具呼叫需要的推理內容。

- 選擇**預設**時，盡量使用 OpenRouter 或上游的預設行為；
- 選擇**關閉**時，向支援的模型傳送停用推理；
- 低、中、高等選項只會對支援相應強度的模型生效；
- 推理 Token 通常會計入輸出用量；
- 部分模型不會傳回可見的思考內容。

如果切換模型後思考按鈕的選項發生變化，這是正常現象。不要將一個模型的推理設定直接套用到所有模型。

## 使用網路搜尋

在對話輸入框開啟**網路搜尋**後，Cherry Studio V2 目前會為 OpenRouter 請求加入 Web Search 外掛程式，並傳入網路搜尋設定中的最大結果數。

使用步驟：

1. 選擇一個 OpenRouter 模型；
2. 開啟輸入框中的**網路搜尋**；
3. 提出需要目前網頁資訊的問題；
4. 等待搜尋和模型回答；
5. 展開並核對引用。

{% hint style="info" %}
OpenRouter 網路搜尋會產生額外的搜尋費用，即使底層模型是免費變體也可能收費。OpenRouter 正在從舊 Web 外掛程式遷移到伺服器端搜尋工具；若網路搜尋突然無法使用，請先更新 Cherry Studio 並查看 OpenRouter 最新文件。
{% endhint %}

Perplexity Sonar 或 OpenAI Search 等內建搜尋的模型可能有不同的網路搜尋行為。模型本身是否強制使用網路搜尋，也由 OpenRouter 和上游能力決定。

## 工具呼叫與 Agent

OpenRouter 內建範本包含 OpenAI Chat Completions 與 Anthropic Messages 端點，但實際工具能力仍取決於模型和上游路由。

使用前：

1. 選擇明確支援工具呼叫的模型；
2. 執行一般對話健康檢查；
3. 啟用一個簡單的 MCP 工具；
4. 確認模型實際發起呼叫；
5. 再增加多個工具或長鏈路 Agent。

若 Agent 穩定性不理想，可以比較模型原廠、Anthropic 或 CherryIN 的直連結果。OpenRouter 的統一入口很方便，但上游路由增加了一層變數。

## 隱私與上游路由

OpenRouter 預設會在可用上游之間路由，以提高可用性。Cherry Studio 目前不會替你設定 OpenRouter 的所有服務商路由和隱私欄位。

在 OpenRouter 控制台中檢查：

- 是否啟用輸入輸出記錄；
- 是否允許 OpenRouter 使用輸入輸出；
- 是否限制可能儲存資料的上游；
- 是否要求 Zero Data Retention；
- 是否允許 fallback；
- 組織或 Key 的模型與額度限制。

這些設定屬於 OpenRouter 帳戶策略，不會因為 Cherry Studio 使用本機用戶端而自動變更。

## 檢查連線

1. 在 API Key 區域執行連線檢查；
2. 選擇一個已同步並啟用的模型；
3. 確認檢查成功；
4. 在模型列表執行健康檢查；
5. 回到對話介面傳送一則簡單訊息；
6. 再分別測試推理、網路搜尋和工具呼叫。

連線檢查成功只表示基本憑證可用。特定模型仍可能因餘額、上游故障、隱私策略或參數不相容而失敗。

## 常見問題

### 傳回 401

API Key 無效、已撤銷或複製不完整。請重新建立 Key，並確認沒有多餘空格。

### 傳回餘額或額度錯誤

檢查 OpenRouter 餘額、Key 限額和組織策略。免費模型也可能受到單獨的速率限制。

### 傳回 404 或模型不存在

模型 ID 已變更、模型被移除，或動態別名目前不可用。重新點選**新增**同步列表，並在 [OpenRouter Models](https://openrouter.ai/models)核對。

### 傳回 429

目前的模型、上游服務商或 Key 已達速率限制。請降低並行請求、稍後重試，或選擇其他可用路由。

### 同一個模型的結果或價格發生變化

動態別名、自動路由或上游 fallback 可能會選擇不同版本或服務商。需要穩定行為時請使用固定模型 ID，並在 OpenRouter 控制台限制路由。

### 網路搜尋沒有引用

確認輸入框中的網路搜尋已開啟，並檢查 OpenRouter 搜尋功能是否仍與目前的 Cherry Studio 版本相容。搜尋外掛程式與模型內建搜尋不是同一種機制。

### 工具呼叫不穩定

確認模型頁面標示支援工具，並檢查上游是否支援請求中的所有參數。可以改用固定服務商路由，或改用模型原廠連線進行比較。

更多一般設定請參閱[模型服務](README.md)、[網路搜尋模式](../../websearch/README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
