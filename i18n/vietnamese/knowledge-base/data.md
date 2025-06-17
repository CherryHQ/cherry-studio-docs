---
icon: database
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Hướng dẫn Lưu trữ Dữ liệu

Dữ liệu được thêm vào kho kiến thức Cherry Studio đều được lưu trữ cục bộ. Trong quá trình thêm, một bản sao của tài liệu sẽ được đặt trong thư mục lưu trữ dữ liệu của Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Sơ đồ quy trình xử lý kho kiến thức</p></figcaption></figure>

Cơ sở dữ liệu vector: [https://turso.tech/libsql](https://turso.tech/libsql)

Khi tài liệu được thêm vào kho kiến thức Cherry Studio, tập tin sẽ được chia thành nhiều đoạn, sau đó các đoạn này sẽ được chuyển đến mô hình nhúng để xử lý.

Khi sử dụng mô hình lớn để hỏi đáp, hệ thống sẽ truy vấn các đoạn văn bản liên quan đến câu hỏi và cùng gửi chúng cho mô hình ngôn ngữ lớn xử lý.

Nếu có yêu cầu về quyền riêng tư dữ liệu, nên sử dụng cơ sở dữ liệu nhúng cục bộ và mô hình ngôn ngữ lớn cục bộ.