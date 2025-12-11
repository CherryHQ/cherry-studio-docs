# 火山引擎

* 登录 [火山引擎](https://console.volcengine.com/)
* 直接点击 [这里直达](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (2).png" alt=""><figcaption></figcaption></figure>

### 获取API Key

* 点击侧栏下方的 [API Key管理](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey)
* 创建 API Key

<figure><img src="../../.gitbook/assets/image (6) (2) (1).png" alt=""><figcaption></figcaption></figure>

* 创建成功后，点击创建好的 API Key 后的小眼睛打开并复制

<figure><img src="../../.gitbook/assets/image (7) (2) (1).png" alt=""><figcaption></figcaption></figure>

* 将复制的 API Key 填入到 CherryStudio 当中后，打开服务商开关。

<figure><img src="../../.gitbook/assets/image (8) (2) (1).png" alt=""><figcaption></figcaption></figure>

### 开通并添加模型

* 在方舟控制台侧栏最下方的 [开通管理](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) 开通需要使用的模型，这里可以按需开通豆包系列和 DeepSeek 等模型。

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 在 [模型列表文档](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90) 里，找到所需模型对应的 模型ID。

<figure><img src="../../.gitbook/assets/火山引擎_模型ID (1).png" alt="火山引擎模型ID列表示例"><figcaption></figcaption></figure>

* 打开 Cherry Studio 的 [模型服务](../../cherrystudio/preview/settings/providers.md) 设置找到火山引擎
* 点击添加，将之前获得的 模型ID 复制至 模型ID 文本对话框即可

<figure><img src="../../.gitbook/assets/volc_ark_01 (1).png" alt=""><figcaption></figcaption></figure>

* 按照此流程依次添加模型

### API地址

API地址有两种写法

* 第一种为客户端默认的：`https://ark.cn-beijing.volces.com/api/v3/`
* 第二种写法为：`https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
两种写法没什么区别，保持默认即可，无需修改。

关于 `/` 和 `#` 结尾的区别参考文档服务商设置的 API 地址部分，[点击前往](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2) (1).png" alt=""><figcaption><p>官方文档cURL示例</p></figcaption></figure>
