---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Vertex AI

## Eğitim Genel Bakışı

### 1. API Anahtarını Alın

* Gemini API Anahtarını almadan önce bir Google Cloud projenizin olması gerekir (zaten varsa bu adım atlanabilir)
* [Google Cloud](https://console.cloud.google.com/projectcreate) üzerinden proje oluşturun, proje adını girerek "Proje Oluştur"u tıklayın

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI kontrol paneline](https://console.cloud.google.com/vertex-ai) gidin
* Oluşturduğunuz projede [Vertex AI API'yi etkinleştirin](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API Erişim İzinlerini Yapılandırın

* [Servis hesapları](https://console.cloud.google.com/iam-admin/serviceaccounts) sayfasına giderek servis hesabı oluşturun

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Servis hesap yönetim sayfasında yeni oluşturduğunuz hesabı bulun, `Anahtarlar` seçeneğine tıklayarak yeni bir JSON formatında anahtar oluşturun

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Başarıyla oluşturulduktan sonra anahtar dosyası JSON formatında otomatik olarak bilgisayarınıza kaydedilecektir, lütfen **bu dosyayı güvenli şekilde saklayın**

## 3. Vertex AI'yi Cherry Studio'da Yapılandırın

* Vertex AI servis sağlayıcısını seçin
* JSON dosyasındaki ilgili alanları karşılık gelen yerlere girin

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[Model ekleyin](https://console.cloud.google.com/vertex-ai/model-garden) seçeneğine tıklayarak kullanmaya başlayabilirsiniz!