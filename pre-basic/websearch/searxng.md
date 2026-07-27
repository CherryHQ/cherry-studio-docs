---
description: 部署可供 Cherry Studio V2 使用的 SearXNG 实例，并完成 JSON、搜索引擎和基础认证配置。
icon: searchengin
---

# SearXNG 本地部署与配置

SearXNG 是开源的元搜索引擎，可以把多个搜索引擎的结果汇总到自己的实例中。Cherry Studio V2 可将自托管的 SearXNG 设为关键词搜索服务商，适合重视可控性和隐私、并具备基础容器运维能力的用户。

{% hint style="info" %}
SearXNG 软件本身开源，但实例运行仍会占用本机或服务器资源；它所调用的上游搜索引擎也可能有各自的访问限制。自托管不等于搜索质量、可用性或匿名性自动得到保证。
{% endhint %}

## 选择 SearXNG 前先了解

与直接填写 API Key 的搜索服务不同，使用 SearXNG 需要先准备一个可访问的实例。

| 方案 | 适用场景 | 注意事项 |
| --- | --- | --- |
| 本机部署 | 个人使用、快速体验 | 只有本机可以直接访问，电脑关机后停止服务 |
| 局域网部署 | 多台可信设备共用 | 需要正确配置监听地址和防火墙 |
| 公网自托管 | 跨网络或团队使用 | 必须考虑 HTTPS、认证、限流、更新和日志 |
| 公共实例 | 临时测试 | 可能关闭 JSON API、限制频率或随时不可用 |

不建议把陌生公共实例作为长期默认服务商。实例管理员可能看到查询和连接信息，且公共实例通常无法提供稳定性承诺。

## Cherry Studio 对实例的要求

一个可用的 SearXNG 实例需要满足：

- Cherry Studio 所在设备能够访问实例地址；
- `/config` 能返回实例配置；
- `/search` 允许 `format=json`；
- 至少有一个已启用的搜索引擎同时属于 `general` 和 `web` 分类；
- 搜索结果中的网页允许从 Cherry Studio 所在网络访问；
- 如果反向代理启用了 HTTP Basic Auth，需在 Cherry Studio 中填写相同凭证。

Cherry Studio 默认使用：

```text
http://localhost:8080
```

这只是预设地址。实际端口和域名必须与自己的部署一致。

## 使用官方容器模板部署

SearXNG 官方推荐使用 Docker 或 Podman 的 Compose 模板。以下步骤适合已经安装 Docker 与 Docker Compose 的用户；生产环境还需自行完成备份、更新和访问控制。

### 1. 准备目录和模板

```bash
mkdir -p ./searxng/core-config
cd ./searxng
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example
cp .env.example .env
```

打开 `.env`，按模板说明检查端口、实例地址和密钥等设置。模板可能随 SearXNG 更新，首次部署或升级前应阅读[官方容器安装文档](https://docs.searxng.org/admin/installation-docker.html)。

### 2. 开启 JSON 输出

在 `core-config/settings.yml` 中至少加入：

```yaml
use_default_settings: true

search:
  formats:
    - html
    - json
```

{% hint style="warning" %}
Cherry Studio 会请求 `format=json`。如果 SearXNG 的 `search.formats` 没有 `json`，搜索接口通常会返回 `403 Forbidden`。
{% endhint %}

如果已有 `settings.yml`，请合并 `json` 项，不要用上面的最小示例覆盖原有引擎、代理、语言或安全配置。

### 3. 启动实例

```bash
docker compose up -d
docker compose ps
```

如需查看日志：

```bash
docker compose logs -f core
```

服务名称可能随官方模板调整。如果日志命令提示找不到 `core`，先执行 `docker compose ps`，再使用实际服务名。

### 4. 验证实例

先在浏览器中打开实例首页，再通过终端验证 JSON API。假设地址是 `http://127.0.0.1:8080`：

```bash
curl "http://127.0.0.1:8080/config"
curl "http://127.0.0.1:8080/search?q=Cherry+Studio&format=json"
```

两个请求都应返回 JSON。第二个响应还应包含可用搜索结果。

SearXNG 的接口和参数说明见[Search API](https://docs.searxng.org/dev/search_api.html)。

## 在 Cherry Studio 中配置

### 1. 打开 SearXNG 设置

进入：

> **设置 → 网络搜索 → SearXNG**

### 2. 填写 API Host

填写实例的根地址，不要手动附加 `/search` 或 `/config`。

本机示例：

```text
http://127.0.0.1:8080
```

公网示例：

```text
https://search.example.com
```

Cherry Studio 会自行拼接 `/config` 和 `/search`。

{% hint style="info" %}
桌面版 Cherry Studio 直接运行在宿主系统中。Docker 已把端口映射到宿主机时，通常使用 `127.0.0.1:映射端口`，不需要使用 `host.docker.internal`。
{% endhint %}

### 3. 填写基础认证

如果反向代理配置了 HTTP Basic Auth：

1. 在 SearXNG 设置中填写用户名；
2. 填写对应密码；
3. 不要把 `用户名:密码` 写进 API Host。

只要用户名非空，Cherry Studio 就会对 `/config`、`/search` 和检测请求发送 Basic Auth 请求头。

HTTP Basic Auth 必须与 HTTPS 配合用于公网连接。仅使用 Basic Auth 而不使用 HTTPS，凭证可能在传输中被窃取。

### 4. 检查连接

点击**检查**按钮。

检查成功后，将 SearXNG 设为默认关键词搜索服务商。然后在对话中开启地球图标即可使用。

## Cherry Studio 如何选择搜索引擎

如果没有保存过单独的引擎列表，Cherry Studio 会读取：

```text
GET /config
```

并选择同时满足以下条件的引擎：

- `enabled` 为 `true`；
- `categories` 包含 `general`；
- `categories` 包含 `web`。

随后，应用会发起类似请求：

```text
GET /search?q=查询内容&language=auto&format=json&engines=引擎列表
```

因此，在 SearXNG 网页端更改一次性的搜索偏好，不一定会改变 Cherry Studio 的请求。应在实例的 `settings.yml` 中长期启用合适的引擎和分类。

### 只保留指定引擎

如果某些上游引擎在当前网络不可访问，可以在 `settings.yml` 中调整引擎。示意配置：

```yaml
use_default_settings:
  engines:
    keep_only:
      - duckduckgo
      - wikipedia
```

引擎名称、可用性和配置项会随 SearXNG 更新。请先在实例的 `/config` 或偏好设置中确认准确名称，并参考[引擎配置文档](https://docs.searxng.org/admin/settings/settings_engines.html)。

{% hint style="warning" %}
不要直接照搬不适合自己网络的固定引擎清单。搜索引擎可能按地区限制访问、触发验证码或改变接口，最终结果应以实例日志和实际搜索为准。
{% endhint %}

## 搜索结果与网页读取

SearXNG 返回标题、摘要和 URL 后，Cherry Studio 会尝试读取结果网页正文，并只保留成功读取的内容。

这意味着：

- 最大结果数会限制应用处理的候选 URL 数量；
- 某些网页需要登录、阻止自动访问或在当前网络不可达时，读取可能失败；
- 若所有候选网页都读取失败，本次搜索可能报错或没有可用结果；
- SearXNG 设置仍属于关键词搜索服务商；单独粘贴 URL 时使用的默认 URL 读取服务商仍需在网络搜索设置中另行选择。

## 公网部署的安全建议

不要把未保护的 SearXNG 管理和搜索接口直接暴露到公网。

至少应考虑：

- 使用可信证书启用 HTTPS；
- 在反向代理层配置访问认证；
- 保留合理的限流和机器人防护；
- 限制管理端口和不必要的网络入口；
- 定期更新 SearXNG、容器镜像和反向代理；
- 避免在访问日志中长期保存敏感查询；
- 只向可信用户提供凭证，并定期轮换。

Cherry Studio 当前支持 HTTP Basic Auth，但不会替你完成服务器端的 TLS、权限和限流配置。

## 常见问题

### 检查返回 403

最常见原因是 JSON 输出没有开启。确认 `settings.yml` 包含：

```yaml
search:
  formats:
    - html
    - json
```

保存后重启实例，再直接访问 `/search?q=test&format=json` 验证。

公共实例也可能主动关闭 JSON API，此时只能更换实例或自行部署。

### 检查返回 401

实例或反向代理要求认证：

- 在 Cherry Studio 中填写正确的 Basic Auth 用户名和密码；
- 确认反向代理保护 `/config` 和 `/search` 时使用同一组凭证；
- 检查用户名、密码是否包含误复制的空格；
- 不要把凭证拼进 URL。

### 提示没有可用的 general/web 引擎

Cherry Studio 从 `/config` 中没有找到同时属于 `general` 与 `web` 的已启用引擎。

检查：

1. `/config` 是否正常返回 `engines`；
2. 目标引擎是否为 `enabled: true`；
3. `categories` 是否同时包含 `general` 和 `web`；
4. 配置修改后是否已重启或重载实例。

### 搜索超时或结果不稳定

查看 SearXNG 日志，重点检查：

- 上游搜索引擎是否返回 403、429 或验证码；
- DNS、代理和服务器出口网络是否正常；
- 实例的请求超时是否过短；
- 选中的引擎是否适合当前地区；
- Cherry Studio 所在设备是否能打开搜索结果网页。

不要直接关闭所有限流和安全保护。先判断限制发生在 SearXNG、反向代理、上游引擎还是本机网络。

### 浏览器能搜索，Cherry Studio 仍失败

浏览器页面默认使用 HTML，而 Cherry Studio 要求 JSON。分别测试：

```text
/config
/search?q=test&format=json
```

还需确认 API Host 只填写根地址、Basic Auth 正确，以及反向代理没有单独拦截这两个路径。

### 返回结果，但回答没有引用

可能是结果页正文读取失败，或模型没有正确使用搜索结果。可以：

- 减少不可访问或登录受限的搜索引擎；
- 提高最大结果数后重试；
- 更换更适合当前网络的引擎；
- 在问题中明确要求列出来源；
- 检查模型是否支持工具调用。

## 更新与维护

更新服务前，先阅读 SearXNG 的迁移说明并备份 `.env` 与 `core-config`。使用容器部署时，通常需要更新官方模板并拉取新镜像；不要假设旧版 Compose 文件永远兼容。

官方资料：

- [SearXNG 容器安装](https://docs.searxng.org/admin/installation-docker.html)
- [SearXNG `settings.yml`](https://docs.searxng.org/admin/settings/settings.html)
- [搜索输出格式](https://docs.searxng.org/admin/settings/settings_search.html)
- [管理 API `/config`](https://docs.searxng.org/admin/api.html)
- [SearXNG GitHub](https://github.com/searxng/searxng)

## 相关文档

- [网络搜索](README.md)
- [免费联网模式](free-search.md)
- [网络搜索黑名单](blacklist.md)

***

### 获取帮助与提交反馈

如果在配置或使用过程中遇到问题，请通过[反馈与建议](../../question-contact/suggestions.md)中列出的官方渠道提交反馈。请附上 Cherry Studio 版本、SearXNG 版本、错误码以及脱敏后的日志，但不要提交真实域名凭证或认证密码。
