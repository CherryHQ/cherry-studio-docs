
{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Cài đặt tự động MCP

> Cài đặt tự động MCP yêu cầu nâng cấp Cherry Studio lên phiên bản v1.1.18 trở lên.

## Giới thiệu tính năng

Ngoài cài đặt thủ công, Cherry Studio còn tích hợp sẵn công cụ `@mcpmarket/mcp-auto-install`, đây là cách cài đặt máy chủ MCP thuận tiện hơn. Bạn chỉ cần nhập lệnh tương ứng vào cuộc hội thoại mô hình lớn hỗ trợ dịch vụ MCP.

{% hint style="warning" %}
**Lưu ý giai đoạn thử nghiệm:**
* `@mcpmarket/mcp-auto-install` hiện vẫn đang trong giai đoạn thử nghiệm
* Hiệu quả phụ thuộc vào "chỉ số thông minh" của mô hình lớn, một số sẽ tự động thêm, một số **vẫn cần thay đổi thủ công một số tham số trong cài đặt MCP**
* Hiện tại nguồn tìm kiếm là từ @modelcontextprotocol, có thể tự cấu hình (xem hướng dẫn bên dưới)
{% endhint %}

## Hướng dẫn sử dụng

Ví dụ, bạn có thể nhập:
```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Nhập lệnh cài đặt máy chủ MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Giao diện cấu hình máy chủ MCP</p></figcaption></figure>

Hệ thống sẽ tự động nhận diện nhu cầu của bạn và hoàn tất cài đặt thông qua `@mcpmarket/mcp-auto-install`. Công cụ này hỗ trợ nhiều loại máy chủ MCP, bao gồm nhưng không giới hạn:
* filesystem (hệ thống tệp)
* fetch (yêu cầu mạng)
* sqlite (cơ sở dữ liệu)
* v.v...

> Biến MCP_PACKAGE_SCOPES có thể tùy chỉnh nguồn tìm kiếm dịch vụ MCP, giá trị mặc định là: `@modelcontextprotocol`, có thể cấu hình tùy chỉnh.

## Giới thiệu thư viện `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Tham khảo cấu hình mặc định:**

```json
// `axun-uUpaWEdMEMU8C61K` là id dịch vụ, tùy chỉnh theo ý muốn
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "Xem chi tiết tại https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` là một gói npm nguồn mở, bạn có thể xem thông tin chi tiết và tài liệu sử dụng tại [kho chính thức npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` là bộ sưu tập dịch vụ MCP chính thức của Cherry Studio.
{% endhint %}