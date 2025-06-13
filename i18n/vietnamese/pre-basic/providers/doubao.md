
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# ByteDance (Đậu Bao)

* Đăng nhập [Volcano Engine](https://console.volcengine.com/)
* Trực tiếp nhấp chuột [truy cập tại đây](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Lấy API Key

* Nhấp vào [Quản lý API Key](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) trong thanh bên dưới
* Tạo API Key

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* Sau khi tạo thành công, nhấp vào biểu tượng con mắt nhỏ cạnh API Key đã tạo để hiển thị và sao chép

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Dán API Key đã sao chép vào CherryStudio, sau đó bật công tắc nhà cung cấp dịch vụ.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Kích hoạt và thêm mô hình

* Trong [quản lý kích hoạt](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) ở cuối thanh bên điều khiển Ark, kích hoạt các mô hình cần sử dụng. Tại đây bạn có thể kích hoạt các mô hình như Đậu Bao series hoặc DeepSeek theo nhu cầu.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* Trong [tài liệu danh sách mô hình](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), tìm Model ID tương ứng với mô hình cần sử dụng.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Ví dụ danh sách Model ID của Volcano Engine"><figcaption></figcaption></figure>

* Mở phần [cài đặt dịch vụ mô hình](../../cherrystudio/preview/settings/providers.md) trong Cherry Studio và tìm Volcano Engine
* Nhấp vào Thêm, dán Model ID đã lấy được vào hộp văn bản Model ID

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Lặp lại quy trình này để thêm các mô hình tiếp theo

### Địa chỉ API

Có hai cách viết địa chỉ API:

* Cách đầu tiên là mặc định của client: `https://ark.cn-beijing.volces.com/api/v3/`
* Cách viết thứ hai: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Hai cách viết không có sự khác biệt, giữ nguyên mặc định là được, không cần sửa đổi.

Để biết sự khác biệt giữa kết thúc bằng `/` và `#`, tham khảo phần Địa chỉ API trong cài đặt nhà cung cấp, [bấm vào đây](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Ví dụ cURL trong tài liệu chính thức</p></figcaption></figure>