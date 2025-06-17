---
icon: floppy-disk
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Lokasi Penyimpanan Default

Cherry Studio menyimpan data sesuai dengan standar sistem, dan data akan secara otomatis ditempatkan di direktori pengguna. Detail lokasi direktori adalah sebagai berikut:

> macOS: /Users/username/Library/Application Support/CherryStudioDev  
> Windows: C:\Users\username\AppData\Roaming\CherryStudio  
> Linux: /home/username/.config/CherryStudio  

Dapat juga dilihat di lokasi berikut:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# Mengubah Lokasi Penyimpanan (Referensi)

**Metode 1:**  
Dapat dilakukan dengan membuat symbolic link. Keluar dari aplikasi, pindahkan data ke lokasi yang diinginkan, kemudian buat link di lokasi asli yang mengarah ke lokasi baru.

Langkah detail dapat merujuk:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Metode 2:**  
Berdasarkan karakteristik aplikasi Electron, ubah lokasi penyimpanan melalui parameter startup.

> --user-data-dir  
> Contoh: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Contoh:

```shell
PS D:\CherryStudio> dir

    目录: D:\CherryStudio

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
@echo Path data CherryStudio:%user_data_dir%

@echo Mencari Cherry-Studio-*-portable.exe di path saat ini
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #Silakan sesuaikan dengan nama file unduhan aktual, berbeda antara unduhan resmi dan GitHub
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo File ditemukan: %target_file%
) else (
    echo File tidak ditemukan, keluar dari skrip
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

    目录: D:\CherryStudio\user-data-dir

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