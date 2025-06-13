---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Chế độ Trực tuyến

{% hint style="info" %}
Ví dụ về các tình huống cần kết nối mạng:

* Thông tin có tính thời sự: ví dụ giá hợp đồng tương lai vàng hôm nay/tuần này/vừa qua.
* Dữ liệu thời gian thực: như thời tiết, tỷ giá hối đoái và các giá trị động khác...
* Kiến thức mới nổi: như sự vật, khái niệm, công nghệ mới...
{% endhint %}

### 1. Cách bật chế độ trực tuyến

Trong cửa sổ đặt câu hỏi của Cherry Studio, nhấp vào biểu tượng 【🌐】 để bật chế độ trực tuyến.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Nhấp vào biểu tượng trái đất - Bật kết nối</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Biểu thị - Đã bật tính năng kết nối mạng</p></figcaption></figure>

### 2. Lưu ý đặc biệt: Có hai chế độ kết nối mạng

#### Chế độ 1: Mô hình lớn của nhà cung cấp dịch vụ có sẵn tính năng kết nối mạng

Trong trường hợp này, sau khi bật kết nối, bạn có thể sử dụng dịch vụ trực tuyến ngay mà rất đơn giản.

{% hint style="warning" %}
Có thể xác định nhanh mô hình nào hỗ trợ kết nối bằng cách kiểm tra xem sau tên mô hình trên giao diện hỏi-đáp có biểu tượng bản đồ nhỏ không.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Trên trang quản lý mô hình, phương pháp này cũng giúp bạn nhanh chóng phân biệt mô hình nào hỗ trợ kết nối và mô hình nào không.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Hiện tại Cherry Studio đã hỗ trợ các nhà cung cấp dịch vụ mô hình trực tuyến sau:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (tất cả mô hình hỗ trợ kết nối)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian</mark>

{% hint style="danger" %}
Lưu ý đặc biệt:

Có một tình huống đặc biệt khi mô hình không có ký hiệu trái đất nhỏ nhưng vẫn có thể kết nối mạng, như giải thích trong hướng dẫn dưới đây.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Chế độ 2: Mô hình không có tính năng kết nối, sử dụng dịch vụ Tavily để kết nối

Khi sử dụng mô hình lớn không có tính năng kết nối (không có biểu tượng trái đất nhỏ sau tên) nhưng cần xử lý thông tin thời gian thực, chúng ta cần sử dụng dịch vụ tìm kiếm mạng Tavily.

**Lần đầu sử dụng dịch vụ Tavily**, một cửa sổ bật lên sẽ hướng dẫn thiết lập, vui lòng làm theo hướng dẫn - rất đơn giản!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Cửa sổ bật lên, nhấp: Đi tới thiết lập</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Nhấp để lấy khoá bí mật</p></figcaption></figure>

Sau khi nhấp lấy khoá, hệ thống sẽ tự động chuyển hướng đến trang **đăng nhập/đăng ký tavily**. Đăng ký và đăng nhập, tạo APIkey rồi sao chép vào Cherry Studio.

{% hint style="danger" %}
Nếu không biết đăng ký, tham khảo hướng dẫn đăng nhập/đăng ký tavily cùng thư mục với tài liệu này.
{% endhint %}

**Tài liệu tham khảo đăng ký tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Giao diện dưới đây cho thấy đăng ký thành công.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Sao chép key</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Dán key, hoàn tất</p></figcaption></figure>

Thử lại lần nữa để xem kết quả. Kết quả cho thấy đã kết nối và tìm kiếm bình thường, số lượng kết quả tìm kiếm mặc định là 5.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Lưu ý: tavily có giới hạn miễn phí hàng tháng, vượt quá sẽ phải trả phí~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Nếu phát hiện lỗi, rất mong mọi người liên hệ bất cứ lúc nào.