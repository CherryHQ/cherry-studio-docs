---
icon: floppy-disk
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ডিফল্ট স্টোরেজ অবস্থান

Cherry Studio ডেটা স্টোরেজ সিস্টেম স্ট্যান্ডার্ড অনুসরণ করে, ডেটা স্বয়ংক্রিয়ভাবে ব্যবহারকারীর ডিরেক্টরিতে সংরক্ষিত হয়। নির্দিষ্ট ডিরেক্টরি অবস্থান নিম্নরূপ:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

আপনি নিম্নলিখিত স্থানে দেখতে পারেন:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# স্টোরেজ অবস্থান পরিবর্তন (রেফারেন্সের জন্য)

**পদ্ধতি ১:**

সিমলিংক তৈরি করে এটা করা যাবে। সফটওয়্যারটি বন্ধ করুন, ডেটা আপনার পছন্দসই স্থানে নিয়ে যান, তারপর মূল অবস্থানে একটি লিঙ্ক তৈরি করুন যা নতুন অবস্থানের দিকে নির্দেশ করে।

নির্দিষ্ট ধাপগুলি এই লিঙ্কে দেখা যাবে: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**পদ্ধতি ২:**
ইলেক্ট্রন অ্যাপ্লিকেশনের বৈশিষ্ট্য ব্যবহার করে, স্টার্টআপ প্যারামিটার কনফিগার করে স্টোরেজ অবস্থান পরিবর্তন করুন।

> --user-data-dir
> উদাহরণ: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> উদাহরণ:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (এনকোডিং: ANSI)

```bash
@title CherryStudio ইনিশিয়ালাইজেশন
@echo off

set current_path_dir=%~dp0
@echo বর্তমান পাথ:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio ডেটা পাথ:%user_data_dir%

@echo বর্তমান পাথে Cherry-Studio-*-portable.exe খুঁজুন
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #নাম পরিবর্তন করুন (অফিসিয়াল ওয়েবসাইট এবং GitHub এর নাম আলাদা)
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo ফাইল পাওয়া গেছে: %target_file%
) else (
    echo কোন ম্যাচিং ফাইল পাওয়া যায়নি, স্ক্রিপ্ট বন্ধ হচ্ছে
    pause
    exit
)

@echo নিশ্চিত করতে চালিয়ে যান
pause

@echo CherryStudio চালু হচ্ছে
start %target_file% --user-data-dir="%user_data_dir%"

@echo অপারেশন সম্পন্ন হয়েছে
@echo on
exit
```

> ডিরেক্টরি user-data-dir ইন্সটলের পরের স্ট্রাকচার:

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