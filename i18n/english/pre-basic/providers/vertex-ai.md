---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Tutorial Overview

### 1. Get API Key

* Before getting a Gemini API Key, you need to have a Google Cloud project (if you already have one, you can skip this step)
* Go to [Google Cloud](https://console.cloud.google.com/projectcreate) to create a project, fill in the project name, and click Create Project.

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Go to [Vertex AI Console](https://console.cloud.google.com/vertex-ai)
* Enable [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1&invt=Ab0iBA) in the created project.

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Set API Access Permissions

* Open the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) permissions page and create a service account.

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* On the service account management page, find the service account you just created, click `Keys` and create a new JSON format key.

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* After successful creation, the key file will be automatically saved to your computer in JSON file format. Please **keep it safe**.

## 3. Configure Vertex AI in Cherry Studio

* Select Vertex AI service provider
* Fill in the corresponding fields from the JSON file.

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Click to add [Model](https://console.cloud.google.com/vertex-ai/model-garden), and you can start using it happily!