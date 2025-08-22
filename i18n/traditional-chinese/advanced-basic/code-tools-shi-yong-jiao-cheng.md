---
description: Tools
icon: code
---
# Code Tools 使用教學


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




Cherry Studio v1.5.7 版本引入了操作簡單、強大的 Code Agent 功能，可以直接啟動和管理多種 AI 編程 agent。本教學將引導您完成設定和啟動的完整流程。

***

### 操作步驟

#### 1. 升級 Cherry Studio

首先，請確保您的 Cherry Studio 已升級至 **v1.5.7** 或更高版本。您可以前往 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 或官方網站下載最新版本。

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### 2. 調整導航列位置

為方便使用頂部標籤頁功能，建議將導航列調整至頂部。

* 操作路徑：`設定` -> `顯示設定` -> `導航列設定`
* 將「導航列位置」選項設為 **`頂部`**。

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### 3. 新增標籤頁

點擊介面頂部的「+」圖示，新增一個空白標籤頁。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 4. 開啟 Code Agent 功能

在新標籤頁中，點擊 `Code`（或 `</>`）圖示，進入 Code Agent 配置介面。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. 選擇 CLI 工具

根據需求和持有的 API Key，選擇要使用的 Code Agent 工具。目前支援以下幾種：

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. 選擇 Agent 調用的模型

在模型下拉清單中，選擇與 CLI 工具相容的模型。_（詳細模型相容性說明，請參考下方「重要注意事項」）_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. 指定工作目錄

點擊「選擇目錄」按鈕，為 Agent 指定工作目錄。Agent 將擁有此目錄下所有檔案和子目錄的存取權限，以協助理解專案內容、讀取檔案和執行程式碼。

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. 設定環境變數

* **自動配置**：您在第 6 步（模型）和第 7 步（工作目錄）中的選擇，會自動產生對應的環境變數。
* **自訂新增**：若 Agent 或專案需要其他特定環境變數（例如 `PROXY_URL` 等），可在此區域自訂新增。

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. 更新選項

* **內建可執行檔**：Cherry Studio 已整合上述所有 Code Agent 的可執行檔，多數情況下無需連網即可直接使用。
* **自動更新**：若希望 Agent 始終保持最新版本，可勾選 **`檢查更新並安裝最新版本`** 選項。勾選後，每次啟動時程式會連網檢查並更新 Agent 工具。

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. 啟動 Agent

完成所有配置後，點擊 **`啟動`** 按鈕。Cherry Studio 會自動呼叫系統自帶的 Terminal（終端）工具，載入所有環境變數後執行選擇的 Code Agent。現在您可在彈出的終端視窗中與 AI Agent 互動。

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### 重要注意事項

1. **模型相容性說明**：
   * **Claude Code**：需選擇支援 Anthropic API Endpoint 格式的模型。目前官方支援模型包括：
     * Claude 系列模型
     * DeepSeek V3.1 (官方 API 平台)
     * Kimi K2 (官方 API 平台)
     * 智譜 GLM 4.5 (官方 API 平台)
     * **注意**：目前許多第三方服務商（如 One API, New API 等）針對 DeepSeek、Kimi、GLM 的 API 介面大多僅支援 OpenAI Chat Completions 格式，可能無法直接相容 Claude Code，需等待服務商逐步適配。
   * **Gemini CLI**：需選擇 Google 的 Gemini 系列模型。
   * **Qwen Code**：支援 OpenAI Chat Completions API 格式的模型，強烈推薦使用 **`Qwen3 Coder`** 系列以獲最佳程式碼生成效果。
   * **OpenAI Codex**：支援 GPT 系列模型（如 `gpt-4o`, `gpt-5` 等）。
2. **依賴與環境衝突**：
   * Cherry Studio 內部整合了獨立的 Node.js 執行環境、Code Agent 可執行檔及環境變數配置，提供開箱即用的純淨環境。
   * 若啟動 Agent 時遇到依賴衝突或異常錯誤，可考慮暫時**解除安裝或停用系統內已安裝的相關依賴**（如全域安裝的 Node.js 或特定工具鏈），以排除衝突。
3. **API Token 消耗警告**：
   * **Code Agent 的 API Token 消耗量極大**。處理複雜任務時，Agent 為進行思考、規劃和生成程式碼，可能產生大量請求導致 Token 快速消耗。
   * 請務必根據自身 API 額度與預算**量力而為**，密切關注 Token 使用情況，以防預算超支。

希望本教學能幫助您快速掌握 Cherry Studio 強大的 Code Agent 功能！