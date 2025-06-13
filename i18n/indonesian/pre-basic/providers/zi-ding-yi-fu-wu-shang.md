
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Penyedia Kustom

Cherry Studio tidak hanya mengintegrasikan layanan model AI utama, tetapi juga memberikan Anda kemampuan penyesuaian yang kuat. Melalui fitur **Penyedia Layanan AI Kustom**, Anda dapat dengan mudah menghubungkan model AI apa pun yang Anda butuhkan.

## Mengapa Memerlukan Penyedia Layanan AI Kustom?

* **Fleksibilitas:** Tidak lagi terbatas pada daftar penyedia layanan bawaan, bebas memilih model AI yang paling sesuai dengan kebutuhan Anda.
* **Keberagaman:** Cobalah berbagai model AI dari platform berbeda untuk menemukan keunggulan uniknya.
* **Kendali:** Kelola langsung kunci API dan alamat akses Anda, jamin keamanan dan privasi.
* **Kustomisasi:** Hubungkan model yang dikerahkan secara privat untuk memenuhi kebutuhan skenario bisnis tertentu.

## Bagaimana Menambahkan Penyedia Layanan AI Kustom?

Hanya dalam beberapa langkah sederhana, Anda dapat menambahkan penyedia AI kustom di Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Buka Pengaturan:** Di bilah navigasi kiri antarmuka Cherry Studio, klik "Pengaturan" (ikon roda gigi).
2. **Masuk ke Layanan Model:** Di halaman pengaturan, pilih tab "Layanan Model".
3. **Tambahkan Penyedia:** Di halaman "Layanan Model", Anda akan melihat daftar penyedia yang ada. Klik tombol "+ Tambah" di bawah daftar untuk membuka popup "Tambahkan Penyedia".
4. **Isi Informasi:** Di popup, Anda perlu mengisi informasi berikut:
   * **Nama Penyedia:** Beri nama yang mudah dikenali untuk penyedia kustom Anda (contoh: MyCustomOpenAI).
   * **Tipe Penyedia:** Pilih tipe penyedia Anda dari daftar dropdown. Saat ini didukung:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Simpan Konfigurasi:** Setelah mengisi, klik tombol "Tambahkan" untuk menyimpan konfigurasi Anda.

## Mengonfigurasi Penyedia Layanan AI Kustom

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Setelah menambahkan, Anda perlu menemukan penyedia yang baru ditambahkan di daftar dan melakukan konfigurasi rinci:

1. **Status Aktif:** Di ujung kanan daftar penyedia kustom, ada sakelar aktif. Aktifkan untuk mengaktifkan layanan kustom ini.
2. **Kunci API:**
   * Isi kunci API (API Key) yang diberikan oleh penyedia AI Anda.
   * Klik tombol "Periksa" di sebelah kanan untuk memverifikasi validitas kunci.
3. **Alamat API:**
   * Isi alamat akses API (Base URL) untuk layanan AI.
   * Pastikan merujuk dokumentasi resmi penyedia AI Anda untuk mendapatkan alamat API yang benar.
4.  **Manajemen Model:**

    * Klik tombol "+ Tambah" untuk menambahkan ID model yang ingin Anda gunakan di penyedia ini. Contoh `gpt-3.5-turbo`, `gemini-pro`, dll.

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * Jika tidak yakin dengan nama model spesifik, silakan rujuk dokumentasi resmi penyedia AI Anda.
    * Klik tombol "Kelola" untuk mengedit atau menghapus model yang sudah ditambahkan.

## Mulai Menggunakan

Setelah menyelesaikan konfigurasi di atas, Anda dapat memilih penyedia AI kustom dan model di antarmuka obrolan Cherry Studio, dan mulai berkomunikasi dengan AI!

## Menggunakan vLLM sebagai Penyedia Layanan AI Kustom

vLLM adalah pustaka inferensi LLM yang cepat dan mudah digunakan, mirip dengan Ollama. Berikut langkah-langkah mengintegrasikan vLLM ke Cherry Studio:

1.  **Instal vLLM:** Ikuti dokumentasi resmi vLLM ([https://docs.vllm.ai/en/latest/getting\_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)) untuk menginstal vLLM.

    ```sh
    pip install vllm # jika menggunakan pip
    uv pip install vllm # jika menggunakan uv
    ```
2.  **Mulai Layanan vLLM:** Mulai layanan menggunakan antarmuka OpenAI-compatible yang disediakan vLLM. Ada dua cara utama:

    * Mulai menggunakan `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Mulai menggunakan `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Pastikan layanan berhasil dimulai dan mendengarkan di port default `8000`. Tentu saja, Anda dapat menentukan nomor port layanan vLLM dengan parameter `--port`.

3. **Tambahkan Penyedia vLLM di Cherry Studio:**
   * Ikuti langkah sebelumnya untuk menambahkan penyedia AI kustom baru di Cherry Studio.
   * **Nama Penyedia:** `vLLM`
   * **Tipe Penyedia:** Pilih `OpenAI`.
4. **Konfigurasi Penyedia vLLM:**
   * **Kunci API:** Karena vLLM tidak memerlukan kunci API, biarkan kosong atau isi dengan konten apa pun.
   * **Alamat API:** Isi alamat API layanan vLLM. Secara default: `http://localhost:8000/` (jika menggunakan port berbeda, ubah sesuai).
   * **Manajemen Model:** Tambahkan nama model yang Anda muat di vLLM. Dalam contoh `python -m vllm.entrypoints.openai.api_server --model gpt2`, masukkan `gpt2` di sini.
5. **Mulai Berkomunikasi:** Sekarang Anda dapat memilih penyedia vLLM dan model `gpt2` di Cherry Studio, dan mulai berkomunikasi dengan LLM berbasis vLLM!

## Tip dan Trik

* **Baca Dokumentasi dengan Cermat:** Sebelum menambahkan penyedia kustom, pastikan membaca dokumentasi resmi penyedia AI yang Anda gunakan untuk memahami informasi kunci seperti kunci API, alamat akses, dan nama model.
* **Periksa Kunci API:** Gunakan tombol "Periksa" untuk memverifikasi keabsahan kunci API dengan cepat, hindari kegagalan karena kesalahan kunci.
* **Perhatikan Alamat API:** Alamat API mungkin berbeda untuk penyedia AI dan model yang berbeda, pastikan mengisi dengan benar.
* **Tambahkan Model Sesuai Kebutuhan:** Hanya tambahkan model yang benar-benar akan Anda gunakan, hindari menambahkan terlalu banyak model yang tidak berguna.