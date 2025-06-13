---
icon: database
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Penjelasan Penyimpanan Data

Data yang ditambahkan ke dalam basis pengetahuan Cherry Studio seluruhnya disimpan secara lokal. Selama proses penambahan, satu salinan dokumen akan ditempatkan di direktori penyimpanan data Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Diagram Alir Pemrosesan Basis Pengetahuan</p></figcaption></figure>

Basis Data Vektor: [https://turso.tech/libsql](https://turso.tech/libsql)

Setelah dokumen ditambahkan ke basis pengetahuan Cherry Studio, file akan dipotong menjadi beberapa segmen. Segmen-segmen ini kemudian akan diproses oleh model embedding.

Saat menggunakan model besar untuk tanya jawab, sistem akan mencari segmen teks yang relevan dengan pertanyaan dan menyertakannya dalam pemrosesan oleh model bahasa besar (LLM).

Jika memiliki persyaratan khusus tentang privasi data, disarankan menggunakan basis data embedding lokal dan model bahasa besar lokal.