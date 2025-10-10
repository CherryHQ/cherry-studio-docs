# Huawei Cloud


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




I. Go to [Huawei Cloud](https://auth.huaweicloud.com/authui/login) to create an account and log in.

II. Click [this link](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) to enter the Maa S console.

III. Authorization

<details>

<summary>Authorization Steps (Skip if already authorized)</summary>

1. After entering the link page from step (II), follow the prompts to enter the authorization page (click IAM Sub-user → New Delegation → Ordinary User).

![](<../../.gitbook/assets/image (49).png>)

2. After clicking Create, return to the link page from step (II).
3. If prompted with insufficient access permissions, click "Click here" in the prompt.
4. Add existing authorization and confirm.

![](<../../.gitbook/assets/image (50).png>)

&#x20;Note: This method is suitable for beginners. You don't need to read too much content; just click according to the prompts. If you can authorize successfully in one go, you can do it your way.

</details>

IV. Click "Authentication Management" in the sidebar, create an API Key, and copy it.

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Then, create a new provider in CherryStudio.

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

After creation, fill in the API Key.

V. Click "Model Deployment" in the sidebar and claim all.

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

VI. Click "Invoke".

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Copy the address from ①, paste it into the CherryStudio provider address, and add a "#" at the end.

And add a "#" at the end.

And add a "#" at the end.

And add a "#" at the end.

And add a "#" at the end.

Why add "#"? [See here](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Of course, you can also skip reading that and just follow the tutorial;
>
> You can also fill it in by deleting "v1/chat/completions". If you know how to fill it, you can do it your way. If not, be sure to follow the tutorial.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Then, copy the model name from ②, and click the "+ Add" button in CherryStudio to create a new model.

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Enter the model name, do not embellish or add quotes; copy it exactly as shown in the example.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Click the "Add Model" button to complete the addition.

{% hint style="info" %}
In Huawei Cloud, since the address for each model is different, each model requires a new provider. You can repeat the steps above.
{% endhint %}