---
icon: ban
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# ネットワーク検索ブラックリスト設定

Cherry Studioでは手動設定と購読ソース追加の2つの方法でブラックリストを設定できます。設定ルールは[ublacklist](https://github.com/iorate/ublacklist)を参照してください。

## 手動設定

検索結果にルールを追加するか、ツールバーアイコンをクリックして特定のウェブサイトをブロックできます。ルールは以下の方法で指定可能です：[マッチパターン](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns)（例：`*://*.example.com/*`）または[正規表現](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions)（例：`/example\.(net|org)/`）。

## 購読ソース設定

公開ルールセットを購読することもできます。以下のサイトで購読リストを確認できます：\
https://iorate.github.io/ublacklist/subscriptions

おすすめの購読ソースリンク：

| 名称                                                                                                    | リンク                                                                                                   | タイプ   |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | 中国語   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | AI生成 |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>購読ソース設定</p></figcaption></figure>