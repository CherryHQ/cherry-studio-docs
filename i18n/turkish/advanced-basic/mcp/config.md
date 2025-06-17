
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# MCP Yapılandırması ve Kullanımı

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1.  Cherry Studio ayarlarını açın.
2.  `MCP Sunucusu` seçeneğini bulun.
3.  `Sunucu Ekle`'ye tıklayın.
4.  MCP Sunucusu ile ilgili parametreleri doldurun ([referans bağlantı](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Doldurulması gerekebilecek içerikler şunları içerir:
   * Ad: Özel bir ad, örneğin `fetch-server`
   * Tür: `STDIO` seçin
   * Komut: `uvx` yazın
   * Parametreler: `mcp-server-fetch` yazın
   * (Belirli Sunucuya bağlı olarak başka parametreler de olabilir)
5.  `Kaydet`'e tıklayın.

{% hint style="success" %}
Yukarıdaki yapılandırmayı tamamladıktan sonra, Cherry Studio otomatik olarak gerekli MCP Sunucusu'nu - `fetch server` indirecektir. İndirme tamamlandıktan sonra kullanmaya başlayabiliriz! Not: mcp-server-fetch yapılandırması başarılı olmazsa, bilgisayarınızı yeniden başlatmayı deneyebilirsiniz.
{% endhint %}

### Sohbet Kutusunda MCP Hizmetini Etkinleştirme

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* `MCP Sunucusu` ayarlarında MCP sunucusu başarıyla eklendi

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Kullanım Etkisi Gösterimi**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Yukarıdaki görselden de görülebileceği gibi, MCP'nin `fetch` işlevi ile birleştirildiğinde, Cherry Studio kullanıcının sorgu niyetini daha iyi anlayabilir, internetten ilgili bilgileri alabilir ve daha doğru, daha kapsamlı yanıtlar verebilir.