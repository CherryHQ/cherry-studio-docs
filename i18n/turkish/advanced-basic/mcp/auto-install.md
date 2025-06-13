
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Otomatik MCP Kurulumu

> Otomatik MCP kurulumu için Cherry Studio'nun v1.1.18 veya üzeri sürüme yükseltilmesi gerekir.

## Özellik Tanıtımı

Manuel kuruluma ek olarak, Cherry Studio içinde `@mcpmarket/mcp-auto-install` aracı bulunmaktadır. Bu, MCP sunucusunu kurmak için daha kolay bir yöntemdir. MCP hizmetini destekleyen büyük dil modeli sohbetlerinde ilgili komutu girmeniz yeterlidir.

{% hint style="warning" %}
**Test Aşaması Hatırlatması:**

* `@mcpmarket/mcp-auto-install` şu anda hala test aşamasındadır
* Sonuçlar büyük dil modellerinin "zekasına" bağlıdır; bazıları otomatik eklerken, bazılarında **MCP ayarlarında belirli parametreleri manuel değiştirmek gerekebilir**
* Şu anda arama kaynağı @modelcontextprotocol üzerinden yapılmaktadır, elle yapılandırılabilir (aşağıda açıklanmıştır)
{% endhint %}

## Kullanım Talimatları

Örneğin şunu girebilirsiniz:

```
bana bir filesystem mcp sunucusu kur
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCP sunucusunu kurmak için komut girin</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP sunucu yapılandırma arayüzü</p></figcaption></figure>

Sistem ihtiyacınızı otomatik tanır ve `@mcpmarket/mcp-auto-install` ile kurulumu tamamlar. Bu araç çeşitli MCP sunucu türlerini destekler:

* filesystem (dosya sistemi)
* fetch (ağ isteği)
* sqlite (veritabanı)
* vb...

> MCP_PACKAGE_SCOPES değişkeni MCP hizmet arama kaynağını özelleştirebilir. Varsayılan değer: `@modelcontextprotocol`

## `@mcpmarket/mcp-auto-install` Kütüphanesi Tanıtımı

{% hint style="info" %}
**Varsayılan Yapılandırma Referansı:**

```json
// `axun-uUpaWEdMEMU8C61K` hizmet kimliğidir, özelleştirilebilir
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "MCP hizmetlerini otomatik kurar (Beta sürümü)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "Detaylar için https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` açık kaynaklı bir npm paketidir. Detaylı bilgi ve kullanım dokümanları için [npm resmi deposuna](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) bakabilirsiniz. `@mcpmarket`, Cherry Studio'nun resmi MCP hizmet koleksiyonudur.
{% endhint %}