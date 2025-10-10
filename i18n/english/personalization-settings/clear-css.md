---
icon: trash-xmark
---
# Clear CSS Settings


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="warning" %}
Use this method to clear CSS settings when incorrect CSS is set, or when you cannot access the settings interface after setting CSS.
{% endhint %}

*   Open the console, click the CherryStudio window, and press the shortcut key <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
*   In the pop-up console window, click `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

*   Then manually type `document.getElementById('user-defined-custom-css').remove()`. Copying and pasting is unlikely to execute.
*   After typing, press Enter to confirm and clear the CSS settings. Then, re-enter CherryStudio's display settings and delete the problematic CSS code.