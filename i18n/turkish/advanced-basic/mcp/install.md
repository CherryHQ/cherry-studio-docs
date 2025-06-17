
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# MCP Ortam Kurulumu

**MCP (Model Context Protocol)**, büyük dil modellerine (LLM) bağlamsal bilgi sağlamak için standartlaştırılmış bir yol sunan açık kaynaklı bir protokoldür. MCP hakkında daha fazla bilgi için bkz. [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Cherry Studio'da MCP Kullanımı

Aşağıda `fetch` işlevi örneğiyle Cherry Studio'da MCP'nin nasıl kullanılacağı gösterilmiştir, detaylar için [dokümantasyonu](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) inceleyebilirsiniz.

### **Hazırlık Adımları: uv ve bun Kurulumu**

{% hint style="warning" %}
Cherry Studio şu anda yalnızca dahili [uv](https://github.com/astral-sh/uv) ve [bun](https://github.com/oven-sh/bun) kullanır ve sistemde zaten kurulu olan uv ve bun'u **yeniden kullanmaz**.
{% endhint %}

`Ayarlar - MCP Sunucusu` bölümünde `Kur` düğmesine tıklayarak otomatik indirme ve kurulum yapın. Doğrudan GitHub'dan indirildiği için hız yavaş olabilir ve başarısızlık olasılığı yüksektir. Kurulumun başarısı aşağıda belirtilen klasörde dosya varlığıyla doğrulanır.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Yürütülebilir Dosyaların Kurulum Dizini:**

Windows: `C:\Users\kullanıcıadı\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin dizini</p></figcaption></figure>

**Kurulumun Başarısız Olması Durumunda:**

Sistemdeki ilgili komutları sembolik bağlantıyla buraya yönlendirebilirsiniz. İlgili dizin yoksa manuel oluşturun veya yürütülebilir dosyaları manuel indirip bu dizine yerleştirin:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)