---
icon: floppy-disk
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Ubicación de almacenamiento predeterminada

Cherry Studio sigue las especificaciones del sistema para almacenar datos, que se colocan automáticamente en el directorio del usuario. Las rutas específicas son las siguientes:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

También puede verificarse en la siguiente ubicación:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# Modificar ubicación de almacenamiento (como referencia)

**Método 1:**

Puede realizarse creando un enlace simbólico. Cierre la aplicación, mueva los datos a la ubicación deseada y cree un vínculo en la ubicación original que apunte a la nueva ubicación.

Consulte los pasos específicos aquí: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Método 2:**
Basado en las características de Electron, modifique la ubicación de almacenamiento mediante parámetros de inicio.

> --user-data-dir
> Ejemplo: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Ejemplo:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (codificación: ANSI)

```bash
@title Inicializar CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Ruta actual:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Ruta de datos CherryStudio:%user_data_dir%

@echo Buscando Cherry-Studio-*-portable.exe en la ruta actual
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Este código es compatible con versiones de GitHub y sitio oficial. Modificar para otros casos.
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Archivo encontrado: %target_file%
) else (
    echo Archivo no encontrado. Finalizando script.
    pause
    exit
)

@echo Confirme para continuar
pause

@echo Iniciando CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Operación completada
@echo on
exit
```

> Estructura del directorio user-data-dir después de inicialización:

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