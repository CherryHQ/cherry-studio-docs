
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# GitHub Copilot

To use GitHub Copilot, you first need a GitHub account and a subscription to the GitHub Copilot service. A free version subscription is also acceptable, but the free version does not support the latest Claude 3.7 model. For details, please refer to the [official GitHub Copilot website](https://github.com/features/copilot).

## Get Device Code

Click "Login with GitHub" to get the Device Code and copy it.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Example image of getting a Device Code"><figcaption><p>Get Device Code</p></figcaption></figure>

## Enter the Device Code in the browser and authorize

After successfully obtaining the Device Code, click the link to open your browser. Log in to your GitHub account in the browser, enter the Device Code, and authorize.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Example image of GitHub authorization"><figcaption><p>GitHub Authorization</p></figcaption></figure>

After successful authorization, return to Cherry Studio and click "Connect to GitHub". Upon success, your GitHub username and avatar will be displayed.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Example image of a successful GitHub connection"><figcaption><p>GitHub Connection Successful</p></figcaption></figure>

## Click "Manage" to get the model list

Click the "Manage" button below, and it will automatically connect to the internet to fetch the list of currently supported models.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Example image of getting the model list via the Manage button"><figcaption><p>Get Model List</p></figcaption></figure>

## Frequently Asked Questions

### Failed to get Device Code, please retry

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Example image of failing to get a Device Code"><figcaption><p>Failed to get Device Code</p></figcaption></figure>

Currently, requests are built using Axios, which does not support SOCKS proxies. Please use a system proxy or an HTTP proxy, or alternatively, do not set a proxy within CherryStudio and use a global proxy instead. First, ensure your network connection is stable to avoid failing to obtain the Device Code.