---
icon: trash-xmark
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Xóa cài đặt CSS

{% hint style="warning" %}
Sử dụng phương pháp này khi đặt CSS sai hoặc không thể truy cập giao diện cài đặt sau khi đặt CSS.
{% endhint %}

* Mở Developer Tools bằng cách nhấp vào cửa sổ CherryStudio và nhấn tổ hợp phím <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* Trong cửa sổ Developer Tools hiện ra, nhấp vào tab `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Nhập thủ công `document.getElementById('user-defined-custom-css').remove()` - sao chép dán thường không thực thi được.
* Nhấn Enter sau khi nhập để xóa cài đặt CSS, sau đó truy cập lại cài đặt hiển thị của CherryStudio để xóa mã CSS có vấn đề.