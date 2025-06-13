---
icon: message
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Antarmuka Percakapan

## Asisten dan Topik

### Asisten

`Asisten` adalah pengaturan personalisasi untuk model yang dipilih, seperti preset petunjuk dan preset parameter, agar model lebih sesuai dengan pekerjaan yang Anda harapkan.

`Asisten default sistem` menyediakan parameter umum (tanpa petunjuk). Anda dapat langsung menggunakannya atau mencari preset yang diperlukan di [halaman Agen](agents.md).

### Topik

`Asisten` adalah induk dari `Topik`. Satu asisten dapat membuat beberapa topik (percakapan). Semua `Topik` berbagi pengaturan model seperti parameter dan prompt dari `Asisten`.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Tombol Dalam Kotak Dialog

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Topik Baru` Buat topik baru di asisten saat ini.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Unggah Gambar/Dokumen` Unggah gambar membutuhkan dukungan model. Dokumen akan otomatis diurai sebagai teks konteks untuk model.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Pencarian Web` Harus mengonfigurasi informasi pencarian di pengaturan. Hasil pencarian akan dikembalikan sebagai konteks ke model besar. Lihat detail di [Mode Terhubung Internet](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Basis Pengetahuan` Aktifkan basis pengetahuan. Lihat [Panduan Basis Pengetahuan](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Server MCP` Aktifkan fungsionalitas server MCP. Lihat [Panduan Penggunaan MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Hasilkan Gambar` Secara default tidak ditampilkan. Untuk model yang mendukung pembuatan gambar (seperti Gemini), perlu diaktifkan secara manual.

{% hint style="info" %}
Karena keterbatasan teknis, Anda harus mengaktifkan tombol secara manual untuk menghasilkan gambar. Tombol ini akan dihapus setelah fungsionalitas dioptimalkan.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Pilih Model` Untuk percakapan selanjutnya, ganti ke model tertentu sambil mempertahankan konteks.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frase Cepat` Harus mengatur frasa umum terlebih dahulu di pengaturan. Dapat dipanggil di sini untuk langsung dimasukkan, mendukung variabel.

![](../../.gitbook/assets/对话界面/清空消息.png) `Hapus Pesan` Hapus semua konten di topik ini.

![](../../.gitbook/assets/对话界面/展开.png) `Perbesar` Perbesar kotak dialog untuk memasukkan teks panjang.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Hapus Konteks` Putuskan konteks yang tersedia untuk model tanpa menghapus konten, artinya model akan "melupakan" percakapan sebelumnya.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Perkiraan Token` Tampilkan perkiraan jumlah Token. Empat data tersebut adalah: `Jumlah konteks saat ini`, `Jumlah maks konteks` (∞ = konteks tak terbatas), `Jumlah karakter pesan saat ini`, `Perkiraan Token`.

{% hint style="info" %}
Fitur ini hanya untuk memperkirakan jumlah Token. Jumlah Token aktual berbeda untuk setiap model. Harap merujuk ke data penyedia model.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Terjemahkan` Terjemahkan konten di kotak masukan saat ini ke bahasa Inggris.

## Pengaturan Percakapan

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Pengaturan Model

Pengaturan model disinkronkan dengan parameter `Pengaturan Model` di pengaturan asisten. Lihat detail di [Edit Asisten](chat.md#edit-asisten).

{% hint style="info" %}
Di pengaturan percakapan, hanya pengaturan model yang berlaku untuk asisten saat ini. Pengaturan lainnya berlaku secara global. Misal: Setelah mengatur gaya pesan menjadi gelembung, gaya tersebut akan diterapkan di semua topik dan asisten.
{% endhint %}

### Pengaturan Pesan

#### <mark style="color:blue;">**`Pemisah Pesan`**</mark>:

Gunakan garis pemisah untuk memisahkan badan pesan dari bilah aksi.

{% tabs %}
{% tab title="Aktif" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Nonaktif" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Gunakan Font Serif`**</mark>：

Berganti gaya font. Sekarang Anda juga bisa mengubah font melalui [CSS khusus](../../personalization-settings/).

#### <mark style="color:blue;">**`Tampilkan Nomor Baris Kode`**</mark>：

Tampilkan nomor baris di blok kode saat model mengeluarkan cuplikan kode.

{% tabs %}
{% tab title="Nonaktif" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Aktif" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blok Kode Dapat Dilipat`**</mark>：

Setelah diaktifkan, bila kode dalam cuplikan terlalu panjang, blok kode akan otomatis dilipat.

#### <mark style="color:blue;">**`Blok Kode Dapat Dipenggal`**</mark>：

Setelah diaktifkan, bila satu baris kode terlalu panjang (melebihi jendela), kode akan otomatis dipenggal.

#### <mark style="color:blue;">**`Proses Pemikiran Otomatis Dilipat`**</mark>：

Setelah diaktifkan, proses pemikiran model yang mendukung fitur pemikiran akan otomatis dilipat setelah selesai.

#### <mark style="color:blue;">**`Gaya Pesan`**</mark>：

Dapat mengganti antarmuka percakapan ke gaya gelembung atau gaya daftar.

#### <mark style="color:blue;">**`Gaya Kode`**</mark>：

Dapat mengganti gaya tampilan cuplikan kode.

#### <mark style="color:blue;">**`Mesin Rumus Matematika`**</mark>：

* KaTeX merender lebih cepat karena dioptimalkan untuk performa;
* MathJax merender lebih lambat tetapi lebih lengkap, mendukung lebih banyak simbol dan perintah matematika.

#### <mark style="color:blue;">**`Ukuran Font Pesan`**</mark>：

Sesuaikan ukuran font di antarmuka percakapan.

### Pengaturan Input

#### <mark style="color:blue;">**`Tampilkan Perkiraan Token`**</mark>：

Tampilkan perkiraan jumlah Token yang dikonsumsi oleh teks masukan (bukan Token konteks aktual, hanya referensi).

#### <mark style="color:blue;">**`Tempel Teks Panjang sebagai File`**</mark>：

Saat menempelkan teks panjang dari sumber lain ke kotak masukan, teks akan otomatis ditampilkan sebagai file untuk mengurangi gangguan pada masukan berikutnya.

#### <mark style="color:blue;">**`Render Pesan Masukan Markdown`**</mark>：

Saat dimatikan, hanya merender pesan balasan model, bukan pesan yang dikirim.

{% tabs %}
{% tab title="Nonaktif" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Aktif" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Terjemahkan dengan Tiga Spasi`**</mark>：

Setelah memasukkan pesan di kotak masukan antarmuka percakapan, ketuk spasi tiga kali untuk menerjemahkan konten menjadi bahasa Inggris.

{% hint style="warning" %}
Perhatian: Operasi ini akan menimpa teks asli.
{% endhint %}

#### <mark style="color:blue;">**`Bahasa Target`**</mark>：

Atur bahasa target untuk tombol terjemahan dan terjemahan tiga kali spasi di kotak masukan.

## Pengaturan Asisten

Di antarmuka asisten, pilih <mark style="background-color:yellow;">nama asisten</mark> yang akan diatur → pilih pengaturan yang sesuai di <mark style="background-color:yellow;">menu klik kanan</mark>

### Edit Asisten

{% hint style="info" %}
Pengaturan asisten berlaku untuk semua topik di bawah asisten ini.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Pengaturan Prompt

#### <mark style="color:blue;">**`Nama`**</mark>：

Nama asisten khusus yang mudah diidentifikasi.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Yaitu petunjuk, dapat mengedit konten dengan merujuk pada cara penulisan prompt di halaman agen.

#### Pengaturan Model

#### <mark style="color:blue;">**`Model Default`**</mark>：

Tetapkan model default untuk asisten ini. Saat menambahkan dari halaman agen atau menyalin asisten, model awal adalah model ini. Jika tidak disetel, model awal adalah model global (yaitu [model asisten default](settings/default-models.md#model-asisten-default)).

{% hint style="info" %}
Ada dua model default asisten: [model percakapan default global](settings/default-models.md#model-asisten-default) dan model default asisten. Model default asisten memiliki prioritas lebih tinggi daripada model percakapan default global. Jika tidak mengatur model default asisten, model default asisten = model percakapan default global.
{% endhint %}

#### <mark style="color:blue;">**`Atur Ulang Model Otomatis`**</mark>：

Aktif - Saat beralih ke model lain selama penggunaan di topik ini, membuat topik baru akan mengatur ulang topik baru ke model default asisten. Saat dinonaktifkan, model topik baru akan mengikuti model yang digunakan topik sebelumnya.

> Misalnya, model default asisten adalah gpt-3.5-turbo, saya membuat topik1 di bawah asisten ini, lalu beralih ke gpt-4o selama percakapan:
>
> Jika pengaturan ulang otomatis aktif: Saat membuat topik2, model default topik2 adalah gpt-3.5-turbo;
>
> Jika pengaturan ulang otomatis nonaktif: Saat membuat topik2, model default topik2 adalah gpt-4o.

#### <mark style="color:blue;">**`Temperatur (Temperature)`**</mark> ：

Parameter temperatur mengontrol keacakan dan kreativitas keluaran model (nilai default 0.7). Manifestasi spesifik:

* Nilai rendah (0-0.3):
  * Keluaran lebih pasti dan terfokus
  * Cocok untuk pembuatan kode, analisis data yang membutuhkan akurasi
  * Cenderung memilih kosakata paling mungkin
* Nilai sedang (0.4-0.7):
  * Seimbangkan kreativitas dan koherensi
  * Cocok untuk percakapan sehari-hari, penulisan umum
  * Direkomendasikan untuk dialog chatbot (sekitar 0.5)
* Nilai tinggi (0.8-1.0):
  * Menghasilkan keluaran lebih kreatif dan beragam
  * Cocok untuk penulisan kreatif, brainstorming
  * Namun dapat mengurangi koherensi teks

#### <mark style="color:blue;">**`Top P (Pemilihan Nuklir)`**</mark>：

Nilai default 1. Semakin kecil nilainya, konten AI lebih monoton dan mudah dipahami; semakin besar nilainya, AI memiliki ruang kosakata lebih luas dan beragam.

Pemilihan nuklir memengaruhi keluaran dengan mengontrol ambang batas probabilitas pemilihan kosakata:

* Nilai kecil (0.1-0.3):
  * Hanya mempertimbangkan kosakata probabilitas tertinggi
  * Keluaran lebih konservatif dan terkendali
  * Cocok untuk komentar kode, dokumen teknis
* Nilai sedang (0.4-0.6):
  * Seimbangkan keragaman dan akurasi kosakata
  * Cocok untuk percakapan umum dan tugas penulisan
* Nilai besar (0.7-1.0):
  * Mempertimbangkan pemilihan kosakata lebih luas
  * Menghasilkan konten lebih kaya dan beragam
  * Cocok untuk penulisan kreatif yang membutuhkan ekspresi beragam

{% hint style="info" %}
- Dua parameter dapat digunakan secara independen atau dikombinasikan
- Pilih nilai parameter yang sesuai berdasarkan jenis tugas
- Disarankan untuk bereksperimen mencari kombinasi terbaik
- Konten di atas hanya sebagai referensi. Rentang parameter mungkin tidak cocok untuk semua model. Silakan merujuk ke saran parameter dokumentasi model.
{% endhint %}

#### <mark style="color:blue;">**`Jumlah Konteks (Context Window)`**</mark>

Jumlah pesan yang disimpan dalam konteks. Semakin besar nilai, semakin panjang konteks, semakin banyak Token yang dikonsumsi:

* 5-10: Cocok untuk percakapan normal
* \>10: Tugas kompleks yang membutuhkan memori lebih panjang (misalnya: Menghasilkan teks panjang langkah demi langkah sesuai draf penulisan, memastikan logika konteks yang dihasilkan koheren)
* Catatan: Semakin banyak pesan, semakin banyak Token yang dikonsumsi

#### <mark style="color:blue;">**`Aktifkan Batas Panjang Pesan (MaxToken)`**</mark>

Jumlah Token maksimum per jawaban. Dalam model bahasa besar, max token (token maks) adalah parameter kunci yang secara langsung memengaruhi kualitas dan panjang jawaban model.

> Misal: Saat menguji konektivitas model dengan mengisi key di CherryStudio, cukup mengetahui apakah model mengembalikan pesan dengan benar tanpa konten spesifik. Atur MaxToken ke 1.

Batas MaxToken sebagian besar model adalah 32k Token, bahkan ada 64k atau lebih. Silakan lihat halaman pengantar tertentu.

Jumlah spesifik tergantung kebutuhan, atau dapat merujuk saran berikut.

{% hint style="success" %}
Saran:

* Percakapan normal: 500-800
* Pembuatan teks pendek: 800-2000
* Pembuatan kode: 2000-3600
* Pembuatan teks panjang: 4000+ (membutuhkan dukungan model itu sendiri)
{% endhint %}

{% hint style="warning" %}
Umumnya jawaban model dibatasi dalam MaxToken. Namun terkadang terpotong (misal saat menulis kode panjang) atau tidak lengkap. Dalam kasus khusus, sesuaikan secara fleksibel berdasarkan situasi aktual.
{% endhint %}

#### <mark style="color:blue;">**`Output Alir (Stream)`**</mark>

Output alir adalah metode pemrosesan data yang memungkinkan transmisi dan pemrosesan data dalam bentuk aliran terus menerus. Cara ini memungkinkan data segera diproses dan dikeluarkan setelah dihasilkan, sangat meningkatkan real-time dan efisiensi.

Dalam lingkungan seperti klien CherryStudio, sederhananya adalah efek mesin ketik.

Setelah dimatikan (non-alir): Model mengeluarkan semua informasi sekaligus setelah selesai dihasilkan (bayangkan menerima pesan WhatsApp);

Saat diaktifkan: Keluarkan karakter demi karakter hingga selesai.

{% hint style="info" %}
Jika model tertentu tidak mendukung aliran, perlu menonaktifkan pengaturan ini, seperti **o1-mini** yang awalnya hanya mendukung non-alir.
{% endhint %}

#### <mark style="color:blue;">**`Parameter Khusus`**</mark>

Tambahkan parameter permintaan ekstra dalam body permintaan, seperti bidang `presence_penalty`. Umumnya tidak diperlukan pengguna biasa.

> Parameter seperti top-p, max_tokens, stream adalah bagian dari parameter ini.

Cara isi: Nama parameter—Tipe parameter (