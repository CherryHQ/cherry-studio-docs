---
icon: cloud-arrow-up
---
# WebDAV 備份


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




Cherry Studio 資料備份支援透過 WebDAV 的方式進行備份。你可以選擇合適的 WebDAV 服務來進行雲端備份。

基於 WebDAV 可以通過 `A電腦` $$\xrightarrow{\text{備份}}$$ `WebDAV` $$\xrightarrow{\text{恢復}}$$ `B電腦` 的方式來實現多端資料同步。

#### 以堅果雲為例

1.  登入堅果雲，點擊右上角使用者名稱，選擇「帳戶資訊」：

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2.  選擇「安全選項」，點擊「新增應用」

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3.  輸入應用名稱，生成隨機密碼；

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4.  複製記錄密碼；

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5.  取得伺服器地址、帳戶和密碼；

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6.  在 Cherry Studio 設定——資料設定中，填寫 WebDAV 資訊；

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7.  選擇備份或者恢復資料，並可以設定自動備份的時間週期。

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV 服務門檻較低的通常是網盤：

- [堅果雲](https://www.jianguoyun.com/)
- [123 盤](https://www.123pan.com/)（需要會員）
- [阿里雲盤](https://www.alipan.com/)（需要購買）
- [Box](https://www.box.com/) (免費空間容量為 10GB，單個檔案大小限制為 250MB。)
- [Dropbox](https://www.dropbox.com/) （Dropbox 免費 2GB，可以邀請好友擴容 16GB 。）
- [TeraCloud](https://teracloud.jp/en/) （免費空間為 10GB，透過邀請可獲得 5GB 額外空間。）
- [Yandex Disk](https://disk.yandex.com/) (免費使用者提供 10GB 容量。)

其次是需自行部署的服務：

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [sharelist](https://github.com/reruin/sharelist)
  {% endhint %}