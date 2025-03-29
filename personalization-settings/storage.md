---
icon: floppy-disk
---

# 修改存储位置

Cherry Studio 数据存储遵循系统规范，数据会自动放在用户目录下，具体目录位置如下：

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio
>
> Linux: /home/username/.config/CherryStudio

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

如果希望能够修改存储位置，可以通过创建软连接的方式来实现。将软件退出，然后把数据移动到你希望保存的位置，然后在原位置创建一个链接指向移动后的位置即可。

具体操作步骤可以参考：[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)
