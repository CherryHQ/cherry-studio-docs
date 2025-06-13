---
icon: database
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# データ保存に関する説明

Cherry Studioナレッジベースに追加されたデータはすべてローカルに保存されます。追加時に、ドキュメントのコピーがCherry Studioデータ保存ディレクトリに置かれます。

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>ナレッジベース処理フローチャート</p></figcaption></figure>

ベクトルデータベース：[https://turso.tech/libsql](https://turso.tech/libsql)

ドキュメントがCherry Studioナレッジベースに追加されると、ファイルはいくつかのセグメントに分割され、その後、これらのセグメントは埋め込みモデルによって処理されます。

大規模言語モデルを使用して質問応答を行う際、問題に関連するテキストセグメントを検索し、それらを大規模言語モデルに渡して処理します。

データのプライバシーに関する要件がある場合は、ローカルの埋め込みデータベースとローカルの大規模言語モデルの使用をお勧めします。