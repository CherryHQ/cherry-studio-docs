---
icon: cloud-check
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Pengaturan Penyedia Layanan

Halaman ini hanya memperkenalkan fungsi antarmuka. Untuk tutorial konfigurasi, lihat tutorial [Konfigurasi Penyedia](../../../pre-basic/providers/) dalam dasar.

{% hint style="info" %}
* Saat menggunakan penyedia bawaan, cukup isi kunci rahasia yang sesuai.
* Istilah untuk kunci rahasia mungkin berbeda antar penyedia: kunci rahasia, Key, API Key, token semuanya merujuk pada hal yang sama.
{% endhint %}

### Kunci API Rahasia

Di Cherry Studio, satu penyedia mendukung penggunaan banyak kunci dengan rotasi, metode rotasinya adalah siklus dari depan ke belakang dalam daftar.

* Tambahkan beberapa kunci dengan dipisahkan koma bahasa Inggris, contoh:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Harus menggunakan koma **Bahasa Inggris**.
{% endhint %}

### Alamat API

Umumnya tidak perlu mengisi alamat API saat menggunakan penyedia bawaan. Jika perlu mengubah, isi sesuai alamat dari dokumen resmi terkait.

> Jika format alamat dari penyedia adalah <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, cukup isi bagian root address (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio akan otomatis menambahkan path sisanya (<mark style="background-color:green;">/v1/chat/completions</mark>). Pengisian yang tidak sesuai dapat menyebabkan kegagalan fungsi.

{% hint style="info" %}
Penjelasan: Umumnya routing model bahasa besar penyedia sudah terstandarisasi. Jika jalur API versi v2/v3/chat/completions, isi versinya diakhiri `/`. Saat routing tidak konvensional (<mark style="background-color:green;">/v1/chat/completions</mark>), gunakan alamat lengkap diakhiri `#`.

Yaitu:
* Akhiri dengan `/` → tambahkan "<mark style="background-color:green;">chat/completions</mark>"
* Akhiri dengan `#` → gunakan alamat apa adanya

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Menambahkan Model

Umumnya klik tombol `Kelola` di pojok kiri bawah halaman akan otomatis mengambil semua model yang didukung. Klik `+` di daftar untuk menambahkannya.

{% hint style="info" %}
Model di popup tidak otomatis ditambahkan semua. Klik `+` di kanan model untuk memunculkannya di daftar pilihan.
{% endhint %}

### Pemeriksaan Konektivitas

Klik tombol cek di samping input Kunci API untuk menguji konfigurasi.

{% hint style="info" %}
Pemeriksaan model menggunakan model percakapan terakhir di daftar. Jika gagal, periksa model yang salah/tidak didukung.
{% endhint %}

{% hint style="danger" %}
**WAJIB** nyalakan tombol aktif di kanan atas setelah konfigurasi berhasil. Jika tidak, penyedia tetap non-aktif dan modelnya tidak tersedia.
{% endhint %}