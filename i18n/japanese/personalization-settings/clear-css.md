---
icon: trash-xmark
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# CSS設定のクリア

{% hint style="warning" %}
誤ったCSSを設定した場合や、CSS設定後に設定画面にアクセスできない場合に、この方法でCSS設定をクリアします。
{% endhint %}

* コンソールを開き、CherryStudioウィンドウをクリックして、ショートカットキー<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>を押します（MacOS：<kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>）。
* ポップアップしたコンソールウィンドウで、`Console`をクリックします

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* その後、手動で`document.getElementById('user-defined-custom-css').remove()`と入力します（コピー＆ペーストでは実行されない可能性が高いです）。
* 入力後、Enterキーを押して確定するとCSS設定がクリアされます。その後、再度CherryStudioの表示設定にアクセスし、問題のあるCSSコードを削除してください。