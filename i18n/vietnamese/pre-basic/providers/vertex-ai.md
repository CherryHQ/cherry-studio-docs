---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Vertex AI

## Tổng quan hướng dẫn

### 1. Lấy API Key

* Trước khi lấy API Key cho Gemini, bạn cần có một dự án Google Cloud (nếu đã có thì bỏ qua bước này)
* Truy cập [Google Cloud](https://console.cloud.google.com/projectcreate) để tạo dự án, điền tên dự án và nhấp "Tạo dự án"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Truy cập [console Vertex AI](https://console.cloud.google.com/vertex-ai)
* Bật [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) trong dự án vừa tạo

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Thiết lập quyền truy cập API

* Mở trang quản lý [dịch vụ tài khoản](https://console.cloud.google.com/iam-admin/serviceaccounts), tạo dịch vụ tài khoản mới

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Tìm dịch vụ tài khoản vừa tạo, nhấp `Khoá` và tạo khoá mới định dạng JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Sau khi tạo thành công, tệp khoá sẽ tự động tải về máy tính dưới dạng JSON, hãy **lưu trữ cẩn thận**

## 3. Cấu hình Vertex AI trong Cherry Studio

* Chọn nhà cung cấp Vertex AI
* Điền các trường tương ứng từ tệp JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Nhấp thêm [mô hình](https://console.cloud.google.com/vertex-ai/model-garden) là bạn có thể bắt đầu sử dụng ngay!