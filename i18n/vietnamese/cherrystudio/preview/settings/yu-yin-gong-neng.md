---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Chức năng thoại

```
Hướng dẫn sử dụng chức năng thoại của Cherry Studio

I. Tổng quan về chức năng thoại

Cherry Studio cung cấp ba mô-đun chức năng thoại chính: TTS (chuyển văn bản thành giọng nói), ASR (nhận diện giọng nói) và cuộc gọi thoại. Các chức năng này cho phép bạn giao tiếp tự nhiên với AI bằng giọng nói, nâng cao trải nghiệm sử dụng.

- TTS (Chuyển văn bản thành giọng nói): Chuyển đổi văn bản phản hồi của AI thành giọng nói đầu ra
- ASR (Nhận diện giọng nói): Chuyển đổi giọng nói của bạn thành văn bản đầu vào
- Cuộc gọi thoại: Kết hợp TTS và ASR, tạo trải nghiệm hội thoại thoại tương tự ChatGPT

II. Chức năng TTS (Chuyển văn bản thành giọng nói)

1. Các loại dịch vụ hỗ trợ

Cherry Studio hỗ trợ bốn loại dịch vụ TTS:

- OpenAI: Sử dụng TTS API của OpenAI, yêu cầu khóa API
- Trình duyệt TTS: Sử dụng tính năng tổng hợp giọng nói tích hợp sẵn của trình duyệt, miễn phí không cần cấu hình
- Siliconflow: Sử dụng dịch vụ TTS của Siliconflow, yêu cầu khóa API
- TTS trực tuyến miễn phí: Sử dụng dịch vụ TTS trực tuyến miễn phí, không cần khóa API

2. Phương pháp cài đặt

1) Vào trang cài đặt, chọn tab "Chức năng thoại"
2) Trong tab con "TTS":
   - Bật chức năng TTS (bật công tắc)
   - Chọn loại dịch vụ TTS
   - Tùy theo loại dịch vụ đã chọn, cấu hình các tham số tương ứng:
     - OpenAI: Nhập khóa API, địa chỉ API, chọn giọng nói và mô hình
     - Trình duyệt TTS: Chọn giọng nói
     - Siliconflow: Nhập khóa API, địa chỉ API, chọn giọng nói, mô hình, định dạng phản hồi và tốc độ nói
     - TTS trực tuyến miễn phí: Chọn giọng nói và định dạng đầu ra
3) Cấu hình tùy chọn lọc TTS (tùy chọn):
   - Lọc quá trình suy nghĩ
   - Lọc đánh dấu Markdown
   - Lọc khối mã
4) Đặt hiển thị thanh tiến trình TTS hay không
5) Nhấp nút "Kiểm tra TTS" để kiểm tra cấu hình có chính xác không

3. Phương pháp sử dụng

- Sau khi bật TTS, phản hồi của AI sẽ tự động chuyển thành giọng nói đầu ra
- Trong giao diện trò chuyện, dưới mỗi phản hồi AI sẽ hiển thị nút phát TTS
- Nhấp nút phát để phát/tạm dừng giọng nói
- Nếu đã bật thanh tiến trình TTS, sẽ hiển thị tiến trình phát dưới văn bản
- Văn bản dài sẽ tự động phân đoạn tổng hợp và phát liên tục

III. Chức năng ASR (Nhận diện giọng nói)

1. Các loại dịch vụ hỗ trợ

Cherry Studio hỗ trợ ba loại dịch vụ ASR:

- OpenAI: Sử dụng mô hình Whisper của OpenAI, yêu cầu khóa API
- Trình duyệt: Sử dụng tính năng nhận diện giọng nói tích hợp sẵn của trình duyệt, miễn phí không cần cấu hình
- Máy chủ cục bộ: Kết nối với máy chủ WebSocket cục bộ để nhận diện giọng nói

2. Phương pháp cài đặt

1) Vào trang cài đặt, chọn tab "Chức năng thoại"
2) Trong tab con "ASR":
   - Bật chức năng ASR (bật công tắc)
   - Chọn loại dịch vụ ASR
   - Tùy theo loại dịch vụ đã chọn, cấu hình các tham số tương ứng:
     - OpenAI: Nhập khóa API, địa chỉ API, chọn mô hình
     - Trình duyệt: Không cần cấu hình thêm
     - Máy chủ cục bộ: Có thể đặt tự động khởi động máy chủ ASR khi ứng dụng khởi động
   - Chọn ngôn ngữ nhận diện giọng nói (mặc định là tiếng Trung)
3) Nhấp nút "Kiểm tra ASR" để kiểm tra cấu hình có chính xác không

3. Phương pháp sử dụng

- Sau khi bật ASR, nút nhận diện giọng nói sẽ hiển thị bên cạnh ô nhập
- Nhấp nút nhận diện giọng nói để bắt đầu ghi âm
- Sau khi nói, giọng nói sẽ được chuyển thành văn bản và điền vào ô nhập
- Nhấp lại nút để kết thúc ghi âm
- ASR hỗ trợ nhận diện liên tục nhiều câu, sử dụng chế độ tích lũy

IV. Chức năng cuộc gọi thoại

1. Đặc điểm chức năng

- Kết hợp TTS và ASR, tạo trải nghiệm hội thoại thoại tương tự ChatGPT
- Sử dụng giao diện cửa sổ nổi có thể kéo
- Hỗ trợ chế độ nhấn giữ để nói
- Hỗ trợ phím tắt tùy chỉnh
- Hỗ trợ thu gọn cửa sổ
- Có thể chọn mô hình cuộc gọi thoại chuyên dụng
- Hỗ trợ lời nhắc tùy chỉnh

2. Phương pháp cài đặt

1) Vào trang cài đặt, chọn tab "Chức năng thoại"
2) Trong tab con "Chức năng gọi":
   - Bật chức năng cuộc gọi thoại (bật công tắc)
   - Nhấp nút "Chọn mô hình" để chọn mô hình AI dùng cho cuộc gọi thoại
   - Tùy chỉnh lời nhắc cuộc gọi thoại trong hộp văn bản lời nhắc (tùy chọn)
   - Nhấp nút "Lưu" để lưu lời nhắc, hoặc nhấp nút "Đặt lại" để khôi phục lời nhắc mặc định

3. Phương pháp sử dụng

1) Trong giao diện trò chuyện, nhấp nút cuộc gọi thoại (biểu tượng điện thoại) bên phải ô nhập
2) Cửa sổ cuộc gọi thoại sẽ mở ra và phát lời chào thoại
3) Nhấn giữ nút "Nhấn giữ để nói" để bắt đầu ghi âm (hoặc sử dụng phím tắt đã cài đặt)
4) Thả nút để kết thúc ghi âm và gửi cho AI xử lý
5) AI tạo phản hồi và phát qua TTS
6) Sử dụng các nút điều khiển trong cửa sổ:
   - Nút tắt tiếng/bật tiếng: Điều khiển đầu ra TTS
   - Nút tạm dừng/tiếp tục: Tạm dừng hoặc tiếp tục hội thoại
   - Nút cài đặt: Cấu hình phím tắt
   - Nút thu gọn: Thu gọn cửa sổ, chỉ giữ lại dòng nhấn giữ để nói
7) Nhấp nút đóng để kết thúc cuộc gọi

4. Cài đặt phím tắt

1) Trong cửa sổ cuộc gọi thoại, nhấp nút cài đặt
2) Trong bảng cài đặt hiện ra, nhấp nút phím tắt
3) Nhấn phím bạn muốn đặt (như phím cách, phím Shift, v.v.)
4) Nhấp nút "Lưu" để lưu cài đặt
5) Khi sử dụng, nhấn giữ phím tắt đã đặt để bắt đầu ghi âm, thả ra để kết thúc ghi âm và gửi

V. Các vấn đề thường gặp và giải pháp

1. Vấn đề liên quan đến TTS

- Vấn đề: TTS không phát ra âm thanh
  Giải pháp: Kiểm tra đã bật chức năng TTS chưa, đảm bảo đã chọn đúng loại dịch vụ và cấu hình các tham số cần thiết

- Vấn đề: Chất lượng phát TTS kém
  Giải pháp: Thử đổi loại dịch vụ TTS hoặc giọng nói khác

- Vấn đề: Hiển thị thông báo lỗi khi phát TTS
  Giải pháp: Kiểm tra khóa API có chính xác không, kết nối mạng có bình thường không

2. Vấn đề liên quan đến ASR

- Vấn đề: ASR không nhận diện được giọng nói
  Giải pháp: Kiểm tra đã bật chức năng ASR chưa, đảm bảo đã chọn đúng loại dịch vụ và cấu hình các tham số cần thiết

- Vấn đề: Độ chính xác nhận diện ASR thấp
  Giải pháp: Thử đổi loại dịch vụ ASR khác, hoặc điều chỉnh vị trí micro và âm lượng

- Vấn đề: Kết nối máy chủ ASR thất bại
  Giải pháp: Kiểm tra máy chủ cục bộ có hoạt động bình thường không, hoặc thử khởi động lại ứng dụng

3. Vấn đề liên quan đến cuộc gọi thoại

- Vấn đề: Không thể mở cửa sổ cuộc gọi thoại
  Giải pháp: Kiểm tra đã bật chức năng cuộc gọi thoại chưa, đảm bảo chức năng TTS và ASR đã được cấu hình chính xác

- Vấn đề: Nhấn giữ để nói không phản ứng
  Giải pháp: Kiểm tra quyền micro đã được cấp chưa, hoặc thử khởi động lại cuộc gọi thoại

- Vấn đề: Phản hồi của AI không có âm thanh đầu ra
  Giải pháp: Kiểm tra đã bật chức năng TTS chưa, đảm bảo không bị tắt tiếng

VI. Cài đặt nâng cao và tùy chọn tùy chỉnh

1. Cài đặt nâng cao TTS

- Tùy chọn lọc: Có thể chọn lọc quá trình suy nghĩ, đánh dấu Markdown và khối mã để phát TTS mượt mà hơn
- Hiển thị thanh tiến trình: Có thể chọn hiển thị thanh tiến trình TTS hay không
- Giọng nói và mô hình tùy chỉnh: Có thể thêm tùy chọn giọng nói và mô hình tùy chỉnh

2. Cài đặt nâng cao ASR

- Tự động khởi động máy chủ: Có thể đặt tự động khởi động máy chủ ASR khi ứng dụng khởi động
- Lựa chọn ngôn ngữ: Có thể chọn ngôn ngữ nhận diện giọng nói khác nhau

3. Cài đặt nâng cao cuộc gọi thoại

- Lời nhắc tùy chỉnh: Có thể tùy chỉnh lời nhắc cuộc gọi thoại để hướng dẫn AI cách phản hồi trong chế độ cuộc gọi thoại
- Lựa chọn mô hình chuyên dụng: Có thể chọn mô hình AI chuyên dụng riêng cho cuộc gọi thoại, tách biệt với mô hình đang sử dụng trong hội thoại hiện tại
- Phím tắt tùy chỉnh: Có thể đặt phím tắt tùy chỉnh để điều khiển ghi âm

VII. Đề xuất sử dụng

1. Chọn dịch vụ TTS phù hợp:
   - Nếu yêu cầu chất lượng giọng nói cao: Khuyến nghị sử dụng OpenAI hoặc Siliconflow
   - Nếu không muốn cấu hình API: Có thể sử dụng trình duyệt TTS hoặc TTS trực tuyến miễn phí

2. Chọn dịch vụ ASR phù hợp:
   - Nếu yêu cầu độ chính xác cao: Khuyến nghị sử dụng OpenAI
   - Nếu không muốn cấu hình API: Có thể sử dụng nhận diện giọng nói tích hợp sẵn trong trình duyệt

3. Tối ưu hóa trải nghiệm cuộc gọi thoại:
   - Sử dụng tai nghe để tránh đầu ra TTS bị ASR thu lại lần nữa
   - Sử dụng trong môi trường yên tĩnh để nâng cao độ chính xác nhận diện
   - Sử dụng lời nhắc tùy chỉnh giúp phản hồi AI phù hợp hơn với phát giọng nói

4. Điều chỉnh cài đặt theo nhu cầu:
   - Nếu chủ yếu giao tiếp bằng văn bản: Chỉ cần bật chức năng TTS
   - Nếu chủ yếu nhập liệu bằng giọng nói: Chỉ cần bật chức năng ASR
   - Nếu cần trải nghiệm hội thoại thoại hoàn chỉnh: Bật chức năng cuộc gọi thoại

Hy vọng hướng dẫn sử dụng này giúp bạn tận dụng tối đa chức năng thoại của Cherry Studio, tận hưởng trải nghiệm tương tác AI tự nhiên và tiện lợi hơn!
```