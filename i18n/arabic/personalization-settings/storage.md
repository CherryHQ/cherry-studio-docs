---
icon: floppy-disk
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# الموقع التخزين الافتراضي

يتبع تخزين بيانات Cherry Studio مواصفات النظام، حيث يتم وضع البيانات تلقائيًا في دليل المستخدم. مواقع الدلائل المحددة كما يلي:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

يمكن أيضًا الاطلاع عليها في الموقع التالي:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# تغيير موقع التخزين (للإشارة)

الطريقة الأولى:

يمكن تحقيق ذلك عن طريق إنشاء وصلة لينة. أغلق البرنامج، ثم انقل البيانات إلى الموقع الذي ترغب في حفظها فيه، ثم أنشئ وصلة في الموقع الأصلي تشير إلى الموقع الجديد.

يمكنك الرجوع إلى الخطوات التفصيلية هنا: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

الطريقة الثانية:
بناءً على خصائص تطبيق Electron، يمكن تعديل موقع التخزين عبر تكوين معلمات بدء التشغيل.

> --user-data-dir
> مثال: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> مثال:

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
@title تهيئة CherryStudio
@echo off

set current_path_dir=%~dp0
@echo المسار الحالي: %current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo مسار بيانات CherryStudio: %user_data_dir%

@echo البحث عن Cherry-Studio-*-portable.exe في المسار الحالي
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # هذا الكود متوافق مع الإصدارات التي تم تنزيلها من GitHub والموقع الرسمي، يرجى تعديل الإصدارات الأخرى يدويًا
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo تم العثور على الملف: %target_file%
) else (
    echo لم يتم العثور على ملف مطابق، الخروج من البرنامج النصي
    pause
    exit
)

@echo يرجى التأكيد للمتابعة
pause

@echo بدء تشغيل CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo انتهت العملية
@echo on
exit
```

> بنية دليل user-data-dir بعد التهيئة:

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