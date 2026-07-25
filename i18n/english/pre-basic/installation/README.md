---
icon: desktop-arrow-down
---

# Installation Guide

This page explains the general Cherry Studio installation process and directs you to detailed instructions for each operating system. If you do not have an installation package yet, start with [Client Downloads](../../cherrystudio/download.md).

## Before installation

1. Make sure the installation package came from the Cherry Studio website or the official `CherryHQ/cherry-studio` GitHub Releases.
2. Check the operating system and CPU architecture to avoid mixing x64, ARM64, amd64, or aarch64 packages.
3. Quit any running instance of Cherry Studio.
4. Before upgrading, downgrading, or testing a preview release, create a backup under **Settings → Data Settings**.

{% hint style="warning" %}
Do not downgrade from a new version to an older version without a backup. A new version may have migrated the local database or configuration, and the older version may not be able to read the migrated data.
{% endhint %}

## Windows

Windows provides installer and portable versions:

* **Setup installer**: Follow the wizard to choose a directory and complete installation. Recommended for most users.
* **Portable version**: Run the executable directly. Suitable for temporary use or when you do not want to run an installation process.

Cherry Studio does not support Windows 7. If a system protection prompt appears on first launch, verify the package source and file digest before following the [Windows Installation Guide](windows.md).

## macOS

1. Download the `.dmg` that matches your chip: choose `arm64` for an Apple chip and `x64` for an Intel chip.
2. Open the DMG and drag Cherry Studio into Applications.
3. Launch it from Applications.

macOS may display developer-verification or security prompts on first launch. See the [macOS Installation Guide](macos.md) for instructions.

## Linux

Linux releases usually provide AppImage, deb, and rpm formats. Choose one format; do not install several formats for the same application.

### AppImage

```bash
chmod +x ./Cherry-Studio-*.AppImage
./Cherry-Studio-*.AppImage
```

AppImage does not require system-wide installation. If it does not start, first make sure the file architecture is correct. Some distributions also require a FUSE compatibility component for AppImage.

### Debian / Ubuntu

```bash
sudo apt install ./Cherry-Studio-*-amd64.deb
```

An ARM64 device should use a deb package with `arm64` in its filename.

### Fedora / RHEL / Rocky Linux

```bash
sudo dnf install ./Cherry-Studio-*.rpm
```

Choose an `x86_64` or `aarch64` package for the device.

## Upgrade

When you install a newer stable version on the same operating system and architecture, local data is usually retained. To reduce risk:

1. Complete a local or remote backup.
2. Completely quit Cherry Studio.
3. Upgrade with a new installation package that matches the current system and architecture.
4. After launch, confirm that Model Services, Chat, Knowledge Base, and Agents work correctly.

A pre-release or daily preview build may contain data migrations that are not yet stable. Do not keep the only copy of important data in a preview environment.

## After installation

After the first launch, complete these steps in order:

1. Add providers and models under **Settings → Model Services**.
2. Return to Chat and send a test message.
3. Confirm the data-storage and backup locations.
4. Enable Knowledge Base, Agents, MCP, or other advanced capabilities as needed.

Continue reading:

* [Configure Model Services](../../pre-basic/providers/)
* [Chat](../../cherrystudio/preview/chat.md)
* [Data Settings](../../data-settings/)
* [Frequently Asked Questions](../../question-contact/questions.md)
