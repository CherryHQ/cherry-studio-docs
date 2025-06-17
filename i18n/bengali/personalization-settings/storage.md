---
icon: floppy-disk
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ডিফল্ট স্টোরেজ লোকেশন

Cherry Studio ডেটা স্টোরেজ সিস্টেমের স্পেসিফিকেশন মেনে চলে, ডেটা স্বয়ংক্রিয়ভাবে ইউজার ডিরেক্টরিতে সংরক্ষিত হবে। নির্দিষ্ট ডিরেক্টরি লোকেশন নিম্নরূপ:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

নিম্নলিখিত লোকেশনেও দেখা যেতে পারে:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# স্টোরেজ লোকেশন পরিবর্তন (রেফারেন্সের জন্য)

পদ্ধতি ১:

সফট লিঙ্ক তৈরি করে পরিবর্তন করা যেতে পারে। সফটওয়্যার বন্ধ করে ডেটাকে আপনার পছন্দসই লোকেশনে সরিয়ে নিন, তারপর মূল লোকেশনে একটি লিঙ্ক তৈরি করুন যা সরানো লোকেশনের দিকে নির্দেশ করে।

নির্দিষ্ট ধাপসমূহ এই লিঙ্কে দেখা যেতে পারে: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

পদ্ধতি ২:
ইলেক্ট্রন অ্যাপ্লিকেশনের বৈশিষ্ট্যের উপর ভিত্তি করে, স্টার্টআপ প্যারামিটার কনফিগার করে স্টোরেজ লোকেশন পরিবর্তন করা যেতে পারে।

> --user-data-dir
> যেমন: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

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
@title CherryStudio আন্তজালিক
@echo off

set current_path_dir=%~dp0
@echo বর্তমান পাথ:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio ডেটা পাথ:%user_data_dir%

@echo বর্তমান পাথে Cherry-Studio-*-portable.exe অনুসন্ধান করুন
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #এই কোডটি GitHub এবং অফিসিয়াল ওয়েবসাইটের সংস্করণের সাথে সঙ্গতিপূর্ণ, অন্যান্য ক্ষেত্রে নিজে পরিবর্তন করুন
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo ফাইল পাওয়া গেছে: %target_file%
) else (
    echo কোন ম্যাচিং ফাইল পাওয়া যায়নি, স্ক্রিপ্ট থেকে প্রস্থান
    pause
    exit
)

@echo নিশ্চিত করতে চালিয়ে যান
pause

@echo CherryStudio চালু করা হচ্ছে
start %target_file% --user-data-dir="%user_data_dir%"

@echo অপারেশন সম্পন্ন
@echo on
exit
```

> user-data-dir ডিরেক্টরি ইন্সটলেশনের পরের স্ট্রাকচার:

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