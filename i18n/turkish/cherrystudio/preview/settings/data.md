---
icon: database
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Veri Ayarları

Bu arayüz, istemci verilerinin bulut ve yerel yedeklemesi, yerel veri dizini sorgulama ve önbellek temizleme gibi işlemleri yapmanızı sağlar.

### Veri Yedekleme

Şu an veri yedekleme yalnızca WebDAV yöntemi ile desteklenmektedir. Bulut yedekleme için WebDAV destekleyen bir hizmet seçebilirsiniz.

Ayrıca çoklu uç veri senkronizasyonunu gerçekleştirmek için `A Bilgisayarı` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restore}}$$ `B Bilgisayarı` yöntemini kullanabilirsiniz.

#### Nutstore Örneği

1. Nutstore'a giriş yapın, sağ üstteki kullanıcı adınıza tıklayın ve "Hesap Bilgileri"ni seçin:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "Güvenlik Seçenekleri"ni seçin, "Uygulama Ekle"ye tıklayın

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Uygulama adını girin, rastgele şifre oluşturun;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Şifreyi kopyalayın ve kaydedin;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Sunucu adresini, hesabı ve şifreyi alın;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio ayarlarında — Veri Ayarları bölümünde, WebDAV bilgilerini doldurun;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Veri yedeklemeyi veya geri yüklemeyi seçin ve otomatik yedekleme zaman periyodunu ayarlayabilirsiniz.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV hizmeti için erişim eşiği düşük olan genellikle bulut depolama hizmetleridir:

* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (Üyelik gereklidir)
* [Aliyundrive](https://www.alipan.com/) (Satın alma gereklidir)
* [Box](https://www.box.com/) (Ücretsiz depolama alanı 10GB, tek dosya boyutu sınırı 250MB.)
* [Dropbox](https://www.dropbox.com/) (Dropbox ücretsiz 2GB, arkadaş davet ederek 16GB'a kadar genişletebilirsiniz.)
* [TeraCloud](https://teracloud.jp/en/) (Ücretsiz alan 10GB, ayrıca davet yoluyla 5GB ekstra alan alabilirsiniz.)
* [Yandex Disk](https://disk.yandex.com/) (Ücretsiz kullanıcılar için 10GB kapasite.)

Ayrıca, kendi kendine dağıtım gerektiren bazı hizmetler:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}