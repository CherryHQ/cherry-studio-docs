---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Connecting to VolcEngine for Online Access

### 1. Login/Register a VolcEngine Account <a href="#rclz7" id="rclz7"></a>

Visit official website: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>VolcEngine Official Website</p></figcaption></figure>

### 2. Create "My Application" with Online Capability <a href="#gvzaa" id="gvzaa"></a>

2.1. Log in to VolcEngine and navigate to "Volc Ark" page: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Follow:** <mark style="color:red;">**"My Applications" → "Create Application" → "Zero-Code" → "Single Chat"**</mark>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Fill Information and Publish Application <a href="#zzdfe" id="zzdfe"></a>

**Application Name**: Any valid name (<mark style="color:red;">**required***</mark>, other fields optional)

<mark style="color:red;">**Key step: Enable Online Plugin (requires activation)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1 Activate Online Plugin (Note costs and free quotas) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Click "Purchase Now" and follow steps until shown below, indicating successful activation.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Check status - successfully activated</p></figcaption></figure>

Return to "Fill Application Information" interface to continue.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2 Online Search "Advanced Configuration" <a href="#sp6uz" id="sp6uz"></a>

Recommended options:
* For precise control: Use **"Custom Invocation"**
* For simplicity: Keep **"Auto Invocation"** (default)
* For high timeliness: Use **"Force Enable"** (increases costs)

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3 Publish Application <a href="#fe1gf" id="fe1gf"></a>

Click "Publish" in top-right corner to finalize creation.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obtain API Key <a href="#jtqlu" id="jtqlu"></a>

Navigate: **"API Guide" → "Select API Key" → "Copy"**

Copy API Key for Cherry Studio configuration (details below):

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Note: If no API Key exists, click **"Create API Key"** in top-right corner.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Use API Key in Cherry Studio for Online Access to DeepSeek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1 Open Cherry Studio → "Settings" → Enter Name → Select Type: **OpenAI** <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2 Configure URL and Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Important: Find exact endpoint address in this location (note trailing "/"):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3 Add Model Name <a href="#qmh3i" id="qmh3i"></a>

Copy the model name from secondary text (small font) to avoid errors.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Preview Effect <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>