---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---
# Volcengine Internet Access Integration


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




### 1. Log in/Register for a "Volcengine" account <a href="#rclz7" id="rclz7"></a>

Visit official website: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Volcengine Official Website</p></figcaption></figure>

### 2. Create "My Application" with Internet Access <a href="#gvzaa" id="gvzaa"></a>

2.1. Log in to Volcengine, go to the "Volcengine Ark" page, portal: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Click in order:** <mark style="color:red;">**"My Applications" - "Create Application" - "No-Code" - "Single Chat"**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Fill in Information and Publish Application <a href="#zzdfe" id="zzdfe"></a>

**Application Name**: You can name it anything according to the requirements. (Fields marked with <mark style="color:red;">**\* are required**</mark>, others can be left blank)

<mark style="color:red;">**Key point: The Internet Access Plugin must be enabled (needs to be activated first)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Enable Internet Access Plugin (Note costs and free usage) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Click "Buy Now" and follow the steps until the interface below is displayed, indicating successful activation.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Note the status, activation is successful.</p></figcaption></figure>

Then return to the "Fill in Application Information" interface and continue.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Internet Search "Advanced Configuration" Description <a href="#sp6uz" id="sp6uz"></a>

Choose according to actual needs, personal suggestions:

*   If you want precise control over input and output, you can use "**Custom Call**" for internet access;
*   If you find it troublesome, you can leave it unchanged and use "**Auto Call**" - default value;
*   If budget is not an issue and real-time information is critical, you can "**Force Enable**".

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publish Application <a href="#fe1gf" id="fe1gf"></a>

Click the "Publish" button in the upper right corner to successfully create the application.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obtain API Key <a href="#jtqlu" id="jtqlu"></a>

Click in order: **"API Calling Guide" - "Select API Key and Copy" - "View and Select"**

Copy the API key first, then go to cherry studio and paste it. (For operation details, see the interface below)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Note: If there is no API key, click "**Create API Key**" in the upper right corner of the pop-up window, then copy the API key.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Use API Key in cherry studio to enable internet access for deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Open cherry studio - "Settings" - "Name it anything" - "Type: openAI" <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Configure URL and Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Note, if you can't find the address, or if it's not a Beijing node, you can find the specific address here. Don't forget the "/" character:</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Add Model Name <a href="#qmh3i" id="qmh3i"></a>

Note, copy the small text below as the model name, otherwise it will cause an error.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Preview of Effect <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>