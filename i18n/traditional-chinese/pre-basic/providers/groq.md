---
icon: bolt
---

# Groq

Groq 是以低延遲推理為特色的模型服務平台，提供多種開放權重模型和 Groq Compound 系統。Cherry Studio V2 的 Groq 內建範本使用 Groq 官方 OpenAI 相容端點，並可同步帳戶目前可用的模型。

{% hint style="warning" %}
**Groq** 與 xAI 的 **Grok** 是兩個獨立服務商。Groq 提供模型推理平台；Grok 是 xAI 的模型系列。設定前請確認選擇了正確的項目。
{% endhint %}

## 開始前的準備

- 可登入 [GroqCloud Console](https://console.groq.com/)的帳戶；
- 在 [Groq API Keys](https://console.groq.com/keys) 建立的 API Key；
- 帳戶具有可用額度和速率限制；
- 已確認準備使用的模型仍處於可用狀態。

Groq 的模型清單和生命週期會有所調整。不要根據舊文件固定新增已經下線的模型。

## 設定 Groq

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，選擇 **Groq**；
3. 輸入 Groq API Key；
4. 保留預設 Base URL `https://api.groq.com/openai`；
5. 開啟頁面頂端的服務商開關；
6. 在模型列表點選**新增**，檢查同步預覽並套用變更；
7. 啟用準備使用的模型。

{% hint style="danger" %}
不要把 API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。洩漏後應立即在 GroqCloud Console 撤銷並重新建立。
{% endhint %}

## 同步並選擇模型

點選**新增**後，Cherry Studio 會呼叫 Groq 的模型列表介面，並顯示目前 Key 可存取的模型。模型變化較快，請以 [Groq Supported Models](https://console.groq.com/docs/models)和同步結果為準。

常見類型包括：

| 類型 | 模型 ID 範例 | 適用情境 |
| --- | --- | --- |
| 輕量文字模型 | `llama-3.1-8b-instant` | 低延遲問答、分類和簡單擷取 |
| 大型通用模型 | `openai/gpt-oss-120b` | 複雜文字、程式碼和推理 |
| 其他代管模型 | `qwen/qwen3.6-27b` | 多語言、結構化輸出和工具任務 |
| Compound 系統 | `groq/compound`、`groq/compound-mini` | Groq 伺服器端搜尋與程式碼執行 |

- 只啟用實際需要的模型；
- 核對完整模型 ID，包括斜線和大小寫；
- 模型下線後應重新同步，不要只修改顯示名稱；
- 同一模型在不同方案下可能具有不同的速率限制；
- 音訊、語音或專用模型不一定適用於一般對話。

## 設定服務層級

在對話的 Groq 設定中，可以選擇**服務層級**：

| 選項 | 含義 |
| --- | --- |
| 忽略 | 不傳送 `service_tier`，由 Groq 使用預設行為 |
| 自動 | 使用帳戶目前可用的合適層級 |
| 按需 | 使用一般按需處理 |
| 彈性 | 優先使用高吞吐量，但容量不足時可能快速失敗 |

服務層級是否生效取決於目前的模型、帳戶方案和 Cherry Studio 的能力識別。不瞭解差異時請保持**忽略**或**自動**。

{% hint style="info" %}
彈性處理可能會在容量不足時傳回 `498 capacity_exceeded`。它適合可重試的批次任務，不適合必須一次成功的互動請求。
{% endhint %}

## 使用 MCP 與工具呼叫

一般 Groq 代管模型可以依其能力使用 Cherry Studio 的 MCP 或其他工具：

1. 選擇支援工具呼叫的模型；
2. 啟用一個簡單的 MCP 工具；
3. 發出明確需要工具的請求；
4. 確認模型實際呼叫工具；
5. 再增加平行工具或複雜參數。

Groq Compound 是另一種機制：

- `groq/compound` 可以在單次請求中使用多個 Groq 伺服器端工具；
- `groq/compound-mini` 每次請求只使用一個伺服器端工具，延遲更低；
- 搜尋、存取網頁和程式碼執行由 Groq 伺服器完成；
- Compound 不等同於 Cherry Studio MCP，也不支援將使用者自訂工具直接傳給 Compound。

如果需要自建 MCP 工具，應選擇支援本機工具呼叫的一般代管模型，而不是將 Compound 當作 MCP 執行器。

## 檢查連線

1. 在 API Key 區域執行連線檢查；
2. 選擇一個已同步並啟用的文字模型；
3. 確認檢查成功；
4. 在模型列表執行健康檢查；
5. 回到對話介面傳送一則簡單訊息；
6. 若使用工具或 Compound，再分別測試相應能力。

連線檢查成功只表示基本請求可用，不代表每個模型都具有相同的上下文、工具和速率限制。

## 連線 Groq 相容閘道

如果使用的不是 Groq 官方 API：

1. 新增[自訂服務商](zi-ding-yi-fu-wu-shang.md)；
2. 將 OpenAI Chat Completions 設為主要端點；
3. 填寫閘道提供的 Base URL 和 API Key；
4. 同步或手動新增閘道實際提供的模型；
5. 驗證工具呼叫和服務層級是否受支援。

不要覆蓋 Groq 官方範本。第三方閘道也不會自動取得 Groq Compound 的伺服器端工具。

## 常見問題

### 傳回 401

API Key 無效、已撤銷或複製不完整。請重新建立 Key，並確認沒有多餘空格。

### 傳回 404 或模型不存在

模型已經下線、模型 ID 輸入錯誤，或目前的帳戶沒有存取權限。重新點選**新增**同步列表。

### 傳回 429

請求已達模型或帳戶的速率限制。請降低並行請求、稍後重試，並在 GroqCloud Console 檢查限制。

### 傳回 498

彈性層級目前沒有可用容量。請切換為自動、按需或忽略，或者為任務增加退避重試。

### 回應很快但內容被截斷

檢查模型的上下文和最大輸出限制，並減少輸入長度或調整最大輸出 Token。推理速度不會改變模型本身的限制。

### Compound 沒有呼叫我的 MCP

Compound 使用 Groq 伺服器端工具，不接受 Cherry Studio 的自訂 MCP 工具。請改用支援一般工具呼叫的代管模型。

### 服務層級沒有變化

目前的模型或帳戶可能不支援所選層級。請保持忽略或自動，並以 GroqCloud Console 的實際請求記錄為準。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
