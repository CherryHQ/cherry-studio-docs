---
icon: message
---
# 對話介面


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




## 助手與話題

### 助手

`助手` 是對所選模型進行個性化設置的配置，如提示詞預設和參數預設等，通過這些設置讓模型更符合預期的工作方式。

`系統預設助手` 提供通用參數（無提示詞），您可直接使用或到 [智能體頁面](agents.md) 尋找所需預設。

### 話題

`助手` 是 `話題` 的父集合，單個助手可建立多個話題（對話），所有 `話題` 共享助手的參數設置和提示詞 (prompt) 等模型配置。

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 對話框內按鈕

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `新話題` 在當前助手內建立新話題。

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `上傳圖片或文件` 需模型支援圖片解析，上傳文件會自動解析為文字作為上下文。

![](../../.gitbook/assets/对话界面/网络搜索.png) `網路搜尋` 需先在設定中配置，搜尋結果將作為上下文提供給模型，詳見 [聯網模式](../../websearch/)。

![](../../.gitbook/assets/对话界面/知识库.png) `知識庫` 開啟知識庫功能，詳見 [知識庫教學](../../knowledge-base/knowledge-base.md)。

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP 伺服器` 開啟 MCP 伺服器功能，詳見 [MCP 使用教學](../../advanced-basic/mcp/)。

![](../../.gitbook/assets/对话界面/生成图片.png) `產生圖片` 預設隱藏，對支援產生圖片的模型（如 Gemini），需手動點亮按鈕才可生成圖片。

{% hint style="info" %}
由於技術限制，您必須手動點亮按鈕才能產生圖片，此按鈕在功能優化後將移除。
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `選擇模型` 為後續對話切換指定模型，保留上下文。

![](../../.gitbook/assets/对话界面/快捷短语.png) `快捷短語` 需先在設定中預設常用短語，此處可直接調用，支援變數。

![](../../.gitbook/assets/对话界面/清空消息.png) `清空訊息` 刪除該話題所有內容。

![](../../.gitbook/assets/对话界面/展开.png) `展開` 擴大對話框，方便輸入長文。

![](../../.gitbook/assets/对话界面/清除上下文.png) `清除上下文` 在不刪除內容情況下截斷模型能獲取的上下文，使模型"忘記"先前對話。

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `預估 Token 數` 顯示預估數據：`當前上下文數`、`最大上下文數`（∞ 表示無限制）、`當前輸入框訊息字數`、`預估 Token 數`。

{% hint style="info" %}
此功能僅供參考，實際 Token 數因模型而異，請以模型供應商資料為準。
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `翻譯` 將輸入框內容翻譯成英文。

## 對話設定

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 模型設定

參數與助手設定中的 `模型設定` 同步，詳見 [編輯助手](chat.md#bian-ji-zhu-shou)。

{% hint style="info" %}
對話設定中僅模型設定作用於當前助手，其餘設定作用於全域（例如設定訊息樣式後所有話題均適用）。
{% endhint %}

### 訊息設定

#### <mark style="color:blue;">**`訊息分隔線`**</mark>:

分隔訊息正文與操作欄。

{% tabs %}
{% tab title="開啟時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="關閉時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`使用襯線字體`**</mark>：

切換字體樣式，也可透過 [自訂css](../../personalization-settings/) 更換字體。

#### <mark style="color:blue;">**`程式碼顯示行號`**</mark>：

模型輸出程式碼時顯示行號。

{% tabs %}
{% tab title="關閉時" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="開啟時" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`程式碼塊可折疊`**</mark>：

程式碼過長時自動折疊區塊。

#### <mark style="color:blue;">**`程式碼塊自動換行`**</mark>：

單行程式碼超出視窗時自動換行。

#### <mark style="color:blue;">**`思考內容自動折疊`**</mark>：

支援思考的模型完成後自動折疊思考過程。

#### <mark style="color:blue;">**`訊息樣式`**</mark>：

切換氣泡樣式或清單樣式。

#### <mark style="color:blue;">**`程式碼風格`**</mark>：

切換程式碼片段顯示風格。

#### <mark style="color:blue;">**`數學公式引擎`**</mark>：

* KaTeX：渲染速度更快，針對效能優化
* MathJax：功能更完整，支援更多數學符號（渲染較慢）

#### <mark style="color:blue;">**`訊息字體大小`**</mark>：

調整對話介面字體大小。

### 輸入設定

#### <mark style="color:blue;">**`顯示預估 Token 數`**</mark>：

輸入框顯示預估消耗 Token 數（僅供參考）。

#### <mark style="color:blue;">**`長文字貼上為文件`**</mark>：

貼上長文字時自動顯示為文件樣式，減少干擾。

#### <mark style="color:blue;">**`Markdown 渲染輸入訊息`**</mark>：

關閉時僅渲染模型回覆，不渲染發送訊息。

{% tabs %}
{% tab title="關閉時" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="開啟時" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`快速敲擊3次空白鍵翻譯`**</mark>：

輸入內容後連敲三次空白鍵可翻譯為英文。

{% hint style="warning" %}
注意：此操作會覆蓋原始內容。
{% endhint %}

#### <mark style="color:blue;">**`目標語言`**</mark>：

設定翻譯按鈕和快速翻譯的目標語言。

## 助手設定

在助手介面右鍵點選<mark style="background-color:yellow;">助手名稱</mark>→選擇設定選項

### 編輯助手

{% hint style="info" %}
助手設定作用於該助手所有話題。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 提示詞設定

#### <mark style="color:blue;">**`名稱`**</mark>：

自訂助手辨識名稱。

#### <mark style="color:blue;">**`提示詞`**</mark>：

即 prompt ，可參考智能體頁面格式編輯。

#### 模型設定

#### <mark style="color:blue;">**`預設模型`**</mark>：

為助手固定預設模型。未設定時採用 [全域預設模型](settings/default-models.md#mo-ren-zhu-shou-mo-xing)。

{% hint style="info" %}
助手預設模型優先級高於全域預設模型。
{% endhint %}

#### <mark style="color:blue;">**`自動重置模型`**</mark>：

開啟時-切換模型後新建話題會重置為助手預設模型；關閉時新建話題沿用上個話題模型。

> 範例：助手預設模型為gpt-3.5-turbo，在話題1切換gpt-4o後：
>
> 開啟自動重置：話題2將使用gpt-3.5-turbo
>
> 關閉自動重置：話題2將使用gpt-4o

#### <mark style="color:blue;">**`溫度 (Temperature)`**</mark> ：

控制輸出隨機性（預設0.7）：
* 低值(0-0.3)：精確輸出，適合程式碼生成
* 中值(0.4-0.7)：平衡創造力，推薦日常對話
* 高值(0.8-1.0)：高創造力，適合創意寫作

#### <mark style="color:blue;">**`Top P (核採樣)`**</mark>：

控制詞彙選擇範圍（預設1）：
* 小值(0.1-0.3)：保守輸出，適合技術文件
* 中值(0.4-0.6)：平衡多樣性
* 大值(0.7-1.0)：多樣化表達，適合創意場景

{% hint style="info" %}
- 參數可單獨或組合使用
- 根據任務類型選擇合適值
- 實際效果請參考模型文件建議
{% endhint %}

#### <mark style="color:blue;">**`上下文數量 (Context Window)`**</mark>

保留的上下文訊息數量：
* 5-10：普通對話
* >10：複雜任務（消耗更多 token）
* 注意：訊息越多消耗 token 越多

#### <mark style="color:blue;">**`開啟訊息長度限制 (MaxToken)`**</mark>

單次回答最大 [Token](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) 數：
> 範例：測試模型連通性時可設 MaxToken=1

多數模型上限為32k Tokens（部分支援更高）

{% hint style="success" %}
建議值：
* 普通聊天：500-800
* 短文生成：800-2000
* 程式碼生成：2000-3600
* 長文生成：4000+ (需模型支援)
{% endhint %}

{% hint style="warning" %}
過低限制可能導致輸出截斷或不完整。
{% endhint %}

#### <mark style="color:blue;">**`流式輸出（Stream）`**</mark>

資料即時傳輸處理方式：
* 開啟：逐字輸出（打字機效果）
* 關閉：整段一次性輸出

{% hint style="info" %}
部分模型（如o1-mini）需關閉此功能。
{% endhint %}

#### <mark style="color:blue;">**`自訂參數`**</mark>

在請求體（body）中添加額外參數（如 `presence_penalty`）。

> 填寫格式：參數名稱—類型—值，參考 [OpenAI 文件](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- 自訂參數優先級高於內建參數
- 使用 <kbd>參數名稱:undefined</kbd> 可排除參數
- 各模型商可能有專屬參數
{% endhint %}