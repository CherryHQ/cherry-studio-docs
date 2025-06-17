
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

```markdown
# PPIO Pai Ou Yun

## Cherry Studio tích hợp với PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Tổng quan hướng dẫn <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio là ứng dụng máy khách đa mô hình, hiện hỗ trợ bản cài đặt cho các hệ điều hành Windows, Linux, MacOS. Nó tích hợp các mô hình LLM chính thống, cung cấp hỗ trợ đa tình huống. Người dùng có thể nâng cao hiệu suất công việc thông qua quản lý hội thoại thông minh, tùy chỉnh mã nguồn mở và giao diện đa chủ đề.

Cherry Studio hiện đã được tích hợp sâu với **kênh API hiệu suất cao PPIO** – thông qua bảo đảm năng lực tính toán cấp doanh nghiệp, đạt được **tốc độ phản hồi cao DeepSeek-R1/V3** và **khả dụng dịch vụ 99.9%**, mang đến trải nghiệm nhanh chóng và mượt mà.

Hướng dẫn dưới đây bao gồm giải pháp tích hợp đầy đủ (bao gồm cấu hình khóa bí mật), giúp bạn kích hoạt chế độ nâng cao "Lập lịch thông minh Cherry Studio + API hiệu suất cao PPIO" chỉ trong 3 phút.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Truy cập CherryStudio, thêm "PPIO" làm nhà cung cấp mô hình <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Đầu tiên truy cập trang web chính thức để tải Cherry Studio: [https://cherry-ai.com/download](https://cherry-ai.com/download) (Nếu không truy cập được, có thể mở liên kết Quark Pan dưới đây để tải phiên bản bạn cần: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Nhấp vào cài đặt ở góc trái dưới cùng, tùy chỉnh tên nhà cung cấp thành: `PPIO`, nhấp "Xác nhận"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Truy cập [Quản lý khóa API PPIO ](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), nhấp vào 【Ảnh đại diện người dùng】—【Quản lý khóa API】 để vào bảng điều khiển

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Nhấp nút 【+ Tạo】 để tạo khóa API mới. Tùy chỉnh tên khóa, **khóa tạo ra chỉ hiển thị khi tạo, bắt buộc sao chép và lưu vào tài liệu để tránh ảnh hưởng sử dụng sau này**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Trong CherryStudio nhập khóa: nhấp vào cài đặt, chọn 【PPIO Pai Ou Yun】, nhập khóa API đã tạo từ trang chủ, cuối cùng nhấp 【Kiểm tra】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Chọn mô hình: ví dụ deepseek/deepseek-r1/community, nếu cần đổi mô hình khác có thể thay đổi trực tiếp.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 và V3 phiên bản community chỉ dành cho trải nghiệm thử, cũng là phiên bản mô hình đầy đủ tham số, độ ổn định và hiệu quả không khác biệt, nếu cần gọi lượng lớn bắt buộc **nạp tiền và chuyển sang phiên bản non-community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Cấu hình sử dụng mô hình <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Nhấp 【Kiểm tra】 hiển thị kết nối thành công là có thể sử dụng bình thường

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Cuối cùng nhấp 【@】 chọn mô hình DeepSeek R1 vừa thêm dưới nhà cung cấp PPIO, sẽ bắt đầu trò chuyện thành công~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Một số tư liệu tham khảo từ: [ Trần Ân ](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Hướng dẫn sử dụng bằng video PPIO×Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Nếu bạn thích học trực quan hơn, chúng tôi đã chuẩn bị hướng dẫn video trên Bilibili. Thông qua hướng dẫn từng bước, giúp bạn nhanh chóng làm chủ phương pháp cấu hình 「PPIO API + Cherry Studio」, nhấp liên kết dưới đây đến thẳng video, bắt đầu trải nghiệm phát triển mượt mà → [《 【Vẫn phát điên vì DeepSeek quay vòng?】PPIO Cloud + DeepSeek phiên bản đầy đủ =? Không còn tắc nghẽn, cất cánh ngay lập tức》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Nguồn tư liệu video: sola】
```