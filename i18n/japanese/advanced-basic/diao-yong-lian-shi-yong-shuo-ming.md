---
icon: route
---
# コールチェーン利用説明


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## 機能紹介

コールチェーン（別名「トレース」）は、対話中の洞察機能をユーザーに提供し、モデル・ナレッジベース・MCP・ネットワーク検索などが対話プロセスでどのように動作しているかを把握するのに役立ちます。これは[OpenTelemetry](https://opentelemetry.io/docs/languages/js/)を基に実装された可観測ツールであり、エンド側でのデータ収集・保存・処理を通じて可視化を実現し、問題の特定や効果の最適化に定量的な評価基準を提供します。

各対話は1つのトレースデータに対応し、1つのトレースは複数のスパンで構成されます。各スパンはCherry Studioのプログラム処理ロジック（例: モデルセッション呼び出し、MCP呼び出し、ナレッジベース呼び出し、ネットワーク検索呼び出し）に対応します。トレースはツリー構造で表示され、スパンがツリーノードとなります。主なデータには処理時間・トークン使用量が含まれ、スパン詳細では具体的な入力/出力を確認できます。

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## トレースの有効化

デフォルトでは、Cherry Studioインストール後、トレースは非表示状態です。「設定」＞「一般設定」＞「開発者モード」で有効化する必要があります（下図参照）:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

なお、有効化前のセッションにはトレース記録が生成されず、新規Q&A発生後にのみ記録が生成されます。生成された記録はローカルに保存され、トレースを完全に消去するには「設定」＞「データ設定」＞「データディレクトリ」＞「キャッシュクリア」を実行するか、手動で`~/.cherrystudio/trace`下のファイルを削除します（下図参照）:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## ユースケース紹介

### フルチェーン表示

Cherry Studioの対話ボックスで「コールチェーン」をクリックすると、コールチェーンのフルチェーンデータを表示します。対話プロセスでモデル・ネットワーク検索・ナレッジベース・MCPのいずれを呼び出しても、コールチェーンウィンドウでフルチェーン呼び出しデータを確認できます。

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### チェーン内モデル確認

チェーン内のモデル詳細を確認するには、モデル呼び出しノードをクリックし、入力/出力の詳細を表示します。

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### チェーン内ネットワーク検索確認

ネットワーク検索の詳細を確認するには、ネットワーク検索呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細画面では、ネットワーク検索でクエリした問題と返却結果を確認できます。

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### チェーン内ナレッジベース確認

ナレッジベースの詳細を確認するには、ナレッジベース呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細画面では、クエリした問題と返却された回答を確認できます。

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### チェーン内MCP呼び出し状況確認

MCPの詳細を確認するには、MCP呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細画面では、当該MCP Server toolへの入力パラメータとtoolの返却結果を確認できます。

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## 問題と提案

現在の機能はAlibaba Cloud [EDAS](https://www.aliyun.com/product/edas)チームが提供しています。問題や提案がある場合は、DingTalkグループ（グループID：21958624）に参加し、開発者と直接ご連絡ください。