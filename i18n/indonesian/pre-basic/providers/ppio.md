
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# PPIO Paiou Cloud

## Cherry Studio Terhubung ke API LLM PPIO

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#ringkasan-tutorial)Ringkasan Tutorial <a href="#ringkasan-tutorial" id="ringkasan-tutorial"></a>

Cherry Studio adalah klien desktop multi-model yang saat ini mendukung: paket instalasi untuk komputer Windows, Linux, dan MacOS. Ini mengintegrasikan model LLM utama, menyediakan bantuan berbagai skenario. Pengguna dapat meningkatkan efisiensi kerja melalui manajemen percakapan cerdas, kustomisasi sumber terbuka, dan antarmuka multi-tema.

Cherry Studio kini terintegrasi penuh dengan **saluran API berkinerja tinggi PPIO** — melalui jaminan komputasi tingkat perusahaan, mencapai **respons cepat DeepSeek-R1/V3** dan **ketersediaan layanan 99,9%**, memberikan Anda pengalaman yang lancar dan andal.

Tutorial di bawah ini berisi skema penyambungan lengkap (termasuk konfigurasi kunci API), mulai mode lanjutan "Penjadwalan Cerdas Cherry Studio + API Berkinerja Tinggi PPIO" dalam 3 menit.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-masuk-ke-cherrystudio-tambahkan-ppio-sebagai-penyedia-model)1. Masuk ke CherryStudio, Tambahkan “PPIO” Sebagai Penyedia Model <a href="#1-masuk-ke-cherrystudio-tambahkan-ppio-sebagai-penyedia-model" id="1-masuk-ke-cherrystudio-tambahkan-ppio-sebagai-penyedia-model"></a>

Pertama, unduh Cherry Studio dari situs resmi: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (Jika tidak dapat diakses, buka tautan Quark Cloud berikut untuk mengunduh versi yang Anda butuhkan: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share)

(1) Klik ikon pengaturan di kiri bawah, atur nama penyedia menjadi: `PPIO`, klik "OK"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Kunjungi [Manajemen Kunci API PPIO Computing Cloud](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), klik 【Ikon Pengguna】—【Manajemen Kunci API】 untuk masuk ke konsol

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Klik tombol 【+ Buat】 untuk membuat kunci API baru. Beri nama untuk kunci, **kunci yang dihasilkan hanya ditampilkan saat pembuatan, pastikan untuk menyalin dan menyimpannya ke dokumen agar tidak mengganggu penggunaan selanjutnya**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Di CherryStudio, masukkan kunci API. Klik pengaturan, pilih 【PPIO Paiou Cloud】, masukkan kunci API yang dihasilkan dari situs resmi, lalu klik 【Periksa】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Pilih model: contohnya deepseek/deepseek-r1/community. Jika ingin mengganti model lain, bisa langsung diganti.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 dan V3 versi community disediakan untuk mencoba, juga merupakan versi penuh dari model. Stabilitas dan performa tidak berbeda. **Jika perlu pemanggilan besar-besaran, isi saldo dan ganti ke versi non-community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-konfigurasi-penggunaan-model)2. Konfigurasi Penggunaan Model <a href="#2-konfigurasi-penggunaan-model" id="2-konfigurasi-penggunaan-model"></a>

(1) Klik 【Periksa】, jika koneksi berhasil, model dapat digunakan secara normal

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Terakhir klik 【@】, pilih model DeepSeek R1 yang baru ditambahkan di bawah penyedia PPIO, lalu mulai percakapan\~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Sumber materi sebagian：[Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-tutorial-penggunaan-video-ppio-cherry-studio)3. Tutorial Penggunaan Video PPIO×Cherry Studio <a href="#3-tutorial-penggunaan-video-ppio-cherry-studio" id="3-tutorial-penggunaan-video-ppio-cherry-studio"></a>

Jika Anda lebih suka belajar secara visual, kami menyiapkan tutorial video di Bilibili. Dengan panduan langkah demi langkah, kami membantu Anda menguasai metode konfigurasi "PPIO API + Cherry Studio" dengan cepat. Klik tautan di bawah ini untuk langsung menuju video → [《 **Masih frustrasi karena DeepSeek terus-menerus berputar?** PPIO Cloud + DeepSeek versi penuh = ? Tidak ada kemacetan, langsung melesat》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Sumber materi video: sola】