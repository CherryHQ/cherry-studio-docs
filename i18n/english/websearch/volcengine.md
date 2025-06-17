---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Connecting to Volcano Engine with Networking

### 1. Log in/Register for a "Volcano Engine" Account <a href="#rclz7" id="rclz7"></a>

Visit the official website: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Volcano Engine official website</p></figcaption></figure>

### 2. Create a "My Application" with Networking Capabilities <a href="#gvzaa" id="gvzaa"></a>

2.1. Log in to Volcano Engine and go to the "Volcano Ark" page. Portal: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Click in order:** <mark style="color:red;">**"My Applications" - "Create Application" - "Zero-code" - "Single Chat"**</mark>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Fill in Information and Publish the Application <a href="#zzdfe" id="zzdfe"></a>

**Application Name**: Just give it a name as required. (Fields marked with <mark style="color:red;">**\* are required**</mark>, others can be left blank).

<mark style="color:red;">**The key is: enable the networking plugin (needs to be activated first).**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Activate the Networking Plugin Function (Note the fees and free quotas) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Click "Buy Now" and follow the steps until the interface below is displayed, which indicates successful activation.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Note the status. Activation is now successful.</p></figcaption></figure>

Then, return to the "Fill Application Information" interface and continue.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Explanation of "Advanced Configuration" for Networked Search <a href="#sp6uz" id="sp6uz"></a>

Choose based on your actual needs. Personal recommendation:

*   If you want precise control over input and output, use "**Custom Invocation**" for networking;
*   If you find it troublesome, you can leave it unchanged and use "**Automatic Invocation**" - the default value;
*   If money is not an issue and you have high requirements for information timeliness, you can "**Force Enable**".

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publish the Application <a href="#fe1gf" id="fe1gf"></a>

Click the "Publish" button in the upper right corner. The application is created successfully.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obtain the API Key <a href="#jtqlu" id="jtqlu"></a>

Click in order: **"API Call Guide" - "Select API Key and Copy" - "View and Select"**

Copy the API key first, then we will go to Cherry Studio to paste it. (See the interface below for operation details).

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Note: If you don't have an API key, click "**Create API Key**" in the upper right corner of the pop-up window, and then copy the API key.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Use the API Key in Cherry Studio to Access deepseek-R1 with Networking <a href="#lrefj" id="lrefj"></a>

#### 5.1. Open Cherry Studio - "Settings" - "Enter any name" - "Type: OpenAI" <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Configure URL and Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Note, if you can't find the address, or if it's not the Beijing node, you can find the specific address here. Remember not to forget the "/":</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Add the Model Name <a href="#qmh3i" id="qmh3i"></a>

Note, copy the smaller text below as the model name, otherwise an error will occur.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Effect Preview <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>