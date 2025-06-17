---
icon: seal-question
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Pertanyaan Umum

## Kode Kesalahan Umum

* **4xx (Kode Status Kesalahan Klien)**: Biasanya disebabkan oleh kesalahan sintaks permintaan, otorisasi gagal, atau autentikasi gagal sehingga permintaan tidak dapat diselesaikan.
* **5xx (Kode Status Kesalahan Server)**: Biasanya disebabkan oleh kesalahan server, server down, atau waktu pemrosesan permintaan terlampaui.

| Kode Kesalahan | Kemungkinan Penyebab | Solusi |
|---------------|---------------------|--------|
| <h4>400</h4> | Format badan permintaan salah | <p>Periksa konten kesalahan dalam respons dialog atau lihat <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">konsol</a> untuk melihat detail kesalahan dan ikuti petunjuknya.</p><p><mark style="color:purple;">【Kasus Umum 1】</mark>: Untuk model Gemini, mungkin perlu mengaitkan kartu pembayaran;<br><mark style="color:purple;">【Kasus Umum 2】</mark>: Ukuran data melebihi batas, umum terjadi pada model visual saat ukuran gambar melebihi batas lalu lintas per permintaan;<br><mark style="color:purple;">【Kasus Umum 3】</mark>: Menambahkan parameter yang tidak didukung atau pengisian parameter salah. Coba buat asisten baru untuk pengujian;<br><mark style="color:purple;">【Kasus Umum 4】</mark>: Konteks melebihi batas. Bersihkan konteks, mulai dialog baru, atau kurangi jumlah konteks.</p> |
| <h4>401</h4> | Autentikasi gagal: Model tidak didukung atau akun server diblokir | Hubungi penyedia layanan atau periksa status akun |
| <h4>403</h4> | Tidak memiliki izin untuk operasi permintaan | Ikuti petunjuk kesalahan dalam respons dialog atau konsol |
| <h4>404</h4> | Tidak dapat menemukan sumber daya yang diminta | Periksa jalur permintaan |
| <h4>422</h4> | Format permintaan benar tetapi semantik salah | Kesalahan umum pada JSON (misal: nilai kosong; mengharapkan string tetapi menulis angka/boolean) |
| <h4>429</h4> | Batas kecepatan permintaan tercapai | Kecepatan permintaan (TPM/RPM) mencapai batas, tunggu beberapa saat |
| <h4>500</h4> | Kesalahan internal server, permintaan tidak dapat diselesaikan | Hubungi penyedia layanan jika berlanjut |
| <h4>501</h4> | Server tidak mendukung fungsi yang diminta | |
| <h4>502</h4> | Server gateway/proxy menerima respons tidak valid dari server jarak jauh | |
| <h4>503</h4> | Server sibuk atau dalam pemeliharaan, coba lagi nanti | |
| <h4>504</h4> | Server gateway/proxy tidak menerima respons tepat waktu | |

***

## Cara Memeriksa Kesalahan di Konsol

* Klik pada jendela klien Cherry Studio lalu tekan <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- Jendela aktif harus merupakan jendela klien Cherry Studio;
- Konsol harus dibuka sebelum melakukan pengujian atau memulai dialog.
{% endhint %}

* Di konsol yang muncul, klik <mark style="color:blue;">`Network`</mark> → Cari entri terakhir dengan tanda <mark style="color:red;">`×`</mark> merah: <mark style="color:red;">`completions`</mark> (untuk kesalahan dialog/terjemahan) atau <mark style="color:red;">`generations`</mark> (kesalahan gambar) → Klik <mark style="color:blue;">`Response`</mark> untuk melihat konten respons lengkap.

> Jika tidak dapat mengidentifikasi penyebabnya, tangkap layar dan kirim ke [Grup Diskusi Resmi](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Metode ini berlaku untuk semua skenario: dialog, pengujian model, pembuatan basis pengetahuan, atau pembuatan gambar. Selalu buka konsol sebelum melakukan permintaan.

{% hint style="info" %}
Nama berbeda untuk skenario berbeda:

Dialog/Terjemahan: <mark style="color:red;">`completions`</mark>

Gambar: <mark style="color:red;">`generations`</mark>

Basis Pengetahuan: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Rumus Tidak Ditampilkan/Kesalahan Render Rumus

* Jika rumus menampilkan kode alih-alih hasil render, periksa pembatas:

> **Panduan Pembatas**
>
> _Rumus Sebaris_
>
> * Tanda dolar tunggal: `$formula$`
> * atau `\(` dan `\)` seperti: `\(formula\)`
>
> _Blok Rumus_
>
> * Tanda dolar ganda: `$$formula$$`
> * atau `\[formula\]`
> * Contoh: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Kesalahan render/karakter acak sering terjadi ketika rumus mengandung karakter Tionghoa. Coba ganti mesin rumus ke KateX.

***

## Tidak Dapat Membuat Basis Pengetahuan/Gagal Mendapatkan Dimensi Embedding

1. Status model tidak tersedia

> Pastikan penyedia layanan mendukung model tersebut dan layanan model berjalan normal.

2. Menggunakan model non-embedding

***

## Model Tidak Dikenali Gambar/Tidak Dapat Mengunggah/Memilih Gambar

Pertama pastikan model mendukung pengenalan gambar. Model populer di Cherry Studio memiliki ikon mata kecil di nama model sebagai penanda dukungan.

Model pengenalan gambar mendukung pengunggahan file gambar. Jika fungsi model tidak terpetakan dengan benar, temukan model di daftar penyedia layanan, klik tombol pengaturan di sebelah nama, dan centang opsi gambar.

Model non-visual tidak akan berfungsi meskipun opsi gambar dicentang.