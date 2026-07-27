---
icon: shuffle
---

# OneAPI

OneAPI 是一個將多個上游大型模型管道轉換成 OpenAI 相容介面的閘道。管理員在 OneAPI 中設定上游 Key、模型和路由，一般使用者使用 OneAPI 發放的權杖連線 Cherry Studio。

Cherry Studio V2 沒有獨立的 OneAPI 內建服務商；OneAPI 與 NewAPI 共用 **New API** 相容轉接。對於標準 OneAPI 執行個體，模型端點類型通常選擇 **OpenAI Chat Completions**。

{% hint style="warning" %}
請求會經過 OneAPI 執行個體及其上游管道。只使用自行部署或明確可信、具有合法上游授權與合規責任的服務。來源不明的公共執行個體可能記錄請求、洩漏附件或錯誤計費。
{% endhint %}

## OneAPI 與 NewAPI 的差異

OneAPI 是較早的統一閘道專案，NewAPI 在類似架構上繼續擴充更多原生通訊協定、端點類型和模型中繼資料。

| 專案 | 在 Cherry Studio 中的建議 |
| --- | --- |
| OneAPI | 使用 New API 相容服務商，預設以 OpenAI Chat Completions 處理 |
| NewAPI | 使用專用 New API 類型，並依模型選擇 Chat、Responses、Anthropic、Gemini、圖片或 Rerank |

如果執行個體經過二次開發或佈景主題自訂，不能只根據頁面外觀判斷它屬於哪個專案。請向管理員確認伺服器版本和支援的 API 通訊協定。

## 先確認你的角色

一般使用者只需要執行個體位址和使用者權杖。管理員還需要維護上游管道：

| 角色 | 準備工作 |
| --- | --- |
| 一般使用者 | 建立專用權杖，確認額度、群組和模型權限 |
| 管理員 | 設定上游管道、模型對應、倍率、群組與容錯移轉 |

不要將 OpenAI、Anthropic 等上游服務商 Key 直接填入 Cherry Studio 的 OneAPI 連線。用戶端應使用 OneAPI 發放的權杖。

## 在 OneAPI 建立權杖

1. 登入可信的 OneAPI 執行個體；
2. 開啟**權杖**頁面；
3. 新增一個專供 Cherry Studio 使用的權杖；
4. 視需要設定名稱、額度、有效期限和可用模型；
5. 複製權杖並妥善儲存；
6. 使用 OneAPI 內建的測試功能驗證一個模型。

不建議長期共用預設權杖。獨立權杖更容易稽核用量、設定上限和單獨撤銷。

{% hint style="danger" %}
不要將 OneAPI 權杖寫入聊天訊息、文件、程式碼儲存庫或問題截圖。洩漏後應立即在 OneAPI 控制台刪除並重新建立。
{% endhint %}

## 取得 API Base URL

OneAPI 官方 OpenAI 相容格式通常使用：

```text
https://your-oneapi.example.com/v1
```

Cherry Studio 的 New API 相容轉接會為網站根位址補上 `/v1`，因此以下兩種寫法都可以：

- `https://your-oneapi.example.com`
- `https://your-oneapi.example.com/v1`

本機或區域網路部署也可以使用：

- `http://localhost:3000`
- `http://192.168.1.20:3000`

注意：

- `http` 與 `https` 必須和伺服器實際設定一致；
- 公開網路服務應使用有效的 HTTPS 憑證；
- `/console/...`、登入頁面和權杖頁面不是 API Base URL；
- 不要填寫特定的 `/chat/completions` 路徑。

## 在 Cherry Studio 中設定

如果沒有使用其他 NewAPI 閘道，可以直接設定內建的 **New API**；如果已有其他執行個體，請先複製或新增一個 New API 相容服務商，避免覆蓋原有設定。

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **New API**，或新增一個以 New API 為範本的服務商；
4. 將名稱改為容易識別的 OneAPI 執行個體名稱；
5. 輸入 OneAPI 使用者權杖；
6. 填寫 OneAPI Base URL；
7. 開啟頁面頂端的服務商開關；
8. 點選**新增**同步模型列表；
9. 將標準 OneAPI 模型的端點類型設為 **OpenAI Chat Completions**；
10. 只啟用準備使用的模型。

OneAPI 的 `/models` 回應通常不會提供 NewAPI 新版本中的 `supported_endpoint_types`。因此 Cherry Studio 可能會要求你在批次新增時選擇端點類型，這是正常現象。

## 新增模型

優先從伺服器同步模型，不要照抄其他執行個體的模型名稱。

如果同步失敗，可以手動新增：

1. 在 OneAPI 控制台確認權杖可見的完整模型 ID；
2. 在 Cherry Studio 點選**新增模型**；
3. 輸入完全相同的模型 ID；
4. 端點類型選擇 **OpenAI Chat Completions**；
5. 儲存並執行健康檢查。

模型顯示名稱可以自訂，但實際模型 ID 必須與 OneAPI 的可用模型或對應名稱一致。

{% hint style="info" %}
OneAPI 會將用戶端請求的模型 ID 對應至上游模型。模型不存在時，應同時檢查 Cherry Studio 中的 ID、OneAPI 管道模型和管理員設定的模型對應。
{% endhint %}

## 能力邊界

OneAPI 主要將不同上游統一成 OpenAI 相容格式。基本對話通常最穩定，較新的原生能力不一定能完整保留。

- Claude 的原生 thinking block 可能被轉換或遺失；
- Gemini 的原生多模態結構可能受到執行個體版本限制；
- OpenAI Responses 專屬能力不等同於 Chat Completions；
- 工具呼叫需要 OneAPI 與上游都正確轉換 `tools` 和 `tool_calls`；
- 網路搜尋、快取、服務層級等服務商專屬參數可能不會生效；
- 模型列表可見不代表所有參數組合都可用。

若工作流程依賴特定服務商的最新原生能力，請優先使用模型原廠服務商或支援對應原生端點的新版 NewAPI。

## 工具呼叫與 MCP

可以使用支援 Function Calling 的 OneAPI 模型連線 MCP，但應先執行最小測試：

1. 選擇明確支援工具呼叫的模型；
2. 完成一輪一般對話；
3. 只啟用一個簡單的 MCP 工具；
4. 明確要求模型呼叫該工具；
5. 確認 OneAPI 記錄中出現工具請求；
6. 再增加更多工具。

如果模型只輸出呼叫計畫，可能是上游模型不支援工具、OneAPI 轉換不完整，或管道刪除了工具欄位。請先在 OneAPI 中直接測試同一個模型。

## 知識庫與嵌入模型

當 OneAPI 執行個體開放相容的 Embeddings 介面時，可以將嵌入模型用於知識庫或[全域記憶](../../advanced-basic/memory.md)。

- 只新增執行個體實際提供的嵌入模型；
- 不要將對話模型當作嵌入模型；
- 對話和嵌入可以使用不同服務商；
- 分別執行健康檢查；
- 核對 OneAPI 與上游的計費倍率。

舊執行個體或特定管道可能沒有嵌入介面。模型名稱存在不代表 `/v1/embeddings` 可用。

## PDF 與附件

OneAPI 是聚合閘道，Cherry Studio 不會只根據模型名稱假設它支援原生 PDF。

目前的 V2 會先在本機擷取 PDF 文字，再傳送到 OneAPI：

- 文字型 PDF 通常可以處理；
- 掃描文件需要先執行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取文字會占用輸入 Token；
- 圖片等多模態附件仍取決於執行個體和上游能力。

## 管理員檢查清單

向使用者發放權杖前，建議管理員確認：

1. 上游管道測試成功；
2. 管道啟用的模型與實際權限一致；
3. 模型對應沒有拼寫錯誤；
4. 使用者群組能存取目標管道；
5. 模型倍率和群組倍率正確；
6. 權杖限制與使用者用途相符；
7. `/v1/models` 和 `/v1/chat/completions` 都可用；
8. 重要模型已完成工具呼叫測試。

使用多個管道進行負載平衡時，同一個模型可能會路由至不同上游。需要穩定行為時，請減少不一致的管道，或由管理員依 OneAPI 支援的方式固定管道。

## 檢查連線

1. 在 OneAPI 內建測試或相容請求中驗證同一個權杖；
2. 在 Cherry Studio 執行服務商連線檢查；
3. 點選**新增**確認模型列表可以同步；
4. 檢查端點類型是 OpenAI Chat Completions；
5. 執行模型健康檢查；
6. 回到對話介面傳送一則簡單訊息；
7. 再測試工具呼叫、附件或知識庫。

伺服器端也失敗時，請優先檢查 OneAPI 管道、權杖和上游；只有 Cherry Studio 失敗時，重點檢查 Base URL、模型 ID 與端點類型。

## 常見問題

### 傳回 401

權杖無效、已刪除、過期或複製不完整。確認填寫的是 OneAPI 使用者權杖，而不是上游服務商 Key。

### 傳回 403

權杖沒有目標模型權限、額度已用盡，或群組無法存取可用管道。請聯絡執行個體管理員檢查。

### 傳回 404

Base URL 填入了管理頁面或特定介面路徑，或者執行個體未開放標準 OpenAI 相容路由。請恢復為網站根位址或 `/v1`。

### 模型列表為空

權杖沒有可見模型、管道未啟用、群組不相符，或執行個體版本的 `/models` 回應不相容。請先在 OneAPI 中測試並確認 `/v1/models`。

### 模型存在但呼叫失敗

檢查 OneAPI 模型對應與上游管道。列表中的模型名稱只是入口，實際路由仍可能找不到或沒有權限。

### 思考內容、網路搜尋或工具能力缺失

OneAPI 的 OpenAI 格式轉換可能未保留服務商原生欄位。請使用簡單的 Chat Completions 功能進行比較；需要完整原生能力時改用原廠服務商或 NewAPI 的對應端點。

### 請求結果時好時壞

多個管道的模型版本、參數支援或餘額不一致。請管理員檢查管道測試、優先順序、權重和自動停用狀態。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。若執行個體實際為 NewAPI，請改看 [NewAPI](newapi.md)；OneAPI 專案說明請參閱[官方儲存庫](https://github.com/songquanpeng/one-api)。意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
