---
icon: book-bookmark
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Kiến thức khoa học

## Tokens là gì?

Tokens là đơn vị cơ bản để mô hình AI xử lý văn bản, có thể hiểu là đơn vị "suy nghĩ" nhỏ nhất của mô hình. Nó không hoàn toàn tương đương với ký tự hoặc từ ngữ chúng ta hiểu, mà là cách phân chia văn bản đặc biệt của chính mô hình.

#### 1. Phân đoạn tiếng Trung
* Một ký tự Trung Quốc thường được mã hóa thành 1-2 tokens
* Ví dụ: `"你好"` ≈ 2-4 tokens

#### 2. Phân đoạn tiếng Anh
* Từ thông thường thường là 1 token
* Từ dài hoặc không phổ biến sẽ bị phân tách thành nhiều tokens
* Ví dụ:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Ký tự đặc biệt
* Khoảng trắng, dấu câu... cũng chiếm tokens
* Ký tự xuống dòng thường là 1 token

{% hint style="info" %}
Tokenizer của các nhà cung cấp dịch vụ khác nhau đều khác nhau, thậm chí Tokenizer của các mô hình khác nhau cùng nhà cung cấp cũng có sự khác biệt, kiến thức này chỉ dùng để làm rõ khái niệm token.
{% endhint %}

***

## Tokenizer là gì?

Tokenizer (công cụ phân đoạn) là công cụ để mô hình AI chuyển đổi văn bản thành tokens. Nó quyết định cách chia nhỏ văn bản đầu vào thành các đơn vị nhỏ nhất mà mô hình có thể hiểu.

### Tại sao Tokenizer của các mô hình khác nhau lại khác nhau?

#### 1. Dữ liệu huấn luyện khác nhau
* Các kho ngữ liệu khác nhau dẫn đến hướng tối ưu khác nhau
* Mức độ hỗ trợ đa ngôn ngữ khác nhau
* Tối ưu chuyên ngành (y tế, pháp lý...)

#### 2. Thuật toán phân đoạn khác nhau
* BPE (Byte Pair Encoding) - OpenAI GPT series
* WordPiece - Google BERT
* SentencePiece - Phù hợp kịch bản đa ngôn ngữ

#### 3. Mục tiêu tối ưu khác nhau
* Một số tập trung vào hiệu quả nén
* Một số tập trung giữ lại ngữ nghĩa
* Một số tập trung tốc độ xử lý

### Ảnh hưởng thực tế
Cùng một văn bản có thể có số token khác nhau ở các mô hình khác nhau:

```
输入："Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## Mô hình Embedding (Embedding Model) là gì?

**Khái niệm cơ bản:** Mô hình Embedding là kỹ thuật chuyển đổi dữ liệu rời rạc chiều cao (văn bản, hình ảnh...) thành vector liên tục chiều thấp, giúp máy tính hiểu và xử lý dữ liệu phức tạp tốt hơn. Tưởng tượng như chuyển đổi bộ xếp hình phức tạp thành điểm tọa độ đơn giản, nhưng vẫn giữ lại đặc điểm chính. Trong hệ sinh thái mô hình lớn, nó đóng vai trò "phiên dịch viên" chuyển đổi thông tin con người hiểu thành dạng số máy tính xử lý.

**Nguyên lý hoạt động:** Lấy xử lý ngôn ngữ tự nhiên làm ví dụ, mô hình Embedding ánh xạ từ ngữ vào vị trí cụ thể trong không gian vector. Tại không gian này, các từ ngữ nghĩa giống nhau sẽ tự động tập hợp lại gần nhau. Ví dụ:
* Vector "国王" (quốc vương) và "王后" (hoàng hậu) rất gần nhau
* Từ vật nuôi như "猫" (mèo) và "狗" (chó) cũng ở gần
* Còn những từ không liên quan ngữ nghĩa như "汽车" (ô tô) và "面包" (bánh mì) sẽ ở xa nhau

**Kịch bản ứng dụng chính:**
* Phân tích văn bản: Phân loại tài liệu, phân tích cảm xúc
* Hệ thống đề xuất: Đề xuất nội dung cá nhân hóa
* Xử lý hình ảnh: Tìm kiếm hình ảnh tương tự
* Công cụ tìm kiếm: Tối ưu tìm kiếm ngữ nghĩa

**Ưu điểm cốt lõi:**
1. Hiệu ứng giảm chiều: Đơn giản hóa dữ liệu phức tạp thành dạng vector dễ xử lý
2. Duy trì ngữ nghĩa: Giữ lại thông tin ngữ nghĩa chính trong dữ liệu gốc
3. Hiệu quả tính toán: Cải thiện đáng kể tốc độ huấn luyện và suy luận mô hình ML

**Giá trị kỹ thuật:** Mô hình Embedding là thành phần nền tảng của hệ thống AI hiện đại, cung cấp biểu diễn dữ liệu chất lượng cao cho nhiệm vụ học máy, là công nghệ then chốt thúc đẩy phát triển các lĩnh vực như xử lý ngôn ngữ tự nhiên, thị giác máy tính.

***

## Nguyên lý hoạt động của mô hình Embedding trong truy xuất kiến thức

**Quy trình làm việc cơ bản:**

1. **Giai đoạn tiền xử lý cơ sở kiến thức**
* Chia tài liệu thành các chunk (khối văn bản) kích thước phù hợp
* Sử dụng mô hình embedding chuyển đổi mỗi chunk thành vector
* Lưu trữ vector và văn bản gốc vào cơ sở dữ liệu vector

2. **Giai đoạn xử lý truy vấn**
* Chuyển đổi câu hỏi người dùng thành vector
* Truy xuất nội dung tương tự trong thư viện vector
* Cung cấp nội dung liên quan đã truy xuất làm bối cảnh cho LLM

***

## **MCP (Model Context Protocol) là gì?**

MCP là giao thức nguồn mở nhằm cung cấp thông tin ngữ cảnh cho mô hình ngôn ngữ lớn (LLM) theo cách tiêu chuẩn hóa.

* **Hiểu bằng phép loại suy:** Có thể tưởng tượng MCP như "USB" trong lĩnh vực AI. Chúng ta đều biết USB có thể lưu trữ nhiều loại tệp, cắm vào máy tính là sử dụng ngay. Tương tự, MCP Server có thể "cắm" nhiều "plugin" cung cấp ngữ cảnh, LLM có thể yêu cầu các plugin này từ MCP Server khi cần, từ đó thu thập thông tin ngữ cảnh phong phú hơn để tăng cường năng lực.
* **So sánh với Function Tool:** Function Tool (công cụ hàm) truyền thống cũng có thể cung cấp chức năng ngoại vi cho LLM, nhưng MCP giống như sự trừu tượng cấp cao hơn. Function Tool chủ yếu là công cụ cho nhiệm vụ cụ thể, còn MCP cung cấp cơ chế tiếp cận ngữ cảnh mô-đun hóa và tổng quát hơn.

### **Ưu điểm cốt lõi của MCP**

1. **Tiêu chuẩn hóa:** Cung cấp giao diện và định dạng dữ liệu thống nhất, giúp các LLM và nhà cung cấp ngữ cảnh khác nhau hợp tác liền mạch.
2. **Mô-đun hóa:** Cho phép nhà phát triển phân giải thông tin ngữ cảnh thành các mô-đun (plugin) độc lập, tiện quản lý và tái sử dụng.
3. **Linh hoạt:** LLM có thể chọn động plugin ngữ cảnh cần thiết theo nhu cầu, đạt tương tác thông minh và cá nhân hóa hơn.
4. **Khả năng mở rộng:** Thiết kế của MCP hỗ trợ bổ sung nhiều loại plugin ngữ cảnh trong tương lai, mở ra khả năng vô hạn cho việc mở rộng năng lực LLM.