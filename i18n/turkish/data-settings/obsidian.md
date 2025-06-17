---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Obsidian Kurulum Rehberi

Cherry Studio, tam diyalogları veya tekli diyalogları Obsidian kütüphanesine aktarmak için Obsidian ile entegrasyonu destekler.

{% hint style="warning" %}
Bu işlem ek Obsidian eklentisi gerektirmez. Ancak Cherry Studio'nun Obsidian'a aktarma mekanizması Obsidian Web Clipper'a benzer olduğundan, kullanıcıların [çok uzun diyaloglarda aktarım hatası](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0) yaşamamak için Obsidian'ı güncel sürüme (en az **1.7.2** üzeri) güncellemeleri önerilir.
{% endhint %}

## Güncel Rehber

{% hint style="info" %}
Eski Obsidian aktarımına kıyasla, yeni sürüm kütüphane yolunu otomatik seçer ve artık kütüphane adı veya klasör adı manuel girilmez.
{% endhint %}

### Adım 1: Cherry Studio'yu Yapılandırma

Cherry Studio'da _Ayarlar_ → _Veri Yönetimi_ → _Obsidian Konfigürasyonu_ menüsünü açın. Açılır menüde bilgisayarınızda açılan Obsidian kütüphaneleri görünecektir. Hedef kütüphanenizi seçin:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Adım 2: Diyalog Aktarma

#### Tam Diyalog Aktarma

Cherry Studio diyalog ekranına dönün, diyaloğa sağ tıklayın, _Aktar_ seçeneğini ve ardından _Obsidian'a Aktar_ seçeneğini tıklayın:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Not özelliklerini (**Properties**), klasör konumunu ve işleme yöntemini ayarlamak için bir pencere açılacaktır:

* **Kütüphane**: Diğer kütüphaneleri seçmek için açılır menü
* **Yol**: Aktarılacak notun kaydedileceği klasör
* Obsidian not özellikleri (Properties):
  * Etiketler (tags)
  * Oluşturulma zamanı (created)
  * Kaynak (source)
* Aktarım yöntemleri:
  * **Yeni oluştur (varsa üzerine yaz)**: Belirtilen klasörde yeni not oluşturur, aynı isimde not varsa üzerine yazar
  * **Önüne ekle**: Aynı isimde not varsa, içeriği mevcut notun başına ekler
  * **Sonuna ekle**: Aynı isimde not varsa, içeriği mevcut notun sonuna ekler

{% hint style="info" %}
Yalnızca ilk yöntem Properties (özellikler) ekler, diğer yöntemler eklemez.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Not özelliklerini yapılandırma</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Yol seçimi</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>İşlem yöntemi seçimi</p></figcaption></figure>

Seçimleri tamamladıktan sonra "Onayla" butonuna tıklayarak diyalogu belirtilen Obsidian klasörüne aktarın.

#### Tekli Diyalog Aktarma

Tek bir diyalog aktarmak için diyalog altındaki _üç çizgi menüsünü_ tıklayın, _Aktar_ ve ardından _Obsidian'a Aktar_ seçeneğini seçin:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Tekli diyalog aktarma</p></figcaption></figure>

Tam diyalog aktarmadakiyle aynı pencere açılacak ve [yukarıdaki rehberdeki](obsidian.md#dao-chu-wan-zheng-dui-hua) adımları izleyerek not özelliklerini ve işlem yöntemini seçebilirsiniz.

### Başarıyla Aktarıldı

🎉 Tebrikler! Cherry Studio-Obsidian entegrasyonunu tamamladınız ve aktarım sürecini başarıyla uyguladınız. Keyfini çıkarın!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidian'a aktarma</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Sonucu görüntüleme</p></figcaption></figure>

***

## Eski Rehber (Cherry Studio\<v1.1.13 sürümleri için)

### Adım 1: Obsidian Hazırlığı

Obsidian kütüphanesini açın ve aktarılan diyalogları saklamak için bir `klasör` oluşturun (örnekte Cherry Studio klasörü):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Sol altta işaretlenen `kütüphane` adını not edin.

### Adım 2: Cherry Studio Yapılandırması

Cherry Studio'daki _Ayarlar_ → _Veri Yönetimi_ → _Obsidian Konfigürasyonu_ menüsüne [Adım 1](obsidian.md#di-yi-bu)'den alınan `kütüphane` ve `klasör` adlarını girin:

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

İsteğe bağlı `Genel etiketler` alanına, tüm diyaloglar için Obsidian etiketleri tanımlayabilirsiniz.

### Adım 3: Diyalog Aktarma

#### Tam Diyalog Aktarma

Cherry Studio diyalog ekranına dönün, diyaloğa sağ tıklayarak _Aktar_ → _Obsidian'a Aktar_ seçin.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Tam diyalog aktarma</p></figcaption></figure>

Not özelliklerini (**Properties**) ve işlem yöntemini ayarlayan pencere açılacaktır:
* **Yeni oluştur (varsa üzerine yaz)**: [Adım 2](obsidian.md#di-er-bu)'de belirtilen klasörde yeni not oluşturur
* **Önüne ekle**: İçeriği mevcut notun başına ekler
* **Sonuna ekle**: İçeriği mevcut notun sonuna ekler

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Not özelliklerini yapılandırma</p></figcaption></figure>

{% hint style="info" %}
Yalnızca ilk yöntem Properties (özellikler) ekler.
{% endhint %}

#### Tekli Diyalog Aktarma

Tekli diyalog için diyalog altındaki _üç çizgi menüsünü_ tıklayıp _Aktar_ → _Obsidian'a Aktar_ seçin.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Tekli diyalog aktarma</p></figcaption></figure>

[Yukarıdaki rehberdeki](obsidian.md#dao-chu-wan-zheng-dui-hua) adımları takip ederek ayarları tamamlayın.

### Başarıyla Aktarıldı

🎉 Tebrikler! Cherry Studio-Obsidian entegrasyonunu tamamladınız ve aktarım sürecini başarıyla uyguladınız. Keyfini çıkarın!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidian'a aktarma</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Sonucu görüntüleme</p></figcaption></figure>