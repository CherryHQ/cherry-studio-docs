---
icon: trash-xmark
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 清除CSS設定

{% hint style="warning" %}
當設定了錯誤的CSS，或在設定CSS後無法進入設定界面時，使用此方法清除CSS設定。
{% endhint %}

* 開啟控制台：點擊CherryStudio視窗，按下快捷鍵<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>（MacOS：<kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>）。
* 在彈出的控制台視窗中，點選`Console`標籤頁
<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* 手動輸入`document.getElementById('user-defined-custom-css').remove()`（複製貼上通常不會被執行）。
* 輸入完成後按Enter確認，即可清除CSS設定。隨後再次進入CherryStudio的顯示設定中刪除有問題的CSS程式碼。