---
hidden: True
icon: code
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Kod Yapısı

```yaml
...
├─ docs/ #belgeler dizini
├─ resources/ #kaynak dosyaları dizini
├─ scripts/ #betik dosyaları dizini
└─ src/ #ana kaynak kod dizini
    ├─main/ #ana işlem kodu
    ├─preload/ #önceden yükleme betiği dizini
    └─renderer/ #render işlem kodu
        ├─src/ #render işleminin kaynak kodu
            ├─assets/ #kaynak dosyaları
                ├─fonts/ #yazı tipi dosyaları
                ├─images/ #profil resimleri vb. resim dosyaları
                └─styles/ #stil dosyaları
            ├─components/ #bileşenler
            ├─config/ #yapılandırma dosyaları
            ├─context/ #bağlam
            ├─databases/ #veritabanı ile ilgili dosyalar
            ├─hooks/ #özel Hook'lar
            ├─i18n/ #uluslararasılaştırma dosyaları
            ├─pages/ #sayfa dosyaları
            ├─providers/ #hizmet sağlayıcı ile ilgili yapılandırma
            ├─services/ #hizmet dosyaları
            ├─store/ #durum yönetimi dosyaları
            ├─types/ #TypeScript tip tanım dosyaları
            ├─utils/ #yardımcı fonksiyonlar
            ...
        ...
    ...
...

```