# 自訂服務商


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




Cherry Studio 不僅整合了主流 AI 模型服務，還賦予您強大的自訂能力。透過 **自訂 AI 服務商** 功能，您可以輕鬆接入任何您需要的 AI 模型。

## 為什麼需要自訂 AI 服務商？

* **靈活性：** 不再受限於預置的服務商清單，自由選擇最適合您需求的 AI 模型。
* **多樣性：** 嘗試各種不同平台的 AI 模型，發掘它們的獨特優勢。
* **可控性：** 直接管理您的 API 金鑰和存取網址，確保安全和隱私。
* **客製化：** 接入私有化部署的模型，滿足特定業務場景的需求。

## 如何新增自訂 AI 服務商？

只需簡單幾步，即可在 Cherry Studio 中新增您的自訂 AI 服務商：

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **開啟設定：** 在 Cherry Studio 介面左側導航欄中，點擊「設定」（齒輪圖示）。
2. **進入模型服務：** 在設定頁面中，選擇「模型服務」頁籤。
3. **新增提供者：** 在「模型服務」頁面中，您會看到現有的服務商清單。點擊清單下方的「+ 新增」按鈕，開啟「新增提供者」彈窗。
4. **填寫資訊：** 在彈窗中，您需要填寫以下資訊：
   * **提供者名稱：** 為您的自訂服務商設定一個易於識別的名稱（例如：MyCustomOpenAI）。
   * **提供者類型：** 從下拉選單中選擇您的服務商類型。目前支援：
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **儲存設定：** 填寫完畢後，點擊「新增」按鈕儲存您的設定。

## 設定自訂 AI 服務商

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

新增完成後，您需要在清單中找到您剛剛新增的服務商，並進行詳細設定：

1. **啟用狀態：** 自訂服務商清單最右側有一個啟用開關，開啟代表啟用該自訂服務。
2. **API 金鑰：**
   * 填寫您的 AI 服務商提供的 API 金鑰（API Key）。
   * 點擊右側的「檢查」按鈕，可以驗證金鑰的有效性。
3. **API 網址：**
   * 填寫 AI 服務的 API 存取網址（Base URL）。
   * 請務必參考您的 AI 服務商提供的官方文件，獲取正確的 API 網址。
4.  **模型管理：**

    * 點擊「+ 新增」按鈕，手動新增此提供者下您想要使用的模型 ID。例如 `gpt-3.5-turbo`、`gemini-pro` 等。

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * 如果您不確定具體的模型名稱，請參考您的 AI 服務商提供的官方文件。
    * 點擊「管理」按鈕，可以對已經新增的模型進行編輯或者刪除。

## 開始使用

完成以上設定後，您就可以在 Cherry Studio 的對話介面中，選擇您自訂的 AI 服務商和模型，開始與 AI 進行對話了！

## 使用 vLLM 作為自訂 AI 服務商

vLLM 是一個類似 Ollama 的快速且易於使用的 LLM 推理函式庫。以下是如何將 vLLM 整合到 Cherry Studio 中的步驟：

1.  **安裝 vLLM：** 按照 vLLM 官方文件（[https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)）安裝 vLLM。

    ```sh
    pip install vllm # 如果你使用 pip
    uv pip install vllm # 如果你使用 uv
    ```
2.  **啟動 vLLM 服務：** 使用 vLLM 提供的 OpenAI 相容介面啟動服務。主要有兩種方式，分別如下：

    * 使用 `vllm.entrypoints.openai.api_server` 啟動

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * 使用 `uvicorn` 啟動

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

確保服務成功啟動，並監聽在預設通訊埠 `8000` 上。當然，您也可以透過參數 `--port` 指定 vLLM 服務的通訊埠號。

3. **在 Cherry Studio 中新增 vLLM 服務商：**
   * 按照前面描述的步驟，在 Cherry Studio 中新增一個自訂 AI 服務商。
   * **提供者名稱：** `vLLM`
   * **提供者類型：** 選擇 `OpenAI`。
4. **設定 vLLM 服務商：**
   * **API 金鑰：** 因為 vLLM 不需要 API 金鑰，可以將此欄位留空，或者填寫任意內容。
   * **API 網址：** 填寫 vLLM 服務的 API 網址。預設情況下，網址為：`http://localhost:8000/`（如果使用了不同的通訊埠，請相應地修改）。
   * **模型管理：** 新增您在 vLLM 中載入的模型名稱。在上面執行 `python -m vllm.entrypoints.openai.api_server --model gpt2` 的例子中，應該在此處填入 `gpt2`。
5. **開始對話：** 現在，您可以在 Cherry Studio 中選擇 vLLM 服務商和 `gpt2` 模型，開始與 vLLM 驅動的 LLM 進行對話了！

## 提示與技巧

* **仔細閱讀文件：** 在新增自訂服務商之前，請務必仔細閱讀您所使用的 AI 服務商的官方文件，了解 API 金鑰、存取網址、模型名稱等關鍵資訊。
* **檢查 API 金鑰：** 使用「檢查」按鈕可以快速驗證 API 金鑰的有效性，避免因金鑰錯誤導致無法使用。
* **關注 API 網址：** 不同的 AI 服務商和模型，API 網址可能有所不同，請務必填寫正確的網址。
* **模型按需新增：** 請只新增您實際上會用到的模型，避免新增過多無用模型。