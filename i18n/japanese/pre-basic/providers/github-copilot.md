
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# GitHub Copilot

GitHub Copilotを使用するには、まずGitHubアカウントを持ち、GitHub Copilotサービスをサブスクリプションする必要があります。free版のサブスクリプションも可能ですが、free版は最新のClaude 3.7モデルをサポートしていません。詳細は[GitHub Copilot公式サイト](https://github.com/features/copilot)を参照してください。

## Device Codeの取得

「GitHubにログイン」をクリックし、Device Codeを取得してコピーします。

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Device Code取得の例"><figcaption><p>Device Codeの取得</p></figcaption></figure>

## ブラウザでDevice Codeを入力して認証

Device Codeを取得したら、リンクをクリックしてブラウザを開きます。GitHubアカウントでログインし、Device Codeを入力して認証します。

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="GitHub認証の例"><figcaption><p>GitHub認証</p></figcaption></figure>

認証が成功したら、Cherry Studioに戻り「GitHubに接続」をクリックします。成功するとGitHubユーザー名とアバターが表示されます。

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="GitHub接続成功の例"><figcaption><p>GitHub接続成功</p></figcaption></figure>

## 「管理」をクリックしてモデルリストを取得

下部の「管理」ボタンをクリックすると、現在サポートされているモデルリストが自動的に取得されます。

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="モデルリスト取得の例"><figcaption><p>モデルリストの取得</p></figcaption></figure>

## よくある質問

### Device Codeの取得に失敗しました。再試行してください

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Device Code取得失敗の例"><figcaption><p>Device Code取得失敗</p></figcaption></figure>

現在のリクエストはAxiosで構築されていますが、Axiosはsocksプロキシをサポートしていません。システムプロキシまたはHTTPプロキシを使用するか、CherryStudioでプロキシを設定せずにグローバルプロキシを使用してください。まずネットワーク接続が正常であることを確認し、Device Codeの取得失敗を防いでください。