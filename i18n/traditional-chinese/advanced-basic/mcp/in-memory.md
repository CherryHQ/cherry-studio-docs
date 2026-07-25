# 內建 MCP 伺服器

Cherry Studio 提供一組可以直接安裝的內建 MCP 伺服器。它們由應用程式內建執行或使用預設連線，無需手動撰寫 JSON 設定，適合快速為助手和 Agent 增加網頁讀取、檔案操作、程式碼執行、記憶及第三方服務等功能。

{% hint style="info" %}
「內建」不代表全部自動啟用。你需要先從內建清單安裝伺服器；帶有**需要設定**標記的伺服器，還必須填寫參數或環境變數。
{% endhint %}

## 安裝與使用

1. 開啟**設定 → MCP 伺服器**。
2. 在**內建伺服器**區域尋找需要的伺服器，也可以切換至**可安裝**篩選條件。
3. 按一下**安裝**。
4. 如果伺服器顯示**需要設定**，請返回已安裝伺服器清單並按一下該伺服器，填寫本頁說明的參數。
5. 儲存並啟用伺服器。
6. 在目標助手或 Agent 的工具設定中新增該 MCP 伺服器。

對話時還需要使用支援工具呼叫的模型。如果只安裝伺服器，但未將其新增至目前的助手或 Agent，模型便無法使用其中的工具。

## 目前的內建伺服器

| 伺服器 | 主要用途 | 是否需要額外準備 |
| --- | --- | --- |
| `@cherry/fetch` | 以 HTML、Markdown、純文字或 JSON 讀取 URL | 否 |
| `@cherry/browser` | 開啟和操作動態網頁、管理分頁、截圖 | 否 |
| `@cherry/filesystem` | 在限定目錄內尋找、讀取、編輯和刪除檔案 | 設定允許存取的目錄 |
| `@cherry/python` | 在 Pyodide 環境中執行 Python 程式碼 | 否 |
| `@cherry/brave-search` | Brave 網頁搜尋與本機地點搜尋 | `BRAVE_API_KEY` |
| `@cherry/memory` | 使用本機知識圖譜儲存跨對話記憶 | `MEMORY_FILE_PATH` |
| `@cherry/sequentialthinking` | 為複雜任務提供分步、修訂和分支思考工具 | 否 |
| `@cherry/dify-knowledge` | 查詢 Dify 知識庫 | API 位址和 `DIFY_KEY` |
| `@cherry/flomo` | 將筆記和想法寫入 flomo | flomo 帳號授權 |
| `@cherry/didi-mcp` | 地點搜尋、價格預估和叫車訂單操作 | `DIDI_API_KEY`，僅支援中國大陸 |
| `@cherry/nowledge-mem` | 連線至本機執行的 Nowledge Mem | 安裝並執行 Nowledge Mem |
| `@cherry/mcp-auto-install` | 讓模型搜尋並安裝其他 MCP 伺服器 | 測試功能，需要可用的 NPX 或內建 Bun |

## 網頁與程式碼工具

### `@cherry/fetch`

適合讀取不需要複雜互動的網頁或介面。它提供 HTML、Markdown、純文字和 JSON 四種讀取方式，並支援在請求中傳入自訂 Header。

如果頁面依賴登入狀態、JavaScript 轉譯或點選操作，請改用 `@cherry/browser`。

### `@cherry/browser`

透過 Cherry Studio 管理的 Electron 瀏覽器視窗操作網頁，支援：

- 開啟 URL 並執行頁面指令碼；
- 取得頁面快照或截圖；
- 列出、切換和關閉分頁；
- 重設瀏覽工作階段。

瀏覽器會接觸頁面內容和可能存在的登入狀態。使用前請檢查模型準備存取的網站，不要讓不受信任的提示詞執行敏感帳號操作。

### `@cherry/python`

提供 `python_execute` 工具，在 Pyodide 環境中執行 Python 3.12 程式碼。適合資料計算、文字處理和格式轉換，也可以透過 PEP 723 中繼資料宣告相依套件。

每次呼叫的預設逾時時間為 60 秒。它不是完整的本機 Python 環境；依賴原生二進位檔、系統指令或特定硬體的程式碼可能無法執行。

### `@cherry/sequentialthinking`

為模型提供可修訂、可分支的分步思考工具。它適合複雜的規劃和分析任務，但不會自動提高所有回答的品質；簡單問題通常不需要啟用。

## 本機檔案與記憶

### `@cherry/filesystem`

提供 `glob`、`ls`、`grep`、`read`、`edit`、`write` 和 `delete` 工具。伺服器只應存取你明確授權的工作目錄。

安裝後，在伺服器詳細資料中使用以下任一方式設定目錄：

- **參數**：第一行填寫工作目錄的絕對路徑；
- **環境變數**：填寫 `WORKSPACE_ROOT=絕對路徑`。

如果兩者同時存在，`WORKSPACE_ROOT` 優先。`~` 可以展開為使用者目錄，但為了減少歧義，建議填寫完整的絕對路徑。

{% hint style="warning" %}
在預設情況下，`write`、`edit` 和 `delete` 不會自動核准。請勿擴大授權目錄，也不要為了省略確認而一次核准不熟悉的寫入或刪除操作。
{% endhint %}

### `@cherry/memory`

將實體、關係和觀察記錄儲存在本機 JSON 檔案中，供模型跨對話讀取和更新。安裝後請設定：

```text
MEMORY_FILE_PATH=/絕對路徑/memory.json
```

這是 MCP 伺服器本身的知識圖譜記憶，與 Cherry Studio 的[全域記憶](../memory.md)是兩套獨立功能。一般使用者可以先使用全域記憶；只有需要直接控制實體和關係時，才啟用此伺服器。

### `@cherry/nowledge-mem`

連線至本機的 `http://127.0.0.1:14242/mcp`。使用前需要安裝並執行 [Nowledge Mem](https://mem.nowledge.co/)；無需在 Cherry Studio 中填寫遠端 URL。

## 搜尋、知識庫與第三方服務

### `@cherry/brave-search`

提供網頁搜尋和本機地點搜尋。請先從 [Brave Search API](https://brave.com/search/api/) 取得金鑰，然後在伺服器詳細資料中填寫：

```text
BRAVE_API_KEY=你的 API Key
```

### `@cherry/dify-knowledge`

列出並檢索 Dify 知識庫。你需要在**參數**中填寫知識庫 API 根位址，並在**環境變數**中填寫 `DIFY_KEY`。完整步驟請參閱[連接 Dify 知識庫](dify.md)。

### `@cherry/flomo`

透過 flomo 的遠端 MCP 位址連接帳號。安裝並啟用後，如果出現授權頁面，請依提示完成 flomo 帳號授權。請勿在 Cherry Studio 的參數或環境變數中貼上 flomo 登入密碼。

### `@cherry/didi-mcp`

提供地點搜尋、價格預估、建立或取消叫車訂單、查詢訂單和駕駛位置等工具。安裝後請填寫：

```text
DIDI_API_KEY=你的 API Key
```

此服務僅支援中國大陸。建立訂單和取消訂單會產生真實的外部操作，建議在**工具**頁面關閉這些工具的自動核准。

### `@cherry/mcp-auto-install`

允許模型在對話中搜尋並安裝其他 MCP 伺服器，目前屬於測試功能。此預設會透過 NPX 啟動；如果啟動失敗，請先在 MCP 設定中檢查並安裝執行相依套件。詳細說明請參閱[自動安裝 MCP](auto-install.md)。

## 權限建議

內建伺服器使用統一的 MCP 權限設定。安裝後建議逐項檢查：

- 只啟用目前任務需要的伺服器和工具；
- 檔案、瀏覽器、記憶和第三方帳號工具只授權必要範圍；
- 寫入檔案、刪除檔案、建立訂單、取消訂單等操作保留人工確認；
- 不再使用的伺服器應及時停用或解除安裝；
- API Key 只儲存在伺服器設定中，不要放入提示詞、截圖或共用記錄。

## 常見問題

### 已安裝，但在對話中找不到工具

確認伺服器已啟用，且已新增至目前的助手或 Agent。然後檢查所選模型是否支援工具呼叫。

### 顯示「需要設定」

安裝後，按一下已安裝伺服器清單中的對應項目，在**設定**頁面填寫參數或環境變數並儲存。參數和環境變數均為一行一項。

### 伺服器啟用失敗

開啟伺服器詳細資料中的日誌，先檢查缺少參數、無效的 API Key、目錄權限或本機相依套件。更多疑難排解方法請參閱 [MCP 伺服器常見問題](chang-jian-wen-ti.md)。

## 相關文件

- [設定與使用 MCP](config.md)
- [自動安裝 MCP](auto-install.md)
- [MCP 伺服器常見問題](chang-jian-wen-ti.md)
- [意見與建議](../../question-contact/suggestions.md)
