
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# GitHub Copilot

GitHub Copilot'u kullanmak için önce bir GitHub hesabınızın olması ve GitHub Copilot hizmetine abone olmanız gerekir. Ücretsiz sürüm de kullanılabilir ancak bu sürüm en yeni Claude 3.7 modelini desteklemez. Detaylar için [GitHub Copilot resmi sitesine](https://github.com/features/copilot) bakınız.

## Device Code Alma

"GitHub'a giriş yap"ı tıklayarak Device Code alın ve kopyalayın.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Device Code Alma Örnek Görsel"><figcaption><p>Device Code Alma</p></figcaption></figure>

## Device Code'u Tarayıcıda Girip Yetkilendirme

Device Code başarıyla alındıktan sonra, bağlantıyı tıklayarak tarayıcıyı açın. GitHub hesabınıza giriş yapın, Device Code'u girip yetki verin.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="GitHub Yetkilendirme Örnek Görsel"><figcaption><p>GitHub Yetkilendirme</p></figcaption></figure>

Yetkilendirme başarılı olduktan sonra Cherry Studio'ya dönün. "GitHub'a bağlan"ı tıklayın; başarılı olursa GitHub kullanıcı adınız ve profiliniz görünecektir.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="GitHub Bağlantısı Başarılı Örnek Görsel"><figcaption><p>GitHub Bağlantısı Başarılı</p></figcaption></figure>

## "Yönet" Butonuyla Model Listesini Alma

Aşağıdaki "Yönet" butonuna tıklayın; otomatik olarak şu an desteklenen modellerin listesi getirilecektir.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Yönet Butonuyla Model Listesi Alma Örnek Görsel"><figcaption><p>Model Listesini Alma</p></figcaption></figure>

## Sık Sorulan Sorular

### Device Code Alınamadı, Lütfen Yeniden Deneyin

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Device Code Alma Hatası Örnek Görsel"><figcaption><p>Device Code Alınamadı</p></figcaption></figure>

İstekler şu anda Axios ile oluşturulmaktadır. Axios socks proxy'leri desteklemez, lütfen sistem proxy'si veya HTTP proxy kullanın ya da CherryStudio içinde proxy ayarlamayarak global proxy kullanın. Öncelikle ağ bağlantınızın sorunsuz çalıştığından emin olun, böylece Device Code alma hatası önlenebilir.