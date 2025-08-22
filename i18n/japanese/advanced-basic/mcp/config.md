# MCPの設定と使用方法


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Cherry Studioの設定を開きます。
2. `MCP サーバー`オプションを探します。
3. `サーバーを追加`をクリックします。
4. MCPサーバーの関連パラメータを入力します（[参考リンク](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。入力が必要な内容は以下の通りです：
   * 名称：任意の名前（例：`fetch-server`）
   * タイプ：`STDIO`を選択
   * コマンド：`uvx`と入力
   * 引数：`mcp-server-fetch`と入力
   * （その他のパラメータが必要な場合があります）
5. `保存`をクリックします。

{% hint style="success" %}
上記設定を完了すると、Cherry Studioは必要なMCPサーバー「fetch server」を自動的にダウンロードします。ダウンロードが完了したら使用を開始できます。注意：mcp-server-fetchの設定が失敗した場合、コンピューターの再起動をお試しください。
{% endhint %}

### チャットボックスでMCPサービスを有効化

<figure><img src="../../.gitbook/assets/MCP-入力框按钮示例.png" alt=""><figcaption></figcaption></figure>

* `MCP サーバー`設定でMCPサーバーが正常に追加された状態

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **使用効果のデモ**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

上図のように、MCPの`fetch`機能を組み合わせることで、Cherry Studioはユーザーの検索意図をより良く理解し、ウェブから関連情報を取得して、より正確で包括的な回答を提供できるようになります。