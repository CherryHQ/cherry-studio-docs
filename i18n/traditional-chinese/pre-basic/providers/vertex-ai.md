---
icon: cloud
---

# Vertex AI

Cherry Studio V2 的 Vertex AI 內建範本透過 Google Cloud **Service Account** 連線 Vertex AI。它需要專案 ID、地區、Service Account Client Email 和私密金鑰，不使用 Gemini API Key。

V2 不僅能呼叫 Vertex AI 上的 Gemini 模型，也能為可用的 Claude 模型選擇 Vertex Anthropic 路由；最終可用範圍取決於專案、地區、權限和 Model Garden 的實際開放情況。

{% hint style="info" %}
Google AI Studio 的 Gemini API Key 不能直接用於本頁設定。若只有 Gemini API Key，請使用 [Google Gemini](google-gemini.md) 服務商。
{% endhint %}

## 開始前的準備

在 Google Cloud 中完成以下準備：

- 選擇或建立一個 Google Cloud 專案；
- 為專案啟用計費功能；
- 啟用 Vertex AI API；
- 建立專供 Cherry Studio 使用的 Service Account；
- 為該帳戶授予呼叫目標模型所需的最低權限；
- 建立並安全下載 Service Account JSON 金鑰；
- 確認目標模型可用的 Location。

Google 官方快速入門通常要求呼叫者具有 **Vertex AI User**（`roles/aiplatform.user`）權限。企業專案可能使用自訂 IAM 角色，請依組織政策由管理員授權。

相關入口：

- [Vertex AI 快速入門](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)
- [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)

## 從 JSON 金鑰讀取欄位

Cherry Studio 目前需要手動填寫以下內容：

| Cherry Studio 欄位 | Service Account JSON 或 Google Cloud 中的值 |
| --- | --- |
| Client Email | `client_email` |
| 私密金鑰 | `private_key`，包含完整的 BEGIN/END 行 |
| 專案 ID | `project_id` |
| 地區 | 目標模型實際可用的 Location，例如 `us-central1` |

複製私密金鑰時應保留原有換行和 `-----BEGIN PRIVATE KEY-----`、`-----END PRIVATE KEY-----`。

{% hint style="danger" %}
Service Account 私密金鑰是高度敏感的憑證。不要把完整 JSON、`private_key` 或用戶端設定頁寫入聊天訊息、文件、程式碼儲存庫和問題截圖。洩漏後應立即在 Google Cloud 中刪除該金鑰並建立新金鑰。
{% endhint %}

## 設定 Vertex AI

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，選擇 **VertexAI**；
3. 在 **Client Email** 填寫 JSON 的 `client_email`；
4. 在 **私密金鑰** 填寫完整的 `private_key`；
5. 在 **專案 ID** 填寫 `project_id`；
6. 在 **地區** 填寫目標模型可用的 Location；
7. 保持 API 位址為空；
8. 開啟頁面頂端的服務商開關；
9. 新增並啟用準備使用的模型。

{% hint style="warning" %}
Vertex AI 的 API 位址通常會根據專案和地區自動產生，不建議手動填寫。只有在明確使用反向代理並瞭解其完整路徑時才修改。
{% endhint %}

## 新增並選擇模型

在模型列表點選**新增**，檢查同步預覽並套用變更。若遠端沒有傳回目標模型，可以點選**自訂**並填寫 Model Garden 或 Google 官方文件中的模型 ID。

- Gemini 模型使用 Google Generate Content 能力；
- Claude 模型會使用 Vertex Anthropic 路由；
- 模型必須在目前的專案和 Location 中可用；
- 第三方模型可能需要額外啟用、授權或接受條款；
- 模型名稱、地區和版本需要同時相符，不能只複製其他專案中的模型 ID。

舊版文件中「暫時不支援 Claude」的說明已不適用於 V2，但程式碼支援路由不代表你的 Google Cloud 專案已經取得該模型的權限。

## 檢查連線

1. 確認四個必填欄位都來自同一個 Service Account 和專案；
2. 確認 Vertex AI API 已啟用；
3. 確認 Service Account 具有所需的 IAM 權限；
4. 選擇一個已新增並啟用的模型；
5. 執行連線檢查；
6. 再執行模型健康檢查；
7. 回到對話介面傳送一則簡單訊息。

如果 Gemini 可用但 Claude 不可用，請優先檢查 Claude 是否已在目前的專案、地區和 Model Garden 中開放，而不是修改 Gemini 設定。

## 管理多個專案或地區

不同專案或地區使用不同憑證時，可以複製 VertexAI 服務商並分別設定：

- 在名稱中標記專案或地區；
- 每個副本只保留該環境可用的模型；
- 不要混用專案 A 的 Service Account 與專案 B 的專案 ID；
- 輪替金鑰時逐一驗證副本；
- 正式環境與測試環境使用不同的 Service Account。

這樣可以縮小權限範圍，也更容易區分配額、地區和模型可用性問題。

## 常見問題

### 提示 VertexAI 未設定

專案 ID、Location、Client Email 或私密金鑰至少有一項為空。請檢查私密金鑰是否完整，並在欄位失去焦點後等待設定儲存。

### 傳回 401 或驗證失敗

Service Account 金鑰無效、已刪除、私密金鑰格式損壞，或 Client Email 與私密金鑰不相符。請重新從同一份 JSON 核對欄位。

### 傳回 403

Vertex AI API 未啟用、Service Account 缺少 IAM 權限，或目標模型尚未對專案開放。請在 Google Cloud 中檢查專案、API 和角色。

### 傳回 404 或模型不存在

模型 ID、專案或 Location 不相符。請到 Model Garden 核對目標模型支援的地區，再更新 Cherry Studio。

### 傳回 429

目前的專案、地區或模型已達配額限制。請在 Google Cloud Console 中檢查配額和用量。

### Gemini 可以使用，但 Claude 不能使用

確認 Claude 模型已在目前的專案和地區開放，並使用完整、正確的模型 ID。Vertex AI 的 Gemini 權限不會自動授予第三方模型權限。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
