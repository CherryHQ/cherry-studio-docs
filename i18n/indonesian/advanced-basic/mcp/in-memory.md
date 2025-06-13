
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Konfigurasi MCP Bawaan

### @cherry/mcp-auto-install

Layanan instalasi otomatis MCP (versi beta)

### @cherry/memory

Implementasi dasar memori persisten berbasis grafik pengetahuan lokal. Ini memungkinkan model untuk mengingat informasi pengguna yang relevan di antara percakapan yang berbeda.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Implementasi server MCP yang menyediakan alat untuk pemecahan masalah dinamis dan reflektif melalui proses berpikir terstruktur.

### @cherry/brave-search

Implementasi server MCP yang mengintegrasikan API Pencarian Brave, menyediakan fungsi ganda untuk pencarian web dan lokal.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

Server MCP untuk mengambil konten halaman web dari URL.

### @cherry/filesystem

Server Node.js yang mengimplementasikan Model Context Protocol (MCP) untuk operasi sistem file.