---
icon: trash-xmark
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Clear CSS Settings

{% hint style="warning" %}
Use this method to clear CSS settings when you have set incorrect CSS or cannot enter the settings interface after setting the CSS.
{% endhint %}

* Open the console, click on the CherryStudio window, and press the shortcut key <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* In the console window that pops up, click `Console`.

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Then, manually type `document.getElementById('user-defined-custom-css').remove()`. Copying and pasting will likely not execute.
* After typing, press Enter to confirm and clear the CSS settings. Then, go back to CherryStudio's display settings and delete the problematic CSS code.