---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Mode Online

{% hint style="info" %}
Contoh situasi yang membutuhkan koneksi internet:

* Informasi terkini: seperti harga kontrak emas hari ini/minggu ini/baru saja.
* Data real-time: seperti cuaca, nilai tukar mata uang, dan data dinamis lainnya.
* Pengetahuan terkini: seperti hal-hal baru, konsep baru, teknologi baru, dll.
{% endhint %}

### 1. Cara Mengaktifkan Mode Online

Pada jendela input pertanyaan di Cherry Studio, klik ikon 【Globe Kecil】 untuk mengaktifkan mode online.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Klik ikon globe - Aktifkan mode online</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Menunjukkan mode online telah aktif</p></figcaption></figure>

### 2. Perhatian Khusus: Dua Mode Online Berbeda

#### Mode 1: Model AI dari penyedia layanan dengan fitur online bawaan

Dalam mode ini, setelah mengaktifkan fitur online, Anda bisa langsung menggunakannya tanpa konfigurasi tambahan.

{% hint style="warning" %}
Cara cepat memeriksa apakah model mendukung fitur online: lihat apakah nama model diikuti dengan ikon miniatur peta di antarmuka bertanya.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Pada halaman manajemen model, metode ini juga membantu mengidentifikasi model yang mendukung mode online.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Penyedia layanan model dengan dukungan online yang sudah didukung Cherry Studio:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (semua model mendukung online)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian dll</mark>

{% hint style="danger" %}
Pengecualian:
Ada situasi khusus di mana model tidak memiliki ikon globe tetapi tetap dapat terhubung ke internet, seperti dijelaskan dalam tutorial berikut.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Mode 2: Layanan Tavily sebagai perantara pencarian online

Ketika menggunakan model AI tanpa fitur online bawaan (tidak ada ikon globe), tetapi membutuhkan informasi real-time, gunakan layanan pencarian web Tavily.

**Pengguna pertama kali** akan melihat jendela pop-up untuk konfigurasi. Ikuti petunjuknya – sangat sederhana!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Jendela pop-up, klik: Ke Pengaturan</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Klik untuk mendapatkan kunci API</p></figcaption></figure>

Setelah mengklik, Anda akan otomatis diarahkan ke **situs web Tavily** untuk registrasi/login. Setelah login, buat API key dan salin kunci tersebut ke Cherry Studio.

{% hint style="danger" %}
Tidak tahu cara registrasi? Lihat tutorial registrasi Tavily dalam direktori dokumen ini.
{% endhint %}

**Dokumen referensi registrasi Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Tampilan antarmuka berikut menandakan registrasi berhasil.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Salin kunci API</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Tempelkan kunci - selesai</p></figcaption></figure>

Hasil pencarian menunjukkan mode online bekerja normal dengan jumlah hasil default yang disetel: 5.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Catatan: Tavily memiliki kuota gratis bulanan; pemakaian melebihi kuota akan dikenakan biaya~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Jika menemui kesalahan, silakan hubungi kami kapan saja.