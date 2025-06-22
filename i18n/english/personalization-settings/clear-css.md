---
icon: trash-xmark
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Clear CSS Settings

{% hint style="warning" %}
Use this method to clear CSS settings when incorrect CSS has been applied, or when you cannot access the settings interface after applying CSS.
{% endhint %}

* Open the console by clicking on the CherryStudio window and pressing <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* In the opened console window, click `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Then manually enter `document.getElementById('user-defined-custom-css').remove()`. Copying and pasting will most likely not work.
* After entering, press Enter to confirm and clear the CSS settings. Then, go back to CherryStudio's display settings and remove the problematic CSS code.