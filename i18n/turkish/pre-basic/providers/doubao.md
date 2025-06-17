
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# ByteDance (Doubao)

*   [Volcengine](https://console.volcengine.com/)'de oturum açın
*   Doğrudan [buraya tıklayarak erişin](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### API Anahtarı Alma

*   Yan çubuk altındaki [API Anahtarı Yönetimi](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey)'ne tıklayın
*   API Anahtarı oluşturun

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   Başarıyla oluşturulduktan sonra, oluşturulan API Anahtarı yanındaki 👁️ simgesine tıklayıp görüntüleyin ve kopyalayın

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Kopyalanan API Anahtarını CherryStudio'ya yapıştırdıktan sonra sağlayıcı anahtarını açın

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Modelleri Etkinleştirme ve Ekleme

*   [Etkinleştirme Yönetimi](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false)'nde (konsol yan çubuğu en altı) kullanmak istediğiniz modelleri etkinleştirin; Doubao serisi ve DeepSeek gibi modelleri ihtiyacınıza göre etkinleştirebilirsiniz

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   [Model Listesi Dökümanı](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)'nda ihtiyacınız olan modelin karşılık gelen Model Kimliğini bulun

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Volcengine Model Kimliği Listesi Örneği"><figcaption></figcaption></figure>

*   Cherry Studio'nun [Model Servisleri](../../cherrystudio/preview/settings/providers.md) ayarlarından Volcengine'i bulun
*   "Ekle"ye tıklayıp, önceki adımda aldığınız Model Kimliğini ilgili metin kutusuna kopyalayın

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Bu süreci izleyerek modelleri tek tek ekleyin

### API Adresi

API adresinin iki yazım biçimi vardır:

*   İlki istemci tarafından varsayılan olarak kullanılan: `https://ark.cn-beijing.volces.com/api/v3/`
*   İkinci yazım biçimi: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
İki yazım biçimi arasında fark yoktur, varsayılanı korumanız yeterlidir, değiştirmeniz gerekmez.

Sonundaki `/` ve `#` farkı hakkında detay için servis sağlayıcı ayarlarındaki [API Adresi bölümüne bakın](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Resmi Dökümandan cURL Örneği</p></figcaption></figure>