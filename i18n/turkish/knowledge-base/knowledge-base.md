---
icon: book-open-cover
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Bilgi Deposu Eğitimi

0.9.1 sürümünde, CherryStudio uzun zamandır beklenen bilgi deposu özelliğini getirdi.

Aşağıda, CherryStudio'nun ayrıntılı kullanım talimatlarını adım adım sunacağız.

## Gömme Modeli Ekleme

1. Model yönetim hizmetinde model arayın, hızlı filtreleme için "Gömme Modeli" seçeneğine tıklayabilirsiniz;
2. İhtiyacınız olan modeli bulun ve modellerime ekleyin.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Bilgi Deposu Oluşturma

1. Bilgi deposu girişi: CherryStudio sol araç çubuğunda, bilgi deposu simgesine tıklayarak yönetim sayfasına girebilirsiniz;
2. Bilgi deposu ekle: Ekle'ye tıklayarak bilgi deposu oluşturmaya başlayın;
3. İsimlendirme: Bilgi deposu için bir ad girin ve bir gömme modeli ekleyin, örneğin bge-m3, böylece oluşturma işlemi tamamlanır.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Dosya Ekleme ve Vektörleştirme

1. Dosya ekle: Dosya ekle düğmesine tıklayarak dosya seçimi penceresini açın;
2. Dosya seçin: Desteklenen dosya formatlarından birini seçin (ör. pdf, docx, pptx, xlsx, txt, md, mdx) ve açın;
3. Vektörleştirme: Sistem otomatik olarak vektörleştirme işlemini gerçekleştirecektir. İşlem tamamlandığında (yeşil ✓) vektörleştirmenin tamamlandığı anlamına gelir.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>



## Çeşitli Kaynaklardan Veri Ekleme

CherryStudio çeşitli veri ekleme yöntemlerini destekler:

1. Klasör dizini: Tüm bir klasör dizini ekleyebilirsiniz, bu dizindeki desteklenen formatlardaki dosyalar otomatik olarak vektörleştirilecektir;
2. Web adresi bağlantısı: Web adresi URL'leri desteklenir, örneğin: [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Site haritası: XML formatında site haritaları desteklenir, örneğin: [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Düz metin notları: Düz metin özel içeriklerin girişi desteklenir.

{% hint style="info" %}
İpucu:

1. Bilgi deposuna aktarılan belgelerdeki çizimler şu an vektöre dönüştürülemez, metne dönüştürmek için manuel işlem gerekir;
2. Web sitesi adresi olarak kaynak kullanırken her zaman başarılı olmayabilir, bazı sitelerde sıkı anti-bot korumaları (veya giriş, yetkilendirme gerektirme) olabilir, bu nedenle bu yöntemle doğru içerik almak garantili değildir. Oluşturma sonrasında önceden arama testi yapmanız önerilir.
3. Genellikle web siteleri site haritası sağlar, CherryStudio'nun [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml) gibi. Genellikle web sitesinin kök adresine (ana adres) `/sitemap.xml` eklenerek ilgili bilgi alınabilir. Örneğin: `aaa.com/sitemap.xml`.
4. Eğer site haritası sağlamıyorsa veya adresler karmaşıksa, kendiniz bir site haritası XML dosyası oluşturabilirsiniz. Dosya, halka açık doğrudan erişilebilen bir bağlantı olmalıdır, yerel dosya bağlantıları tanınmaz.

> 1) Bir AI kullanarak site haritası oluşturabilir veya AI'dan bir site haritası HTML üreteci aracı yazmasını isteyebilirsiniz;
> 2) Doğrudan bağlantı için OSS bağlantısı veya bulut depolama bağlantısı gibi yöntemler kullanılabilir. Hazır araç yoksa [ocoolAI](https://one.ocoolai.com/login) resmi sitesine gidip giriş yaptıktan sonra üst menüdeki ücretsiz dosya yükleme aracını kullanarak doğrudan bağlantı oluşturabilirsiniz.
{% endhint %}

## Bilgi Deposunda Arama

Dosyalar vektörleştirildikten sonra, arama yapılabilir:

1. Sayfanın altındaki "Bilgi Deposunda Ara" düğmesine tıklayın;
2. Sorgunuzu girin;
3. Arama sonuçları görüntülenecektir;
4. Ve ilgili sonucun eşleşme puanı gösterilir.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Görüşmelerde Bilgi Deposuna Başvurarak Yanıt Oluşturma

1. Yeni bir konu oluşturun, sohbet araç çubuğunda "Bilgi Deposu"na tıklayın, bu mevcut bilgi depolarının listesini açar, başvurmak istediğiniz bilgi deposunu seçin;
2. Soruyu yazıp gönderin, model sonucu aratarak elde edilen cevabı döndürecektir;
3. Ayrıca, başvurulan veri kaynağı cevabın altında eklenecektir, böylece kaynak dosyayı hızlıca görüntüleyebilirsiniz.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>