# 自動安裝 MCP

Cherry Studio 內建的 `@cherry/mcp-auto-install` 可以協助模型探索 MCP 伺服器、讀取設定說明並產生啟動指令。當你不確定套件名稱或設定格式時，可以將它作為安裝助手。

{% hint style="warning" %}
此功能仍處於測試階段。目前 V2 會以 JSON 模式執行安裝助手，但不保證將產生的伺服器設定直接寫入 Cherry Studio。請將它視為「探索並產生設定」工具，並在匯入前人工檢查結果。
{% endhint %}

## 工作流程

一次完整的輔助安裝通常分為四個步驟：

1. 模型使用安裝助手搜尋可用伺服器並讀取設定說明。
2. 安裝助手傳回建議的指令、參數和環境變數。
3. 你檢查套件來源和設定內容，再將 JSON 匯入 Cherry Studio。
4. 在 MCP 設定中啟用新伺服器，並檢查工具和日誌。

安裝助手本身會透過以下預設啟動：

```text
npx -y @mcpmarket/mcp-auto-install connect --json
```

Cherry Studio 會管理其使用的本機 Registry 路徑，無需手動填寫 `MCP_REGISTRY_PATH`。

## 啟用安裝助手

1. 開啟**設定 → MCP 伺服器**。
2. 在內建伺服器中搜尋 `@cherry/mcp-auto-install`。
3. 按一下**安裝**，然後在已安裝清單中啟用它。
4. 在目標助手或 Agent 的工具設定中新增 `@cherry/mcp-auto-install`。
5. 選擇支援工具呼叫的模型。

首次啟動需要執行 NPX 套件。Cherry Studio 會優先使用系統中的 NPX；如果無法使用，則會嘗試內建 Bun。相依套件異常時，可以在 MCP 設定中執行相依套件安裝程式並重新啟動應用程式。

## 產生伺服器設定

向模型說明用途、執行平台和輸出格式，比只說「安裝一個 MCP」更容易取得可用的結果。例如：

```text
請使用 MCP 自動安裝工具，尋找一個可以唯讀存取本機 SQLite 資料庫的 MCP 伺服器。
我的系統是 macOS。

請先說明套件來源和所需權限，再產生可匯入 Cherry Studio 的 JSON 設定。
不要替我啟用伺服器，也不要填寫真實金鑰。
```

安裝助手可以提供以下功能：

- 列出 Registry 中可探索的 MCP 伺服器；
- 讀取特定伺服器的 README 和設定建議；
- 根據伺服器產生指令、參數和環境變數；
- 管理安裝助手本身的本機伺服器註冊資訊。

模型傳回設定後，請至少檢查：

- npm 套件名稱、發佈者和文件位址是否可信；
- `command` 與 `args` 是否和專案官方說明一致；
- 是否包含下載指令碼、Shell 指令或不需要的高權限參數；
- 環境變數名稱是否正確，以及是否仍包含預留位置值；
- 伺服器將存取哪些本機檔案、網路服務或帳號。

## 匯入 Cherry Studio

請模型將結果整理為以下結構，每次只保留一個伺服器：

```json
{
  "mcpServers": {
    "example-server": {
      "command": "npx",
      "args": ["-y", "@example/mcp-server"],
      "env": {
        "EXAMPLE_API_KEY": "在 Cherry Studio 中取代"
      }
    }
  }
}
```

然後：

1. 開啟**設定 → MCP 伺服器**。
2. 按一下**新增伺服器 → 從 JSON 匯入**。
3. 貼上已經檢查過的設定。
4. 匯入後開啟伺服器詳細資料，取代預留位置值並儲存。
5. 啟用伺服器，在**工具**頁面檢查實際公開的工具。
6. 完成測試後，再將伺服器新增至需要使用它的助手或 Agent。

{% hint style="danger" %}
NPX 可以下載並執行第三方程式碼。請勿只依模型建議就執行陌生套件，也不要將 API Key 直接傳送給模型。請先核對軟體套件、版本、原始碼或官方文件，再到 Cherry Studio 的伺服器設定中填寫金鑰。
{% endhint %}

## 自訂搜尋範圍

安裝助手預設會從 `@modelcontextprotocol` npm scope 探索伺服器。如需搜尋其他 scope，請在 `@cherry/mcp-auto-install` 的伺服器詳細資料中新增環境變數：

```text
MCP_PACKAGE_SCOPES=@modelcontextprotocol,@your-scope
```

多個 scope 請使用半形逗號分隔。擴大搜尋範圍也會增加第三方套件的數量，因此應同時提高來源審查標準。

## 常見問題

### 對話中沒有呼叫安裝助手

確認 `@cherry/mcp-auto-install` 已啟用並新增至目前的助手或 Agent，同時使用支援工具呼叫的模型。你可以在提示詞中明確要求「先呼叫 MCP 自動安裝工具」。

### 提示找不到 NPX 或啟動失敗

在 MCP 設定中執行相依套件安裝程式，然後重新啟動 Cherry Studio。如果仍然失敗，請開啟伺服器日誌，檢查 NPX、內建 Bun、網路 Proxy 和 npm Registry。

### 找不到目標伺服器

預設搜尋範圍有限。請先確認套件所在的 npm scope，再透過 `MCP_PACKAGE_SCOPES` 新增該 scope。也可以略過自動安裝，直接依專案官方文件[手動設定 MCP](config.md)。

### 已產生設定，但伺服器清單沒有新增項目

這是目前 JSON 模式下的正常情況。請複製模型整理後的 `mcpServers` JSON，透過**新增伺服器 → 從 JSON 匯入**完成安裝。

### 匯入後無法啟用

安裝助手產生的是建議設定，仍可能缺少路徑、金鑰或平台參數。請依目標伺服器的官方文件修正設定，並參考 [MCP 伺服器常見問題](chang-jian-wen-ti.md)檢查日誌。

## 相關文件

- [`@mcpmarket/mcp-auto-install` 套件說明](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install)
- [設定與使用 MCP](config.md)
- [內建 MCP 伺服器](in-memory.md)
- [MCP 伺服器常見問題](chang-jian-wen-ti.md)
- [意見與建議](../../question-contact/suggestions.md)
