---
icon: database
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 數據設置

該界面可以進行客戶端數據的雲端和本地備份、本地數據目錄查詢和清除快取等操作。

### 數據備份

目前數據備份只支援 WebDAV 的方式進行備份。你可以選擇支援 WebDAV 的服務來進行雲端備份。

你也可以通過 `A電腦` $$\xrightarrow{\text{備份}}$$ `WebDAV` $$\xrightarrow{\text{恢復}}$$ `B電腦` 的方式來實現多端數據同步。

#### 以堅果雲為例

1. 登入堅果雲，點選右上角使用者名稱，選擇「帳戶資訊」：

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. 選擇「安全選項」，點選「新增應用」

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. 輸入應用名稱，產生隨機密碼；

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. 複製記錄密碼；

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. 取得伺服器地址，帳戶和密碼；

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. 在 Cherry Studio 設定——數據設定中，填寫 WebDAV 資訊；

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. 選擇備份或者恢復數據，並可以設定自動備份的時間週期。

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV 服務門檻比較低的一般就是網盤：

* [堅果雲](https://www.jianguoyun.com/)
* [123盤](https://www.123pan.com/)（需要會員）
* [阿里雲盤](https://www.alipan.com/)（需要購買）
* [Box](https://www.box.com/) (免費空間容量為10GB，單個檔案大小限制為250MB。)
* [Dropbox](https://www.dropbox.com/) （Dropbox免費2GB，可以邀請好友擴容16GB 。）
* [TeraCloud](https://teracloud.jp/en/) （免費空間為10GB，另外通過邀請可以獲得5GB額外空間。）
* [Yandex Disk](https://disk.yandex.com/) (免費使用者提供10GB容量。)

其次是一些需要自己部署服務：

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}