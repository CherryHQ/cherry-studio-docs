
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Instalasi Otomatis MCP

> Instalasi otomatis MCP memerlukan upgrade Cherry Studio ke versi v1.1.18 atau lebih tinggi.

## Pengenalan Fitur

Selain instalasi manual, Cherry Studio juga menyertakan alat `@mcpmarket/mcp-auto-install`, metode instalasi server MCP yang lebih praktis. Anda hanya perlu memasukkan perintah yang sesuai pada dialog model besar yang mendukung layanan MCP.

{% hint style="warning" %}
**Peringatan tahap pengujian:**

* `@mcpmarket/mcp-auto-install` saat ini masih dalam tahap pengujian
* Efektivitasnya bergantung pada "kecerdasan" model besar - beberapa akan menambahkan secara otomatis, beberapa masih **perlu diubah parameternya secara manual di pengaturan MCP**
* Saat ini sumber pencarian berasal dari @modelcontextprotocol, dapat dikonfigurasi sendiri (penjelasan di bawah)
{% endhint %}

## Petunjuk Penggunaan

Misalnya, Anda dapat memasukkan:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Memasukkan perintah untuk instalasi server MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Antarmuka konfigurasi server MCP</p></figcaption></figure>

Sistem akan secara otomatis mengenali kebutuhan Anda dan menyelesaikan instalasi melalui `@mcpmarket/mcp-auto-install`. Alat ini mendukung berbagai jenis server MCP, termasuk tetapi tidak terbatas pada:

* filesystem (sistem file)
* fetch (permintaan jaringan)
* sqlite (basis data)
* dan lainnya...

> Variabel MCP_PACKAGE_SCOPES dapat menyesuaikan sumber pencarian layanan MCP, nilai default: `@modelcontextprotocol`, dapat dikonfigurasi sesuai kebutuhan.

## Pengenalan Pustaka `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Referensi konfigurasi default:**

```json
// `axun-uUpaWEdMEMU8C61K` adalah ID layanan, bisa disesuaikan
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Menginstal layanan MCP secara otomatis (Versi Beta)",
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
    "MCP_REGISTRY_PATH": "Detail lihat https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` adalah paket npm sumber terbuka. Anda dapat melihat detail dan dokumentasi penggunaannya di [repositori resmi npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` merupakan koleksi layanan MCP resmi Cherry Studio.
{% endhint %}