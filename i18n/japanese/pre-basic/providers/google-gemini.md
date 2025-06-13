
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# Google Gemini

## APIキーの取得

* GeminiのAPIキーを取得する前に、Google Cloudプロジェクトが必要です（既に所有している場合はこの手順をスキップ可能）
* [Google Cloud](https://console.cloud.google.com/projectcreate) にアクセスし、プロジェクトを作成。プロジェクト名を入力後「プロジェクトを作成」をクリック

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

* 公式 [API Keyページ](https://aistudio.google.com/app/apikey?hl=zh-cn) で `APIキーの作成` をクリック

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

* 生成されたキーをコピーし、CherryStudioの [サービスプロバイダー設定](broken-reference) を開く
* Geminiサービスプロバイダーを選択し、取得したキーを入力

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

* 下部の「管理」または「追加」をクリックし、対応モデルを追加後、右上のサービスプロバイダートグルを有効化して使用開始

{% hint style="info" %}
- 中国大陸部（台湾を除く）ではGoogle Geminiを直接利用できません。プロキシ環境の独自設定が必要です
{% endhint %}