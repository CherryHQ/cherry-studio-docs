
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Google Gemini

## Lấy API Key

* Để lấy API Key cho Gemini, trước hết bạn cần có dự án Google Cloud (có thể bỏ qua bước này nếu đã có sẵn)
* Truy cập [Google Cloud](https://console.cloud.google.com/projectcreate) tạo dự án, điền tên dự án và nhấp "Tạo dự án"

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

* Tại trang [API Key chính thức](https://aistudio.google.com/app/apikey?hl=zh-cn), nhấp `密钥 创建API密钥` 

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

* Sao chép key vừa tạo, mở mục [Cài đặt nhà cung cấp](broken-reference) trong CherryStudio
* Tìm nhà cung cấp Gemini, dán key đã lấy được vào

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

* Nhấp "Quản lý" hoặc "Thêm" ở cuối trang, thêm các mô hình hỗ trợ và bật công tắc nhà cung cấp ở góc phải trên cùng để bắt đầu sử dụng.

{% hint style="info" %}
- Khu vực Trung Quốc (trừ Đài Loan) không thể truy cập trực tiếp Google Gemini, cần tự thiết lập proxy
{% endhint %}