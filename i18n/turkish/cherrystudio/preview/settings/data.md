---
icon: database
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Veri Ayarları

Bu arayüz, istemci verilerinin bulut ve yerel yedeklemesi, yerel veri dizini sorgulama ve önbellek temizleme gibi işlemleri yapmanızı sağlar.

### Veri Yedekleme

Şu anda veri yedekleme yalnızca WebDAV yöntemiyle desteklenmektedir. Bulut yedekleme için WebDAV destekleyen bir hizmet seçebilirsiniz.

Ayrıca, `A bilgisayarı $$\xrightarrow{\text{backup}}$$ WebDAV $$\xrightarrow{\text{geri yükleme}}$$ B bilgisayarı` şeklinde çoklu cihaz veri senkronizasyonu gerçekleştirebilirsiniz.

#### Jianyun Örneği

1. Jianyun'a giriş yapın, sağ üst köşedeki kullanıcı adına tıklayın ve "Hesap Bilgileri"ni seçin:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "Güvenlik Seçenekleri"ni seçin ve "Uygulama Ekle"ye tıklayın

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Uygulama adını girin ve rastgele parola oluşturun;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Parolayı kopyalayın ve kaydedin;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Sunucu adresini, kullanıcı adını ve parolayı alın;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio Ayarlar > Veri Ayarları bölümünde WebDAV bilgilerini doldurun;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Verileri yedekleme veya geri yükleme seçeneğini belirleyin ve otomatik yedekleme zaman aralığını ayarlayabilirsiniz.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV hizmetleri için genellikle düşük eşikli seçenekler bulut depolama hizmetleridir:

* [Jianyun](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (üyelik gereklidir)
* [Alibaba Cloud Drive](https://www.alipan.com/) (satın alma gereklidir)
* [Box](https://www.box.com/) (Ücretsiz depolama alanı 10GB, tek dosya boyutu sınırı 250MB'dır)
* [Dropbox](https://www.dropbox.com/) (Dropbox ücretsiz 2GB alan sunar, arkadaş davet ederek 16GB'a kadar genişletebilirsiniz)
* [TeraCloud](https://teracloud.jp/en/) (10GB ücretsiz alan, davet yoluyla ek 5GB alan kazanabilirsiniz)
* [Yandex Disk](https://disk.yandex.com/) (Ücretsiz kullanıcılar için 10GB alan sağlar)

İkinci olarak kendi dağıtımınızı yapmanız gereken hizmetler:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}