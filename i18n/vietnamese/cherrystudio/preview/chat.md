---
icon: message
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Giao Diện Hội Thoại

## Trợ lý và Chủ đề

### Trợ lý

`Trợ lý` là thiết lập cá nhân hóa cho mô hình đã chọn, như cấu hình gợi ý và tham số, giúp mô hình hoạt động phù hợp hơn với công việc bạn mong đợi.

`Trợ lý mặc định` được cấu hình sẵn với tham số chung (không có prompt). Bạn có thể sử dụng trực tiếp hoặc tìm kiếm cấu hình cần thiết tại [Trang Smart Agent](agents.md).

### Chủ đề

`Trợ lý` là tập cha của `Chủ đề`. Một trợ lý có thể tạo nhiều chủ đề (hội thoại), tất cả `Chủ đề` dùng chung thiết lập mô hình như tham số và prompt từ `Trợ lý`.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Nút trong hộp thoại

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Chủ đề mới` Tạo chủ đề mới trong trợ lý hiện tại.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Tải lên ảnh hoặc tài liệu` Tải ảnh lên cần mô hình hỗ trợ. Tải tài liệu sẽ tự động phân tích thành văn bản làm ngữ cảnh cho mô hình.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Tìm kiếm web` Cần cấu hình thông tin tìm kiếm web trong cài đặt. Kết quả tìm kiếm sẽ trả về làm ngữ cảnh cho mô hình lớn. Xem chi tiết tại [Chế độ có kết nối mạng](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Cơ sở tri thức` Bật cơ sở tri thức. Xem [Hướng dẫn Cơ sở tri thức](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Máy chủ MCP` Kích hoạt tính năng máy chủ MCP. Xem [Hướng dẫn sử dụng MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Tạo ảnh` Mặc định không hiển thị. Đối với mô hình hỗ trợ tạo ảnh (như Gemini), cần bật thủ công để tạo ảnh.

{% hint style="info" %}
Vì lý do kỹ thuật, bạn phải bật nút thủ công để tạo ảnh. Nút này sẽ bị loại bỏ sau khi tính năng được tối ưu hóa.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Chọn mô hình` Chuyển sang mô hình cụ thể cho hội thoại tiếp theo, giữ nguyên ngữ cảnh.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Cụm từ nhanh` Cần cấu hình sẵn cụm từ thường dùng trong cài đặt. Hỗ trợ biến.

![](../../.gitbook/assets/对话界面/清空消息.png) `Xóa tin nhắn` Xóa tất cả nội dung trong chủ đề này.

![](../../.gitbook/assets/对话界面/展开.png) `Mở rộng` Mở rộng hộp thoại để nhập văn bản dài.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Xóa ngữ cảnh` Cắt ngữ cảnh mà mô hình nhận được mà không xóa nội dung. Mô hình sẽ "quên" nội dung hội thoại trước đó.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Ước tính số Token` Hiển thị ước tính Token. Bốn dữ liệu lần lượt là `Số ngữ cảnh hiện tại`, `Số ngữ cảnh tối đa` (∞ nghĩa là ngữ cảnh vô hạn), `Số từ trong tin nhắn hiện tại`, `Ước tính số Token`.

{% hint style="info" %}
Tính năng này chỉ dùng để ước tính số Token. Số Token thực tế khác nhau giữa các mô hình. Vui lòng tham khảo dữ liệu từ nhà cung cấp mô hình.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Dịch` Dịch nội dung trong hộp nhập hiện tại sang tiếng Anh.

## Cài đặt hội thoại

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Thiết lập mô hình

Thiết lập mô hình đồng bộ với tham số `Thiết lập mô hình` trong cài đặt trợ lý. Xem [Chỉnh sửa trợ lý](chat.md#chỉnh-sửa-trợ-lý).

{% hint style="info" %}
Trong cài đặt hội thoại, chỉ thiết lập mô hình này áp dụng cho trợ lý hiện tại. Các cài đặt khác áp dụng toàn cục. Ví dụ: thiết lập kiểu tin nhắn thành bong bóng sẽ áp dụng kiểu đó cho tất cả chủ đề trong mọi trợ lý.
{% endhint %}

### Cài đặt tin nhắn

#### <mark style="color:blue;">**`Đường phân cách tin nhắn`**</mark>:

Sử dụng đường phân cách giữa nội dung tin nhắn và thanh tác vụ.

{% tabs %}
{% tab title="Khi bật" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Khi tắt" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Sử dụng font chữ có chân`**</mark>：

Chuyển đổi kiểu font. Bạn cũng có thể đổi font thông qua [css tùy chỉnh](../../personalization-settings/).

#### <mark style="color:blue;">**`Hiển thị số dòng trong mã`**</mark>：

Hiển thị số dòng trong khối mã khi mô hình xuất đoạn mã.

{% tabs %}
{% tab title="Khi tắt" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Khi bật" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Khối mã có thể thu gọn`**</mark>：

Khi bật, nếu mã trong đoạn dài, khối mã sẽ tự động thu gọn.

#### <mark style="color:blue;">**`Khối mã có thể xuống dòng`**</mark>：

Khi bật, nếu một dòng mã quá dài (vượt quá cửa sổ), nó sẽ tự động xuống dòng.

#### <mark style="color:blue;">**`Tự động thu gọn nội dung tư duy`**</mark>：

Khi bật, mô hình hỗ trợ tư duy sẽ tự động thu gọn quá trình tư duy sau khi hoàn thành.

#### <mark style="color:blue;">**`Kiểu tin nhắn`**</mark>：

Có thể chuyển giao diện hội thoại sang kiểu bong bóng hoặc danh sách.

#### <mark style="color:blue;">**`Phong cách mã`**</mark>：

Có thể thay đổi phong cách hiển thị của đoạn mã.

#### <mark style="color:blue;">**`Công cụ công thức toán học`**</mark>：

* KaTeX hiển thị nhanh hơn vì được tối ưu hóa cho hiệu suất;
* MathJax hiển thị chậm hơn nhưng đầy đủ tính năng hơn, hỗ trợ nhiều ký hiệu và lệnh toán học.

#### <mark style="color:blue;">**`Cỡ chữ tin nhắn`**</mark>：

Điều chỉnh kích thước font chữ trong giao diện hội thoại.

### Cài đặt đầu vào

#### <mark style="color:blue;">**`Hiển thị ước tính số Token`**</mark>：

Hiển thị số Token ước tính tiêu thụ cho văn bản đầu vào trong hộp nhập (không phải Token thực tế tiêu thụ ngữ cảnh, chỉ để tham khảo).

#### <mark style="color:blue;">**`Dán văn bản dài dưới dạng tệp`**</mark>：

Khi dán văn bản dài từ nơi khác vào hộp nhập, nó tự động hiển thị dưới dạng tệp để giảm nhiễu khi nhập nội dung sau.

#### <mark style="color:blue;">**`Kết xuất Markdown cho tin nhắn nhập`**</mark>：

Khi tắt, chỉ kết xuất tin nhắn trả lời của mô hình, không kết xuất tin nhắn đã gửi.

{% tabs %}
{% tab title="Khi tắt" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Khi bật" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Dịch bằng cách nhấn nhanh 3 lần dấu cách`**</mark>：

Sau khi nhập tin nhắn vào hộp nhập, nhấn liên tiếp 3 lần dấu cách để dịch nội dung sang tiếng Anh.

{% hint style="warning" %}
Lưu ý: Hành động này sẽ ghi đè lên văn bản gốc.
{% endhint %}

#### <mark style="color:blue;">**`Ngôn ngữ đích`**</mark>：

Thiết lập ngôn ngữ đích cho nút dịch và tính năng dịch bằng cách nhấn nhanh 3 lần dấu cách.

## Cài đặt trợ lý

Trong giao diện trợ lý, chọn <mark style="background-color:yellow;">tên trợ lý</mark> cần cài đặt → Chọn cài đặt tương ứng trong <mark style="background-color:yellow;">menu chuột phải</mark>

### Chỉnh sửa trợ lý

{% hint style="info" %}
Cài đặt trợ lý áp dụng cho tất cả chủ đề trong trợ lý đó.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Thiết lập prompt

#### <mark style="color:blue;">**`Tên`**</mark>：

Có thể tùy chỉnh tên trợ lý dễ nhận biết.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Có thể chỉnh sửa nội dung bằng cách tham khảo cách viết prompt tại trang Smart Agent.

#### Thiết lập mô hình

#### <mark style="color:blue;">**`Mô hình mặc định`**</mark>：

Có thể cố định một mô hình mặc định cho trợ lý này. Mô hình ban đầu khi thêm từ trang Smart Agent hoặc sao chép trợ lý sẽ là mô hình này. Nếu không thiết lập mục này, mô hình ban đầu sẽ là mô hình toàn cục (tức là [Mô hình trợ lý mặc định](settings/default-models.md#mo-hình-trợ-lý-mặc-định)).

{% hint style="info" %}
Mô hình mặc định của trợ lý có hai loại: một là [Mô hình hội thoại mặc định toàn cục](settings/default-models.md#mo-hình-trợ-lý-mặc-định), hai là mô hình mặc định của trợ lý; mô hình mặc định của trợ lý có độ ưu tiên cao hơn mô hình hội thoại mặc định toàn cục. Khi không thiết lập mô hình mặc định trợ lý, mô hình mặc định trợ lý = mô hình hội thoại mặc định toàn cục.
{% endhint %}

#### <mark style="color:blue;">**`Tự động đặt lại mô hình`**</mark>：

Khi bật - Khi sử dụng các mô hình khác trong chủ đề này, chủ đề mới sẽ đặt lại thành mô hình mặc định của trợ lý. Khi tắt, chủ đề mới sẽ theo mô hình đã sử dụng trong chủ đề trước.

> Ví dụ: Mô hình mặc định của trợ lý là gpt-3.5-turbo. Tôi tạo Chủ đề 1 trong trợ lý này, trong quá trình hội thoại Chủ đề 1, tôi chuyển sang gpt-4o:
>
> * Nếu tự động đặt lại bật: Khi tạo Chủ đề 2, mô hình mặc định sẽ là gpt-3.5-turbo;
> * Nếu tự động đặt lại tắt: Khi tạo Chủ đề 2, mô hình mặc định sẽ là gpt-4o.

#### <mark style="color:blue;">**`Nhiệt độ (Temperature)`**</mark> ：

Tham số nhiệt độ kiểm soát tính ngẫu nhiên và sáng tạo của văn bản do mô hình tạo (giá trị mặc định: 0.7). Cụ thể:

* Giá trị thấp (0-0.3):
  * Đầu ra xác định hơn, tập trung hơn
  * Phù hợp cho tạo mã, phân tích dữ liệu, cần độ chính xác cao
  * Xu hướng chọn từ ngữ có khả năng cao nhất
* Giá trị trung bình (0.4-0.7):
  * Cân bằng giữa sáng tạo và mạch lạc
  * Phù hợp cho hội thoại hàng ngày, viết chung
  * Khuyên dùng cho trò chuyện chatbot (khoảng 0.5)
* Giá trị cao (0.8-1.0):
  * Tạo đầu ra sáng tạo và đa dạng hơn
  * Phù hợp cho viết sáng tạo, động não
  * Nhưng có thể giảm tính mạch lạc của văn bản

#### <mark style="color:blue;">**`Top P (Lấy mẫu hạt nhân)`**</mark>：

Giá trị mặc định là 1. Giá trị càng nhỏ, nội dung AI tạo ra càng đơn điệu, dễ hiểu; giá trị càng lớn, phạm vi từ ngữ càng rộng, càng đa dạng.

Lấy mẫu hạt nhân ảnh hưởng đến đầu bằng cách kiểm soát ngưỡng xác suất chọn từ:

* Giá trị nhỏ (0.1-0.3):
  * Chỉ xem xét