---
icon: database
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Thiết lập Dữ liệu

Giao diện này cho phép sao lưu dữ liệu máy khách lên đám mây và cục bộ, kiểm tra thư mục dữ liệu cục bộ và xóa bộ nhớ đệm.

### Sao lưu Dữ liệu

Hiện tại, sao lưu dữ liệu chỉ hỗ trợ phương thức WebDAV. Bạn có thể chọn các dịch vụ hỗ trợ WebDAV để sao lưu lên đám mây.

Bạn cũng có thể đồng bộ dữ liệu đa thiết bị thông qua phương thức:  
`Máy tính A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restore}}$$ `Máy tính B`.

#### Ví dụ với Nutstore (坚果云)

1. Đăng nhập Nutstore, nhấp vào tên người dùng ở góc trên bên phải và chọn "账户信息" (Thông tin tài khoản):
<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Chọn "安全选项" (Tùy chọn bảo mật), nhấp "添加应用" (Thêm ứng dụng):
<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Nhập tên ứng dụng và tạo mật khẩu ngẫu nhiên:
<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Sao chép và lưu mật khẩu:
<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Lấy địa chỉ máy chủ, tài khoản và mật khẩu:
<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Trong Cherry Studio: Cài đặt → Thiết lập Dữ liệu, nhập thông tin WebDAV:
<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Chọn Sao lưu hoặc Khôi phục dữ liệu, có thể đặt chu kỳ sao lưu tự động:
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Các dịch vụ WebDAV có yêu cầu thấp thường là dịch vụ lưu trữ đám mây:
* [Nutstore](https://www.jianguoyun.com/) 
* [123 Cloud](https://www.123pan.com/) (cần thành viên)
* [Aliyun Drive](https://www.alipan.com/) (cần mua)
* [Box](https://www.box.com/) (miễn phí 10GB, giới hạn tệp 250MB)
* [Dropbox](https://www.dropbox.com/) (miễn phí 2GB, tăng tối đa 16GB khi mời bạn bè)
* [TeraCloud](https://teracloud.jp/en/) (miễn phí 10GB, tăng thêm 5GB qua mời)
* [Yandex Disk](https://disk.yandex.com/) (miễn phí 10GB)

Dịch vụ yêu cầu tự triển khai:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}