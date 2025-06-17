
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Nhà Cung Cấp Dịch Vụ Tùy Chỉnh

Cherry Studio không chỉ tích hợp các dịch vụ mô hình AI hàng đầu mà còn trao cho bạn khả năng tùy biến mạnh mẽ. Thông qua tính năng **Nhà cung cấp dịch vụ AI tùy chỉnh**, bạn có thể dễ dàng kết nối bất kỳ mô hình AI nào bạn cần.

## Tại sao cần nhà cung cấp dịch vụ AI tùy chỉnh?

* **Linh hoạt:** Không bị giới hạn bởi danh sách nhà cung cấp có sẵn, tự do lựa chọn mô hình AI phù hợp nhất với nhu cầu của bạn.
* **Đa dạng:** Khám phá các mô hình AI từ nhiều nền tảng khác nhau để tận dụng ưu điểm riêng của chúng.
* **Kiểm soát:** Trực tiếp quản lý khóa API và địa chỉ truy cập, đảm bảo an toàn và quyền riêng tư.
* **Tùy chỉnh:** Kết nối các mô hình triển khai riêng tư để đáp ứng nhu cầu cụ thể của các kịch bản kinh doanh.

## Làm thế nào để thêm nhà cung cấp dịch vụ AI tùy chỉnh?

Chỉ với vài bước đơn giản, bạn có thể thêm nhà cung cấp AI tùy chỉnh vào Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Mở cài đặt:** Trên thanh điều hướng bên trái giao diện Cherry Studio, nhấp vào "Cài đặt" (biểu tượng bánh răng).
2. **Vào dịch vụ mô hình:** Trong trang cài đặt, chọn tab "Dịch vụ mô hình".
3. **Thêm nhà cung cấp:** Tại trang "Dịch vụ mô hình", nhấp nút "+ Thêm" ở cuối danh sách để mở cửa sổ "Thêm nhà cung cấp".
4. **Điền thông tin:** Trong cửa sổ này, cung cấp các thông tin sau:
   * **Tên nhà cung cấp:** Đặt tên dễ nhận biết cho nhà cung cấp của bạn (ví dụ: MyCustomOpenAI).
   * **Loại nhà cung cấp:** Chọn loại từ danh sách thả xuống. Hiện hỗ trợ:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Lưu cấu hình:** Nhấp nút "Thêm" để lưu cấu hình sau khi hoàn thành.

## Cấu hình nhà cung cấp dịch vụ AI tùy chỉnh

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Sau khi thêm, tìm nhà cung cấp mới trong danh sách và cấu hình chi tiết:

1. **Trạng thái kích hoạt** Công tắc bật/tắt ở bên phải danh sách - bật để kích hoạt dịch vụ tùy chỉnh.
2. **Khóa API:**
   * Nhập khóa API (API Key) do nhà cung cấp AI của bạn cấp.
   * Nhấp nút "Kiểm tra" bên phải để xác minh khóa.
3. **Địa chỉ API:**
   * Nhập địa chỉ truy cập API (Base URL) của dịch vụ AI.
   * Tham khảo tài liệu chính thức của nhà cung cấp để lấy địa chỉ chính xác.
4.  **Quản lý mô hình:**

    * Nhấp "+ Thêm" để tự thêm ID mô hình bạn muốn sử dụng, ví dụ `gpt-3.5-turbo`, `gemini-pro`.

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * Tham khảo tài liệu chính thức nếu không rõ tên mô hình cụ thể.
    * Nhấp "Quản lý" để chỉnh sửa hoặc xóa các mô hình đã thêm.

## Bắt đầu sử dụng

Sau khi hoàn thành cấu hình, tại giao diện trò chuyện của Cherry Studio, chọn nhà cung cấp AI tùy chỉnh và mô hình của bạn để bắt đầu tương tác với AI!

## Sử dụng vLLM làm nhà cung cấp dịch vụ AI tùy chỉnh

vLLM là thư viện suy luận LLM nhanh và dễ sử dụng tương tự Ollama. Các bước tích hợp vLLM vào Cherry Studio:

1.  **Cài đặt vLLM:** Làm theo hướng dẫn chính thức ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # Nếu dùng pip
    uv pip install vllm # Nếu dùng uv
    ```
2.  **Khởi động dịch vụ vLLM:** Sử dụng giao diện tương thích OpenAI của vLLM. Hai cách chính:

    * Dùng `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Dùng `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Đảm bảo dịch vụ chạy thành công và lắng nghe ở cổng mặc định `8000`. Bạn có thể chỉ định cổng khác bằng tham số `--port`.

3. **Thêm nhà cung cấp vLLM vào Cherry Studio:**
   * Làm theo các bước trước để thêm nhà cung cấp AI tùy chỉnh mới.
   * **Tên nhà cung cấp:** `vLLM`
   * **Loại nhà cung cấp:** Chọn `OpenAI`.
4. **Cấu hình nhà cung cấp vLLM:**
   * **Khóa API:** Để trống hoặc nhập giá trị bất kỳ vì vLLM không yêu cầu khóa.
   * **Địa chỉ API:** Nhập địa chỉ API của vLLM, mặc định là: `http://localhost:8000/` (điều chỉnh nếu dùng cổng khác).
   * **Quản lý mô hình:** Thêm tên mô hình đã tải trong vLLM. Ví dụ: với lệnh `python -m vllm.entrypoints.openai.api_server --model gpt2`, nhập `gpt2`.
5. **Bắt đầu trò chuyện:** Chọn nhà cung cấp vLLM và mô hình `gpt2` trong Cherry Studio để bắt đầu tương tác với LLM vận hành bởi vLLM!

## Mẹo và thủ thuật

* **Đọc kỹ tài liệu:** Luôn tham khảo tài liệu chính thức trước khi thêm nhà cung cấp để hiểu rõ về khóa API, địa chỉ truy cập và tên mô hình.
* **Kiểm tra khóa API:** Dùng nút "Kiểm tra" để xác minh khóa, tránh lỗi không sử dụng được.
* **Chú ý địa chỉ API:** Địa chỉ có thể khác nhau tùy nhà cung cấp và mô hình.
* **Thêm mô hình theo nhu cầu:** Chỉ thêm các mô hình bạn thực sự dùng, tránh thêm quá nhiều mô hình không cần thiết.