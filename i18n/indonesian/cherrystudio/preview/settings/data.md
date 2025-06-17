---
icon: database
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Pengaturan Data

Antarmuka ini memungkinkan operasi seperti backup data klien secara cloud dan lokal, pencarian direktori data lokal, serta penghapusan cache.

### Backup Data

Saat ini, backup data hanya mendukung metode WebDAV. Anda dapat memilih layanan yang mendukung WebDAV untuk melakukan backup cloud.

Anda juga dapat menyinkronkan data antar perangkat dengan metode `Komputer A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{pulihkan}}$$ `Komputer B`.

#### Menggunakan Jianguoyun sebagai Contoh

1. Login ke Jianguoyun, klik nama pengguna di pojok kanan atas, pilih "Informasi Akun":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Pilih "Opsi Keamanan", klik "Tambahkan Aplikasi"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Masukkan nama aplikasi, hasilkan kata sandi acak;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Salin dan simpan kata sandi;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Dapatkan alamat server, akun, dan kata sandi;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Di Pengaturan Cherry Studio - Pengaturan Data, isi informasi WebDAV;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Pilih backup atau pemulihan data, dan dapat mengatur periode backup otomatis.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Layanan WebDAV dengan persyaratan rendah biasanya adalah penyimpanan cloud:

* [Jianguoyun](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (memerlukan keanggotaan)
* [Aliyun Drive](https://www.alipan.com/) (perlu pembelian)
* [Box](https://www.box.com/) (ruang gratis 10GB, batas file tunggal 250MB)
* [Dropbox](https://www.dropbox.com/) (gratis 2GB, dapat diperluas hingga 16GB dengan mengundang teman)
* [TeraCloud](https://teracloud.jp/en/) (gratis 10GB, tambahan 5GB melalui undangan)
* [Yandex Disk](https://disk.yandex.com/) (menyediakan 10GB untuk pengguna gratis)

Selanjutnya adalah layanan yang memerlukan penerapan mandiri:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}