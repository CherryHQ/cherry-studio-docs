---
icon: route
---
# 調用鏈使用說明


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




## 功能介紹

調用鏈（又稱「trace」）為用戶提供對話的洞察能力，幫助用戶覺察模型、知識庫、MCP、網路搜索等在對話過程中的具體表現。它是一個基於 [OpenTelemetry](https://opentelemetry.io/docs/languages/js/) 實現的可觀測工具，通過端側採集、儲存、處理數據實現可視化，為定位問題、優化效果提供量化評估依據。

每次對話對應一條 trace 數據，一條 trace 由多個 span 組成，每個 span 對應 Cherry Studio 的一個程序處理邏輯，如調用模型會話、調用 MCP、調用知識庫、調用網路搜索等。trace 以樹結構展示，span 為樹節點，主要數據包括耗時、token 使用量，當然在 span 詳情還可以查看其具體的輸入輸出。

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## 開啟 Trace

預設情況下，Cherry Studio 安裝之後，Trace 是隱藏的狀態。需要在「設定」-「常規設定」 - 「開發者模式」中開啟，如下圖：

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

且對於之前的會話不會產生 Trace 記錄，只會在新的問答產生之後才會產生 Trace 記錄。所產生的記錄儲存在本地，如需要徹底清除 Trace ，可以通過「設定」 - 「數據設定」 - 「數據目錄」 - 「清除快取」進行清除，也可通過手動刪除 ~/.cherrystudio/trace 下的檔案進行清除，如下圖：

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## 場景介紹

### 全鏈路查看

在 Cherry Studio 對話框中點擊調用鏈查看調用鏈的全鏈路數據。無論在對話過程中調用了模型，還是網路搜索、知識庫、MCP，都可以在調用鏈視窗中查看到全鏈路調用數據。

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### 查看鏈路中模型

若想要查看調用鏈中模型的詳情，可以點擊模型調用節點，查看其輸入、輸出詳情。

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### 查看鏈路中網路搜索

若想要查看調用鏈中網路搜索的詳情，可以點擊網路搜索調用節點，查看其輸入、輸出詳情。在詳情中，可以查看到調用網路搜索查詢的問題和其返回的結果。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### 查看鏈路中知識庫

若想要查看調用鏈中知識庫的詳情，可以點擊知識庫調用節點，查看其輸入、輸出詳情。在詳情中，可以查看到調用知識庫查詢的問題和其返回的答案。

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### 查看鏈路中 MCP 調用情況

若想要查看調用鏈中 MCP 的詳情，可以點擊 MCP 調用節點，查看其輸入、輸出詳情。在詳情中，可以查看到調用此 MCP Server tool 的入參和 tool 的返回。

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## 問題和建議

目前功能由阿里雲 [EDAS](https://www.aliyun.com/product/edas) 團隊提供，如有問題或建議，請進入釘釘群 （ 群號： 21958624 ） 與開發者進行深度溝通。

\