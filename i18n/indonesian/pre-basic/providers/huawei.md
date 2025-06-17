
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Huawei Cloud

Satu, Buat akun dan login di [Huawei Cloud](https://auth.huaweicloud.com/authui/login)

Dua, Klik [tautan ini](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) untuk masuk ke konsol MaaS

Tiga, Otorisasi

<details>

<summary>Langkah Otorisasi (Lewati jika sudah diotorisasi)</summary>

1. Setelah masuk ke halaman tautan (dua), ikuti petunjuk untuk masuk ke halaman otorisasi (klik Subpengguna IAM → Delegasi Baru → Pengguna Biasa)

![](<../../.gitbook/assets/image (49).png>)

2. Setelah klik buat, kembali ke halaman tautan (dua)
3. Akan muncul peringatan akses tidak cukup, klik "klik di sini" pada peringatan tersebut
4. Tambahkan otorisasi yang sudah ada dan konfirmasi

![](<../../.gitbook/assets/image (50).png>)

&#x20;Catatan: Metode ini cocok untuk pemula, tidak perlu membaca banyak konten, cukup ikuti petunjuk klik. Jika Anda bisa mengotorisasi langsung dengan cara Anda sendiri, silakan lanjutkan.

</details>

Empat, Klik manajemen otorisasi di sidebar, buat API Key (kunci rahasia) dan salin

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Kemudian buat penyedia baru di CherryStudio

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Setelah dibuat, masukkan kunci rahasia

Lima, Klik deploy model di sidebar, klaim semua

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

Enam, Klik panggil

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Salin alamat di lokasi ①, tempel ke alamat penyedia di CherryStudio dan tambahkan "#" di akhir

dan tambahkan "#" di akhir

dan tambahkan "#" di akhir

dan tambahkan "#" di akhir

dan tambahkan "#" di akhir

Mengapa menambahkan "#"? [Lihat di sini](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Tentu saja Anda juga bisa tidak melihatnya, cukup ikuti tutorial saja;
>
> Anda juga bisa menggunakan metode menghapus v1/chat/completions untuk mengisi, jika Anda tahu caranya silakan isi sesuai cara Anda sendiri. Jika tidak tahu, wajib ikuti tutorial.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Kemudian salin nama model di lokasi ②, di CherryStudio klik tombol "+Tambah" untuk membuat model baru

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Masukkan nama model, jangan menambah-nambahi, jangan gunakan tanda kutip, salin persis seperti contoh.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Klik tombol tambah model untuk menyelesaikan.

{% hint style="info" %}
Di Huawei Cloud, karena setiap model memiliki alamat yang berbeda, setiap model perlu membuat penyedia baru dengan mengulangi langkah-langkah di atas.
{% endhint %}