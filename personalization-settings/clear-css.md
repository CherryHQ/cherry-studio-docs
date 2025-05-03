---
icon: trash-xmark
---

# 清除css设置



{% hint style="warning" %}
当设置了错误的css，或者在设置了css后无法进入设置界面时，使用该方法清除css设置。
{% endhint %}

* 打开控制台，点击CherryStudio窗口，按下快捷键<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>（MacOS：<kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>）。
* 在弹出的控制台窗口中，点击`Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* 然后手动输入`document.getElementById('user-defined-custom-css').remove()` ，复制粘贴大概率不会执行。
* 输入完成后回车确认即可清除css设置，然后再次进入CherryStudio的显示设置当中，删除有问题的css代码。
