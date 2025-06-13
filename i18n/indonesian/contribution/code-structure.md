---
hidden: True
icon: code
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Struktur Kode

```yaml
...
├─ docs/ #Direktori dokumentasi
├─ resources/ #Direktori file sumber daya
├─ scripts/ #Direktori file skrip
└─ src/ #Direktori kode sumber utama
    ├─main/ #Kode proses utama
    ├─preload/ #Direktori skrip pramuat
    └─renderer/ #Kode proses renderer
        ├─src/ #Kode sumber proses renderer
            ├─assets/ #File sumber daya
                ├─fonts/ #File font
                ├─images/ #File gambar seperti avatar
                └─styles/ #File gaya
            ├─components/ #Komponen
            ├─config/ #File konfigurasi
            ├─context/ #Konteks
            ├─databases/ #File terkait database
            ├─hooks/ #Kustom Hooks
            ├─i18n/ #File internasionalisasi
            ├─pages/ #File halaman
            ├─providers/ #Konfigurasi terkait penyedia layanan
            ├─services/ #File layanan
            ├─store/ #File manajemen status
            ├─types/ #File definisi tipe TypeScript
            ├─utils/ #Fungsi utilitas
            ...
        ...
    ...
...
```