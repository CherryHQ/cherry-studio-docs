---
icon: route
---
# 調用鏈使用說明


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




## 功能介紹

調用鏈（又稱「trace」）為用戶提供對話的洞察能力，幫助用戶覺察模型、知識庫、MCP、網路搜索等在對話過程中的具體表現。它是一個基於 [OpenTelemetry](https://opentelemetry.io/docs/languages/js/) 實現的可觀測工具，透過端側採集、儲存、處理資料實現視覺化，為定位問題、最佳化效果提供量化評估依據。

每次對話對應一條 trace 資料，一條 trace 由多個 span 組成，每個 span 對應 Cherry Studio 的一個程式處理邏輯如呼叫模型會話、呼叫 MCP 、呼叫知識庫、呼叫網路搜索等。trace 以樹狀結構展示，span 為樹節點，主要資料包括耗時、token 使用量，當然在 span 詳情還可檢視其具體的輸入輸出。

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## 開啟 Trace

預設情況下，Cherry Studio 安裝之後，Trace 是隱藏的狀態。需要在「設定」-「常規設定」 - 「開發者模式」中開啟，如下圖：

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

且對於之前的會話不會產生 Trace 記錄，只會在新的問答產生之後才會產生 Trace 記錄。所產生的記錄儲存在本地，如需要徹底清除 Trace ，可以透過「設定」 - 「資料設定」 - 「資料目錄」 - 「清除快取」進行清除，也可透過手動 刪除 \~/.cherrystudio/trace 下的檔案進行清除，如下圖：

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## 場景介紹

### 全鏈路檢視

在 Cherry Studio 對話方塊中點選調用鏈檢視調用鏈的全鏈路資料。無論在對話過程中呼叫了模型，還是網路搜索、知識庫、MCP，都可以在調用鏈視窗中檢視到全鏈路呼叫資料。

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### 檢視線路中模型

若想要檢視調用鏈中模型的詳情，可以點選模型呼叫節點，檢視其輸入、輸出詳情。

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### 檢視線路中網路搜索

若想要檢視調用鏈中網路搜索的詳情，可以點選網路搜索呼叫節點，檢視其輸入、輸出詳情。在詳情中，可檢視到呼叫網路搜索查詢的問題和其傳回的結果。

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### 檢視線路中知識庫

若想要檢視調用鏈中知識庫的詳情，可以點選知識庫呼叫節點，檢視其輸入、輸出詳情。在詳情中，可檢視到呼叫知識庫查詢的問題和其傳回的答案。

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### 檢視線路中 MCP 呼叫情況

若想要檢視調用鏈中 MCP 的詳情，可以點選 MCP 呼叫節點，檢視其輸入、輸出詳情。在詳情中，可檢視到呼叫此 MCP Server tool 的入參和 tool 的傳回。

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## 問題和建議

當前功能由阿里雲 [EDAS](https://www.aliyun.com/product/edas) 團隊提供，如有問題或建議，請進入釘釘群 （ 群號： 21958624 ） 與開發者進行深度溝通。

\