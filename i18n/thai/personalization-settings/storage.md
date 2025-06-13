---
icon: floppy-disk
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# ตำแหน่งเก็บข้อมูลเริ่มต้น

การจัดเก็บข้อมูล Cherry Studio เป็นไปตามข้อกำหนดของระบบ ข้อมูลจะถูกวางไว้ในไดเรกทอรีผู้ใช้โดยอัตโนมัติ ตำแหน่งไดเรกทอรีมีดังนี้:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

ยังสามารถดูได้ที่ตำแหน่งต่อไปนี้:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# เปลี่ยนตำแหน่งจัดเก็บข้อมูล (สำหรับอ้างอิง)

**วิธีที่ 1:**

สามารถทำได้โดยการสร้าง symbolic link ออกจากซอฟต์แวร์ ย้ายข้อมูลไปยังตำแหน่งที่ต้องการ แล้วสร้างลิงก์ที่ตำแหน่งเดิมชี้ไปยังตำแหน่งใหม่

ขั้นตอนการทำงานโดยละเอียดสามารถดูได้ที่:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**วิธีที่ 2:**
ใช้คุณสมบัติของแอปพลิเคชัน Electron โดยการกำหนดพารามิเตอร์เริ่มต้นเพื่อเปลี่ยนตำแหน่งจัดเก็บ

> --user-data-dir
> ตัวอย่าง: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> ตัวอย่าง:

```shell
PS D:\CherryStudio> dir


    Directory: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (encoding: ANSI)

```bash
@title เริ่มต้น CherryStudio
@echo off

set current_path_dir=%~dp0
@echo PATH ปัจจุบัน:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo PATH ข้อมูลของ CherryStudio:%user_data_dir%

@echo กำลังค้นหา Cherry-Studio-*-portable.exe ใน PATH ปัจจุบัน
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #โปรดเปลี่ยนเป็นชื่อไฟล์ที่ดาวน์โหลดได้จริง ชื่อที่ดาวน์โหลดจากเว็บไซต์ทางการและ Github มีความแตกต่าง
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo พบไฟล์: %target_file%
) else (
    echo ไม่พบไฟล์ที่ตรงกัน ออกจากสคริปต์นี้
    pause
    exit
)

@echo ยืนยันเพื่อดำเนินการต่อ
pause

@echo กำลังเริ่ม CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo การดำเนินการสิ้นสุด
@echo on
exit
```

> โครงสร้างไดเรกทอรี user-data-dir หลังการเริ่มต้น:

```shell
PS D:\CherryStudio> dir .\user-data-dir\


    Directory: D:\CherryStudio\user-data-dir


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