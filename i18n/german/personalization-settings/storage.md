---
icon: floppy-disk
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Standard-Speicherort

Cherry Studio-Daten werden gemäß Systemstandards gespeichert und automatisch im Benutzerverzeichnis abgelegt. Die genauen Verzeichnispfade sind:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Sie können auch an folgender Stelle nachsehen:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# Speicherort ändern (Referenz)

**Methode 1:**

Sie können eine symbolische Verknüpfung erstellen. Beenden Sie die Software, verschieben Sie die Daten an den gewünschten Speicherort und erstellen Sie am ursprünglichen Ort eine Verknüpfung zum neuen Speicherort.

Einzelne Schritte können hier nachgelesen werden:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Methode 2:**  
Basierend auf den Eigenschaften von Electron-Anwendungen kann der Speicherort über Startparameter angepasst werden.

> --user-data-dir  
> Beispiel: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Beispiel:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (Kodierung: ANSI)

```bash
@title CherryStudio Initialisierung
@echo off

set current_path_dir=%~dp0
@echo Aktueller Pfad:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio Datenpfad:%user_data_dir%

@echo Suche nach Cherry-Studio-*-portable.exe im aktuellen Pfad
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #Bitte an den tatsächlichen Dateinamen anpassen (unterschiedliche Namen bei Download von offizieller Website vs. Github)
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Datei gefunden: %target_file%
) else (
    echo Keine passende Datei gefunden, Skript wird beendet
    pause
    exit
)

@echo Bestätigen Sie zum Fortfahren
pause

@echo Starte CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Vorgang abgeschlossen
@echo on
exit
```

> Verzeichnisstruktur nach Initialisierung von user-data-dir:

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