---
icon: server
---

# 数据设置

该界面可以进行客户端数据的云端和本地备份、本地数据目录查询和清除缓存等操作。



### 数据备份

目前数据备份只支持 WebDAV 的方式进行备份。你可以选择支持 WebDAV 的服务来进行云端备份。

你也可以通过 `A电脑` $$\xrightarrow{\text{备份}}$$ `WebDAV` $$\xrightarrow{\text{恢复}}$$ `B电脑` 的方式来实现多端数据同步。

#### 以坚果云为例

1. 登录坚果云，点击右上角用户名，选择“账户信息”：

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. 选择“安全选项”，点击“添加应用”

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. 输入应用名称，生成随机密码；

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. 复制记录密码；

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. 获取服务器地址，账户和密码；

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. 在 Cherry Studio 设置——数据设置中，填写 WebDAV 信息；

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. 选择备份或者恢复数据，并可以设置自动备份的时间周期。

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV 服务门槛比较低的一般就是网盘：

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/)（需要会员）
* [阿里云盘](https://www.alipan.com/)（需要购买）
* [Box](https://www.box.com/) (免费空间容量为10GB，单个文件大小限制为250MB。)
* [Dropbox](https://www.dropbox.com/) （Dropbox免费2GB，可以邀请好友扩容16GB 。）
* [TeraCloud](https://teracloud.jp/en/) （免费空间为10GB，另外一个通过邀请可以获得5GB额外空间。）
* [Yandex Disk](https://disk.yandex.com/) (免费用户提供10GB容量。)

其次是一些需要自己部署服务：

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}







