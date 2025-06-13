---
icon: trash-xmark
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 清除css設定  

{% hint style="warning" %}
當設定了錯誤的css，或在設定css後無法進入設定界面時，請使用此方法清除css設定。  
{% endhint %}  

* 開啟控制台：點擊CherryStudio視窗，按下快捷鍵 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>（MacOS：<kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>）。  
* 在彈出的控制台視窗中，點選`Console`分頁  

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>  

* 手動輸入 `document.getElementById('user-defined-custom-css').remove()`（複製貼上可能無法執行）。  
* 輸入完畢後按下 Enter鍵 確認，即可清除css設定。隨後可重新進入CherryStudio的顯示設定中，刪除有問題的css程式碼。