---
icon: seal-question
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Sıkça Sorulan Sorular

## Sık Karşılaşılan Hata Kodları

* **4xx (İstemci Hata Durum Kodları)**: Genellikle istek sözdizimi hatası, kimlik doğrulama başarısızlığı veya yetkilendirme başarısızlığı gibi isteğin tamamlanamadığı durumlar.
* **5xx (Sunucu Hata Durum Kodları)**: Genellikle sunucu tarafı hatalar, sunucu çökmeleri, istek işleme zaman aşımı gibi durumlar.

| Hata Kodu         | Olası Durumlar                                                                                      | Çözüm Yöntemleri                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4>      | İstek gövdesi format hatası vb.                                                                     | <p>Diyalog dönüş hata içeriğini kontrol edin veya <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">konsol</a> hata mesajını inceleyip talimatları uygulayın.</p><p><mark style="color:purple;">【Sık Durum 1】</mark>: Gemini modeliyse, kart bağlama gerekebilir;<br><mark style="color:purple;">【Sık Durum 2】</mark>: Veri boyutu limit aşımı, görsel modellerde yaygın, tek istek üst limitini aşan görseller;<br><mark style="color:purple;">【Sık Durum 3】</mark>: Desteklenmeyen parametre veya hatalı parametre. Temiz bir yardımcı oluşturup test edin;<br><mark style="color:purple;">【Sık Durum 4】:</mark> Bağlam limit aşımı, bağlamı temizleyin/yeni diyalog başlatın/bağlam sayısını azaltın.</p> |
| <h4>401</h4>      | Kimlik doğrulama başarısız: Model desteklenmiyor veya sunucu hesabı askıya alınmış vb.                    | İlgili servis sağlayıcı hesap durumunu kontrol edin                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <h4>403</h4>      | İstek işlemi için izin yok                                                                        | Diyalog dönüş hata mesajına veya [konsol](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa) hata bilgisine göre hareket edin                                                                                                                                                                                                                                                                                                                                                                                             |
| <h4>404</h4>      | İstenen kaynak bulunamadı                                                                            | İstek yolunu vb. kontrol edin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <h4>422</h4>      | İstek formatı doğru ancak semantik hata                                                              | Sunucu isteği ayrıştırabilir ancak işleyemez. JSON semantik hataları yaygındır (örn: null değer; string beklenirken sayı/boolean girilmesi).                                                                                                                                                                                                                                                                                                                                                                           |
| <h4>429</h4>      | İstek hız limiti aşıldı                                                                            | İstek hızı (TPM veya RPM) limitine ulaşıldı, bir süre bekleyin                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <h4>500</h4>      | Sunucu iç hatası, istek tamamlanamıyor                                                                 | Sürekli olursa servis sağlayıcıyla iletişime geçin                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>501</h4>      | Sunucu istenen fonksiyonu desteklemiyor, istek tamamlanamıyor                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>502</h4>      | Gateway veya proxy sunucusu geçersiz yanıt aldı                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>503</h4>      | Aşırı yük veya bakım nedeniyle sunucu geçici olarak istekleri işleyemiyor                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>504</h4>      | Gateway/proxy sunucusu uzak sunucudan zamanında yanıt alamadı                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

***

## Konsol Hata İnceleme Yöntemi

* Cherry Studio istemci penceresine tıkladıktan sonra kısayol tuşlarına basın: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- Aktif pencerenin Cherry Studio istemcisi olması gereklidir;
- İstek bilgilerini toplamak için önce konsolu açıp sonra test/diyalog başlatma gibi işlemler yapmalısınız.
{% endhint %}

* Açılan konsol penceresinde <mark style="color:blue;">`Network`</mark> → ② numaralı yerde kırmızı <mark style="color:red;">`×`</mark> işaretli son <mark style="color:red;">`completions`</mark> (_diyalog/çeviri/model testi hatalarında_) veya <mark style="color:red;">`generations`</mark> (_resim oluşturma hatalarında_) seçin → <mark style="color:blue;">`Response`</mark> tıklayarak tam yanıtı görüntüleyin (④ numaralı alan).

> Hatayı çözemezseniz, ekran görüntüsünü [Resmi Topluluk Grubuna](https://t.me/CherryStudioAI) gönderin.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Bu yöntem sadece diyalogda değil, model testi, bilgi deposu ekleme, resim oluşturma vb. tüm senaryolarda kullanılabilir. Her durumda önce hata ayıklama penceresi açılmalıdır.

{% hint style="info" %}
Farklı senaryolarda "Name" (②) alanındaki isimler farklıdır:

Diyalog/Çeviri/Model Testi: <mark style="color:red;">`completions`</mark>&#x20;

Resim Oluşturma: <mark style="color:red;">`generations`</mark>

Bilgi Deposu Oluşturma: <mark style="color:red;">`embeddings`</mark>&#x20;
{% endhint %}

***

## Formül Render Edilmiyor/Hatalı Render

* Formül kod olarak görünüyorsa, sınırlayıcıları kontrol edin

> **Sınırlayıcı Kullanımı**
>
> _Satır İçi Formüller_
>
> * Tek dolar işareti: `$formül$`
> * veya `\(` ve `\)`, örn: `\(formül\)`
>
>
>
> _Bağımsız Formül Blokları_
>
> * Çift dolar işareti: `$$formül$$`
> * veya `\[formül\]`
> * Örnek: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Formül render hatası/bozuk karakter: Formül içinde Çince karakterler varsa KateX motoruna geçin.

***

## Bilgi Deposu Oluşturulamıyor/Gömme Boyutu Alınamıyor

1. Model durumu uygun değil
   
> Modelin desteklendiğini veya servis durumunun normal olduğunu doğrulayın.

2. Gömme modeli olmayan model kullanıldı

***

## Model Resim Tanıyamıyor/Resim Yüklenemiyor veya Seçilemiyor

Önce modelin resim tanıma desteği olduğunu doğrulayın. Cherry Studio popüler modelleri kategorize eder - model adı yanındaki göz ikonlu modeller resim tanımayı destekler.

Resim tanıma modelleri görsel dosya yüklemeyi destekler. Model eşleşmesi düzgün yapılmadıysa, ilgili servis sağlayıcının model listesinden modeli bulun ve ayarlar düğmesine tıklayıp "image" seçeneğini etkinleştirin.

Model detaylarını servis sağlayıcıdan kontrol edebilirsiniz. Gömme modellerinde olduğu gibi, görsel yeteneği olmayan modellerde bu seçenek etkisizdir.