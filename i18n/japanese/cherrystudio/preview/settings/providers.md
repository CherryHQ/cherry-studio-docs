---
icon: cloud-check
---
# モデルサービス設定


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




現在のページはインターフェース機能の紹介のみを行っています。設定チュートリアルについては、基本チュートリアルの [プロバイダー設定](../../../pre-basic/providers/) をご参照ください。

{% hint style="info" %}
* 組み込みプロバイダーを使用する場合は、対応するシークレットキーのみを入力してください。
* プロバイダーによってシークレットキーの呼称が異なる場合があります（シークレットキー、Key、API Key、トークンなどはすべて同一のものを指します）。
{% endhint %}

### APIシークレットキー

Cherry Studioでは、単一プロバイダーが複数キーのローテーション使用をサポートしており、ローテーション方式はリスト先頭から順番に循環する方法です。

* 複数のキーは英語のカンマで区切って追加します。以下のような形式で入力します：

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
必ず<strong>英語</strong>のカンマを使用してください。
{% endhint %}

### APIエンドポイント

組み込みプロバイダーを使用する場合、通常はAPIエンドポイントを入力する必要はありません。変更する場合は、対応する公式ドキュメントに記載されたエンドポイントを厳密に従って入力してください。

> プロバイダーから提供されるエンドポイントが <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> 形式の場合、ルートアドレスのみ（<mark style="background-color:red;">https://xxx.xxx.com</mark>）を入力すれば問題ありません。
>
> Cherry Studioは残りのパス（<mark style="background-color:green;">/v1/chat/completions</mark>）を自動的に連結します。指定通りに入力しないと正常に使用できない場合があります。

{% hint style="info" %}
説明：大多数のプロバイダーの大規模言語モデルルーティングは統一されています。通常、以下の操作は不要です。プロバイダーのAPIパスがv2やv3/chat/completionsなど別バージョンの場合、アドレスバーに手動で対応するバージョンを「`/`」で終わるように入力してください。プロバイダーのリクエストルートが標準的な<mark style="background-color:green;">/v1/chat/completions</mark>でない場合は、プロバイダーから提供された完全なアドレスを「`#`」で終わる形で使用します。

要約：
* APIエンドポイントが「`/`」で終わる場合：「<mark style="background-color:green;">chat/completions</mark>」のみを連結
* APIエンドポイントが「`#`」で終わる場合：連結操作をせず、入力されたアドレスのみを使用

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### モデルの追加

通常、プロバイダー設定ページの左下にある「`管理`」ボタンをクリックすると、そのプロバイダーがサポートする全ての呼び出し可能なモデルを自動取得します。取得したリストからモデル名の右にある「`+`」をクリックすると、モデルリストに追加されます。

{% hint style="info" %}
管理ボタンクリック時に表示されるポップアップリスト内のモデルは全て追加されません。モデルリストに表示させるためには、各モデル右側の「`+`」をクリックし、プロバイダー設定ページのモデルリストに追加する必要があります。
{% endhint %}

### 接続性チェック

APIシークレットキー入力欄の右にあるチェックボタンをクリックすると、設定が成功しているかテストできます。

{% hint style="info" %}
接続チェック時は、デフォルトでモデルリストに追加された最後のチャットモデルが使用されます。チェックで失敗した場合は、モデルリストに誤ったまたはサポートされていないモデルが含まれていないか確認してください。
{% endhint %}

{% hint style="danger" %}
設定が成功した後は、必ず右上のスイッチを<strong>ON</strong>にしてください。有効化しない場合、当該プロバイダーは無効状態のままであり、モデルリストに対応モデルが表示されません。
{% endhint %}