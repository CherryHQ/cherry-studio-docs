---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Vertex AI

## Ringkasan Tutorial

### 1. Mendapatkan API Key

* Sebelum memperoleh API Key Gemini, Anda harus memiliki proyek Google Cloud (lewati langkah ini jika sudah punya)
* Kunjungi [Google Cloud](https://console.cloud.google.com/projectcreate) untuk membuat proyek, isi nama proyek lalu klik "Buat Proyek"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Masuk ke [Konsol Vertex AI](https://console.cloud.google.com/vertex-ai)
* Aktifkan [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) di proyek yang telah dibuat

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Mengatur Izin Akses API

* Buka halaman izin [akun layanan](https://console.cloud.google.com/iam-admin/serviceaccounts), lalu buat akun layanan

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Di halaman manajemen akun layanan, temukan akun yang baru dibuat, klik `Kunci` dan buat kunci baru format JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Setelah berhasil dibuat, file kunci akan otomatis tersimpan di komputer Anda dalam format JSON – **simpan dengan baik**

## 3. Mengonfigurasi Vertex AI di Cherry Studio

* Pilih penyedia layanan Vertex AI
* Isi kolom sesuai dengan field di file JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Klik tambah [model](https://console.cloud.google.com/vertex-ai/model-garden), dan Anda bisa mulai menggunakannya dengan senang!