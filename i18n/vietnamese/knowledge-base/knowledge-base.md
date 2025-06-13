---
icon: book-open-cover
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Hướng dẫn sử dụng Kho kiến thức

Trong phiên bản 0.9.1, CherryStudio đã mang đến tính năng Kho kiến thức được mong đợi từ lâu.

Dưới đây, chúng tôi sẽ trình bày hướng dẫn sử dụng chi tiết của CherryStudio theo từng bước.

## Thêm mô hình nhúng

1. Tìm kiếm mô hình trong dịch vụ quản lý mô hình, bạn có thể nhấp vào "Mô hình nhúng" để lọc nhanh;
2. Tìm mô hình bạn cần và thêm vào Mô hình của tôi.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Tạo Kho kiến thức

1. Truy cập kho kiến thức: Trên thanh công cụ bên trái của CherryStudio, nhấp vào biểu tượng Kho kiến thức để vào trang quản lý;
2. Thêm kho kiến thức: Nhấp vào Thêm để bắt đầu tạo kho kiến thức;
3. Đặt tên: Nhập tên cho kho kiến thức và thêm mô hình nhúng (ví dụ: bge-m3), sau đó hoàn tất việc tạo.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Thêm tệp và vector hóa

1. Thêm tệp: Nhấp vào nút Thêm tệp để mở trình chọn tệp;
2. Chọn tệp: Chọn định dạng tệp được hỗ trợ như pdf, docx, pptx, xlsx, txt, md, mdx... và mở;
3. Vector hóa: Hệ thống sẽ tự động xử lý vector hóa. Khi hiển thị hoàn tất (✓ màu xanh), nghĩa là vector hóa đã hoàn thành.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>



## Thêm dữ liệu từ nhiều nguồn

CherryStudio hỗ trợ nhiều cách thêm dữ liệu:

1. Thư mục: Có thể thêm toàn bộ thư mục, các tệp hỗ trợ trong thư mục sẽ tự động được vector hóa;
2. Liên kết trang web: Hỗ trợ URL như [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Sơ đồ trang web: Hỗ trợ sơ đồ trang web định dạng XML như [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Ghi chú văn bản thuần: Hỗ trợ nhập nội dung tùy chỉnh bằng văn bản thuần.

{% hint style="info" %}
Lưu ý:

1. Minh họa trong tài liệu nhập vào kho kiến thức hiện chưa hỗ trợ chuyển đổi thành vector, cần chuyển đổi thủ công thành văn bản;
2. Khi sử dụng URL làm nguồn kho kiến thức không phải lúc nào cũng thành công do một số trang web có cơ chế chống truy cập nghiêm ngặt (hoặc yêu cầu đăng nhập, ủy quyền). Sau khi tạo, nên kiểm tra bằng cách tìm kiếm thử.
3. Hầu hết trang web đều cung cấp sitemap, ví dụ như [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml) của CherryStudio. Thông thường có thể thêm `/sitemap.xml` vào địa chỉ gốc trang web (ví dụ: `aaa.com/sitemap.xml`).
4. Nếu trang web không cung cấp sitemap hoặc URL phức tạp, có thể tự tạo tệp sitemap XML. Tệp này cần sử dụng liên kết trực tiếp có thể truy cập công khai. Liên kết tệp cục bộ sẽ không được nhận diện.

> 1) Có thể nhờ AI tạo tệp sitemap hoặc viết công cụ tạo sitemap HTML;
> 2) Có thể sử dụng liên kết trực từ OSS hoặc dịch vụ lưu trữ đám mây để tạo liên kết trực tiếp. Nếu không có công cụ sẵn, hãy truy cập trang web chính thức [ocoolAI](https://one.ocoolai.com/login), đăng nhập và sử dụng công cụ tải lên tệp miễn phí trên thanh đầu trang để tạo liên kết trực tiếp.
{% endhint %}

## Tìm kiếm trong Kho kiến thức

Sau khi dữ liệu được vector hóa xong, có thể thực hiện truy vấn:

1. Nhấp vào nút Tìm kiếm kho kiến thức ở cuối trang;
2. Nhập nội dung cần truy vấn;
3. Kết quả tìm kiếm sẽ được hiển thị;
4. Điểm khớp của kết quả sẽ được hiển thị.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Trích dẫn kho kiến thức để tạo phản hồi trong hội thoại

1. Tạo chủ đề mới, trong thanh công cụ hội thoại, nhấp vào Kho kiến thức để hiển thị danh sách kho đã tạo, chọn kho kiến thức cần trích dẫn;
2. Nhập và gửi câu hỏi, mô hình sẽ trả về câu trả lời được tạo từ kết quả tìm kiếm;
3. Nguồn dữ liệu trích dẫn sẽ được đính kèm bên dưới câu trả lời, có thể xem nhanh tệp nguồn.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>