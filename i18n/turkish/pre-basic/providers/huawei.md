
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Huawei Cloud

## Bir: [Huawei Cloud](https://auth.huaweicloud.com/authui/login)'da hesap oluşturup giriş yapın

## İki: [Bu bağlantıya](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) tıklayarak MaaS kontrol paneline gidin

## Üç: Yetkilendirme

<details>

<summary>Yetkilendirme adımları (zaten yetkiliyse atlayın)</summary>

1. (İki)'deki bağlantıya girdikten sonra, yönlendirmeleri takip ederek yetkilendirme sayfasına gidin (IAM alt kullanıcılar → Yetkilendirme ekle → Normal kullanıcı)

![](<../../.gitbook/assets/image (49).png>)

2. Oluşturduktan sonra (İki)'deki bağlantıya geri dönün
3. Erişim yetkiniz olmadığına dair uyarı alacaksınız, uyarıdaki "buraya tıklayın" butonuna basın
4. Mevcut yetkilendirmeye ek yapın ve onaylayın

![](<../../.gitbook/assets/image (50).png>)

&#x20;Not: Bu yöntem yeni başlayanlar için tasarlanmıştır, aşırı detay okumanız gerekmez. Sadece yönlendirmeleri takip edip tıklayın. Tek seferde yetkilendirmeyi başarıyorsanız kendi yönteminizi kullanabilirsiniz.

</details>

## Dört: Yan menüden "Yetkilendirme Yönetimi"ne tıklayın, API Anahtarı (gizli anahtar) oluşturun ve kopyalayın

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Ardından CherryStudio'da yeni sağlayıcı oluşturun

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Oluşturduktan sonra gizli anahtarı girin

## Beş: Yan menüden "Model Dağıtımı"na tıklayın, tümünü talep edin

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

## Altı: "Çağrı Yap"a tıklayın

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

① numaralı alandaki adresi kopyalayıp CherryStudio'nun sağlayıcı adresi alanına yapıştırın ve sonuna "#" işareti ekleyin

sonuna "#" işareti ekleyin

sonuna "#" işareti ekleyin

sonuna "#" işareti ekleyin

sonuna "#" işareti ekleyin

Neden "#" eklendiğini [buradan öğrenin](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Tabii ki bakmadan da yapabilirsiniz, direkt eğitimdeki gibi işlemi uygulayın;
>
> v1/chat/completions kısmını silme yöntemiyle de doldurabilirsiniz. Nasıl doldurmayı biliyorsanız istediğiniz şekilde doldurabilirsiniz, bilmiyorsanız mutlaka eğitimdeki adımları uygulayın.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Ardından ② numaralı model adını kopyalayıp CherryStudio'da "+Ekle" butonuna basarak yeni model oluşturun

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Model adını girin, ekleme yapmayın, tırnak içine almayın. Örnekte nasıl yazılıyorsa aynen kopyalayın.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

"Model ekle" butonuna tıklayarak tamamlayın.

{% hint style="info" %}
Huawei Cloud'da her modelin adresi farklı olduğundan, her model için yeni bir sağlayıcı oluşturmanız gerekir. Yukarıdaki adımları her model için tekrarlayın.
{% endhint %}