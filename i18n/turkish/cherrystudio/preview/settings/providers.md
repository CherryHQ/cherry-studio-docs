---
icon: cloud-check
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Sağlayıcı Ayarları

Bu sayfa yalnızca arayüz işlevlerinin tanıtımı içindir; yapılandırma eğitimi için temel eğitimlerdeki [Sağlayıcı Yapılandırması](../../../pre-basic/providers/) eğitimine bakabilirsiniz.

{% hint style="info" %}
* Yerleşik sağlayıcılar kullanılırken yalnızca ilgili gizli anahtarın doldurulması yeterlidir.
* Farklı sağlayıcıların gizli anahtar için kullanılan terimleri farklı olabilir; gizli anahtar, Key, API Key, token gibi ifadelerin hepsi aynı şeyi ifade eder.
{% endhint %}



### API Gizli Anahtarı

Cherry Studio'da, tek bir sağlayıcı birden çok anahtarın dönüşümlü kullanımını destekler. Dönüşüm yöntemi, listedeki anahtarları baştan sona sırayla döngüsel olarak kullanmaktır.

* Birden çok anahtar İngilizce virgülle ayrılarak eklenir. Örnek aşağıdaki gibidir:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
**İngilizce** virgül kullanılmalıdır.
{% endhint %}

### API Adresi

Yerleşik sağlayıcılar kullanılırken genellikle API adresinin doldurulması gerekmez. Değiştirilmesi gerekiyorsa, ilgili resmi belgelerde verilen adresi tam olarak uyarak doldurun.

> Sağlayıcı tarafından verilen adres <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> şeklindeyse, yalnızca kök adres kısmını (<mark style="background-color:red;">https://xxx.xxx.com</mark>) doldurmanız yeterlidir.
>
> Cherry Studio kalan yolu otomatik olarak ekler (<mark style="background-color:green;">/v1/chat/completions</mark>). Gerektiği gibi doldurulmazsa normal kullanımı engelleyebilir.

{% hint style="info" %}
Açıklama: Çoğu sağlayıcının büyük dil modeli rotası standarttır ve genellikle aşağıdaki işlemler gerekmez. Sağlayıcının API yolu v2, v3/chat/completions veya başka bir sürümse:
- Adres çubuğuna ilgili sürümü "`/`" ile biterek elle girin
- Sağlayıcının istek rotası standart <mark style="background-color:green;">/v1/chat/completions</mark> değilse, tam adresi "`#`" ile bitirin.

Yani:
* API adresi `/` ile bitiyorsa yalnızca "<mark style="background-color:green;">chat/completions</mark>" eklenir
* API adresi `#` ile bitiyorsa ekleme işlemi yapılmaz, yalnızca girilen adres kullanılır.

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}



### Model Ekleme

Genel olarak, sağlayıcı yapılandırma sayfasının sol alt köşesindeki `Yönet` düğmesine tıklamak, bu sağlayıcı tarafından desteklenen tüm çağrılabilir modelleri otomatik olarak alır. Alınan listedeki bir modelin sağındaki `+` simgesine tıklayarak model listesine ekleyebilirsiniz.

{% hint style="info" %}
Yönet düğmesine tıklandığında açılan penceredeki modellerin tümü eklenmez; bir modelin sağındaki `+` simgesine tıklayarak sağlayıcı yapılandırma sayfasındaki model listesine eklenmelidir. Ancak bu şekilde model seçim listesinde görünebilir.
{% endhint %}


### Bağlantı Kontrolü

API gizli anahtarı giriş kutusunun yanındaki kontrol düğmesine tıklayarak başarıyla yapılandırılıp yapılandırılmadığını test edebilirsiniz.

{% hint style="info" %}
Model kontrolü sırasında varsayılan olarak model listesine eklenmiş son sohbet modeli kullanılır. Kontrol sırasında hata olursa, model listesinde hatalı veya desteklenmeyen bir model olup olmadığını kontrol edin.
{% endhint %}

{% hint style="danger" %}
Yapılandırma başarılı olduktan sonra mutlaka sağ üst köşedeki anahtarı açın. Aksi takdirde bu sağlayıcı hala etkinleştirilmemiş durumda olacaktır ve model listesinde ilgili modeller bulunamaz.
{% endhint %}