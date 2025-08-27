---
icon: route
---
# トレースの使用説明


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## 機能の紹介

トレース（別名「trace」）は、ユーザーに会話の洞察力を提供し、モデル、ナレッジベース、MCP、ウェブ検索などが会話プロセスでどのように動作しているかを把握するのに役立ちます。これは[OpenTelemetry](https://opentelemetry.io/docs/languages/js/)を基盤に実装された可観測ツールで、エンド側でのデータ収集、保存、処理を通じて可視化を実現し、問題の特定や効果の最適化に定量評価の根拠を提供します。

各会話は1つのトレースデータに対応し、1つのトレースは複数のスパンで構成されます。各スパンはCherry Studioの処理ロジック（モデル呼び出し、MCP呼び出し、ナレッジベース呼び出し、ウェブ検索呼び出しなど）に対応します。トレースはツリー構造で表示され、スパンがツリーノードとなります。主なデータには処理時間やトークン使用量が含まれ、スパンの詳細では具体的な入力/出力を確認できます。

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## トレースの有効化

デフォルトでは、Cherry Studioインストール後、トレースは非表示状態です。「設定」→「一般設定」→「開発者モード」で有効化する必要があります（下図参照）：

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

過去の会話にはトレース記録が生成されず、新しいQ&Aが発生した後にのみ記録が生成されます。生成された記録はローカルに保存され、トレースを完全に消去するには「設定」→「データ設定」→「データディレクトリ」→「キャッシュをクリア」で実行するか、手動で`~/.cherrystudio/trace`ディレクトリのファイルを削除します（下図参照）：

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## ユースケース紹介

### フルチェーンの確認

Cherry Studioのダイアログでトレースアイコンをクリックすると、トレースのフルチェーンデータを表示します。会話中にモデル、ウェブ検索、ナレッジベース、MCPのいずれを呼び出しても、トレースウィンドウでフルチェーン呼び出しデータを確認できます。

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### チェーン内モデルの確認

チェーン内のモデル詳細を確認するには、モデル呼び出しノードをクリックし、入力/出力の詳細を表示します。

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### チェーン内ウェブ検索の確認

チェーン内のウェブ検索詳細を確認するには、ウェブ検索呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細では、ウェブ検索でクエリした問題と返された結果を確認できます。

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### チェーン内ナレッジベースの確認

チェーン内のナレッジベース詳細を確認するには、ナレッジベース呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細では、ナレッジベースでクエリした問題と返された回答を確認できます。

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### チェーン内MCP呼び出し状況の確認

チェーン内のMCP詳細を確認するには、MCP呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細では、このMCP Server toolを呼び出す際のパラメータとtoolの返り値を確認できます。

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## 問題と提案

現在の機能はAlibaba Cloud [EDAS](https://www.aliyun.com/product/edas)チームが提供しています。問題や提案がある場合は、DingTalkグループ（グループID: 21958624）に参加し、開発者と直接ご連絡ください。