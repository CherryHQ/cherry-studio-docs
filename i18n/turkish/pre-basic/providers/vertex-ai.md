---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Vertex AI

## Öğreticiye Genel Bakış

### 1. API Anahtarını Edinme

* Gemini'nin API Anahtarını edinmeden önce, bir Google Cloud projenizin olması gerekiyor (zaten varsa, bu adımı atlayabilirsiniz)
* Proje oluşturmak için [Google Cloud](https://console.cloud.google.com/projectcreate) sayfasına gidin, proje adını yazın ve "Proje Oluştur"u tıklayın

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI kontrol paneline](https://console.cloud.google.com/vertex-ai) gidin
* Oluşturduğunuz projede [Vertex AI API'yi etkinleştirin](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API Erişim İzinlerini Ayarlama

* Hizmet hesapları izin sayfasını açın ([buraya tıklayın](https://console.cloud.google.com/iam-admin/serviceaccounts)) ve yeni bir hizmet hesabı oluşturun

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Hizmet hesapları yönetim sayfasında oluşturduğunuz hesabı bulun, `Anahtarlar`a tıklayın ve yeni bir JSON formatında anahtar oluşturun

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Başarıyla oluşturulduğunda, anahtar dosyası JSON formatında bilgisayarınıza otomatik kaydedilecektir, lütfen **bu dosyayı güvenle saklayın**

## 3. Cherry Studio'da Vertex AI Yapılandırması

* Vertex AI sağlayıcısını seçin
* JSON dosyasındaki ilgili alanları girin

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[Model Ekle'ye](https://console.cloud.google.com/vertex-ai/model-garden) tıklayın ve hemen keyifle kullanmaya başlayabilirsiniz!