
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# バイトダンス(豆包)

* [火山エンジン](https://console.volcengine.com/)にログイン
* ここを[直接クリック](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### APIキーの取得

* サイドバーの下にある [APIキー管理](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey)をクリック
* APIキーを作成

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* 作成が成功したら、作成したAPIキーの隣にある目のアイコンをクリックして表示し、コピー

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* コピーしたAPIキーをCherry Studioに入力後、プロバイダーのスイッチをオンにする

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### モデルの有効化と追加

* 方舟コンソールのサイドバーの一番下にある[有効化管理](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false)で、必要なモデルを有効化（豆包シリーズやDeepSeekなど）

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* [モデルリストドキュメント](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)で、必要なモデルの対応するモデルIDを確認

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="火山エンジン モデルIDリストの例"><figcaption></figcaption></figure>

* Cherry Studioの[モデルサービス](../../cherrystudio/preview/settings/providers.md)設定で火山エンジンを選択
* 「追加」をクリックし、取得したモデルIDをモデルID欄にペースト

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* この手順で各モデルを順次追加

### APIエンドポイント

APIエンドポイントの記述方法は2種類あります：

* クライアントデフォルト：`https://ark.cn-beijing.volces.com/api/v3/`
* 別の記述方法：`https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
両方の記法に違いはありません。デフォルトのまま変更不要。

`/`と`#`終端の違いについては、プロバイダー設定の[APIエンドポイント](../../cherrystudio/preview/settings/providers.md#api-di-zhi)セクションを参照してください。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>公式ドキュメントのcURL例</p></figcaption></figure>