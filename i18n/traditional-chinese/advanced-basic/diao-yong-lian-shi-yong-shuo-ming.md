---
icon: route
---
# 追蹤功能使用說明


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




## 功能介紹

追蹤功能（又稱「trace」）為使用者提供對話的洞察能力，協助使用者覺察模型、知識庫、MCP、網路搜尋等在對話過程中的具體表現。這是一個基於 [OpenTelemetry](https://opentelemetry.io/docs/languages/js/) 實現的可觀測工具，透過終端採集、儲存、處理資料實現視覺化，為定位問題、優化效果提供量化評估依據。

每次對話對應一條 trace 資料，一條 trace 由多個 span 組成，每個 span 對應 Cherry Studio 的一個程式處理邏輯，如呼叫模型會話、呼叫 MCP、呼叫知識庫、呼叫網路搜尋等。trace 以樹狀結構展示，span 為樹節點，主要資料包括耗時、token 使用量，在 span 詳情中還可查看具體的輸入輸出。

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## 開啟 Trace

預設情況下，Cherry Studio 安裝後 Trace 處於隱藏狀態。需在「設定」→「常規設定」→「開發者模式」中開啟，如下圖：

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

注意：此功能僅對新對話生效。開啟後產生的記錄儲存在本機，如需徹底清除 Trace，可透過「設定」→「資料設定」→「資料目錄」→「清除快取」操作，或手動刪除 `~/.cherrystudio/trace` 目錄下的檔案，如下圖：

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## 應用場景

### 全鏈路查看

在 Cherry Studio 對話框中點擊追蹤圖示，即可查看完整呼叫鏈資料。無論對話過程中呼叫了模型、網路搜尋、知識庫或 MCP，都能在追蹤視窗檢視全鏈路資料。

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### 查看模型呼叫詳情

點擊模型呼叫節點，可檢視其輸入輸出詳情與效能數據。

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### 查看網路搜尋詳情

點擊網路搜尋呼叫節點，可檢視查詢問題與返回結果的完整對應關係。

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### 查看知識庫呼叫詳情

點擊知識庫呼叫節點，可檢索問題與知識庫返回答案的匹配詳情。

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### 查看 MCP 呼叫詳情

點擊 MCP 呼叫節點，可檢視伺服器工具的輸入參數與執行返回結果。

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## 問題與建議

本功能由阿里雲 [EDAS](https://www.aliyun.com/product/edas) 團隊提供技術支援，如有問題或建議，請加入釘釘群（群號：21958624）與開發團隊深度交流。

\