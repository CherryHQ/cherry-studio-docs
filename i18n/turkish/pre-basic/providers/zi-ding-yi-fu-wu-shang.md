
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Özel Sağlayıcılar

Cherry Studio sadece ana akım AI model hizmetlerini entegre etmekle kalmaz, aynı zamanda size güçlü özelleştirme yetenekleri sunar. **Özel AI Sağlayıcılar** özelliği sayesinde, ihtiyaç duyduğunuz herhangi bir AI modelini kolayca entegre edebilirsiniz.

## Neden Özel AI Sağlayıcılara İhtiyacınız Var?

* **Esneklik:** Önceden tanımlanmış sağlayıcı listesiyle sınırlı kalmadan, ihtiyaçlarınıza en uygun AI modelini özgürce seçebilirsiniz.
* **Çeşitlilik:** Farklı platformlardaki çeşitli AI modellerini deneyerek benzersiz avantajlarını keşfedebilirsiniz.
* **Kontrol:** API anahtarlarınızı ve erişim adreslerinizi doğrudan yöneterek güvenlik ve gizliliği sağlayabilirsiniz.
* **Özelleştirme:** Belirli iş senaryolarını karşılamak için özel dağıtılmış modelleri entegre edebilirsiniz.

## Özel AI Sağlayıcı Nasıl Eklenir?

Cherry Studio'ya özel AI sağlayıcınızı eklemek için birkaç basit adım yeterlidir:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Ayarları Açın:** Cherry Studio arayüzünde sol gezinti çubuğundaki "Ayarlar" (dişli simgesi) seçeneğine tıklayın.
2. **Model Hizmetlerine Girin:** Ayarlar sayfasında "Model Hizmetleri" sekmesini seçin.
3. **Sağlayıcı Ekle:** "Model Hizmetleri" sayfasında mevcut sağlayıcı listesini göreceksiniz. Listenin altındaki "+ Ekle" düğmesine tıklayarak "Sağlayıcı Ekle" açılır penceresini açın.
4. **Bilgileri Doldurun:** Açılır pencerede aşağıdaki bilgileri girmeniz gerekir:
   * **Sağlayıcı Adı:** Özel sağlayıcınız için kolayca tanımlanabilir bir ad girin (örneğin: BenimOpenAI).
   * **Sağlayıcı Tipi:** Açılır listeden sağlayıcı tipinizi seçin. Şu anda desteklenenler:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Yapılandırmayı Kaydet:** Girdikten sonra "Ekle" düğmesine tıklayarak yapılandırmanızı kaydedin.

## Özel AI Sağlayıcı Yapılandırma

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Ekleme tamamlandıktan sonra, listede yeni eklediğiniz sağlayıcıyı bulup detaylı yapılandırma yapmanız gerekir:

1. **Etkin Durum:** Özel sağlayıcı listesinin en sağında bir etkinleştirme anahtarı vardır. Açık konum, bu özel hizmetin etkin olduğu anlamına gelir.
2. **API Anahtarı:**
   * AI sağlayıcınızın verdiği API Anahtarını (API Key) girin.
   * Sağdaki "Kontrol" düğmesine tıklayarak anahtarın geçerliliğini doğrulayabilirsiniz.
3. **API Adresi:**
   * AI hizmetinin API erişim adresini (Base URL) girin.
   * Mutlaka AI sağlayıcınızın resmi belgelerine başvurarak doğru API adresini alın.
4.  **Model Yönetimi:**

    * "+ Ekle" düğmesine tıklayarak bu sağlayıcı altında kullanmak istediğiniz model kimliklerini (`gpt-3.5-turbo`, `gemini-pro` gibi) manuel olarak ekleyin.

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * Kesin model adından emin değilseniz, AI sağlayıcınızın resmi belgelerine başvurun.
    * "Yönet" düğmesiyle eklenen modelleri düzenleyebilir veya silebilirsiniz.

## Kullanmaya Başlayın

Yukarıdaki yapılandırmayı tamamladıktan sonra, Cherry Studio'nun sohbet arayüzünde özel AI sağlayıcınızı ve modelinizi seçerek AI ile iletişime başlayabilirsiniz!

## Özel AI Sağlayıcı Olarak vLLM Kullanımı

vLLM, Ollama benzeri hızlı ve kullanımı kolay bir LLM çıkarım kütüphanesidir. vLLM'yi Cherry Studio'ya entegre etme adımları şunlardır:

1.  **vLLM Kurulumu:** vLLM resmi belgelerini ([https://docs.vllm.ai/en/latest/getting\_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)) takip ederek vLLM'yi kurun.

    ```sh
    pip install vllm # pip kullanıyorsanız
    uv pip install vllm # uv kullanıyorsanız
    ```
2.  **vLLM Hizmetini Başlatın:** vLLM'nin sağladığı OpenAI uyumlu arayüzü kullanarak hizmeti başlatın. Başlıca iki yol vardır:

    * `vllm.entrypoints.openai.api_server` ile başlatma

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * `uvicorn` ile başlatma

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Hizmetin başarıyla başladığından ve varsayılan `8000` portunda dinlediğinden emin olun. Tabii ki, `--port` parametresiyle vLLM hizmet portunu belirtebilirsiniz.

3. **Cherry Studio'ya vLLM Sağlayıcı Ekleyin:**
   * Yukarıda anlatıldığı gibi Cherry Studio'ya yeni bir özel AI sağlayıcı ekleyin.
   * **Sağlayıcı Adı:** `vLLM`
   * **Sağlayıcı Tipi:** `OpenAI` seçin.
4. **vLLM Sağlayıcısını Yapılandırın:**
   * **API Anahtarı:** vLLM API anahtarı gerektirmediğinden, bu alanı boş bırakabilir veya herhangi bir şey girebilirsiniz.
   * **API Adresi:** vLLM hizmetinin API adresini girin. Varsayılan olarak adres şudur: `http://localhost:8000/` (farklı port kullanıyorsanız buna göre değiştirin).
   * **Model Yönetimi:** vLLM'de yüklediğiniz model adını ekleyin. Yukarıdaki `python -m vllm.entrypoints.openai.api_server --model gpt2` örneğinde, buraya `gpt2` girmelisiniz.
5. **Sohbete Başlayın:** Artık Cherry Studio'da vLLM sağlayıcısını ve `gpt2` modelini seçerek vLLM destekli bir LLM ile iletişime başlayabilirsiniz!

## İpuçları ve Öneriler

* **Belgeleri Dikkatlice Okuyun:** Özel sağlayıcı eklemeden önce mutlaka kullandığınız AI sağlayıcısının resmi belgelerini okuyun. API anahtarı, erişim adresi, model adı gibi kritik bilgileri öğrenin.
* **API Anahtarını Kontrol Edin:** "Kontrol" düğmesini kullanarak API anahtarının geçerliliğini hızlıca doğrulayın. Hatalı anahtar nedeniyle kullanılamama sorununu önleyin.
* **API Adresine Dikkat Edin:** Farklı AI sağlayıcıları ve modeller için API adresleri değişebilir. Mutlaka doğru adresi girdiğinizden emin olun.
* **Modelleri İhtiyaca Göre Ekleyin:** Yalnızca gerçekten kullanacağınız modelleri ekleyin, fazladan gereksiz model eklemekten kaçının.