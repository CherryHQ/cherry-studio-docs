---
icon: floppy-disk
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# ตำแหน่งที่เก็บข้อมูลเริ่มต้น

Cherry Studio จัดเก็บข้อมูลตามมาตรฐานระบบ โดยข้อมูลจะถูกเก็บไว้ในไดเรกทอรีผู้ใช้โดยอัตโนมัติ โดยมีตำแหน่งไดเรกทอรี่ดังนี้:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

คุณยังสามารถดูได้ที่:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# การเปลี่ยนตำแหน่งที่เก็บข้อมูล (อ้างอิง)

**วิธีที่ 1:**

สามารถทำได้โดยการสร้าง symbolic link ออกจากซอฟต์แวร์ ย้ายข้อมูลไปยังตำแหน่งที่ต้องการ จากนั้นสร้างลิงก์ในตำแหน่งเดิมที่ชี้ไปยังตำแหน่งใหม่

ขั้นตอนการดำเนินการสามารถดูได้ที่: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**วิธีที่ 2:**
ใช้คุณสมบัติของแอปพลิเคชัน Electron โดยกำหนดพารามิเตอร์การเริ่มทำงานเพื่อเปลี่ยนตำแหน่งเก็บข้อมูล

> --user-data-dir
> เช่น: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> ตัวอย่าง:

```shell
PS D:\CherryStudio> dir


    ไดเรกทอรี: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (รูปแบบตัวอักษร: ANSI)

```bash
@title เริ่มต้น CherryStudio
@echo off

set current_path_dir=%~dp0
@echo เส้นทางปัจจุบัน:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo เส้นทางข้อมูล CherryStudio:%user_data_dir%

@echo ค้นหาไฟล์ Cherry-Studio-*-portable.exe ในเส้นทางปัจจุบัน
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # รหัสนี้เข้ากันกับเวอร์ชันจาก GitHub และเว็บไซต์หลัก สำหรับเวอร์ชันอื่น ๆ โปรดปรับเปลี่ยนด้วยตนเอง
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo พบไฟล์: %target_file%
) else (
    echo ไม่พบไฟล์ที่ตรงกัน กำลังปิดสคริปต์
    pause
    exit
)

@echo ยืนยันเพื่อดำเนินการต่อ
pause

@echo เริ่มต้น CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo การดำเนินการเสร็จสิ้น
@echo on
exit
```

> โครงสร้างไดเรกทอรี user-data-dir หลังเริ่มต้น:

```shell
PS D:\CherryStudio> dir .\user-data-dir\


    ไดเรกทอรี: D:\CherryStudio\user-data-dir


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