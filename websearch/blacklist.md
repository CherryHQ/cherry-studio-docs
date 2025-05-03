---
icon: ban
---

# 网络搜索黑名单配置

Cherry Studio支持手动和添加订阅源两种方式配置黑名单。配置规则参考[ublacklist](https://github.com/iorate/ublacklist)

## 手动配置

您可以为搜索结果添加规则或点击工具栏图标以屏蔽指定的网站。规则可以通过以下方式指定：[匹配模式](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (示例：`*://*.example.com/*`) 或使用[正则表达式](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (示例：`/example\.(net|org)/`).

## 订阅源配置

您还可以订阅公共规则集。该网站列出了一些订阅：\
https://iorate.github.io/ublacklist/subscriptions

以下是一些比较推荐的订阅源链接：

| 名称                                                                                                    | 链接                                                                                                   | 类型   |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | 中文   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | AI生成 |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>订阅源配置</p></figcaption></figure>
