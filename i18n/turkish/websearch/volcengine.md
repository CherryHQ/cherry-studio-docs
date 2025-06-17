---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# VolcEngine Çevrimiçi Erişim

### 1、 「火山引擎」 Hesabına Giriş/Kayıt <a href="#rclz7" id="rclz7"></a>

Resmi web sitesini ziyaret edin: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>VolcEngine Resmi Web Sitesi</p></figcaption></figure>

### 2、「Çevrimiçi Erişimli」 「Uygulamamı」 Oluşturun <a href="#gvzaa" id="gvzaa"></a>

2.1、 VolcEngine'e giriş yapın,「Volc方舟」 sayfasına gidin: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2、 **Sırasıyla tıklayın:** <mark style="color:red;">**「Uygulamalarım」 - 「Uygulama Oluştur」 - 「Sıfır Kod」 - 「Bire Bir Sohbet」**</mark>&#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3、 Bilgileri Doldurun ve Uygulamayı Yayınlayın <a href="#zzdfe" id="zzdfe"></a>

**Uygulama Adı**: İstediğiniz bir isim verebilirsiniz.（<mark style="color:red;">**\*Zorunlu**</mark> alan, diğerleri boş bırakılabilir）

<mark style="color:red;">**Önemli nokta: Çevrimiçi eklentiyi etkinleştirin (önce etkinleştirmeniz gerekir)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1、 Çevrimiçi Eklenti İşlevini Etkinleştirin（Ücretler ve ücretsiz kotaya dikkat） <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Hemen Satın Al'ı tıklayın, adımları takip edin. Aşağıdaki arayüz görüntülendiğinde etkinleştirme başarılıdır.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Durumu kontrol edin, bu noktada başarıyla etkinleştirildi</p></figcaption></figure>

Ardından önceki「Uygulama Bilgilerini Doldur」ekranına dönün ve işleme devam edin.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2、 Çevrimiçi Arama「Gelişmiş Yapılandırma」Açıklaması <a href="#sp6uz" id="sp6uz"></a>

İhtiyaca göre seçim yapın, kişisel öneriler:

* Girdi ve çıktı üzerinde hassas kontrol istiyorsanız「**Özel Çağrı**」 kullanabilirsiniz;
* Uğraşmak istemiyorsanız değiştirmeden「**Otomatik Çağrı**」- varsayılan değer kullanın;
* Paranız çoksa ve bilginin güncelliği çok önemliyse「**Zorunlu Etkinleştir**」 seçeneğini kullanın.

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3、 Uygulamayı Yayınlayın <a href="#fe1gf" id="fe1gf"></a>

Sağ üstteki「Yayınla」 düğmesine tıklayın, uygulama başarıyla oluşturulur.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4、 API Anahtarını Alın <a href="#jtqlu" id="jtqlu"></a>

Sırasıyla tıklayın: **「API Çağrı Kılavuzu」-「API Anahtarını Seç ve Kopyala」-「Görüntüle ve Seç」**

API anahtarını kopyalayın, Cherry Studio'da kullanmak üzere saklayın. (Detaylar aşağıdaki arayüzde)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Not: API anahtarınız yoksa, açılır pencere sağ üst köşesindeki - 「**API Anahtarı Oluştur**」 seçeneğini kullanıp anahtarı kopyalayın.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5、 Cherry Studio'da API Anahtarı ile deepseek-R1'e Çevrimiçi Erişim <a href="#lrefj" id="lrefj"></a>

#### 5.1、 Cherry studio'yu açın -「Ayarlar」-「Herhangi bir isim yazın」-「Tür: openAI」<a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2、 URL ve Anahtarı Yapılandırın <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Dikkat: Adres bulunamazsa veya Pekin düğümü değilse, tam adresi buradan bulabilirsiniz, unutmayın: “/” eklemeyi atlamayın:</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3、 Model Adını Ekleyin <a href="#qmh3i" id="qmh3i"></a>

Dikkat: Model adı olarak altındaki küçük yazıyı kopyalayın, aksi halde hata alırsınız.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6、 Önizleme Efekti <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>