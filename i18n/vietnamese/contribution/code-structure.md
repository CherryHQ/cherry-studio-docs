---
hidden: True
icon: code
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Cấu Trúc Mã Nguồn

```yaml
...
├─ docs/ #Thư mục tài liệu
├─ resources/ #Thư mục tệp tài nguyên
├─ scripts/ #Thư mục tệp script
└─ src/ #Thư mục mã nguồn chính
    ├─main/ #Mã tiến trình chính
    ├─preload/ #Thư mục script preload
    └─renderer/ #Mã tiến trình render
        ├─src/ #Mã nguồn của tiến trình render
            ├─assets/ #Tệp tài nguyên
                ├─fonts/ #Tệp font
                ├─images/ #Tệp hình ảnh (avatar, v.v.)
                └─styles/ #Tệp kiểu
            ├─components/ #Components
            ├─config/ #Tệp cấu hình
            ├─context/ #Context
            ├─databases/ #Tệp liên quan cơ sở dữ liệu
            ├─hooks/ #Custom Hooks
            ├─i18n/ #Tệp quốc tế hóa
            ├─pages/ #Tệp trang
            ├─providers/ #Cấu hình nhà cung cấp dịch vụ
            ├─services/ #Tệp dịch vụ
            ├─store/ #Tệp quản lý trạng thái
            ├─types/ #Tệp định nghĩa kiểu TypeScript
            ├─utils/ #Hàm tiện ích
            ...
        ...
    ...
...

```