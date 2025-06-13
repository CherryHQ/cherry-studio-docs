
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# MCPの設定と使用

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Cherry Studioの設定を開く
2. `MCP サーバー`オプションを探す
3. `サーバーを追加`をクリック
4. MCPサーバーの関連パラメータを入力（[参考リンク](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。入力が必要な内容：
   * 名称：任意の名称（例：`fetch-server`）
   * タイプ：`STDIO`を選択
   * コマンド：`uvx`と入力
   * 引数：`mcp-server-fetch`と入力
   * （特定のサーバーによっては他のパラメータが存在する場合あり）
5. `保存`をクリック

{% hint style="success" %}
上記の設定完了後、Cherry Studioは自動的に必要なMCPサーバー（`fetch server`）をダウンロードします。ダウンロードが完了すると使用を開始できます。注意：mcp-server-fetchの設定が失敗した場合は、コンピュータの再起動をお試しください。
{% endhint %}

### チャットボックスでMCPサービスを有効化

<figure><img src="../../.gitbook/assets/MCP-入力框按钮示例.png" alt=""><figcaption></figcaption></figure>

* `MCP サーバー`設定でMCPサーバーが正常に追加されている状態

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **使用効果の表示**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

上図からわかるように、MCPの`fetch`機能を統合することで、Cherry Studioはユーザーのクエリ意図をより正確に理解し、ウェブから関連情報を取得して、より正確で包括的な回答を提供できます。