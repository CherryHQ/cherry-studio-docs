
{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# Ollama

Ollama 是一款優秀的開源工具，讓您可以在本地輕鬆執行和管理各種大型語言模型（LLMs）。Cherry Studio 現已支援 Ollama 整合，讓您可以在熟悉的介面中，直接與本地部署的 LLM 進行互動，無需依賴雲端服務！

## 什麼是 Ollama？

Ollama 是一個簡化大型語言模型（LLM）部署和使用的工具。它具有以下特點：

* **本地執行：** 模型完全在您的本地電腦上執行，無需連網，保護您的隱私和資料安全。
* **簡單易用：** 通過簡單的命令列指令，即可下載、執行和管理各種 LLM。
* **模型豐富：** 支援 Llama 2、Deepseek、Mistral、Gemma 等多種流行的開源模型。
* **跨平台：** 支援 macOS、Windows 和 Linux 系統。
* **開放API**：支援與OpenAI兼容的介面，可以和其他工具整合。

## 為什麼要在 Cherry Studio 中使用 Ollama？

* **無需雲端服務：** 不再受限於雲端 API 的配額和費用，盡情體驗本地 LLM 的強大功能。
* **資料隱私：** 您的所有對話資料都保留在本地，無需擔心隱私洩露。
* **離線可用：** 即使在沒有網路連線的情況下，也能繼續與 LLM 進行互動。
* **客製化：** 可以根據您的需求，選擇和配置最適合您的 LLM。

## 在 Cherry Studio 中配置 Ollama

### **1. 安裝和執行 Ollama**

首先，您需要在您的電腦上安裝並執行 Ollama。請按照以下步驟操作：

*   **下載 Ollama：** 瀏覽 Ollama 官網（[https://ollama.com/](https://ollama.com/)），根據您的作業系統下載對應的安裝包。\
    在 Linux 下，可直接執行命令安裝ollama：

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **安裝 Ollama：** 按照安裝程式的指引完成安裝。
*   **下載模型：** 開啟終端機（或命令提示字元），使用 `ollama run` 指令下載您想要使用的模型。例如，要下載 Llama 2 模型，可以執行：

    ```sh
    ollama run llama3.2
    ```

    Ollama 會自動下載並執行該模型。
* **保持 Ollama 執行：** 在您使用 Cherry Studio 與 Ollama 模型互動期間，請確保 Ollama 保持執行狀態。

### **2. 在 Cherry Studio 中添加 Ollama 服務商**

接下來，在 Cherry Studio 中添加 Ollama 作為自訂 AI 服務商：

* **開啟設定：** 在 Cherry Studio 介面左側導覽列中，點擊「設定」（齒輪圖示）。
* **進入模型服務：** 在設定頁面中，選擇「模型服務」選項卡。
* **添加供應商：** 點擊清單中的 Ollama。

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. 配置 Ollama 服務商**

在服務商清單中找到剛剛添加的 Ollama，並進行詳細配置：

1. **啟用狀態：**
   * 確保 Ollama 服務商最右側的開關已開啟，表示已啟用。
2. **API 密鑰：**
   * Ollama 預設**不需要** API 密鑰。您可以將此欄位留空，或者填寫任意內容。
3. **API 地址：**
   *   填寫 Ollama 提供的本地 API 地址。通常情況下，地址為：

       ```
       http://localhost:11434/
       ```

       如果修改了連接埠，請自行更改。
4. **保持活躍時間：** 此選項是設定工作階段的保持時間，單位是分鐘。如果在設定時間內沒有新的對話，Cherry Studio 會自動斷開與 Ollama 的連線，釋放資源。
5. **模型管理：**
   * 點擊「+ 添加」按鈕，手動添加您在 Ollama 中已經下載的模型名稱。
   * 比如您已經通過`ollama run llama3.2`下載了`llama3.2`模型, 那麼此處可以填入`llama3.2`
   * 點擊「管理」按鈕，可以對已添加的模型進行編輯或刪除。

## 開始使用

完成以上配置後，您就可以在 Cherry Studio 的聊天介面中，選擇 Ollama 服務商和您已下載的模型，開始與本地 LLM 進行對話了！

## 技巧與提示

* **首次執行模型：** 第一次執行某個模型時，Ollama 需要下載模型檔案，可能需要較長時間，請耐心等待。
* **檢視可用模型：** 在終端機中執行 `ollama list` 命令，可以檢視您已下載的 Ollama 模型清單。
* **硬體要求：** 執行大型語言模型需要一定的計算資源（CPU、記憶體、GPU），請確保您的電腦配置滿足模型的要求。
* **Ollama 文件**: 可以點擊配置頁面中的`查看Ollama文件及模型`連結快速跳轉至Ollama官網文件。