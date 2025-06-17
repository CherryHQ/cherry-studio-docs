---
icon: floppy-disk
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

```markdown
---
icon: cherries
---

# Local de Armazenamento Padrão

O armazenamento de dados do Cherry Studio segue as especificações do sistema. Os dados são colocados automaticamente no diretório do usuário. Os locais específicos são os seguintes:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Também pode visualizar nesta localização:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# Modificação do Local de Armazenamento (Referência)

Método 1:

Isto pode ser realizado criando uma ligação simbólica. Feche o software, mova os dados para a localização desejada e crie um link simbólico no local original apontando para o novo local.

Passos detalhados podem ser consultados em:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Método 2:
Com base nas características do aplicativo Electron, modifique o local de armazenamento configurando parâmetros de inicialização.

> --user-data-dir
> ex: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

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

> init_cherry_studio.bat (codificação: ANSI)

```bash
@title CherryStudio 初始化
@echo off

set current_path_dir=%~dp0
@echo 当前路径:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio 数据路径:%user_data_dir%

@echo 查找当前路径下 Cherry-Studio-*-portable.exe
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #Por favor, ajuste para o nome do arquivo baixado (os nomes são diferentes no site oficial e no Github)
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo 找到文件: %target_file%
) else (
    echo 未找到匹配文件，退出该脚本
    pause
    exit
)

@echo 确认请继续
pause

@echo 启动 CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo 操作结束
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