---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Vertex AI

## Tổng quan về Hướng dẫn

### 1. Nhận APIKey

*   Trước khi nhận api key của Gemini, bạn cần có một dự án Google Cloud (nếu đã có, có thể bỏ qua bước này)
*   Truy cập [Google Cloud](https://console.cloud.google.com/projectcreate) để tạo dự án, điền tên dự án và nhấp vào "Tạo dự án"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

*   Truy cập [Bảng điều khiển Vertex AI](https://console.cloud.google.com/vertex-ai)
*   Trong dự án vừa tạo, kích hoạt [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Thiết lập Quyền truy cập API

*   Mở giao diện quản lý quyền [Tài khoản dịch vụ](https://console.cloud.google.com/iam-admin/serviceaccounts), tạo tài khoản dịch vụ mới

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   Trong trang quản lý tài khoản dịch vụ, tìm tài khoản vừa tạo, nhấp `Khóa` và tạo khóa mới định dạng JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   Sau khi tạo thành công, file khóa sẽ tự động lưu dưới dạng JSON trên máy tính của bạn, vui lòng **lưu trữ cẩn thận**

## 3. Cấu hình Vertex AI trong Cherry Studio

*   Chọn nhà cung cấp Vertex AI
*   Điền các trường tương ứng từ file JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Nhấp vào [Thêm mô hình](https://console.cloud.google.com/vertex-ai/model-garden), bạn có thể sử dụng ngay lập tức!