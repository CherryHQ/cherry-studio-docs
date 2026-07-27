# GitHub Copilot

Cherry Studio 可以透過 GitHub 裝置授權連線至你的 Copilot 帳號，並讀取該帳號目前可用的模型。你不需要手動建立 API Key，但 GitHub 帳號必須具備有效的 Copilot 使用資格。

{% hint style="info" %}
GitHub Copilot、GitHub Models 和 GitHub Copilot CLI 是三個不同的入口。本頁介紹的是 `設定 → 模型服務 → GitHub Copilot`，用於在 Cherry Studio 對話中呼叫 Copilot 模型。
{% endhint %}

## 使用前確認

開始前請確認：

1. 已有可以正常登入的 GitHub 帳號；
2. 帳號已啟用 Copilot Free、Student、Pro、Pro+、Max，或由組織指派 Business / Enterprise 權限；
3. 組織或企業政策未禁止相關模型或 Copilot 功能；
4. 目前網路可以存取 GitHub 登入與 Copilot 服務；
5. 了解目前方案的模型範圍和 [GitHub AI Credits](https://docs.github.com/en/copilot/concepts/billing) 規則。

不同方案的模型、額度與計費規則可能會變更。Cherry Studio 會從 Copilot 介面同步帳號目前可見且未被政策停用的模型，不應以舊版教學中的固定模型清單為準。

GitHub Copilot Free 和 Student 目前主要透過自動模型選擇提供有限的模型存取權；付費方案和組織方案的可選模型較多，但仍受帳號、地區、組織政策和 GitHub 目前發布狀態影響。

## 在 Cherry Studio 授權

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **GitHub Copilot**；
4. 點選**開始授權**；
5. 等待 Cherry Studio 產生 Device Code；
6. 複製授權碼。應用程式通常會自動複製，也可以手動複製；
7. 點選**開啟授權頁面**；
8. 在瀏覽器中登入準備使用的 GitHub 帳號；
9. 輸入 Device Code 並確認授權；
10. 返回 Cherry Studio；
11. 點選**連線 GitHub**完成連線。

連線成功後，頁面會顯示 GitHub 使用者名稱和大頭貼，並自動啟用服務商。

{% hint style="warning" %}
瀏覽器中已登入的帳號不一定是準備連線的帳號。授權前請檢查使用者名稱，尤其是在個人帳號、工作帳號和企業受管理帳號之間切換時。
{% endhint %}

## 授權過程中發生了什麼

Cherry Studio 採用 GitHub Device Flow：

1. 向 GitHub 請求暫時的 Device Code；
2. 由你在 GitHub 頁面確認授權；
3. 使用授權結果換取 GitHub 存取權杖；
4. 再取得可用於 Copilot 請求的暫時權杖；
5. 將 GitHub 存取權杖透過系統安全儲存空間加密後儲存在本機；
6. 後續同步模型或對話時重新整理 Copilot 權杖。

因此，「GitHub 頁面授權成功」只是第一步。Cherry Studio 還需要成功取得 Copilot 權杖，才能顯示連線成功。

{% hint style="danger" %}
Device Code、存取權杖和 Copilot 權杖都不應傳送給他人，也不要出現在文件、聊天、程式碼儲存庫或截圖中。授權碼雖然是暫時的，仍可能在有效期間內遭到濫用。
{% endhint %}

## 同步模型

授權成功後：

1. 確認 GitHub Copilot 服務商已開啟；
2. 點選**新增**或同步模型；
3. 檢查同步預覽；
4. 套用變更；
5. 只啟用準備使用的模型；
6. 對每個模型執行健康檢查。

Cherry Studio 會存取 Copilot 的 `/models` 介面，並篩除：

- 被 GitHub 政策標記為不可用的模型；
- 帳戶路由等非直接模型項目；
- 語音、轉錄等目前不適合對話清單的模型。

模型突然增加、減少或重新命名，通常是由 GitHub 方案、組織政策或伺服器端發布變更所引起。重新同步即可取得目前清單。

## 方案、模型與費用

GitHub Copilot 的使用量由 GitHub 帳號負責計量，不會因為從 Cherry Studio 發起而變成免費呼叫。

- 不同方案包含不同的 GitHub AI Credits；
- 模型消耗取決於輸入、輸出、快取 token 和模型價格；
- 組織或企業可以設定共享額度、使用者預算和額外使用限制；
- 額度用盡時，呼叫可能會遭到阻止或產生額外費用；
- 部分較舊的年度方案在到期前仍可能使用舊有的 premium request 計量方式。

模型出現在 Cherry Studio 中，不代表它在你的方案下具有相同成本。使用前請在 GitHub 帳單和 Copilot 使用量頁面確認。

## 速率限制

GitHub Copilot 服務商頁面提供 1–60 的**速率限制**滑桿，預設值為 10。它控制 Cherry Studio 連續向該服務商發出請求時的最短等待時間，單位為秒。

- 日常對話建議先保留預設值；
- 遇到頻率限制時，提高該值；
- 需要快速連續測試時可以降低，但無法繞過 GitHub 伺服器端限制；
- 多視窗、自動工作或並行請求仍可能累積至帳號限制。

GitHub 本身也會根據容量、公平使用和濫用防護實施伺服器端限流。遇到限流時，應等待後重試，並檢查使用量和方案，而不是持續快速重新傳送。

## 選擇模型與能力

### 一般對話

先選擇模型清單中目前可用的模型，傳送一則簡短訊息。基礎對話成功後，再測試長上下文、圖片或工具。

### 視覺理解

Cherry Studio 會為 Copilot 請求附加視覺支援請求標頭，但實際能否處理圖片仍取決於具體模型和帳號權限。

1. 選擇明確支援圖片的模型；
2. 上傳一張小圖片；
3. 確認模型確實理解圖片內容；
4. 再測試多張圖片或高解析度圖片。

同一個模型在 GitHub 更新前後可能出現能力差異，應以目前的健康檢查和實際結果為準。

### MCP 與工具呼叫

Cherry Studio MCP 需要模型支援結構化 Tool Calling。

1. 先完成一般對話；
2. 只啟用一個簡單的 MCP 工具；
3. 明確要求模型呼叫工具；
4. 檢查是否確實產生結構化呼叫；
5. 確認工具結果傳回後，模型能夠繼續回答；
6. 再逐步增加工具數量。

帳號能使用 Copilot，不代表所有可見模型都支援工具。如果模型只描述「將呼叫工具」卻沒有實際呼叫，應改用工具能力更強的模型。

### 思考與參數

不同 Copilot 模型使用的推論參數並不相同。Cherry Studio 會根據模型識別套用相應設定，但伺服器端模型更新可能早於用戶端識別規則。

遇到參數錯誤時：

1. 將思考選項恢復為**預設**；
2. 清除自訂參數；
3. 重新同步模型；
4. 重試健康檢查；
5. 再逐項啟用需要的參數。

## PDF 與附件

目前 V2 會先在本機擷取 PDF 文字，再透過 Copilot 的 OpenAI 相容介面傳送給模型：

- 文字型 PDF 通常可以處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會消耗上下文和 GitHub AI Credits；
- PDF 中的圖片需要單獨傳送給視覺模型。

上傳檔案前，應確認內容符合組織的資料使用與保密要求。Copilot 是雲端服務，請勿將它視為本機離線模型。

## 組織與企業帳號

組織或企業可以控制 Copilot 功能、模型和網路存取。即使帳號顯示已指派 Copilot，也可能因為政策而無法使用部分模型。

遇到組織帳號問題時，請讓管理員檢查：

- 使用者是否已指派 Copilot 席位；
- Copilot Chat 和相關模型是否已啟用；
- 是否存在模型層級的政策限制；
- 預算或 GitHub AI Credits 是否用盡；
- 企業網路是否只允許特定 Copilot 訂閱端點；
- 防火牆、Proxy 或 TLS 檢查是否阻擋 GitHub Copilot。

組織政策會套用至使用該身分驗證的多個入口，不只 Cherry Studio。

## Proxy 與網路

授權和模型呼叫至少需要存取 GitHub 登入、GitHub API 與 Copilot 服務。公司 Proxy、防火牆、VPN 或安全軟體可能只允許部分位址，導致：

- 無法產生 Device Code；
- 瀏覽器授權成功，但 Cherry Studio 連線失敗；
- 可以取得使用者資訊，但無法取得 Copilot 權杖；
- 模型清單是空的；
- 對話請求逾時或遭拒。

優先使用 Cherry Studio 目前支援的系統 Proxy 或 HTTP Proxy，並請網路管理員根據 [GitHub Copilot allowlist](https://docs.github.com/en/copilot/reference/copilot-allowlist-reference) 允許所需位址。

不要隨意加入來源不明的自訂請求標頭。GitHub Copilot 頁面提供的請求標頭編輯功能主要用於特殊 Proxy 或相容情境；錯誤的 `Authorization`、`Host`、用戶端識別碼或路由標頭可能導致驗證失敗。

## 登出與更換帳號

若要切換帳號：

1. 在 GitHub Copilot 服務商頁面點選**登出 GitHub**；
2. 確認使用者名稱和大頭貼已清除；
3. 在瀏覽器中切換至目標 GitHub 帳號；
4. 重新執行裝置授權；
5. 重新同步模型。

Cherry Studio 登出會刪除儲存在本機的 Copilot 認證資料和服務商金鑰，但不等同於撤銷 GitHub 帳號中的 OAuth 授權。如果裝置遺失或懷疑認證資料外洩，還應在 GitHub 的授權應用程式設定中撤銷存取權，並檢查帳號安全記錄。

## 常見問題

### 無法取得 Device Code

檢查網路、Proxy、防火牆與 GitHub 服務狀態。確認系統時間正確，並關閉可能攔截 GitHub 登入請求的安全軟體後重試。

### GitHub 頁面已授權，但連線失敗

Cherry Studio 尚未取得 GitHub 或 Copilot 權杖。返回應用程式後點選**連線 GitHub**；如果逾時，請重新產生 Device Code，不要重複使用舊的授權碼。

### 顯示使用者名稱，但無法同步模型

GitHub 登入有效不代表帳號具備 Copilot 權限。檢查 Copilot 方案、組織席位、模型政策和使用額度，然後登出並重新授權。

### 模型清單是空的

帳號可能只有自動模型選擇權限、組織已停用模型，或 Copilot `/models` 請求遭網路阻擋。先在 GitHub 官方 Copilot 頁面確認帳號可用，再重新同步。

### 某個模型突然消失

GitHub 可能調整了模型發布狀態、方案範圍或組織政策。重新同步並檢查 GitHub 目前的模型清單。

### 傳回 401 或 403

認證資料已過期、授權遭撤銷、帳號沒有 Copilot 權限或組織政策拒絕存取。登出後重新授權；仍失敗時，檢查帳號方案和管理員政策。

### 傳回 429 或頻率限制

等待後重試，提高 Cherry Studio 的速率限制值，並檢查 GitHub AI Credits、預算與伺服器端限流狀態。

### 圖片或 MCP 無法使用

確認所選模型支援相應能力。基礎對話成功不代表模型支援視覺或工具呼叫。

### 公司網路中無法使用

請網路管理員檢查 Copilot allowlist、訂閱專屬網域、Proxy 身分驗證和 TLS 檢查。不要透過關閉所有安全政策來解決問題。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。Copilot 方案、用量與政策請參閱 [GitHub Copilot 官方文件](https://docs.github.com/en/copilot)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
