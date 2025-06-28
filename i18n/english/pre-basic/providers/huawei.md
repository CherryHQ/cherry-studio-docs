# Huawei Cloud

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

## Huawei Cloud

1. Create an account and log in at [Huawei Cloud](https://auth.huaweicloud.com/authui/login)
2. Click [this link](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) to enter the MaaS control panel
3. Authorization

<details>

<summary>Authorization steps (skip if already authorized)</summary>

1. After entering the link from step 2, follow the prompts to the authorization page (click IAM sub-account → Add Authorization → General User)\
   ![](<../../.gitbook/assets/image (49).png>)
2. After clicking create, return to the link from step 2
3. If prompted "insufficient access permissions", click "click here" in the prompt
4. Append existing authorization and confirm\
   ![](<../../.gitbook/assets/image (50).png>)\
   Note: This method is suitable for beginners; no need to read excessive content, just follow the prompts. If you can successfully authorize using your own method, proceed accordingly.

</details>

4.  Click Authentication Management in the sidebar, create an API Key (secret key) and copy it

    <figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

    Then create a new service provider in CherryStudio

    <figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

    After creation, enter the secret key
5.  Click Model Deployment in the sidebar, claim all offerings

    <figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>
6.  Click Call

    <figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

    Copy the address from ①, paste it into CherryStudio's service provider address field and add a "#" at the end\
    and add a "#" at the end\
    and add a "#" at the end\
    and add a "#" at the end\
    and add a "#" at the end\
    Why add "#"? \[see here]\(https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)\
    \> You can choose not to read that and just follow this tutorial;\
    \> Alternatively, you can fill it by removing v1/chat/completions - feel free to use your own method if you know how, but if not, strictly follow this tutorial.

    <figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

    Then copy the model name from ②, and click the "+ Add" button in CherryStudio to create a new model

    <figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

    Enter the model name exactly as shown - do not add or remove anything, and don't include quotes. Copy exactly as in the example.

    <figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

    Click the Add Model button to complete.

{% hint style="info" %}
In Huawei Cloud, since each model has a different endpoint, you'll need to create a new service provider for each model. Repeat the above steps accordingly.
{% endhint %}
