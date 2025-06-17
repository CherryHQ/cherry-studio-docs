---
icon: floppy-disk
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Lokasi Penyimpanan Default

Penyimpanan data Cherry Studio mengikuti spesifikasi sistem, data akan otomatis ditempatkan di direktori pengguna. Lokasi spesifik direktori adalah sebagai berikut:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Juga dapat dilihat di lokasi berikut:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# Mengubah Lokasi Penyimpanan (Sebagai Referensi)

Metode 1:

Dapat dilakukan dengan membuat tautan simbolis (symlink). Keluarkan aplikasi, pindahkan data ke lokasi penyimpanan yang diinginkan, lalu buat tautan di lokasi asli yang merujuk ke lokasi baru.

Langkah operasional spesifik dapat merujuk: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Metode 2:
Berdasarkan karakteristik aplikasi Electron, modifikasi lokasi penyimpanan melalui konfigurasi parameter startup.

> --user-data-dir
> Contoh: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Contoh:

```shell
PS D:\CherryStudio> dir


    Direktori: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (encoding: ANSI)

```bash
@title Inisialisasi CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Lokasi saat ini:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Jalur data CherryStudio:%user_data_dir%

@echo Mencari Cherry-Studio-*-portable.exe di jalur saat ini
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #Kode ini disesuaikan untuk versi unduhan GitHub dan situs web resmi, silakan modifikasi sendiri untuk versi lain
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Berkas ditemukan: %target_file%
) else (
    echo Berkas yang cocok tidak ditemukan, keluar dari skrip
    pause
    exit
)

@echo Konfirmasi untuk melanjutkan
pause

@echo Memulai CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Operasi selesai
@echo on
exit
```

> Struktur direktori user-data-dir setelah inisialisasi:

```shell
PS D:\CherryStudio> dir .\user-data-dir\


    Direktori: D:\CherryStudio\user-data-dir


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:29                blob_storage
d-----         2025/4/18     14:07                Cache
d-----         2025/4/18     14:07                Code Cache
d-----         2025/4/18     14:07                Data
d-----         2025/4/18     14:07                DawnGraphiteCache
d-----         2025/4/18     14:07                DawnWebGPUCache
d-----         2025/4/18     14:07                Dictionaries
d-----         2025/4/18     14:07                GPUCache
d-----         2025/4/18     14:07                IndexedDB
d-----         2025/4/18     14:07                Local Storage
d-----         2025/4/18     14:07                logs
d-----         2025/4/18     14:30                Network
d-----         2025/4/18     14:07                Partitions
d-----         2025/4/18     14:29                Session Storage
d-----         2025/4/18     14:07                Shared Dictionary
d-----         2025/4/18     14:07                WebStorage
-a----         2025/4/18     14:07             36 .updaterId
-a----         2025/4/18     14:29             20 config.json
-a----         2025/4/18     14:07            434 Local State
-a----         2025/4/18     14:29             57 Preferences
-a----         2025/4/18     14:09           4096 SharedStorage
-a----         2025/4/18     14:30            140 window-state.json
```