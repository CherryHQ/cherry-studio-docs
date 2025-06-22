
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# GitHub Copilot

To use GitHub Copilot, you must first have a GitHub account and subscribe to the GitHub Copilot service. The free subscription tier is acceptable, but note that it does not support the latest Claude 3.7 model. For details, refer to the [GitHub Copilot official website](https://github.com/features/copilot).

## Obtain Device Code

Click "Log in with GitHub" to generate and copy your Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Example image showing Device Code retrieval"><figcaption><p>Obtaining Device Code</p></figcaption></figure>

## Enter Device Code in Browser and Authorize

After obtaining your Device Code, click the link to open your browser. Log in to your GitHub account, enter the Device Code, and grant authorization.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Example image of GitHub authorization"><figcaption><p>GitHub Authorization</p></figcaption></figure>

After successful authorization, return to Cherry Studio and click "Connect GitHub". Your GitHub username and avatar will appear upon successful connection.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Example image of successful GitHub connection"><figcaption><p>GitHub Connected Successfully</p></figcaption></figure>

## Click "Manage" to Get Model List

Click the "Manage" button below, which will automatically fetch the currently supported models list online.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Example image showing model list retrieval"><figcaption><p>Fetching Model List</p></figcaption></figure>

## Common Issues

### Failed to Obtain Device Code, Please Retry

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Example image of Device Code retrieval failure"><figcaption><p>Device Code Retrieval Failed</p></figcaption></figure>

The current implementation uses Axios for network requests. Note that Axios does not support SOCKS proxies. Please use a system proxy or HTTP proxy, or avoid setting proxies within CherryStudio and use a global proxy instead. First, ensure your network connection is stable to prevent Device Code retrieval failures.