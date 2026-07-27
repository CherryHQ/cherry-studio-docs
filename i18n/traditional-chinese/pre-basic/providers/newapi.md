---
icon: arrows-rotate
---

# NewAPI

NewAPI 是一個統一的大型模型閘道。它在伺服器端連線 OpenAI、Anthropic、Google 等上游管道，再向 Cherry Studio 提供統一的模型列表、驗證、路由和計費介面。

Cherry Studio V2 已內建專用的 **New API** 服務商類型，不需要再將它偽裝成一般 OpenAI 服務商。專用類型可以依模型選擇 OpenAI Chat Completions、OpenAI Responses、Anthropic Messages、Google Generate Content、圖片生成或重排序端點。

{% hint style="warning" %}
請求會經過 NewAPI 執行個體及其設定的上游管道。只使用自行部署或明確可信、具有合法上游授權與合規責任的服務。不要將敏感資料和 API Key 交給來源不明的公共執行個體。
{% endhint %}

## 先確認你的角色

一般使用者與 NewAPI 管理員的準備工作不同：

| 角色 | 在 NewAPI 中需要完成的工作 |
| --- | --- |
| 一般使用者 | 建立權杖，確認額度、群組、模型權限和 IP 限制 |
| 管理員 | 先設定並測試上游管道、模型對應、群組和計費，再向使用者發放權杖 |

如果你只是使用他人維護的執行個體，不需要在 Cherry Studio 中填寫上游服務商的 Key，只需填寫該 NewAPI 執行個體發放的使用者權杖。

## 在 NewAPI 建立權杖

1. 登入可信的 NewAPI 執行個體；
2. 開啟**權杖**頁面；
3. 建立一個專供 Cherry Studio 使用的權杖；
4. 視需要設定額度、有效期限、模型限制、群組和 IP 白名單；
5. 複製權杖並妥善儲存；
6. 先在 NewAPI 內建的 Playground 中測試一個模型。

建議為不同裝置或用途建立獨立權杖。發生洩漏時可以只撤銷受影響的權杖，也更容易核對用量。

{% hint style="danger" %}
不要將 NewAPI 權杖寫入聊天訊息、文件、程式碼儲存庫或問題截圖。洩漏後應立即在 NewAPI 控制台刪除並重新建立。
{% endhint %}

## 取得正確的 API 位址

優先複製 NewAPI 首頁顯示的 API Base URL，或向執行個體管理員確認。常見形式如下：

| 部署方式 | 範例 |
| --- | --- |
| HTTPS 網域 | `https://newapi.example.com` |
| 已包含版本路徑 | `https://newapi.example.com/v1` |
| 本機部署 | `http://localhost:3000` |
| 區域網路 IP | `http://192.168.1.20:3000` |

Cherry Studio 會為一般 NewAPI 位址補上 `/v1`，已包含 `/v1` 時不會重複附加。因此填寫網站根位址或標準的 `/v1` Base URL 都可以。

- `http` 與 `https` 必須和伺服器實際設定一致；
- 公開網路執行個體應使用有效的 HTTPS 憑證；
- 瀏覽器管理頁面中的 `/console/...` 不是 API Base URL；
- 不要將權杖頁面、登入頁面或特定的 `/chat/completions` 路徑填入 Base URL。

## 設定 New API

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇內建的 **New API**；
4. 輸入 NewAPI 發放的權杖；
5. 將 Base URL 改為執行個體的 API 位址；
6. 開啟頁面頂端的服務商開關；
7. 點選**新增**同步模型列表；
8. 檢查模型與端點類型後套用變更；
9. 只啟用準備使用的模型。

內建範本的預設位址為 `http://localhost:3000`，只適用於本機預設部署。連線遠端執行個體時必須替換成實際位址。

如果 NewAPI 管理員設定了 Cherry Studio 一鍵匯入連結，可以使用連結預先填入位址與權杖；匯入前仍應核對目標網域，避免惡意連結將金鑰傳送到錯誤的伺服器。

## 瞭解端點類型

NewAPI 中的同一個模型名稱可能支援一種或多種通訊協定。Cherry Studio 會根據模型的端點類型選擇不同的請求實作：

| Cherry Studio 端點類型 | 典型用途 |
| --- | --- |
| OpenAI Chat Completions | 大多數 OpenAI 相容對話模型 |
| OpenAI Responses | 原生支援 Responses API 的 OpenAI 模型 |
| Anthropic Messages | Claude 或其他原生 Messages 相容模型 |
| Google Generate Content | Gemini 原生通訊協定 |
| OpenAI Image Generation | 繪畫頁面中的生成與編輯模型 |
| Jina Rerank | 知識庫重排序模型 |

較新的 NewAPI 執行個體會在 `/models` 回應中傳回 `supported_endpoint_types`，Cherry Studio 同步時會讀取這些資訊。

如果伺服器沒有傳回端點中繼資料：

- 批次新增時選擇該批模型共同使用的端點類型；
- 使用不同通訊協定的模型分批新增；
- 手動新增模型時至少選擇一種端點類型；
- 只選擇 NewAPI 執行個體真正支援的通訊協定；
- 不要只根據模型名稱猜測。

錯誤的端點類型可能造成 404、參數不相容、工具呼叫遺失或圖片請求失敗。能在列表中看到模型，不代表所有通訊協定都可用。

## 管理員：先檢查管道與模型對應

如果你負責維護 NewAPI 執行個體，在讓使用者連線 Cherry Studio 前完成以下檢查：

1. 每個上游管道都通過 NewAPI 的管道測試；
2. 管道勾選的模型與實際權限一致；
3. 模型對應使用用戶端將要請求的模型 ID；
4. 使用者權杖所在群組能存取對應管道；
5. 計費倍率、額度和自動停用策略已核對；
6. `/v1/models` 傳回的模型與使用者權限一致；
7. 分別測試 Chat、Responses、Messages、Gemini 和圖片端點。

模型對應會將 Cherry Studio 請求的名稱轉換成上游名稱。若健康檢查傳回模型不存在，應同時檢查 Cherry Studio 的模型 ID、NewAPI 模型對應和上游管道中的實際 ID。

## 對話、思考與工具呼叫

NewAPI 只是路由層，最終能力取決於上游模型、管道類型、通訊協定轉換和執行個體版本。

- 思考選項要與目標模型及端點類型相符；
- Claude 原生能力優先使用 Anthropic Messages；
- OpenAI 原生 Responses 功能優先使用 OpenAI Responses；
- Gemini 原生能力優先使用 Google Generate Content；
- MCP 需要模型、上游和轉換層都保留工具欄位；
- 多輪工具呼叫失敗時，先使用單一工具排查。

模型在一般對話中可用，不代表思考內容、工具呼叫、網路搜尋或結構化輸出一定完整。請分別為重要工作流程執行健康檢查，不要只測試一句「你好」。

## 繪畫、嵌入與重排序

Cherry Studio 的 NewAPI 轉接還可以使用：

- OpenAI 相容圖片生成與圖片編輯；
- OpenAI 相容嵌入模型；
- Jina 相容重排序模型。

使用前需要 NewAPI 執行個體實際開放相應端點，並為模型選擇正確的端點類型。

### 繪畫模型

1. 同步或手動新增圖片模型；
2. 將端點類型設為 **OpenAI Image Generation**；
3. 啟用模型；
4. 在繪畫頁面選擇該 NewAPI 服務商；
5. 分別測試生成和編輯。

圖片生成成功不代表圖片編輯也受支援。兩者可能使用不同的上游端點、參數和計費方式。

### 嵌入與重排序

- 嵌入模型使用 Embeddings 介面，可供知識庫與[全域記憶](../../advanced-basic/memory.md)使用；
- 重排序模型需要選擇 **Jina Rerank**；
- 對話、嵌入和重排序模型可以來自不同上游；
- 分別執行健康檢查並核對倍率。

## PDF 與附件

NewAPI 是聚合閘道。Cherry Studio 不會因為模型名稱包含 Claude、Gemini 或 OpenAI，就假設閘道完整支援原生 PDF。

目前的 V2 會先在本機擷取 PDF 文字，再將文字傳送到 NewAPI：

- 文字型 PDF 通常可以處理；
- 掃描文件需要先執行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取文字會計入輸入 Token；
- 若需要原生多模態附件，應使用經過驗證的端點與模型。

## 檢查連線

建議依照從伺服器到用戶端的順序排查：

1. 在 NewAPI Playground 使用同一個權杖測試目標模型；
2. 在 Cherry Studio 執行服務商連線檢查；
3. 點選**新增**並確認模型能夠同步；
4. 檢查模型端點類型；
5. 執行模型健康檢查；
6. 回到對話介面傳送一般訊息；
7. 再測試思考、MCP、繪畫或知識庫。

如果 Playground 也失敗，問題通常出在 NewAPI 權杖、管道、餘額或上游；如果 Playground 成功但 Cherry Studio 失敗，請重點檢查 Base URL、端點類型和用戶端版本。

## 常見問題

### 傳回 401

權杖無效、已刪除、過期或複製不完整。確認填寫的是 NewAPI 使用者權杖，而不是上游服務商 Key。

### 傳回 403

權杖的模型權限、群組或 IP 白名單不允許目前的請求。請執行個體管理員檢查權杖、管道與群組的交集。

### 傳回 404

Base URL 填入了控制台路徑、端點類型錯誤，或伺服器未開放對應路由。恢復為網站根位址或標準的 `/v1` 位址後重試。

### 模型列表為空

權杖沒有可用模型、管道未啟用、群組不相符，或舊版 NewAPI 的 `/models` 回應不相容。請先在 NewAPI Playground 和 `/v1/models` 檢查。

### 模型存在但呼叫時傳回「不支援」

檢查模型對應、上游管道和 Cherry Studio 端點類型。模型出現在 `/models` 中只表示可見，不保證目前的通訊協定與參數組合可用。

### 傳回額度或倍率相關錯誤

檢查使用者餘額、權杖額度、群組倍率、模型倍率和上游帳戶餘額。NewAPI 額度充足時，上游管道仍可能欠費。

### MCP 只輸出呼叫計畫

確認模型支援工具呼叫，且 NewAPI 版本與管道能保留 `tools`、`tool_calls` 和工具結果。請先使用一個簡單工具，並嘗試模型原生通訊協定。

### 繪畫模型出現在對話列表

編輯模型，將端點類型改為 **OpenAI Image Generation**，並在繪畫頁面使用。圖片生成模型不是一般聊天模型。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。NewAPI 使用與管理說明請參閱[官方文件](https://docs.newapi.pro/)；意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
