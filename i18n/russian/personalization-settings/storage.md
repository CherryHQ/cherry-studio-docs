---
icon: floppy-disk
---
# Изменение места хранения


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




## Место хранения по умолчанию

Хранение данных Cherry Studio соответствует системным спецификациям. Данные автоматически размещаются в домашнем каталоге пользователя по следующим путям:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Также можно просмотреть расположение здесь:

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

## Изменение места хранения (справочно)

Способ 1:

Можно создать символическую ссылку. Закройте приложение, переместите данные в желаемое место, затем создайте ссылку из исходного местоположения на новое.

Подробные шаги смотрите в: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Способ 2:\
Измените место хранения через параметры запуска, используя особенности приложений Electron.

> \--user-data-dir\
> Например: Cherry-Studio-\*-x64-portable.exe --user-data-dir="%user\_data\_dir%"

> Пример:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init\_cherry\_studio.bat (кодировка: ANSI)

```bash
@title Инициализация CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Текущий путь:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Путь данных CherryStudio:%user_data_dir%

@echo Поиск Cherry-Studio-*-portable.exe в текущем каталоге
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Этот код подходит для версий с GitHub и официального сайта; для других случаев измените самостоятельно
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Найден файл: %target_file%
) else (
    echo Совпадений не найдено, выход из скрипта
    pause
    exit
)

@echo Подтвердите для продолжения
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