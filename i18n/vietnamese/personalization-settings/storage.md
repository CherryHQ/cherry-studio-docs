---
icon: floppy-disk
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Vị Trí Lưu Trữ Mặc Định

Cherry Studio tuân thủ quy chuẩn hệ thống khi lưu trữ dữ liệu, dữ liệu sẽ tự động được lưu vào thư mục người dùng với các vị trí cụ thể như sau:

> macOS: /Users/username/Library/Application Support/CherryStudioDev
>
> Windows: C:\Users\username\AppData\Roaming\CherryStudio
>
> Linux: /home/username/.config/CherryStudio

Bạn cũng có thể xem tại vị trí sau:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# Thay Đổi Vị Trí Lưu Trữ (Tham Khảo)

**Phương Pháp 1:**

Bạn có thể sử dụng symbolic link để thực hiện việc này. Hãy thoát ứng dụng, di chuyển dữ liệu đến vị trí mong muốn, sau đó tạo một liên kết tại vị trí gốc trỏ đến vị trí mới.

Các bước thực hiện chi tiết tham khảo: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**Phương Pháp 2:**
Dựa trên đặc điểm ứng dụng Electron, sử dụng tham số khởi động để thay đổi vị trí lưu trữ.

> --user-data-dir
> Ví dụ: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Ví dụ:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (mã hóa: ANSI)

```bash
@title Khởi tạo CherryStudio
@echo off

set current_path_dir=%~dp0
@echo Đường dẫn hiện tại:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo Đường dẫn dữ liệu CherryStudio:%user_data_dir%

@echo Tìm Cherry-Studio-*-portable.exe trong đường dẫn hiện tại
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #Script này phù hợp với phiên bản tải từ GitHub và trang chủ, với các phiên bản khác vui lòng tự sửa đổi
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Tìm thấy file: %target_file%
) else (
    echo Không tìm thấy file phù hợp, thoát script
    pause
    exit
)

@echo Xác nhận tiếp tục
pause

@echo Khởi động CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Hoàn tất thao tác
@echo on
exit
```

> Cấu trúc thư mục user-data-dir sau khi khởi tạo:

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