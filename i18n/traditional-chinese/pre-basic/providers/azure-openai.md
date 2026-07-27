---
icon: cloud
---

# Azure OpenAI

Cherry Studio V2 的 Azure OpenAI 內建範本用於連線部署在 Microsoft Azure 上的模型。它會根據 **API Version** 選擇 Azure Responses 或部署式呼叫方式，因此 Base URL、API Version 和模型 ID 必須與 Azure 資源中的設定相符。

{% hint style="info" %}
Azure OpenAI 與 OpenAI 官方 API 是兩個獨立服務。Azure 資源的 Endpoint、API Key、API Version 和部署名稱不能直接填入 OpenAI 範本。
{% endhint %}

## 開始前的準備

在 [Azure Portal](https://portal.azure.com/) 準備以下資訊：

- Azure AI Foundry 或 Azure OpenAI 資源的 Endpoint；
- 該資源對應的 API Key；
- 目前資源支援的 API Version；
- 至少一個可呼叫的模型部署。

若使用日期格式的 API Version，還需要記住每個模型的**部署名稱**。部署名稱由你在 Azure 中設定，可能與底層模型名稱不同。

## 設定 Azure OpenAI

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**，選擇 **Azure OpenAI**；
3. 輸入 Azure 資源的 API Key；
4. 在 Base URL 中填寫資源 Endpoint，例如 `https://<resource>.openai.azure.com`；
5. 填寫 Azure 資源目前支援的 API Version；
6. 開啟頁面頂端的服務商開關；
7. 新增並啟用準備使用的模型；
8. 執行連線檢查和模型健康檢查。

{% hint style="warning" %}
Base URL 只填寫資源 Endpoint。不要附加 `/openai`、`/v1`、`/chat/completions` 或部署路徑；Cherry Studio 會根據目前設定補上請求路徑。
{% endhint %}

{% hint style="danger" %}
不要把 Azure API Key 寫入聊天訊息、文件、程式碼儲存庫或問題截圖。Key 洩漏後，應立即在 Azure Portal 中重新產生。
{% endhint %}

## 選擇 API Version

Cherry Studio 會根據 API Version 選擇呼叫方式：

| API Version | Cherry Studio 的處理方式 | 模型設定重點 |
| --- | --- | --- |
| `v1` 或 `preview` | 使用 Azure Responses 方式 | 依目前 Azure 資源提供的模型路由設定 |
| 日期格式版本，例如 `2024-xx-xx-preview` | 使用 Azure 部署式 URL | 模型 ID 應與 Azure 中的部署名稱一致 |

API Version 必須是 Azure 資源實際支援的值。介面中的範例只用於說明格式，不代表該版本一定適用於你的資源。

如果現有連線升級後突然傳回 404，先到 Azure Portal 或 [Azure OpenAI 文件](https://learn.microsoft.com/azure/ai-services/openai/)核對目前的 Endpoint、API Version 和部署名稱，再修改 Cherry Studio。

## 新增並啟用模型

在模型列表點選**新增**，檢查同步預覽並套用變更。若 Azure 未傳回可用列表，可以點選**自訂**手動填寫模型。

使用日期格式 API Version 時：

- **模型 ID**填寫 Azure 中的部署名稱；
- 不要只填寫底層模型家族名稱，除非它剛好也是部署名稱；
- 多個部署需要分別新增；
- 刪除或重新命名 Azure 部署後，也要同步修改 Cherry Studio 中的模型。

例如，Azure 中將某個模型部署為 `support-prod`，則 Cherry Studio 中的模型 ID 應填寫 `support-prod`，而不是根據底層模型名稱猜測。

## 檢查連線

1. 確認 Base URL 沒有附加 API 路徑；
2. 確認 API Key 來自同一個 Azure 資源；
3. 確認 API Version 受該資源支援；
4. 選擇一個已新增並啟用的模型；
5. 執行連線檢查；
6. 再執行模型健康檢查；
7. 回到對話介面傳送一則簡單訊息。

連線檢查成功只表示憑證和基本請求可用。若準備使用圖片、推理或工具呼叫，還應分別驗證對應模型與部署是否支援這些能力。

## 管理多個資源或部署

如果不同 Azure 資源使用不同的 Endpoint、Key 或 API Version，可以複製 Azure OpenAI 服務商並分別設定：

- 為每個副本設定容易識別的名稱；
- 每個副本只保留該資源實際存在的部署；
- 不要在一個副本中混用其他資源的 Key 或部署名稱；
- 升級 API Version 時先測試一個副本，再更新其他連線。

這樣可以隔離正式、測試或不同區域的資源，也更容易找出配額與權限問題。

## 常見問題

### 傳回 401

API Key 無效、複製不完整，或 Key 與 Base URL 不屬於同一個 Azure 資源。請重新從資源的 Keys and Endpoint 頁面核對。

### 傳回 404

依序檢查 Base URL、API Version 和模型部署名稱。最常見的原因是附加了多餘路徑、日期版本不受支援，或將底層模型名稱當成部署名稱。

### 傳回 429

目前資源、區域或部署已達速率或配額限制。請在 Azure Portal 檢查配額和使用量；切換 Cherry Studio 中的模型名稱不會繞過資源限制。

### 無法同步模型

部分 Azure 設定不會傳回適合直接使用的模型列表。點選**自訂**，依 Azure 中的實際部署新增模型，再執行健康檢查。

### `v1`、`preview` 與日期版本應該選哪一個

以 Azure 資源和官方文件目前支援的方式為準。`v1` 或 `preview` 會使用 Responses 方式；日期版本會使用部署式 URL。不要只根據模型名稱切換 API Version。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
