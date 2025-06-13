
{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 字節跳動(豆包)

*   登入 [火山引擎](https://console.volcengine.com/)
*   直接點擊 [這裡直達](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### 取得API Key

*   點擊側邊欄下方的 [API Key管理](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey)
*   建立 API Key

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   建立成功後，點擊建立好的 API Key 後面的小眼睛圖示開啟並複製

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   將複製的 API Key 填入 CherryStudio 當中，然後開啟服務商開關。

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### 開通並加入模型

*   在方舟控制台側邊欄最下方的 [開通管理](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) 開通需要使用的模型，這裡可以按需開通豆包系列和 DeepSeek 等模型。

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   在 [模型列表文件](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90) 裡，找到所需模型對應的 模型ID。

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="火山引擎模型ID列表範例"><figcaption></figcaption></figure>

*   開啟 Cherry Studio 的 [模型服務](../../cherrystudio/preview/settings/providers.md) 設定，找到火山引擎
*   點擊新增，將之前獲得的 模型ID 複製到 模型ID 文字對話框即可

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   按照此流程依序加入模型

### API位址

API位址有兩種寫法

*   第一種為客戶端預設的：`https://ark.cn-beijing.volces.com/api/v3/`
*   第二種寫法為：`https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
兩種寫法沒有什麼區別，保持預設即可，無需修改。

關於 `/` 和 `#` 結尾的區別，參考文件服務商設定的 API 位址部分，[點擊前往](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>官方文件cURL範例</p></figcaption></figure>