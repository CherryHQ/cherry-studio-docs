---
icon: floppy-disk
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# डिफ़ॉल्ट संग्रहण स्थान

Cherry Studio डेटा संग्रहण सिस्टम मानकों का पालन करता है। डेटा स्वचालित रूप से उपयोगकर्ता डायरेक्टरी में संग्रहीत किया जाता है। विशिष्ट डायरेक्टरी स्थान निम्नलिखित हैं:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

निम्नलिखित स्थान पर भी देखा जा सकता है:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# संग्रहण स्थान बदलना (संदर्भ के लिए)

**विधि 1:**

सॉफ्ट लिंक बनाकर इसे प्राप्त किया जा सकता है। सॉफ़्टवेयर बंद करें, डेटा को वांछित स्थान पर स्थानांतरित करें, फिर मूल स्थान पर नए स्थान की ओर इंगित करने वाला लिंक बनाएँ।

विस्तृत चरणों के लिए देखें: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**विधि 2:**
इलेक्ट्रॉन एप्लिकेशन की विशेषताओं का उपयोग करते हुए, स्टार्टअप पैरामीटर कॉन्फ़िगर करके संग्रहण स्थान बदलें।

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

> init_cherry_studio.bat (एन्कोडिंग: ANSI)

```bash
@title CherryStudio आरंभीकरण
@echo off

set current_path_dir=%~dp0
@echo वर्तमान पथ:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio डेटा पथ:%user_data_dir%

@echo वर्तमान पथ में Cherry-Studio-*-portable.exe खोजें
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #यह कोड GitHub और आधिकारिक वेबसाइट डाउनलोड के लिए अनुकूलित है, अन्य के लिए स्वयं संशोधित करें
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo फ़ाइल मिली: %target_file%
) else (
    echo कोई मिलान फ़ाइल नहीं मिली, स्क्रिप्ट से बाहर निकलना
    pause
    exit
)

@echo पुष्टि करने के लिए जारी रखें
pause

@echo CherryStudio प्रारंभ करें
start %target_file% --user-data-dir="%user_data_dir%"

@echo प्रक्रिया पूर्ण
@echo on
exit
```

> user-data-dir डायरेक्टरी प्रारंभ होने के बाद संरचना:

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