---
icon: message
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 對話介面

## 助手和話題

### 助手

`助手` 是對所選模型進行個性化設定的方式，例如提示詞預設和參數預設等。透過這些設定，能使所選模型更符合您預期的工作方式。

`系統預設助手` 預設了較通用的參數（無提示詞），您可直接使用或前往[智慧體頁面](agents.md)尋找需要的預設。

### 話題

`助手`是`話題`的父集合，單個助手下可建立多個話題（即對話）。所有`話題`共用`助手`的參數設定與提示詞（prompt）等模型設定。

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 對話框內按鈕

<figure><img src="../../.gitbook/assets/對話界面/對話框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/對話界面/新話題.png) `新話題` 在當前助手內建立新話題。

![](../../.gitbook/assets/對話界面/上傳圖片或文檔.png) `上傳圖片或文檔` 上傳圖片需模型支援；上傳文檔會自動解析為文字作為上下文提供給模型。

![](../../.gitbook/assets/對話界面/網絡搜索.png) `網絡搜索` 須在設定中配置網路搜尋相關資訊，搜尋結果作為上下文傳給大模型，詳見[連網模式](../../websearch/)。

![](../../.gitbook/assets/對話界面/知識庫.png) `知識庫` 開啟知識庫功能，詳見[知識庫教學](../../knowledge-base/knowledge-base.md)。

![](<../../.gitbook/assets/對話界面/MCP 服務器.png>) `MCP 伺服器` 開啟 MCP 伺服器功能，詳見[MCP 使用教學](../../advanced-basic/mcp/)。

![](../../.gitbook/assets/對話界面/生成圖片.png) `生成圖片` 預設不顯示，對支援生成圖片的模型（如 Gemini），需手動點亮後才能生成圖片。

{% hint style="info" %}
由於技術原因，您必須手動點亮按鈕才能生成圖片，此按鈕在功能優化後將移除。
{% endhint %}

![](../../.gitbook/assets/對話界面/選擇模型.png) `選擇模型` 為後續對話切換指定模型，保留上下文。

![](../../.gitbook/assets/對話界面/快捷短語.png) `快捷短語` 需先在設定中預設常用短語，此處可調用並直接輸入，支援變數。

![](../../.gitbook/assets/對話界面/清空消息.png) `清空消息` 刪除該話題下所有內容。

![](../../.gitbook/assets/對話界面/展開.png) `展開` 放大對話框以便輸入長文。

![](../../.gitbook/assets/對話界面/清除上下文.png) `清除上下文` 在不刪除內容的前提下截斷模型可取得的上下文，即模型將「忘記」先前對話內容。

![](<../../.gitbook/assets/對話界面/預估 Token 數.png>) `預估 Token 數` 顯示預估 Token 數：四個數據分別為`當前上下文數`、`最大上下文數`（∞表示無限上下文）、`當前輸入框內訊息字數`、`預估 Token 數`。

{% hint style="info" %}
此功能僅用於預估 Token 數，實際 Token 數依模型而異，請以模型提供商的數據為準。
{% endhint %}

![](../../.gitbook/assets/對話界面/翻譯.png) `翻譯` 將當前輸入框內容翻譯為英文。

## 對話設定

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 模型設定

模型設定與助手設定中的`模型設定`參數同步，詳見[助手設定](chat.md#bian-ji-zhu-shou)。

{% hint style="info" %}
在對話設定中，僅模型設定作用於當前助手，其餘設定作用於全域。例如：設定訊息樣式為氣泡後，所有助手的任何話題下皆顯示為氣泡樣式。
{% endhint %}

### 訊息設定

#### <mark style="color:blue;">**`訊息分割線`**</mark>:

使用分割線隔開訊息正文與操作欄。

{% tabs %}
{% tab title="開啟時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="關閉時" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`使用襯線字體`**</mark>：

切換字體樣式，也可透過[自訂css](../../personalization-settings/)更換字體。

#### <mark style="color:blue;">**`程式碼顯示行號`**</mark>：

模型輸出程式碼片段時顯示行號。

{% tabs %}
{% tab title="關閉時" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="開啟時" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`程式碼區塊可折疊`**</mark>：

開啟後，較長的程式碼片段會自動折疊。

#### <mark style="color:blue;">**`程式碼區塊可換行`**</mark>：

開啟後，當單行程式碼過長（超出視窗）時自動換行。

#### <mark style="color:blue;">**`思考內容自動折疊`**</mark>：

開啟後，支援思考的模型在思考完成後會自動折疊思考過程。

#### <mark style="color:blue;">**`訊息樣式`**</mark>：

可切換對話介面為氣泡樣式或清單樣式。

#### <mark style="color:blue;">**`程式碼風格`**</mark>：

可切換程式碼片段的顯示風格。

#### <mark style="color:blue;">**`數學公式引擎`**</mark>：

* KaTeX 渲染速度更快，專為效能優化設計；
* MathJax 渲染較慢，但功能更全面，支援更多數學符號和指令。

#### <mark style="color:blue;">**`訊息字體大小`**</mark>：

調整對話介面的字體大小。

### 輸入設定

#### <mark style="color:blue;">**`顯示預估 Token 數`**</mark>：

在輸入框顯示輸入文本預估消耗的Token數（非實際上下文消耗Token，僅供參考）。

#### <mark style="color:blue;">**`長文字貼上為檔案`**</mark>：

從他處複製長文字貼到輸入框時，自動顯示為檔案樣式，減少後續輸入干擾。

#### <mark style="color:blue;">**`Markdown 渲染輸入訊息`**</mark>：

關閉時僅渲染模型回覆的訊息，不渲染發送的訊息。

{% tabs %}
{% tab title="關閉時" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="開啟時" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`快速敲擊3次空格翻譯`**</mark>：

在輸入框輸入訊息後，連敲三次空格可將內容翻譯為英文。

{% hint style="warning" %}
注意：此操作會覆蓋原文。
{% endhint %}

#### <mark style="color:blue;">**`目標語言`**</mark>：

設定輸入框翻譯按鈕及快速敲擊翻譯的目標語言。

## 助手設定

在助手介面選取需設定的<mark style="background-color:yellow;">助手名稱</mark>→於<mark style="background-color:yellow;">右鍵選單</mark>選擇對應設定

### 編輯助手

{% hint style="info" %}
助手設定作用於該助手下的所有話題。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 提示詞設定

#### <mark style="color:blue;">**`名稱`**</mark>：

可自訂易於辨識的助手名稱。

#### <mark style="color:blue;">**`提示詞`**</mark>：

即 prompt，可參考智慧體頁面的提示詞寫法編輯內容。

#### 模型設定

#### <mark style="color:blue;">**`預設模型`**</mark>：

可為助手固定預設模型，從智慧體頁面新增或複製助手時，初始模型即為此模型。未設定時初始模型為全域初始模型（即[預設助手模型](settings/default-models.md#mo-ren-zhu-shou-mo-xing)）。

{% hint style="info" %}
助手預設模型分兩種：一為[全域預設對話模型](settings/default-models.md#mo-ren-zhu-shou-mo-xing)，另一為助手預設模型；助手預設模型優先級高於全域預設對話模型。未設定助手預設模型時，助手預設模型=全域預設對話模型。
{% endhint %}

#### <mark style="color:blue;">**`自動重置模型`**</mark>：

開啟時 - 在該話題使用過程中切換其他模型後，再次新增話題會將新話題的模型重置為助手預設模型。關閉時新增話題的模型將延用上個話題所用模型。

> 範例：助手預設模型為gpt-3.5-turbo，在該助手下建立話題1，於話題1對話中切換為gpt-4o：
> - 開啟自動重置：新增話題2時預設選gpt-3.5-turbo
> - 關閉自動重置：新增話題2時預設選gpt-4o

#### <mark style="color:blue;">**`溫度 (Temperature)`**</mark> ：

控制模型生成文本的隨機性與創造性（預設值0.7）：
* **低溫值(0-0.3)**：
  * 輸出更確定、專注
  * 適用程式碼生成、資料分析等需準確性場景
* **中溫值(0.4-0.7)**：
  * 平衡創造性與連貫性
  * 適用日常對話與一般寫作（推薦聊天機器人用0.5左右）
* **高溫值(0.8-1.0)**：
  * 輸出更具創造性與多樣性
  * 適用創意寫作、腦力激盪
  * 可能降低文本連貫性

#### <mark style="color:blue;">**`Top P (核取樣)`**</mark>：

預設值1，數值越小AI輸出越單調易理解；數值越大詞彙選擇範圍越廣越多樣：
* **小值(0.1-0.3)**：
  * 僅考慮高概率詞彙
  * 適用程式碼註解、技術文件
* **中值(0.4-0.6)**：
  * 平衡詞彙多樣性與準確性
  * 適用一般對話與寫作
* **大值(0.7-1.0)**：
  * 考慮廣泛詞彙選擇
  * 適用需多樣化表達的創意寫作

{% hint style="info" %}
- 此兩參數可獨立或組合使用
- 根據任務類型選擇合適值
- 建議實驗找出最佳參數組合
- 參數範圍非絕對，請參考模型文件建議
{% endhint %}

#### <mark style="color:blue;">**`上下文數量 (Context Window)`**</mark>

保留在上下文中的訊息數量，數值越大消耗Token越多：
* 5-10：適用一般對話
* \>10：適用需長記憶的複雜任務（如分步生成長文）
* > 注意：訊息越多，Token消耗越大

#### <mark style="color:blue;">**`開啟訊息長度限制 (MaxToken)`**</mark>

單次回答最大[Token](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens)數：
> 範例：測試模型連通性時僅需確認回傳訊息，可設MaxToken為1

多數模型上限為32k Tokens（部分達64k或更高），詳見模型說明頁面。設定建議：
{% hint style="success" %}
* 普通聊天：500-800
* 短文生成：800-2000
* 程式碼生成：2000-3600
* 長文生成：4000+（需模型支援）
{% endhint %}

{% hint style="warning" %}
回答可能被MaxToken限制而截斷（如長程式碼），請依實際情況調整。
{% endhint %}

#### <mark style="color:blue;">**`串流輸出（Stream）`**</mark>

數據以連續流形式傳輸處理（即打字機效果）：
* **關閉時（非串流）**：模型生成完畢後整段輸出（類似微信收訊）
* **開啟時**：逐字即時輸出

{% hint style="info" %}
不支援串流的模型（如早期o1-mini）需關閉此功能
{% endhint %}

#### <mark style="color:blue;">**`自訂參數`**</mark>

在請求體（body）中加入額外參數（如`presence_penalty`等），一般使用者較少使用：
> 前述top-p、maxtokens等皆屬此類參數

填寫格式：參數名稱—參數類型（文字/數字等）—值，參考[文件](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
* 自訂參數優先級高於內建參數（重複時覆蓋內建）
> 範例：自訂`model`為`gpt-4o`後，對話中無論選何模型皆使用gpt-4o
* 使用 <kbd>參數名稱:undefined</kbd> 可排除參數
* 各模型商可能有獨特參數，請查閱提供商文件
{% endhint %}