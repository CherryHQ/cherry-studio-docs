---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Vertex AI

## Tổng quan Hướng dẫn

### 1. Lấy API Key

* Trước khi lấy API Key cho Gemini, bạn cần có một dự án Google Cloud (nếu đã có thể bỏ qua bước này)
* Truy cập [Google Cloud](https://console.cloud.google.com/projectcreate) để tạo dự án, điền tên dự án và nhấp vào tạo dự án

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Truy cập [Bảng điều khiển Vertex AI](https://console.cloud.google.com/vertex-ai)
* Trong dự án đã tạo, kích hoạt [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Thiết lập Quyền truy cập API

* Mở giao diện quyền [Tài khoản dịch vụ](https://console.cloud.google.com/iam-admin/serviceaccounts) và tạo tài khoản dịch vụ

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Trong trang quản lý tài khoản dịch vụ, tìm tài khoản dịch vụ vừa tạo, nhấp vào `Khóa (Key)` và tạo một khóa mới định dạng JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Sau khi tạo thành công, tệp khóa sẽ được tự động lưu vào máy tính của bạn ở định dạng JSON, vui lòng **lưu giữ cẩn thận**

## 3. Cấu hình Vertex AI trong Cherry Studio

* Chọn nhà cung cấp dịch vụ Vertex AI
* Điền các trường tương ứng từ tệp JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Nhấp vào thêm [Mô hình](https://console.cloud.google.com/vertex-ai/model-garden), và bạn có thể bắt đầu sử dụng ngay!