
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# GitHub Copilot

Untuk menggunakan GitHub Copilot, Anda harus memiliki akun GitHub terlebih dahulu dan berlangganan layanan GitHub Copilot. Langganan versi gratis juga bisa digunakan, tetapi versi gratis tidak mendukung model Claude 3.7 terbaru. Untuk detail lengkapnya, silakan lihat [Situs Resmi GitHub Copilot](https://github.com/features/copilot).

## Mendapatkan Device Code

Klik "Login GitHub" untuk mendapatkan Device Code dan salin.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Contoh gambar pengambilan Device Code"><figcaption><p>Mendapatkan Device Code</p></figcaption></figure>

## Mengisi Device Code di Browser dan Memberikan Otorisasi

Setelah berhasil mendapatkan Device Code, klik tautan untuk membuka browser. Masuk ke akun GitHub di browser, masukkan Device Code, dan berikan otorisasi.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Contoh gambar Otorisasi GitHub"><figcaption><p>Otorisasi GitHub</p></figcaption></figure>

Setelah otorisasi berhasil, kembali ke Cherry Studio. Klik "Hubungkan GitHub", dan setelah berhasil, nama pengguna dan foto profil GitHub akan ditampilkan.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Contoh gambar koneksi GitHub berhasil"><figcaption><p>Koneksi GitHub Berhasil</p></figcaption></figure>

## Klik "Kelola" untuk Mendapatkan Daftar Model

Klik tombol "Kelola" di bagian bawah. Sistem akan otomatis terhubung ke internet untuk mendapatkan daftar model yang saat ini didukung.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Contoh gambar tombol kelola yang mendapatkan daftar model"><figcaption><p>Mendapatkan Daftar Model</p></figcaption></figure>

## Pertanyaan Umum

### Gagal Mendapatkan Device Code, Silakan Coba Lagi

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Contoh gambar gagal mendapatkan Device Code"><figcaption><p>Gagal Mendapatkan Device Code</p></figcaption></figure>

Saat ini permintaan dibuat menggunakan Axios. Axios tidak mendukung proxy socks. Silakan gunakan proxy sistem atau proxy HTTP, atau jangan atur proxy di CherryStudio dan gunakan proxy global. Pertama-tama pastikan koneksi jaringan Anda normal untuk menghindari kegagalan dalam mendapatkan Device Code.