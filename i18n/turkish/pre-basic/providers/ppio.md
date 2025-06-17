
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

```markdown
# PPIO Paiou Cloud

## Cherry Studio Entegrasyonu ile PPIO LLM API Kullanımı

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Eğitim Genel Bakışı <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio, şu anda desteklenen çoklu model masaüstü istemcisidir: Windows, Linux, MacOS sistemleri için kurulum paketleri. Ana akım LLM modellerini birleştirir ve çoklu senaryo desteği sunar. Kullanıcılar akıllı sohbet yönetimi, açık kaynaklı özelleştirme ve çoklu tema arayüzleriyle çalışma verimliliğini artırabilir.

Cherry Studio artık **PPIO Yüksek Performanslı API Kanalı** ile derinlemesine entegredir. Kurumsal düzeyde hesaplama güvencesiyle **DeepSeek-R1/V3 yüksek hızlı yanıt** ve **%99.9 hizmet kullanılabilirliği** sağlayarak hızlı ve akıcı bir deneyim sunar.

Aşağıdaki eğitim, tam entegrasyon çözümünü (anahtar yapılandırması dahil) içerir. 3 dakikada **"Cherry Studio Akıllı Yönlendirme + PPIO Yüksek Performanslı API"** ileri seviye modunu başlatın.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. CherryStudio'ya Girin ve "PPIO" Model Sağlayıcısı Ekleyin <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Öncelikle resmi web sitesinden Cherry Studio'yu indirin: [https://cherry-ai.com/download](https://cherry-ai.com/download) (Erişilemiyorsa, aşağıdaki Quark bulut bağlantısından kendi ihtiyacınıza uygun sürümü indirebilirsiniz: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Sol alt köşedeki ayarlara tıklayın, özel sağlayıcı adını girin: `PPIO`, "Onayla"ya tıklayın

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) [Paiou Bulut API Anahtar Yönetimi](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio)'ne gidin. 【Kullanıcı avatarı】—【API Anahtar Yönetimi】'ne tıklayarak kontrol paneline girin

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Yeni bir API anahtarı oluşturmak için 【+ Oluştur】 düğmesine tıklayın. Özel bir anahtar adı belirleyin. **Oluşturulan anahtar yalnızca oluşturma sırasında görüntülenir. Sonraki kullanımları etkilememek için mutlaka kopyalayın ve bir belgeye kaydedin**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) CherryStudio'da anahtarı girin. Ayarlar'ı seçin, 【PPIO Paiou Cloud】'u seçin, resmi web sitesinde oluşturulan API anahtarını girin ve 【Kontrol Et】'e tıklayın

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Model seçin: deepseek/deepseek-r1/community örneğini kullanın. Diğer modellerle değiştirmek isterseniz doğrudan değiştirebilirsiniz

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 ve V3 community sürümleri sadece deneme amaçlıdır ve tam parametreli tam sürüm modellerdir. Kararlılık ve etkililik açısından fark yoktur. Büyük ölçekli çağrılar için **ödeme yaparak community olmayan sürüme geçmelisiniz**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Model Kullanım Yapılandırması <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) 【Kontrol Et】 tıkladığınızda bağlantı başarılı görüntülenirse normal kullanıma hazırsınız demektir

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Son olarak 【@】 simgesine tıklayarak PPIO sağlayıcısı altında eklenen DeepSeek R1 modelini seçin, böylece sohbete başlayabilirsiniz \~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Bazı materyaller kaynak: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. PPIO×Cherry Studio Video Kullanım Eğitimi <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Daha görsel bir öğrenim tercih ederseniz, Bilibili'de video eğitim hazırladık. Adım adım öğretimle **"PPIO API + Cherry Studio"** yapılandırmasını hızla kavramanıza yardımcı olacaktır. Aşağıdaki bağlantıdan videoya ulaşın, akıcı geliştirme deneyimine başlayın → [《【Sinir bozucu dönüp durmalardan bıktınız mı?】Paiou Cloud + DeepSeek Tam Sürüm =? Tıkanıklık Yok, Anında Kalkış》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Video materyal kaynağı: sola】
```