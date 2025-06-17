
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Cấu hình và Sử dụng MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Mở Cài đặt Cherry Studio.
2. Tìm tùy chọn `Máy chủ MCP`.
3. Nhấp vào `Thêm máy chủ`.
4. Điền các tham số liên quan đến MCP Server ([Tham khảo](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Các thông tin cần điền có thể bao gồm:
   * Tên: Tùy chỉnh tên, ví dụ `fetch-server`
   * Loại: Chọn `STDIO`
   * Lệnh: Điền `uvx`
   * Tham số: Điền `mcp-server-fetch`
   * (Có thể có tham số khác tùy thuộc vào máy chủ cụ thể)
5. Nhấp vào `Lưu`.

{% hint style="success" %}
Sau khi hoàn tất cấu hình trên, Cherry Studio sẽ tự động tải xuống MCP Server cần thiết - `fetch server`. Khi tải xong, chúng ta có thể bắt đầu sử dụng! Lưu ý: Nếu cấu hình mcp-server-fetch không thành công, hãy thử khởi động lại máy tính.
{% endhint %}

### Kích hoạt dịch vụ MCP trong hộp chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Khi đã thêm thành công máy chủ MCP trong phần `Máy chủ MCP`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Trình diễn hiệu ứng sử dụng**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Như thể hiện trong hình trên, sau khi tích hợp tính năng `fetch` của MCP, Cherry Studio có thể hiểu rõ hơn ý định truy vấn của người dùng, đồng thời thu thập thông tin liên quan từ mạng để đưa ra câu trả lời chính xác và toàn diện hơn.