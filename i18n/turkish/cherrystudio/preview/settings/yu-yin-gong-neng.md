---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Ses Özellikleri

```
Cherry Studio Ses Özellikleri Kullanım Kılavuzu

## I. Ses Özelliklerine Genel Bakış

Cherry Studio üç ana ses özellik modülü sunar: TTS (Metinden Sese), ASR (Ses Tanıma) ve sesli arama. Bu özellikler, AI ile doğal konuşma yaparak kullanım deneyiminizi geliştirmenizi sağlar.

- **TTS (Metinden Sese)**: AI'nın metin yanıtlarını ses çıktısına dönüştürür
- **ASR (Ses Tanıma)**: Konuşmanızı metin girişine dönüştürür
- **Sesli Arama**: TTS ve ASR'yi birleştirerek ChatGPT benzeri sesli sohbet deneyimi sunar

## II. TTS (Metinden Sese) Özelliği

### 1. Desteklenen Servis Türleri

Cherry Studio dört TTS servis türünü destekler:

- **OpenAI**: OpenAI'nin TTS API'si, API anahtarı gerektirir
- **Tarayıcı TTS**: Tarayıcının yerleşik ses sentezi, ücretsiz ve yapılandırma gerektirmez
- **Silikonflow**: Siliconflow TTS servisi, API anahtarı gerektirir
- **Ücretsiz Çevrimiçi TTS**: API anahtarı gerektirmeyen ücretsiz TTS servisi

### 2. Kurulum Yöntemi

1) Ayarlar sayfasına gidin, "Ses Özellikleri" sekmesini seçin
2) "TTS" alt sekmesinde:
   - TTS'yi etkinleştirin (anahtar açın)
   - TTS servis türünü seçin
   - Seçilen servise göre gerekli parametreleri yapılandırın:
     - OpenAI: API anahtarı, API adresi, ses tonu ve model
     - Tarayıcı TTS: Ses tonu seçimi
     - Silikonflow: API anahtarı, API adresi, ses tonu, model, yanıt formatı ve konuşma hızı
     - Ücretsiz Çevrimiçi TTS: Ses tonu ve çıktı formatı
3) İsteğe bağlı TTS filtre seçeneklerini yapılandırın:
   - Düşünme sürecini filtrele
   - Markdown işaretlemelerini filtrele
   - Kod bloklarını filtrele
4) TTS ilerleme çubuğunun gösterilip gösterilmeyeceğini ayarlayın
5) Yapılandırmanın doğruluğunu test etmek için "TTS Testi" düğmesine tıklayın

### 3. Kullanım Yöntemi

- TTS etkinleştirildiğinde, AI yanıtları otomatik olarak sese dönüştürülür
- Sohbet arayüzünde her AI yanıtı altında TTS oynatma düğmesi görünür
- Oynat/durdur düğmesi sesi kontrol eder
- İlerleme çubuğu etkinse metin altında görünür
- Uzun metinler otomatik olarak segmentlere ayrılıp ardışık oynatılır

## III. ASR (Ses Tanıma) Özelliği

### 1. Desteklenen Servis Türleri

Cherry Studio üç ASR servis türünü destekler:

- **OpenAI**: OpenAI Whisper modeli, API anahtarı gerektirir
- **Tarayıcı**: Tarayıcının yerleşik ses tanıma, ücretsiz ve yapılandırma gerektirmez
- **Yerel Sunucu**: Yerel WebSocket sunucusuna bağlanarak ses tanıma

### 2. Kurulum Yöntemi

1) Ayarlar sayfasına gidin, "Ses Özellikleri" sekmesini seçin
2) "ASR" alt sekmesinde:
   - ASR'yi etkinleştirin (anahtar açın)
   - ASR servis türünü seçin
   - Seçilen servise göre parametreleri yapılandırın:
     - OpenAI: API anahtarı, API adresi, model seçimi
     - Tarayıcı: Ek yapılandırma gerekmez
     - Yerel Sunucu: Uygulama başlangıcında ASR sunucusunu otomatik başlatma seçeneği
   - Varsayılanı Çince olan ses tanıma dilini seçin
3) Yapılandırmanın doğruluğunu test etmek için "ASR Testi" düğmesine tıklayın

### 3. Kullanım Yöntemi

- ASR etkinleştirildiğinde, giriş kutusu yanında ses tanıma düğmesi görünür
- Kayda başlamak için düğmeye tıklayın
- Konuştuktan sonra, ses metne dönüştürülüp giriş kutusuna yerleştirilir
- Kaydı durdurmak için tekrar düğmeye basın
- Çoklu cümleler için kümülatif mod desteklenir

## IV. Sesli Arama Özelliği

### 1. Özellikler

- TTS ve ASR entegrasyonuyla ChatGPT benzeri deneyim
- Sürüklenebilir pencere arayüzü
- Basılı tut konuşma modu
- Özel kısayol desteği
- Pencere daraltma desteği
- Özel sesli arama modelleri
- Özel komut istemleri

### 2. Kurulum Yöntemi

1) Ayarlar sayfasına gidin, "Ses Özellikleri" sekmesini seçin
2) "Arama Özelliği" alt sekmesinde:
   - Sesli aramayı etkinleştirin (anahtar açın)
   - "Model Seç" ile sesli arama için AI modelini belirleyin
   - İsteğe bağlı özel komut istemi ekleyin
   - "Kaydet" ile komut istemini saklayın veya "Sıfırla" ile varsayılana dönün

### 3. Kullanım Yöntemi

1) Sohbet arayüzündeki telefon simgesine tıklayın
2) Sesli arama penceresi açılır ve hoş geldiniz mesajı çalar
3) "Basılı Tut Konuş" düğmesini basılı tutarak kayda başlayın (veya kısayolu kullanın)
4) Bırakınca kayıt durur ve AI'ya gönderilir
5) AI yanıtı TTS ile seslendirilir
6) Kontrol düğmelerini kullanın:
   - Sessiz/aç: TTS çıktısını kontrol eder
   - Duraklat/devam: Konuşmayı duraklatır
   - Ayarlar: Kısayolları yapılandırır
   - Daralt: Pencereyi daraltır
7) Kapat düğmesiyle aramayı sonlandırın

### 4. Kısayol Ayarları

1) Sesli arama penceresinde ayarlar düğmesine tıklayın
2) Açılan panelde kısayol simgesini seçin
3) İstediğiniz tuşa basın (boşluk, Shift vb.)
4) "Kaydet" ile ayarı saklayın
5) Kullanımda kısayolu basılı tutarak kayıt yapın

## V. Sıkça Sorulan Sorular (SSS) ve Çözümler

### 1. TTS Sorunları

- Sorun: TTS ses çıkarmıyor
  Çözüm: TTS etkin mi kontrol edin, doğru servis ve parametre seçimi

- Sorun: TTS kalitesi düşük
  Çözüm: Farklı servis veya ses tonu deneyin

- Sorun: TTS hata mesajı gösteriyor
  Çözüm: API anahtarı ve internet bağlantısını kontrol edin

### 2. ASR Sorunları

- Sorun: ASR sesi tanımıyor
  Çözüm: ASR etkin mi kontrol edin, servis ve parametre ayarları

- Sorun: ASR doğruluk oranı düşük
  Çözüm: Farklı servis deneyin veya mikrofon ayarlayın

- Sorun: ASR sunucu bağlantı hatası
  Çözüm: Yerel sunucuyu kontrol edin veya uygulamayı yeniden başlatın

### 3. Sesli Arama Sorunları

- Sorun: Sesli arama penceresi açılmıyor
  Çözüm: Özellik etkin mi kontrol edin, TTS/ASR ayarları

- Sorun: Basılı tut konuşma çalışmıyor
  Çözüm: Mikrofon izinlerini ve yeniden başlatmayı deneyin

- Sorun: AI sesli yanıt vermiyor
  Çözüm: TTS etkin mi ve sessiz mod kapalı mı kontrol edin

## VI. Gelişmiş Ayarlar ve Özelleştirme

### 1. TTS Gelişmiş Ayarlar

- Filtreleme seçenekleri: TTS çıktısını daha akıcı hale getirir
- İlerleme çubuğu: Görünürlük seçimi
- Özel ses tonları ve modeller

### 2. ASR Gelişmiş Ayarlar

- Otomatik sunucu başlatma
- Dil seçimleri

### 3. Sesli Arama Gelişmiş Ayarlar

- Özel komut istemleri: AI'nın sesli mod davranışını özelleştirin
- Özel modeller: Standart modellerden bağımsız sesli arama modeli
- Kısayol özelleştirmeleri

## VII. Kullanım Tavsiyeleri

1. **TTS Seçimi**:
   - Yüksek kalite için OpenAI veya Silikonflow
   - Basit kullanım için Tarayıcı veya Ücretsiz TTS

2. **ASR Seçimi**:
   - Yüksek doğruluk için OpenAI
   - Kullanım kolaylığı için Tarayıcı

3. **Sesli Arama Optimizasyonu**:
   - TTS/ASR girişimi için kulaklık kullanın
   - Sessiz ortamda kullanın
   - Özel komut istemleriyle AI davranışını özelleştirin

4. **İhtiyaçlara Göre Yapılandırma**:
   - Metin ağırlıklı kullanım için TTS aktif
   - Ses girişi için ASR aktif
   - Tam sesli sohbet için tüm özellikler

Bu kılavuz, Cherry Studio ses özelliklerini kullanarak doğal ve kullanışlı AI etkileşimleri yaşamanıza yardımcı olacaktır!
```