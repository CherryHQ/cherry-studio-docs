
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Ollama

Ollama adalah alat sumber terbuka yang sangat baik yang memungkinkan Anda menjalankan dan mengelola berbagai model bahasa besar (LLM) dengan mudah di perangkat lokal. Cherry Studio sekarang telah mendukung integrasi Ollama, memungkinkan Anda berinteraksi langsung dengan LLM yang dijalankan lokal melalui antarmuka yang familiar, tanpa bergantung pada layanan cloud!

## Apa itu Ollama?

Ollama adalah alat yang menyederhanakan penyebaran dan penggunaan model bahasa besar (LLM). Alat ini memiliki fitur-fitur berikut:

* **Jalankan Lokal:** Model sepenuhnya berjalan di komputer lokal Anda tanpa memerlukan koneksi internet, melindungi privasi dan keamanan data Anda.
* **Mudah Digunakan:** Hanya dengan perintah baris perintah sederhana, Anda dapat mengunduh, menjalankan, dan mengelola berbagai LLM.
* **Model Beragam:** Mendukung berbagai model sumber terbuka populer seperti Llama 2, Deepseek, Mistral, Gemma, dan lainnya.
* **Lintas Platform:** Mendukung sistem macOS, Windows, dan Linux.
* **API Terbuka:** Mendukung antarmuka yang kompatibel dengan OpenAI dan dapat diintegrasikan dengan alat lain.

## Mengapa Menggunakan Ollama di Cherry Studio?

* **Tanpa Layanan Cloud:** Tidak lagi terbatas oleh kuota dan biaya API cloud, nikmati sepenuhnya kemampuan kuat LLM lokal.
* **Privasi Data:** Semua data percakapan Anda tetap disimpan di lokal, tidak perlu khawatir tentang kebocoran privasi.
* **Dapat Digunakan Offline:** Terus berinteraksi dengan LLM meski tanpa koneksi internet.
* **Kustomisasi:** Pilih dan konfigurasikan LLM yang paling sesuai dengan kebutuhan Anda.

## Mengonfigurasi Ollama di Cherry Studio

### **1. Menginstal dan Menjalankan Ollama**

Pertama, Anda perlu menginstal dan menjalankan Ollama di komputer Anda. Ikuti langkah-langkah berikut:

* **Unduh Ollama:** Kunjungi situs web resmi Ollama ([https://ollama.com/](https://ollama.com/)), unduh paket instalasi yang sesuai dengan sistem operasi Anda.\
    Di Linux, Anda dapat langsung menjalankan perintah untuk menginstal ollama:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Instal Ollama:** Ikuti petunjuk instalasi untuk menyelesaikan proses instalasi.
*   **Unduh Model:** Buka terminal (atau command prompt), gunakan perintah `ollama run` untuk mengunduh model yang ingin Anda gunakan. Misalnya, untuk mengunduh model Llama 2, jalankan:

    ```sh
    ollama run llama3.2
    ```

    Ollama akan otomatis mengunduh dan menjalankan model tersebut.
* **Jaga Ollama Tetap Berjalan:** Selama menggunakan Cherry Studio untuk berinteraksi dengan model Ollama, pastikan Ollama tetap berjalan.

### **2. Menambahkan Penyedia Ollama di Cherry Studio**

Selanjutnya, tambahkan Ollama sebagai penyedia layanan AI kustom di Cherry Studio:

* **Buka Pengaturan:** Di bilah navigasi sisi kiri antarmuka Cherry Studio, klik "Pengaturan" (ikon roda gigi).
* **Masuk ke Layanan Model:** Di halaman pengaturan, pilih tab "Layanan Model".
* **Tambahkan Penyedia:** Klik Ollama di daftar yang tersedia.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Mengonfigurasi Penyedia Ollama**

Temukan Ollama yang baru ditambahkan di daftar penyedia dan lakukan konfigurasi detail:

1. **Status Aktif:**
   * Pastikan sakelar di bagian paling kanan penyedia Ollama telah diaktifkan.
2. **Kunci API:**
   * Secara default, Ollama **tidak memerlukan** kunci API. Biarkan kolom ini kosong atau isi dengan konten apa pun.
3. **Alamat API:**
   *    Masukkan alamat API lokal yang disediakan Ollama. Biasanya alamatnya adalah:

       ```
       http://localhost:11434/
       ```

       Jika port telah diubah, silakan sesuaikan.
4. **Waktu Tetap Aktif:** Opsi ini mengatur waktu sesi yang dipertahankan, dalam satuan menit. Jika tidak ada percakapan baru dalam waktu yang ditentukan, Cherry Studio akan otomatis memutus koneksi dengan Ollama untuk menghemat sumber daya.
5. **Manajemen Model:**
   * Klik tombol "+ Tambah" untuk menambahkan nama model yang telah Anda unduh di Ollama secara manual.
   * Misalnya, jika Anda telah mengunduh model `llama3.2` melalui `ollama run llama3.2`, masukkan `llama3.2` di sini.
   * Klik tombol "Kelola" untuk mengedit atau menghapus model yang telah ditambahkan.

## Mulai Menggunakan

Setelah menyelesaikan konfigurasi di atas, Anda dapat memilih penyedia layanan Ollama dan model yang telah diunduh di antarmuka obrolan Cherry Studio, dan mulai berinteraksi dengan LLM lokal!

## Tips dan Trik

* **Pertama Kali Menjalankan Model:** Saat pertama kali menjalankan model tertentu, Ollama perlu mengunduh file model yang mungkin memakan waktu lama. Harap bersabar.
* **Lihat Model yang Tersedia:** Jalankan perintah `ollama list` di terminal untuk melihat daftar model Ollama yang telah Anda unduh.
* **Persyaratan Perangkat Keras:** Menjalankan model bahasa besar membutuhkan sumber daya komputasi yang memadai (CPU, memori, GPU), pastikan spesifikasi komputer Anda memenuhi persyaratan model.
* **Dokumentasi Ollama:** Klik tautan `Lihat dokumentasi dan model Ollama` di halaman konfigurasi untuk langsung menuju ke dokumentasi resmi Ollama.