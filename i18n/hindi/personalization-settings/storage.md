---
icon: floppy-disk
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# डिफ़ॉल्ट स्टोरेज स्थान

Cherry Studio डेटा भंडारण सिस्टम मानकों का पालन करता है। डेटा स्वचालित रूप से उपयोगकर्ता निर्देशिका के अंतर्गत संग्रहीत किया जाता है, विशिष्ट स्थान निम्नलिखित हैं:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

इसे निम्न स्थान पर भी देखा जा सकता है:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# स्टोरेज स्थान बदलना (संदर्भ हेतु)

विधि १:

सॉफ्ट लिंक बनाकर इसे कार्यान्वित किया जा सकता है। सॉफ्टवेयर को बंद करें, डेटा को अपनी इच्छित स्थान पर स्थानांतरित करें, फिर मूल स्थान पर एक लिंक बनाएं जो नए स्थान की ओर संकेत करे।

विस्तृत चरणों के लिए देखें: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

विधि २:
इलेक्ट्रॉन एप्लिकेशन की विशेषताओं के आधार पर, स्टोरेज स्थान को लॉन्च पैरामीटर कॉन्फ़िगर करके संशोधित किया जा सकता है।

> --user-data-dir
> उदाहरण: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> उदाहरण:

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
@title CherryStudio इनिशियलाइजेशन
@echo off

set current_path_dir=%~dp0
@echo वर्तमान पथ:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio डेटा पथ:%user_data_dir%

@echo वर्तमान पथ में Cherry-Studio-*-portable.exe खोजें
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #कृपया वास्तविक डाउनलोड की गई फ़ाइल का नाम डालें, आधिकारिक साइट और GitHub डाउनलोड के नाम भिन्न होते हैं
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo फ़ाइल मिली: %target_file%
) else (
    echo मेल खाने वाली कोई फ़ाइल नहीं मिली, स्क्रिप्ट बंद करें
    pause
    exit
)

@echo जारी रखने के लिए कन्फर्म करें
pause

@echo CherryStudio लॉन्च करें
start %target_file% --user-data-dir="%user_data_dir%"

@echo ऑपरेशन समाप्त
@echo on
exit
```

> निर्देशिका user-data-dir की इनिशियलाइजेशन के बाद संरचना:

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