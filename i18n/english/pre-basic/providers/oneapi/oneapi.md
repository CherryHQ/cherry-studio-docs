
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# OneAPI

* Log in and navigate to the tokens page

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

* Create a new token (you can also directly use the default token ↑)

<figure><img src="../../../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

* Copy the token

<figure><img src="../../../.gitbook/assets/image (24).png" alt="" width="563"><figcaption></figcaption></figure>

* Open CherryStudio's service provider settings and click `Add` at the bottom of the provider list
* Enter a note name, select OpenAI as the provider, and click OK

<figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="291"><figcaption></figcaption></figure>

* Paste the key you just copied
* Return to the API Key page, copy the root address from the browser's address bar, for example:

<figure><img src="../../../.gitbook/assets/image (26).png" alt="" width="563"><figcaption><p><strong>Only copy https://xxx.xxx.com - do not include content after "/"</strong></p></figcaption></figure>

{% hint style="info" %}
* When the address is IP + port, fill in http://IP:port, e.g., http://127.0.0.1:3000
* Strictly distinguish between `http` and `https` - don't use https if SSL isn't enabled
{% endhint %}

* Add models (click Manage to auto-fetch or enter manually) and toggle the switch in the top right corner to start using.

{% hint style="success" %}
The interface may differ in other OneAPI themes, but the addition method follows the same workflow as above.
{% endhint %}