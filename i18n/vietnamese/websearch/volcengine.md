---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Kết nối mạng của Volc Engine

### 1. Đăng nhập/Đăng ký tài khoản Volc Engine <a href="#rclz7" id="rclz7"></a>

Truy cập trang web chính thức: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Trang chủ Volc Engine</p></figcaption></figure>

### 2. Tạo 「Ứng dụng của tôi」 có khả năng kết nối mạng <a href="#gvzaa" id="gvzaa"></a>

2.1. Đăng nhập Volc Engine, truy cập trang 「Volc Ark」 tại: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Thực hiện tuần tự:**<mark style="color:red;">**「Ứng dụng của tôi」 → 「Tạo ứng dụng」 → 「Zero Code」 → 「Single Chat」**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Điền thông tin và xuất bản ứng dụng <a href="#zzdfe" id="zzdfe"></a>

**Tên ứng dụng**: Đặt tên tùy ý (phần có<mark style="color:red;">**\*bắt buộc**</mark>, các phần khác có thể bỏ qua)

<mark style="color:red;">**Quan trọng: Kích hoạt plugin kết nối mạng (cần kích hoạt trước)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Kích hoạt tính năng plugin kết nối mạng (lưu ý chi phí và hạn mức miễn phí) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Nhấp "Mua ngay" và thực hiện từng bước đến khi hiển thị giao diện sau, nghĩa là đã kích hoạt thành công.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Lưu ý trạng thái - đến đây đã kích hoạt thành công</p></figcaption></figure>

Quay lại giao diện "Điền thông tin ứng dụng" để tiếp tục.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Giải thích 「Cấu hình nâng cao」 tìm kiếm mạng <a href="#sp6uz" id="sp6uz"></a>

Chọn tùy theo nhu cầu, đề xuất cá nhân:

* Muốn kiểm soát chính xác đầu vào/đầu ra: Dùng 「**Gọi tùy chỉnh**」
* Muốn đơn giản: Dùng 「**Gọi tự động**」 - giá trị mặc định
* Không quan tâm chi phí, cần thông tin cập nhật nhất: 「**Bắt buộc bật**」

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Xuất bản ứng dụng <a href="#fe1gf" id="fe1gf"></a>

Nhấp nút 「Xuất bản」 ở góc phải trên cùng để hoàn thành tạo ứng dụng.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Lấy API Key <a href="#jtqlu" id="jtqlu"></a>

Thực hiện tuần tự: **「Hướng dẫn gọi API」→「Chọn và sao chép API Key」→「Xem và chọn」**

Sao chép API key, sau đó dán vào cherry studio (xem hướng dẫn chi tiết trong giao diện dưới)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Lưu ý: Nếu không có API key, nhấp 「**Tạo API Key**」 ở góc phải trên cùng hộp thoại rồi sao chép.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Sử dụng API Key trong cherry studio để truy cập mạng deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Mở cherry studio → 「Cài đặt」 → 「Đặt tên bất kỳ」 → 「Loại: openAI」 <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Cấu hình url và key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Lưu ý: Nếu không tìm thấy địa chỉ hoặc không phải node Bắc Kinh, tìm địa chỉ chính xác tại đây, đừng quên "/":</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Thêm tên mô hình <a href="#qmh3i" id="qmh3i"></a>

Lưu ý: Sao chép dòng chữ nhỏ làm tên mô hình, nếu không sẽ báo lỗi.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Xem trước kết quả <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>