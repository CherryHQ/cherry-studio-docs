---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Menghubungkan Volcano Engine ke Internet

### 1. Login/Daftar Akun "Volcano Engine" <a href="#rclz7" id="rclz7"></a>

Kunjungi situs resmi: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Situs Resmi Volcano Engine</p></figcaption></figure>

### 2. Buat "Aplikasi Saya" yang "Dapat Terhubung ke Internet" <a href="#gvzaa" id="gvzaa"></a>

2.1. Login ke Volcano Engine, masuk ke halaman "Volcano Ark": [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Klik berurutan:** <mark style="color:red;">**「Aplikasi Saya」 - 「Buat Aplikasi」 - 「Tanpa Kode」 - 「Obrolan Tunggal」**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Isi Informasi dan Publikasikan Aplikasi <a href="#zzdfe" id="zzdfe"></a>

**Nama Aplikasi**: Beri nama sesuai keinginan (bagian dengan<mark style="color:red;">**\* wajib diisi**</mark>, lainnya bisa dikosongkan)

<mark style="color:red;">**Kuncinya: Aktifkan plugin internet (perlu diaktifkan terlebih dahulu)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Aktifkan Fungsi Plugin Internet (perhatikan biaya dan kuota gratis) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Klik "Beli Sekarang", ikuti langkah sampai muncul tampilan berikut, berarti berhasil diaktifkan.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Perhatikan status, berarti sudah aktif</p></figcaption></figure>

Kembali ke halaman "Isi Informasi Aplikasi", lanjutkan proses.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Penjelasan "Konfigurasi Lanjutan" Pencarian Internet <a href="#sp6uz" id="sp6uz"></a>

Pilih sesuai kebutuhan, rekomendasi pribadi:

* Jika ingin kontrol input/output lebih tepat, gunakan "**Pemanggilan Kustom**"
* Jika tidak ingin repot, biarkan "**Pemanggilan Otomatis**" (nilai default)
* Jika tidak masalah dengan biaya dan butuh info real-time, pilih "**Paksa Aktif**"

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publikasikan Aplikasi <a href="#fe1gf" id="fe1gf"></a>

Klik tombol "Publikasikan" di kanan atas, aplikasi berhasil dibuat.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Dapatkan API Key <a href="#jtqlu" id="jtqlu"></a>

Klik berurutan: **「Panduan Pemanggilan API」-「Pilih API Key dan Salin」-「Lihat dan Pilih」**

Salin API key terlebih dahulu, lalu tempelkan di cherry studio (lihat tampilan berikut):

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Catatan: Jika tidak ada API key, klik "**Buat API Key**" di pojok kanan atas pop-up, lalu salin API key-nya.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Gunakan API Key di Cherry Studio untuk Akses Internet Deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Buka cherry studio - 「Pengaturan」- 「Beri nama」-「Tipe: openAI」 <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Konfigurasi URL dan Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Catatan: Jika tidak menemukan alamat atau bukan node Beijing, temukan alamat spesifik di bagian ini, jangan lupa "/":</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Tambahkan Nama Model <a href="#qmh3i" id="qmh3i"></a>

Salin teks kecil di bawah sebagai nama model, jika tidak akan error.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Pratinjau Hasil <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>