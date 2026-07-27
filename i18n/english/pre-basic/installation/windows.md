---
description: Choose, install, and update Cherry Studio on Windows
icon: windows
---

# Windows

This page explains how to choose the right Windows package, install Cherry Studio, and handle common security prompts or runtime issues during the first launch. If you have not downloaded an installer yet, go to [Download the app](../../cherrystudio/download.md) first.

{% hint style="warning" %}
Cherry Studio does not support Windows 7. Download packages only from the Cherry Studio website or the official `CherryHQ/cherry-studio` GitHub Releases page.
{% endhint %}

## Choose a package

Windows releases provide x64 and ARM64 builds in both Setup and Portable formats.

| Package | Best for |
| --- | --- |
| `x64-setup.exe` | Most Windows PCs with an Intel or AMD processor; recommended for most users |
| `arm64-setup.exe` | Windows PCs with an ARM processor, including some Snapdragon devices |
| `x64-portable.exe` | x64 PCs; no installation, with the app and its data in a directory you choose |
| `arm64-portable.exe` | ARM64 PCs; no installation, with the app and its data in a directory you choose |

If you are unsure which architecture your PC uses, open **Settings → System → About** and check “System type”:

* Choose x64 if it shows “x64-based processor.”
* Choose ARM64 if it shows “ARM-based processor.”

The Setup package is best for everyday use. The Portable package is better suited to temporary testing, use on a USB drive, or keeping data in a separate directory.

## Verify the downloaded file

Official GitHub Releases include a SHA256 hash for each package. After the download finishes, run this command in PowerShell:

```powershell
Get-FileHash ".\Cherry-Studio-*-setup.exe" -Algorithm SHA256
```

For a Portable package, change the file name to the matching `*-portable.exe`. The output must exactly match the SHA256 value shown on the Release page.

If your browser or Windows reports that the file has an unknown source, verify the download domain, file name, and SHA256 first. Do not run the file if you cannot confirm its source.

## Install the Setup package

1. Fully quit any running Cherry Studio process.
2. Double-click `*-setup.exe`.
3. Choose an installation directory in the setup wizard.
4. Confirm the options and complete the installation.
5. Start Cherry Studio from the desktop shortcut or Start menu.

To upgrade an existing installation, run the newer Setup package for the same system architecture. Before upgrading, create a backup under **Settings → Data Settings**.

## Use the Portable package

1. Create a writable directory, such as `D:\Apps\CherryStudio`.
2. Place `*-portable.exe` in that directory.
3. Double-click the executable to start it.
4. Do not move the executable or its data directory while the app is running.

Unless you choose a different data location, the Portable package stores application data in a `data` directory next to the executable. Keep both the executable and this directory when backing up or moving the Portable version.

{% hint style="info" %}
Do not place the Portable package in a directory that requires administrator permission to write. For long-term use, automatic shortcut creation, and upgrades through the setup wizard, use the Setup package instead.
{% endhint %}

## First launch

After the first launch, complete these checks:

1. Open **Settings → Model Services**, add a provider, and enable at least one model.
2. Return to the chat page and send a test message.
3. Open **Settings → Data Settings** and confirm the backup method and data location.

If Windows Defender SmartScreen displays a protection warning, first confirm that the file came from an official source and passed SHA256 verification. Then follow the system prompt to view more information. Do not disable Windows security features for an installer from an unknown source.

## Visual C++ runtime

Some native Cherry Studio components depend on Microsoft Visual C++ Redistributable. If Windows reports a missing runtime during installation or launch:

1. First, allow the Cherry Studio installer to install the required dependencies.
2. If automatic installation fails, go to the [official Microsoft Visual C++ Redistributable page](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist).
3. Download the x64 or ARM64 version that matches your system, install it, and restart Cherry Studio.

Do not download the runtime from a third-party software site.

## Update or switch versions

Before updating:

1. Create a backup under **Settings → Data Settings**.
2. Fully quit Cherry Studio.
3. Download a new package that matches your PC architecture.

Setup users can run the new installer directly. Portable users should keep the existing `data` directory and replace the old executable with the new one.

Downgrading from a newer version can cause database or configuration incompatibilities. Do not downgrade unless you have a backup and understand the impact. Pre-release or daily preview builds should not be the only environment that stores important data.

## Troubleshooting

### Nothing happens after double-clicking

Check the following in order:

1. Make sure the package architecture matches your system.
2. Make sure the file is complete and its SHA256 matches.
3. Confirm that Visual C++ Redistributable is installed correctly.
4. Check whether security software quarantined the application files.
5. Check whether a Cherry Studio process is already running.

If Cherry Studio still does not start, record your Windows version, system architecture, Cherry Studio version, and the error message, then submit them through [Feedback and suggestions](../../question-contact/suggestions.md).

### Portable starts as a fresh installation

Check that the `data` directory is still next to the executable, that the current directory is writable, and that the executable was not moved. Copy the existing directory before attempting a restore so you do not overwrite usable data.

### What to do after installation

Continue with:

* [Configure model services](../../pre-basic/providers/)
* [Chat interface](../../cherrystudio/preview/chat.md)
* [Data settings](../../data-settings/)
