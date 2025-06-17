
{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Dahili MCP Yapılandırması

### @cherry/mcp-auto-install

MCP hizmetini otomatik olarak yükler (beta sürüm)

### @cherry/memory

Yerel bilgi grafiğine dayalı kalıcı bellek temel uygulaması. Bu, modelin farklı konuşmalar arasında kullanıcıyla ilgili bilgileri hatırlamasını sağlar.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Yapılandırılmış düşünce süreci aracılığıyla dinamik ve yansıtmalı problem çözme araçları sunan bir MCP sunucu uygulaması.

### @cherry/brave-search

Brave arama API'sini entegre eden ve hem web hem de yerel arama işlevselliği sunan bir MCP sunucu uygulaması.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

URL'lerin web sayfası içeriğini getirmek için kullanılan MCP sunucusu.

### @cherry/filesystem

Dosya sistemi işlemlerini uygulayan Model Context Protocol (MCP) için Node.js sunucusu.