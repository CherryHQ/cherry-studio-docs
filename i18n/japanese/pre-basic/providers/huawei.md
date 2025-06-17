
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# ファーウェイクラウド

一、[ファーウェイクラウド](https://auth.huaweicloud.com/authui/login)でアカウントを作成してログイン

二、[このリンク](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage)をクリックし、ModelArtsコンソールにアクセス

三、認証

<details>

<summary>認証手順（認証済みの場合はスキップ）</summary>

1. (二)のリンク先ページに移動後、プロンプトに従って認証ページへ進む（「IAMサブユーザー→新規委託→一般ユーザー」をクリック）

![](<../../.gitbook/assets/image (49).png>)

2. 作成後に(二)のリンク先ページに戻る
3. 「アクセス権限が不足しています」と表示されるので、プロンプト内の「ここをクリック」を選択
4. 既存の認証を追加して確定

![](<../../.gitbook/assets/image (50).png>)

注意：この方法は初心者向けで、複雑な内容を確認せずにプロンプトに従ってクリックするだけで完了します。一度で認証できる場合は自身の方法を使用しても問題ありません。

</details>

四、サイドバーの「認証管理」をクリックし、APIキー（シークレットキー）を作成してコピー

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

次にCherryStudioで新規プロバイダーを作成

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

作成後、シークレットキーを入力



五、サイドバーの「モデルデプロイ」をクリックし、「すべて受け取る」を選択

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

六、「呼び出し」をクリック

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

①のアドレスをコピーし、CherryStudioのプロバイダーアドレス欄に貼り付け、末尾に「#」を追加

末尾に「#」を追加

末尾に「#」を追加

末尾に「#」を追加

末尾に「#」を追加

なぜ「#」を追加するかは[こちらを参照](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> もちろん、参照せずにチュートリアル通り操作しても問題ありません。
>
> v1/chat/completionsを削除する方法で入力しても構いません。入力方法がわかれば任意の方法で、わからない場合は必ずチュートリアル通りに操作してください。



<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

次に②のモデル名をコピーし、CherryStudioで「+追加」ボタンをクリックして新規モデルを作成

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

モデル名を入力（引用符を付けず、サンプル通り正確に入力）

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

「モデル追加」ボタンをクリックして完了。

{% hint style="info" %}
ファーウェイクラウドではモデルごとにアドレスが異なるため、各モデルごとに新規プロバイダーを作成する必要があります。上記手順を繰り返し実行してください。
{% endhint %}