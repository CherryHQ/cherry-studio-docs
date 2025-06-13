---
icon: ban
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Cấu hình danh sách đen tìm kiếm trên web

Cherry Studio hỗ trợ cấu hình danh sách đen bằng hai cách: thủ công và thêm nguồn đăng ký. Quy tắc cấu hình tham khảo [ublacklist](https://github.com/iorate/ublacklist)

## Cấu hình thủ công

Bạn có thể thêm quy tắc cho kết quả tìm kiếm hoặc nhấp vào biểu tượng thanh công cụ để chặn các trang web được chỉ định. Quy tắc có thể được xác định bằng các cách sau: [kiểu so khớp](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (ví dụ: `*://*.example.com/*`) hoặc sử dụng [biểu thức chính quy](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (ví dụ: `/example\.(net|org)/`).

## Cấu hình nguồn đăng ký

Bạn cũng có thể đăng ký các bộ quy tắc công cộng. Trang web này liệt kê một số đăng ký:  
https://iorate.github.io/ublacklist/subscriptions

Dưới đây là một số liên kết đăng ký được khuyến nghị:

| Tên                                                                                                        | Liên kết                                                                                                                               | Loại     |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [Đăng ký uBlacklist biên dịch](https://github.com/eallion/uBlacklist-subscription-compilation)             | https://git.io/ublacklist                                                                                                              | Tiếng Trung |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)             | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt                                  | Tạo bởi AI |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Cấu hình nguồn đăng ký</p></figcaption></figure>