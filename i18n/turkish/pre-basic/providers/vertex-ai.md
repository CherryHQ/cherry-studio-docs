---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Vertex AI

## Öğretici Genel Bakışı

### 1. APIKey Alma

* Gemini için API anahtarı almadan önce bir Google Cloud projenizin olması gerekir (zaten varsa bu adım atlanabilir)
* [Google Cloud](https://console.cloud.google.com/projectcreate) adresine gidin, proje adınızı yazın ve "Proje oluştur"a tıklayın

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI kontrol paneli](https://console.cloud.google.com/vertex-ai)ne gidin
* Oluşturduğunuz projede [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) etkinleştirin

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API Erişim İzinlerini Ayarlama

* [Hizmet hesapları](https://console.cloud.google.com/iam-admin/serviceaccounts) izin sayfasını açın, yeni bir hizmet hesabı oluşturun

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Hizmet hesabı yönetim sayfasında yeni oluşturduğunuz hesabı bulun, `Anahtarlar` bölümüne girin ve JSON formatında yeni bir anahtar oluşturun

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Başarıyla oluşturulduğunda, anahtar dosyası JSON formatında bilgisayarınıza otomatik indirilecektir, lütfen **dikkatle saklayın**

## 3. Vertex AI'yi Cherry Studio'da Yapılandırma

* Vertex AI sağlayıcısını seçin
* JSON dosyasındaki ilgili alanları karşılık gelen yerlere girin

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[Model ekle](https://console.cloud.google.com/vertex-ai/model-garden) düğmesine tıklayın ve kullanmaya başlayın! 🎉