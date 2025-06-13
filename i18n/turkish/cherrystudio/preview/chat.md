---
icon: message
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Sohbet Arayüzü

## Yardımcılar ve Konular

### Yardımcılar

`Yardımcılar`, seçilen modeli özelleştirmek için kişiselleştirilmiş ayarları tanımlar (örn. istem ön ayarları ve parametre ön ayarları). Bu ayarlar, modelin beklentilerinize daha uygun çalışmasını sağlar.

`Sistem varsayılan yardımcısı` genel amaçlı parametrelerle (istem kutusuz) önceden yapılandırılmıştır. Direkt kullanabilir veya ihtiyacınız olan ön ayarları bulmak için [Agent'lar sayfasına](agents.md) gidebilirsiniz.

### Konular

`Yardımcılar`, `konuların` üst kümesidir. Tek bir yardımcı altında birden çok konu (sohbet) oluşturulabilir. Tüm `konular`, `yardımcının` parametre ayarlarını ve istem kutusu (prompt) gibi model ayarlarını paylaşır.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Sohbet Kutusu Düğmeleri

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Yeni konu` Mevcut yardımcı altında yeni bir konu oluşturur.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Resim veya belge yükle` Resim yüklemek için model desteği gerekir. Belge yükleme işlemi otomatik olarak metne dönüştürülerek modele bağlam olarak sunulur.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Web araması` Ayar menüsünde arama bilgileri yapılandırılmalıdır. Sonuçlar bağlam olarak büyük modele iletilir. Ayrıntılar için bkz. [Çevrimiçi mod](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Bilgi bankası` Bilgi bankası işlevini etkinleştirir. Ayrıntılar için bkz. [Bilgi Bankası Kılavuzu](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP sunucusu` MCP sunucu işlevini etkinleştirir. Ayrıntılar için bkz. [MCP Kullanım Kılavuzu](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Resim oluştur` Varsayılan olarak gizlidir. Resim oluşturmayı destekleyen modeller (örn. Gemini) için manuel olarak etkinleştirilmelidir.

{% hint style="info" %}
Teknik kısıtlamalar nedeniyle resim oluşturmak için manuel olarak bu düğmeyi etkinleştirmeniz gerekmektedir. Bu kısıtlama düzeltildiğinde düğme kaldırılacaktır.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Model seç` Gelecek konuşmalar için belirtilen modele geçiş yapar. Bağlam korunur.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Kısayol ifadeleri` Önce ayarlardan kısayol ifadeleri ekleyin. Direkt giriş için buradan çağırın (değişken destekler).

![](../../.gitbook/assets/对话界面/清空消息.png) `Mesajları temizle` Bu konudaki tüm içeriği siler.

![](../../.gitbook/assets/对话界面/展开.png) `Genişlet` Uzun metinler için sohbet kutusunu büyütür.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Bağlamı temizle` İçeriği silmeden modelin erişebileceği bağlamı keser. Model "önceki" konuşmaları unutur.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Tahmini Token sayısı` Tahmini Token ölçümlerini gösterir: `Mevcut bağlam boyutu`, `Maksimum bağlam boyutu` (∞ sınırsız bağlam demektir), `Geçerli girdi mesajı boyutu`, `Tahmini Token sayısı`.

{% hint style="info" %}
Bu yalnızca tahmini ölçüm içindir. Gerçek Token sayıları modele göre değişir. Lütfen model sağlayıcınızın verilerini referans alın.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Çeviri` Mevcut girdi kutusu içeriğini İngilizceye çevirir.

## Sohbet Ayarları

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Model Ayarları

Model ayarları, yardımcı ayarlarındaki `Model ayarları` ile senkronizedir. Ayrıntılar için bkz. [Yardımcı düzenleme](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Sohbet ayarlarında sadece bu model ayarları geçerli yardımcı için uygulanır. Diğer tüm ayarlar global olarak etkilidir. Örn: Mesaj stili baloncuk olarak ayarlandığında tüm yardımcılarda geçerli olur.
{% endhint %}

### Mesaj Ayarları

#### <mark style="color:blue;">**`Mesaj ayracı`**</mark>:

Mesaj içeriği ile işlem çubuğunu ayırmak için ayraç kullanın.

{% tabs %}
{% tab title="Açıkken" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Kapalıyken" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Serif yazı tipi kullan`**</mark>：

Yazı tipi stilini değiştirir. İsterseniz [özel CSS](../../personalization-settings/) ile farklı yazı tipleri de yükleyebilirsiniz.

#### <mark style="color:blue;">**`Kod bloklarında satır numarası göster`**</mark>：

Model kod parçası çıktısı verirken satır numaralarını gösterir.

{% tabs %}
{% tab title="Kapalıyken" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Açıkken" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Kod blokları daraltılabilir`**</mark>：

Açıkken, uzun kod parçaları otomatik olarak daraltılır.

#### <mark style="color:blue;">**`Kod bloklarında kaydırma`**</mark>：

Açıkken, pencereden taşan uzun kod satırları otomatik olarak kaydırılır.

#### <mark style="color:blue;">**`Düşünme içeriğini otomatik daralt`**</mark>：

Açıkken, düşünme yeteneği olan modeller işlem tamamlandığında düşünme sürecini otomatik daraltır.

#### <mark style="color:blue;">**`Mesaj stili`**</mark>：

Sohbet arayüzünde baloncuk veya liste stilini seçebilirsiniz.

#### <mark style="color:blue;">**`Kod stili`**</mark>：

Kod parçalarının görüntüleme stilini değiştirebilirsiniz.

#### <mark style="color:blue;">**`Matematik formül motoru`**</mark>：

* KaTeX daha hızlıdır (performans için optimize edilmiştir);
* MathJax daha yavaş ama kapsamlıdır (daha fazla matematik sembolü ve komut destekler).

#### <mark style="color:blue;">**`Mesaj yazı tipi boyutu`**</mark>：

Sohbet arayüzündeki yazı boyutunu ayarlar.

### Girdi Ayarları

#### <mark style="color:blue;">**`Tahmini Token sayısını göster`**</mark>：

Girdi kutusunda tahmini Token tüketimini gösterir (gerçek bağlam tüketimini değil, yalnızca gösterge amaçlı).

#### <mark style="color:blue;">**`Uzun metinleri dosya olarak yapıştır`**</mark>：

Uzun metinler girdi kutusuna yapıştırıldığında otomatik olarak dosya formatında gösterilir. Bu özellik sonraki girdilerdeki karışıklığı azaltır.

#### <mark style="color:blue;">**`Girdi mesajlarında Markdown işleme`**</mark>：

Kapalıyken, yalnızca model yanıtları işlenir. Gönderilen mesajlar işlenmez.

{% tabs %}
{% tab title="Kapalıyken" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Açıkken" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`3 kez boşlukla hızlı çeviri`**</mark>：

Girdi kutusuna mesaj yazdıktan sonra üç kez boşluk tuşuna basarak içeriği İngilizceye çevirebilirsiniz.

{% hint style="warning" %}
Uyarı: Bu işlem orijinal metnin üzerine yazar.
{% endhint %}

#### <mark style="color:blue;">**`Hedef dil`**</mark>：

Hızlı çeviri ve çeviri düğmesi için hedef dili ayarlar.

## Yardımcı Ayarları

<mark style="background-color:yellow;">Yardımcı adı</mark> seçin → <mark style="background-color:yellow;">Sağ tık menüsünden</mark> ilgili ayarları yapın

### Yardımcıyı düzenle

{% hint style="info" %}
Yardımcı ayarları bu yardımcı altındaki tüm konular için geçerlidir.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### İstem kutusu ayarları

#### <mark style="color:blue;">**`Ad`**</mark>：

Kolay tanımlanabilir bir yardımcı adı seçin.

#### <mark style="color:blue;">**`İstem kutusu (Prompt)`**</mark>：

İstem içeriği. Agent sayfasındaki örnekler gibi düzenleyebilirsiniz.

#### Model ayarları

#### <mark style="color:blue;">**`Varsayılan model`**</mark>：

Bu yardımcı için sabit bir varsayılan model atayabilirsiniz. Agent sayfasından eklerken veya kopyalarken bu model kullanılır. Bu ayarlanmazsa global varsayılan model ([Varsayılan yardımcı model](settings/default-models.md#mo-ren-zhu-shou-mo-xing)) geçerli olur.

{% hint style="info" %}
İki tür varsayılan model vardır: Global varsayılan sohbet modeli ve yardımcı varsayılan modeli. Yardımcı modeli globalden daha yüksek önceliklidir. Yardımcı modeli ayarlanmadığında, global model kullanılır.
{% endhint %}

#### <mark style="color:blue;">**`Modeli otomatik sıfırla`**</mark>：

Açıkken - Bu konuda farklı bir model kullanıldığında, yeni konu oluşturulduğunda yardımcının varsayılan modeline geri döner. Kapalıyken yeni konu önceki konuyla aynı modeli kullanır.

> Örn: Yardımcı modeli gpt-3.5-turbo olsun. Konu1'de konuşurken gpt-4o'ya geçersem:
>
> Otomatik sıfırla açıksa: Konu2 oluşturulduğunda model gpt-3.5-turbo olur;
>
> Kapalıysa: Konu2 oluşturulduğunda model gpt-4o olur.

#### <mark style="color:blue;">**`Sıcaklık (Temperature)`**</mark> ：

Çıktının rastgelelik ve yaratıcılık seviyesini kontrol eder (varsayılan: 0.7). Davranışı:

* Düşük değerler (0-0.3):
  * Daha öngörülebilir ve odaklı çıktı
  * Kod üretimi, analiz gibi doğruluk gerektiren senaryolar için
* Orta değerler (0.4-0.7):
  * Yaratıcılık ve tutarlılık dengesi
  * Günlük konuşmalar, genel yazım için
  * Sohbet botları için önerilir (≈0.5)
* Yüksek değerler (0.8-1.0):
  * Daha yaratıcı ve çeşitli çıktı
  * Beyin fırtınası gibi senaryolar için
  * Metin tutarlılığını düşürebilir

#### <mark style="color:blue;">**`Top P (Çekirdek örnekleme)`**</mark>：

Varsayılan değer 1'dir. Düşük değerler daha az çeşitlilikle daha anlaşılır çıktı verirken, yüksek değerler kelime çeşitliliğini artırır.

Örnekleme kelime seçimini etkiler:

* Küçük değerler (0.1-0.3):
  * En yüksek olasılıklı kelimeleri kullanır
  * Konservatif ve kontrollü çıktı
  * Kod açıklamaları için uygundur
* Orta değerler (0.4-0.6):
  * Kelime çeşitliliği ve doğruluk dengesi
  * Genel konuşma ve yazılar için
* Büyük değerler (0.7-1.0):
  * Daha geniş kelime havuzu
  * Zengin içerik üretir
  * Yaratıcı yazım için

{% hint style="info" %}
- Parametreler birlikte/ayrı kullanılabilir
- Görev tipine uygun değer seçin
- Deneysel olarak optimum ayarı bulun
- Yukarı