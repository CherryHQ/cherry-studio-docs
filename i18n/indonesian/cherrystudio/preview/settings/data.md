---
icon: database
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Pengaturan Data

Antarmuka ini memungkinkan pengguna untuk melakukan pencadangan data klien ke cloud maupun lokal, melihat direktori data lokal, membersihkan cache, dan operasi lainnya.

### Pencadangan Data

Saat ini pencadangan data hanya mendukung metode WebDAV. Anda dapat memilih layanan yang mendukung WebDAV untuk pencadangan cloud.

Anda juga bisa menyinkronkan data antar perangkat melalui skema: `Komputer A` $$\xrightarrow{\text{cadangkan}}$$ `WebDAV` $$\xrightarrow{\text{pulihkan}}$$ `Komputer B`.

#### Contoh menggunakan Jianguoyun

1. Masuk ke Jianguoyun, klik nama pengguna di pojok kanan atas, pilih "Informasi Akun":
   <figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Pilih "Opsi Keamanan", klik "Tambah Aplikasi"
   <figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Masukkan nama aplikasi, buat kata sandi acak;
   <figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Salin dan simpan kata sandi;
   <figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Dapatkan alamat server, akun, dan kata sandi;
   <figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Di Cherry Studio Pengaturan - Pengaturan Data, isi informasi WebDAV;
   <figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Pilih pencadangan atau pemulihan data, dan dapat mengatur periode pencadangan otomatis.
   <figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Layanan WebDAV dengan persyaratan yang rendah umumnya disediakan oleh penyimpanan cloud:

* [Jianguoyun](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (perlu keanggotaan)
* [Aliyun Drive](https://www.alipan.com/) (perlu pembelian)
* [Box](https://www.box.com/) (kapasitas gratis 10GB, batas ukuran file 250MB)
* [Dropbox](https://www.dropbox.com/) (gratis 2GB, bisa ditambah 16GB dengan mengundang teman)
* [TeraCloud](https://teracloud.jp/en/) (gratis 10GB, dapat tambahan 5GB melalui undangan)
* [Yandex Disk](https://disk.yandex.com/) (kapasitas gratis 10GB)

Selain itu, ada layanan yang perlu dideploy sendiri:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}