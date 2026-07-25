---
icon: cherries
---

# Cherry Studio 社群版

Cherry Studio 是一款開源的桌面 AI 用戶端，可在 Windows、macOS 和 Linux 上統一使用雲端或本機大型模型。它不僅提供多模型對話，還將助手、Agent、知識庫、技能、MCP、翻譯、繪畫、檔案和筆記等功能整合在同一個工作空間中。

社群版適合希望自行選擇模型服務、在本機管理工作資料，並依需求擴充 AI 工作流程的個人使用者和開發者。

## 你可以用它做什麼

| 需求 | Cherry Studio 中的功能 |
| :--- | :--- |
| 使用不同廠商或本機部署的模型 | 統一設定模型服務，在對話中切換或同時比較多個模型 |
| 儲存固定角色和對話設定 | 建立助手，設定提示詞、模型參數、知識庫和 MCP |
| 讓 AI 讀取工作區並執行任務 | 建立 Agent，控制可存取目錄、工具和核准模式 |
| 讓 AI 遵循專門的工作流程 | 安裝技能，並依 Agent 啟用 |
| 連接搜尋、資料庫或第三方服務 | 新增本機或遠端 MCP Server |
| 建立自己的資料檢索庫 | 匯入文件並設定 Embedding 模型 |
| 處理圖片、翻譯、筆記和檔案 | 使用繪畫、翻譯、筆記和檔案等獨立工作空間 |
| 在聊天平台或固定時間執行 Agent | 設定頻道和排程任務 |

## 主要工作空間

Cherry Studio V2 的側邊欄可以依需求顯示以下應用程式：

* **對話**：與助手和模型交流，管理工作階段和訊息。
* **Agent**：執行需要檔案、指令或多步驟工具呼叫的任務。
* **資源庫**：集中管理助手、Agent、技能和提示詞。
* **繪畫**：使用圖像產生模型建立和管理圖片。
* **翻譯**：進行雙語翻譯和對照閱讀。
* **小程式**：在應用程式內開啟已新增的 Web 工具。
* **知識庫**：匯入資料、處理分段並進行檢索。
* **檔案**：集中查看和管理應用程式中的檔案資源。
* **Code Tools**：管理開發者使用的程式碼工具。
* **筆記**：編輯和整理 Markdown 筆記。
* **OpenClaw**：使用獨立的自主 Agent 工作空間。

側邊欄只會顯示已啟用的入口；隱藏項目不會刪除對應資料。

## 快速開始

### 1. 下載並安裝

前往[用戶端下載](cherrystudio/download.md)，選擇適合系統的版本。首次安裝或遇到系統安全提示時，請參考[安裝教學](pre-basic/installation/)。

Cherry Studio 支援 Windows、macOS 和 Linux。不同系統和晶片架構使用的安裝套件不同，請依下載頁面的說明選擇。

### 2. 設定模型服務

開啟**設定 → 模型服務**：

1. 選擇現有服務提供者，或新增相容的服務提供者。
2. 填寫 API 位址和 API Key。
3. 取得模型清單，啟用需要使用的模型。
4. 返回對話頁面，選擇模型並傳送第一則訊息。

如果使用 Ollama、LM Studio 等本機服務，請先確認對應服務已在本機執行。詳細步驟請參閱[模型服務](pre-basic/providers/)。

### 3. 從一個情境開始

* 日常問答、寫作或翻譯：從[對話介面](cherrystudio/preview/chat.md)開始。
* 需要固定提示詞和參數：在[資源庫](cherrystudio/preview/library.md)建立助手。
* 需要操作本機檔案或執行工具：建立 [Agent](advanced-basic/agent.md)。
* 需要根據個人資料回答：建立[知識庫](knowledge-base/knowledge-base.md)。

不需要一次設定全部功能。請先完成一個可驗證的小型任務，再增加技能、MCP 或自動化，疑難排解會更容易。

## 助手、Agent 與擴充功能

### 助手

助手會儲存可重複使用的對話設定，包括提示詞、模型參數、知識庫和 MCP。它適合以對話為主的穩定情境。

### Agent

Agent 可以存取指定目錄，並呼叫內建工具、MCP 和技能。你可以選擇一般、規劃、自動編輯或全自動權限模式。詳見 [Agent](advanced-basic/agent.md)。

### 技能與 MCP

* [技能](pre-basic/settings/skills.md)告訴 Agent 如何依特定流程完成一類工作。
* [MCP](advanced-basic/mcp/)為助手或 Agent 連接外部工具、提示和資源。

如果還不確定該如何選擇，請先閱讀[概念入門](advanced-basic/concepts-101.md)。

## 資料與安全

Cherry Studio 的應用程式設定和工作資料主要儲存在本機，但「使用桌面應用程式」不代表「所有處理都在本機完成」：

* 使用雲端模型時，訊息、附件或檢索到的上下文會依請求需要傳送給選定的模型服務提供者。
* 使用遠端 MCP Server、頻道或其他第三方服務時，相關資料可能會傳送給對應服務。
* Agent 和本機 MCP Server 可能依已授予的權限讀取檔案或執行指令。
* 使用本機模型可以減少雲端資料傳輸，但仍需要檢查所連接的模型服務、外掛程式和網路工具。

{% hint style="warning" %}
請勿將 API Key、存取權杖、密碼或私密金鑰寫入提示詞、知識庫、文件和截圖。請限制 Agent 的可存取目錄，為 MCP 和頻道使用最小權限，並在啟用全自動模式前先完成受控測試。
{% endhint %}

重要資料應定期備份。Cherry Studio 支援本機匯出，以及 WebDAV、S3 相容儲存空間等備份方式；具體選項請參閱[資料設定](data-settings/)。

## 開放原始碼與授權

Cherry Studio 社群版程式碼託管於 [GitHub](https://github.com/CherryHQ/cherry-studio)，並採用 GNU Affero General Public License v3.0（AGPL-3.0）。在使用、修改或散布前，請閱讀[開放原始碼授權協議](contact-us/questions/cherrystudio-xu-ke-xie-yi.md)。

歡迎參與：

* [貢獻程式碼](contribution/code.md)
* [貢獻文件](contribution/docs.md)
* [提交問題](https://github.com/CherryHQ/cherry-studio/issues)
* [參與討論](https://github.com/CherryHQ/cherry-studio/discussions)

## 取得協助

遇到問題時，請先查看[常見問題](question-contact/questions.md)和[如何有效提問](question-contact/ask.md)。提交意見反應時，請提供 Cherry Studio 版本、作業系統、重現步驟和必要日誌，並先移除 API Key、檔案內容等敏感資訊。

社群入口：

* [Telegram](https://t.me/CherryStudioAI)
* [Discord](https://discord.gg/wez8HtpxqQ)
* [QQ 群組](https://qm.qq.com/q/lo0D4qVZKi)
* [意見與建議](question-contact/suggestions.md)
