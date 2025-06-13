---
icon: cloud-check
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Cài đặt nhà cung cấp

Trang hiện tại chỉ giới thiệu các tính năng giao diện, hướng dẫn cấu hình có thể tham khảo trong bài hướng dẫn [Cài đặt nhà cung cấp](../../../pre-basic/providers/) của phần cơ bản.

{% hint style="info" %}
* Khi sử dụng nhà cung cấp tích hợp sẵn, chỉ cần nhập khóa tương ứng.
* Các nhà cung cấp khác nhau có thể gọi khóa bằng các tên khác nhau như: Secret Key, Key, API Key, Token,... đều chỉ cùng một thứ.
{% endhint %}

### Khóa API

Trong Cherry Studio, một nhà cung cấp duy nhất hỗ trợ sử dụng nhiều Key theo phương thức luân phiên tuần tự từ trước ra sau.

* Thêm nhiều Key bằng cách phân tách bằng dấu phẩy tiếng Anh. Ví dụ:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Phải sử dụng dấu phẩy **tiếng Anh**.
{% endhint %}

### Địa chỉ API

Khi sử dụng nhà cung cấp tích hợp sẵn, thường không cần điền địa chỉ API. Nếu cần sửa đổi, vui lòng nhập chính xác địa chỉ theo tài liệu chính thức.

> Nếu nhà cung cấp cung cấp địa chỉ dạng <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, chỉ cần nhập phần địa chỉ gốc (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio sẽ tự động nối phần đường dẫn còn lại (<mark style="background-color:green;">/v1/chat/completions</mark>), nhập sai có thể dẫn đến không sử dụng được.

{% hint style="info" %}
Lưu ý: Đa số nhà cung cấp có đường dẫn mô hình ngôn ngữ lớn thống nhất, thường không cần thao tác sau. Nếu đường dẫn API của nhà cung cấp là v2, v3/chat/completions hoặc phiên bản khác, có thể nhập thủ công phiên bản tương ứng vào trường địa chỉ kết thúc bằng "`/`"; Khi đường dẫn yêu cầu của nhà cung cấp không phải dạng thông thường <mark style="background-color:green;">/v1/chat/completions</mark>, sử dụng toàn bộ địa chỉ do nhà cung cấp cung cấp và kết thúc bằng `#`.

Cụ thể:
* Khi địa chỉ API kết thúc bằng `/` sẽ chỉ nối "<mark style="background-color:green;">chat/completions</mark>"
* Khi địa chỉ API kết thúc bằng `#` sẽ không thực hiện nối, chỉ sử dụng địa chỉ đã nhập.

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Thêm mô hình

Thông thường, nhấp vào nút `Quản lý` ở góc dưới cùng bên trái trang cấu hình nhà cung cấp sẽ tự động lấy tất cả mô hình hỗ trợ của nhà cung cấp đó. Từ danh sách lấy được, nhấp vào `+` để thêm vào danh sách mô hình.

{% hint style="info" %}
Khi nhấp nút Quản lý, các mô hình trong danh sách popup sẽ không được thêm toàn bộ, cần nhấp `+` bên phải mô hình để thêm vào danh sách mô hình trang cấu hình nhà cung cấp thì mới xuất hiện trong danh sách chọn mô hình.
{% endhint %}

### Kiểm tra kết nối

Nhấp vào nút kiểm tra sau trường nhập Khóa API để kiểm tra xem cấu hình đã thành công hay chưa.

{% hint style="info" %}
Khi kiểm tra mô hình, mặc định sử dụng mô hình đối thoại cuối cùng trong danh sách đã thêm. Nếu kiểm tra thất bại, vui lòng kiểm tra xem danh sách mô hình có mô hình sai hoặc không được hỗ trợ không.
{% endhint %}

{% hint style="danger" %}
Sau khi cấu hình thành công, **bắt buộc** phải bật công tắc ở góc trên bên phải, nếu không nhà cung cấp này vẫn ở trạng thái chưa kích hoạt và không thể tìm thấy mô hình tương ứng trong danh sách mô hình.
{% endhint %}