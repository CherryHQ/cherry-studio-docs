---
icon: ban
---
# ウェブ検索ブラックリスト設定


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




{% hint style="warning" %}
**注意:** このドキュメントはAIによる中国語からの翻訳であり、現在レビュー待ち状態です。  
ドキュメントをひとつずつ確認し、翻訳の適切性を検証するよう努めます。
{% endhint %}

Cherry Studioでは、手動登録とソース購読の2通りの方法でブラックリストを設定できます。設定ルールは[ublacklist](https://github.com/iorate/ublacklist)を参照してください。

## 手動設定

検索結果にルールを追加するか、ツールバーアイコンをクリックして特定サイトをブロックできます。ルールは以下の方法で指定可能です：[マッチパターン](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (例：`*://*.example.com/*`) または[正規表現](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (例：`/example\.(net|org)/`)。

## 購読ソース設定

公開ルールセットを購読することも可能です。こちらのサイトで各種購読リストを確認できます：  
https://iorate.github.io/ublacklist/subscriptions

特におすすめの購読ソース：

| 名称                                                                                                      | リンク                                                                                                                             | タイプ   |
| :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation)     | https://git.io/ublacklist                                                                                                          | 中国語   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)             | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt                                | AI生成   |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>購読ソース設定画面</p></figcaption></figure>