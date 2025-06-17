---
icon: floppy-disk
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Localização Padrão de Armazenamento

O armazenamento de dados do Cherry Studio segue as normas do sistema. Os dados são automaticamente colocados no diretório do usuário, com as localizações específicas abaixo:

> macOS: /Users/username/Library/Application Support/CherryStudioDev
> 
> Windows: C:\Users\username\AppData\Roaming\CherryStudio
> 
> Linux: /home/username/.config/CherryStudio

Também é possível visualizar na seguinte localização:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# Alterar Local de Armazenamento (para referência)

Método 1:

É possível criar um link simbólico. Feche o software, mova os dados para o local desejado e crie um link na localização original apontando para o novo local.

Para passos detalhados, consulte: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Método 2:
Com base nas características dos aplicativos Electron, modifique o local de armazenamento configurando parâmetros de inicialização.

> --user-data-dir
> 
> Exemplo: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Exemplo:

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
@title Inicialização do CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Local atual: %current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Diretório de dados do CherryStudio: %user_data_dir%

@echo Localizando Cherry-Studio-*-portable.exe no diretório atual
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Este código é compatível com versões baixadas do GitHub e do site oficial. Para outras versões, modifique conforme necessário.
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Arquivo encontrado: %target_file%
) else (
    echo Nenhum arquivo correspondente encontrado, saindo do script
    pause
    exit
)

@echo Confirme para continuar
pause

@echo Iniciando CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Operação concluída
@echo on
exit
```

> Estrutura do diretório user-data-dir após inicialização:

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