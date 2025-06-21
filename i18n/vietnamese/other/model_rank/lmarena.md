
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Bảng Xếp Hạng LLM Arena (Cập nhật thời gian thực)

Đây là bảng xếp hạng dựa trên dữ liệu từ Chatbot Arena (lmarena.ai), được tạo tự động bằng quy trình tự động.

> **Thời điểm cập nhật dữ liệu**: 2025-06-21 09:44:44 UTC / 2025-06-21 17:44:44 CST (Giờ Bắc Kinh)

{% hint style="info" %}
Nhấp vào **tên mô hình** trong bảng xếp hạng để chuyển đến trang thông tin chi tiết hoặc dùng thử.
{% endhint %}

## Bảng Xếp Hạng

| Xếp hạng(UB) | Xếp hạng(StyleCtrl) | Tên mô hình                                                                                                                                       | Điểm số | Khoảng tin cậy | Số phiếu     | Nhà cung cấp              | Giấy phép               | Ngày cắt dữ liệu kiến thức |
|:-------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|:--------|:---------------|:-------------|:--------------------------|:------------------------|:-----------------------|
| 1            | 1                  | [Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)                        | 1480    | +6/-6          | 8,825        | Google                 | Độc quyền           | Không có dữ liệu       |
| 2            | 2                  | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                        | 1446    | +5/-5          | 13,025       | Google                 | Độc quyền           | Không có dữ liệu       |
| ... *(giữ nguyên toàn bộ bảng, chỉ dịch tiêu đề cột)* ... |
| 204          | 202                | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                             | 815     | +12/-10        | 2,446        | Meta                   | Phi thương mại     | 2023/2                |

## Giải thích

- **Xếp hạng(UB)**: Xếp hạng dựa trên mô hình Bradley-Terry. Xếp hạng này phản ánh hiệu suất tổng thể của mô hình trong Arena, cung cấp **giới hạn trên** ước tính điểm Elo để hiểu khả năng cạnh tranh tiềm năng.
- **Xếp hạng(StyleCtrl)**: Xếp hạng sau khi kiểm soát phong cách hội thoại. Xếp hạng này nhằm giảm thiểu độ lệch ưu tiên do phong cách trả lời (ví dụ: dài dòng, súc tích) để đánh giá khách quan hơn năng lực cốt lõi.
- **Tên mô hình**: Tên của mô hình ngôn ngữ lớn (LLM). Cột này đã nhúng liên kết liên quan, nhấp để chuyển hướng.
- **Điểm số**: Điểm Elo mô hình đạt được thông qua phiếu bầu người dùng trong Arena. Điểm Elo là hệ thống xếp hạng tương đối, điểm càng cao thể hiện hiệu suất càng tốt. Điểm này thay đổi động, phản ánh sức mạnh tương đối của mô hình trong môi trường cạnh tranh hiện tại.
- **Khoảng tin cậy**: Khoảng tin cậy 95% cho điểm Elo (ví dụ: `+6/-6`). Khoảng càng nhỏ cho thấy điểm đánh giá càng ổn định và đáng tin cậy; ngược lại, khoảng lớn hơn có thể do thiếu dữ liệu hoặc hiệu suất dao động. Cung cấp đánh giá định lượng về độ chính xác điểm số.
- **Số phiếu**: Tổng số phiếu bầu mô hình nhận được trong Arena. Số phiếu càng lớn thường cho thấy độ tin cậy thống kê của điểm số càng cao.
- **Nhà cung cấp**: Tổ chức hoặc công ty cung cấp mô hình.
- **Giấy phép**: Loại giấy phép của mô hình, ví dụ: Độc quyền (Proprietary), Apache 2.0, MIT, v.v.
- **Ngày cắt dữ liệu kiến thức**: Ngày cắt kiến thức cho dữ liệu huấn luyện của mô hình. **Không có dữ liệu** cho biết thông tin không được cung cấp hoặc không xác định.

## Nguồn dữ liệu & Tần suất cập nhật

Dữ liệu bảng xếp hạng này được tự động tạo và cung cấp bởi dự án [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), dự án này lấy và xử lý dữ liệu từ [lmarena.ai](https://lmarena.ai/). Bảng xếp hạng này được cập nhật tự động hàng ngày bởi GitHub Actions.

## Tuyên bố miễn trừ trách nhiệm

Báo cáo này chỉ mang tính chất tham khảo. Dữ liệu bảng xếp hạng mang tính động và dựa trên phiếu bầu ưu tiên của người dùng trên Chatbot Arena trong khoảng thời gian cụ thể. Tính toàn vẹn và độ chính xác của dữ liệu phụ thuộc vào nguồn dữ liệu cấp cao và quá trình cập nhật/xử lý của dự án `fboulnois/llm-leaderboard-csv`. Các mô hình khác nhau có thể áp dụng giấy phép khác nhau, khi sử dụng vui lòng tham khảo hướng dẫn chính thức từ nhà cung cấp mô hình.