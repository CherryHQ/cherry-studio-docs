---
icon: floppy-disk
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Varsayılan Depolama Konumu

Cherry Studio veri depolama, sistem özelliklerini takip eder ve veriler otomatik olarak kullanıcı dizini altına yerleştirilir. Belirli dizin konumları aşağıdaki gibidir:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Ayrıca şu konumda görüntüleyebilirsiniz:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# Depolama Konumunu Değiştirme (Referans İçin)

**Yöntem 1:**

Yumuşak bağlantı oluşturularak gerçekleştirilebilir. Yazılımı kapatın, verileri saklamak istediğiniz konuma taşıyın ve ardından orijinal konumda, taşınan konuma işaret eden bir bağlantı oluşturun.

Spesifik işlem adımları şurada referans alınabilir: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Yöntem 2:**
Electron uygulamasının özelliklerine dayanarak, başlatma parametrelerini yapılandırarak depolama konumu değiştirilebilir.

> --user-data-dir
> Örneğin: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Örnek:

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
@title CherryStudio Başlatma
@echo off

set current_path_dir=%~dp0
@echo Geçerli yol:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio veri yolu:%user_data_dir%

@echo Geçerli dizinde Cherry-Studio-*-portable.exe aranıyor
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #Lütfen gerçek indirilen dosya adına göre değiştirin, resmi web sitesinden indirilen ve Github'dan indirilen farklıdır
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Dosya bulundu: %target_file%
) else (
    echo Eşleşen dosya bulunamadı, komut dosyasından çıkılıyor
    pause
    exit
)

@echo Devam etmek için onaylayın
pause

@echo CherryStudio başlatılıyor
start %target_file% --user-data-dir="%user_data_dir%"

@echo İşlem tamamlandı
@echo on
exit
```

> Dizin user-data-dir başlatma sonrası yapısı:

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