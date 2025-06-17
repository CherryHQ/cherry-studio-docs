
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Huawei Cloud

一、Truy cập [Huawei Cloud](https://auth.huaweicloud.com/authui/login) để tạo tài khoản và đăng nhập

二、Nhấp vào [liên kết này](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) để vào bảng điều khiển MaaS

三、Ủy quyền

<details>

<summary>Các bước ủy quyền (bỏ qua nếu đã ủy quyền)</summary>

1. Sau khi vào trang liên kết ở bước (二), theo hướng dẫn vào trang ủy quyền (Nhấp IAM Sub-user → Thêm ủy quyền → Người dùng thông thường)

![](<../../.gitbook/assets/image (49).png>)

2. Sau khi tạo, quay lại trang liên kết ở bước (二)
3. Hệ thống sẽ báo thiếu quyền truy cập, nhấp vào "bấm vào đây" trong thông báo
4. Thêm ủy quyền hiện có và xác nhận

![](<../../.gitbook/assets/image (50).png>)

Lưu ý: Phương pháp này phù hợp với người mới, không cần xem nhiều nội dung, chỉ cần làm theo hướng dẫn. Nếu bạn có thể ủy quyền thành công ngay lần đầu thì cứ làm theo cách của bạn.

</details>

四、Nhấp vào Quản lý xác thực ở thanh bên, tạo API Key (khóa bí mật) và sao chép

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Sau đó tạo nhà cung cấp mới trong CherryStudio

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Sau khi tạo xong, nhập khóa bí mật vào



五、Nhấp vào Triển khai mô hình ở thanh bên, nhận tất cả

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

六、Nhấp vào Gọi

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Sao chép địa chỉ ở vị trí ①, dán vào địa chỉ nhà cung cấp của CherryStudio và thêm ký tự "#" ở cuối

và thêm ký tự "#" ở cuối

và thêm ký tự "#" ở cuối

và thêm ký tự "#" ở cuối

và thêm ký tự "#" ở cuối

Tại sao thêm "#"? [Xem tại đây](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Tất nhiên bạn có thể không xem mà làm theo hướng dẫn là được;
>
> Hoặc có thể điền bằng cách xóa phần v1/chat/completions, miễn là bạn biết cách điền thì làm thế nào cũng được, nếu không biết thì nhất định phải làm theo hướng dẫn.



<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Sau đó sao chép tên mô hình ở vị trí ②, trong CherryStudio nhấp nút "+ Thêm" để tạo mô hình mới

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Nhập tên mô hình, không thêm thừa, không thêm dấu ngoặc kép, viết y như trong ví dụ.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Nhấp nút Thêm mô hình để hoàn tất.

{% hint style="info" %}
Trong Huawei Cloud, do địa chỉ của mỗi mô hình khác nhau nên mỗi mô hình cần tạo một nhà cung cấp mới, chỉ cần lặp lại các bước trên.
{% endhint %}