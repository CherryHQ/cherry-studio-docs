---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Vertex AI

## Tutorial Overview

### 1. Obtaining API Key

*   Before obtaining the Gemini API Key, you need to have a Google Cloud project (if you already have one, this process can be skipped)
*   Go to [Google Cloud](https://console.cloud.google.com/projectcreate) to create a project, fill in the project name and click Create Project

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

*   Access the [Vertex AI console](https://console.cloud.google.com/vertex-ai)
*   Enable [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) in the created project

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Setting API Access Permissions

*   Open the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) permissions page and create a service account

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   On the service account management page, find the service account you just created, click `Keys` and create a new JSON key

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   After successful creation, the key file will be automatically saved to your computer in JSON format. Please **store it securely**

## 3. Configuring Vertex AI in Cherry Studio

*   Select Vertex AI as the service provider
*   Fill in the corresponding fields from the JSON file

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Click [Add Model](https://console.cloud.google.com/vertex-ai/model-garden), and you can start using it!