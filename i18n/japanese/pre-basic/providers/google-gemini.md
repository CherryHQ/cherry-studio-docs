
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# Google Gemini

## APIキーの取得

* Gemini の API キーを取得する前に、Google Cloud プロジェクトが必要です（すでに所有している場合、この手順はスキップできます）。
* [Google Cloud](https://console.cloud.google.com/projectcreate) にアクセスし、プロジェクトを作成します。プロジェクト名を入力し、「プロジェクトを作成」をクリックしてください。

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

* 公式の [API Keyページ](https://aistudio.google.com/app/apikey?hl=zh-cn) で、`鍵 APIキーを作成` をクリックしてください。

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

* 生成されたキーをコピーし、CherryStudio の [サービスプロバイダ設定](broken-reference) を開いてください。
* サービスプロバイダ Gemini を選択し、取得したキーを入力してください。

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

* 最下部の「管理」または「追加」をクリックし、サポートされているモデルを追加し、右上のサービスプロバイダスイッチをオンにすると、使用可能になります。

{% hint style="info" %}
- 中国では台湾を除く地域で Google Gemini サービスを直接利用できません。プロキシの問題を解決する必要があります。
{% endhint %}