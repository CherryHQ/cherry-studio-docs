---
icon: cloud-arrow-up
---
# WebDAV Backup


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




Cherry Studio data backup supports WebDAV for backup. You can choose a suitable WebDAV service for cloud backup.

Based on WebDAV, you can achieve multi-device data synchronization through `Computer A` $$\xrightarrow{\text{Backup}}$$ `WebDAV` $$\xrightarrow{\text{Restore}}$$ `Computer B`.

#### Example with Jianguoyun (Nutstore)

1. Log in to Jianguoyun, click your username in the top right corner, and select "Account Info":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Select "Security Options" and click "Add Application":

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Enter the application name and generate a random password;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copy and record the password;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Get the server address, account, and password;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. In Cherry Studio Settings -> Data Settings, fill in the WebDAV information;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Choose to back up or restore data, and you can set the automatic backup time period.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV services with a lower barrier to entry are generally cloud drives:

- [Jianguoyun](https://www.jianguoyun.com/)
- [123pan](https://www.123pan.com/) (requires membership)
- [Aliyundrive](https://www.alipan.com/) (requires purchase)
- [Box](https://www.box.com/) (Free storage capacity is 10GB, single file size limit is 250MB.)
- [Dropbox](https://www.dropbox.com/) (Dropbox offers 2GB free, can expand by 16GB by inviting friends.)
- [TeraCloud](https://teracloud.jp/en/) (Free space is 10GB, an additional 5GB can be obtained through invitation.)
- [Yandex Disk](https://disk.yandex.com/) (Free users get 10GB capacity.)

Secondly, there are some services that require self-deployment:

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [sharelist](https://github.com/reruin/sharelist)
{% endhint %}