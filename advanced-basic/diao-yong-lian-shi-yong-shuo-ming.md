---
icon: route
---

# 调用链使用说明

## 功能介绍

调用链（又称“trace”）为用户提供对话的洞察能力，帮助用户觉察模型、知识库、MCP、网络搜索等在对话过程中的具体表现。它是一个基于 [OpenTelemetry](https://opentelemetry.io/docs/languages/js/) 实现的可观测工具，通过端侧采集、存储、处理数据实现可视化，为定位问题、优化效果提供量化评估依据。

每次对话对应一条 trace 数据，一条 trace 由多个 span 组成，每个 span 对应 Cherry Studio 的一个程序处理逻辑如调用模型会话、调用 MCP 、调用知识库、调用网络搜索等。trace 以树结构展示，span 为树节点，主要数据包括耗时、token 使用量，当然在 span 详情还可以查看其具体的输入输出。

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

## 开启 Trace

默认情况下，Cherry Studio 安装之后，Trace 是隐藏的状态。需要在 "设置"-"常规设置" - "开发者模式" 中开启，如下图：

<figure><img src="https://static.moblin.net/waken-feishuhelper/RHYcbRY6co8TlKxhCbxcjWisn1g?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023236Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=8e2b18e403fffedc599959f05841acfc1ee7a5bb0ee98eb73fe49a714f585166" alt=""><figcaption></figcaption></figure>

且对于之前的会话不会产生 Trace 记录，只会在新的问答产生之后才会产生 Trace 记录。所产生的记录存储在本地，如需要彻底清除 Trace ，可以通过 "设置" - "数据设置" - "数据目录" - "清除缓存" 进行清除，也可通过手动 删除 \~/.cherrystudio/trace 下的文件进行清除，如下图：

<figure><img src="https://static.moblin.net/waken-feishuhelper/OwWMbElUkokG0PxMSENcNgIanDh?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023236Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=30b3519fb068d7e87c05c07670281e3e211c18ff48348a387de444d40b978728" alt=""><figcaption></figcaption></figure>

## 场景介绍

### 全链路查看

在 Cherry Studio 对话框中点击调用链查看调用链的全链路数据。无论在对话过程中调用了模型，还是网络搜索、知识库、MCP，都可以在调用链窗口中查看到全链路调用数据。

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://static.moblin.net/waken-feishuhelper/INIqbz5BAoQNGKx1r0ccnqqyn8f?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023237Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=5abe0a0a8d9a188f033522ee54970d94698fdeee25b019822bd3a630c7bb5d09" alt=""><figcaption></figcaption></figure>

### 查看链路中模型

若想要查看调用链中模型的详情，可以点击模型调用节点，查看其输入、输出详情。

<figure><img src="https://static.moblin.net/waken-feishuhelper/N73RbLZbAoIPpTxqnjrcMDpCnTh?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023238Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=00b50bede11f9f306f6045e1c220252cb365764d221adb34d382d22261aadd94" alt=""><figcaption></figcaption></figure>

<figure><img src="https://static.moblin.net/waken-feishuhelper/MZ7lbD5KIo1zl1xIVMCcyQr9nFh?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023238Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=bbecc0e549ffe3a4ba359086a7f9556e4b62207bc9452cb800b25fcfef589414" alt=""><figcaption></figcaption></figure>

<figure><img src="https://static.moblin.net/waken-feishuhelper/HoPxbbhuloIOuZx4IzVcfzawnWf?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023238Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=5a3ccc7df5e3cb71ff6a5fe99338c4c6237edd0b67edfc464d89caf1d0b71552" alt=""><figcaption></figcaption></figure>

### 查看链路中网络搜索

若想要查看调用链中网络搜索的详情，可以点击网络搜索调用节点，查看其输入、输出详情。在详情中，可以查看到调用网络搜索查询的问题和其返回的结果。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://static.moblin.net/waken-feishuhelper/PAAnbTX4woDXcdx2jQEcvKJcnTg?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023237Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=6f3ea476935bd8da52106cd4f0510ec558c41a545ce3602828d78fede4df7159" alt=""><figcaption></figcaption></figure>

<figure><img src="https://static.moblin.net/waken-feishuhelper/DSC9bINDDoGFg9xpLeXca0HYnDg?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023237Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=9c0a87cf4c6c5ee9497cd5fea2d083d26c52ab9c135ed0ff3e296d752bbbad40" alt=""><figcaption></figcaption></figure>

### 查看链路中知识库

若想要查看调用链中知识库的详情，可以点击知识库调用节点，查看其输入、输出详情。在详情中，可以查看到调用知识库查询的问题和其返回的答案。

<figure><img src="https://static.moblin.net/waken-feishuhelper/ICZ2bQXJcocB4lxWkp7cpSgNntY?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023238Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=18e10d6ac70ba02352d39605406e9aa302fe6a73061f89243e136dde637955e6" alt=""><figcaption></figcaption></figure>

### 查看链路中 MCP 调用情况

若想要查看调用链中 MCP 的详情，可以点击 MCP 调用节点，查看其输入、输出详情。在详情中，可以查看到调用此 MCP Server tool 的入参和 tool 的返回。

<figure><img src="https://static.moblin.net/waken-feishuhelper/AiMXbqpWEoMmLJxqTbxcuf3mnLg?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023238Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=0321ec7e321606252622b638512a8af97b4f449b79a3c27ddad0b7b20c316547" alt=""><figcaption></figcaption></figure>

<figure><img src="https://static.moblin.net/waken-feishuhelper/Dn32bKxoao0160xZXLccx6eynUl?X-Amz-Algorithm=AWS4-HMAC-SHA256&#x26;X-Amz-Credential=sBtm1lOXfha5fQNt%2F20250730%2Fus-east-1%2Fs3%2Faws4_request&#x26;X-Amz-Date=20250730T023239Z&#x26;X-Amz-Expires=129600&#x26;X-Amz-SignedHeaders=host&#x26;X-Amz-Signature=93461b7c9c16cd20f5af4c66b73dde99db2a91bd41f60c232e54b68c92d53703" alt=""><figcaption></figcaption></figure>

## 问题和建议

当前功能由阿里云 [EDAS](https://www.aliyun.com/product/edas) 团队提供，如有问题或建议，请进入钉钉群 （ 群号： 21958624 ） 与开发者进行深度沟通。

\
