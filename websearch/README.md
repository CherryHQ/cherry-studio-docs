---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

# 联网模式

{% hint style="info" %}
需要联网的场景举例：

* 时效性信息：比如今天/本周/刚刚 黄金期货价格等。
* 实时数据：比如天气，汇率等动态数值。
* 新兴知识：比如新事物，新概念，新技术等等...
{% endhint %}

### 一、如何开启联网

在Cherry Studio 的提问窗口，点击 【小地球】 图标即可开启联网。

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>点击地球图标 - 开启联网</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>表示 - 已开启联网功能</p></figcaption></figure>

### 二、特别注意：联网有两种模式

#### 模式1：模型服务商的大模型自带联网功能

这种情况下，开启联网后，直接就可以使用联网服务了，非常简单。

{% hint style="warning" %}
可以通过问答界面上方，模型名字后面是否带有小地球标记，迅速判断该模型是否支持联网。
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

在模型管理页面，这个方法也可以让你快速分辨出哪些模型支持联网，哪些不支持。

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio 目前已经支持的联网模型服务商有**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter（全部模型支持联网）</mark>
> * <mark style="color:green;">腾讯混元</mark>
> * <mark style="color:green;">智谱AI</mark>
> * <mark style="color:green;">阿里云百炼等</mark>

{% hint style="danger" %}
特别注意：

存在一种特殊的情况，即便模型上没带小地球标记，但是它也能实现联网，比如下面这个攻略教程解释的情况。
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***



#### 模式2：模型不带联网功能，使用 Tavily服务 实现联网功能

当我们使用一个不带联网功能的大模型时（名字后面没有小地球图标），而我们又需要它获取一些实时性的信息进行处理，此时就需要用到Tavily网络搜索服务。

**初次使用Tavily服务**，会弹窗提示去设置一些信息，请根据指引操作即可-非常简单！

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>弹窗，点击：去设置</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>点击获取秘钥</p></figcaption></figure>

点击获取秘钥后，会自动跳转到**tavily的官网**登录注册页面，注册并登录后，创建APIkey，然后复制key到Cherry Studio即可。

{% hint style="danger" %}
不会注册，参考本文档同目录下tavily联网登录注册教程。
{% endhint %}

**tavily注册参考文档：**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

显示下面的界面表示注册成功。

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>复制key</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>粘贴key，大功告成</p></figcaption></figure>

再来试一次看看效果。结果表明，已经正常联网搜索了，并且搜索结果数是我们设置的默认值：5个。

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
注意：tavily 每个月有白嫖限制，超过了要付费\~\~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS：如果发现错误，欢迎大家随时联系。

