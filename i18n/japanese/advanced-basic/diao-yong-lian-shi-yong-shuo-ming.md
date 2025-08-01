---
icon: route
---
# 呼び出しチェーンの使用説明


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## 機能紹介

呼び出しチェーン（別名「トレース」）は、会話の洞察を提供し、ユーザーが対話プロセスにおけるモデル、ナレッジベース、MCP、ウェブ検索などの具体的なパフォーマンスを把握するのに役立ちます。これは[OpenTelemetry](https://opentelemetry.io/docs/languages/js/)を基に実装された可観測ツールで、エンドサイドのデータ収集・保存・処理により可視化を実現し、問題の特定や効果最適化のための定量評価基準を提供します。

各対話は1つのトレースデータに対応し、1つのトレースは複数のスパンで構成されます。各スパンはCherry Studioのプログラム処理ロジック（モデルセッション呼び出し、MCP呼び出し、ナレッジベース呼び出し、ウェブ検索呼び出しなど）に対応します。トレースはツリー構造で表示され、スパンがツリーノードとなります。主なデータには処理時間とトークン使用量が含まれ、スパンの詳細では具体的な入力/出力も確認できます。

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## トレースの有効化

デフォルトでは、Cherry Studioインストール後、トレースは非表示状態です。有効化には「設定」→「一般設定」→「開発者モード」で以下のように有効にします：

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

過去のセッションではトレース記録は生成されず、新しい質問応答が発生した後にのみ記録が生成されます。生成された記録はローカルに保存され、トレースを完全にクリアする場合は「設定」→「データ設定」→「データディレクトリ」→「キャッシュクリア」で実行可能です。または手動で `~/.cherrystudio/trace` ディレクトリのファイルを削除することもできます：

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## ユースケース紹介

### フルリンク表示

Cherry Studioのダイアログで呼び出しチェーンをクリックすると、全リンクデータを表示します。対話中にモデル、ウェブ検索、ナレッジベース、MCPのいずれを呼び出しても、呼び出しチェーンウィンドウで全リンク呼び出しデータを確認できます。

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### リンク中のモデル表示

呼び出しチェーン内のモデルの詳細を確認するには、モデル呼び出しノードをクリックし、その入力/出力の詳細を表示します。

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### リンク中のウェブ検索表示

呼び出しチェーン内のウェブ検索詳細を確認するには、ウェブ検索呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細では、呼び出した検索クエリと返却結果を確認できます。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### リンク中のナレッジベース表示

呼び出しチェーン内のナレッジベース詳細を確認するには、ナレッジベース呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細では、呼び出したクエリと返却された回答を確認できます。

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### リンク中のMCP呼び出し状況確認

呼び出しチェーン内のMCP詳細を確認するには、MCP呼び出しノードをクリックし、入力/出力の詳細を表示します。詳細では、当該MCPサーバーツールの入力パラメータとツールの返却結果を確認できます。

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## 問題と提案

現在の機能は阿里云[EDAS](https://www.aliyun.com/product/edas)チームが提供しています。問題やご提案がある場合は、DingTalkグループ（グループID: 21958624）に参加し、開発者と直接ご連絡ください。