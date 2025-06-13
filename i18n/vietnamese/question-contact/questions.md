---
icon: seal-question
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Các Câu Hỏi Thường Gặp

## Mã Lỗi Thường Gặp

* **4xx (Mã trạng thái lỗi máy khách)**: Thường là lỗi cú pháp yêu cầu, xác thực không thành công hoặc không thể hoàn tất yêu cầu.
* **5xx (Mã trạng thái lỗi máy chủ)**: Thường là lỗi phía máy chủ, máy chủ ngừng hoạt động, yêu cầu xử lý quá thời gian.

| Mã lỗi        | Tình huống có thể xảy ra                                        | Giải pháp                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4> | Định dạng phần thân yêu cầu không đúng                           | <p>Kiểm tra nội dung lỗi từ hội thoại hoặc xem nội dung báo lỗi tại <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">Bảng điều khiển</a>, thực hiện theo hướng dẫn.</p><p><mark style="color:purple;">【Trường hợp 1】</mark>: Nếu là mô hình Gemini, có thể cần liên kết thẻ thanh toán;<br><mark style="color:purple;">【Trường hợp 2】</mark>: Dữ liệu vượt giới hạn, thường gặp ở mô hình thị giác khi ảnh vượt giới hạn;<br><mark style="color:purple;">【Trường hợp 3】</mark>: Tham số không hỗ trợ hoặc sai. Thử tạo trợ lý mới;<br><mark style="color:purple;">【Trường hợp 4】</mark>: Ngữ cảnh vượt giới hạn, xóa ngữ cảnh hoặc giảm số lượng.</p> |
| <h4>401</h4> | Xác thực không thành công: Mô hình không hỗ trợ hoặc tài khoản bị khoá | Kiểm tra trạng thái tài khoản với nhà cung cấp                                                                                                                                                                                                                                                                                                                                                                                       |
| <h4>403</h4> | Không có quyền thực hiện thao tác                                | Thực hiện theo thông báo lỗi từ hội thoại hoặc [Bảng điều khiển](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                                    |
| <h4>404</h4> | Không tìm thấy tài nguyên yêu cầu                                | Kiểm tra đường dẫn yêu cầu                                                                                                                                                                                                                                                                                                                                                                                                         |
| <h4>422</h4> | Đúng định dạng nhưng sai ngữ nghĩa                              | Lỗi khi máy chủ hiểu nhưng không xử lý được. Thường do lỗi ngữ nghĩa JSON (vd: giá trị null; yêu cầu chuỗi nhưng nhập số/boolean)                                                                                                                                                                                                                                                                                                   |
| <h4>429</h4> | Vượt giới hạn tốc độ yêu cầu                                     | Tạm dừng sử dụng một thời gian                                                                                                                                                                                                                                                                                                                                                                                                     |
| <h4>500</h4> | Lỗi nội bộ máy chủ                                               | Liên hệ nhà cung cấp nếu lỗi tiếp diễn                                                                                                                                                                                                                                                                                                                                                                                             |
| <h4>501</h4> | Máy chủ không hỗ trợ tính năng yêu cầu                           |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>502</h4> | Máy chủ cổng/gateway nhận phản hồi không hợp lệ                   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>503</h4> | Máy chủ quá tải/bảo trì tạm thời                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>504</h4> | Gateway/proxy không nhận phản hồi kịp thời                       |                                                                                                                                                                                                                                                                                                                                                                                                                                    |



***

## Cách kiểm tra lỗi trong bảng điều khiển

* Nhấn <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> khi cửa sổ Cherry Studio đang hoạt động (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- Cửa sổ Cherry Studio phải là cửa sổ đang hoạt động
- Cần mở bảng điều khiển trước khi thực hiện yêu cầu kiểm tra/hội thoại
{% endhint %}

* Trong bảng điều khiển, chọn <mark style="color:blue;">`Network`</mark> → Tìm mục có dấu <mark style="color:red;">`×`</mark>  màu đỏ: <mark style="color:red;">`completions`</mark> (lỗi hội thoại/dịch thuật) hoặc <mark style="color:red;">`generations`</mark> (lỗi vẽ) → Chọn <mark style="color:blue;">`Response`</mark> để xem nội dung phản hồi (vùng ④ trong ảnh).

> Nếu không xác định được nguyên nhân, vui lòng chụp màn hình và gửi tới [Nhóm thảo luận chính thức](https://t.me/CherryStudioAI)

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Phương pháp này áp dụng cho: kiểm tra mô hình, thêm kho kiến thức, vẽ,... Luôn mở bảng điều khiển trước khi thực hiện thao tác.

{% hint style="info" %}
Tên mục (vùng ②) thay đổi theo ngữ cảnh:

Hội thoại/dịch/kiểm tra: <mark style="color:red;">`completions`</mark>&#x20;

Vẽ: <mark style="color:red;">`generations`</mark>

Tạo kho kiến thức: <mark style="color:red;">`embeddings`</mark>&#x20;
{% endhint %}

***

## Công thức không hiển thị/hiển thị sai

* Khi công thức hiện mã nguồn: Kiểm tra định dạng giới hạn

> **Định dạng giới hạn**
>
> _Công thức nội dòng_
>
> * Dùng ký hiệu `$`: `$công_thức$`
> * Hoặc `\(` và `\)`: `\(công_thức\)`
>
> _Khối công thức độc lập_
>
> * Dùng `$$công_thức$$`
> * Hoặc `\[công_thức\]`
> * Ví dụ: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Lỗi hiển thị (đặc biệt với nội dung tiếng Trung): Thử đổi công cụ kết xuất sang KateX

***

## Không tạo được kho kiến thức/Lỗi lấy chiều nhúng

1. Mô hình không khả dụng

> Kiểm tra nhà cung cấp có hỗ trợ mô hình hay không

2. Dùng mô hình không hỗ trợ nhúng

***

## Mô hình không nhận diện ảnh/Không tải/chọn được ảnh

Kiểm tra biểu tượng 👁️ cạnh tên mô hình - biểu thị hỗ trợ nhận diện ảnh.

Để bật chức năng hình ảnh: Vào danh sách mô hình của nhà cung cấp → Chọn mô hình → Bật tùy chọn hình ảnh trong cài đặt.

Lưu ý: Mô hình không hỗ trợ thị giác sẽ không thể nhận diện ảnh dù đã bật tính năng.