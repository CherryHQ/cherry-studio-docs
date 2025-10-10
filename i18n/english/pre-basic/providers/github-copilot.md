# GitHub Copilot


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




To use GitHub Copilot, you need to have a GitHub account and subscribe to the GitHub Copilot service. A free subscription is also acceptable, but the free version does not support the latest Claude 3.7 model. For details, please refer to the [official GitHub Copilot website](https://github.com/features/copilot).

## Obtain Device Code

Click "Log in to GitHub" to obtain and copy the Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Example image for obtaining Device Code"><figcaption><p>Obtain Device Code</p></figcaption></figure>

## Enter Device Code in Browser and Authorize

After successfully obtaining the Device Code, click the link to open your browser, log in to your GitHub account in the browser, enter the Device Code, and authorize.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Example image for GitHub authorization"><figcaption><p>GitHub Authorization</p></figcaption></figure>

After successful authorization, return to Cherry Studio, click "Connect GitHub", and your GitHub username and avatar will be displayed upon success.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Example image for successful GitHub connection"><figcaption><p>GitHub Connection Successful</p></figcaption></figure>

## Click "Manage" to Get Model List

Click the "Manage" button below to automatically retrieve the list of currently supported models online.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Example image for getting model list with Manage button"><figcaption><p>Get Model List</p></figcaption></figure>

## Frequently Asked Questions

### Failed to Obtain Device Code, Please Retry

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Example image for failed Device Code acquisition"><figcaption><p>Failed to Obtain Device Code</p></figcaption></figure>

Currently, requests are built using Axios, which does not support SOCKS proxies. Please use a system proxy or HTTP proxy, or do not set a proxy directly in CherryStudio and use a global proxy instead. First, please ensure your network connection is normal to avoid failures in obtaining the Device Code.