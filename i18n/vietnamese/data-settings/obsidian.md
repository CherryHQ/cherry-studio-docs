---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Hướng dẫn Cấu hình Obsidian

Cherry Studio hỗ trợ tích hợp với Obsidian, cho phép xuất toàn bộ cuộc trò chuyện hoặc từng tin nhắn riêng lẻ vào vault Obsidian.

{% hint style="warning" %}
Quy trình này không yêu cầu cài đặt plugin bổ sung cho Obsidian. Tuy nhiên, do cơ chế Cherry Studio nhập vào Obsidian tương tự như Obsidian Web Clipper, người dùng nên nâng cấp Obsidian lên phiên bản mới nhất (phiên bản Obsidian hiện tại nên từ **1.7.2** trở lên) để tránh [lỗi nhập liệu khi cuộc trò chuyện quá dài](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Hướng dẫn Mới Nhất

{% hint style="info" %}
So với phiên bản cũ khi xuất sang Obsidian, tính năng xuất sang Obsidian phiên bản mới có thể tự động chọn đường dẫn vault, không cần nhập thủ công tên vault hay tên thư mục.
{% endhint %}

### Bước 1: Cấu hình Cherry Studio

Mở Cherry Studio: vào _Cài đặt_ → _Cài đặt Dữ liệu_ → _Cấu hình Obsidian_, danh sách thả xuống sẽ tự động hiển thị tên các vault Obsidian đã mở trên thiết bị này. Chọn vault Obsidian mục tiêu của bạn:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Bước 2: Xuất Cuộc Trò Chuyện

#### Xuất toàn bộ cuộc trò chuyện

Quay lại giao diện trò chuyện của Cherry Studio, nhấp chuột phải vào cuộc trò chuyện, chọn _Xuất_ → _Xuất sang Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Một cửa sổ sẽ xuất hiện để cấu hình **Properties (thuộc tính)** của ghi chú khi xuất sang Obsidian, **vị trí thư mục** trong Obsidian và **phương thức xử lý**:

* **Vault (kho dữ liệu)**: Chọn vault Obsidian khác từ menu thả xuống
* **Path (đường dẫn)**: Chọn thư mục lưu trữ ghi chú từ menu thả xuống
* Các thuộc tính dành cho ghi chú Obsidian:
  * Tags (thẻ)
  * Created (thời gian tạo)
  * Source (nguồn)
* **Phương thức xử lý** gồm ba tùy chọn:
  * **Tạo mới (ghi đè nếu tồn tại)**: Tạo ghi chú mới trong thư mục đã chọn, ghi đè nếu đã tồn tại ghi chú cùng tên
  * **Chèn vào đầu**: Thêm nội dung trò chuyện vào phần đầu ghi chú nếu đã tồn tại
  * **Chèn vào cuối**: Thêm nội dung trò chuyện vào phần cuối ghi chú nếu đã tồn tại

{% hint style="info" %}
Chỉ phương pháp đầu tiên đi kèm Properties (thuộc tính), hai phương pháp sau không bao gồm Properties.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Cấu hình thuộc tính ghi chú</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Chọn đường dẫn</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Chọn phương thức xử lý</p></figcaption></figure>

Sau khi chọn tất cả tùy chọn, nhấn Xác nhận để xuất toàn bộ cuộc trò chuyện sang vault Obsidian tương ứng.

#### Xuất tin nhắn riêng lẻ

Nhấp vào _biểu tượng menu ba dấu gạch ngang_ bên dưới tin nhắn, chọn _Xuất_ → _Xuất sang Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Xuất tin nhắn riêng lẻ</p></figcaption></figure>

Cửa sổ cấu hình **thuộc tính ghi chú** và **phương thức xử lý** tương tự sẽ xuất hiện. Hoàn thành theo [hướng dẫn xuất toàn bộ cuộc trò chuyện ở trên](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Xuất thành công

🎉 Chúc mừng! Bạn đã hoàn thành toàn bộ cấu hình tích hợp Cherry Studio với Obsidian và hoàn tất quy trình xuất!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Xuất sang Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Kiểm tra kết quả xuất</p></figcaption></figure>

***

## Hướng dẫn Cũ (Áp dụng cho Cherry Studio <v1.1.13)

### Bước 1: Chuẩn bị Obsidian

Mở vault Obsidian, tạo một `thư mục` để lưu trữ cuộc trò chuyện đã xuất (ví dụ: thư mục Cherry Studio):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Ghi nhớ tên `vault` được đánh dấu ở góc dưới bên trái.

### Bước 2: Cấu hình Cherry Studio

Trong Cherry Studio: _Cài đặt_ → _Cài đặt Dữ liệu_ → _Cấu hình Obsidian_, nhập tên `vault` và tên `thư mục` đã chuẩn bị ở [Bước 1](obsidian.md#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

`Thẻ toàn cục` là tùy chọn, có thể đặt thẻ trong Obsidian cho mọi cuộc trò chuyện sau khi xuất.

### Bước 3: Xuất Cuộc Trò Chuyện

#### Xuất toàn bộ cuộc trò chuyện

Tại giao diện trò chuyện Cherry Studio, nhấp chuột phải vào cuộc trò chuyện, chọn _Xuất_ → _Xuất sang Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Xuất toàn bộ cuộc trò chuyện</p></figcaption></figure>

Cửa sổ sẽ xuất hiện để cấu hình **thuộc tính ghi chú** và chọn **phương thức xử lý**:

* **Tạo mới (ghi đè nếu tồn tại)**: Tạo ghi chú mới trong thư mục đã chọn
* **Chèn vào đầu**: Thêm nội dung vào đầu ghi chú hiện có
* **Chèn vào cuối**: Thêm nội dung vào cuối ghi chú hiện có

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Cấu hình thuộc tính ghi chú</p></figcaption></figure>

{% hint style="info" %}
Chỉ phương pháp đầu tiên đi kèm Properties (thuộc tính), hai phương pháp sau không bao gồm Properties.
{% endhint %}

#### Xuất tin nhắn riêng lẻ

Nhấp vào _biểu tượng menu ba dấu gạch ngang_ bên dưới tin nhắn, chọn _Xuất_ → _Xuất sang Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Xuất tin nhắn riêng lẻ</p></figcaption></figure>

Hoàn thành cấu hình theo [hướng dẫn xuất toàn bộ cuộc trò chuyện ở trên](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Xuất thành công

🎉 Chúc mừng! Bạn đã hoàn thành toàn bộ cấu hình tích hợp Cherry Studio với Obsidian và hoàn tất quy trình xuất!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Xuất sang Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Kiểm tra kết quả xuất</p></figcaption></figure>