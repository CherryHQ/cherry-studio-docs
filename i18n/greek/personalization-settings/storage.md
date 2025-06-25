---
icon: floppy-disk
---

# Αλλαγή θέσης αποθήκευσης

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

## Προεπιλεγμένη θέση αποθήκευσης

Το Cherry Studio ακολουθεί τα πρότυπα του συστήματος για την αποθήκευση δεδομένων. Τα δεδομένα αποθηκεύονται αυτόματα στον κατάλογο χρήστη. Οι συγκεκριμένες τοποθεσίες καταλόγων είναι:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

Μπορείτε επίσης να δείτε την τοποθεσία εδώ:

<figure><img src="../../.gitbook/assets/image%20(31).png" alt=""><figcaption></figcaption></figure>

## Αλλαγή θέσης αποθήκευσης (για αναφορά)

Μέθοδος 1:

Μπορείτε να δημιουργήσετε μια συμβολική σύνδεση. Κλείστε την εφαρμογή, μετακινήστε τα δεδομένα στη θέση που επιθυμείτε και στη συνέχεια δημιουργήστε έναν συμβολικό σύνδεσμο στην αρχική τοποθεσία που δείχνει στη νέα τοποθεσία.

Για λεπτομερείς οδηγίες, ανατρέξτε: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Μέθοδος 2:\
Χρησιμοποιώντας χαρακτηριστικά εφαρμογών Electron, τροποποιήστε τη θέση αποθήκευσης ρυθμίζοντας παραμέτρους εκκίνησης.

> \--user-data-dir\
> Πχ: Cherry-Studio-\*-x64-portable.exe --user-data-dir="%user\_data\_dir%"

> Παράδειγμα:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init\_cherry\_studio.bat (κωδικοποίηση: ANSI)

```bash
@title Αρχικοποίηση CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Τρέχων διαδρομή:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Διαδρομή δεδομένων CherryStudio:%user_data_dir%

@echo Εύρεση Cherry-Studio-*-portable.exe στην τρέχουσα διαδρομή
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #Αυτός ο κώδικας είναι προσαρμοσμένος για εκδόσεις από GitHub και την επίσημη ιστοσελίδα. Για άλλες εκδόσεις, τροποποιήστε ανάλογα
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Βρέθηκε αρχείο: %target_file%
) else (
    echo Δεν βρέθηκε αρχείο, κλείσιμο σεναρίου
    pause
    exit
)

@echo Πατήστε οποιοδήποτε πλήκτρο για συνέχεια
pause

@echo Εκκίνηση CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Η λειτουργία ολοκληρώθηκε
@echo on
exit
```

> Δομή καταλόγου user-data-dir μετά την αρχικοποίηση:

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
