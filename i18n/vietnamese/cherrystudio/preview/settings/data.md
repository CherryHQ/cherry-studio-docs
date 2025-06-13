---
icon: database
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Cài đặt Dữ liệu

Giao diện này cho phép thực hiện các thao tác như sao lưu dữ liệu máy khách lên đám mây và sao lưu cục bộ, truy vấn thư mục dữ liệu cục bộ và xóa bộ nhớ đệm.

### Sao lưu Dữ liệu

Hiện tại, sao lưu dữ liệu chỉ hỗ trợ phương thức WebDAV. Bạn có thể chọn các dịch vụ hỗ trợ WebDAV để sao lưu lên đám mây.

Bạn cũng có thể đồng bộ dữ liệu đa thiết bị thông qua phương thức: `Máy tính A` $$\xrightarrow{\text{Sao lưu}}$$ `WebDAV` $$\xrightarrow{\text{Phục hồi}}$$ `Máy tính B`.

#### Lấy Nutstore làm ví dụ

1. Đăng nhập Nutstore, nhấp vào tên người dùng ở góc trên bên phải, chọn "Thông tin tài khoản":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Chọn "Tùy chọn bảo mật", nhấp vào "Thêm ứng dụng"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Nhập tên ứng dụng, tạo mật khẩu ngẫu nhiên;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Sao chép và ghi lại mật khẩu;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Lấy địa chỉ máy chủ, tài khoản và mật khẩu;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Trong Cài đặt Cherry Studio → Cài đặt Dữ liệu, điền thông tin WebDAV;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Chọn sao lưu hoặc phục hồi dữ liệu, và có thể đặt chu kỳ thời gian sao lưu tự động.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Các dịch vụ WebDAV có ngưỡng thấp thường là các dịch vụ lưu trữ đám mây:

* [Nutstore](https://www.jianguoyun.com/) (cần thành viên)
* [123Pan](https://www.123pan.com/) (cần thành viên)
* [Alibaba Cloud Disk](https://www.alipan.com/) (cần mua)
* [Box](https://www.box.com/) (Dung lượng miễn phí 10GB, giới hạn kích thước tập tin đơn lẻ 250MB.)
* [Dropbox](https://www.dropbox.com/) (Dropbox miễn phí 2GB, có thể mời bạn bè để mở rộng lên 16GB.)
* [TeraCloud](https://teracloud.jp/en/) (Dung lượng miễn phí 10GB, ngoài ra thông qua lời mời có thể nhận thêm 5GB.)
* [Yandex Disk](https://disk.yandex.com/) (Người dùng miễn phí được cung cấp 10GB.)

Tiếp theo là một số dịch vụ cần tự triển khai:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}