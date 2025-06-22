---
icon: floppy-disk
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Стандартное расположение хранения данных

Данные Cherry Studio сохраняются согласно системным стандартам и автоматически размещаются в пользовательском каталоге. Точные пути следующие:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Также можно посмотреть расположение здесь:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# Изменение места хранения данных (справочно)

**Способ 1:**
Создайте символическую ссылку. Завершите работу приложения, переместите данные в нужное расположение, затем создайте ссылку из оригинального пути к новому местоположению.

Подробные инструкции смотрите здесь: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Способ 2:**
Используйте особенности приложений Electron и измените путь через параметры запуска.

> --user-data-dir
> Пример: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Пример реализации:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (кодировка: ANSI)

```bash
@title CherryStudio Initialization
@echo off

set current_path_dir=%~dp0
@echo Текущий путь:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Путь к данным CherryStudio:%user_data_dir%

@echo Поиск Cherry-Studio-*-portable.exe в текущей директории
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Этот код совместим с версиями с GitHub и с официального сайта; для других версий измените самостоятельно
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Найден файл: %target_file%
) else (
    echo Совпадающие файлы не найдены, выход из скрипта
    pause
    exit
)

@echo Подтвердите действие
pause

@echo Запуск CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Операция завершена
@echo on
exit
```

> Структура каталога user-data-dir после инициализации:

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