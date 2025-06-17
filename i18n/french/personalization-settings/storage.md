---
icon: floppy-disk
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Emplacement de stockage par défaut

Le stockage des données de Cherry Studio suit les normes système. Les données sont automatiquement placées dans le répertoire utilisateur, aux emplacements spécifiques suivants :

> macOS: /Users/username/Library/Application Support/CherryStudioDev  
> Windows: C:\Users\username\AppData\Roaming\CherryStudio  
> Linux: /home/username/.config/CherryStudio  

Vous pouvez également consulter l'emplacement ici :  
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# Modifier l'emplacement de stockage (à titre indicatif)

**Méthode 1 :**  
Vous pouvez utiliser des liens symboliques. Fermez l'application, déplacez les données vers le nouvel emplacement, puis créez un lien symbolique pointant vers cet emplacement.

Consultez les étapes détaillées :  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Méthode 2 :**  
Modifiez l'emplacement via les paramètres de démarrage, en exploitant les caractéristiques des applications Electron.

> --user-data-dir  
> Exemple : Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Exemple :

```shell
PS D:\CherryStudio> dir

    目录: D:\CherryStudio

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (encodage : ANSI)

```bash
@title Initialisation CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Chemin actuel : %current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Chemin des données CherryStudio : %user_data_dir%

@echo Recherche de Cherry-Studio-*-portable.exe dans le chemin actuel
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Ce code est compatible avec les versions GitHub et officielles, modifiez pour d'autres
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Fichier trouvé : %target_file%
) else (
    echo Aucun fichier correspondant trouvé, fermeture du script
    pause
    exit
)

@echo Confirmer pour continuer
pause

@echo Lancement de CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Opération terminée
@echo on
exit
```

> Structure du répertoire user-data-dir après initialisation :

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