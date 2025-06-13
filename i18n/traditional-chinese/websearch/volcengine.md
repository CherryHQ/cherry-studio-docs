---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 火山引擎接入聯網

### 1、登陸/註冊「火山引擎」賬號 <a href="#rclz7" id="rclz7"></a>

訪問官網：[https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>火山引擎官網</p></figcaption></figure>

### 2、建立「可聯網的」「我的應用」 <a href="#gvzaa" id="gvzaa"></a>

2.1、 登陸火山引擎，進入「火山方舟」頁面，傳送門：[https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2、 **依次點擊：**<mark style="color:red;">**「我的應用」 - 「建立應用」 - 「零程式碼」 - 「單聊」**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3、填寫資訊並發佈應用 <a href="#zzdfe" id="zzdfe"></a>

**應用名稱**：按照要求隨意命名即可（帶<mark style="color:red;">**\*必填**</mark>，其他可不填寫）

<mark style="color:red;">**關鍵步驟：開啟聯網外掛程式（需先開通）**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1、 開通聯網外掛程式功能（注意費用和免費次數） <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>點選立即購買，逐步操作至顯示下方介面，即表示開通成功</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>注意狀態，至此開通成功</p></figcaption></figure>

返回「填寫應用資訊」介面繼續操作

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2、聯網搜尋「進階設定」說明 <a href="#sp6uz" id="sp6uz"></a>

根據實際需求選擇，個人建議：
* 需精確控制輸入輸出時，選用「**自訂呼叫**」聯網
* 想簡化操作可維持「**自動呼叫**」- 預設值
* 預算充足且要求資訊實時性時，選「**強制開啟**」

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3、發佈應用 <a href="#fe1gf" id="fe1gf"></a>

點選右上角「發佈」按鈕，應用建立完成

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4、取得 API Key <a href="#jtqlu" id="jtqlu"></a>

依次點擊：**「API 呼叫指南」-「選取 API Key 並複製」-「檢視並選擇」**

複製 API key 後，前往 cherry studio 貼入（操作詳見下方介面）

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

若無 API key，在彈窗右上角 - 「**建立 API Key**」後複製即可

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5、在 cherry studio 中使用 API Key 實現聯網存取 deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1、開啟 cherry studio - 「設定」- 「隨意命名」-「類型選：openAI」 <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2、設定 url 和 key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">提示：若找不到地址或非北京節點，可在此處查詢具體地址（注意保留結尾"/"）：</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3、新增模型名稱 <a href="#qmh3i" id="qmh3i"></a>

注意：需複製下方小字作為模型名稱，否則會報錯

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6、 效果預覽 <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>