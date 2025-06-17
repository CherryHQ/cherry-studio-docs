---
icon: book-bookmark
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Pengetahuan Dasar

## Apa itu tokens?

Tokens adalah satuan dasar yang digunakan model AI untuk memproses teks, dapat dipahami sebagai unit terkecil "berpikir" model. Ini tidak sepenuhnya setara dengan karakter atau kata seperti yang kita pahami, melainkan cara khusus model memisahkan teks.

#### 1. Segmentasi Bahasa Mandarin
* Satu karakter Hanzi biasanya dikodekan menjadi 1-2 token
* Contoh: `"你好"` ≈ 2-4 tokens

#### 2. Segmentasi Bahasa Inggris
* Kata umum biasanya 1 token
* Kata panjang atau tidak umum dipecah menjadi beberapa token
* Contoh:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Karakter Khusus
* Spasi, tanda baca, dll. juga menggunakan token
* Karakter baris baru biasanya 1 token

{% hint style="info" %}
Tokenizer setiap penyedia layanan berbeda, bahkan model yang berbeda dari penyedia sama pun punya Tokenizer berbeda. Pengetahuan ini hanya untuk memahami konsep token.
{% endhint %}

***

## Apa itu Tokenizer?

Tokenizer (perangkat segmentasi) adalah alat model AI untuk mengubah teks menjadi token. Ini menentukan cara memecah teks input menjadi unit terkecil yang dapat dipahami model.

### Mengapa Tokenizer berbeda antar model?

#### 1. Data pelatihan berbeda
* Korpus berbeda menyebabkan arah optimasi berbeda
* Tingkat dukungan multibahasa berbeda
* Optimasi khusus bidang tertentu (medis, hukum, dll.)

#### 2. Algoritma segmentasi berbeda
* BPE (Byte Pair Encoding) - OpenAI GPT series
* WordPiece - Google BERT
* SentencePiece - cocok untuk skenario multibahasa

#### 3. Tujuan optimasi berbeda
* Fokus efisiensi kompresi
* Fokus preservasi semantik
* Fokus kecepatan pemrosesan

### Dampak praktis
Teks sama bisa menghasilkan jumlah token berbeda di model berbeda:

```
Input: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## Apa itu Model Embedding (Embedding Model)?

**Konsep dasar:** Model embedding adalah teknik untuk mengubah data diskrit dimensi tinggi (teks, gambar, dll.) menjadi vektor kontinu dimensi rendah, memungkinkan mesin memahami dan memproses data kompleks lebih baik. Bayangkan seperti menyederhanakan puzzle kompleks menjadi titik koordinat sederhana yang tetap mempertahankan fitur kunci puzzle. Dalam ekosistem model besar, ia berperan sebagai "penerjemah" yang mengubah informasi yang dapat dipahami manusia menjadi bentuk numerik yang dapat dihitung AI.

**Cara kerja:** Dalam pemrosesan bahasa alami, model embedding memetakan kata ke posisi spesifik dalam ruang vektor. Dalam ruang ini, kata dengan makna serupa otomatis berkelompok. Contoh:
* Vektor "raja" dan "ratu" akan sangat dekat
* Kata hewan peliharaan seperti "kucing" dan "anjing" juga berjarak dekat
* Sedangkan kata tidak terkait seperti "mobil" dan "roti" akan berjarak jauh

**Aplikasi utama:**
* Analisis teks: klasifikasi dokumen, analisis sentimen
* Sistem rekomendasi: rekomendasi konten personalisasi
* Pemrosesan gambar: pencarian gambar serupa
* Mesin pencari: optimasi pencarian semantik

**Keunggulan inti:**
1. Reduksi dimensi: menyederhanakan data kompleks menjadi bentuk vektor yang mudah diproses
2. Preservasi semantik: mempertahankan informasi semantik kunci dari data asli
3. Efisiensi komputasi: meningkatkan efisiensi pelatihan dan inferensi model secara signifikan

**Nilai teknis:** Model embedding adalah komponen dasar sistem AI modern, menyediakan representasi data berkualitas tinggi untuk tugas pembelajaran mesin, dan merupakan teknologi kunci dalam mendorong perkembangan bidang seperti pemrosesan bahasa alami dan visi komputer.

***

## Prinsip Kerja Model Embedding dalam Pencarian Pengetahuan

**Alur kerja dasar:**

1. **Tahap pra-pemrosesan basis pengetahuan**
* Membagi dokumen menjadi chunk (potongan teks) berukuran sesuai
* Menggunakan model embedding untuk mengubah setiap chunk menjadi vektor
* Menyimpan vektor dan teks asli ke database vektor

2. **Tahap pemrosesan kueri**
* Mengubah pertanyaan pengguna menjadi vektor
* Mencari konten serupa dalam database vektor
* Menyediakan konten terkait yang ditemukan sebagai konteks untuk LLM

***

## **Apa itu MCP (Model Context Protocol)?**

MCP adalah protokol sumber terbuka yang bertujuan menyediakan informasi konteks untuk model bahasa besar (LLM) secara terstandarisasi.

* **Analogi:** Bayangkan MCP sebagai "flashdisk" dunia AI. Seperti flashdrive yang menyimpan berbagai file dan bisa langsung digunakan saat dihubungkan ke komputer, server MCP dapat "memasang" berbagai "plugin" yang menyediakan konteks. LLM dapat meminta plugin ini dari server MCP sesuai kebutuhan untuk memperkaya informasi konteks dan meningkatkan kemampuannya.
* **Perbandingan dengan Function Tool:** Function Tool (alat fungsi) tradisional juga dapat menyediakan fungsi eksternal untuk LLM, tetapi MCP merupakan abstraksi yang lebih tinggi. Function Tool lebih fokus pada alat untuk tugas spesifik, sementara MCP menyediakan mekanisme pengambilan konteks yang lebih universal dan modular.

### **Keunggulan Inti MCP**

1. **Standarisasi:** Menyediakan antarmuka dan format data seragam sehingga LLM dan penyedia konteks berbeda dapat berkolaborasi tanpa hambatan.
2. **Modularitas:** Memungkinkan pengembang mengurai informasi konteks menjadi modul (plugin) independen yang mudah dikelola dan digunakan kembali.
3. **Fleksibilitas:** LLM dapat secara dinamis memilih plugin konteks yang dibutuhkan untuk interaksi yang lebih cerdas dan personal.
4. **Skalabilitas:** Desain MCP mendukung penambahan lebih banyak jenis plugin konteks di masa depan, membuka kemungkinan tak terbatas untuk ekspansi kemampuan LLM.

***