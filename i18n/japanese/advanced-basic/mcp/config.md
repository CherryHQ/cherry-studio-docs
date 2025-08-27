# MCPの設定と使用方法


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Cherry Studioの設定を開く
2. `MCP サーバー`オプションを探す
3. `サーバーを追加`をクリック
4. MCP Serverの関連パラメータを入力（[参考リンク](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。入力が必要な内容：
   * 名称：任意の名前（例：`fetch-server`）
   * タイプ：`STDIO`を選択
   * コマンド：`uvx`を入力
   * 引数：`mcp-server-fetch`を入力
   * （その他Server固有のパラメータがある場合）
5. `保存`をクリック

{% hint style="success" %}
上記設定が完了すると、Cherry Studioは必要なMCP Server（`fetch server`）を自動的にダウンロードします。ダウンロード完了後、使用を開始できます。注意：mcp-server-fetchの設定が失敗する場合、PCの再起動をお試しください。
{% endhint %}

### チャットボックスでMCPサービスを有効化

<figure><img src="../../.gitbook/assets/MCP-入力框按钮示例.png" alt=""><figcaption></figcaption></figure>

* `MCP サーバー`設定にサーバーが正常に追加された状態

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **使用効果のデモンストレーション**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

上図から分かるように、MCPの`fetch`機能を統合することで、Cherry Studioはユーザーのクエリ意図をより正確に理解し、Webから関連情報を取得して、より正確で包括的な回答を提供できます。