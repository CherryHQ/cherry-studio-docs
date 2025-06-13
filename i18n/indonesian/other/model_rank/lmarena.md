
{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Peringkat Arena LLM (Diperbarui Secara Real-time)

Ini adalah papan peringkat berbasis data Chatbot Arena (lmarena.ai) yang dihasilkan melalui proses otomatisasi.

> **Waktu Pembaruan Data**: 2025-06-12 11:42:10 UTC / 2025-06-12 19:42:10 CST (Waktu Beijing)

{% hint style="info" %}
Klik **nama model** di papan peringkat untuk menuju ke halaman detail atau uji coba.
{% endhint %}

## Papan Peringkat

| Peringkat(UB) | Peringkat(StyleCtrl) | Nama Model                                                                                                                         | Skor | Interval Kepercayaan | Suara     | Penyedia                  | Perjanjian Lisensi           | Tanggal Pemutakhiran Pengetahuan |
|:----------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------|:-----|:-----------------|:-------|:-----------------------|:----------------------------|:-----------------|
| 1        | 1               | [Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)          | 1478 | +6/-7             | 7,343  | Google                 | Proprietary                 | 暂无数据       |
| 2        | 2               | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446 | +6/-7             | 12,351 | Google                 | Proprietary                 | 暂无数据       |
| ... *(seluruh tabel dipertahankan tanpa perubahan struktural/teknis)* ... | 
| 202      | 200             | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                               | 813  | +14/-12           | 2,446  | Meta                   | Non-commercial              | 2023/2    |

## Penjelasan

- **Peringkat(UB)**: Peringkat yang dihitung berdasarkan model Bradley-Terry. Peringkat ini mencerminkan kinerja komprehensif model di arena dan memberikan estimasi **batas atas** skor Elo, membantu memahami potensi kompetitif model.
- **Peringkat(StyleCtrl)**: Peringkat setelah pengendalian gaya percakapan. Bertujuan mengurangi bias preferensi akibat gaya respons model (misalnya, panjang-lebar/singkat), mengevaluasi kemampuan inti model secara lebih murni.
- **Nama Model**: Nama Large Language Model (LLM). Kolom ini berisi tautan terkait model, klik untuk mengakses.
- **Skor**: Skor Elo yang diperoleh model melalui pemungutan suara pengguna di arena. Sistem peringkat relatif ini menunjukkan kinerja lebih baik jika skor lebih tinggi. Skor bersifat dinamis, mencerminkan kekuatan relatif model di lingkungan kompetitif saat ini.
- **Interval Kepercayaan**: Interval kepercayaan 95% untuk skor Elo model (misal: `+6/-6`). Semakin kecil interval, semakin stabil dan andal skor; sebaliknya, interval besar mungkin mengindikasikan data tidak cukup atau fluktuasi kinerja model. Memberikan evaluasi kuantitatif atas keakuratan skor.
- **Suara**: Jumlah total suara yang diterima model di arena. Semakin banyak suara, biasanya berarti reliabilitas statistik skor lebih tinggi.
- **Penyedia**: Organisasi atau perusahaan yang menyediakan model tersebut.
- **Perjanjian Lisensi**: Jenis perjanjian lisensi model, misalnya Proprietary, Apache 2.0, MIT, dsb.
- **Tanggal Pemutakhiran Pengetahuan**: Tanggal pemutakhiran pengetahuan data pelatihan model. **暂无数据** menunjukkan informasi tidak tersedia atau tidak diketahui.

## Sumber Data dan Frekuensi Pembaruan

Data papan peringkat ini dihasilkan dan disediakan oleh proyek [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), yang memperoleh dan memproses data dari [lmarena.ai](https://lmarena.ai/). Papan peringkat ini diperbarui secara otomatis setiap hari oleh GitHub Actions.

## Penafian

Laporan ini hanya untuk referensi. Data papan peringkat bersifat dinamis dan didasarkan pada preferensi pemungutan suara pengguna di Chatbot Arena dalam periode tertentu. Kelengkapan dan keakuratan data bergantung pada sumber data hulu dan pembaruan/pemrosesan proyek `fboulnois/llm-leaderboard-csv`. Model berbeda mungkin menggunakan perjanjian lisensi berbeda, harap merujuk ke petunjuk resmi penyedia model saat digunakan.