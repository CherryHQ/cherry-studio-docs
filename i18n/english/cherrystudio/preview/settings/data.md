---
icon: database
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Data Settings

This interface allows users to perform operations such as cloud and local backup of client data, querying local data directories, and clearing cache.

### Data Backup

Currently, data backup is only supported via WebDAV. You can choose a WebDAV-supported service for cloud backup.

You can also achieve multi-device data synchronization through the method: `Computer A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restore}}$$ `Computer B`.

#### Using Nutstore as an example

1. Log in to Nutstore, click the username in the upper right corner, and select "Account Information":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Select "Security Options" and click "Add Application":

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Enter an application name and generate a random password:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copy and record the password:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtain the server address, account, and password:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. In Cherry Studio settings → Data settings, fill in the WebDAV information:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Choose to back up or restore data, and set the automatic backup frequency:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Common cloud storage services with low WebDAV usage barriers include:

* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (requires membership)
* [Aliyun Drive](https://www.alipan.com/) (requires purchase)
* [Box](https://www.box.com/) (10GB free space, 250MB file size limit)
* [Dropbox](https://www.dropbox.com/) (2GB free space, expandable to 16GB via referrals)
* [TeraCloud](https://teracloud.jp/en/) (10GB free space, +5GB via referrals)
* [Yandex Disk](https://disk.yandex.com/) (10GB free space)

Self-hosted solutions include:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}