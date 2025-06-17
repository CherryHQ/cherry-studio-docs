
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Ollama

Ollama, yerel olarak çeşitli büyük dil modellerini (LLM'ler) kolayca çalıştırmanızı ve yönetmenizi sağlayan harika bir açık kaynaklı araçtır. Cherry Studio artık Ollama entegrasyonunu destekliyor ve size tanıdık arayüzde bulut hizmetlerine bağlı kalmadan yerel olarak dağıtılan LLM'lerle doğrudan etkileşim kurma imkanı sunuyor!

## Ollama nedir?

Ollama, büyük dil modellerinin (LLM) dağıtımını ve kullanımını basitleştiren bir araçtır. Şu özelliklere sahiptir:

* **Yerel çalıştırma:** Modeller tamamen yerel bilgisayarınızda çalışır, internete gerek yoktur, böylece gizliliğiniz ve veri güvenliğiniz korunur.
* **Kullanım kolaylığı:** Basit komut satırı talimatlarıyla çeşitli LLM'leri indirebilir, çalıştırabilir ve yönetebilirsiniz.
* **Zengin model desteği:** Llama 2, Deepseek, Mistral, Gemma gibi popüler açık kaynak modelleri destekler.
* **Platformlar arası:** macOS, Windows ve Linux sistemleriyle uyumludur.
* **Açık API:** OpenAI ile uyumlu arayüz desteği sayesinde diğer araçlarla entegre edilebilir.

## Cherry Studio'da Ollama neden kullanılmalı?

* **Bulut hizmeti gerekmez:** Bulut API'lerinin kotaları ve ücretleriyle sınırlı kalmazsınız, yerel LLM'lerin gücünü sınırsızca deneyimleyin.
* **Veri gizliliği:** Tüm konuşma verileriniz yerelde kalır, gizlilik ihlali endişesi yaşamazsınız.
* **Çevrimdışı kullanım:** İnternet bağlantısı olmadığı durumlarda bile LLM'lerle etkileşime devam edebilirsiniz.
* **Özelleştirme:** İhtiyaçlarınıza göre en uygun LLM'yi seçip yapılandırabilirsiniz.

## Cherry Studio'da Ollama yapılandırma

### **1. Ollama'yı Kurun ve Çalıştırın**

Öncelikle bilgisayarınıza Ollama'yı kurup çalıştırmanız gerekiyor. Şu adımları izleyin:

* **Ollama indirin:** Ollama resmi sitesini ([https://ollama.com/](https://ollama.com/)) ziyaret edip işletim sisteminize uygun kurulum paketini indirin.  
Linux'ta doğrudan şu komutla kurabilirsiniz:
    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Ollama'yı kurun:** Kurulum sihirbazının talimatlarını takip edin.
* **Model indirin:** Terminal (veya komut istemi) açın ve kullanmak istediğiniz modeli indirmek için `ollama run` komutunu kullanın. Örneğin, Llama 2 modelini indirmek için:
    ```sh
    ollama run llama3.2
    ```
    Ollama modeli otomatik olarak indirip çalıştıracaktır.
* **Ollama'yı çalışır durumda tutun:** Ollama modelleriyle Cherry Studio'da etkileşim kurduğunuz süre boyunca Ollama'nın çalışmaya devam ettiğinden emin olun.

### **2. Cherry Studio'da Ollama Sağlayıcı Ekleme**

Ardından, Cherry Studio'da Ollama'yı özel AI sağlayıcısı olarak ekleyin:

* **Ayarları açın:** Cherry Studio arayüzünün sol gezinme çubuğunda "Ayarlar" (dişli simgesi) seçeneğine tıklayın.
* **Model servisine gidin:** Ayarlar sayfasında "Model servisi" sekmesini seçin.
* **Sağlayıcı ekleyin:** Listeden Ollama'yı seçin.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Ollama Sağlayıcı Yapılandırması**

Sağlayıcı listesinden yeni eklediğiniz Ollama'yı bulun ve detaylı yapılandırın:

1. **Aktif durum:**
   * Ollama sağlayıcısının sağındaki anahtarın açık (mavi) olduğundan emin olun, bu etkinleştirildiğini gösterir.
2. **API anahtarı:**
   * Ollama varsayılan olarak API anahtarı **gerektirmez**. Bu alanı boş bırakabilir veya istediğiniz herhangi bir içeriği girebilirsiniz.
3. **API adresi:**
   * Ollama'nın sağladığı yerel API adresini girin. Genellikle şu şekildedir:
       ```
       http://localhost:11434/
       ```
       Bağlantı noktasını değiştirdiyseniz bunu güncelleyin.
4. **Aktif tutma süresi:** Oturumların kaç dakika açık kalacağını ayarlar. Belirtilen sürede yeni konuşma olmazsa Cherry Studio otomatik olarak Ollama bağlantısını keser, böylece kaynaklar serbest bırakılır.
5. **Model yönetimi:**
   * "+ Ekle" düğmesine tıklayıp Ollama'da zaten indirdiğiniz modellerin adını manuel olarak ekleyin.
   * Örneğin `ollama run llama3.2` komutuyla `llama3.2` modelini indirdiyseniz, buraya `llama3.2` girebilirsiniz.
   * "Yönet" düğmesi, eklenen modelleri düzenlemenizi veya silmenizi sağlar.

## Kullanmaya Başlayın

Yukarıdaki yapılandırma tamamlandıktan sonra, Cherry Studio'nun sohbet arayüzünden Ollama sağlayıcısını ve indirdiğiniz modeli seçerek yerel LLM'lerle konuşmaya başlayabilirsiniz!

## İpuçları ve Teknik Notlar

* **Modelin ilk çalıştırılması:** Bir model ilk kez çalıştırıldığında, Ollama model dosyalarını indireceği için uzun zaman alabilir, lütfen sabırlı olun.
* **Kullanılabilir modelleri görüntüleme:** Terminalde `ollama list` komutunu çalıştırarak indirdiğiniz Ollama modellerinin listesini görebilirsiniz.
* **Donanım gereksinimleri:** Büyük dil modellerini çalıştırmak önemli hesaplama kaynakları (CPU, bellek, GPU) gerektirir, bilgisayarınızın model gereksinimlerini karşıladığından emin olun.
* **Ollama belgeleri:** Yapılandırma sayfasındaki `Ollama belgelerini ve modellerini görüntüle` bağlantısına tıklayarak doğrudan Ollama resmi belgelerine ulaşabilirsiniz.