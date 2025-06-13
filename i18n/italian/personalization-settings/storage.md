---
icon: floppy-disk
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Posizione di archiviazione predefinita

La memorizzazione dei dati di Cherry Studio segue le specifiche del sistema. I dati vengono automaticamente posizionati nella directory utente nelle seguenti posizioni:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Puoi anche verificare la posizione qui:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# Modifica della posizione di archiviazione (per riferimento)

Metodo 1:

È possibile utilizzare un collegamento simbolico. Chiudi il software, sposta i dati nella posizione desiderata, quindi crea un collegamento alla nuova posizione nella posizione originale.

Per passaggi dettagliati, consulta: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Metodo 2:
Sfruttando le caratteristiche delle applicazioni Electron, modifica la posizione di archiviazione configurando i parametri di avvio.

> --user-data-dir
> Esempio: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Esempio:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (codifica: ANSI)

```bash
@title Inizializzazione CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Percorso corrente: %current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Percorso dati CherryStudio: %user_data_dir%

@echo Ricerca di Cherry-Studio-*-portable.exe nel percorso corrente
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #Modificare con il nome effettivo del file scaricato, i nomi differiscono tra sito ufficiale e GitHub
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo File trovato: %target_file%
) else (
    echo Nessun file corrispondente trovato, script terminato
    pause
    exit
)

@echo Confermare per continuare
pause

@echo Avvio CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Operazione completata
@echo on
exit
```

> Struttura della directory user-data-dir dopo l'inizializzazione:

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