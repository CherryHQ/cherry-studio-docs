---
icon: ban
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 網路搜尋黑名單配置

Cherry Studio支援手動和新增訂閱來源兩種方式設定黑名單。設定規則參考[ublacklist](https://github.com/iorate/ublacklist)

## 手動配置

您可以為搜尋結果新增規則或點選工具列圖示以封鎖指定的網站。規則可以透過以下方式指定：[匹配模式](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (示例：`*://*.example.com/*`) 或使用[正則表達式](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (示例：`/example\.(net|org)/`).

## 訂閱來源配置

您還可以訂閱公共規則集。該網站列出了一些訂閱：\
https://iorate.github.io/ublacklist/subscriptions

以下是一些比較推薦的訂閱來源連結：

| 名稱                                                                                                    | 連結                                                                                                   | 類型   |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | 中文   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | AI生成 |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>訂閱來源配置</p></figcaption></figure>