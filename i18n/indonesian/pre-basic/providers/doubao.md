
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# ByteDance (Doubao)

*   Masuk ke [Mesin Vulkanik](https://console.volcengine.com/)
*   Klik langsung [di sini](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Mendapatkan Kunci API

*   Klik [Manajemen Kunci API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) di bilah samping bawah
*   Buat Kunci API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   Setelah berhasil dibuat, klik ikon mata di sebelah Kunci API untuk menampilkan dan menyalin

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Tempelkan Kunci API yang disalin ke CherryStudio, lalu nyalakan sakelar penyedia layanan

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Mengaktifkan dan Menambahkan Model

*   Di [Manajemen Aktivasi](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) (bagian bawah bilah samping Konsol Ark), aktifkan model yang dibutuhkan seperti seri Doubao dan DeepSeek sesuai kebutuhan

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   Di [Dokumen Daftar Model](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), temukan ID Model yang sesuai dengan model yang Anda butuhkan

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Contoh Daftar ID Model Mesin Vulkanik"><figcaption></figcaption></figure>

*   Buka pengaturan [Layanan Model](../../cherrystudio/preview/settings/providers.md) Cherry Studio, temukan Mesin Vulkanik
*   Klik "Tambah", lalu tempelkan ID Model ke kolom teks ID Model

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Tambahkan model satu per satu mengikuti alur ini

### Alamat API

Ada dua cara penulisan alamat API:
*   Versi default klien: `https://ark.cn-beijing.volces.com/api/v3/`
*   Alternatif: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Kedua format memiliki fungsi yang sama. Biarkan menggunakan default tanpa modifikasi.

Untuk perbedaan akhiran `/` dan `#`, lihat bagian **Alamat API** di pengaturan penyedia layanan: [Kunjungi Dokumen](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Contoh cURL dalam Dokumen Resmi</p></figcaption></figure>