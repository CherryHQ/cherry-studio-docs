
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Ollama

Ollama là một công cụ nguồn mở xuất sắc cho phép bạn dễ dàng chạy và quản lý nhiều mô hình ngôn ngữ lớn (LLMs) trên thiết bị cục bộ. Cherry Studio hiện đã hỗ trợ tích hợp Ollama, giúp bạn tương tác trực tiếp với LLM triển khai cục bộ trong giao diện quen thuộc mà không cần phụ thuộc vào dịch vụ đám mây!

## Ollama là gì?

Ollama là công cụ đơn giản hóa việc triển khai và sử dụng mô hình ngôn ngữ lớn (LLM) với các đặc điểm:

* **Chạy cục bộ:** Mô hình hoàn toàn chạy trên máy tính cục bộ của bạn, không cần kết nối mạng, bảo vệ quyền riêng tư và an ninh dữ liệu.
* **Dễ sử dụng:** Chỉ cần các lệnh đơn giản để tải xuống, chạy và quản lý nhiều LLM.
* **Đa dạng mô hình:** Hỗ trợ nhiều mô hình nguồn mở phổ biến như Llama 2, Deepseek, Mistral, Gemma.
* **Đa nền tảng:** Tương thích với macOS, Windows và Linux.
* **API mở:** Hỗ trợ giao diện tương thích OpenAI để tích hợp với các công cụ khác.

## Tại sao nên dùng Ollama trong Cherry Studio?

* **Không cần dịch vụ đám mây:** Thoát khỏi hạn ngạch và chi phí API đám mây, trải nghiệm sức mạnh LLM cục bộ.
* **Bảo mật dữ liệu:** Mọi dữ liệu hội thoại được lưu trữ cục bộ, không lo rò rỉ thông tin.
* **Dùng ngoại tuyến:** Tương tác với LLM ngay cả khi không có kết nối internet.
* **Tùy chỉnh:** Chọn và định cấu hình LLM phù hợp nhất với nhu cầu của bạn.

## Cấu hình Ollama trong Cherry Studio

### **1. Cài đặt và chạy Ollama**

Trước tiên, bạn cần cài đặt và chạy Ollama trên máy tính:

* **Tải Ollama:** Truy cập trang web Ollama ([https://ollama.com/](https://ollama.com/)), tải gói cài đặt cho hệ điều hành của bạn.\
    Trên Linux, chạy lệnh:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Cài đặt Ollama:** Hoàn thành cài đặt theo hướng dẫn.
* **Tải mô hình:** Mở terminal (hoặc Command Prompt), dùng lệnh `ollama run` để tải mô hình mong muốn. Ví dụ tải mô hình Llama 2:

    ```sh
    ollama run llama3.2
    ```

    Ollama sẽ tự động tải và chạy mô hình.
* **Giữ Ollama hoạt động:** Đảm bảo Ollama luôn chạy khi sử dụng Cherry Studio.

### **2. Thêm nhà cung cấp Ollama trong Cherry Studio**

Thêm Ollama làm nhà cung cấp AI tùy chỉnh:

* **Mở Cài đặt:** Trên thanh điều hướng bên trái Cherry Studio, nhấp "Settings" (biểu tượng bánh răng).
* **Vào Dịch vụ mô hình:** Chọn tab "Model Services".
* **Thêm nhà cung cấp:** Nhấp vào Ollama trong danh sách.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Cấu hình nhà cung cấp Ollama**

Tìm Ollama trong danh sách và cấu hình chi tiết:

1. **Trạng thái kích hoạt:**
   * Đảm bảo công tắc bên phải được bật.
2. **Khóa API:**
   * Ollama mặc định **không cần** khóa API. Có thể để trống hoặc nhập bất kỳ giá trị nào.
3. **Địa chỉ API:**
   *    Nhập địa chỉ API cục bộ của Ollama. Thông thường:

       ```
       http://localhost:11434/
       ```

       Thay đổi nếu bạn chỉnh cổng.
4. **Thời gian duy trì:** Thiết lập thời gian chờ (đơn vị: phút). Cherry Studio sẽ tự động ngắt kết nối nếu không có hội thoại mới.
5. **Quản lý mô hình:**
   * Nhấp "+ Thêm" để nhập tên mô hình đã tải trong Ollama.
   * Ví dụ: nếu đã dùng `ollama run llama3.2`, nhập `llama3.2` tại đây.
   * Nhấp "Quản lý" để chỉnh sửa hoặc xóa mô hình.

## Bắt đầu sử dụng

Sau khi cấu hình, hãy chọn nhà cung cấp Ollama và mô hình đã tải trong giao diện trò chuyện để bắt đầu hội thoại với LLM cục bộ!

## Mẹo và gợi ý

* **Lần đầu chạy mô hình:** Ollama cần tải xuống tệp mô hình, có thể mất nhiều thời gian.
* **Xem mô hình khả dụng:** Chạy lệnh `ollama list` trong terminal để xem mô hình đã tải.
* **Yêu cầu phần cứng:** LLM cần tài nguyên máy tính đáng kể (CPU, RAM, GPU), hãy đảm bảo cấu hình phù hợp.
* **Tài liệu Ollama:** Nhấp liên kết `Xem tài liệu và mô hình Ollama` trong trang cấu hình để truy cập nhanh trang web chính thức.