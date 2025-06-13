---
icon: trash-xmark
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# CSS Ayarlarını Temizleme

{% hint style="warning" %}
Yanlış CSS ayarı yapıldığında veya CSS ayarlandıktan sonra ayar arayüzüne erişilemediğinde, CSS ayarlarını temizlemek için bu yöntemi kullanın.
{% endhint %}

* Konsolu açın, CherryStudio penceresine tıklayın ve <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> kısayolunu kullanın (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* Açılan konsol penceresinde `Console` sekmesine tıklayın

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* Daha sonra `document.getElementById('user-defined-custom-css').remove()` komutunu elle girin (kopyalayıp yapıştırmak genellikle çalışmaz).
* Komutu girip Enter tuşuna basarak CSS ayarlarını temizleyin. Ardından CherryStudio'nun görüntü ayarlarına geri dönerek sorunlu CSS kodunu silin.