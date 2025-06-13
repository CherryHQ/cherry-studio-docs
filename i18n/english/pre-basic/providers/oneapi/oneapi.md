
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# OneAPI

* Log in and go to the token page

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

* Create a new token (or you can directly use the default token ↑)

<figure><img src="../../../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

* Copy the token

<figure><img src="../../../.gitbook/assets/image (24).png" alt="" width="563"><figcaption></figcaption></figure>

* Open CherryStudio's provider settings and click `Add` at the bottom of the provider list.
* Enter a note name, select OpenAI as the provider, and click OK.

<figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="291"><figcaption></figcaption></figure>

* Paste the key you just copied.
* Go back to the page where you got the API Key and copy the root address from the browser's address bar, for example:

<figure><img src="../../../.gitbook/assets/image (26).png" alt="" width="563"><figcaption><p><strong>You only need to copy https://xxx.xxx.com; the "/" and the content after it are not needed.</strong></p></figcaption></figure>

{% hint style="info" %}
* When the address is an IP + port, fill in http://IP:port, for example: http://127.0.0.1:3000
* Strictly distinguish between `http` and `https`. If SSL is not enabled, do not use https.
{% endhint %}

* Add models (click Manage to automatically fetch or manually enter them) and toggle the switch in the upper right corner to enable them.

{% hint style="success" %}
Other OneAPI themes may have different interfaces, but the method for adding them is the same as the process described above.
{% endhint %}