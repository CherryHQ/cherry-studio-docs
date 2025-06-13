---
icon: floppy-disk
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Standaard Opslaglocatie

Cherry Studio-gegevensopslag volgt de systeemnormen. Gegevens worden automatisch in de gebruikersmap geplaatst, op de volgende specifieke locaties:

> macOS: /Users/username/Library/Application Support/CherryStudioDev  
> Windows: C:\Users\username\AppData\Roaming\CherryStudio  
> Linux: /home/username/.config/CherryStudio  

De locatie is ook zichtbaar via:  
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# Opslaglocatie Wijzigen (ter referentie)

**Methode 1:**  
Maak een symbolische link aan. Sluit de software, verplaats de gegevens naar de gewenste locatie en maak vervolgens een link vanaf de oorspronkelijke locatie naar de nieuwe locatie.  

Zie voor gedetailleerde stappen:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Methode 2:**  
Pas opslaglocatie aan via opstartparameters (gebaseerd op Electron-applicatiekenmerken).

> --user-data-dir  
> Voorbeeld: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Voorbeeld:

```shell
PS D:\CherryStudio> dir

    目录: D:\CherryStudio

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (codering: ANSI)

```bash
@title CherryStudio Initialisatie
@echo off

set current_path_dir=%~dp0
@echo Huidig pad:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio gegevenspad:%user_data_dir%

@echo Zoeken naar Cherry-Studio-*-portable.exe in huidige pad
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #Wijzig naar daadwerkelijke bestandsnaam (officiële site en GitHub gebruiken verschillende namen)
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Bestand gevonden: %target_file%
) else (
    echo Geen overeenkomend bestand gevonden, script wordt afgesloten
    pause
    exit
)

@echo Bevestig om door te gaan
pause

@echo CherryStudio opstarten
start %target_file% --user-data-dir="%user_data_dir%"

@echo Operatie voltooid
@echo on
exit
```

> Directorystructuur na initialisatie van user-data-dir:

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