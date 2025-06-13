---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Tutorial Konfigurasi Obsidian

Cherry Studio mendukung integrasi dengan Obsidian untuk mengekspor percakapan lengkap atau pesan tunggal ke dalam perpustakaan Obsidian.

{% hint style="warning" %}
Proses ini **tidak memerlukan** instalasi plugin Obsidian tambahan. Namun karena mekanisme impor Cherry Studio ke Obsidian mirip dengan Obsidian Web Clipper, disarankan untuk mengupgrade Obsidian ke versi terbaru (minimal versi **1.7.2**) untuk menghindari [kegagalan impor jika percakapan terlalu panjang](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Tutorial Terbaru

{% hint style="info" %}
Dibandingkan versi lama, fitur ekspor ke Obsidian versi baru dapat **memilih jalur perpustakaan otomatis**, tidak perlu lagi memasukkan nama perpustakaan atau folder secara manual.
{% endhint %}

### Langkah 1: Konfigurasi Cherry Studio

Buka _Pengaturan_ → _Pengaturan Data_ → Menu _Konfigurasi Obsidian_ di Cherry Studio. Nama perpustakaan Obsidian yang pernah dibuka di perangkat ini akan muncul otomatis di menu dropdown. Pilih perpustakaan Obsidian target Anda:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Langkah 2: Ekspor Percakapan

#### Ekspor Percakapan Lengkap

Kembali ke antarmuka percakapan Cherry Studio, klik kanan pada percakapan, pilih _Ekspor_, lalu klik _Ekspor ke Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Sebuah jendela akan muncul untuk mengonfigurasi **Properti (Properties)**, **lokasi folder** di Obsidian, dan **metode pemrosesan** untuk catatan percakapan yang diekspor:

* **Perpustakaan**: Gunakan menu dropdown untuk memilih perpustakaan Obsidian lain
* **Jalur**: Gunakan menu dropdown untuk memilih folder penyimpanan catatan
* Properti sebagai catatan Obsidian:
  * Tag
  * Waktu dibuat (created)
  * Sumber (source)
* **Metode pemrosesan** ekspor ke Obsidian:
  * **Buat Baru (timpa jika ada)**: Buat catatan baru di folder yang ditentukan, timpa catatan lama jika namanya sama
  * **Tambahkan di Awal**: Tambahkan konten percakapan di awal catatan yang sudah ada
  * **Tambahkan di Akhir**: Tambahkan konten percakapan di akhir catatan yang sudah ada

{% hint style="info" %}
Hanya metode pertama yang menyertakan Properties, dua metode lainnya tidak menyertakan Properties.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Konfigurasi properti catatan</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Pemilihan jalur</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Pemilihan metode pemrosesan</p></figcaption></figure>

Setelah memilih semua opsi, klik OK untuk mengekspor percakapan lengkap ke folder yang sesuai di perpustakaan Obsidian.

#### Ekspor Pesan Tunggal

Untuk mengekspor pesan tunggal, klik menu _tiga garis_ di bawah pesan, pilih _Ekspor_, lalu klik _Ekspor ke Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Ekspor pesan tunggal</p></figcaption></figure>

Jendela konfigurasi yang sama dengan ekspor percakapan lengkap akan muncul. Ikuti [tutorial di atas](obsidian.md#langkah-2-ekspor-percakapan) untuk menyelesaikan proses.

### Ekspor Berhasil

🎉 Selamat! Anda telah menyelesaikan semua konfigurasi integrasi Cherry Studio dengan Obsidian dan menuntaskan seluruh alur ekspor. Nikmati penggunaannya!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Ekspor ke Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Lihat hasil ekspor</p></figcaption></figure>

***

## Tutorial Lama (untuk Cherry Studio < v1.1.13)

### Langkah 1: Persiapan Obsidian

Buka perpustakaan Obsidian, buat `folder` untuk menyimpan percakapan yang diekspor (contoh: folder Cherry Studio):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Catat nama `Perpustakaan` yang dilingkari di pojok kiri bawah.

### Langkah 2: Konfigurasi Cherry Studio

Di menu _Pengaturan_ → _Pengaturan Data_ → _Konfigurasi Obsidian_ Cherry Studio, masukkan nama `Perpustakaan` dan `folder` yang didapat di [Langkah 1](obsidian.md#langkah-1-persiapan-obsidian):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

Kolom `Tag Global` bersifat opsional, dapat diisi untuk menetapkan tag default semua percakapan di Obsidian.

### Langkah 3: Ekspor Percakapan

#### Ekspor Percakapan Lengkap

Kembali ke antarmuka percakapan Cherry Studio, klik kanan pada percakapan, pilih _Ekspor_, lalu klik _Ekspor ke Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Ekspor percakapan lengkap</p></figcaption></figure>

Jendela akan muncul untuk mengonfigurasi **Properti (Properties)** dan **metode pemrosesan** catatan. Pilih salah satu metode:

* **Buat Baru (timpa jika ada)**: Buat catatan baru di folder yang ditentukan
* **Tambahkan di Awal**: Tambahkan konten di awal catatan yang ada
* **Tambahkan di Akhir**: Tambahkan konten di akhir catatan yang ada

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Konfigurasi properti catatan</p></figcaption></figure>

{% hint style="info" %}
Hanya metode pertama yang menyertakan Properties, dua metode lainnya tidak menyertakan Properties.
{% endhint %}

#### Ekspor Pesan Tunggal

Untuk ekspor pesan tunggal, klik menu _tiga garis_ di bawah pesan, pilih _Ekspor_, lalu klik _Ekspor ke Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Ekspor pesan tunggal</p></figcaption></figure>

Konfigurasikan properti dan metode pemrosesan dengan mengikuti [tutorial di atas](obsidian.md#langkah-3-ekspor-percakapan).

### Ekspor Berhasil

🎉 Selamat! Anda telah menyelesaikan semua konfigurasi integrasi Cherry Studio dengan Obsidian dan menuntaskan seluruh alur ekspor. Nikmati penggunaannya!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Ekspor ke Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Lihat hasil ekspor</p></figcaption></figure>