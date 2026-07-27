---
description: Choose, install, and update Cherry Studio on macOS
icon: apple
---

# macOS

This page explains how to choose the right package for an Intel or Apple silicon Mac, install Cherry Studio, and handle macOS security prompts during the first launch. If you have not downloaded an installer yet, go to [Download the app](../../cherrystudio/download.md) first.

## Check the chip type

1. Click the Apple menu  in the upper-left corner of the screen.
2. Select **About This Mac**.
3. Check “Chip” or “Processor.”

| Your Mac shows | Download architecture |
| --- | --- |
| Apple M-series chip | `arm64` |
| Intel processor | `x64` |

On an Apple silicon Mac, use the native arm64 package when possible. If you download the x64 package by mistake, macOS may ask you to install Rosetta; downloading the arm64 package instead is usually the better choice.

## Choose DMG or ZIP

macOS releases usually include both `.dmg` and `.zip` packages:

| Format | How to use it | Recommendation |
| --- | --- | --- |
| DMG | Open the disk image and drag the app to Applications | Best for most users |
| ZIP | Extract the archive, then move the app to Applications | Use if the DMG cannot be mounted or for manual distribution |

Both formats contain the same app. You do not need to install both.

## Verify the downloaded file

Official GitHub Releases include a SHA256 hash for each package. Open Terminal and run:

```bash
shasum -a 256 ~/Downloads/Cherry-Studio-*.dmg
```

For a ZIP package, change the extension to `*.zip`. The output must exactly match the SHA256 value shown on the Release page.

If your browser or macOS reports that the file has an unknown source, verify the download domain, file name, and SHA256 first. Do not open the file if you cannot confirm its source.

## Install with a DMG

1. Double-click the downloaded `.dmg` file.
2. In the window that opens, drag Cherry Studio to the Applications folder.
3. Wait for the copy to finish.
4. Eject the Cherry Studio disk image from the Finder sidebar.
5. Open **Finder → Applications → Cherry Studio**.

Do not run the app from the DMG window for everyday use. Copy it to Applications before launching it so future updates and permission management work more reliably.

## Install from a ZIP

1. Double-click the `.zip` file to extract it.
2. Move the extracted Cherry Studio app to the Applications folder.
3. Start it from Applications.

If Applications already contains an older version, fully quit Cherry Studio and create a backup under **Settings → Data Settings** before updating.

## Handle the first-launch security prompt

macOS runs a Gatekeeper check the first time you open an app downloaded from the internet.

If macOS only asks whether you are sure you want to open the app, confirm its name and download source, then choose Open. If it says the developer cannot be verified or the app cannot be checked for malicious software:

1. Confirm that the file came from the Cherry Studio website or the official GitHub Releases page.
2. Verify the SHA256.
3. Try to open the app once so macOS records the block.
4. Open **System Settings → Privacy & Security**.
5. Find the corresponding message in the Security section and select **Open Anyway**.
6. Authenticate when prompted, then confirm that you want to open the app.

{% hint style="warning" %}
Do not disable Gatekeeper or use Open Anyway for a file from an unknown source or with a mismatched SHA256. If macOS explicitly says the app will damage your computer or contains malware, delete the file and download it again from an official source.
{% endhint %}

For Apple's latest instructions, see [Safely open apps on your Mac](https://support.apple.com/102445).

## Grant system permissions

Cherry Studio requests permissions only when a related feature needs them. For example:

* Microphone permission when you use voice or audio features.
* Camera permission when you use camera-related features.
* Documents or Downloads folder permission when reading or saving files.

Grant only the permissions required by the feature you are using. To change them later, go to **System Settings → Privacy & Security** and adjust Cherry Studio under the relevant permission category.

## Update Cherry Studio

Before updating:

1. Create a backup under **Settings → Data Settings**.
2. Fully quit Cherry Studio.
3. Download the new version that matches your Mac chip.

Then open the new DMG or extract the ZIP, move the new Cherry Studio app to Applications, and choose Replace when macOS asks. After launching the new version for the first time, confirm that model services, chats, knowledge bases, and agents work normally.

Downgrading from a newer version can cause database or configuration incompatibilities. Do not downgrade unless you have a backup and understand the impact.

## Troubleshooting

### The app does not open

Check the following in order:

1. Make sure the package architecture matches your Mac chip.
2. Make sure the file is complete and its SHA256 matches.
3. Confirm that the app has been moved to Applications.
4. Check **System Settings → Privacy & Security** for a corresponding block message.
5. Check whether a Cherry Studio process is already running.

### macOS says the app is damaged

Delete the current file, then download it again from an official source and verify its SHA256. Do not copy commands from the internet to remove security attributes. If the file is actually damaged or has been tampered with, those commands bypass system protection.

### The app quits immediately after opening

Record your macOS version, chip type, Cherry Studio version, and the complete error message, then submit them through [Feedback and suggestions](../../question-contact/suggestions.md). If you are using a pre-release version, also include its build date or download source.

### What to do after installation

Continue with:

* [Configure model services](../../pre-basic/providers/)
* [Chat interface](../../cherrystudio/preview/chat.md)
* [Data settings](../../data-settings/)
