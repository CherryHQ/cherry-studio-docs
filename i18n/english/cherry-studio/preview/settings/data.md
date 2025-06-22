---
icon: database
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Data Settings

This interface allows you to perform operations such as cloud and local backup of client data, querying the local data directory, and clearing the cache.

### Data Backup

Currently, data backup only supports WebDAV. You can choose a service that supports WebDAV for cloud backup.

You can also synchronize data across multiple devices by following the process: `Computer A` $$\xrightarrow{\text{Backup}}$$ `WebDAV` $$\xrightarrow{\text{Restore}}$$ `Computer B`.

#### Taking Jianguoyun as an Example

1.  Log in to Jianguoyun, click on the username in the upper right corner, and select "Account Info":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2.  Select "Security Options" and click "Add Application"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3.  Enter the application name and generate a random password;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4.  Copy and save the password;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5.  Obtain the server address, account, and password;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6.  In Cherry Studio Settings -> Data Settings, fill in the WebDAV information;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7.  Choose to back up or restore data, and you can set the automatic backup time interval.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Generally, the easiest WebDAV services to get started with are cloud storage providers:

*   [Jianguoyun](https://www.jianguoyun.com/)
*   [123Pan](https://www.123pan.com/) (Requires membership)
*   [Aliyun Drive](https://www.alipan.com/) (Requires purchase)
*   [Box](https://www.box.com/) (Free space is 10GB, single file size limit is 250MB.)
*   [Dropbox](https://www.dropbox.com/) (Dropbox offers 2GB for free, and you can get up to 16GB by inviting friends.)
*   [TeraCloud](https://teracloud.jp/en/) (Free space is 10GB, and an additional 5GB can be obtained through referrals.)
*   [Yandex Disk](https://disk.yandex.com/) (Provides 10GB of capacity for free users.)

Next are some services that you need to deploy yourself:

*   [Alist](https://alist.nn.ci/zh/)
*   [Cloudreve](https://cloudreve.org/)
*   [sharelist](https://github.com/reruin/sharelist)
{% endhint %}