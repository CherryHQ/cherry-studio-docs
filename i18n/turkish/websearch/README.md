---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Çevrimiçi Mod

{% hint style="info" %}
İnternet bağlantısı gerektiren senaryo örnekleri:

* Zaman duyarlı bilgiler: Örneğin bugün/bu hafta/az önce altın vadeli işlem fiyatları vb.
* Gerçek zamanlı veriler: Örneğin hava durumu, döviz kurları gibi dinamik değerler.
* Gelişmekte olan bilgiler: Örneğin yeni şeyler, yeni kavramlar, yeni teknolojiler vb...
{% endhint %}

### I. Çevrimiçi Modu Nasıl Açarım

Cherry Studio'nun soru sorma penceresinde 【küçük dünya】 simgesine tıklayarak çevrimiçi modu açabilirsiniz.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Dünya simgesine tıklayın - Çevrimiçi modu açın</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Çevrimiçi özelliğinin açıldığını gösterir</p></figcaption></figure>

### II. Özel Dikkat: İki Çeşit Çevrimiçi Mod

#### Mod 1: Model sağlayıcılarının büyük modelleri yerleşik çevrimiçi özelliğe sahiptir

Bu durumda, çevrimiçi mod açıldıktan sonra doğrudan çevrimiçi hizmeti kullanabilirsiniz, çok basittir.

{% hint style="warning" %}
Soru-cevap arayüzünün üst kısmında, model adının yanında küçük bir dünya işareti olup olmadığına bakarak modelin çevrimiçi desteğinin olup olmadığını hızlıca belirleyebilirsiniz.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Model yönetim sayfasında, bu yöntem hangi modellerin çevrimiçi desteklediğini ve hangilerinin desteklemediğini hızlıca ayırt etmenizi sağlar.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio'nun şu anda desteklediği çevrimiçi model sağlayıcıları:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (tüm modeller çevrimiçi desteğe sahiptir)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Aliyun Bailian vb.</mark>

{% hint style="danger" %}
Özel dikkat:
Özel bir durum vardır: Modelde dünya işareti olmasa bile çevrimiçi olabilir, aşağıdaki kılavuzda açıklandığı gibi.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Mod 2: Model çevrimiçi özelliğe sahip değilse, Tavily hizmeti ile çevrimiçi özelliği etkinleştirme

Çevrimiçi özelliği olmayan bir büyük model kullandığımızda (adında dünya simgesi yok) ve gerçek zamanlı bilgileri işlemesi gerektiğinde, Tavily internet arama hizmetini kullanmamız gerekir.

**Tavily hizmetini ilk kullanışınızda**, bilgileri ayarlamaya yönlendiren bir açılır pencere görünür - yönergeleri izlemeniz yeterlidir, çok basittir!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Açılır pencere, tıklayın: Ayarlara git</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Anahtarı almak için tıklayın</p></figcaption></figure>

Anahtarı almak için tıklayınca, otomatik olarak **tavily sitesi** giriş/kayıt sayfasına yönlendirileceksiniz. Kaydolun ve giriş yaptıktan sonra bir API anahtarı oluşturun, ardından anahtarı Cherry Studio'ya kopyalayın.

{% hint style="danger" %}
Kayıt işlemini bilmiyorsanız, bu belgeyle aynı dizindeki tavily çevrimiçi kayıt ve giriş kılavuzuna bakın.
{% endhint %}

**tavily kayıt kılavuzu:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Aşağıdaki arayüz kaydın başarılı olduğunu gösterir.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Anahtarı kopyala</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Anahtarı yapıştırın, tamamlandı</p></figcaption></figure>

Şimdi tekrar deneyelim ve sonucu görelim. Sonuçlar, çevrimiçi aramanın başarılı olduğunu ve varsayılan olarak ayarladığımız 5 arama sonucunun görüntülendiğini gösterir.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Not: tavily'nin aylık ücretsiz kullanım sınırı vardır, aşılırsa ücret ödemeniz gerekir~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Herhangi bir hata bulursanız, lütfen bize ulaşmaktan çekinmeyin.