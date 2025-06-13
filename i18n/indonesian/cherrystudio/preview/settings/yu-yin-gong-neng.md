---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Fitur Suara

```
Manual Penggunaan Fitur Suara Cherry Studio

I. Gambaran Umum Fitur Suara

Cherry Studio menyediakan tiga modul fitur suara utama: TTS (Text-to-Speech), ASR (Automatic Speech Recognition), dan Panggilan Suara. Fitur-fitur ini memungkinkan Anda berinteraksi secara alami dengan AI melalui suara, meningkatkan pengalaman penggunaan.

- TTS (Text-to-Speech): Mengonversi respons teks AI menjadi output suara
- ASR (Automatic Speech Recognition): Mengonversi suara Anda menjadi input teks
- Panggilan Suara: Menggabungkan TTS dan ASR untuk pengalaman percakapan suara seperti ChatGPT

II. Fitur TTS (Text-to-Speech)

1. Jenis Layanan yang Didukung

Cherry Studio mendukung empat jenis layanan TTS:

- OpenAI: Menggunakan TTS API OpenAI, memerlukan kunci API
- TTS Browser: Menggunakan fitur sintesis suara bawaan browser, gratis tanpa konfigurasi
- Siliconflow: Menggunakan layanan TTS Siliconflow, memerlukan kunci API
- TTS Online Gratis: Menggunakan layanan TTS online gratis, tidak memerlukan kunci API

2. Metode Pengaturan

1) Masuk ke halaman pengaturan, pilih tab "Fitur Suara"
2) Pada sub-tab "TTS":
   - Aktifkan fitur TTS (nyalakan saklar)
   - Pilih jenis layanan TTS
   - Sesuai jenis layanan yang dipilih, konfigurasi parameter berikut:
     - OpenAI: Isi kunci API, alamat API, pilih suara dan model
     - TTS Browser: Pilih suara
     - Siliconflow: Isi kunci API, alamat API, pilih suara, model, format respons dan kecepatan bicara
     - TTS Online Gratis: Pilih suara dan format output
3) Konfigurasi opsi penyaringan TTS (opsional):
   - Saring proses berpikir
   - Saring markup Markdown
   - Saring blok kode
4) Atur apakah akan menampilkan bilah kemajuan TTS
5) Klik tombol "Uji TTS" untuk memverifikasi konfigurasi

3. Metode Penggunaan

- Setelah mengaktifkan fitur TTS, respons AI akan secara otomatis diubah menjadi output suara
- Di antarmuka obrolan, tombol putar TTS akan muncul di bawah setiap respons AI
- Klik tombol putar untuk memutar/menjeda suara
- Jika bilah kemajuan TTS diaktifkan, akan muncul di bawah teks
- Teks panjang akan disintesis secara otomatis per segmen dan diputar terus menerus

III. Fitur ASR (Automatic Speech Recognition)

1. Jenis Layanan yang Didukung

Cherry Studio mendukung tiga jenis layanan ASR:

- OpenAI: Menggunakan model Whisper OpenAI, memerlukan kunci API
- Browser: Menggunakan fitur pengenalan suara bawaan browser, gratis tanpa konfigurasi
- Server Lokal: Terhubung ke server WebSocket lokal untuk pengenalan suara

2. Metode Pengaturan

1) Masuk ke halaman pengaturan, pilih tab "Fitur Suara"
2) Pada sub-tab "ASR":
   - Aktifkan fitur ASR (nyalakan saklar)
   - Pilih jenis layanan ASR
   - Sesuai jenis layanan yang dipilih, konfigurasi parameter berikut:
     - OpenAI: Isi kunci API, alamat API, pilih model
     - Browser: Tidak memerlukan konfigurasi tambahan
     - Server Lokal: Dapat mengatur apakah server ASR akan dimulai secara otomatis saat aplikasi diluncurkan
   - Pilih bahasa pengenalan suara (default: Bahasa Tionghoa)
3) Klik tombol "Uji ASR" untuk memverifikasi konfigurasi

3. Metode Penggunaan

- Setelah mengaktifkan ASR, tombol pengenalan suara akan muncul di sebelah kolom input
- Klik tombol pengenalan suara untuk memulai rekaman
- Setelah berbicara, suara akan dikonversi menjadi teks dan dimasukkan ke kolom input
- Klik tombol lagi untuk mengakhiri rekaman
- Pengenalan suara mendukung pengenalan multi-percakapan secara berkelanjutan dalam mode akumulasi

IV. Fitur Panggilan Suara

1. Karakteristik Fitur

- Menggabungkan TTS dan ASR untuk pengalaman percakapan suara seperti ChatGPT
- Menggunakan antarmuka jendela mengambang yang dapat diseret
- Mendukung mode tekan-tahan untuk berbicara
- Mendukung pintasan keyboard kustom
- Mendukung perampingan jendela
- Dapat memilih model panggilan suara khusus
- Mendukung petunjuk kustom

2. Metode Pengaturan

1) Masuk ke halaman pengaturan, pilih tab "Fitur Suara"
2) Pada sub-tab "Fitur Panggilan":
   - Aktifkan fitur panggilan suara (nyalakan saklar)
   - Klik tombol "Pilih Model" untuk memilih model AI untuk panggilan suara
   - Kustomisasi petunjuk panggilan suara di kotak teks (opsional)
   - Klik "Simpan" untuk menyimpan petunjuk, atau "Reset" untuk mengembalikan petunjuk default

3. Metode Penggunaan

1) Di antarmuka obrolan, klik tombol panggilan suara di sebelah kanan kolom input (ikon telepon)
2) Jendela panggilan suara akan terbuka dan memutar sapaan suara
3) Tekan dan tahan tombol "Tekan untuk Berbicara" untuk memulai rekaman (atau gunakan pintasan keyboard)
4) Lepaskan tombol untuk mengakhiri rekaman dan mengirim ke AI
5) AI menghasilkan respons dan memutarnya melalui TTS
6) Gunakan tombol kontrol di jendela:
   - Tombol bisu/non-bisu: Mengontrol output TTS
   - Tombol jeda/lanjut: Menjeda atau melanjutkan percakapan
   - Tombol pengaturan: Mengonfigurasi pintasan
   - Tombol perampingan: Merampingkan jendela, hanya menyisakan baris tekan untuk berbicara
7) Klik tombol tutup untuk mengakhiri panggilan

4. Pengaturan Pintasan

1) Di jendela panggilan suara, klik tombol pengaturan
2) Di panel pengaturan, klik tombol pintasan
3) Tekan tombol yang ingin Anda tetapkan (misalnya spasi, Shift, dll.)
4) Klik "Simpan" untuk menyimpan pengaturan
5) Gunakan: Tekan tombol pintasan untuk memulai rekaman, lepaskan untuk mengakhiri dan mengirim

V. Masalah dan Solusi Umum

1. Masalah Terkait TTS

- Masalah: TTS tidak mengeluarkan suara
   Solusi: Periksa apakah fitur TTS diaktifkan, pastikan jenis layanan yang benar dipilih dan parameter yang diperlukan dikonfigurasi

- Masalah: Kualitas suara TTS buruk
   Solusi: Coba ganti jenis layanan TTS atau suara yang berbeda

- Masalah: Pesan kesalahan muncul saat pemutaran TTS
   Solusi: Periksa apakah kunci API benar dan koneksi jaringan normal

2. Masalah Terkait ASR

- Masalah: ASR tidak mengenali suara
   Solusi: Periksa apakah fitur ASR diaktifkan, pastikan jenis layanan yang benar dipilih dan parameter yang diperlukan dikonfigurasi

- Masalah: Akurasi pengenalan ASR rendah
   Solusi: Coba ganti jenis layanan ASR, atau sesuaikan posisi mikrofon dan volume

- Masalah: Koneksi ke server ASR gagal
   Solusi: Periksa apakah server lokal berjalan normal, atau coba mulai ulang aplikasi

3. Masalah Terkait Panggilan Suara

- Masalah: Jendela panggilan suara tidak dapat dibuka
   Solusi: Periksa apakah fitur panggilan suara diaktifkan, pastikan TTS dan ASR dikonfigurasi dengan benar

- Masalah: Tombol tekan-tahan tidak merespons
   Solusi: Periksa apakah izin mikrofon diberikan, atau coba mulai ulang panggilan suara

- Masalah: Respons AI tanpa output suara
   Solusi: Periksa apakah fitur TTS diaktifkan, pastikan tidak dalam mode bisu

VI. Pengaturan Lanjutan dan Opsi Kustom

1. Pengaturan Lanjutan TTS

- Opsi Penyaringan: Dapat memilih untuk menyaring proses berpikir, markup Markdown, dan blok kode agar pemutaran TTS lebih lancar
- Tampilan Bilah Kemajuan: Dapat memilih apakah akan menampilkan bilah kemajuan TTS
- Suara dan Model Kustom: Dapat menambahkan opsi suara dan model kustom

2. Pengaturan Lanjutan ASR

- Mulai Otomatis Server: Dapat mengatur apakah server ASR dimulai secara otomatis saat aplikasi diluncurkan
- Pemilihan Bahasa: Dapat memilih bahasa pengenalan suara yang berbeda

3. Pengaturan Lanjutan Panggilan Suara

- Petunjuk Kustom: Dapat menyesuaikan petunjuk panggilan suara untuk memandu AI dalam mode panggilan suara
- Pemilihan Model Khusus: Dapat memilih model AI khusus untuk panggilan suara, terpisah dari model yang digunakan dalam percakapan saat ini
- Kustomisasi Pintasan: Dapat mengatur pintasan kustom untuk mengontrol rekaman

VII. Saran Penggunaan

1. Pilih Layanan TTS yang Tepat:
   - Untuk kualitas suara tinggi, rekomendasikan OpenAI atau Siliconflow
   - Jika tidak ingin mengonfigurasi API, gunakan TTS Browser atau TTS Online Gratis

2. Pilih Layanan ASR yang Tepat:
   - Untuk akurasi tinggi, rekomendasikan OpenAI
   - Jika tidak ingin mengonfigurasi API, gunakan pengenalan suara bawaan browser

3. Optimalkan Pengalaman Panggilan Suara:
   - Menggunakan headphone dapat mencegah output TTS ditangkap kembali oleh ASR
   - Penggunaan di lingkungan tenang meningkatkan akurasi pengenalan
   - Petunjuk kustom dapat membuat respons AI lebih cocok untuk pemutaran suara

4. Sesuaikan Pengaturan Sesuai Kebutuhan:
   - Jika terutama berkomunikasi melalui teks, cukup aktifkan fitur TTS
   - Jika terutama menggunakan input suara, cukup aktifkan fitur ASR
   - Jika memerlukan pengalaman percakapan suara lengkap, aktifkan fitur panggilan suara

Semoga manual ini membantu Anda memanfaatkan fitur suara Cherry Studio secara penuh, menikmati pengalaman interaksi AI yang lebih alami dan mudah!
```