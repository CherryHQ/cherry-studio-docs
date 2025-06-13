---
icon: book-bookmark
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Bilgi Bilimi

## Token Nedir?

Tokenler, AI modellerinin metni işlemede kullandığı temel birimlerdir ve modelin "düşünme"nin en küçük parçası olarak anlaşılabilir. Tam olarak karakter veya kelimelerle eşleşmez; modelin kendine özgü bir metin bölümleme yöntemidir.

#### 1. Çince Segmentasyon
* Bir Çince karakter genellikle 1-2 token olarak kodlanır
* Örneğin: `"你好"` ≈ 2-4 token

#### 2. İngilizce Segmentasyon
* Yaygın kelimeler genellikle 1 token olur
* Uzun veya nadir kelimeler birden fazla tokene bölünür
* Örneğin:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 token

#### 3. Özel Karakterler
* Boşluklar, noktalama işaretleri de token kullanır
* Satır sonu genellikle 1 token'dır

{% hint style="info" %}
Farklı servis sağlayıcıların Tokenizer'ları farklıdır, hatta aynı sağlayıcıdaki farklı modellerin Tokenizer'ları da değişiklik gösterir. Bu bilgi yalnızca token kavramını açıklamak içindir.
{% endhint %}

***

## Tokenizer Nedir?

Tokenizer (Segmentasyon Aracı), AI modelinin metni tokenlere dönüştürdüğü araçtır. Girdi metninin model tarafından anlaşılabilir en küçük birimlere nasıl bölüneceğini belirler.

### Neden Farklı Modellerin Tokenizer'ları Farklıdır?

#### 1. Eğitim Verileri Farklıdır
* Farklı dil külliyatları optimizasyon yönünü değiştirir
* Çok dilli destek seviyeleri farklılık gösterir
* Belirli alanlara (tıp, hukuk vb.) özel optimizasyonlar

#### 2. Segmentasyon Algoritmaları Farklıdır
* BPE (Byte Pair Encoding) - OpenAI GPT serisi
* WordPiece - Google BERT
* SentencePiece - Çok dilli senaryolara uygun

#### 3. Optimizasyon Hedefleri Farklıdır
* Bazıları sıkıştırma verimliliğine odaklanır
* Bazıları anlamsal korumaya öncelik verir
* Bazıları işleme hızını önemser

### Pratik Etkisi

Aynı metin farklı modellerde farklı sayıda token üretebilir:
```
Girdi: "Hello, world!"
GPT-3: 4 token
BERT: 3 token
Claude: 3 token
```

***

## Gömme Modelleri (Embedding Model) Nedir?

**Temel Kavram:** Gömme modelleri, yüksek boyutlu kesikli verileri (metin, görüntü vb.) düşük boyutlu sürekli vektörlere dönüştüren bir tekniktir. Bu dönüşüm, makinelerin karmaşık verileri daha iyi anlamasını ve işlemesini sağlar. Tıpkı karmaşık bir yapbozu basit bir koordinat noktasına indirgemek gibi, ancak bu nokta yapbozun temel özelliklerini korur. Büyük model ekosisteminde "çevirmen" rolü üstlenerek insan tarafından anlaşılabilir bilgiyi AI'nın hesaplayabileceği sayısal forma çevirir.

**Çalışma Prensibi:** Doğal dil işlemede, gömme modelleri kelimeleri vektör uzayında belirli konumlara eşler. Bu uzayda anlamsal olarak yakın kelimeler otomatik olarak gruplanır. Örneğin:
* "Kral" ve "Kraliçe" vektörleri birbirine yakın olacaktır
* "Kedi" ve "Köpek" gibi evcil hayvan isimleri de yakın mesafede bulunur
* "Araba" ve "Ekmek" gibi anlamsal ilişkisi olmayan kelimeler uzakta konumlanır

**Başlıca Kullanım Alanları:**
* Metin analizi: Belge sınıflandırma, duygu analizi
* Öneri sistemleri: Kişiselleştirilmiş içerik önerileri
* Görüntü işleme: Benzer resim arama
* Arama motorları: Anlamsal arama optimizasyonu

**Temel Avantajlar:**
1. Boyut indirgeme: Karmaşık veriyi işlenebilir vektör formuna sadeleştirme
2. Anlamsal koruma: Orijinal verideki temel anlam bilgisini saklama
3. Hesaplama verimliliği: Makine öğrenimi modellerinin eğitim ve çıkarım verimliliğini önemli ölçüde artırma

**Teknolojik Değer:** Gömme modelleri modern AI sistemlerinin temel bileşenleridir. Makine öğrenimi görevleri için yüksek kaliteli veri temsili sağlayarak doğal dil işleme, bilgisayarlı görü gibi alanlardaki gelişmeleri yönlendiren kilit teknolojidir.

***

## Bilgi Arama Sistemlerinde Gömme Modellerinin Çalışma Prensibi

**Temel İş Akışı:**

1. **Bilgi bankası ön işleme aşaması**
   * Belgeler uygun boyutlarda chunk'lara (metin blokları) bölünür
   * Her chunk gömme modeli kullanılarak vektöre dönüştürülür
   * Vektörler ve orijinal metinler vektör veritabanına kaydedilir

2. **Sorgu işleme aşaması**
   * Kullanıcı sorusu vektöre dönüştürülür
   * Vektör bankasında benzer içerikler taranır
   * Bulunan ilgili içerik LLM'e bağlam olarak sağlanır

***

## **MCP (Model Context Protocol) Nedir?**

MCP, büyük dil modellerine (LLM) standartlaştırılmış şekilde bağlam bilgisi sağlamayı amaçlayan açık kaynaklı bir protokoldür.

* **Analoji:** MCP'yi AI dünyasının "USB bellek"i olarak düşünebilirsiniz. USB bellekler çeşitli dosyaları saklar ve bilgisayara takıldığında kullanılabilir. Benzer şekilde, MCP Sunucusu'na çeşitli "eklentiler" takılabilir. LLM'ler ihtiyaç duydukça bu eklentileri MCP Sunucusu'ndan talep ederek daha zengin bağlam bilgisine erişebilir ve yeteneklerini geliştirebilir.
* **Fonksiyon Araçlarıyla Karşılaştırma:** Geleneksel Fonksiyon Araçları (Function Tools) da LLM'lere harici işlevler sağlayabilir, ancak MCP daha yüksek seviyeli bir soyutlamadır. Fonksiyon Araçları belirli görevlere yönelikken, MCP daha genel ve modüler bir bağlam edinim mekanizması sunar.

### **MCP'nin Temel Avantajları**

1. **Standardizasyon:** Farklı LLM'ler ve bağlam sağlayıcıların sorunsuz çalışması için birleşik arayüz ve veri formatı sunar.
2. **Modülerlik:** Bağlam bilgisini bağımsız modüllere (eklentiler) bölerek yönetimi ve yeniden kullanımı kolaylaştırır.
3. **Esneklik:** LLM'ler ihtiyaçlarına göre dinamik olarak bağlam eklentileri seçerek daha akıllı ve kişiselleştirilmiş etkileşim sağlar.
4. **Ölçeklenebilirlik:** Gelecekte daha fazla bağlam eklentisi türü eklenebilecek şekilde tasarlanmıştır, LLM'lerin yetenek genişletmesi için sınırsız olanak sunar.

***