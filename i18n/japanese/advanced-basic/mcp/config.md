
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# MCPの設定と使用方法

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Cherry Studioの設定を開く
2. `MCPサーバー`オプションを探す
3. `サーバーを追加`をクリック
4. MCP Serverの関連パラメータを入力（[参考リンク](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。入力が必要な内容：
   * 名前：任意の名前（例：`fetch-server`）
   * タイプ：`STDIO`を選択
   * コマンド：`uvx`と入力
   * パラメータ：`mcp-server-fetch`と入力
   * （他のパラメータが存在する場合もあり、具体的なServerによる）
5. `保存`をクリック

{% hint style="success" %}
上記設定完了後、Cherry Studioは自動的に必要なMCP Server - `fetch server`をダウンロードします。ダウンロード完了後、使用を開始できます。注意：mcp-server-fetchの設定が成功しない場合、PCの再起動をお試しください。
{% endhint %}

### チャットボックスでMCPサービスを有効化

<figure><img src="../../.gitbook/assets/MCP-入力框按钮示例.png" alt=""><figcaption></figcaption></figure>

* `MCPサーバー`設定でMCPサーバーの追加に成功

<figure><img src="../../.gitbook/assets/MCPサーバー示例.png" alt=""><figcaption></figcaption></figure>

### **使用効果のデモ**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

上図から分かるように、MCPの`fetch`機能を組み合わせることで、Cherry Studioはユーザーのクエリ意図をより良く理解し、ウェブから関連情報を取得して、より正確で包括的な回答を提供できます。