---
icon: trash-xmark
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# CSS設定のクリア

{% hint style="warning" %}
誤ったCSSを設定した場合や、CSS設定後に設定画面に入れなくなった場合に、この方法でCSS設定をクリアできます。
{% endhint %}

* コンソールを開く：CherryStudioウィンドウをクリックし、<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>キー（MacOS：<kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>）を押します。
* 表示されたコンソールウィンドウで、`Console`タブをクリックします

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* 手動で`document.getElementById('user-defined-custom-css').remove()`と入力します（コピー＆ペーストでは通常実行されません）。
* 入力後Enterキーを押すとCSS設定がクリアされます。その後、改めてCherryStudioの表示設定画面で問題のあるCSSコードを削除してください。