# Google Gemini


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## APIキーの取得

* GeminiのAPIキーを取得する前に、Google Cloudプロジェクトが必要です（既にお持ちの場合はこの手順をスキップできます）
* [Google Cloud](https://console.cloud.google.com/projectcreate) にアクセスし、プロジェクト名を入力して「プロジェクトを作成」をクリック

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

* 公式の [API Keyページ](https://aistudio.google.com/app/apikey?hl=zh-cn) で `密钥 创建API密钥` をクリック

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

* 生成されたキーをコピーし、CherryStudioの [サービスプロバイダー設定](broken-reference) を開く
* Geminiプロバイダーを選択し、取得したキーを入力

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

* 下部の「管理」または「追加」をクリックし、サポートモデルを追加後、右上のサービスプロバイダートグルを有効化すると利用可能になります

{% hint style="info" %}
- 中国本土（台湾を除く）ではGoogle Geminiサービスが直接利用できません。プロキシ設定を自身で解決する必要があります
{% endhint %}