
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Otomatik MCP Kurulumu

> Otomatik MCP kurulumu için Cherry Studio'nun v1.1.18 veya üzeri sürüme yükseltilmesi gerekir.

## Özellik Tanımı

Manuel kuruluma ek olarak, Cherry Studio dahili `@mcpmarket/mcp-auto-install` aracını barındırır. Bu, MCP sunucularını kurmak için daha kolay bir yöntemdir. Desteklenen MCP hizmeti olan büyük dil modeli diyaloglarında ilgili komutu girmeniz yeterlidir.

{% hint style="warning" %}
**Test Aşaması Uyarıları:**

* `@mcpmarket/mcp-auto-install` halen test aşamasındadır
* Sonuçlar büyük dil modellerinin "zekasına" bağlıdır; bazıları otomatik eklerken bazı durumlarda **MCP ayarlarında bazı parametreleri manuel değiştirmek gerekebilir**
* Şu anda arama kaynağı @modelcontextprotocol üzerinden yapılır, kendi yapılandırmanızı uygulayabilirsiniz (aşağıda açıklanmıştır)
{% endhint %}

## Kullanım Talimatları

Örneğin şunu girebilirsiniz:

```
bana bir filesystem mcp sunucusu kur
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCP sunucusu kurmak için komut girin</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP sunucusu yapılandırma ekranı</p></figcaption></figure>

Sistem gereksiniminizi otomatik algılayacak ve `@mcpmarket/mcp-auto-install` aracılığıyla kurulumu tamamlayacaktır. Bu araç çeşitli MCP sunucu türlerini destekler:

* filesystem (dosya sistemi)
* fetch (ağ isteği)
* sqlite (veritabanı)
* vb.

> MCP_PACKAGE_SCOPES değişkeniyle MCP hizmet arama kaynakları özelleştirilebilir. Varsayılan değer: `@modelcontextprotocol`

## `@mcpmarket/mcp-auto-install` Kütüphanesi Tanımı

{% hint style="info" %}
**Varsayılan yapılandırma referansı:**

```json
// `axun-uUpaWEdMEMU8C61K` servis kimliğidir, özelleştirilebilir
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "MCP hizmetlerini otomatik kur (Beta sürümü)",
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
    "MCP_REGISTRY_PATH": "Ayrıntılar için bkz: https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` açık kaynaklı bir npm paketidir. Detaylı bilgi ve kullanım dokümanları için [npm resmi deposunu](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) inceleyebilirsiniz. `@mcpmarket`, Cherry Studio'nun resmi MCP hizmet koleksiyonunu temsil eder.
{% endhint %}