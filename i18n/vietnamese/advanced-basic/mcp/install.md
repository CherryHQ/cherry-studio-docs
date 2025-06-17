
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Cài đặt môi trường MCP

**MCP (Model Context Protocol)** là một giao thức mã nguồn mở nhằm cung cấp thông tin ngữ cảnh cho các mô hình ngôn ngữ lớn (LLM) theo cách tiêu chuẩn hóa. Xem thêm về MCP tại [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Sử dụng MCP trong Cherry Studio

Dưới đây minh họa cách sử dụng MCP trong Cherry Studio với tính năng `fetch` làm ví dụ. Xem chi tiết tại [tài liệu](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Chuẩn bị: Cài đặt uv và bun**

{% hint style="warning" %}
Hiện tại Cherry Studio chỉ sử dụng [uv](https://github.com/astral-sh/uv) và [bun](https://github.com/oven-sh/bun) tích hợp sẵn, **không tái sử dụng** uv và bun đã cài đặt trong hệ thống.
{% endhint %}

Trong `Cài đặt - Máy chủ MCP`, nhấn nút `Cài đặt` để tự động tải xuống và cài đặt. Vì tải trực tiếp từ GitHub nên tốc độ có thể chậm và dễ gặp lỗi. Kiểm tra cài đặt thành công bằng cách xem trong thư mục được đề cập dưới đây có tệp hay không.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Thư mục cài đặt chương trình thực thi:**

Windows: `C:\Users\Tên người dùng\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Thư mục bin</p></figcaption></figure>

**Khi không cài đặt được bình thường:**

Có thể tạo liên kết mềm từ các lệnh tương ứng trong hệ thống đến đây. Nếu không có thư mục tương ứng, cần tạo thủ công. Hoặc tải xuống thủ công tệp thực thi vào thư mục này:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)