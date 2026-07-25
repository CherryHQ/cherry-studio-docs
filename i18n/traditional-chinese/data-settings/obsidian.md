---
description: 將 Cherry Studio V2 的話題、訊息或筆記匯出到本機 Obsidian 保管庫。
icon: gem
---

# Obsidian 設定與匯出

Cherry Studio V2 可以將完整話題、單一訊息或 Cherry Studio 筆記匯出為 Obsidian 中的 Markdown 檔案。匯出會使用 Obsidian 內建的 `obsidian://` URI 和系統剪貼簿，不需要安裝第三方 Obsidian 外掛程式。

設定入口位於 **設定 > 整合 > Obsidian**。**資料設定 > 匯出選單**只會控制「匯出到 Obsidian」是否出現在選單中。

{% hint style="warning" %}
「新建（如果存在則覆寫）」會取代相同路徑的現有 Markdown 檔案。第一次使用時，請建立測試資料夾，並先備份重要的 Vault。
{% endhint %}

## 使用前準備

1. 在目前的電腦上安裝 Obsidian，並至少啟動一次。
2. 在 Obsidian 中開啟目標本機 Vault。
3. 確認 Vault 資料夾仍然存在，而且目前使用者可以讀寫。
4. 重新開啟 Cherry Studio 的 Obsidian 設定。

Cherry Studio 會讀取 Obsidian 的本機設定，並列出這部電腦上已經登記的 Vault：

- Windows：讀取使用者應用程式資料中的 Obsidian 設定；
- macOS：讀取 `~/Library/Application Support/obsidian/obsidian.json`；
- Linux：相容於常見的 XDG、Snap 和 Flatpak 設定位置。

只同步到其他電腦，但從未在目前 Obsidian 用戶端中開啟過的 Vault，不會自動出現在清單中。

## 選擇預設 Vault

1. 開啟 **設定 > 整合 > Obsidian**。
2. 在 **預設 Obsidian 儲存庫**中選擇目標 Vault。
3. 返回對話頁面。

如果尚未選擇預設值，Cherry Studio 會在發現 Vault 後使用清單中的第一個。匯出時仍可以在彈出視窗中暫時改選其他 Vault。

{% hint style="info" %}
Cherry Studio 介面中的「儲存庫」和「保管庫」都表示 Obsidian Vault。此處選擇的是 Vault 名稱，不是 Obsidian Sync 的遠端 Vault 或帳號。
{% endhint %}

## 啟用匯出選單

如果選單中沒有「匯出到 Obsidian」：

1. 開啟 **設定 > 資料設定 > 匯出選單**。
2. 開啟 **匯出到 Obsidian**。
3. 返回對話或筆記，重新開啟匯出選單。

此開關只會控制入口是否顯示，不會影響 Vault 發現或 `obsidian://` 通訊協定。

## 開啟匯出彈出視窗

### 匯出完整話題

在左側話題清單中開啟目標話題的選單，選擇 **匯出到 Obsidian**。

完整話題會依訊息順序轉換為 Markdown。預設處理方式為 **新建（如果存在則覆寫）**。

### 匯出單一訊息

開啟訊息選單，選擇 **匯出到 Obsidian**。

單一訊息只會匯出目前的訊息內容。彈出視窗仍允許修改標題、目標路徑和處理方式。

### 匯出 Cherry Studio 筆記

在筆記選單中選擇 **匯出到 Obsidian**。筆記會使用目前的 Markdown 內容，不會顯示「匯出思維鏈」開關。

## 設定匯出彈出視窗

| 欄位 | 作用 |
| --- | --- |
| 標題 | 新建檔案的檔案名稱來源，也是新建模式下的 YAML `title` |
| 保管庫 | 本次匯出的目標 Obsidian Vault |
| 路徑 | Vault 根目錄、現有資料夾或現有 `.md` 檔案 |
| 標籤 | 新建模式下寫入 YAML `tags`，多個標籤使用半形逗號分隔 |
| 建立時間 | 新建模式下寫入 YAML `created` |
| 來源 | 新建模式下寫入 YAML `source`，預設為 `Cherry Studio` |
| 處理方式 | 新建/覆寫、前置或附加 |
| 匯出思維鏈 | 對話或訊息存在思考內容時，決定是否一併匯出 |

標題不能為空。新建檔案時，Cherry Studio 會移除各平台不允許的檔案名稱字元，並截短過長的名稱。

### 選擇路徑

路徑選擇器會讀取目標 Vault 中的資料夾和 Markdown 檔案，並忽略以 `.` 開頭的隱藏項目。

- 選擇 **根目錄** 或某個資料夾時，會依標題產生新的 `.md` 檔案名稱。
- 選擇現有 `.md` 檔案時，會直接使用該檔案路徑，標題會自動改成檔案名稱，並預設切換為 **附加**。
- 切換 Vault 後，需要重新選擇路徑。

目錄樹狀結構為空時，請先確認 Vault 路徑仍然存在，並檢查 Cherry Studio 是否有權限讀取該目錄。

## 三種處理方式

| 處理方式 | 現有同名檔案 | 寫入位置 | YAML Properties |
| --- | --- | --- | --- |
| 新建（如果存在則覆寫） | 覆寫現有內容 | 取代整個檔案 | 寫入 `title`、`created`、`source`、`tags` |
| 前置 | 保留現有內容 | 將新內容加到開頭 | 不寫入新的 Properties |
| 附加 | 保留現有內容 | 將新內容加到末尾 | 不寫入新的 Properties |

前置和附加會在新舊內容之間加入 Markdown 分隔線。它們不會嘗試合併標題或重新產生現有 YAML。

{% hint style="warning" %}
選擇資料夾並使用「新建（如果存在則覆寫）」時，標題會決定目標檔案名稱。目標目錄中已有同名檔案時，該檔案會被取代。
{% endhint %}

## 匯出思考內容

對話和訊息匯出彈出視窗提供 **匯出思維鏈** 開關：

- 關閉：只匯出一般回答內容；
- 開啟：訊息存在思考 / 推理內容時一併寫入。

匯出內容會成為一般 Markdown。需要將檔案分享給他人或公開發佈時，請先檢查其中是否包含草稿、中間過程或敏感資訊。

該開關不會產生原本不存在的思考內容，也不會出現在 Cherry Studio 筆記匯出中。

## 匯出如何完成

點擊確認後，Cherry Studio 會：

1. 將 Markdown 內容寫入系統剪貼簿；
2. 建構包含 Vault、檔案路徑和處理方式的 `obsidian://new` URI；
3. 請求系統開啟 Obsidian；
4. 由 Obsidian 從剪貼簿建立、覆寫、前置或附加檔案。

因此，Cherry Studio 中的成功提示表示匯出請求已經送出，不代表檔案一定已經寫入。切換到 Obsidian 後，應確認目標檔案存在且內容正確。

此流程以 [Obsidian 官方 URI](https://help.obsidian.md/Extending%2BObsidian/Obsidian%2BURI)提供的 `clipboard`、`append` 和 `overwrite` 等參數為基礎。

## 常見問題

### 設定中顯示「找不到 Obsidian 儲存庫」

請先在相同的系統使用者帳號下啟動 Obsidian，開啟目標本機 Vault，再重新進入 Cherry Studio 設定。只有 Obsidian 本機設定中登記過的 Vault 才會被發現。

### 可以看到 Vault，但路徑清單為空

Vault 資料夾可能已經移動、離線或沒有讀取權限。返回 Obsidian，確認 Vault 可以正常開啟，並檢查外接磁碟或網路目錄是否在線上。

### 點擊匯出後 Obsidian 沒有開啟

系統可能尚未登記 `obsidian://` 通訊協定。Windows 和 macOS 通常會在執行 Obsidian 後自動登記；Linux 需要確認桌面檔案的 `Exec` 支援 `%u` 參數。你可以參閱 Obsidian 官方 URI 文件中的登記說明。

### Cherry Studio 提示成功，但沒有產生筆記

成功提示只表示 URI 已經送出。請檢查 Obsidian 是否已彈出、目標 Vault 是否正確，以及系統是否允許 Cherry Studio 開啟外部通訊協定。也應確認剪貼簿沒有被安全軟體阻止或立即改寫。

### 匯出覆寫了舊筆記

「新建（如果存在則覆寫）」會取代相同路徑的檔案。你可以從 Vault 備份、版本控制或 Obsidian Sync 版本歷史記錄還原；後續請改用不同的標題、其他資料夾、前置或附加。

### 前置或附加後沒有 Properties

這是目前的設計。只有新建/覆寫模式會產生 YAML Properties；前置和附加只會寫入分隔線與 Markdown 正文。

### 對話選單中沒有 Obsidian

前往 **設定 > 資料設定 > 匯出選單**，開啟 **匯出到 Obsidian**。如果已經開啟，請重新進入目前的對話，再開啟選單。

### Linux 上仍然找不到 Vault

請確認 Obsidian 的安裝方式和設定路徑。Cherry Studio 會檢查常見的 XDG、Snap 與 Flatpak 位置，但自訂可攜式版本或非標準路徑可能無法自動發現。

如果仍無法解決，請透過[意見回饋與建議](../question-contact/suggestions.md)提交 Cherry Studio 與 Obsidian 版本、作業系統、安裝方式、是否可以開啟 `obsidian://` 連結，以及已移除敏感資訊的 Vault 名稱和路徑。
