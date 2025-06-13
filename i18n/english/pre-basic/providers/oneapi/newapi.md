
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# NewAPI

*   Log in and open the token page
*   Click "Add Token"

<figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

*   Enter a token name and click "Submit" (other settings can be configured as needed).

<figure><img src="../../../.gitbook/assets/image (29).png" alt="" width="240"><figcaption></figcaption></figure>

*   Open the provider settings in CherryStudio and click `Add` at the bottom of the provider list.
*   Enter a memo name, select OpenAI as the provider, and click OK.

<figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="291"><figcaption></figcaption></figure>

*   Paste the key you just copied.
*   Go back to the page where you obtained the API Key and copy the base URL from your browser's address bar. For example:

<figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption><p><strong>You only need to copy https://xxx.xxx.com. The "/" and everything that follows are not needed.</strong></p></figcaption></figure>

{% hint style="info" %}
*   When the address is an IP + port, enter http://IP:port, for example: http://127.0.0.1:3000
*   Strictly distinguish between `http` and `https`. If SSL is not enabled, do not use https.
{% endhint %}

*   Add models (click "Manage" to fetch them automatically or enter them manually), then enable the switch in the top-right corner to start using them.