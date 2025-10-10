# OneAPI


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




*   Log in and go to the token page

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

*   Create a new token (you can also use the default token directly ↑)

<figure><img src="../../../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

*   Copy the token

<figure><img src="../../../.gitbook/assets/image (24).png" alt="" width="563"><figcaption></figcaption></figure>

*   Open CherryStudio's service provider settings and click `Add` at the bottom of the service provider list.
*   Enter a remark name, select OpenAI as the provider, and click Confirm.

<figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="291"><figcaption></figcaption></figure>

*   Fill in the key you just copied.
*   Go back to the API Key acquisition page, and copy the root address from the corresponding browser's address bar, e.g.:

<figure><img src="../../../.gitbook/assets/image (26).png" alt="" width="563"><figcaption><p><strong>Only copy https://xxx.xxx.com; the "/" and anything after it are not needed.</strong></p></figcaption></figure>

{% hint style="info" %}
*   When the address is IP+Port, just fill in http://IP:Port, e.g., http://127.0.0.1:3000
*   Strictly distinguish between `http` and `https`; if SSL is not enabled, do not use `https`.
{% endhint %}

*   Add a model (click Manage to auto-acquire or enter manually) and turn on the switch in the upper right corner to use it.

{% hint style="success" %}
Other OneAPI themes might have different interfaces, but the adding method is consistent with the process described above.
{% endhint %}