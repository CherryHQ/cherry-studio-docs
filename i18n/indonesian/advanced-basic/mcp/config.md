
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Konfigurasi dan Penggunaan MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Buka Pengaturan Cherry Studio.
2. Temukan opsi `MCP Server`.
3. Klik `Tambah Server`.
4. Isi parameter terkait MCP Server ([referensi](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Konten yang mungkin perlu diisi:
   * Nama: Tentukan nama kustom, misalnya `fetch-server`
   * Tipe: Pilih `STDIO`
   * Perintah: Isi `uvx`
   * Parameter: Isi `mcp-server-fetch`
   * (Mungkin ada parameter lain tergantung pada Server spesifik)
5. Klik `Simpan`.

{% hint style="success" %}
Setelah konfigurasi di atas, Cherry Studio akan otomatis mengunduh MCP Server yang dibutuhkan - `fetch server`. Setelah pengunduhan selesai, kita bisa mulai menggunakannya! Catatan: Jika konfigurasi mcp-server-fetch tidak berhasil, coba restart komputer.
{% endhint %}

### Mengaktifkan Layanan MCP di Kotak Obrolan

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Server MCP telah berhasil ditambahkan di pengaturan `MCP Server`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demonstrasi Hasil Penggunaan**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Dari gambar di atas dapat dilihat, dengan mengintegrasikan fungsi `fetch` MCP, Cherry Studio mampu lebih baik memahami maksud kueri pengguna, mengambil informasi relevan dari internet, dan memberikan jawaban yang lebih akurat serta komprehensif.