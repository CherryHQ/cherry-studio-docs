---
description: Tools
icon: code
---
# Code Tools 使用教學


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




Cherry Studio v1.5.7 版本引入了操作簡易且功能強大的 Code Agent 功能，可直接啟動和管理多種 AI 編程agent。本教程將引導您完成設定和啟動的完整流程。

***

### 操作步驟

#### 1. 升級 Cherry Studio

首先，請確保您的 Cherry Studio 已升級至 **v1.5.7** 或更高版本。您可前往 [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) 或官方網站下載最新版本。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 2. 調整導航列位置

為方便使用頂部標籤頁功能，建議將導航列調整至頂部。

* 操作路徑：`設定` -> `顯示設定` -> `導航列設定`
* 將「導航列位置」選項設為 **`頂部`**。

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. 新增標籤頁

點選介面頂部的「+」號圖標，新增空白標籤頁。

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. 開啟 Code Agent 功能

在新標籤頁中點擊 `Code`（或 `</>`）圖標，進入 Code Agent 設定介面。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. 選擇 CLI 工具

根據需求及持有的 API Key 選擇要使用的 Code Agent 工具。目前支援以下幾種：

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. 選擇 Agent 調用的模型

在下拉式選單中選擇與 CLI 工具相容的模型。_（詳細模型相容性說明請參考下方「重要注意事項」）_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. 指定工作目錄

點擊「選擇目錄」按鈕，為 Agent 指定工作目錄。Agent 將具備存取此目錄下所有檔案及子目錄的權限，以便理解專案脈絡、讀取檔案及執行程式碼。

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. 設定環境變數

* **自動配置**：您在步驟 6（模型）和步驟 7（工作目錄）的選擇會自動生成相應環境變數。
* **自訂新增**：若 Agent 或專案需特定環境變數（如 `PROXY_URL` 等），可在此區域自訂新增。

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. 更新選項

* **內建可執行檔**：Cherry Studio 已整合上述所有 Code Agent 執行檔，多數情況下無需連網即可直接使用。
* **自動更新**：若希望 Agent 始終維持最新版本，可勾選 **`檢查更新並安裝最新版本`** 選項。勾選後每次啟動時會自動連網檢查並更新 Agent 工具。

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. 啟動 Agent

完成所有設定後點擊 **`啟動`** 按鈕。Cherry Studio 將自動呼叫系統 Terminal（終端機），載入所有環境變數後運行所選 Code Agent。現在您可在彈出的終端機視窗中與 AI Agent 互動。

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### 重要注意事項

1. **模型相容性說明**：
   * **Claude Code**：需選擇支援 Anthropic API Endpoint 格式的模型。目前官方支援模型包含：
     * Claude 系列模型
     * DeepSeek V3.1 (官方 API 平台)
     * Kimi K2 (官方 API 平台)
     * 智譜 GLM 4.5 (官方 API 平台)
     * **注意**：當前許多第三方服務商（如 One API, New API 等）針對 DeepSeek, Kimi, GLM 的 API 接口多數僅支援 OpenAI Chat Completions 格式，可能需等待服務商逐步適配後方能與 Claude Code 相容。
   * **Gemini CLI**：需選擇 Google 的 Gemini 系列模型。
   * **Qwen Code**：支援 OpenAI Chat Completions API 格式模型，強烈建議使用 **`Qwen3 Coder`** 系列模型以獲得最佳程式碼生成效果。
   * **OpenAI Codex**：支援 GPT 系列模型（如 `gpt-4o`, `gpt-5` 等）。
2. **依賴與環境衝突**：
   * Cherry Studio 內建獨立 Node.js 運行環境、Code Agent 執行檔及環境變數配置，旨在提供開箱即用的潔淨環境。
   * 若啟動 Agent 時遇到依賴衝突或異常錯誤，建議暫時**解除安裝或停用系統內相關全域依賴**（如 Node.js 或特定工具鏈）以排除衝突。
3. **API Token 消耗警示**：
   * **Code Agent 的 API Token 消耗量極大**。處理複雜任務時，Agent 需反覆思考、規劃並生成程式碼，可能產生大量請求導致 Token 快速耗盡。
   * 請務必依據自身 API 額度及預算**量力而為**，密切關注 Token 使用狀況以防預算超支。

希望本教學能協助您快速掌握 Cherry Studio 強大的 Code Agent 功能！