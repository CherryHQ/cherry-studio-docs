# 华为云

一、到[华为云](https://auth.huaweicloud.com/authui/login)创建账号登录

二、点击[此链接](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage)，进入Maa S控制台

三、授权

<details>

<summary>授权步骤（已授权跳过）</summary>

1. 进入(二)的链接页面后，根据提示进入授权页面(点击IAM子用户→新增委托→普通用户)

![](<../../.gitbook/assets/image (49) (1).png>)

2. 点击创建后重新返回(二)处链接页面
3. 会提示访问权限不足，点击提示里的"点击此处"
4. 追加已有授权并确定

![](<../../.gitbook/assets/image (50) (1).png>)

注意：该方法适用于小白，不用看过多内容，只需要根据提示点击，如果你可以一次性授权成功按照自己的方式来即可。

</details>

四、点击侧栏鉴权管理，创建API Key（秘钥）并复制

<figure><img src="../../.gitbook/assets/微信截图_20250214034650 (1).png" alt=""><figcaption></figcaption></figure>

然后在CherryStudio里创建新服务商

<figure><img src="../../.gitbook/assets/image (1) (2) (2).png" alt="" width="300"><figcaption></figcaption></figure>

创建完成后填入秘钥

五、点击侧栏模型部署，全部领取

<figure><img src="../../.gitbook/assets/微信截图_20250214034751 (1).png" alt=""><figcaption></figcaption></figure>

六、点击调用

<figure><img src="../../.gitbook/assets/image (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

把①处的地址复制，粘贴到CherryStudio的服务商地址当中并在结尾加上“#”号

并在结尾加上“#”号

并在结尾加上“#”号

并在结尾加上“#”号

并在结尾加上“#”号

为什么加“#”号[看这里](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> 当然也可以不看那里，直接按照教程操作即可；
>
> 也可以使用删除v1/chat/completions的方法填写，只要会填按照自己方法怎么填都行，不会填务必按照教程操作。

<figure><img src="../../.gitbook/assets/image (2) (3) (1).png" alt=""><figcaption></figcaption></figure>

然后把②处模型名称复制，到CherryStudio当中点“+添加”按钮新建模型

<figure><img src="../../.gitbook/assets/image (4) (3) (1).png" alt=""><figcaption></figcaption></figure>

输入模型名称，不要添油加醋，不要带引号，示例当中怎么写就怎么抄。

<figure><img src="../../.gitbook/assets/image (3) (3) (1).png" alt=""><figcaption></figcaption></figure>

点击添加模型按钮即可添加完成。

{% hint style="info" %}
在华为云当中由于每个模型的地址不一样，所以每个模型都需要新建一个服务商，按照以上步骤重复操作即可。
{% endhint %}
