---
icon: ban
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# ネット検索ブラックリスト設定

Cherry Studioは、手動設定とフィード購読の2通りの方法でブラックリストを設定できます。設定ルールは[ublacklist](https://github.com/iorate/ublacklist)を参照してください。

## 手動設定

検索結果にルールを追加するか、ツールバーアイコンをクリックして特定のサイトをブロックできます。ルールは以下の方法で指定可能です：[マッチパターン](https://developer.mozilla.org/ja/docs/Mozilla/Add-ons/WebExtensions/Match_patterns)（例: `*://*.example.com/*`) または[正規表現](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Regular_expressions)（例: `/example\.(net|org)/`）。

## フィード購読設定

パブリックなルールセットを購読することも可能です。購読可能なリストは以下のサイトで公開されています：\
https://iorate.github.io/ublacklist/subscriptions

以下におすすめの購読リンクを紹介します：

| 名前                                                                                                      | リンク                                                                                                                          | 種類           |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation)     | https://git.io/ublacklist                                                                                                       | 中国語（中国語） |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)             | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt                          | AI生成         |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>フィード購読設定</p></figcaption></figure>