---
icon: floppy-disk
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Local de Armazenamento Padrão

O armazenamento de dados do Cherry Studio segue as normas do sistema, onde os dados são automaticamente salvos no diretório do usuário, conforme as seguintes localizações:

> macOS: /Users/username/Library/Application Support/CherryStudioDev  
> Windows: C:\Users\username\AppData\Roaming\CherryStudio  
> Linux: /home/username/.config/CherryStudio  

Esta localização também pode ser verificada em:  
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# Modificar o Local de Armazenamento (Referência)

**Método 1:**  
Você pode criar um link simbólico. Saia do aplicativo, mova os dados para o local desejado e crie um link no local original apontando para o novo diretório.

Instruções detalhadas:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Método 2:**  
Aproveitando características do Electron, configure parâmetros de inicialização para alterar o diretório de armazenamento.

> --user-data-dir  
> Exemplo: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Demonstração:

```shell
PS D:\CherryStudio> dir

     Diretório: D:\CherryStudio

Modo        ÚltimaEscrita    Comprimento Nome
----        -------------    ------ ----
d-----      2025/4/18 14:05             user-data-dir
-a----      2025/4/14 23:05   94987175  Cherry-Studio-1.2.4-x64-portable.exe
-a----      2025/4/18 14:05        701  init_cherry_studio.bat
```

> init_cherry_studio.bat (codificação: ANSI)

```bash
@title Inicializar CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Diretório atual: %current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Diretório de dados: %user_data_dir%

@echo Procurando executável Cherry-Studio-*-portable.exe
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Adaptado para versões do GitHub e site oficial
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Arquivo encontrado: %target_file%
) else (
    echo Nenhum arquivo compatível encontrado
    pause
    exit
)

@echo Pressione qualquer tecla para continuar
pause

@echo Iniciando CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Processo concluído
@echo on
exit
```

> Estrutura do diretório user-data-dir após inicialização:

```shell
PS D:\CherryStudio> dir .\user-data-dir\

     Diretório: D:\CherryStudio\user-data-dir

Modo        ÚltimaEscrita    Comprimento Nome
----        -------------    ------ ----
d-----      2025/4/18 14:29             blob_storage
d-----      2025/4/18 14:07             Cache
d-----      2025/4/18 14:07             Code Cache
d-----      2025/4/18 14:07             Data
d-----      2025/4/18 14:07             DawnGraphiteCache
d-----      2025/4/18 14:07             DawnWebGPUCache
d-----      2025/4/18 14:07             Dictionaries
d-----      2025/4/18 14:07             GPUCache
d-----      2025/4/18 14:07             IndexedDB
d-----      2025/4/18 14:07             Local Storage
d-----      2025/4/18 14:07             logs
d-----      2025/4/18 14:30             Network
d-----      2025/4/18 14:07             Partitions
d-----      2025/4/18 14:29             Session Storage
d-----      2025/4/18 14:07             Shared Dictionary
d-----      2025/4/18 14:07             WebStorage
-a----      2025/4/18 14:07         36  .updaterId
-a----      2025/4/18 14:29         20  config.json
-a----      2025/4/18 14:07        434  Local State
-a----      2025/4/18 14:29         57  Preferences
-a----      2025/4/18 14:09       4096  SharedStorage
-a----      2025/4/18 14:30        140  window-state.json
```