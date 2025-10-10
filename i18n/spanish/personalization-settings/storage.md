---
icon: floppy-disk
---
# Cambiar Ubicación de Almacenamiento


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Ubicación de Almacenamiento Predeterminada

El almacenamiento de datos de Cherry Studio sigue las especificaciones del sistema. Los datos se colocan automáticamente en el directorio del usuario, en las siguientes ubicaciones específicas:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

También puede verificarse en la siguiente ubicación:

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

## Cambiar Ubicación de Almacenamiento (Referencia)

Método 1:

Puede lograr esto creando un enlace simbólico. Cierre el software, mueva los datos a la ubicación deseada, luego cree un enlace en la ubicación original que apunte a la nueva ubicación.

Los pasos operativos específicos pueden consultarse en:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Método 2:  
Basado en las características de las aplicaciones Electron, modifique la ubicación de almacenamiento mediante parámetros de inicio.

> \--user-data-dir  
> Ejemplo: Cherry-Studio-\*-x64-portable.exe --user-data-dir="%user\_data\_dir%"

> Ejemplo:

```shell
PS D:\CherryStudio> dir

    Directorio: D:\CherryStudio

Modo         ÚltimaEscritura         Longitud Nombre
----         -------------         ------ ----
d-----   2025/4/18     14:05                user-data-dir
-a----   2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----   2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (codificación: ANSI)

```bash
@title Inicialización de CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Ruta actual: %current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Ruta de datos de CherryStudio: %user_data_dir%

@echo Buscando Cherry-Studio-*-portable.exe en la ruta actual
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Este código es compatible con las versiones descargadas de GitHub y del sitio oficial. Para otros, modifíquelo usted mismo.
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Archivo encontrado: %target_file%
) else (
    echo No se encontraron archivos coincidentes, saliendo del script
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

> Estructura del directorio user-data-dir después de la inicialización:

```shell
PS D:\CherryStudio> dir .\user-data-dir\

    Directorio: D:\CherryStudio\user-data-dir

Modo         ÚltimaEscritura         Longitud Nombre
----         -------------         ------ ----
d-----   2025/4/18     14:29                blob_storage
d-----   2025/4/18     14:07                Cache
d-----   2025/4/18     14:07                Code Cache
d-----   2025/4/18     14:07                Data
d-----   2025/4/18     14:07                DawnGraphiteCache
d-----   2025/4/18     14:07                DawnWebGPUCache
d-----   2025/4/18     14:07                Dictionaries
d-----   2025/4/18     14:07                GPUCache
d-----   2025/4/18     14:07                IndexedDB
d-----   2025/4/18     14:07                Local Storage
d-----   2025/4/18     14:07                logs
d-----   2025/4/18     14:30                Network
d-----   2025/4/18     14:07                Partitions
d-----   2025/4/18     14:29                Session Storage
d-----   2025/4/18     14:07                Shared Dictionary
d-----   2025/4/18     14:07                WebStorage
-a----   2025/4/18     14:07             36 .updaterId
-a----   2025/4/18     14:29             20 config.json
-a----   2025/4/18     14:07            434 Local State
-a----   2025/4/18     14:29             57 Preferences
-a----   2025/4/18     14:09           4096 SharedStorage
-a----   2025/4/18     14:30            140 window-state.json
```