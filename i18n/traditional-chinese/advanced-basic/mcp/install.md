# MCP 環境安裝

Cherry Studio 可以管理兩種常用的 MCP 執行環境：

- **UV**：執行透過 `uv` 或 `uvx` 啟動的 Python MCP 伺服器；
- **Bun**：執行 JavaScript 工具，並在系統沒有 NPX 時作為部分 NPX 伺服器的備用執行環境。

{% hint style="info" %}
並非所有 MCP 伺服器都需要安裝 UV 和 Bun。遠端 SSE / Streamable HTTP 伺服器和多數 Cherry Studio 內建伺服器都不依賴這兩個執行環境。請根據伺服器文件中的 `command` 判斷需要安裝的項目。
{% endhint %}

## 使用應用程式內的安裝程式

1. 開啟**設定 → 環境相依套件**。
2. 找到 **UV** 或 **Bun**。
3. 對顯示為**未安裝**的項目按一下**安裝**。
4. 等待狀態變為**已安裝**。

MCP 伺服器頁面缺少環境相依套件時，也會顯示警告入口；按一下後會前往相同的環境相依套件頁面。

應用程式內的安裝程式會下載適合目前作業系統和 CPU 架構的執行檔，並將其儲存在 Cherry Studio 的私有目錄：

{% tabs %}
{% tab title="Windows" %}
`C:\Users\<使用者名稱>\.cherrystudio\bin`
{% endtab %}

{% tab title="macOS / Linux" %}
`~/.cherrystudio/bin`
{% endtab %}
{% endtabs %}

安裝完成後，可以按一下相依套件旁的資料夾圖示來開啟該目錄。

## 系統指令與私有執行環境

執行 STDIO 伺服器時，Cherry Studio 會依以下順序尋找：

### `uv` 和 `uvx`

1. 先在登入 Shell 環境中尋找系統安裝的 `uv` 或 `uvx`；
2. 如果找不到，再使用 Cherry Studio 安裝在 `~/.cherrystudio/bin` 中的 UV。

### `npx`

1. 先在登入 Shell 環境中尋找系統安裝的 `npx`；
2. 如果找不到，再嘗試使用 Cherry Studio 安裝的 Bun 執行該套件。

因此，已正確安裝在系統 PATH 中的 UV、UVX 或 NPX 也可以使用。**環境相依套件**頁面的「已安裝」狀態只會檢查 Cherry Studio 私有目錄，不代表系統指令一定無法使用。

{% hint style="warning" %}
如果剛在系統中安裝或修改了 Node.js、NPX、UV 或 UVX，請完全結束並重新開啟 Cherry Studio，讓應用程式重新讀取登入 Shell 環境。
{% endhint %}

## 如何判斷需要哪個執行環境

查看 MCP 開發者提供的設定：

| 設定中的指令 | 所需環境 |
| --- | --- |
| `uvx` 或 `uv` | UV |
| `npx` | Node.js 提供的 NPX，或 Cherry Studio 的 Bun 備用環境 |
| `bun` 或 `bunx` | Bun |
| `node` | 系統 Node.js |
| 其他指令 | 依開發者文件安裝對應的程式 |
| 只有遠端 URL | 通常不需要本機執行環境 |

Cherry Studio 的環境相依套件頁面不會安裝 Node.js 或任何第三方系統指令。

## 手動安裝作為備用方式

如果應用程式內下載失敗，可以依執行環境的官方文件在系統中安裝：

- [UV 官方安裝說明](https://docs.astral.sh/uv/getting-started/installation/)
- [Bun 官方安裝說明](https://bun.com/docs/installation)
- [Node.js 下載](https://nodejs.org/en/download)

安裝後，請在系統終端機中驗證：

```bash
uv --version
bun --version
npx --version
```

你只需要驗證實際會使用的指令。驗證成功後，重新啟動 Cherry Studio，再啟用 MCP 伺服器。

進階使用者也可以將符合目前系統和架構的執行檔放入 `~/.cherrystudio/bin`，Windows 則使用對應的使用者目錄。請勿從不受信任的來源下載二進位檔。

## 常見問題

### 按一下安裝後失敗

請依序檢查：

- 目前網路是否可以存取執行環境下載來源；
- Proxy、防火牆或安全軟體是否封鎖 Cherry Studio；
- 使用者目錄是否有寫入權限；
- 作業系統與 CPU 架構是否有對應的安裝套件；
- 磁碟空間是否足夠。

### 已安裝，但伺服器仍提示找不到指令

確認伺服器詳細資料中的**指令**拼字正確，例如 `uvx` 不要寫成完整的參數字串。參數應逐行填寫在**參數**欄位。

如果使用系統安裝的指令，請在終端機中驗證後重新啟動 Cherry Studio。如果使用應用程式內的執行環境，請開啟相依套件目錄，確認對應的執行檔存在。

### UV 和 Bun 都已安裝，但伺服器仍無法啟動

執行環境只負責啟動程式，無法修正錯誤的參數、缺少 API Key 或伺服器本身的故障。請開啟 MCP 伺服器詳細資料中的日誌，並參考 [MCP 伺服器常見問題](chang-jian-wen-ti.md)。

## 相關文件

- [MCP 使用教學](README.md)
- [設定與使用 MCP](config.md)
- [MCP 伺服器常見問題](chang-jian-wen-ti.md)
- [意見與建議](../../question-contact/suggestions.md)
