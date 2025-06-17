---
icon: floppy-disk
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 기본 저장 위치

Cherry Studio 데이터 저장은 시스템 규범을 따르며, 데이터는 자동으로 사용자 디렉터리에 저장됩니다. 구체적인 디렉터리 위치는 다음과 같습니다:

> macOS: /Users/username/Library/Application Support/CherryStudioDev  
> Windows: C:\Users\username\AppData\Roaming\CherryStudio  
> Linux: /home/username/.config/CherryStudio  

다음 위치에서도 확인할 수 있습니다:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# 저장 위치 변경 (참고용)

방법 1:  
소프트 링크 생성 방식으로 구현 가능합니다. 소프트웨어를 종료한 후 데이터를 원하는 위치로 이동하고, 원본 위치에 이동한 위치를 가리키는 링크를 생성하세요.

구체적인 단계는 다음 참고:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

방법 2:  
Electron 애플리케이션 특성을 활용한 시작 매개변수 구성으로 저장 위치 변경.

> --user-data-dir  
> 예시: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Example:

```shell
PS D:\CherryStudio> dir

    디렉터리: D:\CherryStudio

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (인코딩: ANSI)

```bash
@title CherryStudio 초기화
@echo off

set current_path_dir=%~dp0
@echo 현재 경로:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio 데이터 경로:%user_data_dir%

@echo 현재 경로에서 Cherry-Studio-*-portable.exe 파일 찾기
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #실제 다운로드된 파일명으로 변경하세요. 공식 홈페이지와 Github 다운로드 파일명 상이
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo 파일 발견: %target_file%
) else (
    echo 일치하는 파일 없음, 스크립트 종료
    pause
    exit
)

@echo 확인 후 계속 진행
pause

@echo CherryStudio 시작
start %target_file% --user-data-dir="%user_data_dir%"

@echo 작업 완료
@echo on
exit
```

> user-data-dir 디렉터리 초기화 후 구조:

```shell
PS D:\CherryStudio> dir .\user-data-dir\

    디렉터리: D:\CherryStudio\user-data-dir

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